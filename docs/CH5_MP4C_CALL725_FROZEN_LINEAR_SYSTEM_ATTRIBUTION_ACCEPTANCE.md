# P32 frozen linear-system attribution — Reviewer acceptance

Date: 2026-09-07. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Candidate tip: `2ff3eb212ea9a0d101183f9ff49dd1043bb6b886`.
Initial result commit: `30438ea1468ddc59862f40574bd06c8625427e1b`.
Task: `tasks/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.md`.

## Decision
Accepted diagnostic completion:
`FROZEN_LINEAR_SYSTEM_ATTRIBUTION_COMPLETE__TRAJECTORY_AND_GENERATOR_BLOCKERS_OPEN`.

Accept the two-commit candidate into main under Owner standing authorization. All failed numerical comparisons remain failed. This is L3 commit/report acceptance with L4 inspection of the published focused-test log, not independent model execution, full parity, convergence, generator validity, annual coverage or Results acceptance.

## Review actually performed
Live main was read as `80ce3f25ecc4455df15206d6ecab3909552f1b61` and rechecked before publication. GitHub comparison reports the candidate ahead2/behind0 with that merge base; the dedicated branch ref equals the candidate tip. All25 changed paths are additions within the four task-allowed groups: seven validator files, one test file, one report and sixteen small evidence files. No production source, parameter, solver configuration or historical report was modified by the candidate.
Reviewer read the complete report, preparation/binding/scaling code, both single-solve workers, launcher, analysis, test runner/finalizer, all11 test definitions, result/attribution/loaded-input summaries, relevant representation evidence, test log, manifest receipt, and the final commit's log-recovery diff. Current authority at the unchanged main was reused; no historical gates were restarted.

The published raw-log base64 was independently decoded:1472 bytes, SHA256 `7568599EC5860B3078CED7F48113FC6BE44D388BCEF304364053054FBCC9F560`. Reviewer independently counted11 named `ok` lines and the `Ran 11 tests`/`OK` footer. CRLF-to-LF normalization yields Git blob `01171f5976cf7f9bf98e353fc7bac2d3b59d661f`, matching the published readable log. Thus the log-byte mismatch and its appended correction are reconciled without a test/model rerun.
Reviewer did NOT independently execute the11 tests, read Windows MAT/NPZ, recalculate saved scientific arrays, inspect all external manifest entries, or run any scientific solve. The log verification is byte/hash/text processing only. External exact-input checks, residuals, attribution vectors and manifest validation remain Builder evidence inspected through code and published summaries.

## Accepted findings
| Identical linear payload | Cross-language max absolute difference | Scaled maximum | Material coordinates | Frozen-rule result |
| --- | ---: | ---: | ---: | --- |
| M ORIGINAL | 2.802202914153895e-13 | 4.557530133662654 | 383 | FAIL |
| P ORIGINAL | 1.6830981053317373e-13 | 2.738929942147486 | 314 | FAIL |
| M ROW_POW2 | 4.587441537751147e-13 | 7.443459762669312 | 404 | FAIL |
| P ROW_POW2 | 4.4941828036826337e-13 | 7.313384580532408 | 401 | FAIL |

The eight loaded-input receipts report identical binary64 values/support/RHS for each common payload; workers validate reference bits before their single direct solve. This improves on the preceding merely within-tolerance M/RHS comparison. Both originating-language ORIGINAL replays have exact_equal=true and zero difference against their saved predecessor solutions. Both vector decompositions exactly reconstruct the saved P32 split in the reported comparisons. Fixed-input language/solver-path differences and within-solver input sensitivity are both observable at this checkpoint. Their infinity norms cannot be added as causal shares. This does not isolate the sparse backend alone or establish the cause of the entire nonlinear trajectory.

The fixed power-of-two scaling is reversible on these stored payloads. Python solutions are unchanged; MATLAB changes do not consistently improve original-equation backward error. All four cross-language comparisons still fail. No production adoption is supported.

Decimal80 residuals use exact conversion of binary64 operands, with products/sums evaluated at80 decimal digits. They are more informative here than fsum of already-rounded products; they are not high-precision solutions or certified forward-error bounds. At stored row704 both origins have Mii+Aii=0 and local spacing65536, whereas the exact-operand sigma is approximately0.051. This establishes loss of that shift in the stored diagonal, not its full effect on the solution or an independently proven condition number. Scaling an already stored entry cannot recover the omitted term.
The reported MATLAB nearly-singular warning/RCOND is a runtime diagnostic of the existing backslash call, not an independent condition-number experiment. Absence of a warning after scaling does not prove validity.

## Publication correction and evidence limits
The initial publication continued after a raw-log byte assertion failed because Git normalized CRLF. The appended commit records that failure and retains the original history, exact raw bytes and readable log. This is an engineering publication defect with a verified correction, not an unreported numerical retry. Future dependent shell steps must stop on failed required commands; do not add a separate documentation task for this.
Final published manifest receipt: SHA256 `A0FF925E71273345043ACE4F666E07A4C990116E7F7BF6BDC1011853A1C64BDD`,176 artifact entries,26 source/report entries. These counts describe external files, not the25 changed Git paths. The receipt was read, not independently re-hashed against Windows files.
Builder ledger: each language4 direct solves, retries0, HJB/policy and downstream0. Reviewer added0 scientific calls; predecessor budgets remain consumed.

## Route decision
The prescribed P32 linear-attribution question is complete. Do not repeat crossed solvers, tune tolerances, try more row scalings, or launch another long trajectory merely to chase agreement at1e-13.
The independent convergence gap and legacy signed-generator/boundary-leakage problems remain open, including the invalid signs/leakage at M143_FINAL. No KFE/GE/annual/Results release follows.
Next authority: `tasks/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC.md`. It uses saved states to produce concrete drift/conservation witnesses, a repair specification and the minimum explicit scientific decisions. It authorizes no replacement policy, model solve or production change. Boundary/FOC changes are proposals until their scientific authority is resolved; the MATLAB-faithful reference remains frozen.

Sources: the candidate report and `reports/call725_frozen_linear_system_20260907/`; prior policy/operator acceptance at b2d7a814039a585b696d8cc5079b8b9865017501. Historical accepted configurations and their limits are unchanged.
