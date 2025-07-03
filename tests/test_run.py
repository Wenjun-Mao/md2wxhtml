import sys
from pathlib import Path
import os

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from md2wxhtml.core.converter import WeChatConverter

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = Path(__file__).parent

    with open(script_dir / "test.md", "r", encoding="utf-8") as f:
        sample_md = f.read()
    
    converter = WeChatConverter(content_theme="default", code_theme="default")
    result = converter.convert(sample_md)
    
    output_file = script_dir / "output.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.html)

    with open(script_dir / "expected_output.html", "r", encoding="utf-8") as f:
        expected_html = f.read()

    if result.html.strip() == expected_html.strip():
        print("Test passed!")
        # Clean up the generated output file
        os.remove(output_file)
        sys.exit(0)
    else:
        print("Test failed!")
        print(f"Output written to {output_file}")
        print("Please compare it with expected_output.html")
        sys.exit(1)
