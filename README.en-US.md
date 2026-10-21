# OpenFAPTA

**An open, general-purpose merchant-engine design for credit creation through recovery-potential and exploration-frontier portfolios.**

OpenFAPTA discovers, tests, and reassesses potential recovery paths and the unexplored commons. Currency issuers, credit providers, and communities choose which Folds to connect and which topology, area measure, evaluation units, and allocation policies to use. The design applies recursively across individual, organizational, community, and issuer scales.

FAPTA stands for **Fold Autonomous Potential Transaction Architecture**.

Canonical source: [Japanese README](README.md). This en-US text is a reference manuscript. When definitions or responsibilities differ, consult Japanese; do not use this text to overwrite or narrow the source.

## Discover, try, retry, reassess

Discover and register recovery candidates; perform a trial; retain results, failures, and newly found unknowns; reassess changed conditions and possible retries; update the portfolio and its remaining exploration space.

The proposed M-dimensional chart distinguishes frontier extent, volatility, recovery conditions, resource dependencies, and retry capacity. A wide frontier with high volatility, stable recovery with thin tails, and apparent gains consuming another Fold's resources are different portfolio shapes. Frontier expansion and volatility changes inform positive-sum assessment alongside cross-Fold consumption and duplicate-resource accounting.

Users can compete through different configuration algorithms and political or currency-issuance philosophies. The engine does not prescribe a universal value score or a mandatory currency. Area measures and evaluation units are distinct from exchange units.

Exchange units, currency issuance and balances, payments, and accounting or distributed ledgers belong to external implementations. Cryptocurrency, stablecoin, voucher, and points systems are possible choices for integrators, not adapters already shipped in this repository. The CLI's `ledger` example compares accounting visibility with physical effects; it is not a distributed-ledger engine.

See the [Japanese design](docs/theory/merchant-engine.ja.md) and [en-US reference manuscript](docs/theory/merchant-engine.en-US.md) for definitions, the responsibility matrix, and proposed comparison fixtures.

## Current implementation

Status: `EXPERIMENTAL / TOY MODEL`. Standard-library Python models currently cover:

- `ledger`: accounting visibility versus physical activity;
- `activation`: physical presence, access permission, stewardship, conversion, and timing;
- `information`: deterministic data processing versus new observation;
- `exploration`: retained unknown benefits, bounded exploration, and expectation/activity/observation/Last Order states.

General M-dimensional portfolios and area measures, persistent candidate/retry management, and external settlement adapters remain design and implementation work. No existing toy result is promoted into a verified economic outcome.

## Principles

```text
unknown risk    != safe
unknown benefit != zero
belief          != physical proof
accounting zero != physical absence
processed data  != new observation
```

Belief, gifts, maintenance, and exploration can motivate resource allocation without being collapsed into cash value. Record the initiator, executor, observation, and result separately. `UNPRICED_HI_Z` is not numeric infinity. `LAST_ORDER` closes a particular route and retains unobserved possibilities.

## Run

```console
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m openfapta.cli --model all
```

Python 3.11 or later; no runtime dependencies beyond the standard library.

## Sources and development

[Japanese operating rules](docs/operations/development-governance.ja.md), the [pinned source map](references/source-map.json), and the [source lineage](docs/sources/lineage.ja.md) retain governance and provenance. The project references ZeroRoomLab Manifest, SphereOS Atlantis DOS/MAGI, OpenSourcePITETO, and KUMA800 without claiming runtime integration or importing their ownership.

Continue implementation work in the existing [#8](https://github.com/saitoomituru/OpenFAPTA/issues/8), [#3](https://github.com/saitoomituru/OpenFAPTA/issues/3), and [#4](https://github.com/saitoomituru/OpenFAPTA/issues/4).

Code, schemas, CLI, and tests: [Apache-2.0](LICENSE). Documentation and research context: [CC BY 4.0](LICENSE-CONTEXT.md). Third-party material retains its original attribution and terms.

Copyright 2026 齋藤みつるSaitooMituru-Fusamofu-ふさもふ
