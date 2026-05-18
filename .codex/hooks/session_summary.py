from datetime import date


def render_session_summary(project: str, title: str, agent: str = "codex") -> str:
    today = date.today().isoformat()
    return f"""---
type: session-summary
project: {project}
created: {today}
agent: {agent}
status: generated
sensitivity: low
---

# Session Summary: {title}

## Goal
<Original task.>

## Changes made
- <Changed file or behavior>

## Commands run
- `<command>`: pass | fail | not run

## Key findings
- <Finding>

## Memory delta
### Promote to docs
- <Candidate item>

### Keep as working memory
- <Candidate item>

### Discard
- <Temporary or low-confidence item>

## Unresolved questions
- <Question>
"""


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Render a session summary template.")
    parser.add_argument("--project", default="the-vault")
    parser.add_argument("--title", default="Untitled task")
    parser.add_argument("--agent", default="codex")
    args = parser.parse_args()

    print(render_session_summary(args.project, args.title, args.agent), end="")
