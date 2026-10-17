# sources/

Third-party skill files. They live on your machine only and are **never committed** (see `docs/decisions/0004-licensing-and-third-party-content.md`).

Fetch or update:

```
python scripts/fetch_sources.py            # all sources
python scripts/fetch_sources.py pstack     # one source
```

Sources, pinned commits and license settings are in `scripts/sources.json`.
