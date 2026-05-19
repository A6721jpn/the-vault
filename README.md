# the-vault

Agent Memory Kernel prototype for coordinating repo-local canonical docs with an external Obsidian-compatible memory vault.

## What is here
- `AGENTS.md` and `CLAUDE.md`: short agent boot maps.
- `docs/`: canonical project docs, memory policy, runbooks, pitfall notes, templates, and evaluation material.
- `.codex/`: Codex config example and memory-write hooks.
- `.claude/`: Claude Code rules and command prompts.
- `scripts/`: validation scripts for boot file size, docs links, and memory safety.
- `tests/`: Python standard library tests for the validation scripts and memory guard.

## Visual guide
Open `docs/usage-guide.html` in a browser for a diagram-based usage guide.

## External vault
The prototype expects an Obsidian-compatible vault at:

`C:/Users/aokuni/Obsidian/AI-Memory-Vault`

Generated agent notes should be written only under `00-inbox/` and reviewed before promotion into canonical repo docs.

Natural-language notes in the vault should be written in Japanese by default. English is fine for code identifiers, file paths, commands, product names, logs, and short technical terms.

Human development decisions can be recorded with criteria, options, result, impact, and review conditions. See `docs/ai/DECISION_LOG_POLICY.md`.

Promotion from external memory into canonical repo docs follows `docs/ai/PROMOTION_PLAYBOOK.md`.

Codex connection details are documented in `docs/ai/CODEX_CONNECTION.md`.

## Validation
Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -m unittest tests/test_memory_kernel_scripts.py
python scripts/check_agents_size.py
python scripts/scan_memory_secrets.py C:/Users/aokuni/Obsidian/AI-Memory-Vault/00-inbox
python scripts/check_docs_links.py docs
```

MCP server startup is environment-dependent. `.codex/config.example.toml` documents the intended Basic Memory-style configuration, but the local environment must provide `uvx` or an equivalent MCP server command.
