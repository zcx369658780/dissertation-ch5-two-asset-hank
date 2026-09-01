# CH5 TWO ASSET HANK MP4B POST LT PREV REPAIR PYTHON CORRECTED2009 ONE SHOT AND PARITY REASSESSMENT REPORT

Date: 2026-09-01

## Terminal verdict

`MP4B_POST_LT_PREV_REPAIR_PYTHON_CORRECTED2009_ONE_SHOT_BLOCKED_NO_RERUN`

The single authorized corrected-calendar-2009 Python stationary execution completed successfully and produced strong material-improvement evidence. The required qualified comparator did not complete: its sole attempt failed immediately because the invocation used a nonexistent module path. The comparator budget is consumed and no rerun was performed. Therefore this execution cannot issue the PASS terminal or claim formal stationary parity.

Scientific evidence classification:

`MP4B_LT_PREV_REPAIR_TRAJECTORY_PARITY_MATERIAL_IMPROVEMENT`

## Live authority and continuity

- Live task authority: `ba98537fd5ae004f0aa37d319865da1f1739e503`.
- Required direct parent: `216283cf4f1303afa60f1915e143a0b7303a9ffb`.
- Execution-start state: `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.
- Repaired `one_turn.py` blob: `e5d6835cdc9e6d182e1c84e11f4d51938be592e1`.
- Frozen `firm.py` blob: `1f7d37247e2d712fc0477a9f562dce81d1b367ce`.
- Driver blob: `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`.
- Binding helper blob: `20123513f232cb2d3cca1264565837e4882ea19f`.
- Accepted comparator blob: `cbe7ce4e4855c139cc7bb3b20b56d124c4add266`.

The repaired mapping was present before science:

`firm_source["Lt_prev"] = float(household.household_lt[index])`

Current destination labor remained `float(migration.lt_supply[index])`.

## Pre-science gate

- Runtime overlay input SHA-256: `072E5E943FB6BFF6768CD40001B031C3AF1A6DD92FCC3A86E1B6D476E03E0137`.
- Binding role: `MATLAB_CACHE_RUNTIME_PARITY_OVERLAY`; it did not replace primary canonical authority `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
- Overlay invariants: 31-province order exact; 24 equal rows; 7 replacement rows; five 1-ULP and two 2-ULP replacements; only `initialized_zt` differed.
- `py_compile`: PASS.
- Focused non-scientific tests: `23 passed in 0.83s`.
- D-drive free space before science: `73,354,334,208` bytes.
- Scientific/model calls before stationary: zero.

The no-overwrite pre-science record is in the external diagnostic root as `pre_science_gate.json`.

## Single stationary execution

Run root:

`D:\ProjectTemp\ch5-mp4b-post-lt-prev-repair-python-overlay-one-shot-20260901-001`

The immutable driver was invoked exactly once with the accepted runtime-overlay input and this fresh root. It exited `0`; no rerun occurred.

- Status: `SOURCE_CONVERGED`.
- Outer iterations: `184`.
- Household calls: `5704`.
- Complete final state: `31` provinces.
- Terminal SHA-256: `A3C1297107504B1023CBB395E558B64DEA5B9DD8515148C4C67BDD6A315D7987`.
- Terminal bytes: `29,480,953`.

## Repair effect versus pre-repair overlay Python

The earliest changed source layer was turn 1, province 1, firm `mt`:

- pre-repair: `1.0080400772138627`;
- post-repair: `1.0121097874161467`;
- absolute change: `0.0040697102022839715`;
- normalized change: `0.004021016546706547`.

This is downstream of unchanged same-turn household outputs, migration, and capital, and is consistent with the authorized firm-reference mapping repair. Runtime serialization did not expose the inner `firm_source["Lt_prev"]`; that mapping remains source- and deterministic-test-backed rather than directly runtime-captured.

Final national post-repair changes relative to the pre-repair Python run were material:

| Field | Absolute change | Normalized change |
|---|---:|---:|
| `Ct` | 6.863736174592475 | 2.4220026575654408e-2 |
| `At` | 0.8413778102479483 | 1.7544958143310745e-2 |
| `Bt` | 0.06778308158027357 | 1.0382933987775872e-3 |
| `Yt` | 28910.70895987749 | 8.246404849639129e-5 |

Final wage-upper count moved from `5` to `7`; wage-lower remained `17`; ra-upper and ra-lower remained `0`; household convergence remained `31/31`.

