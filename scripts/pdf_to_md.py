"""Convert PDF files to markdown.

Usage: uv run scripts/pdf_to_md.py <file.pdf> [<file.pdf> ...]

Writes a .md file next to each input PDF, with the same basename.
"""

import re
import sys
from pathlib import Path

import pymupdf4llm


def normalize(md_text: str) -> str:
    """Strip trailing whitespace and collapse blank lines (markdownlint
    MD009/MD012)."""
    md_text = re.sub(r"[ \t]+$", "", md_text, flags=re.MULTILINE)
    md_text = re.sub(r"\n{3,}", "\n\n", md_text)
    return md_text.strip() + "\n"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__.strip())
    for arg in sys.argv[1:]:
        pdf_path = Path(arg)
        md_path = pdf_path.with_suffix(".md")
        # use_ocr=False: OCR-ing pages that contain images (e.g. the DiEM25
        # logo) produces gibberish and can drop the page's real text layer.
        md_text = pymupdf4llm.to_markdown(pdf_path, use_ocr=False)
        md_path.write_text(normalize(md_text), encoding="utf-8")
        print(f"{pdf_path} -> {md_path}")


if __name__ == "__main__":
    main()
