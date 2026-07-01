---
name: human-docs-readability
description: Human-first editing standard for README.md files and user-facing Markdown docs. Use when Codex needs to rewrite, review, or gate public docs so humans see the value story first, links are easy to scan, modern GitHub Markdown components are used tastefully, and LLM or machine-readable audit details move into bottom collapsible sections while preserving adversarially-confirmed to add value evidence.
---

# Human Docs Readability

## Workflow

Use this skill when editing public Markdown, especially README files, docs pages, finding packets,
PR packets, and evidence pages.

1. Put the human story first: what this is, who it helps, why it matters, what to click next.
2. Keep the first screen scannable: short paragraphs, callouts, compact tables, and direct links.
3. Use GitHub-native components: badges, tables, task lists, blockquotes, and `<details>` sections.
4. Move long machine material to the bottom under:
   `<details><summary>LLM / Machine-readable details</summary>`.
5. Preserve evidence links, commands, hashes, source pins, and reproducibility material.
6. Keep public links absolute when the repo's gates require shareable GitHub URLs.
7. Never bury the primary share link, demo, or maintainer ask below audit internals.

## Page Shape

For a README or landing page:

- H1: project or packet name.
- Badges, if already present.
- One-sentence value proposition.
- `> [!NOTE]` or `> [!TIP]` callout with the best next action.
- Demo or screenshot.
- Compact "Share / Open / Run" table.
- Short "How it works" narrative.
- Collapsible LLM section at the bottom for exhaustive gates, schemas, matrix details, and receipts.

For finding and PR packet pages:

- Share link in the first 10 lines.
- Human summary before the evidence list.
- "What changed", "Why it matters", and "How to verify" before raw artifacts.
- Full bundle links near the top.
- Reproduction commands and machine-readable evidence below the human summary, collapsed if lengthy.

## Quality Bar

Reject docs that:

- start with implementation internals before the value proposition
- contain long uncollapsed checker, schema, matrix, or receipt inventories above the fold
- use vague link labels such as "here" for important share targets
- mix founder-facing guidance with LLM audit material in the same section
- drop evidence needed for the adversarially-confirmed to add value bar

Read `references/markdown-style.md` for the detailed checklist when doing a full rewrite.
