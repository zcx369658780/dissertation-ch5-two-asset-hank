# Current Builder Task — one C8 same-frozen-input timing measurement

Task ID: `CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION`
Status: `ACTIVE__ONE_SHOT_SEPARATE_C8_TIMING_MEASUREMENT`
Execution authorization ID: `CH5_C8_TIMING_MEASUREMENT_RUN001_20260926`
Authorized output root: `reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001`
Owner adoption SHA-256: `1914E2FE0C6E21E0F767210E6ED55FB3092B1D19A6DC8A9E19821043527F7D1A`
Measurement contract SHA-256: `64E0A111E6C8FC186DB58F188CF55159ADCD3BBF213EF1457EF5EA7AEB569CB5`
Independent review SHA-256: `6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9`
Wrapper SHA-256: `8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A`

GPT Work issues this single scientific attempt only to “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) in `D:\ProjectTemp\c5k1bturn56`. Owner explicitly replied `授权一次 C8 测时`, recorded at `docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_OWNER_ADOPTION.md`. No other conversation may write this tree. Never access `deep-learning-hank`.

## Mandatory prelaunch identity gate

Before invoking the wrapper, verify this active task and `tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION.md` are byte-identical and committed; HEAD descends from Owner one-shot authorization commit `45232f17d18e78f9bf1eb6c80f9aec8dd7c5c49c`; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; no tracked dirt. The only pre-existing untracked roots must be protected C6-prime, C7 and C8, with full execution-manifest SHA-256 respectively `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`. The measurement output root must not exist, including as a link or reparse point. Verify the committed wrapper, independent review, Owner adoption and contract SHA-256 values above. Verify C7's sealed entering-C8 manifest/readback identities `20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E` and `5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA`. Stop at the first mismatch before science. Do not mutate or clean protected roots.

## Exactly one authorized execution

After the gate passes, invoke exactly once from the sole worktree:

`python -B validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py --repository D:\ProjectTemp\c5k1bturn56 --execute --execution-id CH5_C8_TIMING_MEASUREMENT_RUN001_20260926`

The accepted wrapper performs its own committed-authority gate and full C7/C8 preflight before output creation. The fixed contract gives one separate `SEPARATE_C8_TIMING_ONLY` attempt, its exact 39 per-category and five explicit per-province maximum attempted-call ceilings, zero retries, and a cooperative 43,200-second monotonic wall. At the wall, refuse the next scientific entry; an in-flight operation may pass the wall and Asia/Shanghai 00:00 until a safe point. No hard watchdog, parallel runner, resume, rerun, alternate output root, old C6-to-C8 budget or C9/C10 budget is authorized. Every failed attempt counts. If interrupted, uncertain or failed, preserve the first original terminal and ledger; no automatic retry or continuation. Do not change model, economics, solver, grid, tolerance, wrapper, accepted C8 delegate or task/contract during the run.

## Evidence and stop gate

The wrapper may create only its exclusive output root `reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/**`. After the attempt, Builder may create `docs/CH5_K1B_C8_TIMING_MEASUREMENT_EXECUTION_20260926.md` and `EVIDENCE/ch5_k1b_c8_timing_measurement_execution_20260926/execution_receipt.json` to report exact process outcome, attempt ledger, timing/censoring, original numerical terminal, output ownership, science seal/readback and hashes. If prelaunch fails before science, record zero calls and the first gate failure in those same report paths. Stage and commit only those two report paths; never stage the protected or measurement output roots. Return commit/parent/tree, output manifest or failure identity, call ledger and first remaining gate for independent GPT Work review. Do not self-accept or issue a successor.

A complete timing observation does not by itself establish a C9/C10 duration upper bound. C9/C10 prelaunch remains `BLOCKED__DURATION_BOUND_UNAVAILABLE`; Results eligibility remains `FALSE`.
