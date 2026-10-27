# Independent Acceptance — TEMP31 NBS Wage Workbook Raw-Candidate Copy R1

DATE=2026-10-27
TASK=CH5_TEMP31_NBS_PROVINCIAL_WAGE_RAW_CANDIDATE_COPY_R1_20261027
VERDICT=PASS_BOUNDED_COPY_AND_DELIVERY__NO_MODEL_ADOPTION
STOP=TRUE

## Fixed identities
- Candidate: 8de1c89ae04dcfd7b1462c642418a29ae03715d5
- Parent: 59462dda9f8b686a55adcafea578f29d00834302
- Root tree: 097ed3e7df1acdfb720abf5108538c20414fc53b
- Task source commit: 3cc5b64d35fa0be439afb37d12dee7d52550597f
- Candidate branch: codex/ch5-temp31-nbs-wage-raw-candidate-copy-20261027-r1
- Candidate GitHub change scope compared to fixed task: 5 task-folder report files only; no raw Excel uploaded.
- Fixed task manifest has four payload entries and one manifest itself.

## Evidence examined
1. Independently read all four manifest-listed report files at the fixed GitHub commit: DELIVERY_FINAL_RECEIPT.json, SOURCE_COPY_RECEIPT_PUBLIC.json, gap_register.json, result.md. Verified 4/4 Git Blob SHA, UTF-8 byte length and SHA-256. Manifest itself read and its remote Git Blob and directory size checked; manifest intentionally excludes self-hash.
2. Independently checked the original user-uploaded Excel in the conversation working container. Byte length 12652; SHA-256 8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176, agreeing with the task and Codex copy readback.
3. Independent spreadsheet inspection of the uploaded original: Sheet1, 31 province rows, 2018 column present with 31 nonempty numeric-looking strings. 2025 and 2001–2005 province cells contain the identical literal '30' and remain quarantined. No year was newly scientifically certified.
4. Public readback reports source/destination SHA-256 8bb799fc41da5728a52c4958b2da0641ccbc81470a8d6e377625d79b5816b176, both 12652 bytes; local sidecar receipt 2291 bytes, SHA-256 6d66a514fb672b245b018dac2dd513cd126d60a32a636acf2707c0b54450035a. Since the project-local copies are not uploaded and this chat cannot directly access Owner's Windows filesystem, those local copy and sidecar identities remain well-documented executor observations, not independently reopened local bytes.
5. Public receipt records before/after local HEAD, index, refs, six governance file fingerprints and exact-exclusion dirty/untracked status hashes as unchanged, with only two new allowed local files. This is self-reported local protection evidence; no independent Windows worktree read occurred.
6. GitHub comparison from fixed task commit to delivered commit is ahead by two commits and adds exactly five report files in the authorized task directory. No raw workbook is part of the candidate Git commit.
7. The payload receipt references its pre-seal commit 59462dda9f8b686a55adcafea578f29d00834302. The final sealing commit 8de1c89ae04dcfd7b1462c642418a29ae03715d5 has parent 59462dda9f8b686a55adcafea578f29d00834302, so this is consistent two-stage sealing; no circular self-reference is required.

## Boundary and disposition
- Source role: OWNER_DOWNLOADED_NBS_CLAIMED.
- Statistical sector: NONPRIVATE_LIKELY__DEFINITION_PENDING; no exact original NBS indicator ID, export permalink/timestamp or revision vintage.
- 2018: 31 raw candidate values present; this proves no model-ready wage panel or household net wage.
- Years 2001–2005 and 2025 are quarantined due to 31 repeated '30' entries. Other years unadmitted.
- No gross-to-net conversion, w/wjt/tau/sigma/phi write, HA/HJB/KFE/GE/IRF, test, preflight, external download or scientific model result.
- Independent completion event UNKNOWN.

## Layered verdict
artifact_integrity=PASS_BOUNDED_4_OF_4_GITHUB_REPORT_PAYLOADS_AND_MANIFEST_IDENTIFIED
source_identity=PASS_BOUNDED_USER_UPLOAD_HASH_MATCHES_LOCAL_COPY_ATTESTATION
implementation_review=PASS_BOUNDED_COPY_AND_DELIVERY
numeric_review=NOT_RUN
scientific_review=NOT_RUN
privacy_review=PASS_BOUNDED_NO_RAW_WAGE_WORKBOOK_OR_PRIVATE_ABSOLUTE_PATHS_IN_GITHUB_TASK_DIRECTORY
actual_terminal=PASS_BOUNDED_COPY_AND_DELIVERY__STOPPED
delivery=PASS_BOUNDED
cleanup=NOT_AUTHORIZED_FOR_RESEARCH_DATA_OR_TASK_EVIDENCE; ONLY_THIS_TEMPORARY_REVIEW_RECORD_WILL_BE_REMOVED_AFTER_REMOTE_READBACK
not_completed=DEFINITIVE_NBS_INDICATOR_ID;EXPORT_PERMALINK;EXPORT_TIMESTAMP;REVISION_VINTAGE;SCIENCE_UNIT_BRIDGE;PRODUCTION_JOIN;INDEPENDENT_LOCAL_DISK_REOPEN

## Scientific state
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=False
REAL_GE=False
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE

This verdict accepts only the file preservation and bounded delivery, not the wage definition or use in the scientific model.
