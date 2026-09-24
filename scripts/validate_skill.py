#!/usr/bin/env python3
"""Integrity check for the awesome-bug-bounty skill package.

Verifies: frontmatter, bundled knowledge files, relative paths referenced
from SKILL.md, README local links, and (optionally) drift between the repo
package and an installed copy under ~/.config/opencode/skills/.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "awesome-bug-bounty"
SKILL_MD = SKILL_DIR / "SKILL.md"
README = ROOT / "README.md"
KNOWLEDGE = [
    "vuln-types.md",
    "payloads.md",
    "business-logic.md",
    "methodology.md",
    "tools.md",
    "install.md",
]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PATH_RE = re.compile(r"`(knowledge/[A-Za-z0-9._-]+)`")
MAX_DESCRIPTION_CHARS = 600

errors: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def check_frontmatter() -> None:
    if not SKILL_MD.exists():
        err(f"missing {SKILL_MD.relative_to(ROOT)}")
        return
    text = SKILL_MD.read_text(encoding="utf-8")
    if not (text.startswith("---") and text.count("---") >= 2):
        err("SKILL.md missing YAML frontmatter")
        return
    meta = text.split("---", 2)[1]
    if not re.search(r"(?m)^name:\s*\S", meta):
        err("frontmatter missing name")
    m = re.search(r"(?m)^description:\s*(.+)$", meta)
    if not m:
        err("frontmatter missing description")
    else:
        desc = m.group(1).strip().strip('"')
        if len(desc) > MAX_DESCRIPTION_CHARS:
            err(
                f"description too long: {len(desc)} chars "
                f"(max {MAX_DESCRIPTION_CHARS}) — triggers only; behavior belongs in the body"
            )


def check_knowledge_bundled() -> None:
    for name in KNOWLEDGE:
        path = SKILL_DIR / "knowledge" / name
        if not path.exists():
            err(f"missing bundled knowledge file: skills/awesome-bug-bounty/knowledge/{name}")
        elif path.stat().st_size == 0:
            err(f"empty knowledge file: {name}")
    stray = ROOT / "knowledge"
    if stray.exists():
        err("top-level knowledge/ still exists — it must live inside the skill package")


def check_skill_paths() -> None:
    if not SKILL_MD.exists():
        return
    text = SKILL_MD.read_text(encoding="utf-8")
    for match in PATH_RE.finditer(text):
        rel = match.group(1)
        if not (SKILL_DIR / rel).exists():
            err(f"SKILL.md references missing path: {rel}")


def check_readme_links() -> None:
    if not README.exists():
        err("missing README.md")
        return
    text = README.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (README.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            err(f"README link escapes repo: {match.group(1)}")
            continue
        if not resolved.exists():
            err(f"broken README link: {match.group(1)}")


def check_installed_drift() -> None:
    installed = Path.home() / ".config" / "opencode" / "skills" / "awesome-bug-bounty"
    if not installed.exists():
        return
    if installed.is_symlink():
        if installed.resolve() != SKILL_DIR.resolve():
            err(f"installed symlink points elsewhere: {installed} -> {installed.resolve()}")
        return
    if not SKILL_MD.exists():
        return
    installed_skill = installed / "SKILL.md"
    if not installed_skill.exists():
        err(f"installed copy missing SKILL.md: {installed}")
        return
    if installed_skill.read_text(encoding="utf-8") != SKILL_MD.read_text(encoding="utf-8"):
        err(
            f"installed skill drifts from repo: {installed} — "
            "replace it with a symlink: ln -sfn "
            f"{SKILL_DIR} {installed}"
        )
    if not (installed / "knowledge").exists():
        err(f"installed copy has no bundled knowledge/: {installed}")


def main() -> int:
    check_frontmatter()
    check_knowledge_bundled()
    check_skill_paths()
    check_readme_links()
    check_installed_drift()
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        return 1
    print("skill package validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
