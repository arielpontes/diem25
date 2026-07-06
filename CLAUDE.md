# CLAUDE.md

## About this repo

A public repository for AI-assisted content creation for DiEM25, maintained
by a member of the movement's Bucharest Collective. Its main output is a set
of localized vision documents for DiEM25 Romania, drafted here so that
colleagues in the Bucharest Collective — and eventually collectives in other
Romanian cities or other countries — can read, discuss and adapt them. It
also holds reference documents from the DiEM25 website converted to markdown
for use as context.

Because the repo is public, everything in it (including this file) should be
written as if read by friends and opponents alike.

## Layout

- `romanian-vision/` — draft vision documents for DiEM25 Romania (see
  principles below).
- `downloads/` — reference documents: markdown files converted from
  diem25.org pages (each starts with a `<!-- Source: URL -->` comment) and
  from PDFs (converted with the script below), plus the original PDFs.
- `scripts/` — utility scripts.

## Principles for the `romanian-vision` documents

When writing or editing files in `romanian-vision/`, respect these
principles:

- **Follow the DiEM25 vision format.** A statement headline, a short intro
  that localizes the argument to Romania, bold-led vision bullets, then a
  "What we propose" section with concrete policy directions.
- **Concrete but high-level, and honest about it.** Name real policies, but
  leave detailed specifications to future democratic deliberation — and say
  so openly (each document carries a standard preamble to that effect).
- **Anchor every proposal in policy that already works.** Take inspiration
  from countries where workers have achieved more, and cite the actual law,
  directive or court ruling by name so readers can verify. Nothing should
  read as an experiment on Romania.
- **Stay empirical.** Drop concrete facts and numbers regularly — the more
  striking the better — but only verifiable ones, double-checked before
  publishing, with the important caveats kept (e.g. income inequality is not
  wealth inequality).
- **Redirect anti-EU sentiment toward its real target.** Romanian
  frustration with "Europe" is legitimate, but its cause is corporate
  extraction, not European integration. Always advocate reforming the EU,
  never leaving it.
- **Corporations are the adversary, never peoples.** Criticize foreign
  corporations hard; celebrate the workers of Western Europe and their
  victories as the standard Romanians deserve too.
- **Decentralist socialism, not state socialism.** Romanians carry the
  trauma of top-down, centralized state "socialism", and the documents must
  never evoke it. Favor the bottom-up, self-managed tradition: cooperatives,
  municipalism, participatory budgeting, citizens' assemblies, economic
  democracy. Apply subsidiarity — centralize only when pragmatic (since we
  inherit a centralized system), or when scale is genuinely required
  (EU-level taxes, the European Basic Dividend); err towards
  decentralization otherwise.
- **Fight at both levels.** Pair national/local policies with EU-level
  floors that protect them: the local tax and the European floor reinforce
  each other.
- **Tone: confident, declarative, sober.** Address misconceptions as
  misconceptions ("Romania is often imagined as...") rather than as quoted
  strawmen ("to those who say..."). Be combative toward corporations and
  militarism, never toward ordinary people, whatever their current views.
- **English first.** Documents stay in English until finalized; Romanian
  translation comes after.

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
