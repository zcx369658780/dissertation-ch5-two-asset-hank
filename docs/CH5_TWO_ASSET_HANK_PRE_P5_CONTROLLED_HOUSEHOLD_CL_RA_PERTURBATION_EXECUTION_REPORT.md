# CH5 Two-Asset HANK Pre-P5 Controlled Household C/L and r_a Perturbation Execution

## Verdict

`PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

The source, cache, frozen-input and pre-scientific harness gates passed. The accepted original MATLAB baseline household call at `rah=0.040` was invoked exactly once and returned to the external harness's summary-assignment statement. The external harness then failed on MATLAB struct-container assignment before it could persist the returned baseline object. Because scientific execution had begun, the task forbids editing that harness or rerunning the baseline. MATLAB perturbation and both Python runs were therefore not started. No scientific failure is inferred from this external-container failure, and no P5 acceptance is issued.

## Live authority and workspaces

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live/base `origin/main`: `8aa45b948a0077cd620746ba4688bd93acd46a77`
- accepted Python scientific/test baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence commit: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- snapshot-authority report commit: `079ec59cda8d46d2904af21b04dc8dc4afb301a3`
- isolated Git workspace: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`
- external artifact root: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-artifacts-20260829`
- stale source checkout mutated: no

`git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..8aa45b948a0077cd620746ba4688bd93acd46a77 -- src tests` was empty. Python scientific/test continuity passed.

## Owner-selected MATLAB snapshot and identity gates

- candidate: `C2016-P10`
- year/data index: `2016 / 8`
- province: `P10 江苏省`
- cache: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\Multi_Province_12sts_2016.mat`
- cache bytes: `2442336`
- cache SHA-256: `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A` — PASS
- observed exact loaded `st.results{10}.rah`: `0.040026998056627239` — PASS
- `st.results{10}.convergent == 1` — PASS
- required direct-call fields present — PASS

Accepted original MATLAB identities:

| File | SHA-256 | Result |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |

The diagnostic-patch HJB was not executed. The selected diagnostic-patch cache was used only as a frozen input snapshot.

## Frozen-input proof and harness identities

MATLAB preflight loaded only `st`, selected `st.param`, `st.grids{10}`, `st.num`, `st.CHI`, and two independent copies of `st.results{10}`. Before override, `isequaln(R0,R1)` was true. After setting `R0.rah=0.040` and `R1.rah=0.041`, recursive top-level field comparison found exactly one differing field, `rah`; `isequaln(rmfield(R0,'rah'),rmfield(R1,'rah'))` was true.

Python baseline/perturbation manifests were serialized before scientific execution. Their only difference was `r_a: 0.040 -> 0.041`; Python scientific execution was not started.

| Frozen external artifact | Bytes | SHA-256 |
|---|---:|---|
| `matlab_preflight.m` | 1960 | `AF2B0338097AA5BDD0A8C2B0A9B538CEC2F64E201C47EDB13B1A5034A2D6C50D` |
| `run_matlab_pair.m` | 1935 | `F761D6E4AB6A1E75091B7D54DBAE26C94B88C19EF192B6AAFCF2704C16557ACA` |
| `python_preflight.py` | 1412 | `C0D15A95BC4E3991BF7C8EE907939C5280EF1300F8BB4455372715FC7CD34DE0` |
| `run_python_pair.py` | 6749 | `BEB71A2A3BB9AFA5CECFCC1B9E56FD16AA422DF145C3F1C98D950BF304CE040A` |
| `matlab_snapshot_manifest.mat` | 92192 | `50603C35F94A4B5AD56DE29AC1FBFCE583BF8E5A7BD6410AC39ACF3FCD804101` |
| `matlab_preflight.json` | 319 | `9CEC0C5F7995A2EF071F368D7F0EFA4752E5D363FF73CDC389C31C872C4E90EC` |
| `python_input_manifests.json` | 3255 | `32252AD3899FFE65EC96D31D6A74637A95597502FDCB6BA629C8D0CD2B3F8DA8` |

Pre-scientific checks:

- MATLAB R2022b `checkcode` for the final preflight and scientific harnesses: zero issues;
- Python static compilation for preflight and pair harnesses: PASS;
- MATLAB direct-call resolution to the accepted original source: asserted in the frozen scientific harness;
- P1-P4 reused and not rerun.

