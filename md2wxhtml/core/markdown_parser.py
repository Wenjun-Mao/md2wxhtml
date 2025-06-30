import re
from typing import List, Tuple
from ..models.code_block import CodeBlock
from ..utils.placeholder_manager import PlaceholderManager

def extract_code_blocks(markdown: str) -> Tuple[str, List[CodeBlock], dict]:
    """
    Extract fenced and indented code blocks from markdown.
    Replace them with unique placeholders.
    Return (clean_markdown, code_blocks, placeholder_map)
    """
    code_blocks = []
    placeholder_manager = PlaceholderManager()
    placeholder_map = {}

    # Fenced code blocks: ```lang\n...\n```
    fenced_pattern = re.compile(r'```(\w+)?\n([\s\S]*?)```', re.MULTILINE)
    def fenced_replacer(match):
        lang = match.group(1) or None
        content = match.group(2)
        code_block = CodeBlock(content=content, language=lang)
        placeholder = placeholder_manager.generate()
        code_block.placeholder = placeholder
        code_blocks.append(code_block)
        placeholder_map[placeholder] = code_block
        return placeholder
    clean_md = fenced_pattern.sub(fenced_replacer, markdown)

    # TODO: Add indented code block extraction if needed

    return clean_md, code_blocks, placeholder_map
