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
from md2wxhtml import WeChatConverter

converter = WeChatConverter(content_theme="blue", code_theme="monokai")
conversion_result = converter.convert("Your markdown content here.")
html_output = conversion_result.html
print(html_output)
```

## Available Themes

The `content_theme` argument accepts the following built-in theme names:

- `default`
- `blue`
- `dark`
- `github`
- `green`
- `hammer`
- `red`

The `code_theme` argument uses [Pygments](https://pygments.org/docs/styles/) styles for code highlighting. You can specify any valid Pygments style name (e.g., `monokai`, `default`, `friendly`, `colorful`, etc.) to adjust the appearance of code blocks.

You can specify these names when creating a `WeChatConverter` instance. For example:

```python
converter = WeChatConverter(content_theme="github", code_theme="monokai")
```
