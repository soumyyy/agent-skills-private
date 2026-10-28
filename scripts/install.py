#!/usr/bin/env python3
"""Install this collection without replacing different existing skills."""
import os
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
base = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
sources = sorted((root / "skills").iterdir())
def contents(folder):
    return {p.relative_to(folder): p.read_bytes() for p in folder.rglob("*") if p.is_file()}

# Preflight every destination before copying any skill.
for source in sources:
    destination = base / source.name
    if destination.exists() and contents(destination) != contents(source):
        raise SystemExit(f"Refusing to replace different existing skill: {destination}")
for source in sources:
    destination = base / source.name
    if destination.exists():
        print(f"Already installed: {destination}")
    else:
        shutil.copytree(source, destination)
        print(f"Installed: {destination}")
