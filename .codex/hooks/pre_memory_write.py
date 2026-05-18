import re
from pathlib import PurePosixPath


class Blocked(Exception):
    """Raised when generated memory is unsafe to write."""


INBOX_PREFIX = PurePosixPath("AI-Memory-Vault/00-inbox")

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


def _normalize_note_path(note_path: str) -> PurePosixPath:
    normalized = note_path.replace("\\", "/")
    marker = "AI-Memory-Vault/"
    if marker in normalized:
        normalized = normalized[normalized.index(marker) :]
    return PurePosixPath(normalized)


def _is_in_inbox(note_path: PurePosixPath) -> bool:
    return note_path == INBOX_PREFIX or INBOX_PREFIX in note_path.parents


def _has_phone_number(note_content: str) -> bool:
    for match in PHONE_CANDIDATE_PATTERN.finditer(note_content):
        digits = re.sub(r"\D", "", match.group(0))
        if len(digits) >= 10:
            return True
    return False


def pre_memory_write(note_path: str, note_content: str) -> bool:
    path = _normalize_note_path(note_path)
    if not _is_in_inbox(path):
        raise Blocked("Agents may only write generated memory to AI-Memory-Vault/00-inbox.")

    for name, pattern in FORBIDDEN_PATTERNS:
        if pattern.search(note_content):
            raise Blocked(f"Potential sensitive content detected: {name}. Do not store this in memory.")

    if _has_phone_number(note_content):
        raise Blocked("Potential sensitive content detected: phone_number. Do not store this in memory.")

    if re.search(r"(?im)^\s*status\s*:\s*canonical\s*$", note_content):
        raise Blocked("Generated memory cannot mark itself as canonical.")

    return True


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Validate a generated memory note before writing.")
    parser.add_argument("note_path")
    parser.add_argument("content_file")
    args = parser.parse_args()

    content = Path(args.content_file).read_text(encoding="utf-8")
    try:
        pre_memory_write(args.note_path, content)
    except Blocked as exc:
        raise SystemExit(str(exc))

    print("Memory write is allowed.")
