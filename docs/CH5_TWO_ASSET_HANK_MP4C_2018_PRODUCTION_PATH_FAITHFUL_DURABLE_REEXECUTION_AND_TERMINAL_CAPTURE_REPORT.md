# MP4C 2018 terminal-capture zero-science regression repair and certification

## Terminal

`MP4C_2018_TERMINAL_CAPTURE_ZERO_SCIENCE_REGRESSION_REPAIRED_AND_CERTIFIED__N_TO_N_BATCH_SEMANTICS_RESTORED__READY_FOR_FINAL_DURABLE_2018_EXECUTION_TASK`

## Authority and continuity

- Live repair-task authority: `00c0d467d84731faf8ff78d2dd6fb0c95dd6d730`, direct child of aborted terminal-capture authority `97f0ac6ff8d4fc5380602c115a5e609f4f632bf5`.
- Before repair, dirty local status and complete diff were copied to fresh no-overwrite external evidence before the safe fast-forward to this live task.
- The certified production-path-parity baseline remains `c225f3ce3eff4a95236f7b7f9f0f6c814119c222`; production worker and model sources were not changed.

## Aborted preflight and confirmed local regression

The prior terminal-capture task stopped at its zero-science gate: `py_compile` passed and focused pytest was `1 failed, 6 passed, 1 warning`. It did not read frozen 2018 input, create a scientific PID, or run stationary, household, production HJB/KFE, MATLAB, R/PLM, shock, or IRF work.

The failure was not a 2018, HJB, KFE, or production-science result. The local terminal-observability edit had moved `outputs.append(...)` outside the `for state, result in completed` loop in `pre_frozen_household_output_batch`. Therefore N completed province results became one final-row output (`N -> 1`), violating the batch's at-least-two-province contract. This is `ZERO_SCIENCE_LOCAL_DIAGNOSTIC_SOURCE_REGRESSION`.

## Bounded repair

The repair restored `outputs.append(...)` to the completed-items loop. Each state/result pair again contributes exactly one ordered row with its own `c_ss`, `l_ss`, `a_ss`, `b_ss`, production-literal faithful-helper `AtTax`, convergence flag, iterations, and statistic. The inherited normal-completion persistence addition remains observability-only.

No change was made to phi formula, timing, or destination-row/origin-column orientation; AtTax formula; HJB/KFE; grid; parameters; controller; migration; capital allocation; firm; wage; monetary; fiscal; Owner-A input semantics; durable ledgers; or capture-before-postmortem behavior.

## Zero-science certification

`python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py` passed.

`python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py` passed: `7 passed, 1 warning`. The only warning is the intentional dummy `MatrixRankWarning` in the existing raw-capture test.

The retained and extended focused coverage verifies two- and three-province N-to-N batch materialization; vector lengths, ordering, province-specific aggregates, independently calculated nonzero AtTax, convergence diagnostics, and prevention of final-row copying. It also retains terminal-result persistence with a valid 31-province synthetic result, phi/AtTax parity, pure one-turn sensitivity, durable HJB-ledger persistence, raw capture before postmortem, and separate postmortem.

Frozen 2018 input reads, scientific PIDs, stationary, household, production HJB, production KFE, MATLAB, R/PLM, shock, and IRF calls are all zero. No retry or scientific repair occurred.

## Evidence and boundary

Fresh no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-2018-terminal-capture-zero-science-regression-repair-20260903-001`

It contains the pre-repair snapshot, live-authority identity, repair diff, two- and three-province receipts, terminal-persistence receipt, compiler/pytest logs, zero-science ledger, report-consistency receipt, and SHA-256 audit manifest.

This repair task does not authorize a 2018 scientific child. A separate final durable 2018 execution task remains required.
