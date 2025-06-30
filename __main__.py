import sys
from md2wxhtml.core.converter import WeChatConverter

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m wechat_converter_v2 <input_markdown_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    with open(input_path, 'r', encoding='utf-8') as f:
        markdown = f.read()
    converter = WeChatConverter()
    html = converter.convert(markdown)
    output_path = input_path.rsplit('.', 1)[0] + '.wechat.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Converted HTML written to {output_path}")

if __name__ == "__main__":
    main()
