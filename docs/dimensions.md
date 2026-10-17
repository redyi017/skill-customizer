# Dimension catalog

> **Version v0 (2026-10-17)**: Based only on catalog and description pages, not on a full reading. All four sources must go through full ingestion (see `docs/method.md`) before this can support decisions. Items marked "unverified" are Claude's inferences, not yet checked against the originals.

Kind: **General** = carries over to other domains; **Domain** = specific to coding.

## Overview

Source abbreviations: **Matt** = Matt Pocock skills; **pstack**; **A-skills** = Anthropic skills; **CC** = Anthropic Claude Code plugins. The CC column is based only on each plugin's description.

| # | Dimension | Kind | Matt | pstack | A-skills | CC | My position |
|---|---|---|---|---|---|---|---|
| 1 | Roles and authority | General | The user is the tech lead; the agent questions first, then executes | The agent is a principled senior engineer and judges for itself | The agent is a specialist with a toolkit and works toward the stated goal | Several coexist: `learning-output-style` asks the user to write code at decision points; `ralph-wiggum` loops the agent until done | TBD |
| 2 | Entry and triggering (who triggers: user only / Claude only / both) | General | Many user-invoked commands, plus `/ask-matt` to pick one | One sticky mode skill routes to playbooks automatically | Independent skills, triggered automatically by Claude from their descriptions | Mostly user-invoked commands, plus automatic hooks | TBD |
| 3 | Planning depth | Domain | Heavy: grill → spec → tickets | Light: no planning skill; uses plan mode | Mostly not addressed; `doc-coauthoring` has a staged flow | `feature-dev`: explore → design architecture → implement → quality review (unverified) | TBD |
| 4 | Clarifying requirements | General | Interview-style questioning (`/grilling`) | Follows the playbook's steps | `skill-creator` interviews for intent first (unverified) | `feature-dev` includes a clarifying-questions step (unverified) | TBD |
| 5 | How work is split | Domain | By development **phase** | By **task type** (bug, perf, refactor, …) | By **capability or output format** (docx, MCP, web testing, …) | By **single step of the workflow** (commit, PR review, security check) | TBD |
| 6 | Artifacts and records | General | Specs, tickets, domain glossary | Todo list | Concrete files; `skill-creator` produces eval results | Commits, PRs, review comments | TBD |
| 7 | Implementation discipline | Domain | TDD, deep modules | TDD, delete before adding, no comments, unslop | Tool-specific best practices with bundled scripts | `security-guidance` warns on edits; `hookify` blocks unwanted behavior with hooks | TBD |
| 8 | Verification | Domain | Code review against standards and the spec | Prove it works | `webapp-testing` runs real Playwright checks; `skill-creator` runs evals | `code-review`: several specialized agents with confidence scores; `pr-review-toolkit` reviews by aspect (tests, error handling, types, …) | TBD |
| 9 | Delegation and multiple agents | Domain | `/implement-spec` uses parallel subagents | arena and swarm multi-model workflows; models mapped to roles | `skill-creator` runs evals in parallel subagents (unverified) | Heavy use of specialized subagents (explore, architect, review) | TBD |
| 10 | Context and handoff | General | `/handoff` | Guard the context window (principle skill) | Progressive loading: reference files and scripts beyond SKILL.md are read only when needed | Work goes to subagents; the main conversation gets only results (unverified) | TBD |
| 11 | Communication style | General | `/wait-what` restates in plain English | Written for the consumer and maintainer of the work; technical-writing | `doc-coauthoring` has readers test the document (unverified); `internal-comms` uses fixed formats | `explanatory-output-style` explains implementation choices; `learning-output-style` teaches | TBD |
| 12 | Self-improvement | General | `/retro` | `reflect`; `automate-me` drafts a personal skill from transcripts | `skill-creator`: iterate with evals, optimize descriptions | `hookify` creates hooks from conversation patterns | TBD |
| 13 | Per-repo / per-org setup | General | `/setup-matt-pocock-skills` | `/setup-pstack`: reasoning budget, model roles | Org settings written into the skill itself (`brand-guidelines`, `internal-comms`) | No dedicated setup plugin seen (unverified) | TBD |
| 14 | Skill type and granularity | General | **Process** skills (by phase) + **reference** skills | **Playbooks** (by task) + **principle** skills (one principle each) | **Capability** skills (one tool or format each, with scripts) | **Step** plugins (one workflow step each) | TBD |
| 15 | Mechanism (skill / subagent / hook) | General | Mostly skills (including legacy commands) | Mostly skills, plus subagents | Skills only | Skills (including legacy commands), subagents and hooks; hooks **enforce** behavior instead of relying on the agent to remember | TBD |

> Note: Claude Code has merged custom slash commands into skills (`.claude/commands/x.md` and `.claude/skills/x/SKILL.md` both create `/x` and behave the same; new work should be skills). So "slash command" is no longer a separate mechanism; it is a triggering option under dimension 2, controlled by the frontmatter fields `disable-model-invocation: true` (user only) and `user-invocable: false` (Claude only). Source: https://code.claude.com/docs/en/skills

## Dimension details

Detailed positions, citations and trade-offs for each dimension are added during full ingestion in phase 1. Format:

```
### N. Dimension name
- Definition: the design question this dimension answers
- Kind: General / Domain
- Positions:
  - A (source, skill, file path): description
  - B (...): description
- Trade-offs:
- My position: TBD (link to the ADR once decided)
```
