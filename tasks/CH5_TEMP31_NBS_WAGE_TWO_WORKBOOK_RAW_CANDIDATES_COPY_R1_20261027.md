# CH5_TEMP31_NBS_WAGE_TWO_WORKBOOK_RAW_CANDIDATES_COPY_R1_20261027

STATUS=ISSUED__OWNER_PROVIDED_TWO_DOWNLOADED_FILES_AND_REQUESTED_PROJECT_RECEIPT_WORKFLOW
SCOPE=TWO_LOCAL_RAW_XLSX_BYTE_IDENTICAL_COPIES_PLUS_ONE_RECEIPT
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=d4ccd0df13e5a166857ae782cc3babb7f66b1cc0
CANDIDATE_BRANCH=codex/ch5-temp31-nbs-wage-two-workbooks-copy-20261027-r1
SOURCE_FOLDER=OWNER_WINDOWS_DOWNLOADS__RESOLVE_LOCALLY
TARGET_PROJECT_RELATIVE_DIRECTORY=data/external_sources/nbs_wage_supplement_20261027
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_WRITES=0
EXTERNAL_DOWNLOADS=0
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## Purpose and frozen source identities

Owner provided two Excel downloads to the GPT reviewer and stated identical files are present in the Windows Downloads directory. GPT independently imported both attached files with a spreadsheet reader; only the following exact filenames, sizes and SHA-256 are authorized:

A. `分省年度数据_城镇私营单位就业人员平均工(元).xlsx`
- Expected bytes: 12411
- Expected SHA-256: `5c790a478a244ca12b4c3c2c682465683c64e2b36bbf1d6f5e430bd79b23f21a`
- Workbook: Sheet1 A1:Z36
- A2 indicator label: 城镇私营单位就业人员平均工资 (元)
- 2018 in column I, province rows 5–35: 31 region labels, 30 non-'30' numeric entries, Tibet (西藏自治区) has literal '30'; do not count Tibet as verified wage.
- 2025 and 2001–2008: all 31 provinces literal '30'; Tibet 2009–2019 also literal '30'. Quarantine suspicious cells/years in metadata only. Their semantic meaning (missing sentinel vs other) is NOT definitively proven.

B. `分省年度数据_城镇单位就业人员工资总额(亿元).xlsx`
- Expected bytes: 13310
- Expected SHA-256: `f27313c73dc08e8217aeeefe147ce62d7bc0d7c463ecc651c54c7682682c9dc7`
- Workbook: Sheet1 A1:Z37
- A2 indicator label: 城镇单位就业人员工资总额 (亿元)
- 2018 in column I, province rows 5–35: 31 non-'30' numeric-looking values.
- 2025, 2001–2003, 2005: all provinces literal '30'; 2004: 25 provinces literal '30', 6 non-'30' values. Quarantine affected values; do not auto-fill/estimate.
- Sheet1 A36 caveat: 1995–2008 城镇单位就业人员工资总额原为劳动报酬总额； preserve the wording, and do not assume complete longitudinal comparability.

Cross-file verification by GPT: the new two workbooks and the previously retained `分省年度数据_城镇单位就业人员平均工资(元).xlsx` have identical 25 year headers and matching 31 explicit province names in the same order AFTER trimming labels. This demonstrates candidate join labels only, not administrative ID or production array identity.

The worksheets claim `数据来源：国家统计局`; no verified database indicator code, original export permalink, export timestamp, revision-vintage, tax/scope/model transformation is attached. Therefore SOURCE_ROLE=OWNER_DOWNLOADED_NBS_CLAIMED; RAW_CANDIDATE_ONLY=TRUE; MODEL_ADOPTED=FALSE.

## Authorized local procedure
1. Read effective AGENTS and current GitHub governance task. Verify the intended scientific worktree identity and state; resolve Windows Downloads using the actual local user environment, not private paths published to GitHub. Do not guess worktree or filename.
2. Read the exact two source files in the Downloads directory. Match filename, bytes and SHA-256 exactly. If either absent or mismatched, STOP WITHOUT COPYING A SUBSTITUTE and report.
3. Check exact target paths under the verified worktree. If a destination already exists with a different hash, STOP rather than overwrite. If identical, report ALREADY_PRESENT_IDENTICAL; otherwise create using an exclusive non-overwriting copy.
4. Reopen original and destination bytes separately; verify exact SHA-256/length and byte-identical state for both. Do not modify or rename user source files.
5. Create a new sidecar `SOURCE_RECEIPT_20261027.json` in the same target directory recording both relative destination paths, original file identities, pre/post byte hashes, owner source claim, discovered sheet/range/units, 2018 candidate coverage, quarantined-year/region metadata, SOURCE_DEF_PENDING, no model adoption, and provenance unknowns.
6. Snapshot exact original HEAD/branch/index/refs and dirty/untracked fingerprints before and after; protect all previous local files, including the already imported prior mean-wage workbook and its receipt. Exactly three newly authorized local paths are exempt (two XLSX and one JSON); no other local modification or staging.
7. Publish sanitized copy evidence to dedicated candidate branch via existing authorized ordinary-permission SSH in an isolated Git object/worktree context. Deliver `result.md`, `SOURCE_COPY_RECEIPT_PUBLIC.json`, `gap_register.json`, `manifest.json`, `DELIVERY_FINAL_RECEIPT.json`, and `INDEPENDENT_COMPLETION_EVENT.json` (UNKNOWN without independent witness). Each source Excel and local sidecar must stay ONLY local; do not push workbook/raw salary rows/personal absolute paths/credentials.
8. Read back the final remote commit/parent/tree/paths/Blob/size/SHA-256 from GitHub, truthfully distinguish payload commit and final sealing commit. STOP.

## Scientific and data constraints
- No original XLSX edit, CSV conversion, missing-value repair, model-ready panel, interpolation, extrapolation, gross-to-net assumption, effective-labor conversion, private/nonprivate weighted synthesis, or production `w/wjt/tau/sigma/phi` binding.
- The previously copied urban-unit average pay file remains `NONPRIVATE_LIKELY__DEFINITION_PENDING`; the private-unit average wage is labelled private directly in its workbook but original NBS indicator identity remains unverified.
- Wage bill (亿元) has different units and object from average annual pay (元/人); do not infer compatible employment without a separately authorized identity and denominator review.
- No new internet downloads, external purchases, source/data rewrites, scientific test/preflight, HA/HJB/KFE/GE/IRF, calibration, tuning, merge, cleanup, auto-next.
- Preserve V010=UNCHANGED, V011=NOT_STARTED, Results=FALSE, FORMAL_SOURCE_FREEZE=FALSE, model_activation=False, REAL_GE=False, FULL_RUNNER_IO_CLOSURE=BLOCKED.

## Acceptance
Report separately artifact_integrity, source_identity, implementation_review=COPY_ONLY, numeric_review=NOT_RUN, scientific_review=NOT_RUN, privacy_review, actual_terminal, delivery, cleanup=NOT_AUTHORIZED, not_completed. Independent review must read the fixed GitHub deliverable and distinguish local Codex attestations from independently accessed files. No follow-up automatically issued.
