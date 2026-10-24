# 0010 Purpose, stance, mechanisms; dimensions become a checklist; mark what can be trusted

- Date: 2026-10-24
- Status: Accepted. Amends ADR 0002 (dimension catalog), ADR 0006 (profiles) and phase 2 in `docs/method.md`.

## Context

After profiling `mattpocock-skills` and `pstack`, the user asked whether extracting dimensions and picking a position on each would produce a working skill set. Two findings:

- The coupling notes (13 across 15 dimensions) show the dimensions are not independent. Each source's positions follow from a deeper choice, so mixing positions per dimension risks an incoherent result (for example, an agent that stops to ask questions with no spec to anchor them).
- The deeper choice has two levels. **Purpose** (user's framing): who the skill set is built for and what the human keeps doing. Matt builds for a human engineer who stays the engineer; pstack builds for an operator who delegates as much as possible to agents. **Stance** (Claude's framing): where trust in the work comes from. Matt builds trust before the code (grilling, spec, review against it); pstack builds it after (independent verification on the real app). Stance follows from purpose.

The user added a principle: the user should always know which parts of an output can be trusted and which cannot.

## Options

1. Keep the flat list of 15 dimensions and pick a position on each.
2. Three layers: purpose → stance → mechanisms, with problems filtering stance and mechanisms; dimensions kept as a completeness checklist.
3. Drop dimensions and borrow whole packages per kind of work.

## Decision

Option 2.

- Every profile gets a **Purpose** section and a **Stance** section after its header, each claim quoted from the source or labeled inferred.
- Phase 2 order: the user states their purpose (one, or one per kind of work), picks the problems they have, chooses a stance, then picks mechanisms that fit the stance. Mechanisms are borrowed from any source.
- The 15 dimensions become a checklist: "has the chosen stance answered this?" Positions on them are recorded as consequences, not separate choices. Coupling notes are checked when a mechanism is borrowed across stances.
- **Trust marking** (origin `user`): every skill the user's set produces must make clear what in its output can be trusted and what cannot (for example: measured / inferred / guess labels, an "Attention" list, an explicit unverified marker). This is a requirement on phase 4 skills, not a dimension position.

## Rationale

- Purpose and stance explain most coupling notes at once; choosing them first prevents incoherent mixes.
- Mechanisms that solve one problem without assuming a whole package (grilling, decision log, benchmark checklist, two-axis review, enforcement ranking) still transfer between sources.
- Keeping the dimensions as a checklist preserves the catalog work and catches gaps a stance leaves open.
- The user may hold different purposes for different kinds of work (designing a feature vs. an overnight migration); the layering allows that.
