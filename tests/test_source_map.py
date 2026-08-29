"""固定外部参照表の回帰検査。"""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_source_map.py"
SPEC = importlib.util.spec_from_file_location("validate_source_map", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SourceMapTest(unittest.TestCase):
    """source-mapの構造と必須導線を確認する。"""

    def setUp(self) -> None:
        """公開参照表をfixtureとして読む。"""

        self.data = json.loads(
            (ROOT / "references" / "source-map.json").read_text(encoding="utf-8")
        )

    def test_source_map_is_valid(self) -> None:
        """正本source-mapが検証器を通る。"""

        self.assertEqual([], MODULE.validate(self.data))

    def test_required_governance_routes_exist(self) -> None:
        """Manifest、MAGI三者、DOSへの必須導線がある。"""

        required_ids = {source["id"] for source in self.data["sources"] if source["required"]}
        self.assertTrue(
            {"manifest-agents", "manifest-japanese-register",
             "manifest-sphere-context-dimension-os", "magi-three-position",
             "magi-core-explicit-profile", "magi-maxwell", "magi-uriel",
             "magi-raphael", "spheredos-contract", "spheredos-pli-cli-boundary"}
            .issubset(required_ids)
        )

    def test_validator_rejects_mismatched_url(self) -> None:
        """revisionと一致しないURLを拒否する。"""

        broken = json.loads(json.dumps(self.data))
        broken["sources"][0]["public_url"] = "https://example.invalid/not-pinned"
        self.assertTrue(any("public_url" in error for error in MODULE.validate(broken)))


if __name__ == "__main__":
    unittest.main()
