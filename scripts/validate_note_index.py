#!/usr/bin/env python3
"""公開Noteマイニング索引の構造を検査する。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "references" / "note-mining-index.json"
KEY_RE = re.compile(r"^n[0-9a-f]{12}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
RELATIONS = {"direct", "composite", "direct-and-composite"}
REQUIRED_ISSUES = set(range(1, 7))


def validate(data: dict[str, Any]) -> list[str]:
    """索引の必須fieldとIssue導線を検査する。"""

    errors: list[str] = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_versionは1.0でなければならない")
    articles = data.get("articles")
    if not isinstance(articles, list) or not articles:
        return errors + ["articlesは空でない配列でなければならない"]

    keys: set[str] = set()
    covered_issues: set[int] = set()
    for index, article in enumerate(articles):
        label = f"articles[{index}]"
        if not isinstance(article, dict):
            errors.append(f"{label}はobjectでなければならない")
            continue
        key = article.get("key")
        if not isinstance(key, str) or not KEY_RE.fullmatch(key):
            errors.append(f"{label}.keyはNote記事keyでなければならない")
            continue
        if key in keys:
            errors.append(f"重複key: {key}")
        keys.add(key)
        expected_url = f"https://note.com/fusamofu326/n/{key}"
        if article.get("url") != expected_url:
            errors.append(f"{label}.urlがkeyと一致しない")
        digest = article.get("body_sha256")
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"{label}.body_sha256は64桁小文字SHA-256でなければならない")
        if article.get("evidence_relation") not in RELATIONS:
            errors.append(f"{label}.evidence_relationが未登録")
        issues = article.get("related_issues")
        if not isinstance(issues, list) or not issues:
            errors.append(f"{label}.related_issuesは空でない配列でなければならない")
        elif any(not isinstance(issue, int) or issue not in REQUIRED_ISSUES for issue in issues):
            errors.append(f"{label}.related_issuesに対象外Issueがある")
        else:
            covered_issues.update(issues)
    missing_issues = REQUIRED_ISSUES - covered_issues
    if missing_issues:
        errors.append(f"未接続Issue: {sorted(missing_issues)}")
    return errors


def main() -> int:
    """索引検査を実行して終了codeを返す。"""

    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"NOTE-SOURCE-BLOCK: 索引を読めない: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"NOTE-SOURCE-BLOCK: {error}", file=sys.stderr)
        return 1
    print(f"note-mining-index OK: {len(data['articles'])} articles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
