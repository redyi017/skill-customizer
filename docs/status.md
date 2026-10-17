# Status

The single place to pick up from. Update it at the end of every session; git history keeps earlier versions.

## Where we are

Repo build-up. Phase 0 (choose sources) is done; phase 1 (extract dimensions) has not started.

- Method, working agreement and licensing rules are in place (ADRs 0001–0007).
- Four sources are configured and can be fetched with `python scripts/fetch_sources.py`.
- Dimension catalog v0 has 15 dimensions, based only on catalog pages (`docs/dimensions.md`).
- Workflow profile template is ready (`docs/workflows/README.md`); no profiles written yet.

## Open questions

None.

## Next step

Phase 1: ingest each source within its scope (`docs/sources.md`). For each one, update the catalog, write its workflow profile and add its coupling notes. Then the user confirms the list of dimensions.
