# Chapter 5 MP4C 2018 revised GDP closure and canonical data workbook

Date: 2026-09-09

Repository baseline: `7fa237d9a5e9e26bec95d1cd329f1cebb07a5cba`

Task: `tasks/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK.md`

External artifact root: `D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001`

## Verdict

`REVISED_2018_GDP_CLOSED__CANONICAL_WORKBOOK_BUILT`

The Anhui Provincial Bureau of Statistics directly publishes the post-Fourth-National-Economic-Census revised 2018 current-price GDP as `34010.9` 亿元. The protected workbook value `34010.91` 亿元 rounds to the same value at the official publication precision of `0.1` 亿元. The GDP identity is therefore classified `REVISED_GDP_MATCHES_CURRENT_PROVISIONAL` at the authority's published precision.

The canonical workbook records `34010.9` as the official final-use value and keeps `34010.91` as the protected provisional/source value. No protected workbook was changed. This closure is a static data-input result. `Results eligibility = FALSE`.

## Official GDP evidence

Source: 安徽省统计局, *安徽省统计局关于修订2018年全省生产总值数据的公告*, published 2020-01-21 08:18, [official page](https://tjj.ah.gov.cn/ssah/qwfbjd/fxjd/113609921.html).

The article states that the National Bureau of Statistics and provincial statistical bureaus revised 2018 regional GDP using the national regional-GDP accounting system and Fourth National Economic Census results. Its comparison table is explicitly headed `现价总量（亿元）` and reports:

| Observation | Value (亿元) |
| --- | ---: |
| Revised 2018 Anhui GDP, official publication | 34010.9 |
| Protected workbook provisional/source value | 34010.91 |
| Exact decimal difference, revised minus workbook | -0.01 |
| Official preliminary display | 30006.8 |
| Task-carried preliminary value | 30006.82 |
| Revised minus task-carried preliminary | 4004.08 |

The source HTML was saved read-only outside the repository as `evidence\anhui_statistics_2018_gdp_revision_20200121.html`, SHA-256 `1470A5E12777258326E58C8F3BE0FA318338FD9C628CBF9EBA407E90405F6526`. The official page publishes one decimal place; it does not establish whether the underlying unrounded value is exactly `34010.91`. The receipt preserves that precision boundary rather than claiming exact two-decimal identity.

## Canonical workbook

Workbook: `D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

SHA-256: `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

The workbook contains all 12 required sheets in the specified order. It includes 31 provinces for 2000–2023 GDP, population, investment, and PIM capital; 2009–2023 temporal bindings, industry-4 PLM alpha, and static same-year Zt; the compact Anhui 2018 final static input; source provenance; and machine-readable quality flags.

The private/CNKI-curated panel remains only in the external workbook. GitHub receives hashes, receipts, summaries, tests, and readback evidence, not the workbook or protected source files.

## Anhui 2018 static input

| Field | Accepted value/status |
| --- | --- |
| steady year / analysis index / data_MAT index | 2018 / 10 / 10 |
| level row / PLM vintage / rolling window | 19 / 19 / 2009–2018 |
| GDP raw and transformed | 34010.9 亿元 / 34010900.0 |
| Population raw and transformed | 6076 万人 / 607600.0 |
| PIM capital raw and transformed | 1357314108.2013683 万元 / 1357314108201.3684 |
| Industry-4 alpha | 0.772866243094144 |
| Static same-year IND_Zt | 0.0006934644495858678561 |
| Input status | FINAL_STATIC_INPUT_READY__NO_MODEL_RUN |

Population carries forward the accepted 2023 *中国人口和就业统计年鉴* table 1-1 history revised using the 2020 Census. PIM carries forward the exact binary64 closure under `K0=I0/.1` and `Kt=(1-.096)K(t-1)+I(t-1)`. The capital object remains model-derived and is not official published capital stock.

## Panel and quality evidence

The workbook preserves the original and filled cell status for GDP, population, and investment. All 744 generated PIM capital records are binary64-identical to the protected workbook capital panel. Six nonpositive capital observations remain in 2022–2023: 上海 2022; 吉林、上海、江西、湖南、新疆 2023. Their Zt fields are blank with `INVALID_NONPOSITIVE_OR_MISSING_INPUT`; no repair or complex logarithm is introduced.

The visible quality ledger also retains the 2011 investment definition break, CNKI/manual-curation limitation, stale ii15 alpha cache, deprecated mixed-year 2018 representation, purchased-TFP noncomparability, and official GDP precision note.

## Workbook validation

- `12/12` required sheets exist in exact order.
- Every data sheet has a filter table; every sheet freezes its header row.
- Workbook contains no formulas, formula errors, macros, or external links.
- Artifact Tool reopened the saved workbook and inspected the sheet list, final-input table, GDP value, and formula-error scan.
- All 12 sheet previews were rendered and visually reviewed for headers, legibility, formats, widths, and clipping.
- Independent package readback confirms the official/source/final-use GDP values `34010.9 / 34010.91 / 34010.9`, PIM `744/744` binary64 matches, and the six retained nonpositive-capital flags.

## Tests and calls

The related synthetic/static test module checks official-precision comparison, frozen PIM timing, same-year Zt arithmetic, invalid-input closure, exact sheet contract, receipt authority limits, and absence of scientific entry points. The actual unittest log was retained and parsed: `8/8` tests passed.

MATLAB, household/HJB/KFE, root/direct/eigen, firm/controller, stationary/GE/annual model, IRF/dynamics/Results calls are all `0`. `scientific_calls = 0`. `Results_eligible = FALSE`.
