# Module Map

## Repository docs
- `AGENTS.md`: short boot map for Codex and other agents.
- `CLAUDE.md`: Claude Code-specific behavior layered on top of `AGENTS.md`.
- `docs/ai/`: memory policy, prompt protocol, context map, review checklist, and templates.
- `docs/runbooks/`: operational procedures.
- `docs/pitfalls/`: known failures and test caveats.

## Enforcement
- `.codex/hooks/pre_memory_write.py`: validates generated memory before writing.
- `scripts/check_agents_size.py`: keeps boot files under the configured line limit.
- `scripts/scan_memory_secrets.py`: scans memory inbox notes for forbidden patterns.
- `scripts/check_docs_links.py`: validates local Markdown links.

## External memory
- `~/Obsidian/AI-Memory-Vault/00-inbox/`: generated proposals and summaries.
- `~/Obsidian/AI-Memory-Vault/20-global/`: reviewed cross-project knowledge.
- `~/Obsidian/AI-Memory-Vault/90-archive/`: rejected or stale notes.
