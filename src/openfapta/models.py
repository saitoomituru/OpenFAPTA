"""FAPTAの境界を小さな状態遷移へ落とすトイモデル。"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import StrEnum
from math import log2
from typing import Hashable, Iterable, TypeVar

Symbol = TypeVar("Symbol", bound=Hashable)


class ActivationState(StrEnum):
    """資源候補の利用可能状態。"""

    ACTIVE = "active"
    BLOCKED = "blocked"
    UNKNOWN = "unknown"


class DecisionRoute(StrEnum):
    """未知risk／benefitを焼却しない探索経路。"""

    SANDBOX = "sandbox"
    RESOURCE_WAIT = "resource-wait"
    BLOCK = "block"
    OBSERVE = "observe"


class ExplorationState(StrEnum):
    """期待、実践、観測、Last Orderを分離する探索状態。"""

    EXPECTATION_HI_Z = "expectation-hi-z"
    MINING = "mining"
    OBSERVED = "observed"
    LAST_ORDER = "last-order"


@dataclass(frozen=True, slots=True)
class ActionEvent:
    """物理作用とFIAT台帳上の可視性を分離した行為。"""

    name: str
    physical_effect_units: float
    fiat_recorded: bool
    motive: str

    @property
    def fiat_visible_units(self) -> float:
        """FIAT台帳が認識する単位を返す。物理価値の総量ではない。"""

        return self.physical_effect_units if self.fiat_recorded else 0.0


@dataclass(frozen=True, slots=True)
class ResourceCandidate:
    """物理在庫から利用可能資源までの接続条件。"""

    physical_presence: bool | None
    access_permission: bool | None
    steward_available: bool | None
    conversion_bridge: bool | None
    timing_matches: bool | None

    def activation_state(self) -> ActivationState:
        """偽が一つあれば停止し、不明を成功へ変換しない。"""

        conditions = (
            self.physical_presence,
            self.access_permission,
            self.steward_available,
            self.conversion_bridge,
            self.timing_matches,
        )
        if False in conditions:
            return ActivationState.BLOCKED
        if None in conditions:
            return ActivationState.UNKNOWN
        return ActivationState.ACTIVE


@dataclass(frozen=True, slots=True)
class ExplorationCandidate:
    """価格未接続のHi-Z探索候補。未知benefitをゼロへしない。"""

    name: str
    exploration_cost: float
    maximum_loss: float
    belief_in_mineable_benefit: bool
    benefit_estimate: float | None = None
    risk_estimate: float | None = None
    hard_physical_stop: bool = False

    @property
    def valuation_state(self) -> str:
        """未価格候補を数値の無限大へ変換せず状態名で返す。"""

        if self.benefit_estimate is None:
            return "UNPRICED_HI_Z"
        return "ESTIMATED"


@dataclass(frozen=True, slots=True)
class ExplorationProcess:
    """信仰、マイニング実践、結果観測の成立状況。"""

    belief_active: bool
    mining_performed: bool
    result_observed: bool

    def state(self) -> ExplorationState:
        """期待を結果へ昇格せず、信仰終了時はLast Orderを返す。"""

        if self.result_observed and not self.mining_performed:
            raise ValueError("マイニング実践なしに結果観測を確定できません")
        if self.result_observed:
            return ExplorationState.OBSERVED
        if not self.belief_active:
            return ExplorationState.LAST_ORDER
        if self.mining_performed:
            return ExplorationState.MINING
        return ExplorationState.EXPECTATION_HI_Z


def route_exploration(candidate: ExplorationCandidate) -> DecisionRoute:
    """未知riskと未知benefitを保持したまま、探索経路を決める。

    信仰は物理成功の証明ではないが、探索資源を配分する入力にはなる。
    物理的な強制停止だけは信仰で解除しない。
    """

    if candidate.hard_physical_stop:
        return DecisionRoute.BLOCK
    if candidate.exploration_cost > candidate.maximum_loss:
        return DecisionRoute.RESOURCE_WAIT
    if candidate.belief_in_mineable_benefit:
        return DecisionRoute.SANDBOX
    return DecisionRoute.OBSERVE


def mutual_information(pairs: Iterable[tuple[Symbol, Symbol]]) -> float:
    """有限離散標本の相互情報量をbit単位で推定する。"""

    observations = list(pairs)
    if not observations:
        raise ValueError("少なくとも一つの観測対が必要です")

    joint = Counter(observations)
    left = Counter(first for first, _ in observations)
    right = Counter(second for _, second in observations)
    total = len(observations)
    information = 0.0
    for (first, second), count in joint.items():
        joint_probability = count / total
        independent_probability = (left[first] / total) * (right[second] / total)
        information += joint_probability * log2(
            joint_probability / independent_probability
        )
    return information


def exploration_trial() -> dict[str, float]:
    """既知枝固定と未知枝を一度掘る場合を比較する決定論的な玩具例。

    この結果は探索一般の優越を証明しない。未知benefitを常にゼロと置くと、
    この世界では到達できない枝があることだけを示す反例である。
    """

    known_reward = 1.0
    hidden_rewards = (0.0, 3.0, 0.5)
    rounds = 10
    exploit_only = known_reward * rounds
    explore_then_use_best = sum(hidden_rewards) + max(hidden_rewards) * (
        rounds - len(hidden_rewards)
    )
    return {
        "exploit_only": exploit_only,
        "explore_then_use_best": explore_then_use_best,
    }
