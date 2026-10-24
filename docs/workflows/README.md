# Workflow profiles

One file per source (`<source>.md`, using the names in `scripts/sources.json`), written during ingestion (ADR 0006). The dimension catalog says what each source's answer is to each design question; a profile says how the source's pieces fit together.

Write profiles in our own words (ADR 0004). For non-open-source sources, describe the flow without quoting.

## Template

```
# <Source> workflow

- Source: <name>, pinned commit <hash>
- Shape: one line, e.g. "linear pipeline by phase" or "router dispatching to playbooks"

## Problems it solves
Start here (ADR 0008). Each problem the source targets, the skills that fix it, and how. Follow the source's own structure when it has one (e.g. a README organized by failure mode). Mark problems Claude inferred rather than read. Add each problem to the shared list in `docs/dimensions.md`.

| Problem | Fixed by (skills / steps) | How | Kind of work (e.g. development / maintenance) |

## Entry points
How work starts and who triggers it (user / Claude / hook).

## Flow
Mermaid diagram of the steps, with arrows labeled by the artifact passed along.

## Steps
| Step | Skill / mechanism | Input | Output | Who triggers |

## User checkpoints
Where the flow stops for the user to decide, confirm or approve.

## Loops
Where the flow goes back (review → fix, retro → repo changes, …).

## Coupling
Positions in this source that only work together, linked to dimension numbers in `docs/dimensions.md`.

## Inferences
Anything Claude inferred rather than read, labeled as such.
```

## Visual report (ADR 0009)

Each profile also gets `docs/reports/<source>.html`, derived from the profile and the catalog (no new claims). Sections, in order:

1. How the profile was built
2. Problems it solves (read vs. inferred)
3. How you would use it: a decision flowchart from the user's situation to the skill they type; model-invoked skills marked
4. How the pieces connect (artifact flow)
5. Positions on each dimension, filterable by problem
6. Coupling
7. Open questions
