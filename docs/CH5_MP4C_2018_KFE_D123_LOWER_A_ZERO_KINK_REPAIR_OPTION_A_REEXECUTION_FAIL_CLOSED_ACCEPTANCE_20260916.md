# CH5 MP4C 2018 KFE D1-D3 lower-a zero-kink repair / Option A reexecution — Reviewer acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`PASS__LOWER_A_ZERO_KINK_REPAIR_ACCEPTED__OPTION_A_CELL5_FAIL_CLOSED_EVIDENCE_ACCEPTED__LIQUID_DIRECTION_SWITCH_REQUIRES_ZERO_SCIENCE_ATTRIBUTION`

Accepted Builder candidate: `054ba005a351d279f98b243bd2891225872ba86e`.

The candidate is one commit ahead of baseline `49af569233685ab082fff0e8a101c1129accc283`. It implements only the authorized active lower-`a` / zero-kink multiplier repair, adds focused tests, and preserves one fresh Option A fail-closed execution with frozen code and no retry.

## Accepted findings

1. The previously identified Cell 0 omission is repaired under the already adopted lower-face KKT law. At active lower-`a`, zero transfer now permits `q_a=p_a+lambda_a`, `lambda_a>=0`, intersected with the D3 zero-kink interval, and uses the preregistered deterministic minimum feasible shadow. Cell 0 selects the repaired branch with `q_a=lambda_a=0.020741942377698892` and marker `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`.
2. Fresh Option A execution advances through Cells 0–4, all `SELECTED_ADMISSIBLE`. This confirms the Cell 0 terminal was an implementation omission rather than rejection of the Owner-selected seed.
3. The first new fail-closed terminal is Cell 5, F-order flat index `5`, coordinate `(5,0,0)`. Its repaired lower-a zero-kink branch is valid on the a side, but the two liquid finite-difference branches cross direction: backward derivative `p_b^B=0.02256028269097067` produces `g_b=+3.3967923469887262`, while forward derivative `p_b^F=0.012481806039037598` produces `g_b=-0.009203423814039269`. Both fail the frozen branch-direction condition.
4. This Cell 5 evidence does not by itself decide whether the corrected interior-liquid selector contract is complete. In particular, Reviewer has not yet established whether repository authority already implies a zero-drift / switching / Hamiltonian branch when backward and forward drifts point toward one another, or whether the Option A derivative pair is structurally incompatible with the currently frozen selector law.
5. Scientific-call ledger is accepted: one policy map started, six selector evaluations, four roots, D2=0, direct HJB solve=0, retries=0, KFE/MATLAB/downstream=0. No scientific code changed after execution freeze.

## Route decision

Do not rerun Option A and do not add a derivative selection rule yet. Before any further selector execution, perform a zero-science algebraic/source-authority attribution of Cell 5.

The attribution must answer whether an interior liquid zero-drift/switching candidate is already required or permitted by the accepted HJB/upwind/Hamiltonian authority, whether the selector omitted a mathematically legal branch, or whether no such branch exists under current authority. It must also distinguish a true mathematical selector omission from a new numerical/economic law requiring Owner decision.

No tolerance fitting, derivative floor, central derivative, averaging rule, drift clipping, new root procedure, seed change, grid/calibration change, HJB solve, KFE solve, or production change is authorized by this acceptance.

Results eligibility remains `FALSE`.
