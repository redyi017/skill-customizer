# Dimension catalog

> **Version v0.1 (2026-10-18)**: Matt column, coupling notes and Matt's dimension details checked against a full read of `mattpocock-skills` @ `49dd158`. Other columns still from v0.
>
> **Version v0 (2026-10-17)**: Based only on catalog and description pages, not on a full reading. All four sources must go through full ingestion (see `docs/method.md`) before this can support decisions. Items marked "unverified" are Claude's inferences, not yet checked against the originals.

Kind: **General** = carries over to other domains; **Domain** = specific to coding.

Since ADR 0010 the dimensions are a **completeness checklist**, not separate choices: phase 2 picks purpose, problems, stance and mechanisms, and each dimension records what that choice implies.

The catalog is a reference, not a boundary (ADR 0007). Dimensions and positions without a source are cited as `user`, or `usage` if they came from phase 5. Record the user's position in the last column with a one-line reason.

## Problems

Shared across sources (ADR 0008). Phase 2 starts here: the user picks the problems they actually have, then takes positions on the linked dimensions. Filled in during ingestion from each profile's "Problems it solves".

| # | Problem | Dimensions that serve it | Solved by |
|---|---|---|---|
| P1 | The agent didn't do what I want (misalignment) | 4, 1 | Matt, pstack |
| P2 | The agent is too verbose (no shared language) | 11, 6 | Matt |
| P3 | The code doesn't work / isn't proven to work (no feedback loops, "it compiles", unvetted numbers) | 7, 8 | Matt, pstack |
| P4 | We built a ball of mud (entropy) | 7, (maintenance, held) | Matt |
| P5 | Context lost between sessions and phases (inferred) | 10 | Matt |
| P6 | Work too big for one session (inferred); parallel agents overwrite each other | 3, 5, 9 | Matt, pstack |
| P7 | Raw incoming issues pile up (inferred) | 2, 6 | Matt |
| P8 | The agent's environment never improves (inferred); repeating the same correction | 12 | Matt, pstack |
| P9 | Steps only a human or another person can do (inferred) | 1 | Matt |
| P10 | Slop: too much low-quality code and prose | 7, 11 | pstack |
| P11 | The agent lacks the context to do the work right | 10, 4 | pstack |
| P12 | Locking in the first design, or polishing an untested plan | 3, 9 | pstack |
| P13 | Unattended work can't be trusted or audited | 1, 6, 8 | pstack |

## Overview

Source abbreviations: **Matt** = Matt Pocock skills; **pstack**; **A-skills** = Anthropic skills; **CC** = Anthropic Claude Code plugins. The CC column is based only on each plugin's description.

