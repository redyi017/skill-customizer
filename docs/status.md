# Status

The single place to pick up from. Update it at the end of every session; git history keeps earlier versions.

## Where we are

Repo build-up. Phase 0 (choose sources) is done; phase 1 (extract dimensions) has started with `mattpocock-skills`: read in full, nothing written yet.

- Method, working agreement and licensing rules are in place (ADRs 0001–0008).
- ADR 0008: profiles start with the problems a source solves; a shared problem list in the catalog; built-in self-checks; diagrams first.
- Four sources are configured and can be fetched with `python scripts/fetch_sources.py`.
- Dimension catalog v0 has 15 dimensions, based only on catalog pages (`docs/dimensions.md`).
- Workflow profile template is ready (`docs/workflows/README.md`); no profiles written yet.

## Open questions

None.

## Decided, waiting to be applied

- Candidate dimensions 16–20 (work state, unattended vs. human-in-the-loop, shared language, portability, maintenance) are held until all four sources are ingested, then added or merged together.
- Provisional user position (origin `user`), to attach to the maintenance dimension when it is added: `improve-codebase-architecture` is a key loop beside the main grill → spec → tickets → implement flow, not an optional side tool.

## Next step

Phase 1: write the `mattpocock-skills` profile (problems first; Matt's README sections #1–#4 name four problems), its catalog entries and coupling notes, then ingest the other sources within scope (`docs/sources.md`). Then the user confirms the list of dimensions.
