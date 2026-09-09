# Chapter 5 MP4C 2018 PIM capital-chain closure

Date: 2026-09-09

Repository baseline: `d7798b4f8e32db0b7192898da846f4cb623f07c0`

Task: `tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`

External evidence: `D:\ProjectTemp\ch5-2018-pim-capital-chain-closure-20260909-001`

## Verdict

`PIM_CAPITAL_CHAIN_CLOSED__EXISTING_2018_CAP_REPRODUCED`

The protected Anhui province investment chain reproduces the existing 2018 workbook-derived capital stock exactly under the frozen source recurrence. This closes only the capital/PIM data-method blocker, subject to Reviewer acceptance. The capital stock remains a model-constructed calibration object. It is not an official published capital-stock observation or an official continuous same-definition investment series.

`Results eligibility = FALSE` because revised 2018 Anhui current-price GDP remains open and no scientific model run is authorized by this result.

## Source timing and identity

`It_to_Kt.m` implements:

```text
K(1,:) = I(1,:) / 0.1
K(i,:) = (1 - delta) * K(i-1,:) + I(i-1,:), i = 2..N
```

`load_GDPdata.m` reads `固定资产投资额!B2:AG25`, applies `fillmissing(...,'makima')`, calls `It_to_Kt(temp2, delta)`, and writes the resulting capital matrix to `总资本存量!B2:AG25`. Therefore the 2018 capital row uses the 2017 investment row; `K2018` depends on `I2000..I2017`, while `I2018` is excluded.

The province identities are MATLAB index 12, Python index 11, and Excel column `N`. The protected-source identities used here are:

| Object | SHA-256 |
| --- | --- |
| `2000年后各省数据.xlsx` | `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3` |
| `2000年后各省数据_填充NA.xlsx` | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` |
| `It_to_Kt.m` | `4A407DE29F2DCD370932DAE35436A1B9D3C0432A360D94ABC0F78E1F94FEBE50` |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` |

For安徽 `固定资产投资额!N2:N20` (2000–2018), all 19 raw cells are present and binary64-identical to the filled workbook. No Anhui observation was changed by the fill stage. The recurrence uses `N2:N19`; `N20` was checked only to close the full observed/unfilled lineage statement.

Source classification is:

`MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL`

## Recurrence result

The static binary64 replay produced:

| Check | Result |
| --- | --- |
| Calculated `K2018` | `1357314108.2013683` 万元 |
| Existing workbook `K2018` | `1357314108.2013683` 万元 |
| IEEE-754 binary64 | `41D439BE0F0CE338` on both sides |
| Exact binary64 equality | `TRUE` |
| Absolute difference | `0` |
| Relative difference | `0` |
| First divergence year | none |
| V2 transformed CAP (`×1000`) | `1357314108201.3684` |

Every annual value `K2000..K2018` is binary64-identical to `总资本存量!N2:N20`. The complete year-by-year inputs, formulas, calculated values, workbook values, bit patterns, and differences are preserved in `anhui_pim_recurrence_2000_2018.csv`.

The receipt schema is `CH5_2018_PIM_CAPITAL_INPUT_V1`. It records the source hashes, province indices, required years, units, formula, timing, derived value, V2 transformation, lineage state, and authority limits.

## 2011 definition break

The accepted 2011 fixed-asset-investment statistical coverage change remains a material comparability limitation. Owner has authorized continued use of this series as model calibration data, so it does not block the PIM recurrence identity. Metadata classifies it as:

`MODEL_CALIBRATION_SERIES_WITH_DOCUMENTED_2011_DEFINITION_BREAK`

No backcast, bridge factor, rescaling, splice, interpolation, or historical observation change was applied. Future model and paper limitations must retain this caveat.

## Purchased city-data directional check

The `sj479` data were used only for `SECONDARY_DIRECTIONAL_CROSSCHECK_ONLY`. No city sum or city-based PIM candidate was computed.

Across 2001–2017, the province series direction agrees with the majority direction among the 16 city-level pairs in 16 of 17 years. The exception is 2001: the province sequence decreases while 13 of 16 purchased city series increase. In 2017, the province sequence increases and 15 of 16 city levels increase. All 16 rows also contain positive stored growth fields, but documentation permits a mix of growth-derived and directly published levels; the stored growth field was therefore not assumed to generate each level.

This mixed directional evidence neither validates province-level additivity nor authorizes replacing any province observation.

## Relationship to other 2018 inputs

- Resident population remains closed at `6076` 万人 under the accepted revised 2023 official yearbook evidence.
- The temporal contract remains `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`.
- Revised 2018 current-price GDP remains open: provisional `34010.91` 亿元 versus preliminary official `30006.82` 亿元.
- No GDP decision or V2 production-input promotion was made in this task.

## Verification and calls

- Synthetic tests: `7/7` passed; the actual unittest log was retained and parsed.
- Protected source readback: all five consumed source files retained their pre-read SHA-256 identities.
- Manifest/readback covers the report and all machine-readable repository artifacts.
- MATLAB, household/HJB/KFE, roots/direct/iterative/eigen, firm/controller, stationary/GE/annual, IRF/Results calls: all `0`.
- `scientific_calls = 0`.
- `Results_eligible = FALSE`.
