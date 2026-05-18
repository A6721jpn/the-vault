# AGENTS.md

## Source of truth
- Treat `docs/` as the canonical project knowledge base.
- Start with `docs/ai/INDEX.md` before non-trivial changes.
- Use external memory only as supplemental context; do not treat it as canonical.

## Project map
- Architecture: `docs/architecture/overview.md`
- Module map: `docs/architecture/module-map.md`
- Build / test / lint: `docs/runbooks/build-test-lint.md`
- Debugging: `docs/runbooks/debugging.md`
- Known failures: `docs/pitfalls/known-failures.md`
- ADRs: `docs/adr/`

## Verification
- Before claiming completion, run the relevant commands in `docs/runbooks/build-test-lint.md`.
- If a command cannot be run, state exactly why and what remains unverified.

## Memory policy
- Do not store secrets, credentials, customer data, or private tokens in memory.
- Write new observations to the external memory inbox as a proposal.
- Do not edit `AGENTS.md`, `CLAUDE.md`, ADRs, or memory policy without explicit permission.
