# Chapter 5 MP4C steady-state calibration and initialization redesign specification acceptance

Date: 2026-09-10

Accepted candidate: `abfeec3bd7443cd5a95ef3a62aedae16be81b702`.

Reviewer verdict:

`STEADY_STATE_REDESIGN_SPEC_ACCEPTED_PARTIAL__UNIT_AND_INITIALIZATION_PROBE_AUTHORIZED__PRODUCTION_RUNTIME_STILL_BLOCKED`

## Acceptance basis

The candidate is accepted as a correct zero-science design/source-mapping package. It correctly identifies the legacy GDP/capital multiplier inconsistency, the implicit `At*N` household-to-macro asset bridge, the active alpha behavior, legacy arbitrary first-household prices, the existing K/N-reference damping, source Zt/GovInv controller order, and the single-loop update semantics. It also cleanly separates path-stabilization proposals from production authority.

The following Reviewer/Owner decisions are frozen for the next bounded probe only:

1. Correct 2018 GDP/POP remain mandatory.
2. Raw-NBS GFCF Track A with PIM `delta=.096` is the selected **probe capital route**. This does not yet promote it to final Results authority; it is selected because the Owner supplied the official raw series specifically to replace the legacy mixed-year object, and the lagged-flow identity can construct K2018 from observed 2017 flows.
3. Common macro normalization for the probe is approved: `MU=10万元`, `NU=100 persons`; GDP亿元 `×1000`, capital亿元 `×1000` (or 万元 `÷10`), population万人 `×100`.
4. Alpha successor contract is approved: save `alpha_raw`, clip to `[.2,.8]`, save `alpha_used/flag/reason`; current `0.7380939146868483` remains unchanged.
5. PIM depreciation `.096` and firm depreciation `.025` remain distinct roles for now. They must be documented separately; no silent unification.
6. Preserve source-lagged `rah` timing as the baseline for the next probe. The after-firm current-ra timing remains a separately labelled future candidate.
7. No additional GovInv damping is adopted yet.
8. No production `w/rah` lambda or hysteresis threshold is frozen yet; the preregistered candidate sets remain future bounded-validation objects.

## Still unresolved

The household asset-grid currency normalization remains unresolved. The next task may use the current implicit bridge coefficient `1` **only as a source-faithful diagnostic baseline**, while clearly labelling it as not yet economically justified. It must not select a replacement bridge from convergence behavior.

Wage/transfer/AtTax aggregate normalization remains to be mapped into the successor implementation. No HJB/KFE/steady-state production run is authorized by this acceptance.

Results eligibility remains `FALSE`.
