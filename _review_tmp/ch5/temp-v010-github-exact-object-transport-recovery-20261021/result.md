# B-only exact GitHub object transport recovery

Task: CH5_TEMP_V010_GITHUB_EXACT_OBJECT_TRANSPORT_RECOVERY_20261021
Run: 9c6e5cf85fbc4e498b479e0f242be939
Effective revision: ISSUED_20261021_R2

Classification: BLOB_EXACT_4_OF_4_VERIFIED. Four native exact-Blob connector calls returned full UTF-8 contents; re-encoded original bytes match all frozen Git Blob SHA1 values. Total decoded source bytes 34923/45000; source requests 4/9. SHA256 and lengths are in response_identity_checks.json.

Exact path reads: NOT_RUN; Blob succeeded, so the conditional fallback was not authorized. No transient source failure, no E1 retry, no provider denial observed. HTTP status is UNKNOWN_NOT_EXPOSED, never guessed as 200. Source directory queries: 0. The delivery baseline tree was read nonrecursively only.

Windows A was not rerun or upgraded. HA/HJB/KFE/GE/IRF/TEMP A0-A3 calls are all zero. Real supervisor/reader, production runtime and production GLOBAL_STOP remain UNVERIFIED. Protected roots were not read or written; OS descendants UNKNOWN. Formal V010 unchanged; Results FALSE; V011 NOT_STARTED. Old PENDING refs were read-only and matched frozen identities.

This package records evidence available before upload. Candidate identities, remote original-byte readback and actual terminal are recorded in the final original JSON. Candidate requires independent Astra review; Codex does not self-accept or clean it. No next task is authorized.
