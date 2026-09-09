# Chapter 5 MP4C 2018 official-data identity closure report

- Primary verdict: `PARTIAL_OFFICIAL_IDENTITY__MANUAL_DATA_REQUIRED`.
- Temporal contract retained: `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`.
- Scientific calls: `0` in every prohibited category.
- Results eligibility: `FALSE`.
- Final evidence root: `D:\ProjectTemp\ch5-2018-official-data-identity-closure-20260909-005`.

## Identity decisions

| Item | Status | Finding |
|---|---|---|
| GDP | `OFFICIAL_SOURCE_NOT_OBTAINED` | The structured 2018 Anhui official bulletin reports preliminary current-price GDP of `30006.82` 亿元. The provisional workbook has `34010.91` 亿元, a difference of `4004.09` 亿元 (`13.343933%` relative to the preliminary publication). The 2019 official bulletin says historical GDP was revised after the fourth national economic census, but the obtained structured pages do not publish the exact revised 2018 value. |
| Resident population | `OFFICIAL_SOURCE_NOT_OBTAINED` | The structured 2018 official bulletin reports year-end resident population of `6323.6` 万人. The provisional workbook has `6076` 万人, a difference of `-247.6` 万人 (`-3.915491%`). No later official table establishing `6076` and its revision chronology was obtained. |
| Investment chain | `CAPITAL_CHAIN_OFFICIAL_CLOSURE_INCOMPLETE` | All Anhui workbook investment cells for 2000–2018 are numeric and unchanged between raw and filled workbooks. No complete same-definition official absolute series was obtained. The official bulletin records a material 2011 coverage change. |
| 2018 capital stock | `NOT_COMPUTED__INCOMPLETE_OR_NONCOMPARABLE_OFFICIAL_INVESTMENT_CHAIN` | The official investment chain is incomplete and crosses a documented definition break, so no official-source-based candidate recurrence was computed. The existing `1357314108.2013683` remains a workbook-derived provisional value, not an official capital-stock observation. |
| Candidate V2 input | `NO_CANDIDATE_PACKAGE__OFFICIAL_IDENTITIES_AND_INVESTMENT_CHAIN_INCOMPLETE` | No corrected candidate values or candidate Zt were emitted. The current provisional values were preserved for comparison only. |

These classifications do not declare the preliminary official values to be the final revised identities. They record that authoritative observations were obtained but the exact official vintages needed to validate the provisional workbook were not closed.

## Official evidence obtained

The Anhui Provincial Government page for the 2018 statistical bulletin identifies the publishing statistical authorities as the Anhui Provincial Bureau of Statistics and the NBS Anhui Survey Office. Its structured HTML provides:

- `30006.82` 亿元 for 2018 GDP, described as a preliminary calculation; the absolute GDP value is at current prices and the growth rate is at comparable prices;
- `6323.6` 万人 for 2018 year-end resident population;
- fixed-asset-investment growth of `11.8%` at a comparable scope, without an absolute 2018 investment value;
- a note that the 2011 statistical-system reform changed fixed-asset-investment coverage to projects with planned total investment of at least RMB 5 million plus real-estate development investment.

The official 2019 bulletin states that historical GDP and sector value-added series were revised after the fourth national economic census. It does not expose the precise revised 2018 GDP in its structured page. This prevents treating either the preliminary `30006.82` or the provisional workbook `34010.91` as the closed revised identity.

The National Bureau of Statistics' official *China Statistical Yearbook 2019* index and the image tables `2-6 分地区年末人口数`, `3-9 地区生产总值(2018年)`, and `10-1 全社会固定资产投资` were downloaded and hashed. The tables are image-only. Consistent with the task's no-OCR rule, no value was transcribed from them. The Owner manual request names the exact tables and required fields.

All accepted observations and method notes have institution, publication/table name, province/year, value/unit where present, price-basis wording, retrieval date, stable URL, downloaded SHA-256, table locator, and revision caveat in `official_observation_ledger.csv`. The downloaded official pages and table images remain outside Git in the final evidence root.

## Frozen recurrence and workbook chain

The protected source contract remains:

```text
K0 = I0 / 0.1
Kt = (1 - 0.096) * K(t-1) + I(t-1)
```

Therefore `K2018` uses `I2000` through `I2017`; `I2018` is `NOT_REQUIRED_BY_RECURRENCE`. The year-by-year ledger records the workbook values and raw/filled identity. For Anhui, all 19 investment entries from 2000 through 2018 are `ORIGINAL_OBSERVED_UNCHANGED`. That status establishes workbook lineage only; it does not establish official identity.

The 2011 official coverage change blocks a defensible splice without an official linked/backcast series or a documented compatibility decision. The task consequently performs no makima fill, linear interpolation, estimation, or capital recurrence using substitute official values.

## Provisional V2 comparison

The frozen 2018 coordinates remain `analysis_index=10`, `data_mat_index=10`, `level_row=19`, `steady_year=2018`, `PLM vintage=19`, rolling window `2009–2018`, same-year Zt year `2018`, and alpha `0.772866243094144`.

| Variable | Provisional raw | Provisional transformed | Official observation obtained | Candidate verified value |
|---|---:|---:|---:|---:|
| GDP | `34010.91` 亿元 | `34010910.0` | `30006.82` 亿元, preliminary | not closed |
| POP | `6076` 万人 | `607600.0` | `6323.6` 万人, preliminary | not closed |
| CAP | `1357314108.2013683`, workbook-derived | `1357314108201.3684` | no complete comparable investment chain | not computed |
| Zt | frozen same-year formula | current provisional arithmetic only | requires closed GDP/POP/CAP candidate | not computed |

No production data, workbook, cache, MATLAB source, Python annual model input, PLM object, temporal contract, or scientific parameter was changed.

## Exact manual closure request

`manual_official_data_request.csv` asks the Owner to obtain:

1. the post-fourth-economic-census revised Anhui 2018 current-price GDP value, with official table/page and revision vintage;
2. the official revised Anhui 2018 year-end resident population, with census/survey basis and revision chronology sufficient to resolve `6323.6` versus `6076`;
3. official Anhui 2000–2017 annual fixed-asset-investment absolute values in a consistent or explicitly linked definition, including units, price basis, coverage, and the 2011 linkage/backcast note.

Until those data are supplied, the official identity closure remains partial and no candidate-data package is scientifically warranted.

## Validation and evidence boundary

The task validator checks the two frozen workbook hashes before reading values and emits only the narrow Anhui ledger and provenance records. Synthetic tests cover recurrence timing, the frozen recurrence arithmetic, unit conversion, difference bookkeeping, and absence of model/solver entry points. The committed `tests.txt` is the actual test-process output, and manifest readback verifies all committed report artifacts plus the external evidence package.

The call ledger records zero MATLAB, household/HJB/KFE, root/direct/eigen, firm/controller, stationary/GE/annual-model, IRF, and Results calls. This report closes only the evidence available in this task. It does not authorize a 2018 household, HJB, KFE, firm, GE, annual, IRF, or Results run.
