import re

import markdown
from bs4 import BeautifulSoup
from premailer import transform

from ..processors.themes import blue, dark, default, github, green, hammer, red

theme_map = {
    "default": default,
    "github": github,
    "hammer": hammer,
    "dark": dark,
    "blue": blue,
    "green": green,
    "red": red,
}

# General content processing
def process_content(clean_markdown: str, theme: str = "default") -> str:
    """
    Convert clean markdown (with placeholders) to WeChat-styled HTML.
    Applies the selected article theme and injects its CSS as inline styles (for WeChat compatibility).
    """
    html = markdown.markdown(clean_markdown, extensions=["tables", "fenced_code", "codehilite", "toc"])
    html = _auto_link_urls(html)
    theme_mod = theme_map.get(theme, default)
    if hasattr(theme_mod, "postprocess_html"):
        html = theme_mod.postprocess_html(html)
    html = _lists_to_paragraphs(html)
    html = _add_paragraph_spacing(html, margin_px=16)
    css = theme_mod.get_css() if hasattr(theme_mod, "get_css") else None
    # Wrap in container for theme selectors
    html = '<div class="wechat-content">' + html + '</div>'
    # Inline the CSS for WeChat compatibility (removes <style>, applies inline styles)
    if css:
        html = transform(html, css_text=css, keep_style_tags=False, remove_classes=False)
    return html

def _auto_link_urls(html: str) -> str:
    """
    Find standalone URLs in the HTML and convert them into clickable links.
    Skips URLs already inside <a> tags.
    """
    url_pattern = re.compile(
        r'((https?://|www\.)[^\s<>"\']+)', re.IGNORECASE
    )

    def replacer(match):
        url = match.group(1)
        href = url if url.startswith("http") else f"http://{url}"
        return f'<a href="{href}" style="color:#1d4ed8; border-bottom-color:#3b82f6">{url}</a>'

    soup = BeautifulSoup(html, "html.parser")
    for text in soup.find_all(string=True):
        if text.parent.name == "a":
            continue
        new_text = url_pattern.sub(replacer, text)
        if new_text != text:
            text.replace_with(BeautifulSoup(new_text, "html.parser"))
    return str(soup)

def _lists_to_paragraphs(html: str) -> str:
    """
    Convert <ul>/<ol>/<li> lists to <p> paragraphs for WeChat compatibility.
    Preserves nesting structure with indentation.
    For <ul>, highlight only the content before '：' if present, no vertical line.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    def process_list(list_element, indent_level=0):
        """Recursively process lists, maintaining nesting with indentation."""
        margin_left = indent_level * 20  # 20px per nesting level
        
        for li in list_element.find_all("li", recursive=False):
            p = soup.new_tag("p")
            if list_element.name == "ul":
                p["class"] = "list-highlight"
            
            # Add indentation for nested items
            base_style = li.get("style", "")
            if margin_left > 0:
                if base_style and not base_style.strip().endswith(";"):
                    base_style += ";"
                base_style += f"margin-left:{margin_left}px;"
            
            # Process nested lists first (recursively)
            nested_lists = li.find_all(["ul", "ol"], recursive=False)
            for nested in nested_lists:
                nested.extract()  # Remove from li temporarily
            
            # Get li content without nested lists
            li_html = li.decode_contents()
            
            # Handle the '：' highlighting logic for ul
            if list_element.name == "ul" and '：' in li.get_text(strip=False):
                before, after = li.get_text(strip=False).split('：', 1)
                highlight_span = soup.new_tag("span")
                highlight_span["class"] = "list-highlight-span"
                highlight_span.string = before + '：'
                p.append(highlight_span)
                
                html_split = li_html.split('：', 1)
                if len(html_split) == 2 and html_split[1].strip():
                    after_html = BeautifulSoup(html_split[1], "html.parser")
                    for elem in after_html.contents:
                        p.append(elem)
            else:
                # No '：' or ordered list, just insert the HTML as-is
                if li_html.strip():
                    p.append(BeautifulSoup(li_html, "html.parser"))
            
            p["style"] = base_style
            list_element.insert_before(p)
            
            # Process nested lists after creating the parent paragraph
            for nested in nested_lists:
                process_list(nested, indent_level + 1)
    
    # Process all top-level lists
    for list_element in soup.find_all(["ul", "ol"]):
        # Only process if this is a top-level list (not nested)
        if not list_element.find_parent(["ul", "ol"]):
            process_list(list_element, 0)
            list_element.decompose()
    
    return str(soup)

def _add_paragraph_spacing(html: str, margin_px: int = 16) -> str:
    """
    Add inline margin-bottom to all <p> tags for WeChat compatibility.
    Excludes paragraphs containing code block placeholders.
    """
    soup = BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p"):
        # Skip paragraphs that contain code block placeholders
        text_content = p.get_text(strip=False)
        if text_content.startswith("{{CODE_BLOCK_PLACEHOLDER_") and text_content.endswith("}}"):
            # Remove the <p> wrapper from code block placeholders
            p.replace_with(text_content)
            continue
            
        style = p.get("style", "")
        # Ensure margin-bottom is set (append or update)
        if "margin-bottom" not in style:
            if style and not style.strip().endswith(";"):
                style += ";"
            style += f"margin-bottom:{margin_px}px;"
        p["style"] = style
    return str(soup)
