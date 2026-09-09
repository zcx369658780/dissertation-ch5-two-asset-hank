# Chapter 5 MP4C 2018 PIM capital-chain closure — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `0bfff9ff9f388e39812c6592f72d5eedd633ae18`.

## Verdict

Reviewer marker: `PIM_CAPITAL_CHAIN_ACCEPTED__2018_CAP_BINARY64_REPRODUCED__GDP_ONLY_DATA_BLOCKER_REMAINS`.

Accept `PIM_CAPITAL_CHAIN_CLOSED__EXISTING_2018_CAP_REPRODUCED`.

Accepted findings:

- The frozen PIM method remains `K0=I0/0.1`, `Kt=(1-.096)K(t-1)+I(t-1)`.
- Anhui `K2000..K2018` are reproduced exactly, year by year, in binary64 from the protected province investment chain.
- `K2018=1357314108.2013683` and V2 transformed CAP=`1357314108201.3684`; absolute and relative differences are both zero and no divergence year exists.
- `I2018` is not used in `K2018`; the final flow is `I2017`.
- Anhui investment source cells used for the recurrence are raw/filled binary64-identical; no fill, interpolation, bridge, backcast, rescaling, splice, or parameter adjustment was used.
- The 2011 fixed-asset-investment statistical-definition break remains an explicit calibration limitation.
- Capital stock is a model-derived calibration object from `MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL`, not an official published capital-stock series.
- Purchased city investment was used only as directional cross-check and did not become a province total or PIM input.
- Scientific/model calls were all zero; Results eligibility remains FALSE.

## Route consequence

The capital/PIM data-method blocker is closed for the 2018 bounded validation route. Resident population is already closed at 6076万人. The remaining 2018 data-identity blocker is the post-fourth-economic-census revised Anhui 2018 current-price GDP identity.

This acceptance does not authorize a new 2018 scientific model run by itself.
