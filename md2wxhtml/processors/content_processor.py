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
    Convert <ul>/<ol>/<li> lists to <p> paragraphs with bullet/number prefixes for WeChat compatibility.
    For <ul>, highlight only the content before '：' if present, no vertical line.
    """
    soup = BeautifulSoup(html, "html.parser")
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li", recursive=False):
            p = soup.new_tag("p")
            p["class"] = "list-highlight"
            # Use decode_contents() to preserve links and formatting
            li_html = li.decode_contents()
            if '：' in li.get_text(strip=False):
                before, after = li.get_text(strip=False).split('：', 1)
                highlight_span = soup.new_tag("span")
                highlight_span["class"] = "list-highlight-span"
                highlight_span.string = before + '：'
                p.append(highlight_span)
                # Insert the rest of the HTML after the highlight
                # Find the index of '：' in the HTML and split there
                html_split = li_html.split('：', 1)
                if len(html_split) == 2 and html_split[1].strip():
                    # Append as NavigableString or parse as HTML fragment
                    after_html = BeautifulSoup(html_split[1], "html.parser")
                    for elem in after_html.contents:
                        p.append(elem)
            else:
                # No '：', just insert the HTML as-is
                p.append(BeautifulSoup(li_html, "html.parser"))
            p["style"] = li.get("style", "")
            ul.insert_before(p)
        ul.decompose()
    for ol in soup.find_all("ol"):
        for idx, li in enumerate(ol.find_all("li", recursive=False), 1):
            p = soup.new_tag("p")
            # Use decode_contents() to preserve links and formatting
            li_html = li.decode_contents()
            # p.append(f"{idx}. ")
            p.append(BeautifulSoup(li_html, "html.parser"))
            p["style"] = li.get("style", "")
            ol.insert_before(p)
        ol.decompose()
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
