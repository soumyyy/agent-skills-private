"""Exercise generated Claude installs and preservation of existing user skills."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

INSTALLER = Path(__file__).resolve().parents[1] / 'scripts/install.py'


class InstallerTests(unittest.TestCase):
    def create_source(self, root, name, manual=False):
        folder = root / name
        folder.mkdir(parents=True)
        (folder / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Test workflow\n---\n\n# Workflow\n')
        if manual:
            (folder / 'agents').mkdir()
            (folder / 'agents/openai.yaml').write_text('policy:\n  allow_implicit_invocation: false\n')
        helper = folder / 'helper.py'
        helper.write_text('#!/usr/bin/env python3\n')
        helper.chmod(0o755)
        return folder

    def run_install(self, source, dest, agent='claude'):
        return subprocess.run([sys.executable, str(INSTALLER), '--agent', agent,
                               '--skills-dir', str(source), '--dest', str(dest)], capture_output=True, text=True)

    def test_claude_policy_repeat_install_and_source_preservation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, dest = root / 'source', root / 'dest'
            original = self.create_source(source, 'manual', manual=True)
            self.create_source(source, 'automatic')
            before = (original / 'SKILL.md').read_bytes()
            for _ in range(2):
                self.assertEqual(self.run_install(source, dest).returncode, 0)
            self.assertEqual((original / 'SKILL.md').read_bytes(), before)
            self.assertIn('disable-model-invocation: true', (dest / 'manual/SKILL.md').read_text())
            self.assertNotIn('disable-model-invocation: true', (dest / 'automatic/SKILL.md').read_text())
            self.assertTrue((dest / 'manual/helper.py').stat().st_mode & 0o111)
            codex = root / 'codex'
            self.assertEqual(self.run_install(source, codex, 'codex').returncode, 0)
            self.assertEqual((codex / 'manual/SKILL.md').read_bytes(), before)

    def test_late_conflict_leaves_earlier_missing_skill_uninstalled(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, dest = root / 'source', root / 'dest'
            self.create_source(source, 'a-first')
            self.create_source(source, 'z-conflict')
            (dest / 'z-conflict').mkdir(parents=True)
            custom = dest / 'z-conflict/SKILL.md'
            custom.write_text('user-owned work')
            self.assertNotEqual(self.run_install(source, dest).returncode, 0)
            self.assertFalse((dest / 'a-first').exists())
            self.assertEqual(custom.read_text(), 'user-owned work')

    def test_existing_symlink_is_not_followed_or_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, dest = root / 'source', root / 'dest'
            original = self.create_source(source, 'linked')
            dest.mkdir()
            (dest / 'linked').symlink_to(original, target_is_directory=True)
            before = (original / 'SKILL.md').read_bytes()
            self.assertNotEqual(self.run_install(source, dest).returncode, 0)
            self.assertTrue((dest / 'linked').is_symlink())
            self.assertEqual((original / 'SKILL.md').read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
