# 0008 Problems first, built-in self-checks, visual-first communication

- Date: 2026-10-17
- Status: Accepted. Amends ADR 0006 (profile template) and the working agreement.

## Context

A review of the first two sessions found six gaps the user caught before Claude did. Two patterns explain them:

- **Frame not checked.** Claude built a structure (catalog, profile template) and filled it faithfully, without checking it against how the source is organized or what a later phase needs. The profile recorded *what* each skill does and in what order, but not *which problem* it solves. Matt Pocock's README is organized by problem, and `improve-codebase-architecture` (problem: ball of mud) was underweighted as a side tool.
- **Overbuilding and overclaiming.** Structure and arguments were added before checking that anything used them or that they fit the session goal.

The user also found long, text-heavy tables hard to read, which hid these gaps from review.

## Options

How to record problems:

1. A "Problems it solves" section in each profile only.
2. Option 1, plus a shared problem list in `docs/dimensions.md`, with each dimension tagged by the problems it serves.
3. Reorganize the catalog by problem.

How to adopt the checks:

- A. Rules in `CLAUDE.md` only.
- B. Build the checks into templates and a visible self-review block, with `CLAUDE.md` pointing to them.
- C. Hooks.

## Decision

- **Problems: option 2.** Profiles open with "Problems it solves". `docs/dimensions.md` holds one shared problem list across sources; each problem lists the dimensions that serve it. Phase 2 starts by asking which problems the user actually has, then takes positions only on the linked dimensions (others may still be added; ADR 0007).
- **Checks: option B.** Four checks:
  1. **Name what uses it**: every proposed file, folder or step carries a "used by phase N" label; no label, no item.
  2. **Self-review**: every outline ends with a short self-review: what the source's author would say is missing, and what the proposed rules would accidentally forbid.
  3. **Session goal**: the self-review also states whether the proposal fits the current session goal.
  4. **Problems first**: enforced by the profile template's first section.
- **Communication**: lead with a diagram whenever there is a structure or flow to show, then short points. Tables only for short cells. One line per option in decisions.

## Rationale

- Option 2 narrows phase 2 to what matters to the user, exposes problems one source solves and another ignores, avoids duplicating dimensions, and can be drawn as a problem-to-dimension diagram.
- A rule Claude must remember is what failed. Template slots cannot be skipped silently, and a visible self-review lets the user verify it was done.
- Hooks can block commands but cannot judge whether a profile missed the point (option C rejected).
- Diagrams make gaps visible to the user during review.
