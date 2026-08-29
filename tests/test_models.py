"""OpenFAPTAトイモデルの境界試験。"""

from __future__ import annotations

import unittest

from openfapta.models import (
    ActionEvent,
    ActivationState,
    DecisionRoute,
    ExplorationCandidate,
    ExplorationProcess,
    ExplorationState,
    ResourceCandidate,
    exploration_trial,
    mutual_information,
    route_exploration,
)


class LedgerTests(unittest.TestCase):
    """FIAT可視性と物理作用を分ける。"""

    def test_accounting_zero_is_not_physical_absence(self) -> None:
        """無償清掃にも物理作用が残る。"""

        event = ActionEvent("信仰清掃", 10.0, False, "信仰実践")
        self.assertEqual(event.physical_effect_units, 10.0)
        self.assertEqual(event.fiat_visible_units, 0.0)


class ResourceTests(unittest.TestCase):
    """資源接続条件を試す。"""

    def test_unknown_is_not_active(self) -> None:
        """維持者不明を利用可能へ昇格しない。"""

        resource = ResourceCandidate(True, True, None, True, True)
        self.assertEqual(resource.activation_state(), ActivationState.UNKNOWN)

    def test_explicit_blocker_blocks(self) -> None:
        """利用許可なしは現在利用不能である。"""

        resource = ResourceCandidate(True, False, True, True, True)
        self.assertEqual(resource.activation_state(), ActivationState.BLOCKED)


class ExplorationTests(unittest.TestCase):
    """未知benefitと未知riskを焼かない経路を試す。"""

    def test_unknown_benefit_can_enter_bounded_sandbox(self) -> None:
        """信仰入力と損失上限があればHi-Z候補をsandboxへ送る。"""

        candidate = ExplorationCandidate("候補", 2.0, 3.0, True)
        self.assertEqual(candidate.valuation_state, "UNPRICED_HI_Z")
        self.assertEqual(route_exploration(candidate), DecisionRoute.SANDBOX)

    def test_belief_does_not_override_physical_stop(self) -> None:
        """信仰は物理的停止条件を解除しない。"""

        candidate = ExplorationCandidate("危険候補", 1.0, 3.0, True, hard_physical_stop=True)
        self.assertEqual(route_exploration(candidate), DecisionRoute.BLOCK)

    def test_exploration_counterexample_preserves_possible_benefit(self) -> None:
        """未知を常にゼロと置く政策への反例が存在する。"""

        result = exploration_trial()
        self.assertGreater(result["explore_then_use_best"], result["exploit_only"])

    def test_expectation_is_not_observed_result(self) -> None:
        """信仰だけの段階を観測済みへ昇格しない。"""

        process = ExplorationProcess(True, False, False)
        self.assertEqual(process.state(), ExplorationState.EXPECTATION_HI_Z)

    def test_mining_without_observation_remains_unresolved(self) -> None:
        """実践済みでも結果未観測なら採掘中に留める。"""

        process = ExplorationProcess(True, True, False)
        self.assertEqual(process.state(), ExplorationState.MINING)

    def test_lost_belief_issues_last_order_without_zeroing_value(self) -> None:
        """信仰終了は未探索価値の不存在判定ではない。"""

        process = ExplorationProcess(False, False, False)
        self.assertEqual(process.state(), ExplorationState.LAST_ORDER)

    def test_observation_requires_mining(self) -> None:
        """採掘実践なしの結果観測を拒否する。"""

        with self.assertRaises(ValueError):
            ExplorationProcess(True, False, True).state()


class InformationTests(unittest.TestCase):
    """既知観測の決定的加工境界を試す。"""

    def test_deterministic_processing_does_not_increase_mutual_information(self) -> None:
        """粗視化後の相互情報量は元観測を超えない。"""

        source = [(0, 0), (0, 0), (1, 1), (1, 1), (2, 2), (2, 2), (3, 3), (3, 3)]
        processed = [(world, observation % 2) for world, observation in source]
        self.assertLessEqual(mutual_information(processed), mutual_information(source))


if __name__ == "__main__":
    unittest.main()
