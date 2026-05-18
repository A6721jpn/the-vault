# Architecture Overview

Agent Memory Kernel separates durable project knowledge from generated working memory.

The repository `docs/` directory is the canonical knowledge base. External memory, such as an Obsidian-compatible vault served through MCP, is a supplemental workspace for search, proposals, session summaries, and cross-project notes.

Generated notes enter the memory inbox first. A human or review agent can later promote useful notes into repo docs, ADRs, runbooks, or pitfall docs after checking evidence and sensitivity.
