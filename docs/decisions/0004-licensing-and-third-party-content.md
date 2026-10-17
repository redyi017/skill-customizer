# 0004 Licensing and third-party content in a public repo

- Date: 2026-10-17
- Status: Accepted

## Context

The repo is public on GitHub. The four sources have different licenses:

- Matt Pocock skills and pstack: MIT.
- Anthropic skills: mostly Apache 2.0; docx, pdf, pptx and xlsx are proprietary and forbid copying, keeping copies outside Anthropic's services, adapting and distributing.
- Claude Code plugins: all rights reserved; not open source.

## Decision

1. **Original files stay out of the repo**: `sources/` is git-ignored. `scripts/fetch_sources.py` fetches each source locally at the commit pinned in `scripts/sources.json`. The four proprietary Anthropic skills are not fetched.
2. **The catalog is written in our own words**: describe practices and link to them; quote only short phrases, and avoid quoting non-open-source sources at all.
3. **Skills follow each source's license**:
   - MIT and Apache sources: wording may be borrowed; name the source in that skill's folder and add the copyright and license notice to `THIRD_PARTY_NOTICES.md`. For Apache sources, also state what was changed.
   - Non-open-source sources: borrow ideas only; write all text and code ourselves.
4. **This repo is MIT-licensed** (`LICENSE`).

## Rationale

- Not distributing other people's files avoids distribution-license issues, while the pinned commits keep the originals traceable.
- MIT is compatible with MIT and Apache material and makes clear how others may use these skills.
- This is a general reading of the license terms, not legal advice. Commercial use should be checked with a professional.