## Post-repair Python versus preserved MATLAB chronology

- Turn-1 entry `Zt`: `31/31` binary64 exact.
- The earliest remaining continuous source-layer difference is still turn 1, Beijing, `household_outputs.Ct`: MATLAB `11.400731651946101` versus Python `11.400731651949162`, MATLAB-minus-Python `-3.0606628342866316e-12`. The repair occurs after household production, and the new turn-1 Beijing household output is binary64-identical to the pre-repair overlay output.
- Protected MATLAB carried `Lt_1` is supplied by same-turn household `Lt=0.6476235981139693`; repaired Python supplies the same role from `household_lt=0.647623598114104`. This is the already documented representation-scale household difference, not a role mismatch. The resulting Beijing firm `mt` is binary64 exact: MATLAB and repaired Python both equal `1.0121097874161467`, versus pre-repair Python `1.0080400772138627`.
- The former turn-8 Shanghai/Qinghai reset exchange disappeared: post-repair Python reset indices equal the preserved MATLAB set, excluding indices 9 and 26 and including index 29.
- The former turn-154 Zhejiang MATLAB-only low action disappeared: post-repair Python includes coordinate `(154, 11)`.
- Final category counts are exact: household convergence `31`, wage upper/lower `7/17`, ra upper/lower `0/0`.
- Maximum normalized difference across the final 31x20 frozen fields in the independent read-only extraction was `3.835889478194021e-11`.

Final national differences versus preserved MATLAB were:

| Field | Absolute difference | Normalized difference |
|---|---:|---:|
| `Ct` | 7.048583938740194e-12 | 2.487229782359025e-14 |
| `At` | 2.595257342363766e-10 | 5.41179965626544e-12 |
| `Bt` | 1.4878764886816498e-11 | 2.279111985436448e-13 |
| `Yt` | 2.562999725341797e-6 | 7.311227289308414e-15 |

These results support material trajectory-parity improvement. They do not establish formal parity because the accepted qualified comparator did not complete.

## Comparator failure and no-rerun disposition

Eligibility was established: the new terminal was readable and contained a complete 31-province final state. The sole comparator attempt then failed before comparison with:

`ModuleNotFoundError: No module named 'validators.multi_province.compare_mp4b_final_state'`

The accepted comparator actually resides at `validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py`; however, the task allowed no comparator rerun. No second invocation was made and no `qualified_final_state_comparison.json` was fabricated.

## Scientific call ledger

- MATLAB calls: `0`.
- Python corrected-2009 stationary: `1`; reruns: `0`.
- Separate household/HJB/KFE: `0`.
- Standalone MP2/MP3: `0`.
- Qualified comparator attempts: `1`; completed comparisons: `0`; reruns: `0`.
- Other years/batch: `0`.
- Shocks/AR(1)/transition/dynamics/IRF: `0`.
- R5/Results: `0`.

## External evidence

Diagnostic root:

`D:\ProjectTemp\ch5-mp4b-post-lt-prev-repair-parity-reassessment-20260901-001`

It contains the required pre-science gate, Python-vs-Python comparison, Python-vs-MATLAB read-only chronology comparison, Beijing source-chain disposition, controller disposition, scientific-call ledger, diagnostic manifest, and an additive `matlab_chronology_reassessment_supplement.json` created after independent closeout review identified two missing explicit fields. No earlier diagnostic artifact was overwritten. `qualified_final_state_comparison.json` is absent by design because the sole comparator attempt did not complete. The initial manifest records the original persisted evidence. The additive supplement receipt is `2,066` bytes, SHA-256 `5E733433F2F987E683692D77BAB3F6B0EC108FAA4111F3CBB313BA2BB4A92FE5`, and is also recorded without overwrite in `diagnostic_manifest_supplement.json`.

## Scope statement

No MATLAB process, separate household/HJB/KFE run, standalone MP2/MP3 replay, other year, batch, shock, AR(1), transition, dynamics, IRF, R5, or Results execution occurred. No source, validator, test, rule, task index, threshold, tolerance, MATLAB, canonical, or binding artifact changed. The repository mutation is this report only.

## Exactly one recommended next gate

Independent L3 review of this blocked no-rerun evidence package, including a decision on whether a separately published comparator-only task may consume a new comparator authorization against the already completed immutable Python terminal; no stationary rerun is recommended or authorized.
