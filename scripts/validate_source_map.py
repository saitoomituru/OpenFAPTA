#!/usr/bin/env python3
"""固定外部参照表の構造とURLの整合だけを検査する。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_MAP = ROOT / "references" / "source-map.json"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_FIELDS = {"id", "role", "repository", "revision", "path", "public_url", "required"}


def expected_url(source: dict[str, Any]) -> str:
    """sourceから固定GitHub blob URLを組み立てる。"""

    return (
        "https://github.com/saitoomituru/"
        f"{source['repository']}/blob/{source['revision']}/{source['path']}"
    )


def validate(data: dict[str, Any]) -> list[str]:
    """参照表を検査し、人が読める問題一覧を返す。"""

    errors: list[str] = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_versionは1.0でなければならない")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + ["sourcesは空でない配列でなければならない"]

    ids: set[str] = set()
    coordinates: set[tuple[str, str, str]] = set()
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label}はobjectでなければならない")
            continue
        missing = REQUIRED_FIELDS - source.keys()
        if missing:
            errors.append(f"{label}に必須fieldがない: {sorted(missing)}")
            continue
        source_id = source["id"]
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{label}.idは空でない文字列でなければならない")
        elif source_id in ids:
            errors.append(f"重複id: {source_id}")
        else:
            ids.add(source_id)
        revision = source["revision"]
        if not isinstance(revision, str) or not SHA_RE.fullmatch(revision):
            errors.append(f"{label}.revisionは40桁小文字SHAでなければならない")
        path_value = source["path"]
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"{label}.pathは空でない文字列でなければならない")
        else:
            path = PurePosixPath(path_value)
            if path.is_absolute() or ".." in path.parts:
                errors.append(f"{label}.pathは安全な相対pathでなければならない")
        if not isinstance(source["required"], bool):
            errors.append(f"{label}.requiredはbooleanでなければならない")
        coordinate = (str(source["repository"]), str(revision), str(path_value))
        if coordinate in coordinates:
            errors.append(f"重複source座標: {coordinate}")
        else:
            coordinates.add(coordinate)
        if source["public_url"] != expected_url(source):
            errors.append(f"{label}.public_urlがsource座標と一致しない")
    return errors


def main() -> int:
    """検査を実行して終了codeを返す。"""

    try:
        data = json.loads(SOURCE_MAP.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"SOURCE-BLOCK: source-mapを読めない: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"SOURCE-BLOCK: {error}", file=sys.stderr)
        return 1
    print(f"source-map OK: {len(data['sources'])} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
