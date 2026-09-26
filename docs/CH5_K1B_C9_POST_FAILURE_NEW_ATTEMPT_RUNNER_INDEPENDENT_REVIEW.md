# Independent GPT Work review - new C9 post-failure runner

Reviewer: GPT Work
Verdict: ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_RUNNER
Scope: STATIC_RUNNER_ONLY__NO_LIVE_CONTRACT__NO_SCIENCE

Wrapper SHA-256: `B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`
Delegate SHA-256: `AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`
Source tree: `00682b2e1a7ba23665f6e16f6acf48ad35874883`

The Owner selected a fresh read-only whole-runner static review and permitted this single R path **only on independent ACCEPT** in `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_REVIEW_PATH_OWNER_SELECTION_A_20260926.md` (raw SHA-256 `752BC6590C626B88542E179E4F2780695F7F334D2E8224BD6876A512822DA0ED`). At review start the local HEAD was `8bfd8329bca07b1208261df0ae5133b7c0da5b82`, tracked files and index were clean, and only the five existing protected output roots were untracked. The wrapper, delegate and focused inert-test bytes are unchanged since final static candidate `96ef5966aae543dd348a8205f06d0cb51d39fb1a`. Their current raw SHA-256 values are the two above and test `F22BCE672DE5D1E62C3BBC7353D822059290F5AEE074147BD6B5F352DB72F3F1`.

The final static-preparation review at `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_STATIC_PREPARATION_INDEPENDENT_REVIEW_20260926.md` (raw SHA-256 `17A6EBFB415A38D225268FFAD501D9FF623CA1C5CF0B4919BB9BC7CB71B34826`) and static receipt (raw SHA-256 `5A24A4C2C68F1513EAE1DDC98E0FC3DDF30F4C5660D4AB2C744D57F54A6CB725`) preserve the two allowed complete inert runs: `61 passed in 2.98s`, then `62 passed in 2.89s` after the `..` case. No code or test bytes changed after the second run. This fresh review independently inspected the unchanged final source and prior evidence without running a test, importing the runner, invoking `--execute`, or calling a model/scientific entrypoint.

The wrapper checks sealed inputs, protected manifests and exclusive output-root absence before its delegate import or science entry; pre-import authority verifies the exact C contract, adopted budgets, R review identity, Owner execution adoption O, and committed byte-identical execution T. The delegate repeats the fail-closed entry checks before model imports. Its budget ledger rejects missing, malformed, negative or non-integral attempted-call counts, and unresolved reconciliation cannot be reported as a resolved terminal ledger. Generated entering-bundle leaves are checked for owned-root, safe path and regular-file status before the old sealer's reads. These are static properties of the fixed bytes, not proof that a full C9 run will complete.

All earlier static-runner REJECT decisions remain historical for their own candidates, as do the limited final-entry and inert-test ACCEPT scopes. The original two prohibited `--execute` probes remain violations and are not reclassified. The 36,000-second wall blocks the next scientific entry after expiry but cannot interrupt an in-flight call. The lstat-before-read checks have an ordinary TOCTOU window; no atomic race-proof claim is made.

This R verdict is a **static runner qualification only**. It does not adopt exact live C bytes, create C/O/T, authorize dispatch or a model call, establish actual old-call counts, or support convergence/Results. At review, C, O, the future execution task-copy and new C9 output root were absent. Old `C9_TIMED_RISK_RUN001` is consumed; actual calls remain `CALL_LEDGER_UNRESOLVED`, and full-old-turn charge is governance accounting only. New C9/C10 science, retries and partial resume remain closed; Results eligibility is `FALSE`. Later live content requires separate exact review and Owner adoption, and any new C9 attempt requires a separate explicit Owner one-shot execution decision and final independent dispatch review.
