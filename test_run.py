# Example usage and test for the new WeChatConverter
from md2wxhtml.core.converter import WeChatConverter

if __name__ == "__main__":
    sample_md = '''
# Sample Title

This is a paragraph.

```python
def hello():
    print("Hello, world!")
```

Another paragraph.
'''
    converter = WeChatConverter(content_theme="default", code_theme="default")
    html = converter.convert(sample_md)
    print(html)