| # | Dimension | Kind | Matt | pstack | A-skills | CC | My position |
|---|---|---|---|---|---|---|---|
| 1 | Roles and authority | General | The user is the tech lead; the agent questions first, then executes | The agent is a principled senior engineer and judges for itself | The agent is a specialist with a toolkit and works toward the stated goal | Several coexist: `learning-output-style` asks the user to write code at decision points; `ralph-wiggum` loops the agent until done | TBD |
| 2 | Entry and triggering (who triggers: user only / Claude only / both) | General | Split by who may invoke: user-invoked skills orchestrate, model-invoked skills hold discipline; an orchestrator never calls another orchestrator; `/ask-matt` routes | One sticky mode skill routes to playbooks automatically | Independent skills, triggered automatically by Claude from their descriptions | Mostly user-invoked commands, plus automatic hooks | TBD |
| 3 | Planning depth | Domain | Heavy: grill → spec → tickets | Light: no planning skill; uses plan mode | Mostly not addressed; `doc-coauthoring` has a staged flow | `feature-dev`: explore → design architecture → implement → quality review (unverified) | TBD |
| 4 | Clarifying requirements | General | Interview-style questioning (`/grilling`) | Follows the playbook's steps | `skill-creator` interviews for intent first (unverified) | `feature-dev` includes a clarifying-questions step (unverified) | TBD |
| 5 | How work is split | Domain | By development **phase** | By **task type** (bug, perf, refactor, …) | By **capability or output format** (docx, MCP, web testing, …) | By **single step of the workflow** (commit, PR review, security check) | TBD |
| 6 | Artifacts and records | General | Specs and tickets on the tracker, `GLOSSARY.md`, ADRs, HTML architecture report, handoff files, cited research notes | Todo list | Concrete files; `skill-creator` produces eval results | Commits, PRs, review comments | TBD |
| 7 | Implementation discipline | Domain | TDD, deep modules | TDD, delete before adding, no comments, unslop | Tool-specific best practices with bundled scripts | `security-guidance` warns on edits; `hookify` blocks unwanted behavior with hooks | TBD |
| 8 | Verification | Domain | Code review against standards and the spec | Prove it works | `webapp-testing` runs real Playwright checks; `skill-creator` runs evals | `code-review`: several specialized agents with confidence scores; `pr-review-toolkit` reviews by aspect (tests, error handling, types, …) | TBD |
| 9 | Delegation and multiple agents | Domain | `/implement-spec` runs implementer subagents across the ready-ticket frontier; `code-review` runs two parallel review subagents; `research` runs as a background agent | arena and swarm multi-model workflows; models mapped to roles | `skill-creator` runs evals in parallel subagents (unverified) | Heavy use of specialized subagents (explore, architect, review) | TBD |
| 10 | Context and handoff | General | `/handoff` | Main chat coordinates; bulk goes to subagents with file-pointer briefs; fresh agent per task; state on disk (decision log, resume note); scripts return query results, not raw data | Progressive loading: reference files and scripts beyond SKILL.md are read only when needed | Work goes to subagents; the main conversation gets only results (unverified) | TBD |
| 11 | Communication style | General | `/wait-what` restates in plain English | Written for the consumer and maintainer of the work; technical-writing | `doc-coauthoring` has readers test the document (unverified) | `explanatory-output-style` explains implementation choices; `learning-output-style` teaches | TBD |
| 12 | Self-improvement | General | `/retro` | `reflect`; `automate-me` drafts a personal skill from transcripts | `skill-creator`: iterate with evals, optimize descriptions | `hookify` creates hooks from conversation patterns | TBD |
| 13 | Per-repo / per-org setup | General | `/setup-matt-pocock-skills` | `/setup-pstack`: reasoning budget, model roles | Not addressed within scope (unverified) | No dedicated setup plugin seen (unverified) | TBD |
| 14 | Skill type and granularity | General | **Process** skills (by phase) + **reference** skills | **Playbooks** (by task) + **principle** skills (one principle each) | **Capability** skills (one tool or format each, with scripts) | **Step** plugins (one workflow step each) | TBD |
| 15 | Mechanism (skill / subagent / hook) | General | Mostly skills (including legacy commands) | Mostly skills, plus subagents | Skills only | Skills (including legacy commands), subagents and hooks; hooks **enforce** behavior instead of relying on the agent to remember | TBD |
| 16 | Unattended vs. human-in-the-loop | General | No offline mode; only tightly scoped AFK tasks go to a subagent | Planned offline mode: trust check, contract with a pass/fail done condition, `/loop`, decision log audited by another model | Not covered (unverified) | `ralph-wiggum` loops until done (unverified) | TBD |

> Note: Claude Code has merged custom slash commands into skills (`.claude/commands/x.md` and `.claude/skills/x/SKILL.md` both create `/x` and behave the same; new work should be skills). So "slash command" is no longer a separate mechanism; it is a triggering option under dimension 2, controlled by the frontmatter fields `disable-model-invocation: true` (user only) and `user-invocable: false` (Claude only). Source: https://code.claude.com/docs/en/skills

## Coupling notes

Positions that depend on or conflict with each other (ADR 0006). Filled in during ingestion; each note names the dimensions involved and cites its source.

| Dimensions | Note | Source |
|---|---|---|
| 1, 3, 6 | User as decider, heavy planning and spec/ticket artifacts form one package. `implement` consumes tickets, so dropping `to-spec`/`to-tickets` leaves multi-session builds without input. | Matt, `skills/engineering/ask-matt/SKILL.md` |
| 6, 10 | `/clear` between tickets works only because each ticket is self-contained. | Matt, `ask-matt/SKILL.md` |
| 3, 8 | `code-review`'s Spec axis needs an originating spec or issue; without one it skips. | Matt, `skills/engineering/code-review/SKILL.md` |
| 4, 11 | (inferred) `wait-what` and concise vocabulary need the `GLOSSARY.md` that `grill-with-docs` builds; `grill-me` leaves none. | Matt, `ask-matt/SKILL.md` |
| 2, 14, 15 | The invocation split is how process skills are kept apart from reference skills; the no-nesting rule depends on it. | Matt, `README.md` (Reference) |
| 13, 6 | `setup-matt-pocock-skills` must run first; `triage`, `to-spec`, `to-tickets`, `code-review` read its tracker config. | Matt, `code-review/SKILL.md`, `implement-spec/SKILL.md` |
| 7, 8 | Refactoring is moved out of the TDD loop into review; the reviewer, not the implementer, enforces coding standards (less context pressure). | Matt, `skills/engineering/tdd/SKILL.md`, `skills/engineering/retro/SKILL.md` |

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

Matt's positions below are from the full read (2026-10-18). Other sources are added when ingested.

