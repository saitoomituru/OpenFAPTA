"""公開Noteマイニング索引の回帰検査。"""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_note_index.py"
SPEC = importlib.util.spec_from_file_location("validate_note_index", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NoteIndexTest(unittest.TestCase):
    """Note索引の構造とIssue導線を検査する。"""

    def setUp(self) -> None:
        """正本索引を読む。"""

        self.data = json.loads(
            (ROOT / "references" / "note-mining-index.json").read_text(encoding="utf-8")
        )

    def test_index_is_valid(self) -> None:
        """正本索引がvalidatorを通る。"""

        self.assertEqual([], MODULE.validate(self.data))

    def test_all_current_issues_are_covered(self) -> None:
        """Issue #1〜#6が少なくとも一つの原稿候補へ接続される。"""

        covered = {
            issue
            for article in self.data["articles"]
            for issue in article["related_issues"]
        }
        self.assertEqual(set(range(1, 7)), covered)

    def test_url_drift_is_rejected(self) -> None:
        """Note keyと一致しないURLを拒否する。"""

        broken = json.loads(json.dumps(self.data))
        broken["articles"][0]["url"] = "https://example.invalid"
        self.assertTrue(any("url" in error for error in MODULE.validate(broken)))


if __name__ == "__main__":
    unittest.main()
