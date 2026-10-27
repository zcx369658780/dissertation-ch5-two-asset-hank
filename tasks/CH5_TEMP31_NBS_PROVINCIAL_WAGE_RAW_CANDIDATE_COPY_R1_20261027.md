# CH5_TEMP31_NBS_PROVINCIAL_WAGE_RAW_CANDIDATE_COPY_R1_20261027

STATUS=ISSUED__OWNER_AUTHORIZED_LOCAL_RAW_CANDIDATE_COPY
TASK_TYPE=FILE_IDENTITY_PRESERVING_LOCAL_COPY_AND_METADATA_REGISTRATION_ONLY
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=e6cde7e95aa808cabc6623d0e754b60c096695e3
CANDIDATE_BRANCH=codex/ch5-temp31-nbs-wage-raw-candidate-copy-20261027-r1
SOURCE_DIRECTORY=C:\Users\zcxve\Downloads
SOURCE_FILENAME=分省年度数据_城镇单位就业人员平均工资(元).xlsx
EXPECTED_SOURCE_BYTES=12652
EXPECTED_SOURCE_SHA256=8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176
DESTINATION_DIRECTORY_RELATIVE_TO_VERIFIED_LOCAL_PROJECT=data/external_sources/nbs_provincial_urban_unit_wage_20261027
DESTINATION_FILENAME=分省年度数据_城镇单位就业人员平均工资(元).xlsx
SCIENCE_BUDGET=0
TEST_BUDGET=0
PREFLIGHT_BUDGET=0
MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
FORMAL_SOURCE_MODIFICATIONS=0
EXTERNAL_DOWNLOADS=0
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE

## 1. Goal and Owner authorization

Owner directly supplied this Excel and requested that, if suitable, Codex copy one byte-identical original into the verified local dissertation project. GPT has independently inspected the uploaded byte-identity counterpart and accepts it as a CANDIDATE RAW WAGE SOURCE ONLY, not as canonical/model-adopted data. Do not overwrite or transform the original.

## 2. Pre-verified GPT findings (do not expand or promote)
- Workbook SHA-256: 8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176; bytes: 12652.
- One worksheet, `Sheet1`, range `A1:Z36`.
- A4:Z4 contains 31-province labels and years 2001–2025; province rows 5–35 comprise 31 unique province names after trimming whitespace. Header text: `指标：城镇单位就业人员平均工资 (元)`. A36: `数据来源：国家统计局`.
- Column I is 2018 and contains 31 nonblank distinct numeric-looking strings. Example 2018: 福建=74316; 湖南=70221. These match independently identified official 2018 nonprivate urban wage totals.
- Years 2025 and 2001–2005 contain the literal string `30` for every province. These are suspicious and MUST be quarantined, not treated as observed wages.
- Official NBS Q&A says an unqualified `城镇单位` label generally refers to nonprivate urban units; however, the spreadsheet does not provide the full indicator code, definitive definition, database permalink or export timestamp. Classify `NONPRIVATE_LIKELY__DEFINITION_PENDING`.
- This is annual average pay in yuan per urban unit employee for the likely nonprivate sector, not household take-home/net wage, not weighted all-worker mean, and not the model w/wjt without a separately accepted economic/unit bridge.
- `2018_31_CELLS_COMPLETE__SOURCE_AND_MODEL_ELIGIBILITY_PENDING`. No other year admitted. For 2006–2024 data, do not assert annual certification from structural plausibility alone.

NBS definition/provenance references for documentary use:
- https://www.stats.gov.cn/hd/lyzx/zxgk/202407/t20240719_1955719.html
- https://www.stats.gov.cn/hd/cjwtjd/202302/t20230207_1902273.html
- https://tjj.fujian.gov.cn/xxgk/tjxx/gzqk/201905/t20190523_4882127.htm

## 3. Authorized local actions

1. Read the effective AGENTS and current workflow authority from GitHub at this task-issuing commit, and verify the actual repository/worktree identity. Expected historic local worktree identity was `D:\ProjectTemp\c5k1bturn56`, but verify rather than blindly assuming it.
2. In the precise Downloads directory above, verify the exact source filename, 12,652 bytes and SHA-256. If absent or mismatch, STOP without guessing substitutes. Do not enumerate unrelated personal files.
3. Check the exact destination path under the verified project. If a file already exists with different bytes/hash, STOP rather than overwrite. If identical, record ALREADY_PRESENT_IDENTICAL.
4. Copy the original file without modification into `data/external_sources/nbs_provincial_urban_unit_wage_20261027/分省年度数据_城镇单位就业人员平均工资(元).xlsx`. Reopen the destination from disk and independently confirm byte length and SHA-256 match the source. Preserve source in Downloads unchanged.
5. In the SAME destination directory, create a concise `SOURCE_RECEIPT_20261027.json` with original filename, source_role=OWNER_DOWNLOADED_NBS_CLAIMED, source_sha256, bytes, destination-relative-path, workbook/sheet/range metadata, 2018_31_count, accepted_as_raw_candidate=true, official_definitive_indicator_id=UNKNOWN, sector=NONPRIVATE_LIKELY__DEFINITION_PENDING, model_adopted=false, excluded_years=[2001,2002,2003,2004,2005,2025], excluded_reason=ALL_31_LITERAL_30, no_net_wage_conversion=true, provenance_url=UNKNOWN_UNTIL_OWNER_PROVIDES_ORIGINAL_EXPORT_LINK, and readback result.
6. Record local dirty/untracked, index, HEAD and ref fingerprints before/after. Because this task intentionally adds one raw candidate file and sidecar, exempt only those two exact paths from unchanged-state checks. Do not modify or stage existing local files.
7. To provide independent evidence without publishing raw data, publish a sanitized `result.md`, `manifest.json`, `SOURCE_COPY_RECEIPT_PUBLIC.json`, `gap_register.json` and `DELIVERY_FINAL_RECEIPT.json` under `tasks/CH5_TEMP31_NBS_PROVINCIAL_WAGE_RAW_CANDIDATE_COPY_R1_20261027/` on the specified dedicated candidate branch, using approved SSH delivery via a separate isolated Git object/worktree environment. Original workbook must NOT be pushed to GitHub unless Owner explicitly authorizes it. GitHub artifacts are review metadata, not substitutes for the local copy.
8. Remote read back exact candidate commit, parent, tree, all GitHub report paths, Blob SHAs, sizes and SHA-256. Stop and honestly report transport/authentication/tool failures. No alternate account/protocol/privilege escalation or bypass of a denial.

## 4. Strict prohibitions

No external data downloads, web scraping, contacting vendors, modifying source workbook, converting XLSX to CSV, appending wage values to existing model inputs, data imputation, changing production w/wjt/tau/sigma/phi, new salary tax assumptions, formulas or model code, scientific test/preflight, HJB/KFE/HA/GE/IRF, economic parameter changes, MATLAB, source freeze, official results, default/governance branch write during candidate delivery, auto merge/cleanup/next tasks.

## 5. Acceptance and STOP

Success is an exact local raw candidate copy with source/destination byte identity and a sufficient published GitHub receipt. This does not constitute a 31-province net wage panel, accepted common vintage, or model-ready input.

Report separately artifact_integrity, source_identity, implementation_review=COPY_ONLY, numeric_review=NOT_RUN, scientific_review=NOT_RUN, privacy_review, actual_terminal, delivery, cleanup, not_completed.

No cleanup is authorized for the local original or the research candidate. The transient review materials can be handled later under explicit reviewer scope; keep all historical research STOP/PENDING unchanged. Stop after verifying remote delivery.
