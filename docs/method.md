# Method for building a personal workflow

The method is not tied to a domain. Its first application is coding.

## Core concepts

- **Dimension**: a design question every workflow has to answer, such as "who has the final say" or "how much planning happens up front".
- **Position**: one answer to a dimension. Any existing skill set can be read as a particular combination of positions.
- **Dimension catalog** (`docs/dimensions.md`): every dimension, each source's position on it, and the position the user has chosen. This is the core asset of the repo.
- **Workflow profile** (`docs/workflows/<source>.md`): how one source's pieces fit together as a flow: steps, what each step hands to the next, user checkpoints, loops (ADR 0006).
- **Coupling notes** (in `docs/dimensions.md`): which positions depend on or conflict with each other.
- **General vs. domain dimensions**: general dimensions mostly carry over to other domains (roles, records, handoff, self-improvement). Domain dimensions have to be extracted again for each domain (for coding: TDD, how work is verified).

## Six phases, and where the user steps in

| Phase | What Claude does | How the user steps in |
|---|---|---|
| 0. Choose sources | List candidate skill sets and what sets each apart | **Decide** which to ingest |
| 1. Extract dimensions | Ingest the sources (see "Ingestion" below) and update the catalog | **Confirm** the list of dimensions: add, remove or merge |
| 2. Take positions | In order (ADR 0010): the user states their purpose (one, or one per kind of work); picks the problems they have from the problem list; chooses a stance (where trust comes from); then picks mechanisms from any source that fit the stance, checking coupling notes when borrowing across stances. The dimensions are a completeness checklist: record each as a consequence with a one-line reason | **Decide** purpose, problems, stance and mechanisms. Add dimensions the catalog lacks. This step is always the user's |
| 3. Design skill architecture | Turn the positions into a list of skills and how they relate, starting from the source workflow profiles | **Approve** the architecture |
| 4. Write skills | Write the skills one by one, going back to the originals for wording when needed | **Spot-check** drafts |
| 5. Use them | Record where things got stuck or felt wrong in real projects | **Supply material**: real usage that only the user has |
| 6. Revise | Work out which layer the problem is in: wording, architecture or position | If a position was wrong, **go back to phase 2** |

## Source lifecycle: ingest once, then use the catalog

Existing skill sets are not re-read every time. Each source goes through one ingestion and becomes entries in the catalog plus a workflow profile:

1. **Fetch**: Add the source to `scripts/sources.json` (URL, pinned commit, license, fetch scope), run `python scripts/fetch_sources.py <name>`, and update `docs/sources.md`. Check the license first: do not fetch anything whose license forbids keeping copies. Limit the scope to parts that bear on the domain. Fetched files stay local and are never committed.
2. **Read in full**: Within the scope, read every SKILL.md and the files it references. Catalog pages and READMEs are not enough.
3. **Map**: Map each practice in the source onto an existing dimension as a position, with a citation.
4. **Profile the workflow**: Write `docs/workflows/<source>.md` from the template in `docs/workflows/README.md`, starting with the problems the source solves. Add those problems to the shared problem list and the source's coupling notes to `docs/dimensions.md` (ADR 0008).
5. **Extend**: If the source answers a design question no existing dimension covers, add a dimension and fill in the other sources' positions on it (marking "not addressed" where needed).
6. **Mark done**: Set the source's status in `docs/sources.md` to "ingested".

After ingestion:

- Later phases use the catalog and the workflow profiles instead of re-reading sources.
- Adding a source means running ingestion for that source only; older sources are not re-read.
- Go back to the originals in only two cases: phase 4 needs specific wording or structure, or a catalog summary is not enough for the user to decide.

Trade-off: summarizing always loses detail, so every position must cite its origin and stay traceable to the original.

## The catalog is a reference, not a boundary

The catalog saves re-reading; it does not limit what the skill set can be (ADR 0007).

- The user may take a position no source takes.
- Dimensions may be added in any phase: from the user's own needs, from designing the architecture, or from real use in phase 5.
- The skill architecture may include skills no source has.
- Anything without a source is cited as `user`, or `usage` if it came from phase 5, so every entry stays traceable.

## Optional input: the user's current workflow

During phases 2–3 the user may describe how they work today, in the same format as a workflow profile. It is optional: phase 2 positions already capture what the user wants. Its value is catching steps no source covers and habits worth keeping. Nothing is written for it during repo build-up (ADR 0006).

## Extending to another domain

1. Reuse the general dimensions. The user's positions on them can carry over or be adjusted for the new domain.
2. Choose sources for the new domain (phase 0) and extract its domain dimensions (phase 1).
3. Continue with the remaining phases as usual.
