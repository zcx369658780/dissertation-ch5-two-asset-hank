# CH5 Review Path Classifier V1.9 — Synthetic-Only Engineering Task

TASK_ID=CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018
STATUS=ISSUED_NOT_STARTED
SCOPE=ENGINEERING_ONLY / SYNTHETIC_ONLY / NO_ARCHIVE_SCAN / NO_NETWORK / NO_RUNNER / NO_SCIENCE

## 1. Immutable identity
This contract is a read-only original. Read it directly from the fixed issue commit/path and preserve the returned content unchanged. Do not rewrite, template, regex-replace or reconstruct it for validation. Distinguish Git Blob SHA from file SHA256. If only decoded connector text is available, label CONNECTOR_TEXT_VERIFIED. Identity mismatch => read-only STOP.

## 2. Predecessor and fixed facts
Predecessor task: TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018
Predecessor run_id: 447f9775e1b5482f9e3add9344742017
Predecessor terminal: FAIL_CLOSED / STOP before fake-bare or network publication.
Reported issue: URI `https://` was falsely classified as a drive path due to substring `s:/`; after the single E1 repair, a JSON-escaped path fragment remained unresolved. Only 17/491 ZIP members were reviewed (16 classified, 1 unresolved, 474 not reviewed); complete ZIP safety remains UNKNOWN. No candidate was published. Do not resume or edit the predecessor.
This does not prove sensitive data leaked or source files changed.

## 3. Objective
Implement/fix a small path/text classifier and validate it only with synthetic fixtures. Do not access the old source ZIP or scan any of its 491 members. Do not build a new ZIP, do not run fake-bare, SSH, fetch, push, remote readback, Python/Windows resource gate, adapter, runner or model. No science.

## 4. Required types and parser rules
At minimum classify spans as:
- URI
- WINDOWS_DRIVE_PATH
- UNC_PATH
- JSON_ESCAPED_FRAGMENT
- CREDENTIAL_CANDIDATE
- ORDINARY_TEXT
- UNKNOWN

Use syntax/context first, not bare regex as final decision:
1. Parse valid container formats (e.g. JSON with a JSON parser) while preserving raw bytes, parsed strings and offsets; never globally unescape backslashes.
2. A URI scheme such as https:// or ssh:// must not be classified as a Windows drive because a substring resembles s:/.
3. Windows drive path requires path context and structure such as drive-letter colon followed by slash/backslash, excluding URI scheme position.
4. UNC needs valid double-backslash server/share structure.
5. JSON escaped fragment is a serialized-text classification only; it is not automatically a real path or credential. Invalid JSON => FORMAT_PARSE_ERROR/UNKNOWN, no heuristic unescape.
6. Preserve original input and span offsets. Separate classification from security verdict. CREDENTIAL_CANDIDATE means candidate requiring contextual review, not proven leakage. UNKNOWN/unparseable means block publication, not claim leakage.
7. Never execute any inspected text or archive content.

## 5. Synthetic regression suite
Include and report assertions for:
- https://example.test/a/b and ssh://host/path => URI, not drive path;
- C:\Users\demo\file.txt and D:/data/file.txt => Windows path;
- \\server\share\file => UNC;
- valid JSON string with escaped backslashes, distinguishing raw JSON token and parsed string;
- mixed URI/path/JSON text;
- ordinary text containing s:/ not classified as drive path solely by substring;
- real absolute path candidates, credential candidates, malformed JSON, nested-archive metadata and UNKNOWN;
- Unicode, case-insensitive duplicates, traversal candidates;
- input bytes remain unchanged and offset mapping is stable.

Report sample count, per-class confusion matrix or TP/FP/FN where meaningful, negative cases, UNKNOWN count and failures. Do not report only an undifferentiated PASS.

## 6. Bootstrap and protection
Use existing BOOTSTRAP 0/1/2 and V1.5/V1.6 rules. First verify fixed task identity and governance state read-only. Protect finite declared roots; do not recursively scan unrelated dependency trees to infer root identity. For actual intended scratch/target and parent chain, resolve aliases as required. If a relevant target or protected boundary remains unknown, STOP; do not switch paths to evade. No artifact before BOOTSTRAP 0 passes.

Only work in a newly verified independent scratch. Preserve old ZIP, manifest, receipt, source code, old attempts and formal model trees byte-identically.

## 7. Budget
Engineering descendants <=96; Python/focused starts <=24; simultaneous Python <=4; active threads across Python <=32; active engineering time <=90 minutes; batches <=4; new non-Git bytes <=128 MiB. Every cap must be enforced before creation/activation. No network operations, no runner, no archive scan, no science.

E1 syntax/assertion errors may be fixed within the four batches; preserve first error. E2 path protection uncertainty, unexpected network, resource-accounting inconsistency or sensitive data from non-synthetic inputs => immediate STOP.

## 8. Delivery and terminal
Local-only delivery: result.md, manifest.json, source/test SHA index. No ZIP required; no network publication authorized. Delivery must identify run_id, fixed source identities, changed paths, test denominators/results, actual resource usage, first errors, UNKNOWN and STOP point. No model or source evidence modification.

PASS means only the synthetic classifier suite passes; it does not establish old ZIP safety or authorize GitHub publication. Predecessor Delivery V2 remains FAIL_CLOSED. Formal V010 unchanged; model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED; FULL_RUNNER_IO_CLOSURE=BLOCKED.

Final stop: WAIT_ASTRA_PATH_CLASSIFIER_V19_REVIEW.
