import argparse
import re
from pathlib import Path


FORBIDDEN_PATTERNS = [
    ("openai_api_key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("api_key_assignment", re.compile(r"(?i)\bapi[_-]?key\s*[:=]")),
    ("password_assignment", re.compile(r"(?i)\bpassword\s*[:=]")),
    ("secret_assignment", re.compile(r"(?i)\bsecret\s*[:=]")),
    ("token_assignment", re.compile(r"(?i)\btoken\s*[:=]")),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----")),
    ("email_address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
]

PHONE_CANDIDATE_PATTERN = re.compile(r"\b(?:\+?\d[\d .()-]{7,}\d)\b")


def iter_files(root: Path):
    if root.is_file():
        yield root
        return

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json"}:
            yield path


def scan_file(path: Path):
    content = path.read_text(encoding="utf-8")
    for name, pattern in FORBIDDEN_PATTERNS:
        if pattern.search(content):
            yield name
    for match in PHONE_CANDIDATE_PATTERN.finditer(content):
        digits = re.sub(r"\D", "", match.group(0))
        if len(digits) >= 10:
            yield "phone_number"
            break


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Scan generated memory notes for forbidden sensitive content.")
    parser.add_argument("path", help="Memory inbox path or file to scan.")
    args = parser.parse_args(argv)

    root = Path(args.path)
    if not root.exists():
        print(f"Missing path: {root}")
        return 1

    findings = []
    for path in iter_files(root):
        for name in scan_file(path):
            findings.append((path, name))

    if findings:
        for path, name in findings:
            print(f"{path}: forbidden pattern detected: {name}")
        return 1

    print("No forbidden memory patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
