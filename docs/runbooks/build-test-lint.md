# Build / Test / Lint Runbook

## Install
No package install is required for the current prototype. It uses Python standard library tests.

## Build
No build step is required.

## Unit tests
`python -m unittest tests/test_memory_kernel_scripts.py`

## Lint
No linter is configured yet.

## Type check
No type checker is configured yet.

## Validation scripts
- `python scripts/check_agents_size.py`
- `python scripts/scan_memory_secrets.py C:/Users/aokuni/Obsidian/AI-Memory-Vault/00-inbox`
- `python scripts/check_docs_links.py docs`

## Notes for agents
- Run only relevant commands for the changed area when the full suite is too expensive.
- If a command cannot be run, state why.
- Never claim tests passed unless the command was actually run and passed.
