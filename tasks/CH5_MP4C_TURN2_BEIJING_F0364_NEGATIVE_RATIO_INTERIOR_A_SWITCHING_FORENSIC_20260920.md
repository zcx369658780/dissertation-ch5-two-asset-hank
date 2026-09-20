# Task — turn-2 Beijing F0364 negative-ratio interior-a switching forensic

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_20260920`

Status: `COMPLETED_PASS_ACCEPTED`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_TURN2_RUN002_F0364_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`
6. accepted F0579 repair authority/evidence
7. current selector.py and cost.py
8. exact F0364 failure-cell receipt.

No selector source change and no HJB rerun are authorized.

## Objective

Determine whether F0364 is:

A. a second selector false negative caused specifically by the current
   `ratio <= 0`
   early-return guard in the existing interior-a switching constructor;

B. a genuine no-admissible-policy state after applying the existing switching equations and downstream checks;

C. numerically admissible but scientifically dependent on an unresolved q_a/ratio-sign domain assumption that requires explicit Owner authority;

or

D. forensically inconsistent.

This task is single-cell only.

## Exact evidence binding

Bind:

`reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002/`

Require manifest:

`A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`.

Bind exact cell:

`household/p00_北京/checkpoint_005/cell_0364.json`

with:

- Git blob:
  `5e6528e07998cb6fe3b571cb21c778f3acf3775a`
- SHA-256:
  `F63B2D685F02D74ED3ED560F5DBD02FE5D7FF2B80ABF6D4F64414FFE1FCC7632`
- checkpoint = 5
- flat = 364
- index = [4,18,0]
- cell id = `v005_f0364_b004_a018_z000`
- outcome = `NO_ADMISSIBLE_POLICY`.

Require exact persisted scalars:

- b = `-0.5263157894736843`
- a = `9.473684210526315`
- z = `0.8`
- effective_r_a = `0.8273888725630669`
- effective_r_b = `0.09`
- net_wage = `13.186487914419764`
- transfer_income = `0.1`.

Require exact derivatives:

- p_b_backward = `0.006091715618507631`
- p_b_forward = `0.008179870108012337`
- p_a_backward = `-0.0031029058502000167`
- p_a_forward = `-0.004925792041697845`.

Selector parameters remain:

- gamma_c = 2
- phi = 5
- labor_weight = 1
- chi_0 = 0.1
- chi_1 = 2
- a_bar = 1e-6.

## Part 1 — reproduce current eight-candidate failure

Without a full selector call, reproduce the persisted eight ordinary candidates and verify their exact rejection classes.

In particular confirm for negative transfer + p_b_backward:

- a-backward:
  g_a = `1.1624821053092704`,
  rejection contains only the existing a-direction inconsistency;
- a-forward:
  g_a = `-0.25497146700720563`,
  rejection contains only the existing a-direction inconsistency.

Confirm this is a strict drift crossing under the existing arithmetic bounds.

Also confirm p_b_forward negative-transfer pair does not form the same strict crossing.

## Part 2 — current switching-constructor stop reason

Using the existing formulas only, compute:

`d_z=-effective_r_a*a`

and the frozen D3 negative-transfer ratio:

`R = 1-chi_0 + chi_1*d_z/max(a,a_bar)`.

Persist:

- d_z;
- R;
- current code condition that returns no candidate when `R<=0`;
- sorted illiquid derivative interval.

Do not change or bypass selector.py during this part.

## Part 3 — sign-aware mathematical candidate diagnostic

This is diagnostic only and does not change selector authority.

Because the persisted illiquid derivative interval and R may both be negative, compute the mapped positive q_b set as the exact image:

`{ q_b>0 : q_a=R*q_b lies inside [p_a_min,p_a_max] }`.

Implement this by mapping both interval endpoints through division by R and then sorting the two resulting q_b endpoints.

Do not assume ratio sign.

For each liquid derivative branch separately:

### p_b backward

Use q_b fixed at:

`0.006091715618507631`.

Evaluate whether q_b lies in the sign-aware mapped q_b interval.

