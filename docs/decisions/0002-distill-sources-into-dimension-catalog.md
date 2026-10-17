# 0002 Distill sources into the dimension catalog instead of re-reading them

- Date: 2026-10-17
- Status: Accepted

## Context

When building or revising skills, should we go back to the original files of existing skill sets each time, or first distill them into something that accumulates?

## Options

1. Consult the original files every time.
2. Read each source in full once, distill it into the dimension catalog, and work from the catalog afterwards; adding a source means ingesting only that source.
3. Distill, then delete the originals.

## Decision

Option 2. Original files are kept locally in `sources/` at a pinned commit as an archive, not as day-to-day reference.

## Rationale

- The catalog accumulates: a new source is mapped onto existing dimensions, plus any new ones it reveals.
- No re-reading saves time and context.
- Distilling loses detail, so the originals and citations are kept for borrowing wording in phase 4 or when a summary is not enough.
- Option 3 would make decisions untraceable.
