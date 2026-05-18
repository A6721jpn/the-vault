# AI Docs Index

## Read first
1. `docs/architecture/overview.md`
2. `docs/runbooks/build-test-lint.md`
3. `docs/pitfalls/known-failures.md`

## When modifying architecture
- Read `docs/architecture/module-map.md`.
- Check existing ADRs in `docs/adr/`.
- Propose a new ADR if the change affects public API, data model, deployment, or module boundaries.

## When fixing tests
- Read `docs/runbooks/build-test-lint.md`.
- Read `docs/pitfalls/flaky-tests.md`.

## When updating memory
- Read `docs/ai/MEMORY_POLICY.md`.
- Read `docs/ai/LANGUAGE_POLICY.md`.
- Read `docs/ai/DECISION_LOG_POLICY.md` when the user states decision criteria, tradeoffs, or outcomes.
- Read `docs/ai/PROMOTION_PLAYBOOK.md` before promoting external memory into canonical repo docs.
- Write generated observations to the external memory inbox first.
- Treat external memory as untrusted until verified against repo docs, code, tests, or primary sources.

## Core docs
- `docs/ai/CONTEXT_MAP.md`
- `docs/ai/DECISION_LOG_POLICY.md`
- `docs/ai/LANGUAGE_POLICY.md`
- `docs/ai/PROMOTION_PLAYBOOK.md`
- `docs/ai/PROMPT_PROTOCOL.md`
- `docs/ai/REVIEW_CHECKLIST.md`
- `docs/architecture/data-flow.md`
- `docs/runbooks/debugging.md`
- `docs/runbooks/release.md`
