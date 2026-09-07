# Call-725 policy/operator diagnostic — Reviewer acceptance

Date: 2026-09-07. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Candidate: `b2d7a814039a585b696d8cc5079b8b9865017501`.
Task: `tasks/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY.md`.

## Decision
Accepted at L3 repository/commit and published-report scope:
`COMMON_STATE_IMPLEMENTATION_OR_NUMERICAL_DIFFERENCE_LOCALIZED`.
This accepts completion of the bounded diagnostic question, not full common-state parity, independent-trajectory convergence, a valid Markov generator, KFE, annual coverage or Results.
The candidate is authorized for inclusion in main under Owner standing authorization.

## Review actually performed
Live main was independently read as `a55019d4a6fe7b36eb783223e8b20dbc73fa59fb`. GitHub comparison identifies the candidate as its direct child, ahead 1/behind 0. The dedicated branch ref was independently read at the candidate SHA.
All 20 changed paths are additions within the task's four allowed path groups: six diagnostic/wrapper files, one test file, one report and twelve small JSON summaries. There are no deletions or production-source changes.
Reviewer read current governance/status/roadmap/task, candidate metadata/diff, the full report, diagnostic/preparation/launcher/finalizer code, Python wrapper and the relevant MATLAB scientific/capture body, all eight test definitions, and published result, checks, state identities, generator summary, terminal diagnostics and ledger totals.

Reviewer did not access Windows MAT/NPZ, independently execute the eight tests, read raw external test logs, recalculate model outputs, or run MATLAB/Python scientific computations. Test counts in checks.json are Builder-reported summary values; finalize.py writes those counts rather than deriving them from a parsed test log. Do not upgrade them to independent L4 test verification. External manifest readback and source-hash checks remain published Builder evidence, not a new direct file verification by Reviewer. These limits do not prevent this proportionate L3 diagnostic acceptance.

## Accepted findings and qualifications
| Common state | Published comparison | Interpretation |
| --- | --- | --- |
| M24 | 38/38 | Same MATLAB pre-step24 state passes the frozen rule |
| P24 | 38/38 | Same Python pre-step24 state passes the frozen rule |
| P32 | 36/38 | First failure V1, then its stopping statistic; preceding stages pass |
| M143_FINAL | 38/38 | Both maps locally satisfy the original stopping rule at this supplied terminal state |

P32 V1 maximum absolute difference is 8.881784197001252e-14, with 296 material coordinates and maximum scaled V1 difference 1.4168286451819037. The statistic maximum scaled difference is 1.546875. A small absolute difference is still a failure of the frozen rule; the rule is not relaxed.
P32 M/RHS pass within tolerance, not bitwise. M's maximum absolute difference is 65536 at its extreme scale, maximum scaled difference 0.171875; RHS maximum difference is 1.1102230246251565e-15. This localizes the first material difference to the value-update stage but does not isolate solver arithmetic from sensitivity to upstream sub-tolerance differences, or prove ill-conditioning or a formula defect.

The step24 transfer split is at tensor (5,19,0), with derivative ratios on opposite sides of the 0.9 threshold. M24/P24 replay supports a different-state threshold crossing at that cell. It does not prove all possible states equivalent.
Operator growth is traced to the unclamped transfer derivative denominator and quadratic adjustment cost in both frozen sources. Consumption/labor derivative flooring is a different operation. Candidate/margin arithmetic is explicitly reconstructed from saved operands, not independently captured runtime branches.

The stored operators show negative off-diagonals and omitted outward rates in both languages. These are an open legacy numerical-admissibility blocker, not merely a Python-only port defect. At M143_FINAL each side still has 18 negative off-diagonals and 15 leakage cells. Do not release KFE/GE/annual/Results on the basis of stopping agreement or small normwise linear backward error. Faithful reproduction and operator validity remain distinct claims.
At the supplied terminal state the two update distances are 2.6173063716328215e-11 and 2.6199042935104444e-11; both input-state nonlinear defects have infinity norm 1.3374745755356798e-11. This does not show Python's independent trajectory reaches that state.
Python updates 401–500 continue switching in the approximately 0.00862 statistic band; a limit cycle is not proven. The independent convergence gap remains open.

## Budget and successor
Published ledger: each language four invocations, four updates and four direct solves; retries 0; downstream calls 0. This review added zero scientific calls and did not reset any predecessor budget.
The completed task must not be rerun. Next authority is `tasks/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.md`: exact stored P32 systems, crossed direct solves, residual/representation diagnostics and a separately labelled power-of-two row-equilibration probe. No HJB trajectory or production modification is authorized. The scaling probe is an algebraically equivalent frozen-linear-system representation experiment, not adoption of a new HJB algorithm or a repair of signed rates.

Source evidence: `docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_REPORT.md` and `reports/call725_policy_operator_stability_20260907/` at the candidate SHA. Historical first-iteration and trajectory acceptances remain unchanged.
