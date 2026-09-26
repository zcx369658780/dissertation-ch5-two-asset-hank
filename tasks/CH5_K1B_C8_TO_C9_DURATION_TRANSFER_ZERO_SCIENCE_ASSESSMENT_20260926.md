# Current Builder Task — C8 timing transfer and uncertainty assessment

Task ID: `CH5_K1B_C8_TO_C9_DURATION_TRANSFER_ZERO_SCIENCE_ASSESSMENT_20260926`
Status: `ACTIVE__ZERO_SCIENCE_DECISION_EVIDENCE_ONLY`
Issued from HEAD `8dfb3ebc09d754c157c7371dfe4fd66792050dff`; frozen `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`.

Only the existing Codex conversation “第五章 K1B 跨天继续接续” (`01a0d867-be22-7d93-b2fb-0ddff659b686`) may execute this task in `D:\ProjectTemp\c5k1bturn56`. The Owner has placed that conversation in the Codex project `Zotero-Analytical-Workflow`; app-project context does not enlarge repository scope. Never access `deep-learning-hank` or send another conversation to write this tree.

## Authority and preflight

The C8 same-frozen-input measurement is independently `ACCEPT__SINGLE_C8_FROZEN_INPUT_COMPLETE_TIMING_OBSERVATION_ONLY`: one complete process observation of 3,382.203 seconds, numerical terminal `VALID__LEVEL_NOT_MET_AT_BUDGET`. Its one-shot budget is consumed. C9/C10 attempted-call ceilings are adopted, but the prelaunch gate remains `BLOCKED__DURATION_BOUND_UNAVAILABLE`; turn9 has not run; Results eligibility is `FALSE`.

Before writing, verify this archived task and `TASK_CURRENT.md` are byte-identical and committed, `HEAD:src` is frozen, tracked files are clean, and only four protected untracked roots exist. Verify full manifest SHA-256: C6-prime `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`; C7 `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`; C8 `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`; C8 timing science `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`. Stop at the first mismatch; do not repair or change protected roots.

Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, `REVIEW_GATE.md`, `docs/CH5_K1B_C8_TIMING_MEASUREMENT_EXECUTION_INDEPENDENT_REVIEW_20260926.md`, `docs/CH5_K1B_C8_TIMING_MEASUREMENT_EXECUTION_20260926.md`, `docs/CH5_K1B_PROCESS_BOUND_TIMING_ACQUISITION_ZERO_SCIENCE_DESIGN_20260925.md`, and `docs/CH5_K1B_C9_C10_COMPLETE_TURN_TIME_BUDGET_ZERO_SCIENCE_PROPOSAL_20260925.md`. In protected roots read only directly relevant receipts and manifests: C7 entering-C8 manifest/readback, C8 entering-C9 manifest/readback, C8 timing receipt, terminal, science manifest/readback, and their directly named input files if needed for static comparison. Read committed contract or wrapper only to resolve exact provenance; never import or run it. No broad historical search.

## Deliverable

Write exactly two new files: `docs/CH5_K1B_C8_TO_C9_DURATION_TRANSFER_ZERO_SCIENCE_ASSESSMENT_20260926.md` and `EVIDENCE/ch5_k1b_c8_to_c9_duration_transfer_zero_science_assessment_20260926/assessment_receipt.json`. Bind claims to exact source paths and SHA-256, and bind the report hash in the JSON receipt. Record zero model/scientific calls and retries, duration gate status, and Results eligibility `FALSE`.

Statically compare the measured C8 entering bundle with the sealed candidate C9 entering bundle: identity, file shape/size, province order, parameter and recorded environment/version/load fields. Distinguish observed differences from their unmeasured runtime effects. State exactly what the C8 monotonic interval covers and whether measurement overhead is included. Evaluate missing repeat samples, failure/censoring, input variation, load/tail variation, coverage target, uncertainty method, safety margin, and the Asia/Shanghai next-00:00 prelaunch predicate. Decide whether present evidence supports a defensible numeric C9 or C10 `E_upper`; leave it null if not. Do not turn C8 time, file timestamps, task duration, call counts, or guessed multipliers into an upper bound.

Give Owner a short decision table of concrete evidence/risk routes and what new scientific budget or policy change each would require. These are proposals only. Preserve complete-outer-turn checkpoint and cooperative midnight semantics: an in-flight call may cross 00:00; manual interruption or an uncertain call ledger is terminal for the task, not a free retry.

## Hard limits and handback

Model calls 0; scientific calls 0; repeat timing 0; C9/C10 calls 0; retries 0. Do not implement or run a batch runner, resume/intraprocess recovery, interrupt/retry logic, benchmark, solver/economic change, or new output root. Static file parsing, hashing and shape checks are allowed without importing scientific runner modules. Do not modify existing evidence.

Stage and commit only the two deliverable paths. Return commit/parent/tree, the two blob IDs, source hashes and compact findings for independent GPT Work ACCEPT/REJECT. Do not self-accept, edit `TASK_CURRENT.md`, clear the C9 gate, or issue a successor. Results eligibility remains `FALSE`.
