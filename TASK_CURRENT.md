# Current Builder Task

Task ID: `CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_ZERO_SCIENCE_20260923`

Status: `ACTIVE__ZERO_SCIENCE_RUNNER_PREPARATION_ONLY`

## Authority and objective

The Owner agreed to the separately budgeted same-frozen-state repeat route. Prepare a minimal, reviewable **single-turn turn6 replay runner** and static preflight/comparison contracts. Do not execute the replay in this task. The scientific object is one new evaluation of the sealed entering-turn6 C5 input, producing C6-prime to compare with the already sealed C6. This is not turn7 household and not an outer stopping law.

## Startup and exact input/output references

- Work only in `D:\ProjectTemp\c5k1bturn56`; read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the accepted complete-outer-state dossiers and directly named old turn5/6 runner/receipts. Never access `deep-learning-hank`.
- Verify a clean dispatch HEAD whose parent is `1376297341548d569351b566e1507bdc37b6ef33` and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. GitHub is not a gate.
- Original evidence root: `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/`. Sealed C5 entering JSON `turn6_k1b_input_candidate.json` SHA-256 `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC`; plan `turn6_k1b_frozen_share_payoff_plan.npz` SHA-256 `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34`. Original C6 reference JSON `turn7_k1b_input_candidate.json` SHA-256 `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`; plan `turn7_k1b_frozen_share_payoff_plan.npz` SHA-256 `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E`.
- Frozen distance file `docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv` SHA-256 `51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D`.
- Existing `validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py` is read-only. Its top-level `execute()` runs turn5 then turn6 and uses obsolete remote/preflight/baseline checks; it is **forbidden to invoke**. Reuse its accepted turn6 household/integration semantics only with exact entering-source binding and a new isolated output root.

## Exact allowed writes

1. `validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py`
2. `tests/test_mp4c_k1b_turn6_same_frozen_input_repeat_preflight.py`
3. `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_PREPARATION_20260923.md`
4. `EVIDENCE/ch5_turn6_same_frozen_input_repeat_runner_preparation_20260923/preparation_receipt.json`

Do not edit any other path, including `src/`, the old runner, historical evidence, `CURRENT.md` or `SCIENTIFIC_DECISIONS.md`. Explicitly stage only these four paths and make one local candidate commit. No push, PR or scientific successor.

## Runner contract to implement, not execute

1. Default invocation must be **preflight/dry static inspection only**. An actual replay must require a distinct, explicit future execution authorization identifier and fresh task gate. No household, HJB, KFE, integration, firm, K1B network or GE call in this preparation task, including tests. Do not import a module merely to trigger execution. No synthetic science point.
2. Before any future model call, bind exact sealed C5 JSON/NPZ and reference C6 JSON/NPZ hashes; verify 31 canonical provinces, `S[destination,origin]` 31x31, `raw_ra0_turn5`, `rah_turn6`, state/NPZ bit identities, share columns, frozen distance and production/helper source identity. Capture Python, NumPy, SciPy, BLAS/platform/thread environment. A mismatch must stop with zero scientific calls. The future output root must be new and disjoint from all historical evidence.
3. Future replay is exactly one turn6 evaluation from C5, using source-native initialization, accepted 20x20x2 F-order grid, existing selector/HJB/relaxation/KFE law, canonical serial province order, and at most one complete integration after 31/31 household PASS. Reuse existing accepted functions without changing equations, solver, parameters, grid, tolerances, K1B timing or payoff law. Prepare/seal the following entering-turn7 bundle as part of C6-prime; do not run turn7 household. No retries, warm starts, fallback, rescue or second integration.
4. Put every future attempted call under an **entry-before-call** budget guard and ledger. The proposed single-repeat ceilings are: 31 source-native initializations; 24,800 scalar labor roots attempted and 24,800 returned; 1,581 corrected policy maps and 1,581 D2/Q assemblies; 1,264,800 selector evaluations; scalar selector roots total at most 20,000,000 per province and 620,000,000 globally (existing source hard ceiling, not expected usage); direct HJB updates and post-update checkpoints 50 per province/1,550 globally each; 1,550 relaxation helper calls; 82,150 arithmetic alpha candidates; 31 terminal KFE attempts and at most one per province; SCC/restricted GESVD/normalized stationary candidate/full-Q validation each at most 31; 31 aggregates, 31 firms; household batch, full integration, labor, frozen K1B allocation, C1, wage, monetary, fiscal, completed raw-ra0, lagged next K1B preparation and same-S payoff each at most one. `k1b_feedback_calls=1` is an alias of the one frozen allocation event, not extra feedback. Interior-Z, interior-a and joint root subtypes share the total selector-root budget; do not sum them as independent allowances. Turn7 household, full-space GESVD, retries, solver substitutions, K2/GE/MATLAB/Results each have ceiling zero. A failed attempted call consumes budget.
5. Ensure failed selector/HJB/KFE attempts are not silently lost from the global ledger: the old helper may only merge local counts on normal return. If exact attempted counts cannot be preserved on the first exception, the runner must fail closed as `CALL_LEDGER_UNRESOLVED`, not record zero. Per-category guards must apply before invocation, not only at finalization. If this cannot be implemented without changing production source or scientific law, stop and report the blocker; do not relax the requirement.
6. Comparison of C6-prime against sealed C6 must be post-execution static arithmetic on the same nine fields (`Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0_6,rah_7,S_7`), plus available household/KFE and integration intermediates. Report both float64 bitwise mismatches and full-precision numerical differences with locations/shape/finite checks; use the already accepted four formula families to describe differences. The old value is the sealed reference output, the new value is replay output. Do not compare whole output-file hashes as a numerical equivalence test. Do not apply `1e-6` as a repeatability PASS threshold. Classify exact bitwise match for this pair, legal difference observed, or unavailable field without inventing a tolerance.
7. On first identity, scientific-legality, call-budget, sealing or readback failure, preserve the earliest original terminal and consumed-call ledger; stop globally. No second run. Recheck input/source hashes after execution before any reproducibility conclusion. Even exact agreement would cover this pair only, not an outer error bound, fixed point, GE, MATLAB original predicate or Results.

## Preparation evidence and checks

- The report and receipt must state exact source/reference hashes, code/helper identity, planned output root, budget table and provenance (old two-turn ceiling plus source `MAX_ROOTS_PER_PROVINCE`), first-failure policy, zero literal scientific/model call ledger, and `execution_authorized=false`, `scientific_adoption=false`, `results_eligibility=false`. Do not self-hash the receipt.
- Run only static preflight and tests that verify identity rejection, dry-run default, authorization gate, budget guard, and comparison arithmetic without model evaluation. If a test would call a model, do not run it. Record exact tests and results. Check frozen `src` tree, explicit changed-path inventory, `git diff --check`, output readback and clean worktree after commit.

## Terminal gate

Success: `TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_CANDIDATE_READY__ZERO_SCIENCE__WORK_REVIEW_PENDING`. Work must independently ACCEPT/REJECT the runner and then issue a distinct one-shot execution task before a single model call. Results eligibility remains `FALSE`.
