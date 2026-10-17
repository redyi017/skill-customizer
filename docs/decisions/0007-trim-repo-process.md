# 0007 Trim the repo process

- Date: 2026-10-17
- Status: Accepted. Amends ADR 0001 (decision records), ADR 0002 (how the catalog is used) and ADR 0006 (scope of ingestion).

## Context

A review checked every file and rule against one question: does a later phase actually use it? Most do. A few duplicate each other, grow without adding value, or come too early. The wording also implied that later phases may not go beyond the catalog.

## Decision

1. **One source of truth for sources**: pinned commits and fetch scope live only in `scripts/sources.json`; `docs/sources.md` keeps license details, scope rationale and status.
2. **One status file instead of session notes**: `docs/status.md` (where we are, open questions, next step) replaces `docs/sessions/`. Git history keeps earlier versions.
3. **Lighter decision records**: the user's phase 2 positions are recorded in `docs/dimensions.md` with a one-line reason each. ADRs are reserved for changes to the repo or the method.
4. **No `evals/` yet**: added back when phase 4 needs it.
5. **Scoped ingestion**: Matt Pocock skills and pstack are ingested in full; Anthropic skills and Claude Code plugins only where they bear on coding (`docs/sources.md`). Out-of-scope parts are not fetched.
6. **The catalog is a reference, not a boundary**: later phases use the catalog and workflow profiles instead of re-reading sources, but may go beyond them. The user may take positions no source takes and add dimensions in any phase. Anything without a source is cited as `user`, or `usage` if it came from phase 5.

## Rationale

- Each kept artifact is consumed by a later phase; duplicates and premature folders only add upkeep.
- Fifteen position ADRs would bury the few records that explain the repo's structure.
- Out-of-scope skills (art, branding, model migration, …) cannot inform a coding workflow.
- The purpose of the catalog is to save re-reading, not to limit what the user's skill set can be.
