#!/usr/bin/env python3
"""Scan frontend files for common responsive UI issues."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HTML_EXTENSIONS = {".html", ".tsx", ".jsx", ".vue"}
CSS_EXTENSIONS = {".css", ".scss", ".module.css"}
ALL_EXTENSIONS = HTML_EXTENSIONS | CSS_EXTENSIONS

ISSUE = tuple[str, int, str, str]


def scan_html_like(path: Path, text: str) -> list[ISSUE]:
    issues: list[ISSUE] = []
    lines = text.splitlines()

    has_viewport = "viewport" in text.lower()
    if path.suffix in HTML_EXTENSIONS and not has_viewport and "<html" in text.lower():
        issues.append((str(path), 0, "warning", "Missing viewport meta tag"))

    for line_no, line in enumerate(lines, start=1):
        if re.search(r"width:\s*100vw\b", line):
            issues.append((str(path), line_no, "warning", "100vw may cause horizontal scroll (scrollbar width)"))
        if re.search(r"overflow-x:\s*hidden\b", line) and "TODO" not in line:
            issues.append((str(path), line_no, "info", "overflow-x:hidden masks layout issues; fix root cause"))
        if re.search(r"min-(?:width|height):\s*\d+px\b", line) and "44px" not in line and "48px" not in line:
            if re.search(r"min-(?:width|height):\s*(?:2[0-9]|[0-9])px\b", line):
                issues.append((str(path), line_no, "warning", "Touch target may be below 44px minimum"))

    return issues


def scan_css(path: Path, text: str) -> list[ISSUE]:
    issues: list[ISSUE] = []
    lines = text.splitlines()

    has_reduced_motion = "prefers-reduced-motion" in text
    if path.suffix in CSS_EXTENSIONS and not has_reduced_motion and "@keyframes" in text:
        issues.append((str(path), 0, "info", "Animations present but no prefers-reduced-motion handling"))

    for line_no, line in enumerate(lines, start=1):
        if re.search(r"@media\s*\(\s*max-width", line):
            issues.append((str(path), line_no, "info", "Desktop-first max-width media query; prefer min-width (mobile-first)"))

    issues.extend(scan_html_like(path, text))
    return issues


def scan_file(path: Path) -> list[ISSUE]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [(str(path), 0, "critical", f"Cannot read file: {exc}")]

    if path.suffix in CSS_EXTENSIONS:
        return scan_css(path, text)
    if path.suffix in HTML_EXTENSIONS:
        return scan_html_like(path, text)
    return []


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix in ALL_EXTENSIONS else []
    skip = {"node_modules", "dist", "build", ".next"}
    return [
        p for p in target.rglob("*")
        if p.suffix in ALL_EXTENSIONS and not any(part in skip for part in p.parts)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate responsive UI patterns in frontend files")
    parser.add_argument("target", nargs="?", default=".", help="File or directory to scan")
    args = parser.parse_args()

    target = Path(args.target)
    files = collect_files(target)
    if not files:
        print("No files found (.html, .tsx, .jsx, .vue, .css, .scss)")
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
