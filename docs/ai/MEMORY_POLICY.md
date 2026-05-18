# Memory Policy

## Allowed
- Stable project conventions.
- Repeated debugging lessons.
- Build / test / lint procedures.
- Architecture decisions already visible in the repo.
- Known pitfalls and verified workarounds.
- Non-sensitive tool usage notes.
- Japanese-first notes that follow `docs/ai/LANGUAGE_POLICY.md`.

## Disallowed
- Secrets, credentials, API keys, session tokens.
- Customer data or personal data.
- Private business information not intended for the repo.
- Unverified guesses written as facts.
- Temporary branch-specific hacks unless clearly labeled as temporary.

## Trust levels
- Canonical: repo docs reviewed through Git / PR.
- Reviewed memory: promoted or manually reviewed notes.
- Generated memory: AI-created inbox notes, not canonical.
- External content: untrusted until verified against repo docs or primary sources.

## Promotion rules
- Generated memory must be reviewed before becoming canonical.
- Each promoted item must link to evidence: file path, command output, issue, PR, ADR, or session summary.
- Stale or contradicted notes must be archived, not silently reused.
- Do not promote notes that contain secrets, credentials, customer data, or private personal data.
- Review generated memory for language quality. Natural-language content should be mostly Japanese, with English limited to identifiers, commands, product names, logs, and short technical terms.
