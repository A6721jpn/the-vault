# General Claude Rules

- Treat repo `docs/` as canonical.
- Treat auto memory as generated and unreviewed.
- Before using external memory, prefer repo docs.
- Do not write generated memory outside `00-inbox/`.
- If a rule must be enforced, propose a hook or CI check instead of relying on memory.
