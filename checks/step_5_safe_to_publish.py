"""Safe to publish: no keys or secrets in the repository"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}")
SKIP = {".git", ".venv", "venv", "__pycache__", "node_modules"}


def test_no_api_key_in_files():
    """No API key appears in any file"""
    for path in ROOT.rglob("*"):
        if path.is_file() and not SKIP & set(path.relative_to(ROOT).parts) and path.stat().st_size < 2_000_000:
            text = path.read_text(encoding="utf-8", errors="ignore")
            assert not KEY.search(text), f"{path.relative_to(ROOT)} holds an API key. Delete it, revoke the key and use a secret."


def test_env_file_ignored():
    """.gitignore keeps .env files out of Git"""
    ignore = ROOT / ".gitignore"
    assert ignore.exists() and ".env" in ignore.read_text(encoding="utf-8").split(), "Add .env to .gitignore."
