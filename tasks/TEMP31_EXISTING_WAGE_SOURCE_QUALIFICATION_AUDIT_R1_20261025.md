# TEMP31_EXISTING_WAGE_SOURCE_QUALIFICATION_AUDIT_R1_20261025

STATUS=ISSUED__OWNER_AUTHORIZED_READ_ONLY_SOURCE_AUDIT
TASK_TYPE=EXISTING_SOURCE_QUALIFICATION_PLUS_OFFICIAL_SOURCE_AVAILABILITY_DISCOVERY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=9fb8ed823e11234a531aee5b45be0504840cb2dc
CANDIDATE_BRANCH=codex/temp31-wage-source-qualification-20261025-r1
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
NEW_DATA_PURCHASE=NOT_AUTHORIZED
NEW_DATA_DOWNLOAD=NOT_AUTHORIZED
EXTERNAL_WEB_SEARCH=OFFICIAL_SOURCES_ONLY
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## Goal
Audit existing 2018 province-level wage observations and determine whether official National Bureau of Statistics (NBS) or provincial statistical bureau/yearbook sources can fill the documented gaps. This is source qualification and availability research only; do not choose a model wage definition, construct a completed panel, or execute scientific code.

Owner preference: reuse existing 31-province data first; if official provincial yearbooks can fill gaps, identify the exact sources. Commercially prepared data is only a possible later fallback. This task does not authorize contacting sellers, purchasing, downloading paid data, or using unverified marketplace spreadsheets.

## Fixed context
- Current route: TEMP31_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_AND_DESTINATION_INDEX.
- Prior bounded discovery candidate: 1072e615062ca85437c06b500d5a301939de6734.
- Strict 2018/O table S03: 3 numeric private-wage observations and 4 numeric nonprivate-wage observations.
- Flagged table S04: 12 private and 16 nonprivate numeric observations, but mixed source qualification.
- Six cached official source records exist for CQ_W, FJ_P, FJ_NP, HN_P, HN_NP, YN_NP; raw HTML was not uploaded in the prior task.
- Historical 2009 input has common scalar wage/tax fields, not 31 empirical wage observations.
- Existing mapping has 31 explicit province names and MATLAB/Python indices, but production wjt/tau/sigma/phi joins remain unproven.
- Blockers: full comparable 31-province wage panel; source scope/units; gross-to-net bridge; common vintage; matched employment/hour/efficiency weights; production join/callback/snapshot.

## Workstream A — Existing source qualification (first priority)
1. Verify local worktree/repository, branch, HEAD, status, index and protected-state fingerprints. Never guess a path or change worktree state.
2. Read current AGENTS/workflow rules, TEMP31 route status and the prior discovery evidence at the fixed GitHub commit.
3. Audit existing official_source_provenance_2018.csv, source_value_normalization_ledger.csv, official_source_and_endpoint_ledger.csv, official_discovery_receipts.jsonl, source_province_registry.json, S03/S04/S08/S09 and related evidence.
4. For each potentially usable observation record: raw official source vs excerpt/transcription/imputation; province; private/nonprivate and urban/workplace scope; year/publication vintage; annual average vs other measure; gross/pre-tax vs net; nominal/real; unit/denominator; URL; exact evidence pointer; qualification status and reason.
5. Do not count qualifier strings or missing markers as numeric observations. Do not promote S04 merely because its filename says “verified”. Do not infer missing province values.

## Workstream B — Official-source availability discovery
External read-only search is authorized ONLY for official sources: NBS (国家统计局), provincial statistical bureaus, official provincial statistical yearbooks and government publication catalogs.
1. Check whether NBS tables/catalogs provide comparable 2018 province-level annual average wages for urban private and nonprivate units. Record exact title/table/indicator, year, URL, publisher, publication vintage, unit, scope and whether the source table is accessible.
2. If NBS cannot provide a complete usable panel, identify official provincial yearbook/bureau sources for missing provinces and exact tables needed. Do not assume a yearbook/table exists until its official page/catalog entry is found.
3. Build a 31-province × wage-category coverage matrix with statuses FOUND_OFFICIAL_ORIGINAL, OFFICIAL_CATALOG_ONLY, OFFICIAL_PAGE_UNAVAILABLE, NOT_FOUND_IN_BOUNDED_SEARCH, or UNKNOWN. Record search terms and limits.
4. Public page/catalog lookup is allowed. No bulk downloads, scraping behind access controls, CAPTCHA/paywall bypass, or paid-data acquisition. If a yearbook is paid/unavailable, record official title, publisher, edition, catalog page and access condition; do not purchase.
5. Do NOT search or contact Taobao sellers. If official coverage remains insufficient, provide a conditional procurement specification for Owner review: 31 provinces, 2018 annual average wage by private/nonprivate urban units, citations/page/table, units, population scope, vintage, missingness, revision history, raw evidence, license and sample/refund/verification conditions. No purchase is made or authorized.

## Scientific interpretation boundaries
- Official wage observations may be gross/pre-tax and cannot automatically be treated as household net wage or model w/wjt.
- Do not choose wage concept, tax base, mean/median, workplace/resident basis or reference year.
- Do not define tax/hours/efficiency/employment-weight conversion.
- Do not infer a common vintage merely because all observations refer to 2018.
- Do not synthesize, interpolate or create a model-ready wage panel.
- Keep unresolved fields UNKNOWN/BLOCKED.

## Deliverables
Publish under tasks/TEMP31_EXISTING_WAGE_SOURCE_QUALIFICATION_AUDIT_R1_20261025/ on the dedicated candidate branch:
- result.md: decision-ready summary.
- evidence_matrix.csv: qualification of existing observations plus 31-province × wage-category official-source coverage.
- source_inventory.json: title, URL/path, identity, provenance, year/vintage, unit, scope, availability and evidence pointer.
- search_coverage.json: official-site search scope, terms, date and negative-search limits.
- gap_register.json: unresolved gaps and evidence needed.
- procurement_specification.md: conditional fallback only; state no purchase was made/authorized.
- manifest.json: every report path, bytes, SHA-256, Git Blob, provenance and purpose.
- DELIVERY_FINAL_RECEIPT.json: branch, parent, commit, tree, remote readback, budgets and STOP.
- INDEPENDENT_COMPLETION_EVENT.json: UNKNOWN unless a genuinely independent witness exists.

Do not publish raw wage-value tables or local-only datasets unless public and necessary. Prefer metadata, official URLs, table/page citations and minimal public excerpts. Do not publish private paths, credentials or unrelated data.

## Forbidden
No source/data edits, staging, local commit/push of dirty worktree changes, reset, clean, destructive checkout, project-code imports, tests, preflights, model calls, calibration, parameter sweeps, HA/HJB/KFE/GE/IRF, scientific result generation, paid purchase, seller contact or commercial dataset download. Do not change V010/V011/source-freeze markers. No follow-up tasks or cleanup.

## STOP and acceptance
Stop after candidate publication and remote readback. Report artifact_integrity; source_identity; numeric_review=NOT_RUN; implementation_review=SOURCE_QUALIFICATION_ONLY; scientific_review=NOT_RUN; privacy_review; actual_terminal; delivery; cleanup=NOT_AUTHORIZED_NOT_PERFORMED; not_completed.
Success means a bounded evidence-based answer on what can be qualified, official-source routes, and whether procurement merits consideration—not model acceptance.
