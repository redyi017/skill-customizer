"""Fetch third-party skill sources into sources/ at pinned commits.

The fetched files stay local and are git-ignored (ADR 0004).
Usage: python scripts/fetch_sources.py [name ...]
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "scripts" / "sources.json"
DEST = ROOT / "sources"


def git(*args, cwd=None):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def fetch(name, spec):
    target = DEST / name
    if target.exists():
        shutil.rmtree(target)
    git("init", "-q", str(target))
    git("remote", "add", "origin", spec["repo"], cwd=target)
    git("sparse-checkout", "init", "--no-cone", cwd=target)
    (target / ".git" / "info" / "sparse-checkout").write_text(
        "\n".join(spec["sparse"]) + "\n", encoding="utf-8"
    )
    git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", spec["commit"], cwd=target)
    git("checkout", "-q", "FETCH_HEAD", cwd=target)
    print(f"{name}: {spec['commit'][:12]}  [{spec['license']}]")


def main():
    sources = json.loads(CONFIG.read_text(encoding="utf-8"))
    names = sys.argv[1:] or list(sources)
    unknown = [n for n in names if n not in sources]
    if unknown:
        sys.exit(f"unknown source(s): {', '.join(unknown)}")
    DEST.mkdir(exist_ok=True)
    for name in names:
        fetch(name, sources[name])


if __name__ == "__main__":
    main()
