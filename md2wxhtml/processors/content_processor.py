import markdown
from premailer import transform
from bs4 import BeautifulSoup

from ..processors.themes import default, github, hammer, dark, blue, green, red

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
            text = li.get_text(strip=False)
            if '：' in text:
                before, after = text.split('：', 1)
                highlight_span = soup.new_tag("span")
                highlight_span["class"] = "list-highlight-span"
                highlight_span.string = before + '：'
                p.append(highlight_span)
                if after.strip():
                    p.append(after)
            else:
                p.string = text
            p["style"] = li.get("style", "")
            ul.insert_before(p)
        ul.decompose()
    for ol in soup.find_all("ol"):
        for idx, li in enumerate(ol.find_all("li", recursive=False), 1):
            p = soup.new_tag("p")
            p.string = f"{idx}. {li.get_text(strip=True)}"
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
        text_content = p.get_text(strip=True)
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
