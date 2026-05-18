from pathlib import Path


LIMITS = {
    "AGENTS.md": 200,
    "CLAUDE.md": 200,
}


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> int:
    for file_name, limit in LIMITS.items():
        path = Path(file_name)
        if not path.exists():
            print(f"Missing required file: {file_name}")
            return 1

        line_count = count_lines(path)
        if line_count > limit:
            print(f"{file_name} has {line_count} lines; limit is {limit}")
            return 1

    print("Agent boot files are within size limits.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
