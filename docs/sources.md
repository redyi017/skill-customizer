# Sources

Pinned commits, fetch scope and license labels live in `scripts/sources.json`, the single source of truth. This file holds license details, scope rationale and ingestion status. Source files are fetched locally with `python scripts/fetch_sources.py` and never committed (ADR 0004).

| Source | URL | Author | License | Scope | Status |
|---|---|---|---|---|---|
| `mattpocock-skills` | https://github.com/mattpocock/skills | Matt Pocock | MIT (© 2026 Matt Pocock) | Full | Fetched, not ingested |
| `pstack` | https://github.com/backnotprop/pstack | poteto (Lauren Tan) | MIT (© 2026 Lauren Tan) | Full | Fetched, not ingested |
| `anthropic-skills` | https://github.com/anthropics/skills | Anthropic | Apache 2.0 for the skills in scope. docx, pdf, pptx and xlsx are proprietary (no copying, retaining, adapting or distributing) and are never fetched | Coding-related only | Fetched, not ingested |
| `claude-code-plugins` | https://github.com/anthropics/claude-code/tree/main/plugins | Anthropic | **All rights reserved**, governed by Anthropic's Commercial Terms; not open source | Coding-related only | Fetched, not ingested |

## Scope (ADR 0007)

Matt Pocock skills and pstack are the two main, contrasting coding workflows, so they are ingested in full. The other two are ingested only where they bear on coding:

- `anthropic-skills`: `skill-creator`, `webapp-testing`, `mcp-builder`, `doc-coauthoring`, plus the repo README and the Agent Skills spec. Out of scope: academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, frontend-design, internal-comms, slack-gif-creator, theme-factory, web-artifacts-builder, and the proprietary document skills.
- `claude-code-plugins`: `feature-dev`, `code-review`, `pr-review-toolkit`, `security-guidance`, `hookify`, `commit-commands`, `ralph-wiggum`, `explanatory-output-style`, `learning-output-style`, plus the plugins README. Out of scope: agent-sdk-dev, claude-opus-4-5-migration, frontend-design, plugin-dev.

To widen the scope, add paths to the source's `sparse` list in `scripts/sources.json` and fetch again.
