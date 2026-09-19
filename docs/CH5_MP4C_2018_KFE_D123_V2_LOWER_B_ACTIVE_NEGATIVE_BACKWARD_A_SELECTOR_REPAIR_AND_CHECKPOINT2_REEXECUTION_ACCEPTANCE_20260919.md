# CH5 MP4C 2018 KFE D1-D3 V2 lower-b selector repair and checkpoint-2 reexecution acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__REPAIR_AND_REEXECUTION_EVIDENCE_ACCEPTED__V2_CELL100_EIGHT_CASE_CENSUS_COMPLETE__FROZEN_LOCAL_KKT_INCOMPATIBILITY_CONFIRMED__OWNER_SCIENTIFIC_DECISION_REQUIRED`

## Accepted candidate

- baseline live main before task: `5b2e7e159945a70a53fcc5920e2273ae54844be9`
- Builder candidate: `19e12ff6c87b2c08490883851e7c50ef958b9c3d`
- candidate tree: `2d943974de864ee2470dcffef84d3052d0aa727f`
- candidate chain is `3 ahead / 0 behind` baseline; the intermediate commits are the authorized implementation freeze and pre-science freeze
- source-faithful/production paths remain unchanged
- Results eligibility remains `FALSE`

## L3 acceptance

The minimal selector repair is accepted.

The corrected diagnostic selector now uses the lower-face active multiplier domain `q_b >= p_b` for active lower-b negative-transfer screening and preserves the distinct upper-b domain. The newly required active lower-b / negative-transfer / backward-`a` case is represented explicitly. Focused tests passed `53/53`; the repaired selector SHA-256 is:

`DBEB8EDCDA18B14579F36C2B68A50A47C9E717F49E84BC31A2E4E17180E9C327`.

The one authorized checkpoint-2 scientific reexecution is also accepted as fail-closed evidence.

Cells 0-99 preserve the predecessor selected-policy identities exactly, with maximum numeric change 0. The first failure remains flat F index 100, zero-based `(i_b,i_a,i_z)=(0,5,0)`, physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`.

At cell 100 the repaired selector persists the complete frozen eight-case census and still returns `NO_ADMISSIBLE_POLICY`, with zero admissible comparisons.

The newly restored eighth case is:

- active set: `lower_b`
- transfer regime: negative
- `a` derivative: backward
- root: `ROOT_CONVERGED`
- `q_b=0.012457851515416401`
- `d=-0.23013514168909557`
- canonical `g_b=0`
- `g_a=0.00670682022114244`
- rejection: `A_DERIVATIVE_DIRECTION_INCONSISTENT`

The authority-backed active negative/forward-`a` case also converges to a liquid equality root but has `g_a=-0.0005429159000894801`, so it is likewise direction-inconsistent. The zero-kink branch remains transfer-KKT inconsistent, the positive active branch remains a genuine no-root legal rejection, and the slack branches remain rejected by the frozen primal/direction/KKT requirements. Interior-Z remains unavailable at the liquid boundary.

Therefore, after repairing the known implementation omission, every authority-backed frozen local case is now represented and rejected. The supported local scientific classification is:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

This is a statement about the frozen V2 local inputs plus the currently adopted corrected boundary/KKT/derivative law. It is **not** a proof of global nonlinear HJB nonexistence.

## Scientific ledger accepted

The formal run used exactly one fresh V2 policy-map attempt:

- accepted V1/V2/Q1 loads: `1 / 1 / 1`
- selector evaluations: `101`
- scalar roots: `56`
- interior-Z roots: `20`
- Q2 assemblies: `0`
- checkpoint-2 diagnostics: `0`
- direct HJB solves / V2->V3 updates: `0 / 0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/production/outer/GE/annual/shock/IRF/Results: `0`
- scientific retries: `0`

The preserved pre-science blocked launcher attempt is accepted as zero-science and did not consume the scientific attempt. The formal sealed manifest verifies `109/109` entries, total bytes `1,619,867`, SHA-256:

`55B689DCF4DD547CAE650A1353062390148050BC2EE95EA51E16571C2CB30947`.

## Consequence

Because the complete repaired policy map still fails at cell 100, no P2/u2/Q2 exists and no B2/D2/stability/cycle or terminal KFE claim exists.

The previous implementation blocker is closed. The remaining blocker is now scientific: progressing past V2 requires changing or replacing at least one currently frozen scientific/numerical law, domain choice, or trajectory construction. That requires Owner authority.

No successor scientific task is published by this acceptance.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain closed.
