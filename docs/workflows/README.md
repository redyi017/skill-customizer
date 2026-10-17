# Workflow profiles

One file per source (`<source>.md`, using the names in `scripts/sources.json`), written during ingestion (ADR 0006). The dimension catalog says what each source's answer is to each design question; a profile says how the source's pieces fit together.

Write profiles in our own words (ADR 0004). For non-open-source sources, describe the flow without quoting.

## Template

```
# <Source> workflow

- Source: <name>, pinned commit <hash>
- Shape: one line, e.g. "linear pipeline by phase" or "router dispatching to playbooks"

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
