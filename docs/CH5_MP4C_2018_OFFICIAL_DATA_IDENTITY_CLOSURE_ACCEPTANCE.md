# Chapter 5 MP4C 2018 official-data identity closure — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `729d2c13c5864e0f607ac6dc8fd863d19f02d3f7`.

## Verdict

Reviewer marker: `OFFICIAL_2018_DATA_IDENTITY_AUDIT_ACCEPTED__MANUAL_OFFICIAL_DATA_REQUIRED__SCIENCE_STILL_BLOCKED`.

Accept the candidate verdict `PARTIAL_OFFICIAL_IDENTITY__MANUAL_DATA_REQUIRED` and its bounded evidence.

## Accepted findings

1. The structured 2018 Anhui official bulletin provides preliminary 2018 GDP `30006.82`亿元 and year-end resident population `6323.6`万人. These do not match the current provisional workbook values `34010.91`亿元 and `6076`万人. The 2019 official bulletin confirms historical GDP revisions after the fourth national economic census, but the exact revised 2018 GDP identity was not obtained in structured form. Therefore neither the preliminary bulletin values nor the provisional workbook values are promoted to final revised official identities.
2. Under the frozen recurrence `K0=I0/.1`, `Kt=(1-.096)K(t-1)+I(t-1)`, `K2018` requires `I2000..I2017`; `I2018` is not required. The audit correctly keeps 2018 investment only for ledger completeness.
3. A documented 2011 fixed-asset-investment coverage change creates a statistical-definition break. No complete same-definition official absolute 2000–2017 chain was obtained, so the task correctly did not splice, interpolate, or recompute a candidate capital stock.
4. The current `1357314108.2013683` remains a workbook-derived model input, not an official published capital-stock observation. Any future recomputation from an official investment chain must be labeled `MODEL_DERIVED_FROM_OFFICIAL_INVESTMENT`.
5. No candidate V2 data package or candidate Zt was generated because GDP/population revision identity and the investment chain remain incomplete.
6. Scientific/model calls were all zero. The task changed no production data, model equations, PLM estimator, temporal contract, solver, grid, or MATLAB source.

## Required manual closure

Before a new 2018 scientific run, Owner must provide or approve authoritative evidence for:

- post-fourth-economic-census revised Anhui 2018 current-price GDP;
- revised/authoritative Anhui 2018 year-end resident population with revision basis sufficient to resolve `6323.6` vs `6076`;
- Anhui 2000–2017 annual fixed-asset-investment absolute values under a defensibly comparable definition, plus the 2011 linkage/backcast/definition note needed to justify use in one recurrence chain.

If official sources cannot provide a directly comparable investment chain, a separate Owner scientific decision will be required on capital-stock reconstruction methodology. Do not silently retain or splice incompatible definitions merely to obtain a complete series.

## Current route

Active Builder task: none.

Next action is Owner/manual official-data acquisition and upload. No household/HJB/KFE/firm/GE/annual scientific run, no GovInv/alpha tuning, and no new bmax experiment is authorized before data identity closure.

Results eligibility = FALSE.
