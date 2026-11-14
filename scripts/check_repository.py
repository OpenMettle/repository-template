#!/usr/bin/env python3
"""Dependency-free repository hygiene checks; not a replacement for secret scanning or application tests."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_KEY = re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")
TOKEN = re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})\b")
ACTION = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
FORBIDDEN_NAMES = {".env", "id_rsa", "id_ed25519", "kubeconfig", "terraform.tfstate", "terraform.tfstate.backup"}


def tracked_files():
    result = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True)
    if result.returncode == 0:
        return [ROOT / name.decode() for name in result.stdout.split(b"\0") if name]
    # Allows checking the unpacked starter before its first commit.
    return [p for p in ROOT.rglob("*") if p.is_file() and not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)]


def check():
    errors = []
    files = tracked_files()
    for path in files:
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            errors.append(f"{relative}: symlinks require a project-specific review policy")
            continue
        if path.name in FORBIDDEN_NAMES or path.name.endswith((".key", ".pem", ".tfstate", ".tfstate.backup")):
            errors.append(f"{relative}: local credentials or runtime state do not belong in source control")
            continue
        data = path.read_bytes()
        if b"\0" in data:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if data and not data.endswith(b"\n"):
            errors.append(f"{relative}: missing final newline")
        if b"\r\n" in data:
            errors.append(f"{relative}: use LF line endings")
        if PRIVATE_KEY.search(text) or TOKEN.search(text):
            errors.append(f"{relative}: possible credential; remove it and assess whether it needs rotation")
        if relative.parts[:2] == (".github", "workflows") or relative.parts[0] == "workflow-templates":
            for action in ACTION.findall(text):
                action = action.strip("\"'")
                if not action.startswith("./") and not re.fullmatch(r"[\w.-]+/[\w./-]+@[0-9a-f]{40}", action):
                    errors.append(f"{relative}: external actions must be pinned to full commit SHAs")
    for name in ("README.md", "LICENSE"):
        if not (ROOT / name).is_file():
            errors.append(f"{name}: required")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Repository hygiene passed ({len(files)} files). Add component-specific tests as code is introduced.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
