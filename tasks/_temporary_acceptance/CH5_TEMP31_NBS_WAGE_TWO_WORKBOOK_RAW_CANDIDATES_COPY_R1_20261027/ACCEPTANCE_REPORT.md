# CH5 TEMP31 — Two NBS-claimed wage workbooks copied: Independent Bounded Review

TASK=CH5_TEMP31_NBS_WAGE_TWO_WORKBOOK_RAW_CANDIDATES_COPY_R1_20261027
CANDIDATE_COMMIT=a02eb9a830c2bd3b150bc3a425ad38c36604d06c
VERDICT=PASS_BOUNDED_RAW_CANDIDATE_COPY_AND_DELIVERY__NO_MODEL_ADOPTION
STOP=TRUE

## Fixed GitHub identity
- Candidate branch: codex/ch5-temp31-nbs-wage-two-workbooks-copy-20261027-r1
- Final candidate commit: a02eb9a830c2bd3b150bc3a425ad38c36604d06c
- Parent: b7790a0f9cb6d4e061ed87f02d6595ea4d4ba729
- Root tree: fa60415f226c62166e326c6e51d867d550b927a2
- Fixed task commit: a2f3489e99382c56ee35ba55eac15bfdaaa8f04d
- Governance head at review: a2f3489e99382c56ee35ba55eac15bfdaaa8f04d
- GitHub comparison: exactly six new files in the task evidence folder, no unrelated repository file modifications. No fund-closing record appears in this candidate delta.

## Independent artifact checks
- Six remote report files at the candidate commit: five manifest-listed files plus manifest.json.
- All five manifest-listed files were independently fetched at the fixed SHA. UTF-8 length, Git Blob SHA and SHA-256 recomputation: 5/5 PASS.
- Manifest itself independently read, Blob=f1273b273e1d8210f3390575a8030383c3db6b83, bytes=3904; self-excluded by construction.
- Previously uploaded user originals remain available to the reviewer in the conversation container, and their independent original-file checksums are:
  - 分省年度数据_城镇私营单位就业人员平均工(元).xlsx; 12411 bytes; SHA-256=5c790a478a244ca12b4c3c2c682465683c64e2b36bbf1d6f5e430bd79b23f21a.
  - 分省年度数据_城镇单位就业人员工资总额(亿元).xlsx; 13310 bytes; SHA-256=f27313c73dc08e8217aeeefe147ce62d7bc0d7c463ecc651c54c7682682c9dc7.
- Local destination copies are NOT uploaded. Their matching source/destination byte hashes and local sidecar (6348 bytes, SHA-256 87ef3d9a8a072a7eb4e029fb67187b218f7d45a2c21bcb79ad6ba9506628a2c3) remain executor-reported local readback. GPT does not claim independent Windows filesystem access.
- The public receipt records pre/post HEAD, index, refs, existing workbook/receipt and six governance-file identities equal, and excludes exactly three authorized new files when checking other dirty/untracked state. These checks were performed and attested by Codex, not independently run from the Windows filesystem.

## Data handling and scope
- A: private urban unit average annual wage, 2018 raw candidate 30 of 31 provinces; Tibet literal '30' quarantined, no imputation or source-meaning assumption.
- B: urban unit wage bill in RMB 100 million, 2018 raw candidate 31/31; not an average wage or direct household wage.
- Private workbook: 2001–2008 and 2025 full literal '30' years, Tibet 2009–2019 '30', all suspect cells quarantined as metadata.
- Wage-bill workbook: 2001–2003, 2005, 2025 full literal '30' years; 2004 partial literal '30' values, whole year not certified. Historical source label caveat preserved.
- Indicator IDs, original NBS database export permalink/timestamp, revision vintage, exact underlying definitions, sentinel meaning and model eligibility still UNKNOWN/BLOCKED.
- No wage-rate or net-wage variable generated; no source or model code change, scientific test/preflight/model, or data normalization.
- Independent completion event UNKNOWN.

## Layered verdict
artifact_integrity=PASS_BOUNDED_GITHUB_5_OF_5_SHA256_BLOB_BYTES_AND_MANIFEST
source_identity=PASS_BOUNDED_USER_UPLOAD_ORIGINAL_HASH_MATCHES_CODEX_LOCAL_READBACK_CLAIMS
implementation_review=PASS_BOUNDED_COPY_ONLY
numeric_review=NOT_RUN
scientific_review=NOT_RUN
privacy_review=PASS_BOUNDED_NO_RAW_XLSX_WAGE_VALUES_OR_PRIVATE_ABSOLUTE_PATHS_PUBLISHED
actual_terminal=PASS_BOUNDED_TWO_RAW_CANDIDATE_COPIES_AND_DELIVERY__STOPPED
delivery=PASS_BOUNDED
cleanup=NOT_AUTHORIZED_FOR_RESEARCH_EVIDENCE; TEMPORARY_REVIEW_FILES_CAN_BE_REMOVED_AFTER_READBACK
not_completed=LOCAL_DISK_INDEPENDENT_REOPEN;OFFICIAL_INDICATOR_IDS;ORIGINAL_EXPORT_METADATA;ANOMALY_SEMANTICS;PRIVATE_TIBET_2018;MODEL_UNIT_GROSS_NET_AND_EMPLOYMENT_BRIDGE;SCIENTIFIC_ACCEPTANCE

## Protected science state
ACTIVE_TASK=NONE (review disposition)
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
FORMAL_SOURCE_FREEZE=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
SCIENCE_TEST_PREFLIGHT_MODEL_CALLS=0
AUTO_NEXT=FALSE

No next research task is issued by this bounded acceptance.
