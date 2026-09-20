# Task — turn-2 Beijing F0579 upper-b negative-branch root forensic

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_20260920`

Status: `ACTIVE`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_TURN2_BEIJING_CHECKPOINT2_POLICY_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`
6. current selector/cost authority files
7. turn-2 run001 report and sealed evidence
8. exact failure-cell receipt.

No selector change and no HJB rerun are authorized in this task.

## Objective

Determine whether the current active-upper-b negative-transfer pre-root branch-uniqueness rejection at Beijing checkpoint-2 flat 579 is:

A. a false negative because exactly one derivative branch becomes admissible after its own liquid-boundary root is solved;

B. a genuine no-admissible-policy result because no branch passes the existing post-root checks; or

C. a genuine unresolved ambiguity because more than one distinct branch remains admissible within Hamiltonian comparison tolerance.

The forensic is limited to the already persisted failure cell.

## Exact authority binding

Bind run evidence root:

`reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001/`

Require sealed manifest:

`50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`.

Bind exact cell receipt:

`household/p00_北京/checkpoint_002/cell_0579.json`.

Require:

- checkpoint = 2
- flat = 579
- index = `[19,8,1]`
- cell id = `v002_f0579_b019_a008_z001`
- outcome = `NO_ADMISSIBLE_POLICY`
- active upper-b negative candidate rejection includes:
  `DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT`
- active upper-b zero-kink root status:
  `ROOT_FAILURE_NO_UNIQUE_BRACKET`.

Require exact persisted cell scalars and derivatives. Do not reconstruct them from V.

Bind selector parameters from the accepted corrected household authority:

- gamma_c = 2
- phi = 5
- labor_weight = 1
- chi_0 = 0.1
- chi_1 = 2
- a_bar = 1e-6.

## Strict scope

Allowed:

- load persisted JSON;
- call frozen scalar helper equations from selector/cost code;
- deterministic scalar evaluation;
- exactly bounded scalar root solves defined below;
- existing KKT/direction/boundary arithmetic checks;
- serialization, hashes, tests and readback.

Forbidden:

- source-native initialization;
- full policy-map execution;
- selector call over any other cell;
- D2/Q assembly;
- HJB/direct solve;
- SCC/KFE/SVD;
- aggregate/K1A/C1/firm/outer;
- modifying selector/cost/HJB source;
- retrying the turn-2 scientific run;
- changing tolerances/root grids/equations.

## Part 1 — reproduce the current failure

Using only the persisted receipt, reproduce a machine-readable summary of all current candidates and confirm:

- inactive candidates remain rejected for their recorded reasons;
- active zero-kink remains non-rooting under the current allowed upper-b liquid multiplier domain;
- active positive remains inadmissible for the recorded sign/KKT reasons;
- active negative reaches the current pre-root derivative-branch uniqueness rejection.

Do not re-run the full selector.

## Part 2 — active upper-b negative branch decomposition

For active constraint `upper_b` and transfer regime `negative`, examine the two persisted illiquid derivative branches independently:

- backward:
  `p_a=-0.00014542975673859096`
- forward:
  `p_a=-0.0004814219651986697`.

The liquid derivative/shadow endpoint is:

`p_b=0.005058006084641677`.

For each branch separately:

1. use the exact frozen negative-transfer formula;
2. use the same upper-b active liquid shadow domain:
   `0 < q_b <= p_b`;
3. use the same 513-point log-domain bracket screen used by `_one_scalar_root`;
4. execute at most one Brent root if and only if exactly one bracket exists;
5. no retry and no altered grid;
6. evaluate at the resulting root:
   - q_b
   - q_a
   - d
   - cost
   - c
   - l
   - raw g_b
   - g_a
   - upper-b slack
   - upper-b multiplier
   - complementarity residual
   - derivative-direction consistency
   - transfer-sign consistency
   - frozen transfer-KKT residual/target
   - finite checks
   - arithmetic tolerance
   - Hamiltonian under the same existing candidate convention.

Do not introduce any new admissibility condition.

Persist the complete root-screen samples or a deterministic hash plus endpoint/sign-change summary sufficient to prove unique-bracket status.

## Part 3 — switching impossibility check

Using the already persisted cell state, evaluate the existing interior-a switching prerequisite for the active upper-b negative regime.

Persist:

- `d_z=-r_a*a`
- frozen negative-transfer ratio corresponding to d_z
- implied q_b interval from the two a derivatives
- upper-b liquid multiplier domain intersection.

Do not call an interior-a switching root unless the existing frozen prerequisite is satisfied.

This check is descriptive and must follow current code exactly.

## Part 4 — exact post-root classification

Apply only existing post-root candidate checks.

Then choose exactly one classification:

### A
`TURN2_F0579_UPPER_B_NEGATIVE_PRE_ROOT_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED`

iff:

- more than one a branch survives the current pre-root screen;
- branch-specific root evaluation produces exactly one fully admissible distinct policy under all existing downstream checks;
- every other branch is inadmissible;
- there is no Hamiltonian ambiguity.

### B
`TURN2_F0579_TRUE_NO_ADMISSIBLE_POLICY_CONFIRMED`

iff no branch is fully admissible under existing downstream checks.

### C
`TURN2_F0579_MULTIPLE_POST_ROOT_ADMISSIBLE_POLICIES_CONFIRMED__OWNER_DECISION_REQUIRED`

iff more than one distinct policy remains admissible and the existing Hamiltonian comparison does not produce a unique selected policy.

### D
`TURN2_F0579_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION`

for provenance or reproduction inconsistency.

This task does not repair the selector under any classification.

## Scientific-call budget

Maximum:

- failure-cell JSON loads: bounded/read-only
- scalar branch-root invocations: 2
- Brent solves: <=2
- interior-a switching roots: 0 unless current prerequisite is satisfied
- full selector calls: 0
- policy maps: 0
- D2/Q: 0
- HJB: 0
- KFE/SVD: 0
- scientific retries: 0.

## Deliverables

Allowed implementation path:

`validators/multi_province/turn2_f0579_upper_b_negative_branch_forensic/run.py`

Allowed focused test:

`tests/test_mp4c_turn2_f0579_upper_b_negative_branch_forensic.py`

Write:

`docs/CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_REPORT.md`

Create evidence root:

`reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run001/`

Persist:

- authority binding;
- current-candidate reproduction receipt;
- branch-root screen/solve receipts;
- branch post-root admissibility receipt;
- switching-prerequisite receipt;
- classification receipt;
- exact scientific ledger;
- sealed manifest;
- independent readback.

Terminal marker if forensic executes correctly:

`PASS__TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE`

followed by exactly one classification A/B/C/D.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.
