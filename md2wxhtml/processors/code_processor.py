import re

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.styles import get_style_by_name

from ..models.code_block import CodeBlock


def _select_lexer(language: str, code: str):
    """
    Select the appropriate lexer for the given language and code.
    """
    try:
        return get_lexer_by_name(language, stripall=True)
    except Exception:
        try:
            return guess_lexer(code)
        except Exception:
            from pygments.lexers.special import TextLexer
            return TextLexer(stripall=True)

def _get_background_color(theme: str) -> str:
    """
    Get the background color for the given Pygments theme.
    """
    try:
        style = get_style_by_name(theme)
        return getattr(style, 'background_color', '#272822') or '#272822'
    except Exception:
        return '#272822'

def _build_pre_code_style(background_color: str) -> (str, str):
    """
    Build inline styles for <pre> and <code> tags to ensure WeChat compatibility.
    """
    pre_style = (
        f"box-sizing: border-box;"
        f"border-width: 0px;"
        f"border-style: solid;"
        f"border-color: #e5e5e5;"
        f"font-family: -apple-system-font, BlinkMacSystemFont, 'Helvetica Neue', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei UI', 'Microsoft YaHei', Arial, sans-serif;"
        f"font-size: 14.4px;"
        f"margin: 10px 8px;"
        f"color: #c9d1d9;"
        f"background: {background_color};"
        f"text-align: left;"
        f"line-height: 1.5;"
        f"overflow-x: auto;"
        f"border-radius: 8px;"
        f"padding: 0px !important;"
    )
    code_style = (
        f"box-sizing: border-box;"
        f"border-width: 0px;"
        f"border-style: solid;"
        f"border-color: #e5e5e5;"
        f"font-family: Menlo, 'Operator Mono', Consolas, Monaco, monospace;"
        f"font-feature-settings: normal;"
        f"font-variation-settings: normal;"
        f"font-size: 12.96px;"
        f"display: -webkit-box;"
        f"padding: 0.5em 1em 1em;"
        f"overflow-x: auto;"
        f"text-indent: 0px;"
        f"text-align: left;"
        f"line-height: 1.75;"
        f"margin: 0px;"
        f"white-space: nowrap;"
    )
    return pre_style, code_style

def _replace_spaces_and_linebreaks(html: str) -> str:
    # Replace all spaces/tabs outside HTML tags with &nbsp;, and \n with <br />
    def replace_line(line):
        result = ''
        in_tag = False
        for char in line:
            if char == '<':
                in_tag = True
                result += char
            elif char == '>':
                in_tag = False
                result += char
            elif not in_tag and char == ' ':
                result += '&nbsp;'
            elif not in_tag and char == '\t':
                result += '&nbsp;' * 4
            else:
                result += char
        return result

    lines = html.split('\n')
    processed_lines = [replace_line(line) for line in lines]
    return '<br />'.join(processed_lines)

def _move_all_nbsp_outside_span(html: str) -> str:
    # Replace all whitespace-only spans with &nbsp; outside the span
    def repl(m):
        ws = m.group(2)
        nbsp_count = ws.count('&nbsp;') + ws.count(' ')
        return '&nbsp;' * nbsp_count
    # This regex matches any <span ...>   </span> or <span ...>&nbsp;&nbsp;</span>
    return re.sub(r'(<span[^>]*>)((?:\s|&nbsp;)+)</span>', repl, html)

def process_code_block(code_block: CodeBlock, theme: str = "monokai") -> str:
    """
    Convert a CodeBlock to WeChat-compatible styled HTML using <pre><code> structure,
    matching the working example for WeChat editor compatibility.
    """
    code = code_block.content
    language = code_block.language or "text"
    lexer = _select_lexer(language, code)
    background_color = _get_background_color(theme)
    pre_style, code_style = _build_pre_code_style(background_color)
    formatter = HtmlFormatter(style=theme, noclasses=True, nowrap=True)
    highlighted_code = highlight(code, lexer, formatter)
    # Remove outer <div class="highlight"><pre>...</pre></div> if present
    if highlighted_code.startswith('<div class="highlight"><pre>'):
        highlighted_code = highlighted_code[len('<div class="highlight"><pre>'):]
    if highlighted_code.endswith('</pre></div>'):
        highlighted_code = highlighted_code[:-len('</pre></div>')]
    highlighted_code = highlighted_code.strip()
    if highlighted_code.startswith('<pre'):
        pre_start = highlighted_code.find('>') + 1
        pre_end = highlighted_code.rfind('</pre>')
        highlighted_code = highlighted_code[pre_start:pre_end].strip()
    if highlighted_code.startswith('<code'):
        code_start = highlighted_code.find('>') + 1
        code_end = highlighted_code.rfind('</code>')
        highlighted_code = highlighted_code[code_start:code_end].strip()
    # Now replace spaces and linebreaks as in the working example
    highlighted_code = _replace_spaces_and_linebreaks(highlighted_code)
    highlighted_code = _move_all_nbsp_outside_span(highlighted_code)
    html = (
        f'<pre style="{pre_style}">'
        f'<code style="{code_style}">'
        f'{highlighted_code}'
        f'</code></pre>'
    )
    return html