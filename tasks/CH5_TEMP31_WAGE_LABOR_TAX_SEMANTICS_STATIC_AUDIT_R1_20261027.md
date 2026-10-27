# CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027

STATUS=OWNER_AUTHORIZED__ISSUED_WAITING_CODEX
TASK_TYPE=READ_ONLY_STATIC_ECONOMIC_AND_IMPLEMENTATION_SEMANTIC_AUDIT
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=79b0502feae4c400be3a1cdbd7aad3aa67c55004
CANDIDATE_BRANCH=codex/ch5-temp31-wage-labor-tax-semantics-20261027-r1
TASK_DIRECTORY=tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/
CURRENT_ROUTE=TEMP31_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_AND_DESTINATION_INDEX
WORKFLOW=MANUAL_GITHUB_TASK__LOCAL_CODEX__SSH_CANDIDATE__GPT_FIXED_COMMIT_REVIEW__OWNER_DECISION
SCIENCE_EXECUTION_BUDGET=0
NUMERIC_MODEL_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
HA_HJB_KFE_GE_IRF_BUDGET=0
MODEL_CALLS=0
FORMAL_SOURCE_WRITES=0
DATA_REWRITES=0
EXTERNAL_DOWNLOADS=0
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED

## 1. Purpose: one bounded acceptance question

Compare the actual economic meanings and static source-to-consumer flows of wages, labor, workplace taxes and related units in:
1. the user's dissertation Chapter 5 TeX and cited equations;
2. the ORIGINAL multi-province MATLAB HANK program;
3. the historical Python replication and current Python model source;
4. the isolated TEMP31 workplace-wage-tax route and its actual implementation, if present.

Trace `w`, `wjt`, `tau`, labor supply/demand, `L`, `N`, `n`, `ell`, hours, efficiency, migration, tax application, `sigma` and `phi` WHERE DEFINED; do not assume identically named variables have the same meaning. Show how current scientific model requirements compare against THREE newly preserved Owner-downloaded wage/statistics Excel RAW CANDIDATES. Produce an Owner decision brief, not an implemented wage formula or chosen economic concept.

NO source changes, model runs, calibration, derived net wage, interpolation, or new data collection.

## 2. Frozen authority and evidence

