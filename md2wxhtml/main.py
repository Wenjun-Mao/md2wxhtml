import argparse
from . import WeChatConverter

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to WeChat HTML.")
    parser.add_argument("--input", required=True, help="Input Markdown file path.")
    parser.add_argument("--output", required=True, help="Output HTML file path.")

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        converter = WeChatConverter()
        conversion_result = converter.convert(markdown_content)

        if conversion_result.success:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(conversion_result.html)
            print(f"Successfully converted '{args.input}' to '{args.output}'")
        else:
            print(f"Conversion failed for '{args.input}'. Errors: {conversion_result.errors}")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
