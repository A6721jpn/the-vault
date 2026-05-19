# Prototype Evaluation Report

## Date
2026-05-18

## Environment
- Repository root: `C:/github_repo/the-vault`
- External vault: `C:/Users/aokuni/Obsidian/AI-Memory-Vault`
- MCP runtime: verified through Basic Memory 0.21.1 installed as a user tool.
- Basic Memory project: `codex-vault`
- Codex user config: `C:/Users/aokuni/.codex/config.toml`

## Checks run
- `python -m unittest tests/test_memory_kernel_scripts.py`: pass
- `python scripts/check_agents_size.py`: pass
- `python scripts/scan_memory_secrets.py C:/Users/aokuni/Obsidian/AI-Memory-Vault/00-inbox`: pass
- `python scripts/check_docs_links.py docs`: pass
- `python .codex/hooks/pre_memory_write.py AI-Memory-Vault/00-inbox/memory-proposals/2026-05-18-prototype-smoke-test.md C:/Users/aokuni/Obsidian/AI-Memory-Vault/00-inbox/memory-proposals/2026-05-18-prototype-smoke-test.md`: pass

## Scenario status
- Scenario 1: prepared, not run against a real agent task.
- Scenario 2: prepared, smoke-test proposal created.
- Scenario 3: covered by automated guard and secret scan tests.
- Scenario 4: prepared, not run against an MCP memory note.
- Scenario 5: prepared, review command documented.

## Remaining gaps
- Restart Codex and confirm the newly configured `basic-memory` MCP tools are visible in the active tool list.
- Run the five evaluation scenarios with a baseline agent session and a memory-enabled session.
- Promote or archive the smoke-test proposal after human review.

## 2026-05-19 connection update

- Installed `uv` as a user Python tool.
- Installed Basic Memory 0.21.1.
- Added Basic Memory project `codex-vault` at `C:/Users/aokuni/Obsidian/AI-Memory-Vault`.
- Set `codex-vault` as the default project.
- Added `basic-memory` MCP server to `C:/Users/aokuni/.codex/config.toml`.
- Added global memory instructions to `C:/Users/aokuni/.codex/AGENTS.md`.
- Reindexed the vault.
- Verified `search-notes`, `read-note`, and `write-note`.