## Exact execution counts and terminal blocker

| Scientific household run | Count | Outcome |
|---|---:|---|
| MATLAB baseline, `rah=0.040` | 1 | HJB call returned; result not persisted because external container assignment failed |
| MATLAB perturbation, `rah=0.041` | 0 | not entered after baseline harness blocker |
| Python baseline, `r_a=0.040` | 0 | not entered after terminal four-run gate blocker |
| Python perturbation, `r_a=0.041` | 0 | not entered |

Terminal external-harness error:

```text
Unable to perform assignment because the left and right sides have a different number of elements/structure fields.
run_matlab_pair (line 16)
rows(1) = summarize_output(out0, 0.040);
```

The baseline call immediately preceding that statement was exactly:

```matlab
out0 = HANK_2ASSETS_HJB(st.param, st.grids{10}, st.num, st.CHI, R0, 0);
```

The defect is classified as external output-container plumbing: `rows` was preallocated as an empty-field struct and could not accept the populated summary struct. It is not evidence of an HJB, KFE, convergence, equation, calibration, or production-source defect. Under the no-edit/no-rerun-after-scientific-start rule, the harness was not corrected and the consumed baseline was not rerun.

## Requested aggregate tables

No returned aggregate may be reconstructed or guessed after the failed persistence step. `N/A — NOT PERSISTED / NOT EXECUTED` is therefore reported rather than inventing values.

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | N/A — not persisted | N/A — not persisted |
| Python | 0.040 | N/A — not executed | N/A — not executed |
| MATLAB | 0.041 | N/A — not executed | N/A — not executed |
| Python | 0.041 | N/A — not executed | N/A — not executed |

| Implementation | Delta C_hh | %Delta C_hh | Delta L_hh | %Delta L_hh | A_hh baseline/perturbed | B_hh baseline/perturbed |
|---|---|---|---|---|---|---|
| MATLAB | N/A | N/A | N/A | N/A | N/A / N/A | N/A / N/A |
| Python | N/A | N/A | N/A | N/A | N/A / N/A | N/A / N/A |

Cross-language response differences and sign agreement are not available. No native-level parity tolerance is invented. Accepted shared-input P1-P4 evidence remains the formal parity evidence.

## Validity diagnostics

MATLAB baseline output diagnostics, aggregate identities, convergence and mass checks are `NOT PERSISTED_DUE_TO_EXTERNAL_HARNESS_CONTAINER_BLOCK`. MATLAB perturbation diagnostics and all Python HJB/KKT/generator/connectivity/recurrent-class/KFE/mass-density diagnostics are `NOT_EXECUTED`. The report does not infer a scientific failure from missing persistence.

## Files read and written

Read: the live task, `AGENTS.md`, both required project rules, the accepted snapshot-authority report, blocked predecessor aggregate report, accepted P3/P4 report, accepted Python R4 HJB/KFE/steady-state source, the three accepted MATLAB source/helper files, and the selected cache metadata/content needed for preflight.

Repository write: only this report. External writes: the listed preflight/scientific harnesses, frozen manifests, preflight JSON, and Python bytecode cache. No scientific output JSON was produced.

## Forbidden-operation check

- P1-P4 rerun: no
- outer MATLAB equilibrium/turn/shock or multi-province routine called: no
- diagnostic-patch HJB executed: no
- MATLAB/Python production source or tests modified: no
- selected cache modified/regenerated: no
- input changed beyond `rah/r_a` within either prepared pair: no
- grid, productivity process, initialization, equations, FOCs, KKT/boundary, generator/KFE logic or tolerance changed: no
- consumed MATLAB baseline rerun: no
- harness edited after scientific execution began: no
- MATLAB perturbation or Python runs entered after blocker: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension, dynamics or Results entered: no
- merge, rebase, reset or force-push: no

## Acceptance level and recommended next gate

Acceptance level: supplementary robustness evidence is blocked at external MATLAB result-container persistence. Python R4 acceptance and P1-P4 parity evidence remain unchanged; P5 remains pending.

Recommended next gate: a new, explicit one-shot authority would be required to correct only the frozen MATLAB external output-container preallocation and decide whether the already-consumed baseline may be rerun. Without that authority, do not rerun or infer `CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`.
