# Chapter 5 MP4C unit-normalized initialization-only probe — Reviewer acceptance

Date: 2026-09-10

Accepted candidate: `ff2a32e6c6eb799931b741c9a8557afdaa5c8bfa`.

Reviewer verdict:

`UNIT_NORMALIZED_INITIALIZATION_PROBE_ACCEPTED__BROAD_FIRM_PRICE_BOUNDARY_HITS_PERSIST_AFTER_DATA_AND_MACRO_UNIT_CORRECTION__NEXT_DIAGNOSIS_MUST_TARGET_PRICE_NORMALIZATION_AND_BRIDGE_SEMANTICS`

## Acceptance basis

The candidate is accepted as an initialization-only diagnostic receipt. It stays within the authorized scope: no MATLAB model call, no household/HJB/KFE/control solve, no `Lt_seperate` call, no root solver, no outer turn, no steady state, no GE/annual/IRF/Results, and no parameter tuning.

The evidence package correctly preserves protected-source identities, records the source-equation discrepancy `mt0=.92` rather than silently using the redesign prose simplification `.9`, and preserves raw versus clipped firm prices.

Key accepted findings:

- corrected 2018 GDP/population, Track-A PIM capital, common macro units `MU=10万元`, `NU=100 persons`, and `alpha=.7380939146868483` do not restore an interior first-firm price state;
- raw `ra` classification against `[.02,.09]` is `0/1/30` below/inside/above;
- raw wage classification against `[.8,1.3]` is `0/0/31` below/inside/above;
- all 31 provinces hit at least one price boundary;
- Anhui raw/used `ra0=.32587797015041736/.09`, raw/used `wjt0=13.487571992789512/1.3`, source-lagged `rah0=.08895777765800762`, and static composite wage `w0=18.29792118969518`;
- the legacy `At=2` bridge diagnostic remains `SOURCE_FAITHFUL_BASELINE_ONLY` and does not select a production asset bridge.

## Scientific interpretation boundary

This acceptance does **not** show that the household algorithm is wrong, nor does it justify changing price bounds to force an interior start.

The accepted evidence instead narrows the next question: after fixing the obvious mixed-year and macro-money-unit problems, the firm-side price normalization remains inconsistent with the historical safety ranges. Candidate explanations include source-unit conventions, the household/macroeconomic asset bridge, wage/transfer normalization, firm-price formula normalization, or legacy safety bounds that were tuned under the old numerical scale. These possibilities must be separated before any production change.

The acceptance therefore does not authorize:

- widening `ra` or wage bounds;
- selecting an asset bridge coefficient from convergence behavior;
- changing firm equations;
- changing `rah` timing;
- running a household solve or full outer turn;
- testing damping/hysteresis;
- steady state, GE, annual, IRF, or Results.

Results eligibility remains `FALSE`.