### 1. Roles and authority
- Definition: Who decides what: the user, the agent, or both, and on which kinds of questions.
- Kind: General
- Positions:
  - Matt: The user decides; the agent finds facts. In grilling, facts are the agent's job (it dispatches subagents to look things up), decisions are the user's, and it does not act until the user confirms shared understanding (`skills/productivity/grilling/SKILL.md`). TDD seams are confirmed with the user before any test (`skills/engineering/tdd/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Keeps the user in control and catches misalignment early; costs user attention on every change.
- My position: TBD

### 2. Entry and triggering
- Definition: Who triggers each skill: user only, Claude only, or both.
- Kind: General
- Positions:
  - Matt: Two classes. User-invoked (`disable-model-invocation: true`) orchestrate; model-invoked hold reusable discipline and can also be typed. A user-invoked skill may call model-invoked ones, never another user-invoked one. `ask-matt` is a router (`README.md`, Reference; `skills/engineering/ask-matt/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Predictable: the process never starts by itself. The user must know or ask which skill to type.
- My position: TBD

### 3. Planning depth
- Definition: How much planning happens before code, and in what form.
- Kind: Domain
- Positions:
  - Matt: Scaled to size: single-session work goes grill → implement; multi-session work goes grill → `to-spec` → `to-tickets` → implement; foggy, huge efforts go through `wayfinder` first (`ask-matt/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Plans match the work's size; three tiers to learn, and the user picks the tier.
- My position: TBD

### 4. Clarifying requirements
- Definition: How the agent closes the gap between what the user said and what they want.
- Kind: General
- Positions:
  - Matt: Relentless interview over a design tree, in rounds: ask the whole frontier, numbered, each with a recommended answer worded so "yes" accepts it; done when the frontier is empty (`skills/productivity/grilling/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Thorough and fast to answer; long sessions for small changes. Matt says use it every time (`README.md` #1).
- My position: TBD

### 5. How work is split
- Definition: The axis along which skills are cut.
- Kind: Domain
- Positions:
  - Matt: By development phase (align, spec, tickets, build, review, retro), plus on-ramps by situation (triage, bugs, wayfinder) (`ask-matt/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Clear hand-offs between phases; task-type knowledge (e.g. perf work) has no home of its own.
- My position: TBD

### 6. Artifacts and records
- Definition: What the workflow writes down, and where.
- Kind: General
- Positions:
  - Matt: Specs and tickets on the issue tracker (or local files), `GLOSSARY.md`, ADRs, HTML architecture report, handoff files in the OS temp dir (not the repo), cited research notes in the repo (`to-spec`, `to-tickets`, `domain-modeling`, `handoff`, `research` SKILL.md files).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Durable, reviewable trail that later phases consume; requires a tracker setup and some ceremony.
- My position: TBD

### 7. Implementation discipline
- Definition: Rules the agent follows while writing code.
- Kind: Domain
- Positions:
  - Matt: TDD with vertical slices at pre-agreed seams; tests through public interfaces; refactoring is not part of the loop; deep modules via `codebase-design` vocabulary (`skills/engineering/tdd/SKILL.md`, `skills/engineering/codebase-design/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - High-quality tests and design; slower start, and seams need user confirmation.
- My position: TBD

### 8. Verification
- Definition: How the work is checked before it is done.
- Kind: Domain
- Positions:
  - Matt: Two-axis review of the diff since a fixed point: Standards (repo standards plus a Fowler smell baseline, repo overrides) and Spec (matches the originating issue), as parallel subagents. PR bodies carry before/after evidence (`skills/engineering/code-review/SKILL.md`, `skills/engineering/pr/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Separates "is it good code" from "is it the right code"; the Spec axis needs a spec to exist.
- My position: TBD

### 9. Delegation and multiple agents
- Definition: When and how work is sent to other agents.
- Kind: Domain
- Positions:
  - Matt: Subagents for fact-finding in grilling, parallel review axes, background research, and `implement-spec`'s implementer subagents (own worktree each), merger subagent and exploration subagent; communication via context pointers, not copies (`skills/engineering/implement-spec/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Concurrency and clean contexts; merge coordination and harder debugging.
- My position: TBD

### 10. Context and handoff
- Definition: How context is preserved or reset across phases and sessions.
- Kind: General
- Positions:
  - Matt: Decide only at phase boundaries, in order: continue → `/clear` → `/handoff` (only for a new harness, directory, colleague, or a side fork) → subagent → `/compact` (default, last). Keep grill → spec → tickets in one window (`ask-matt/PHASE-BOUNDARIES.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Explicit and cheap-first; relies on the user judging the boundaries.
  - pstack: The main chat coordinates and keeps summaries; bulk reading, writing and verifying go to subagents ("Route bulk to subagents; keep summaries in the main thread", `principle-guard-the-context-window`). Briefs carry file pointers, not pasted context; each new task gets a fresh subagent with one consolidated brief, because "interrupt-chained resumes silently drop directives" (`poteto-mode`, Subagents). State lives on disk: decision log (`show-me-your-work`), resume note before compaction (`pause-safely.md`), Orchestrate's store. Scripts return query results instead of raw data (`principle-build-the-lever`, `trace-forensics.md`).
  - Trade-offs (two-source view):
    - Matt keeps reasoning first-hand but depends on the user calling the boundary; pstack keeps the window clean but the main thread works mostly from summaries, which Matt calls lossy secondary sources.
- Implementation note (user, 2026-10-24): context management is an implementation concern, decided in phase 3 (skill architecture), not at the purpose or stance layer. One requirement flows down from stance: conclusions drawn from summaries are marked (ADR 0010, trust marking).
- My position: TBD

### 11. Communication style
- Definition: How the agent talks to the user.
- Kind: General
- Positions:
  - Matt: Concise via a shared domain language in `GLOSSARY.md`; `wait-what` re-pitches a missed message in plain English (`README.md` #2; `skills/productivity/wait-what/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Fewer words, consistent naming in code; needs the glossary to be built and kept up.
- My position: TBD

### 12. Self-improvement
- Definition: How the workflow gets better over time.
- Kind: General
- Positions:
  - Matt: `retro` suggests environment changes after a session, most severe first, across navigation, automated checks, coding standards, AGENTS.md, tool economy, no-ops and information access; mechanical mistakes become deterministic checks, judgement calls become coding standards (`skills/engineering/retro/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Improves the environment, not the skills; suggestions only, the user applies them.
- My position: TBD

### 13. Per-repo / per-org setup
- Definition: How the skills learn about a specific repo.
- Kind: General
- Positions:
  - Matt: `setup-matt-pocock-skills`, once per repo: issue tracker (GitHub, GitLab, local, or custom), triage labels, doc locations (`skills/engineering/setup-matt-pocock-skills/SKILL.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Skills stay generic; one more step before the first use.
- My position: TBD

### 14. Skill type and granularity
- Definition: What kinds of skills exist and how big each is.
- Kind: General
- Positions:
  - Matt: Process skills (user-invoked orchestrators) plus reference skills (model-invoked discipline and vocabulary, e.g. `codebase-design`, `domain-modeling`, `tdd`); small and composable by design (`README.md`).
  - Trade-offs (Matt-only view, revisit after other sources):
    - Easy to swap one piece; the flow lives in `ask-matt`, not in the skills themselves.
- My position: TBD

### 15. Mechanism (skill / subagent / hook)
- Definition: Which Claude Code mechanism carries each behavior.
- Kind: General
- Positions:
  - Matt: Skills plus subagents; no hooks in the main flow (`git-guardrails-claude-code` in `misc/` is outside the documented flows). Enforcement comes from review and from checks that `retro` proposes.
  - Trade-offs (Matt-only view, revisit after other sources):
    - Portable across agents (Claude Code, Codex, Copilot, Gemini); nothing enforces behavior automatically.
- My position: TBD

### 16. Unattended vs. human-in-the-loop
- Definition: What the workflow does when the user is away: stop, keep going, or never start.
- Kind: General
- Origin: candidate held until all sources were in; brought forward by the user on 2026-10-24 after the pstack profile.
- Positions:
  - Matt: No offline mode. The phase-boundary tree asks "Can the task be done AFK?" and sends only a tightly scoped task to a subagent; the main flow expects the user at each phase (`ask-matt/PHASE-BOUNDARIES.md`).
  - pstack: A planned offline mode. Before: a trust check (done it once, agent has your tools, every stage can stop the line, repeated failures turned into checks) and a contract (goal, pass/fail done condition, worktree, pre-answered permissions, escape hatch) (`docs/guide/07-overnight.md`). During: `/loop` wakes on a timer or event; each iteration makes one change, verifies, commits or discards, logs one row; the predicate never relaxes (`autonomous-run.md`). Irreversible actions still pause; calls only the user can make get a default plus a report (`poteto-mode`, Autonomy and Non-negotiables). After: `show-me-your-work` ends with an Attention list from a reviewer on another model. Larger: Autopilot-full, Autopilot-stack, Orchestrate (`gates.md` parks questions with a default).
  - Trade-offs (two-source view):
    - Matt never acts without the user but cannot use time the user is away; pstack uses that time but needs a working verification setup first, and its trust rests on the done condition being right.
- My position: TBD
