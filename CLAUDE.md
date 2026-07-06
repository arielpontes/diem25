# CLAUDE.md

## About this repo

A playground for AI-assisted content creation for DiEM25 (the user is a
member of the movement's Bucharest Collective). It holds reference documents
from the DiEM25 website converted to markdown for use as context.

## Layout

- `downloads/` — reference documents: markdown files converted from
  diem25.org pages (each starts with a `<!-- Source: URL -->` comment) and
  from PDFs (converted with the script below), plus the original PDFs.
- `scripts/` — utility scripts.

## Tooling

- Python dependencies are managed with `uv` (`pyproject.toml` + `uv.lock`,
  venv in `.venv`). Add dependencies with `uv add`, run scripts with
  `uv run`.
- Convert PDFs to markdown with:

  ```sh
  uv run scripts/pdf_to_md.py <file.pdf> [<file.pdf> ...]
  ```

  It writes a `.md` file next to each input PDF. OCR is disabled on purpose:
  these PDFs have text layers, and OCR-ing pages with images produces
  gibberish and can drop real text.

## Conventions

- Markdown files must be markdownlint-compliant; the repo config is
  `.markdownlint.jsonc`, which disables rules that conflict with keeping the
  source documents' text verbatim.
- Converted documents are reference material — keep their text intact rather
  than editing it to satisfy lint rules.
