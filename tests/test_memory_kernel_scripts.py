import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_hook_module():
    hook_path = REPO_ROOT / ".codex" / "hooks" / "pre_memory_write.py"
    spec = importlib.util.spec_from_file_location("pre_memory_write", hook_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PreMemoryWriteTests(unittest.TestCase):
    def test_allows_safe_note_in_inbox(self):
        hook = load_hook_module()

        self.assertTrue(
            hook.pre_memory_write(
                "AI-Memory-Vault/00-inbox/memory-proposals/test.md",
                "---\nstatus: proposed\n---\n# Safe note\nNo sensitive data.",
            )
        )

    def test_blocks_writes_outside_inbox(self):
        hook = load_hook_module()

        with self.assertRaises(hook.Blocked):
            hook.pre_memory_write(
                "AI-Memory-Vault/20-global/tool-notes.md",
                "# Note\nGenerated agents cannot write here.",
            )

    def test_blocks_secret_like_content(self):
        hook = load_hook_module()

        with self.assertRaises(hook.Blocked):
            hook.pre_memory_write(
                "AI-Memory-Vault/00-inbox/memory-proposals/test.md",
                "api_key = example",
            )

    def test_blocks_generated_canonical_status(self):
        hook = load_hook_module()

        with self.assertRaises(hook.Blocked):
            hook.pre_memory_write(
                "AI-Memory-Vault/00-inbox/memory-proposals/test.md",
                "---\nstatus: canonical\n---",
            )

    def test_allows_dates_and_file_paths_in_safe_evidence(self):
        hook = load_hook_module()

        self.assertTrue(
            hook.pre_memory_write(
                "AI-Memory-Vault/00-inbox/memory-proposals/2026-05-18-test.md",
                "Session date: `2026-05-18`\nRelated file: `C:/repo/file.md`",
            )
        )


class ValidationScriptTests(unittest.TestCase):
    def run_script(self, script_name, *args, cwd=None):
        script = REPO_ROOT / "scripts" / script_name
        return subprocess.run(
            [sys.executable, str(script), *map(str, args)],
            cwd=cwd or REPO_ROOT,
            text=True,
            capture_output=True,
        )

    def test_check_agents_size_accepts_short_boot_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
            (root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")

            result = self.run_script("check_agents_size.py", cwd=root)

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("within size limits", result.stdout)

    def test_check_agents_size_rejects_oversized_boot_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("\n".join(["x"] * 201), encoding="utf-8")
            (root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")

            result = self.run_script("check_agents_size.py", cwd=root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("AGENTS.md has 201 lines", result.stderr + result.stdout)

    def test_scan_memory_secrets_detects_forbidden_patterns(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inbox = root / "AI-Memory-Vault" / "00-inbox"
            inbox.mkdir(parents=True)
            (inbox / "safe.md").write_text("# Safe\nNo secrets here.", encoding="utf-8")
            (inbox / "unsafe.md").write_text("token: example", encoding="utf-8")

            result = self.run_script("scan_memory_secrets.py", inbox)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsafe.md", result.stderr + result.stdout)

    def test_scan_memory_secrets_allows_dates_and_file_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inbox = root / "AI-Memory-Vault" / "00-inbox"
            inbox.mkdir(parents=True)
            (inbox / "safe.md").write_text(
                "Session date: `2026-05-18`\nRelated file: `C:/repo/file.md`",
                encoding="utf-8",
            )

            result = self.run_script("scan_memory_secrets.py", inbox)

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_check_docs_links_rejects_missing_internal_markdown_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text(
                "[Good](./target.md)\n[Missing](./missing.md)\n",
                encoding="utf-8",
            )
            (docs / "target.md").write_text("# Target\n", encoding="utf-8")

            result = self.run_script("check_docs_links.py", docs)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing.md", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
