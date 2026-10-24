# 0009 A visual report for each source, with a usage flowchart

- Date: 2026-10-23
- Status: Accepted. Extends ADR 0006 (profiles) and ADR 0008 (visual-first communication).

## Context

After the first profile (`mattpocock-skills`) was written, the user found the markdown profile and catalog entries hard to review as a whole. A one-page visual summary made the result easy to check. The user also wanted to see how a person would actually use the skill set, which the flow diagram does not show: it shows how artifacts pass between skills, not which skill to reach for in which situation.

## Options

1. Keep the markdown profile only.
2. Markdown profile plus a visual report per source, published as an artifact for review.
3. Replace the markdown profile with the visual report.

## Decision

Option 2. Each ingested source gets a visual report alongside its markdown profile:

- Source file: `docs/reports/<source>.html` (committed), published as a private artifact for review.
- Sections, in order: how the profile was built; problems it solves (read vs. inferred marked); **how you would use it** (a decision flowchart from the user's situation to the skill they type, model-invoked skills marked); how the pieces connect (artifact flow); positions on each dimension (filterable by problem); coupling; open questions.
- The markdown profile and `docs/dimensions.md` stay the source of truth; the report is derived from them and adds no new claims.
- Licensing (ADR 0004) applies: for non-open-source sources the report describes, never quotes.

## Rationale

- The markdown files are what later phases read; the report is what the user reviews. Keeping both serves each reader (option 3 would lose the citations later phases need).
- The usage flowchart answers a question no other section does, and it is the natural input to phase 3 (designing the user's own skill architecture).