Before reading, verify the intended local worktree identity, branch, HEAD, Git index and refs, dirty/untracked state, and effective AGENTS. Previously reported local science HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e` is a check, NOT permission to switch/reset. In any mismatch or risk, record and STOP rather than repair.

Read at the exact task source commit:
- `docs/CH5_GITHUB_WORKFLOW_AUTHORITY_CURRENT_20261025.md`
- `docs/CH5_INDEPENDENT_REVIEW_RULES_20261025.md`
- `CURRENT.md`, `TASK_CURRENT.md`, `docs/CH5_PROJECT_MEMORY_CURRENT.md`
- `docs/CH5_TEMP31_WORKPLACE_TAX_ROUTE_STATUS_20261025.md`
- this task and the matching documented scientific contracts.

Relevant FIXED prior GitHub sources (not a mandate to re-audit unrelated history):
- `2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0`: published TEMP31 source context / provenance.
- `1072e615062ca85437c06b500d5a301939de6734`: historical data discovery. The 2009 input has common scalar `composite_wage`, `wjt`, `wage_tax`, mapped to all 31 states by historical loader, NOT 31 observed wages.
- `c8e0bb0636a1089a0bf82e1f1b917ad39cf6265f`: official wage source qualification, not a completed verified panel.
- `8de1c89ae04dcfd7b1462c642418a29ae03715d5`: first wage workbook candidate copy.
- `a02eb9a830c2bd3b150bc3a425ad38c36604d06c`: two further workbook copies.

TEMP31 contract already states workplace/destination tax attribution, ONE tax application only, no duplicate deduction inside HA, and destination-indexed `tau_j` when splitting labor. Treat this as DESIGN CONTRACT, not proof current Python correctly implements it.

Historical candidate baseline `ba98537fd5ae004f0aa37d319865da1f1739e503` is NOT silently upgraded to formal V010; historical convergence is not a semantic audit.

Three local raw, unadopted files:
A. `data/external_sources/nbs_provincial_urban_unit_wage_20261027/分省年度数据_城镇单位就业人员平均工资(元).xlsx` 12652 B SHA256 `8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176`. 2018 31/31 raw candidates, `NONPRIVATE_LIKELY__DEFINITION_PENDING`.
B. `data/external_sources/nbs_wage_supplement_20261027/分省年度数据_城镇私营单位就业人员平均工(元).xlsx` 12411 B SHA256 `5c790a478a244ca12b4c3c2c682465683c64e2b36bbf1d6f5e430bd79b23f21a`. 2018 30/31 non-suspect raw candidates; Tibet literal `30` quarantined.
C. `data/external_sources/nbs_wage_supplement_20261027/分省年度数据_城镇单位就业人员工资总额(亿元).xlsx` 13310 B SHA256 `f27313c73dc08e8217aeeefe147ce62d7bc0d7c463ecc651c54c7682682c9dc7`. 2018 31/31 non-suspect raw candidates; wage BILL (亿元), not mean pay (元).

File labels alone do not prove NBS database indicator IDs, export permalink/time, revision vintage, or tax/statistical definitions; all still UNKNOWN. Previous year/cell quarantines for repeated literal `30` remain; do not define its semantic meaning or fill anything.

## 3. Gate A — Actual source identity and static inventory

Discover ACTUAL (not guessed) file/archive-member paths of dissertation Chapter 5 TeX, original MATLAB ZIP/source, original Python HANK code, and isolated TEMP31 branch/patch. If originals are not in the verified local worktree, follow only already documented project paths/archives. Do not search whole disk or unrelated Zotero repository. Record Git ref/Blob or file/archive SHA-256, archive member, TeX equation/section label, function name, source line(s), or a verifiable exact quote. Mark source class clearly: ORIGINAL_SOURCE / HISTORIC_REPLICATION / TEMP31_PATCH / PRODUCTION_CALLER / STATIC_TEST_SPY / DOC_ONLY / UNAVAILABLE.

For each relevant symbol/definition, record the actual:
- economic quantity and mathematical formula;
- scalar/31-province vector/household-type/time dimension;
- residence/origin versus destination/workplace index;
- raw/nominal/real and model-period/frequency/unit, ONLY if supported by source;
- gross/pre-tax, post-tax/disposable, wage bill, marginal product or normalized efficiency wage, ONLY if supported;
- actual producer and consumer in code, plus provenance;
- discrepancies among TeX/MATLAB/historical Python/TEMP31 as PROVEN, SUSPECTED or UNKNOWN.

Distinguish `w` from `wjt`, wage index from observed wage level, `N` from `L`, labor-hour/efficiency weights from population, and `tau` meanings by module. Do not generalize from one caller to all production.

## 4. Gate B — Static source→consumer chain

READ ONLY trace:
1. firm production/labor demand/wage formation and inputs;
2. households' labor choice/endowment, effective units and budget/wage income;
3. movement of workers across origin/destination and the place-indexing of wages/taxes/population;
4. any gross-to-net, payroll, personal tax, transfer, wage-tax `tau`, and proof or potential double tax deduction, with exact equations/call references;
5. old MATLAB→Python historical mapping vs current TEMP31 actual callbacks, including `w/wjt/tau/sigma/phi` source, shape, keys and consumer;
6. wage nominal/real, annual/period, employee/hour/effective labor unit bridges and where the equations/data conversion actually exist versus do NOT EXIST IN READ SCOPE;
7. 2009 scalar historical input and 2018 31-province raw candidates, preserving distinct vintages and source/adoption statuses.

Produce a directed lineage graph in JSON with source and consumer IDs, line citations, flow and confidence. A static suspected defect is NOT a runtime failure. Critical ambiguity must stay UNKNOWN/BLOCKED; stop early if original economic definitions are inaccessible.

NO executing source, project import, programmatic simulation, tests or pseudo-data numbers. Extract only necessary bounded scientific expressions and metadata.

## 5. Gate C — Statistical candidates versus actual model needs

Construct a THREE-row data-source matrix against EACH ACTUAL wage/labor model target identified:
- data kind and observational coverage; exact unit/scope/year; raw source status;
- required model quantity and index/period/tax position as evidenced;
- compatibility DIRECTLY_MATCHES_WITH_EVIDENCE / REQUIRES_OWNER_DECISION_OR_TRANSFORMATION / INCOMPATIBLE_BY_DEFINITION / UNKNOWN;
- missing fields: NBS indicator ID, export timestamp/vintage, private Tibet 2018, administrative province ID, matching worker counts by scope, hours, effective labor, tax/deflator as applicable;
- evidence locations and explicit reasons.

Do not divide wage bill by mean wage to declare employment, do not combine private/nonprivate wages with invented weights, do not define gross→net formulas or labor rates, and do not adopt the 2018 data into model arrays.

Provide Owner decision brief: up to three source-grounded alternatives ONLY IF warranted by actual code/equations, with non-binding advantages/risks, explicit open questions and minimal next evidence required. Do NOT select the economics route or publish a calibration suggestion as a fact.

## 6. Required GitHub-only sanitized review package

Publish ONLY under `tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/` on the isolated `codex/ch5-temp31-wage-labor-tax-semantics-20261027-r1` branch:
- `result.md` — bounded findings and STOP;
- `symbol_semantics_matrix.md` or CSV — source/equation/line-backed symbols by TeX, MATLAB, Python, TEMP31;
- `wage_labor_tax_lineage.json` — actual source→transform→consumer, location/time/tax edges and certainty labels;
- `statistics_to_model_bridge_matrix.md` — three workbooks versus actual model quantities;
- `owner_decision_brief.md` — open decisions and non-binding alternatives;
- `source_inventory.json`, `gap_register.json`, `audit_checkpoint.json`, `privacy_report.json`;
- `manifest.json`, `DELIVERY_FINAL_RECEIPT.json`, `INDEPENDENT_COMPLETION_EVENT.json` (UNKNOWN without independent witness).

Actual code/source context needed for independent review must be inspectable through fixed GitHub paths/line ranges or bounded, sanitized excerpt files. Hashes and summaries alone are insufficient. Avoid publishing confidential dissertation TeX, full MATLAB archives, raw Excel or salary-value rows, Windows absolute personal paths, secrets, or broad unrelated research trees. Publish the public-safe excerpts with precise provenance, not an offline ZIP.

Use the previously authorized ordinary-permission SSH isolated publication mechanism; verify actual final remote commit, parent, tree, individual Git Blob, lengths and SHA-256 at fixed ref. Do not rely on executor self-PASS; GPT performs independent acceptance. STOP.

## 7. Protection / prohibitions

Protect original science worktree HEAD, index, refs, dirty/untracked state and all original files. Read only: no modification or normalization to source/data/code/TeX, no tests, preflights, scientific solver/model calls, HA/HJB/KFE/GE/IRF, steady-state, numerical welfare, calibration, optimization, mutation or model activation. Do not download new data or buy anything. No auto merge/cleanup/next task or formal V010/V011 update.

Acceptance fields: artifact_integrity, source_identity, numeric_review=NOT_RUN, implementation_review=STATIC_TRACE_ONLY, scientific_review=STATIC_SEMANTICS_ONLY__NO_FORMAL_ACCEPTANCE, privacy_review, actual_terminal, delivery, cleanup=NOT_AUTHORIZED_NOT_PERFORMED, not_completed. Keep `FORMAL_SOURCE_FREEZE=FALSE`, `V010=UNCHANGED`, `V011=NOT_STARTED`, `Results=FALSE`, `model_activation=FALSE`, `REAL_GE=FALSE`, `FULL_RUNNER_IO_CLOSURE=BLOCKED`.

No new research task after this one. Final status STOP.
