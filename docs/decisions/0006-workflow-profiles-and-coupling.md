# 0006 Workflow profiles and coupling notes

- Date: 2026-10-17
- Status: Accepted

## Context

The dimension catalog breaks each source into one answer per design question. That makes sources easy to compare, but it loses how each source's pieces work together: the order of steps, what each step hands to the next, where the user steps in, and where the flow loops back. Positions also depend on each other; some only work as a package.

## Options

1. A workflow profile per source, in `docs/workflows/`.
2. One more dimension, "workflow shape" (a single table cell per source).
3. Coupling notes in `docs/dimensions.md`: which positions depend on or conflict with each other.
4. A profile of the user's own current workflow.

## Decision

- Adopt 1 and 3 as part of repo build-up: writing a source's workflow profile and its coupling notes becomes part of ingestion.
- Reject 2: one cell cannot hold a flow.
- Defer 4: the user's current workflow is an optional input for phases 2–3. Nothing is written for it during build-up.

## Rationale

- Phase 2 (taking positions) needs the coupling notes to avoid combinations that break a flow.
- Phase 3 (designing the skill architecture) needs whole flows, not single cells.
- The user's own workflow does not affect the completeness of the repo. Its value comes during customization, mainly to catch steps no source covers and habits worth keeping.
