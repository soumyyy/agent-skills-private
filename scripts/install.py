#!/usr/bin/env python3
"""Install personal skills for Codex or Claude without replacing different files."""
import argparse
import os
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_NOTE = '''## Claude Code compatibility

Use `/skill-name` to invoke skills. Personal skills live in `~/.claude/skills/`; do not write personal Claude skills into Codex or plugin-cache directories. Use the current session's tools and authorization rules. Runtime references apply with these host-specific paths. Resolve supporting workflows from the available skills; if an authoring helper is unavailable, write a scoped SKILL.md directly rather than pretending to invoke it. Use project-scoped history or current conversation context when transcript access is unavailable. Never assume T3 tools or cross-provider model access exists in standalone Claude Code; council and sol-loop must report a missing exact-model route rather than substitute reviewers. References to prose unslopping mean plain-language editing, not the UI-only `unslop` workflow.

'''


def contents(folder):
    return {p.relative_to(folder): p.read_bytes() for p in folder.rglob('*') if p.is_file()}


def explicit_only(source):
    metadata = source / 'agents/openai.yaml'
    if not metadata.is_file():
        return False
    # Only inspect the top-level policy block; interface prose is not policy.
    match = re.search(r'^policy:\s*\n((?:[ \t]+[^\n]*\n|\s*\n)*)', metadata.read_text(), re.M)
    if not match:
        return False
    setting = re.search(r'^  allow_implicit_invocation:\s*(true|false)\s*(?:#.*)?$', match[1], re.M)
    if not setting:
        raise ValueError(f'Unsupported invocation policy in {metadata}')
    return setting[1] == 'false'


def claude_entrypoint(source, original):
    text = original.decode('utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError(f'Invalid frontmatter: {source / "SKILL.md"}')
    closing = text.index('\n---\n', 4)
    header, body = text[:closing], text[closing + 5:]
    if explicit_only(source):
        header = re.sub(r'^disable-model-invocation:.*\n?', '', header, flags=re.M)
        header = header.rstrip() + '\ndisable-model-invocation: true'
    return (header + '\n---\n\n' + CLAUDE_NOTE + body.lstrip('\n')).encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=['codex', 'claude'], default='codex')
    parser.add_argument('--dest', type=Path, help='Override the destination skills directory')
    parser.add_argument('--skills-dir', type=Path, default=ROOT / 'skills', help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.dest is not None:
        base = args.dest.expanduser()
    elif args.agent == 'claude':
        base = Path.home() / '.claude/skills'
    else:
        base = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
    sources = sorted(p for p in args.skills_dir.iterdir() if (p / 'SKILL.md').is_file())
    prepared = []
    # Preflight every skill before making any destination changes.
    for source in sources:
        expected = contents(source)
        if args.agent == 'claude':
            expected[Path('SKILL.md')] = claude_entrypoint(source, expected[Path('SKILL.md')])
        destination = base / source.name
        if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
            raise SystemExit(f'Refusing to replace existing path: {destination}')
        if destination.exists() and contents(destination) != expected:
            raise SystemExit(f'Refusing to replace different existing skill: {destination}')
        prepared.append((source, destination, expected))
    for source, destination, expected in prepared:
        if destination.exists():
            print(f'Already installed: {destination}')
            continue
        shutil.copytree(source, destination)
        if args.agent == 'claude':
            (destination / 'SKILL.md').write_bytes(expected[Path('SKILL.md')])
        print(f'Installed: {destination}')


if __name__ == '__main__':
    main()
