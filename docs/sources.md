# Sources

The machine-readable settings (commits, excluded paths) are in `scripts/sources.json`; keep the two in sync. Source files are fetched locally with `python scripts/fetch_sources.py` and never committed (ADR 0004).

| Source | URL | Author | License | Pinned commit | Status |
|---|---|---|---|---|---|
| Matt Pocock skills | https://github.com/mattpocock/skills | Matt Pocock | MIT (© 2026 Matt Pocock) | `49dd158d1076134a641b33efb035946536778336` (2026-10-17) | Fetched, not ingested |
| pstack | https://github.com/backnotprop/pstack | poteto (Lauren Tan) | MIT (© 2026 Lauren Tan) | `6f131f137de64fdaf928278c0fd9ecec520ccbee` (2026-10-17) | Fetched, not ingested |
| Anthropic skills | https://github.com/anthropics/skills | Anthropic | Mostly Apache 2.0; **docx, pdf, pptx and xlsx are proprietary** and may not be copied, retained, adapted or distributed | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (2026-10-17) | Fetched (proprietary skills excluded), not ingested |
| Anthropic Claude Code plugins | https://github.com/anthropics/claude-code/tree/main/plugins | Anthropic | **All rights reserved**, governed by Anthropic's Commercial Terms; not open source | `c017428c8c27e604840435048d5bce6a9a22c040` (2026-10-17) | Fetched, not ingested |

## Notes

- 2026-10-17: Catalog v0 is based only on catalog and description pages, not on a full reading.
- Anthropic skills on 2026-10-17: academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx.
- Claude Code plugins on 2026-10-17: agent-sdk-dev, claude-opus-4-5-migration, code-review, commit-commands, explanatory-output-style, feature-dev, frontend-design, hookify, learning-output-style, plugin-dev, pr-review-toolkit, ralph-wiggum, security-guidance. Besides skills, they use slash commands, subagents and hooks.
