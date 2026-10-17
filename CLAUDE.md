# SkillCustomizer

This repo builds a **personal workflow skill set**. The first domain is coding (Python, Claude Code, GitHub Issues/PRs). Other domains may follow.

At the start of every session, read this file, then `docs/status.md`.

## Working agreement

- **Language**: Everything in the repo is in English (ADR 0003, ADR 0005). In conversation, Claude replies in the language the user writes in.
- **One goal per session**: Confirm the goal at the start. At the end, update `docs/status.md` (where we are, open questions, next step).
- **Who decides what**:
  - Structural decisions (method, repo layout, the list of dimensions, the user's position on each dimension, skill architecture): Claude presents 2–3 options with trade-offs; the user decides.
  - Small things (wording, file details): Claude decides and says afterwards what it chose.
  - Deleting or overwriting the user's content: always ask first.
- **Four ways the user steps in**: decide, confirm, approve, supply material. `docs/method.md` says which one applies at each phase.
- **Discuss before building**: Show an outline or options first; write the full content only after the user agrees.
- **Self-checks (ADR 0008)**:
  - Every proposed file, folder or step carries a "used by phase N" label. No label, no item.
  - Every outline or proposal of something to build or change ends with a short **self-review** (not status updates or answers to questions): what the source's author would say is missing; what the proposed rules would accidentally forbid; whether it fits the session goal.
  - Profiles start with "Problems it solves" (template in `docs/workflows/README.md`).
- **Communication (ADR 0008)**: Lead with a diagram whenever there is a structure or flow to show, then short points. Tables only for short cells. One line per option when asking for a decision.
- **Record decisions**: Changes to the repo or the method become an ADR in `docs/decisions/NNNN-title.md` (Context / Options / Decision / Rationale). The user's positions on dimensions are recorded in `docs/dimensions.md` with a one-line reason each, not as ADRs (ADR 0007).

## Method in brief

Details are in `docs/method.md`.

0. Choose sources → 1. Extract dimensions → 2. Take positions → 3. Design skill architecture → 4. Write skills → 5. Use them → 6. Revise

- Each existing skill set is **read in full once, when it is ingested**. After that it lives in the dimension catalog (`docs/dimensions.md`) and its workflow profile (`docs/workflows/`). Later phases use those instead of re-reading the sources, **as a reference, not a boundary**: the user may take positions no source takes and add dimensions in any phase (ADR 0007).
- Third-party files are fetched with `python scripts/fetch_sources.py` into `sources/` (local only, never committed) and pinned to a commit so the originals stay traceable. Matt Pocock skills and pstack are ingested in full; Anthropic skills and Claude Code plugins only where they bear on coding (`docs/sources.md`). Go back to them only in phase 4, to borrow specific wording, or when the catalog summary is not enough to make a decision.

## Layout

```
CLAUDE.md               Working agreement and repo rules (this file)
docs/method.md          The method for building a workflow
docs/dimensions.md      Dimension catalog: problem list, dimensions, each source's position, coupling notes, the user's position
docs/workflows/         Workflow profile per source: steps, hand-offs, user checkpoints, loops
docs/sources.md         Sources: license details, scope, ingestion status
docs/status.md          Where we are, open questions, next step
docs/decisions/         ADRs
sources/<source>/       Third-party files, local only (git-ignored), read-only
scripts/                fetch_sources.py and sources.json (single source of truth for commits and scope)
LICENSE                 MIT
THIRD_PARTY_NOTICES.md  Copyright and license notices for adapted third-party material
skills/<domain>/        The user's own skill set
```

## Rules

- **Licensing (ADR 0004)**: Never commit third-party source files. Do not edit files in `sources/`; to update a source, change its commit in `scripts/sources.json` and fetch again.
- Borrowing wording from an MIT or Apache source: name the source in that skill's folder and update `THIRD_PARTY_NOTICES.md` (for Apache, also state what was changed).
- Non-open-source sources (Claude Code plugins): borrow ideas only; never copy text or code, and avoid quoting them in the catalog.
- Every position and dimension in the catalog cites its origin: source, skill name and file path; or `user` / `usage` (phase 5) when it has no source.
- Every skill in `skills/` states which dimensions and sources it draws on.
- Keep Claude's own inferences separate from what the sources say, and label them.

## GitHub

- Public repo: https://github.com/redyi017/skill-customizer
- From the cloud environment, Claude carries local commits over with a git bundle and pushes from there. The user can also `git push` from their own machine.