If yes construct diagnostic switching shadows:

- d = d_z
- q_b = persisted p_b backward
- q_a = R*q_b
- g_a must be zero up to existing arithmetic canonicalization
- compute c,l,cost,raw g_b,g_b
- apply existing b-direction check
- apply existing transfer-sign/KKT check
- require q_a inside the original illiquid derivative interval
- apply existing finite checks
- compute utility/raw Hamiltonian/final Hamiltonian using the same existing switching-candidate convention.

### p_b forward

Repeat using:

`0.008179870108012337`.

Do not root q_b because F0364 is interior in b and the existing interior-a switching path uses the selected liquid derivative shadow directly when b is not active.

## Part 4 — existing authority consistency audit

Read current selector/cost source and designated current scientific authority docs.

Persist whether any explicit accepted authority outside the implementation guard requires:

- q_a > 0;
- D3 ratio R > 0;
- interior-a switching ratio > 0

as an economic/KKT domain law.

Distinguish:

- explicit scientific authority;
- current implementation condition;
- absence of explicit authority.

Do not infer a scientific permission merely from absence.

## Classification

Choose exactly one:

### A

`TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED`

only if:

- strict a-drift crossing is confirmed;
- exactly one liquid derivative branch yields a switching candidate that passes all existing downstream numerical/KKT/direction checks;
- q_a lies inside the persisted a-derivative interval;
- no explicit accepted scientific authority independently requires positive R or positive q_a.

### B

`TURN2_F0364_TRUE_NO_ADMISSIBLE_POLICY_AFTER_SIGN_AWARE_SWITCHING_DIAGNOSTIC`

iff no sign-aware switching candidate passes the existing downstream laws.

### C

`TURN2_F0364_NEGATIVE_RATIO_SWITCHING_NUMERICALLY_ADMISSIBLE__OWNER_DOMAIN_DECISION_REQUIRED`

iff at least one candidate is numerically admissible but an explicit or unresolved scientific domain assumption prevents treating the current `R<=0` guard as a mere implementation defect.

### D

`TURN2_F0364_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION`

for provenance/reproduction inconsistency.

No selector repair is allowed in this task.

## Scientific budget

Maximum:

- F0364 cell loads: bounded/read-only
- full selector calls: 0
- scalar roots: 0
- interior-a switching roots: 0
- policy maps: 0
- D2/Q: 0
- HJB: 0
- KFE/SVD: 0
- aggregate/integration: 0
- scientific retries: 0
- turn 3: 0.

All computations are deterministic scalar diagnostics from the persisted cell.

## Deliverables

Allowed validator:

`validators/multi_province/turn2_f0364_negative_ratio_switching_forensic/run.py`

Allowed focused test:

`tests/test_mp4c_turn2_f0364_negative_ratio_switching_forensic.py`

Write report:

`docs/CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_REPORT.md`

Fresh evidence root:

`reports/ch5_mp4c_turn2_beijing_f0364_negative_ratio_switching_forensic_20260920_run001/`

Persist:

- authority binding;
- current-candidate reproduction;
- strict-crossing receipt;
- ratio/sign-aware mapped-interval receipt;
- p_b-backward switching diagnostic;
- p_b-forward switching diagnostic;
- scientific-authority/domain audit;
- classification receipt;
- exact zero-root scientific ledger;
- sealed manifest/readback.

## Terminal marker

If the forensic completes:

`PASS__TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE`

followed by A/B/C/D.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.


## Reviewer closure — 2026-09-21

Forensic candidate `5a6f3870ceccb7730d5417e87d801ac0bc8e210a` is accepted.

Terminal:
`PASS__TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE`

Classification:
`TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED`.

The backward liquid derivative yields exactly one sign-aware, D3/KKT-consistent interior-a switching candidate; the forward liquid derivative is outside the mapped interval and direction-inconsistent. The positive-ratio restriction is an implementation guard, not an adopted scientific-domain law.

Acceptance:
`docs/CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_ACCEPTANCE_20260921.md`

Next active task:
`tasks/CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_20260921.md`
