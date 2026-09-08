# Call725 rah=0.07 native-init sensitivity — Reviewer acceptance

Date: 2026-09-09. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Candidate: e3176e9352b4f7e155c91891a4cabdd517e9e232.
Reviewed live main: f455bdb8904f92a027bf6dc4437c75d900835bbb.
Task: tasks/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY.md.

## Decision

Accept the bounded intervention, published execution evidence and the outcome HJB_CONVERGED_AND_KFE_RETURNED. Reviewer marker: CALL725_RAH_0P07_SENSITIVITY_ACCEPTED__STATIONARITY_BLOCKER_REMAINS.
This is NOT a valid stationary-distribution acceptance, MODEL_PASS, a production change, general-equilibrium/rate calibration, corrected-2018 coverage or Results acceptance. The original unmodified stationary residual remains a material blocker. The returned aggregates are diagnostic integrals, not accepted steady-state statistics.

The named remote branch resolves to the candidate; candidate is ahead1/behind0 relative to the reviewed main. All 41 added files are inside the four task-allowed path families. No production/export/helper, old task, calibration or protected source changed. Integration preserves the candidate history with a non-force descendant update.

## Actual review scope

Reviewer read the exact task and active index; report; intervention binding; operator/distribution diagnostics; delivery checks and manifest-readback receipt; final tests_04 log and all 12 test definitions. Reviewer inspected run.py, control.py, evidence.py and the relevant binding, operator and residual portions of analyze.py. Unchanged AGENTS, source/post-loop contracts and earlier evidence were reused.
Evidence labels: L3 commit/scope/code/report review and L4 inspection of published synthetic test logs. Reviewer did NOT independently execute those tests or any scientific solver, read Windows raw NPZ/MAT files, recompute all array diagnostics, or independently rehash the 80 manifest references/39 Git-output LF identities. These external checks remain Builder evidence. Several synthetic tests are simple fixtures rather than integration tests of the complete wrapper; their scope is not expanded beyond what their definitions test.
Final log has 12 named ok entries, Ran 12 tests and OK. Manifest receipt: F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459, 80 verified references, 21 scientific capture files, 12 stages. No extra gate or rerun is required merely to obtain an independent log label.

## Accepted findings

1. The complete copied state changes only rah from .09 to float('0.07'), hex 0x1.1eb851eb851ecp-4. Only mapped HouseholdInputs.r_a changes. Carried ra=.09 and ramax=.09 remain unchanged, as do other scalar/grid/parameter/helper/solver inputs. The wrapper regenerates the original native initialization exactly once; the .09 initial arrays are comparison evidence only. New V0/l0 differences are downstream effects of the approved intervention, not a second chosen intervention.
2. Reused .09 native-init baseline: HJB100 false, statistic .3038218386543494, nonfinite KFE raw solve and no valid density/aggregates. New .09 calls=0. This is not the separate exact-common-MAT MATLAB143/Python500 experiment.
3. New .07: original strict HJB stopping rule passes at update26 with statistic 8.867440115523095e-11. Original KFE and aggregation return. C=10.292627721151788, effective z-weighted L=.6800557026886584, A=7.300066770790965, B=4.69218565897191, A+B=11.992252429762875, mass=.9999999999999999. No new nonlinear fixed-point evaluation was performed.
4. This controlled local change supports sensitivity of this implementation's complete rate-dependent native-initialization/household chain. It does not separate initialization from subsequent rate effects, identify a unique general cause, establish a universally safe .07 cutoff, or warrant changing production ramax.
5. Last HJB iteration operator has 21 negative offdiagonal entries, minimum -4.0056579039558065; max absolute row sum .005241251210036213. Post-loop KFE operator has zero negative offdiagonal entries but max absolute row sum 4.00987105374827. They are distinct operators; the latter's nonnegative offdiagonals do not validate the former.
6. Independent drift-based post-loop boundary-rate reconstruction reports 29 upper-b outward cells, max rate 4.00987105374827, unweighted sum34.068684700799736, row-sum-plus-leak discrepancy2.942091015256665e-15. Other faces have no observed outward drift. The unweighted rate sum is NOT escaped probability mass; that requires density weighting. Counts of slightly negative floating row sums in interior rows are not additional physical leak cells.
7. Contaminated-system raw residual is 2.054563116860031e-17, normwise ratio5.10588263142955e-17. Original unmodified-transpose residual is3.4540415243199343, denominator23.043925230125268, ratio.14988946066377937. That ratio is a matrix/vector-scaled residual, NOT a percentage of population or mass loss. Good solve residual of the row-replaced system and normalization do not establish stationarity of the original system.
8. Density has 160 exact negative entries, minimum -1.5082603896975325e-16 and weighted negative mass -1.0402057506525602e-16. Preserve these signs and magnitudes; do not equate them with the much larger stationary residual or clip them away. A finite nearly nonnegative normalized density is insufficient for acceptance here.

## Budget and retained failures

One Python scientific process, one native initialization, 800 labor-root entries and 800 nested brentq entries, 6654 residual evaluations (1600 bracketing+5054 brentq), one adapter/HJB with26 HJB direct solves, one KFE/direct solve and one aggregation. No scientific restart or launch retry. Actual runtime is reported as2.938 seconds. Source interpreter/library/thread identity with the .09 baseline is supported by the saved environment/report, not an independently inspected local installation.
The first preflight root -001 stopped before science because of manifest/index path binding, then -002 established identity of the external index with its published copy. The mapping-key/array-descriptor test failure and other engineering traces remain preserved. These are not additional HJB runs. All MATLAB, firm/GE/annual/dynamic/IRF and extra diagnostic solves are zero.

## Next complete work unit

Do not repeat the .07 experiment, run more rates, or feed this density into GE. New finite density now permits a mass-balance question that earlier nonfinite .09 output could not answer: localize the unmodified stationary residual, test whether the discarded row supplies an implicit source balancing escaped upper-b mass, and map the implicated coordinates. This remains a hypothesis until the saved arrays close the ledger.
Publish tasks/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION.md with zero new model/solver/evaluator calls. It uses only the original .07 saved objects; no change to boundary law, a_bar, FOC/cost, pinning row, matrix diagonals, solver or price. Do not redo the old D1–D3 specification. Any later boundary/calibration/production choice stays with Owner.
Default Builder model is Owner-designated gpt-5.6-sol / medium; the next task needs no model exception. Model routing is a workflow preference, not a verified runtime setting or a reset of scientific budgets.
Results eligibility=FALSE. Reviewer publication started no local model.
