"""OpenFAPTAトイモデルのCLI。"""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable
from typing import Any

from .models import (
    ActionEvent,
    ExplorationCandidate,
    ExplorationProcess,
    ResourceCandidate,
    exploration_trial,
    mutual_information,
    route_exploration,
)


def ledger_example() -> dict[str, Any]:
    """公費清掃と信仰清掃の台帳差を返す。"""

    events = (
        ActionEvent("公費で拾った神社のゴミ", 10.0, True, "委託契約"),
        ActionEvent("信仰で拾った神社のゴミ", 10.0, False, "信仰実践"),
    )
    return {
        event.name: {
            "physical_effect_units": event.physical_effect_units,
            "fiat_visible_units": event.fiat_visible_units,
            "motive": event.motive,
        }
        for event in events
    }


def activation_example() -> dict[str, str]:
    """存在する空き家が利用可能とは限らない例を返す。"""

    candidates = {
        "存在するが維持者不明": ResourceCandidate(True, True, None, True, True),
        "利用許可なし": ResourceCandidate(True, False, True, True, True),
        "全条件接続": ResourceCandidate(True, True, True, True, True),
    }
    return {
        name: candidate.activation_state().value
        for name, candidate in candidates.items()
    }


def information_example() -> dict[str, float]:
    """観測を決定的に粗くしても相互情報量が増えない例を返す。"""

    world_and_observation = [
        (0, 0),
        (0, 0),
        (1, 1),
        (1, 1),
        (2, 2),
        (2, 2),
        (3, 3),
        (3, 3),
    ]
    processed = [(world, observation % 2) for world, observation in world_and_observation]
    return {
        "world_observation_bits": mutual_information(world_and_observation),
        "world_processed_bits": mutual_information(processed),
    }


def exploration_example() -> dict[str, Any]:
    """Hi-Z候補の経路と探索反例を返す。"""

    candidate = ExplorationCandidate(
        name="未探索の循環資源用途",
        exploration_cost=2.0,
        maximum_loss=3.0,
        belief_in_mineable_benefit=True,
    )
    return {
        "candidate": candidate.name,
        "valuation_state": candidate.valuation_state,
        "decision_route": route_exploration(candidate).value,
        "states": {
            "期待": ExplorationProcess(True, False, False).state().value,
            "採掘中": ExplorationProcess(True, True, False).state().value,
            "観測済み": ExplorationProcess(True, True, True).state().value,
            "信仰終了": ExplorationProcess(False, False, False).state().value,
        },
        "toy_trial": exploration_trial(),
    }


def build_parser() -> argparse.ArgumentParser:
    """CLI引数解析器を作る。"""

    parser = argparse.ArgumentParser(
        description="OpenFAPTAの回収可能性・探索境界を試すマーチャントエンジン研究用トイモデル"
    )
    parser.add_argument(
        "--model",
        choices=("ledger", "activation", "information", "exploration", "all"),
        default="all",
    )
    return parser


def main() -> None:
    """選択したモデルをJSONで表示する。"""

    arguments = build_parser().parse_args()
    models: dict[str, Callable[[], dict[str, Any]]] = {
        "ledger": ledger_example,
        "activation": activation_example,
        "information": information_example,
        "exploration": exploration_example,
    }
    result = (
        {name: function() for name, function in models.items()}
        if arguments.model == "all"
        else {arguments.model: models[arguments.model]()}
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
