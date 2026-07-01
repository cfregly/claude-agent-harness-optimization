# Markdown Style Checklist

Use this checklist for public README and docs rewrites.

## Human-first top

- Lead with the user outcome, not the implementation.
- Prefer two short paragraphs over one dense paragraph.
- Put "who this helps" and "what to click" before installation or audit detail.
- Use one compact table for links instead of a long bullet list.
- Keep headings short and concrete.

## GitHub-native components

- Use `> [!NOTE]` for orientation.
- Use `> [!TIP]` for the next best action.
- Use tables for link cards and status matrices.
- Use `<details><summary>LLM / Machine-readable details</summary>` for long audit detail.
- Keep code blocks only where the reader will copy a command.

## Machine-readable bottom

Move these below the human sections:

- exhaustive checker descriptions
- schemas and field-by-field contracts
- raw matrix details and source pins
- long reproduction command sets
- CI/gate inventories
- generated PR packet internals

## Final pass

- Important links use descriptive labels.
- The first 80 lines are useful to a human skimming the page.
- The LLM details section preserves enough context for agents and audits.
- Public URLs still point to existing files or folders.
