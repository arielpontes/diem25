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

- `romania/` — documents for DiEM25 Romania: the draft vision documents in
  `romania/vision/` and local documents such as `romania/bucharest.md` (see
  principles below).
- `international/` — reference documents: markdown files converted from
  diem25.org pages (each starts with a `<!-- Source: URL -->` comment) and
  from PDFs (converted with the script below).
- `scripts/` — utility scripts.

## Principles for the `romania/` political documents

When writing or editing political documents anywhere under `romania/` —
the vision documents in `romania/vision/` as well as local documents such
as `romania/bucharest.md` — respect these principles:

- **Follow the DiEM25 vision format.** A statement headline, a short intro
  that localizes the argument to Romania, bold-led vision bullets, then a
  "What we propose" section with concrete policy directions.
- **Concrete but high-level, and honest about it.** Name real policies, but
  leave detailed specifications to future democratic deliberation — and say
  so openly (each document carries a standard preamble to that effect).
- **Match the document to the movement's stage.** Until DiEM25 Romania
  democratically adopts proposals of its own, anything meant for
  publication (like `romania/vision/summary.md`, written as a news
  article for diem25.org/ro) presents a direction and its European
  inspirations — "we are inspired by...", no "What we propose"
  sections — while the full vision documents remain internal discussion
  drafts. Frame the document's status positively, by what it is and what
  comes next, never with disclaimers about what it is not: defensive
  framing reads the same whether aimed at opponents or at anticipated
  internal criticism.
- **Anchor every proposal in policy that already works.** Take inspiration
  from countries where workers have achieved more, and cite the actual law,
  directive or court ruling by name so readers can verify. Nothing should
  read as an experiment on Romania.
- **Cite laws through lay-readable links.** When a foreign law or policy
  is named as inspiration, link its mention to an article from a
  trustworthy general-audience source (Reuters, The Guardian, Euronews,
  official EU or government press pages) that a lay reader can grasp in a
  few paragraphs; fall back to official or academic sources only when no
  such article exists. Before publishing, verify that every link loads
  and actually covers the law it is attached to.
- **Propose only what the office can do.** A document addressed to a level
  of government (a city, a sector, the national level) anchors every
  proposal in that level's actual legal competences, citing them — never
  promising from city hall what only parliament can deliver. Where the
  level in question lacks the power, say so and name the level that has it.
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
- **Win the sovereigntist working class without losing anyone else.** The
  strategic challenge is to win over part of the working-class electorate
  that currently votes "sovereigntist"/far-right, without alienating either
  progressive leftists or centrist liberals. Make the positive case for each
  policy on its merits and its legal pedigree; never add defensive
  disclaimers distancing the movement from authoritarian figures (Orbán and
  the like) just because they once used a similar instrument. That
  throat-clearing persuades no one, reads as tribal signaling to the very
  voters we need to win, and concedes the frame that the policy is suspect.
- **Public space is a commons.** Visual space, parks, lakeshores and
  squares belong to everyone. Commerce is welcome in them as a competitively
  tendered, revocable service to the people using the space (the kiosk
  model), never as an enclosure that prices them out (the terrace model) —
  and advertising must never colonize the view.
- **Entrepreneurs are allies.** Small businesses, the self-employed and
  people who build things are part of the "many", not the adversary. Be
  vocal about supporting entrepreneurship and cutting bureaucracy, anchored
  as always in European policy that already works; reserve hostility for
  corporate extraction, never for people who start businesses.
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
- **Lead with the four pillars.** The DiEM25 Romania elevator pitch is:
  participatory democracy, tax justice, sustainable development, peace
  through diplomacy. Published documents should be skimmable down to
  exactly these four — title, subtitle and section headings carry the
  pitch. On the fourth: "peace through diplomacy", not "non-alignment"
  (which reads as naive to the Romanian public) and not bare "peace"
  (which leaves hostile readers to fill in the method) — keep the word,
  supply the method. Local documents carry their own pillar list in the
  same style: clear, sober policy terms ("participatory democracy"), not
  invented slogans, which read as salesy.
- **Participatory democracy always comes first.** The movement's name is
  Democracy in Europe Movement 2025 for a reason: participatory democracy
  is priority number one at every level, national and local. In every
  document it leads — first in the pillar list, first among the sections.
- **Affordability is the master frame.** The central lesson of Zohran
  Mamdani's New York campaign: name the cost of living as the defining
  issue and make residents feel entitled to affordable essentials —
  transport, housing, energy, heat. Lead with affordability throughout;
  where a European city has already made an essential free (transport in
  Tallinn or Luxembourg), say so plainly — "affordable" is the floor,
  not the ceiling. But never force the frame onto an essential that is
  not actually expensive locally: a complaint that doesn't match lived
  experience reads as an imported cause. Prefer terms with genuine local
  momentum behind them (e.g. "urban mobility", which speaks to Bucharest's
  real bike activism, over "affordable transport", when transport is not
  a local pain point) — each pillar term should pull its own part of the
  coalition.
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
