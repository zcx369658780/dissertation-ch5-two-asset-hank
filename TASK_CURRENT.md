# Current Builder Task

Task ID: `CH5_FULL_OUTER_STATE_UNIT_SCALE_PRECISION_EVIDENCE_20260923`

Status: `ACTIVE__ZERO_SCIENCE_EVIDENCE_ONLY`

## Authority and objective

The Owner authorized the next zero-science step after independent acceptance of the complete outer state design: collect **source-bound unit, scale, and numerical-precision evidence** for its proposed eight-vector/one-matrix carrier. This task prepares a reviewable Owner decision; it does not adopt the carrier, norm, scale, tolerance, stopping law, call budget, or turn7 execution.

## Startup and identity

- Work only in `D:\ProjectTemp\c5k1bturn56`. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, `docs/CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_20260923.md`, its independent review, and directly cited current source/sealed evidence. Never access `deep-learning-hank`.
- Before any write, verify clean local HEAD at the Work dispatch commit, whose parent must be `4d80d992e0d5f537a400f586cb526b584342adc0`, and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Record the identities. GitHub is not a gate.
- The turn3–turn6 trajectory is descriptive; turn7 is a prepared input bundle only. Results eligibility stays `FALSE`.

## Exact allowed writes

1. `docs/CH5_FULL_OUTER_STATE_UNIT_SCALE_PRECISION_EVIDENCE_20260923.md`
2. `EVIDENCE/ch5_full_outer_state_unit_scale_precision_20260923/evidence_receipt.json`

Do not modify any other path. After checks, stage exactly these two outputs and make one local candidate commit. Do not push, open a PR, or create a scientific successor.

## Required evidence work

1. For each proposed carrier component `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0,rah,S`, trace the exact definition and unit from active source through source inputs, adapters, update equations, and sealed reports. Distinguish a documented unit from an inferred dimension or empirical magnitude. Track per-person versus provincial aggregate, MU/NU conversions, one-model-period versus calendar rates, and any normalization. State citation path and line/field for each claim; conflicts and missing source declarations remain `UNRESOLVED`.
2. Make an evidence table with component, axis/order, economic unit, typical level and zero/near-zero behavior from already sealed data **only if available**, valid fixed scale candidates and their economic interpretation, numeric representation/precision evidence, and remaining gaps. Any scale candidate is `PROPOSED_NOT_ADOPTED`; do not choose a scale just because a turn3–turn6 level or change looks convenient. Keep portfolio share, raw return, payoff, firm wage, composite household wage, and firm versus household labor distinct.
3. Audit what existing receipts actually bound: HJB/KFE solver gates, integration identities, input/output rounding or serialization, repeated-run evidence if any, and existing static readback. Separate inner solve residuals from outer-map evaluation error, deterministic identity checks from empirical noise estimates, and single-run precision from reproducibility. If no replicated evaluation at the same frozen state exists, label an outer-map noise floor `UNAVAILABLE`; do not manufacture one from adjacent trajectory changes.
4. Provide an Owner-facing decision matrix for each component: supported unit/scale, unsupported threshold evidence, and the smallest *future* evidence or scientific budget that would close the gap if necessary. A future repeated evaluation or probe is a proposal only; this task's model call budget is zero. Do not give an outer tolerance unless a source-backed economic precision target and numerical-error bound both support it; otherwise explicitly mark `UNRESOLVED`.
5. Check whether the proposed nine-component carrier and the frozen-input identity need any correction based on this unit/precision audit. Report a possible design conflict for Work review; do not silently edit the accepted design, source, or scientific decisions.

## Evidence and stop rules

- Receipt: task ID, dispatch/start/precommit HEAD and source tree, all input paths with SHA-256, design-document SHA-256, two output paths, exact changed-path list, per-component statuses, unresolved/conflict list, first failure if any, and literal zero counts for household/HJB/KFE/integration/firm/K1B network/GE/turn7/other model or scientific calls. Do not self-hash the receipt; report its SHA-256 after commit.
- Static reading, bounded text search, parsing sealed numerical files, and arithmetic on already sealed data are allowed. Do not import/execute model modules or scientific validators, rerun a solve, evaluate the K1B map, generate new synthetic model points, or alter any numerical file.
- Stop on an accepted-law/source contradiction, sealed-evidence identity mismatch, need for model execution to establish a claimed fact, or a required mathematical rule change. Preserve the first defect within allowed outputs if feasible. Ordinary missing evidence is `UNRESOLVED` or `UNAVAILABLE`, then continue independent sections.
- Verify only the two allowed outputs changed, `src` tree unchanged, `git diff --check` passes, and all science-call counts remain zero. Worktree must be clean after explicit-path commit.

## Terminal and next gate

Success: `UNIT_SCALE_PRECISION_EVIDENCE_CANDIDATE_READY__ZERO_SCIENTIFIC_CALLS__WORK_REVIEW_PENDING`.

Return candidate commit and output hashes to GPT Work for independent ACCEPT/REJECT. This task cannot authorize turn7 or adopt a convergence law.
