@AGENTS.md

## Claude Code behavior
- For non-trivial changes, first summarize relevant files and propose a plan.
- Use `.claude/rules/` for path-specific conventions.
- If the same correction appears twice, propose a memory update in the external memory inbox.
- Write external memory notes in Japanese by default, except for identifiers, commands, paths, product names, logs, and short terms.
- Use hooks, tests, and CI for hard enforcement; do not rely on memory as a hard rule.
