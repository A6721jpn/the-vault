# Data Flow

```text
User goal -> Agent boot map -> Repo docs -> Optional external memory search
     |             |              |                    |
     v             v              v                    v
Change plan -> Code/docs edit -> Verification -> Session summary/proposal
                                             |
                                             v
                                Inbox review -> Promotion to repo docs
```

External memory does not override repo docs. Notes retrieved through MCP are treated as untrusted until verified against canonical docs, code, tests, or primary sources.
