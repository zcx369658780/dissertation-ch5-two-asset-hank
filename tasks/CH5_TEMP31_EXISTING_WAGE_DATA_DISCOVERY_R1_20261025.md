# CH5_TEMP31_EXISTING_WAGE_DATA_DISCOVERY_R1_20261025

STATUS=ISSUED__OWNER_AUTHORIZED_READ_ONLY_DISCOVERY
TASK_TYPE=LOCAL_EXISTING_DATA_DISCOVERY_ONLY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=b52e3dd2dfce52eb38d4d06365aef78526575d19
CANDIDATE_BRANCH=codex/ch5-temp31-wage-data-discovery-20261025-r1
ACTIVE_RESEARCH_TASK=NONE
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
EXTERNAL_WEB_SEARCH=NOT_AUTHORIZED
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## Goal
Find whether existing local/project archives already contain the wage data and province mapping needed for TEMP31. Owner prefers reusing the previous 31-province data first. This is discovery only; it does not choose a wage definition or authorize model execution.

## Fixed context
Current route: TEMP31_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_AND_DESTINATION_INDEX.
Blockers: authentic canonical net-wage source; real 31-province ID/order joins; authoritative units/period/vintage; production callback and common input-snapshot closure.
D1=B, D2, D3=B remain target/design contracts only.
Relevant evidence commit: 2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0.
Prior audit run: 0e5c56f56a7f446d9748212738b509ee.
Prior audit ZIP: 100834 bytes; SHA-256 00ecaf1cf987956d48379e440015dd39963c84779bc5ba9f94ca2ee2e38431fa.

## Scope: existing sources only
1. Verify local worktree/repository, branch, HEAD, status, index and protected-state fingerprints before reading. Never guess a path.
2. Read effective AGENTS/workflow rules and TEMP31 route status.
3. Search existing workspace, data directories, project docs, local archives, prior TEMP31 artifacts, and relevant tracked/untracked files for wage datasets and metadata. Search Chinese/English terms for wages, salary, labor/employee compensation, average wage, payroll, wage bill, employment/labor, provincial yearbooks. Names are clues, not proof.
4. Prioritize previously used 31-province data. Do not download data, browse the external web, or contact outside services.
5. For each plausible candidate, report repository-relative path or archive/member, format, bytes, SHA-256, Git commit/Blob if tracked, provenance/source citation, period/vintage, province ID/name/order fields, wage variable/definition, unit/frequency, coverage/missingness, nominal/real basis if evidenced, ability to join 31 provinces, and exact header/metadata/line evidence.
6. Inspect metadata, headers, schemas and narrowly relevant rows only. Avoid dumping full datasets. For large files, hash and inspect a bounded sample; do not rewrite.
7. Distinguish raw source, transformed data, model input, cached export, summary and historical receipt. Trace derivation only when existing evidence supports it.
8. Report strongest candidates, conflicts, and UNKNOWN/BLOCKED gaps. Do not infer province order from row order, units from magnitude, gross wage as net wage, or canonical status without a traceable generation chain.
9. Publish a discovery report to the task directory on the dedicated candidate branch using authorized SSH. Do not upload raw sensitive datasets. Include manifest, gap register and delivery receipt; read back remote commit/tree/path/Blob/size/hash.
10. If worktree identity differs, protected state changes, data cannot be safely accessed, or privacy concerns arise, stop and report; do not switch worktrees or invent workarounds.

## Deliverables
Under `tasks/CH5_TEMP31_EXISTING_WAGE_DATA_DISCOVERY_R1_20261025/`:
- result.md: findings, strongest candidates, what they establish/do not establish.
- evidence_matrix.csv or .md: path/member, SHA-256, provenance, years/vintage, province ID/order, wage field/definition, units, evidence references, confidence/gaps.
- source_inventory.json: identity and metadata for each relevant source.
- gap_register.json: unknown/blocked fields and evidence needed.
- manifest.json: delivered report path, bytes, SHA-256, Git Blob and purpose.
- DELIVERY_FINAL_RECEIPT.json: branch, parent, commit, tree, remote readback, budgets and STOP state.
- INDEPENDENT_COMPLETION_EVENT.json: UNKNOWN unless an independent witness exists.

Do not upload raw data, unrelated archives, credentials, private paths/usernames, or a duplicate of the whole worktree. Summaries must preserve exact source identities and citations.

## Forbidden
No scientific source/data edits; no staging, local commit/push of working-tree changes, reset, clean, or destructive checkout; no tests, preflights, project-code imports, model calls, calibration, parameter sweeps, HA/HJB/KFE/GE/IRF, or scientific result generation. Do not change V010/V011/source-freeze markers. No external search or new data acquisition. No follow-up tasks or cleanup.

## STOP and acceptance
Stop after publication and remote readback. Report artifact_integrity; source_identity; numeric_review=NOT_RUN; implementation_review=DISCOVERY_ONLY; scientific_review=NOT_RUN; privacy_review; actual_terminal; delivery; cleanup=NOT_AUTHORIZED_NOT_PERFORMED; not_completed.
The result must state whether existing data can be identified with sufficient evidence, not whether the model is accepted.
