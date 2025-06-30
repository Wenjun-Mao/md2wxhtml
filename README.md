# md2wxhtml

A tool to convert Markdown files into a format suitable for WeChat articles, handling general content and code blocks with syntax highlighting.

## Features

*   Converts Markdown to HTML.
*   Separates and processes code blocks for syntax highlighting and horizontal scrolling.
*   Merges processed content and code blocks into a single HTML document.

## Disclaimer

This project is an independent open-source tool and is not affiliated with, endorsed by, or officially connected to WeChat or Tencent.

## Installation

```bash
pip install md2wxhtml
```

## Usage

### Command-line Interface

```bash
md2wxhtml --input <input_file.md> --output <output_file.html>
```

### As a Python Library

```python
from md2wxhtml.core.converter import WeChatConverter

converter = WeChatConverter()
html_output = converter.convert("Your markdown content here.")
print(html_output)
```
