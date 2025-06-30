from .markdown_parser import extract_code_blocks
from ..processors.content_processor import process_content
from ..processors.code_processor import process_code_block
from ..models.code_block import ConversionResult


# Main orchestrator for the conversion process
class WeChatConverter:
    def __init__(self, content_theme: str = "default", code_theme: str = "default"):
        self.content_theme = content_theme
        self.code_theme = code_theme

    def convert(self, markdown: str) -> ConversionResult:
        # 1. Extract code blocks
        clean_md, code_blocks, placeholder_map = extract_code_blocks(markdown)
        # 2. Process general content
        html_with_placeholders = process_content(clean_md, theme=self.content_theme)
        # 3. Process code blocks
        code_html_map = {}
        for cb in code_blocks:
            code_html_map[cb.placeholder] = process_code_block(cb, theme=self.code_theme)
        # 4. Merge components
        for placeholder, code_html in code_html_map.items():
            html_with_placeholders = html_with_placeholders.replace(placeholder, code_html)
        # 5. Final styling/cleanup (to be implemented)
        return ConversionResult(
            html=html_with_placeholders,
            code_blocks=code_html_map,
            success=True,
            errors=[],
            warnings=[]
        )
