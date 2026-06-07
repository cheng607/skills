#!/usr/bin/env python3
"""Scan frontend component files for common accessibility and API issues."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EXTENSIONS = {".tsx", ".jsx", ".vue", ".svelte"}
ISSUE = tuple[str, int, str, str]  # file, line, severity, message

PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    (
        "critical",
        "Interactive div without role",
        re.compile(r"<div[^>]*\bonClick\b(?![^>]*\brole=)", re.I),
    ),
    (
        "critical",
        "Interactive span without role",
        re.compile(r"<span[^>]*\bonClick\b(?![^>]*\brole=)", re.I),
    ),
    (
        "warning",
        "Button missing type attribute",
        re.compile(r"<button(?![^>]*\btype=)[^>]*>", re.I),
    ),
    (
        "warning",
        "Image may be missing alt",
        re.compile(r"<img(?![^>]*\balt=)[^>]*/?>", re.I),
    ),
    (
        "warning",
        "Array index used as key",
        re.compile(r"\bkey=\{(?:index|i|idx)\}"),
    ),
    (
        "info",
        "Large component file (>300 lines)",
        re.compile(r"."),  # handled separately
    ),
]


def scan_file(path: Path) -> list[ISSUE]:
    issues: list[ISSUE] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [(str(path), 0, "critical", f"Cannot read file: {exc}")]

    lines = text.splitlines()
    if len(lines) > 300:
        issues.append((str(path), 300, "info", f"File has {len(lines)} lines; consider splitting"))

    for line_no, line in enumerate(lines, start=1):
        for severity, message, pattern in PATTERNS[:-1]:
            if pattern.search(line):
                issues.append((str(path), line_no, severity, message))

    return issues


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix in EXTENSIONS else []
    return [p for p in target.rglob("*") if p.suffix in EXTENSIONS and "node_modules" not in p.parts]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate frontend component files")
    parser.add_argument("target", nargs="?", default=".", help="File or directory to scan")
    args = parser.parse_args()

    target = Path(args.target)
    files = collect_files(target)
    if not files:
        print("No component files found (.tsx, .jsx, .vue, .svelte)")
        return 0

    all_issues: list[ISSUE] = []
    for file in files:
        all_issues.extend(scan_file(file))

    severity_order = {"critical": 0, "warning": 1, "info": 2}
    all_issues.sort(key=lambda x: (severity_order.get(x[2], 9), x[0], x[1]))

    for file, line, severity, message in all_issues:
        loc = f"{file}:{line}" if line else file
        print(f"[{severity.upper()}] {loc} — {message}")

    critical_count = sum(1 for i in all_issues if i[2] == "critical")
    print(f"\nScanned {len(files)} file(s), {len(all_issues)} issue(s), {critical_count} critical")
    return 1 if critical_count else 0


if __name__ == "__main__":
    sys.exit(main())
