import argparse
import re
from pathlib import Path
from urllib.parse import unquote


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def is_external_target(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("#")
    )


def normalize_target(target: str) -> str:
    target = target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target.split("#", 1)[0])


def markdown_files(root: Path):
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return
    yield from root.rglob("*.md")


def check_links(root: Path):
    failures = []
    for source in markdown_files(root):
        content = source.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            raw_target = match.group(1)
            if is_external_target(raw_target):
                continue
            target = normalize_target(raw_target)
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                failures.append((source, raw_target))
    return failures


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown links under a docs directory.")
    parser.add_argument("path", nargs="?", default="docs")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.exists():
        print(f"Missing docs path: {root}")
        return 1

    failures = check_links(root)
    if failures:
        for source, target in failures:
            print(f"{source}: missing link target: {target}")
        return 1

    print("All local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
