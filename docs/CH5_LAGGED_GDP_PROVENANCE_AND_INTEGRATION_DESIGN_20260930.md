# Lagged GDP provenance and integration preparation

Date: 2026-09-30 (Asia/Shanghai).
Status: ZERO_SCIENCE_DESIGN_PROPOSAL__NO_SOURCE_INTEGRATION_AUTHORITY.
Owner requested continued progress after inactive-helper engineering acceptance. This document records further read-only findings and a concrete prospective integration contract; it does not activate a route or authorize model calls.

## Fresh state and scope

Only model worktree: D:\ProjectTemp\c5k1bturn56. Parent HEAD 75cee92b1ad9e5cb6fc069bca892213838ffdddc; HEAD:src 00682b2e1a7ba23665f6e16f6acf48ad35874883. Inactive helper engineering acceptance remains as recorded in EVIDENCE/ch5_lagged_observed_gdp_wedge_helper_20260930/independent_engineering_review_final.md. No tests repeated this phase, no source modified and no scientific execution. Owner AGENTS change and protected report roots remain outside write scope. C9 paused, Objective A retained, old actual ledgers CALL_LEDGER_UNRESOLVED, Results eligibility FALSE.

## Official price evidence: limited attribution

On 2026-09-30, browser inspection of the National Bureau of Statistics current national annual topical report, titled 国民经济核算指标, visibly showed:

> 1. 绝对数和构成按当年价格计算，指数按不变价格计算。

The displayed table distinguishes GDP absolute amounts in 亿元 from GDP indices. Exact observed page:
https://data.stats.gov.cn/dg/website/page.html#/pc/national/home/report?reportId=7ddb6b4f94b241378c1a70e7ef36e7ba&catalogId=97ea139acc9d4f1aa5858041004d9b0d&type=year

This is current national report evidence, not a verified historical provincial download identity. A single direct read attempt at the legacy provincial annual database https://data.stats.gov.cn/easyquery.htm?cn=E0103 returned 403 Forbidden. No access restriction was bypassed. The current table's prices cannot by themselves assign current_price to the existing historical XLS.

The manuscript's previously recorded E09 source identities are GDP SHA-256 0EA17C78F60054ACCA26D0B56402977E560EE3FF4B220D666A5D0E98178F83E7 and population SHA-256 565B83873D56B8F9770F46BF897452B08A8850A3A954519643C1370188C09CAA. These were read from the manuscript this phase, not a new spreadsheet read/hash. E09 says both source sheets are 分省年度数据; GDP unit 亿元, year-end resident population unit 万人, and 2017 is column H. E09 explicitly leaves GDP price and release vintage unresolved.

Required closure evidence: original indicator/download attribution plus its specific price note or corresponding edition documentation. Owner has been asked for remembered download origin/year or retained indicator notes. A response supports attribution but must not be misreported as a fresh statistical-table match. Any revised contemporary panel would be a new source, with separate identity and vintage acceptance, not a silent substitute for the old file. Until closure, real-data price_verified remains False and an observed helper binding must be rejected.

## Read-only program mapping

Mapping helper wedge_code_map found the exact worktree absent from the code graph; it used the named file directly without external indexing. In src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py:

| Location | Observed contract |
|---|---|
| load_initial_states, lines 184-243 | Fixed entering-turn-2 receipt, 31 records and province order; no target calendar-year parsing/validation. |
| OneTurnInputs, lines 96-131 | phi axes are destination by origin. |
| _one_turn_inputs, lines 857-873 | Builds a 31 by 31 phi matrix from state Yt/Lt. |
| integrate_one_turn, lines 941-953 and 989-993 | The same input phi feeds migration labor reconstruction and composite household wages. |
| execute, line 1527 and following | Household completion followed by integration; numerical turn labels do not bind a calendar year. |

The current file has no observed calendar binding, so an outer turn must never be interpreted as t. A prospective 2018 experiment would require explicit acceptance of target_year=2018 and observation_year=2017; names in archived diagnostics alone are not annual authority.

## Prospective integration contract, not adopted implementation

1. An explicit annual boundary supplies target_year, exact accepted 31-province order and verified GDP/population source identities/vintage. Read only the named t-1 year; no latest-year fallback or inferred year from iteration count.
2. Construct one AnnualLaborWedge at annual entry. Freeze target year, observation year, province axes, q, amplitude, price/population provenance and coefficients. The same snapshot is passed through every iteration in that target year. No global cache or rebuild from model Yt/Lt.
3. Pass the snapshot explicitly through the integration inputs. Validate year and exact province-axis correspondence before deriving any numerical array. The observed-GDP route must not fall back to the endogenous formula on absent/mismatched data. Any baseline comparison must be separately named, frozen and reviewed.
4. Supply identical destination-by-origin coefficients to both migration labor and composite wages. Do not independently transpose/recompute one branch. Validate both consumers with invented asymmetric fixtures, without executing household/firm/scientific modules.
5. Model target-year population remains unchanged; lagged population is only the denominator of the GDP proxy. No division by three, recalibration, wage/return-law, labor FOC or productivity normalization change is included in this integration design.
6. Preserve complete identities at the boundary. Failure in metadata, year/order, representability or strict coefficient direction is explicit and terminal; no clipping, tolerance weakening or coefficient substitution. Existing scientific budgets and historic ledger uncertainties are not reset.

## Gates before source changes and a numerical comparison

First close price/source/target-year/province bindings, then issue a new exact-path source integration task with zero science and independent review. Annual orchestration is not currently implemented; no production-ready once-per-year behavior is claimed. After integration review, separately define baseline/candidate inputs, safe outputs satisfying retained Objective A, named finite call/time budgets, first-failure accounting and unchanged numerical stopping laws. The current C9 route is not automatically reused or reopened.

An experiment must report numerical validity and convergence separately from economic interpretation. A frozen lagged GDP wedge removes this coefficient's same-iteration endogenous feedback; it does not remove all HANK/K1B feedback or prove convergence. Final dissertation formula selection needs both an economically defensible mechanism and accepted numerical evidence.
