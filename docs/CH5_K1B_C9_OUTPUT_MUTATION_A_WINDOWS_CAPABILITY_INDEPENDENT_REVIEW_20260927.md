# C9 safety-A Windows capability candidate: independent GPT Work review

Verdict: `REJECT__TARGET_INTERPRETER_IDENTITY_UNBOUND__NO_SCIENCE`.
Date: 2026-09-27 (Asia/Shanghai).

Candidate `107965099b6dbd31fe6f56db932dbdbd01c82b4b`; parent `bf20d06f20f890eb4fff5f720fbdd666e8e176f9`; tree `1a1c943d4229fafbb0f17ac4005f065164725b56`; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Exactly two allowed files were added: report raw SHA-256 `CEFC809980C5005C9D5BFC62AAF73D3A26587D0F0F9405C295E676CA39322131` and receipt `272B5013874E5BE56FF4E817537B96971033CF1CA9A3782FCFB9276011B5460B`. Tracked/index are clean; six protected untracked roots and seven named manifest/readback hashes match. The one read-only probe, no tests, no temporary mutation and zero scientific calls are preserved facts.

## Blocking identity defect

The probe invoked PATH-resolved `python -` and did not record `sys.executable`. The historical new-C9 execution task explicitly fixed `C:\Users\zcxve\AppData\Local\Programs\Python\Python311\python.exe` as its interpreter. A matching `3.11.9` version string does not prove the probed process is that exact interpreter. Thus `os.supports_dir_fd` results establish only the PATH-resolved process's capability, **not** the specified C9 target build. The report's claims that the target/current C9 build cannot use these stdlib `dir_fd` operations are not established. The original probe's missing independent exit code and stdout/stderr split remain `UNAVAILABLE`; no retrospective rerun is permitted under that consumed probe budget.

The report otherwise separates Python stdlib support, native Windows API contract, and runner integration appropriately. It does not claim that `CreateFileW`, `GetFileInformationByHandleEx` or a handle alone proves ancestor containment. Native handle-relative create/delete remains `UNRESOLVED__FAIL_CLOSED`, and no inert isolation experiment or runner implementation was authorized. The original two prohibited `--execute` probes, all historical REJECT and limited ACCEPT scopes, consumed old/new C9 attempts, both `CALL_LEDGER_UNRESOLVED` actual ledgers and Results eligibility `FALSE` are unchanged.

## Next gate

Only a separate zero-science identity repair task may perform **one** read-only probe by the exact historical interpreter absolute path, record `sys.executable`, version and the relevant support vectors, and correct the target-build wording in new evidence. If the exact interpreter is unavailable or its output cannot be retained, stop with `UNAVAILABLE`; do not infer equivalence from PATH, retry, run mutation experiments, edit runner or start science. Any later isolation study still needs a new task and independent review. This REJECT does not restore C9 budget or authorize C10, retry, partial resume or Results.
