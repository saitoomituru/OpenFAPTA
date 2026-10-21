# Recovery potential and exploration-frontier merchant engine

Status: `DESIGN`; current code: `EXPERIMENTAL / TOY MODEL`
Updated: 2026-10-21
Author: 齋藤みつるSaitooMituru-Fusamofu-ふさもふ
Documentation: CC BY 4.0

This en-US text is a reference manuscript of the [canonical Japanese document](merchant-engine.ja.md). Consult Japanese when definitions, responsibilities, or scope differ. Do not use the English manuscript to overwrite or narrow the source. This is an explanatory design document, not an executable Kernel translation or a new ABI.

## Purpose

OpenFAPTA is an open, general-purpose merchant-engine design for credit creation through discovering, registering, testing, and reassessing recovery potential and the exploration frontier of unknown commons. FAPTA stands for Fold Autonomous Potential Transaction Architecture.

Its intended users include currency issuers, credit providers, communities, and organizations allocating research or operating resources. Credit-card merchant systems provide a practical analogy; OpenFAPTA focuses on the underlying recovery and exploration assessment. It does not claim implementation of a particular card-network contract.

The portfolio concerns futures that can be attempted, conditions for recovering resources or capabilities, and remaining avenues of exploration. Each Fold declares what counts as recovery; recovery is not restricted to cash repayment.

## Discovery, trials, and retries

Discover and register candidates and unknowns; define inputs, observations, resources, and stopping or resumption conditions; perform a trial; retain results, failures, inaccessible paths, and newly discovered unknowns; reassess retries with changed conditions; update the portfolio.

A failed attempt, an unobserved result, closure of one route, and exhaustion of the available search space are distinct. `LAST_ORDER` closes the current route without declaring the candidate universally worthless. Reprocessing existing data is distinct from a new trial or observation.

## M-dimensional charts, topology, and area

The proposed chart retains recovery candidates, frontier extent, rarity, volatility, timing, resource dependencies, and retry capacity under an explicitly selected evaluation profile. No fixed dimension count or universal aggregate value score is prescribed.

“Area” means an evaluation quantity under the configuration's declared measure. Fold topology, evaluation axes, measure, unit, aggregation rule, and comparison scope must be specified separately. Topology alone does not determine an area value or a currency amount. Values from different measures require an explicit mapping before aggregation.

A wide frontier with extreme volatility can contain substantial unexplored opportunity while recovery remains unresolved. A stable chart with thin tails can retain dependable recovery while offering little additional exploration. A growing tail can also consume resources from another Fold. Unmeasured or described-as-unbounded volatility remains explicitly qualified; Hi-Z is not assigned numeric infinity.

Frontier expansion and changing volatility are dimensions for detecting positive-sum candidates. Assessment also follows resource transfers, depletion and recovery in other Folds, and duplicate counting of shared commons. Local gains and gains across the declared system boundary remain distinct.

## Configurable, fractal portfolios

Users choose Folds, connections, partitions, hierarchies, measures, and credit-allocation policies according to their political and currency-issuance philosophies. “Fractal” describes reuse of the configuration principle at individual, organizational, community, and issuer scales; it does not merge their authority or resources.

The proposed competition is among algorithms that sustain commons, explore unknowns, and improve recovery and future exploration capacity. Comparisons retain the selected Folds, measure and unit, policy revision, trial history, consumed resources, and unresolved questions. No ideology becomes the engine's universal ruler.

## External currencies and ledgers

Exchange units, currency issuance and balances, settlement, and distributed-ledger consensus belong to external implementations. Operators can select cryptocurrency, stablecoin, premium-voucher, points, or other FIAT v2 systems. Listing these choices does not imply that adapters already exist.

An area unit used for evaluation is separate from a unit used for exchange. OpenFAPTA supports assessment underlying credit, equities, or currency issuance. Historical-credit versus future-recovery evaluation is the project's comparison axis, not a universal claim that existing fiat systems evaluate only the past.

## Current code and remaining work

Existing Python toys distinguish resource activation conditions (`ResourceCandidate`), ledger visibility and physical effects (`ActionEvent`), unknown benefits and exploration routes (`ExplorationCandidate`), and expectation, activity, observation, and Last Order (`ExplorationProcess`). The CLI's `ledger` example is not a distributed-ledger product.

Persistent candidate/retry management, general M-dimensional charts and measures, fractal configuration, commons depletion and cross-Fold positive-sum detection, and external currency adapters are not implemented by these toys. The Japanese document contains the responsibility matrix.

Next fixtures compare wide uncertain frontiers, stable but nearly exhausted frontiers, gains paid for by another Fold, duplicate resource accounting, successful retries after changed conditions, lost observation capacity, and unit changes versus measure changes. Continue in existing [#8](https://github.com/saitoomituru/OpenFAPTA/issues/8), [#3](https://github.com/saitoomituru/OpenFAPTA/issues/3), and [#4](https://github.com/saitoomituru/OpenFAPTA/issues/4).

## Provenance

This document records the author's October 21, 2026 clarification. The inspected implementation baseline is `a11695d677501ccd20b9170067cc1c1ebcbd92cb`. The original Japanese [principles](../philosophy/open-fapta-principles.ja.md) and [toy-model boundary](toy-model-boundary.ja.md) remain available. Today's interpretation is not backdated into those records.
