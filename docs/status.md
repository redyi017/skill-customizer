# Status

The single place to pick up from. Update it at the end of every session; git history keeps earlier versions.

## Where we are

Repo build-up, end of phase 1 for the two full sources. `mattpocock-skills` and `pstack` are both ingested: profiles, visual reports, shared problems P1–P13, coupling notes, and dimension details for all 16 dimensions (catalog v0.2, 2026-10-24).

- Method, working agreement and licensing rules are in place (ADRs 0001–0010).
- ADR 0010: purpose → stance → mechanisms; dimensions become a checklist; every skill output marks what can be trusted.
- Dimension 15 has an implementation note (2026-10-24): what ships with a skill set (scripts, subagents, frontmatter or plugin hooks) vs. harness commands the user starts (`/loop`, `/goal`); skills run under `/goal` need a checkable done condition with evidence in the transcript.
- `anthropic-skills` and `claude-code-plugins` are set aside for now (user, 2026-10-24); their catalog columns stay at v0.

## Open questions

None.

## Decided, waiting to be applied

- Candidate dimensions work state, shared language, portability and maintenance are still held. With the Anthropic sources set aside, decide at the start of phase 2 whether to add or merge them now.
- Provisional user position (origin `user`), to attach to the maintenance dimension when it is added: `improve-codebase-architecture` is a key loop beside the main grill → spec → tickets → implement flow, not an optional side tool.

## Next step

Phase 2 (take positions). The user has used Matt's skills for real development and has not used pstack:

- Start from the user's Matt usage: which skills they ran, full flow or single skills, where they skipped or stopped and why. Record it as the optional "user's current workflow" input (`docs/method.md`).
- Use pstack's positions as contrast where Matt's skills did not fit, explained against that experience; the user does not need prior pstack knowledge.
- Optional later: the P1 + P3 design trial; ingesting the Anthropic sources.
