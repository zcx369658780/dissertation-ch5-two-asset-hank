# CH5 Two-Asset HANK Pre-P5 Controlled Household C/L Persistence Correction and Reexecution

## Verdict

`PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

The corrected external MATLAB persistence/container path passed its mandatory synthetic plumbing preflight. The replacement MATLAB baseline at `rah=0.040` and the MATLAB perturbation at `rah=0.041` were each invoked exactly once, and both raw returned objects were persisted before summary construction. Both MATLAB outputs passed the exposed convergence, aggregation, finiteness, and normalization checks.

The Python baseline and perturbation were then each executed exactly once. Both `run_one` calls returned to the final output-construction path, but final JSON serialization failed with `TypeError: Object of type bool is not JSON serializable`. No Python result object was persisted. Because scientific execution had completed and the task forbids harness editing or rerun after a scientific failure, the Python harness was not corrected and neither Python rate was rerun. This is an external result-serialization blocker, not evidence of a Python scientific numerical failure. P5 remains pending.

## Live authority and continuity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live task/base `origin/main`: `4bc7cc00d36aab144a63387b737f1ed40200c034`
- task: `CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION`
- accepted predecessor report: `240fe1432722eac6996a1093c5783c102ef91aba`
- accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- isolated Git workspace: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`
- new external artifact root: `D:\ProjectTemp\ch5-pre-p5-controlled-household-persistence-reexec-artifacts-20260829`
- predecessor artifact root: preserved read-only in substance; no predecessor artifact was overwritten
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..4bc7cc00d36aab144a63387b737f1ed40200c034 -- src tests`: empty

Python production source and tests therefore remain identical to the accepted scientific baseline. P1-P4 were not rerun.

## Source, cache, and frozen-input identities

| Object | SHA-256 | Result |
|---|---|---|
| accepted original `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| accepted helper `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| accepted helper `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |
| selected cache `Multi_Province_12sts_2016.mat` | `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A` | PASS |

The selected object remained `C2016-P10`, year `2016`, province `P10 江苏省`, with exact loaded native `rah=0.040026998056627239` and saved `convergent=1`. The accepted original HJB was resolved directly; the diagnostic-patch HJB was not executed.

The predecessor MATLAB snapshot manifest was copied byte-identically: 92192 bytes, SHA-256 `50603C35F94A4B5AD56DE29AC1FBFCE583BF8E5A7BD6410AC39ACF3FCD804101`. The predecessor Python input manifest was copied byte-identically: 3255 bytes, SHA-256 `32252AD3899FFE65EC96D31D6A74637A95597502FDCB6BA629C8D0CD2B3F8DA8`.

For MATLAB, `R0` and `R1` were independent copies of the same `st.results{10}` and passed pre-override `isequaln`. After override, removing `rah` made them exactly equal. For Python, the serialized manifests differed only at `r_a: 0.040 -> 0.041`. No other economic or numerical input changed within either pair.

## Predecessor defect and replacement authority

The predecessor MATLAB baseline returned from the accepted HJB but failed at `rows(1) = summarize_output(out0, 0.040)` because `repmat(struct(),1,2)` created an incompatible empty-field container. The predecessor output was not persisted. The current live task explicitly authorized one fresh replacement baseline only after correction and freeze of this external plumbing.

## Complete predecessor-to-corrected MATLAB harness diff

```diff
--- run_matlab_pair_predecessor.m
+++ run_matlab_pair.m
@@
-artifact_root = 'D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-artifacts-20260829';
+artifact_root = 'D:\ProjectTemp\ch5-pre-p5-controlled-household-persistence-reexec-artifacts-20260829';
@@
-rows = repmat(struct(), 1, 2);
 out0 = HANK_2ASSETS_HJB(st.param, st.grids{10}, st.num, st.CHI, R0, 0);
-rows(1) = summarize_output(out0, 0.040);
-assert(rows(1).convergent == 1);
+save(fullfile(artifact_root, 'matlab_out_0040.mat'), 'out0', '-v7');
+summary0 = summarize_output(out0, 0.040);
+assert(summary0.convergent == 1);
 out1 = HANK_2ASSETS_HJB(st.param, st.grids{10}, st.num, st.CHI, R1, 0);
-rows(2) = summarize_output(out1, 0.041);
+save(fullfile(artifact_root, 'matlab_out_0041.mat'), 'out1', '-v7');
+summary1 = summarize_output(out1, 0.041);
+rows = [summary0, summary1];
```

The complete diff artifact is 1441 bytes, SHA-256 `13D7E722AB55BBDC45B9699CAC09EFD33ED4ADB495497B71D72F19D6D6792259`. All modifications are confined to artifact-path plumbing, immediate raw persistence, and compatible summary collection. The two scientific calls and every scientific input are unchanged.

## Mandatory plumbing preflight and harness freeze

Exactly one pure-plumbing preflight was executed before any HJB call. It used two synthetic raw structs and two synthetic summary structs with the exact production summary field names and types. It proved:

- both raw `.mat` save/load round trips succeeded;
- independent `summary0` and `summary1` collection into `rows` succeeded;
- field names, order, and classes matched;
- JSON encode/decode and file write succeeded;
- no model, HJB, KFE, or numerical solver was called.

Preflight result: `PLUMBING_PREFLIGHT_PASS`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| corrected `run_matlab_pair.m` | 2088 | `0CF4C88A9DF80C410C03157E95DD1165209257C9085E4CFD67DF9069190EC4CA` |
| `matlab_plumbing_preflight.m` | 2374 | `0F351E700EBD11181243B168F9242FABD38E0AAEA7E035035C0A0E1D1A9ADB1C` |
| plumbing JSON | 925 | `433CA7652035934ADA7AACA23F6F800C34B780CDD4110472B64C95032D763E3D` |
| plumbing MAT evidence | 915 | `0C12276971AC56FA23C59B45FE3EA7A9E59FF87A984BCE8AF2649BCAE54F95B8` |

The corrected MATLAB harness was frozen read-only before scientific execution and retained the same hash afterward.

## Exact scientific execution counts

| Action | Count | Outcome |
|---|---:|---|
| MATLAB replacement baseline `rah=0.040` | 1 | raw persisted; summary valid |
| MATLAB perturbation `rah=0.041` | 1 | raw persisted; summary valid |
| Python baseline `r_a=0.040` | 1 | solve returned; result not persisted because final JSON serialization failed |
| Python perturbation `r_a=0.041` | 1 | solve returned; result not persisted because final JSON serialization failed |
| P1-P4 reruns | 0 | forbidden and not performed |

The Python execution count follows directly from the frozen control flow: `rows = [run_one(0.040)]`, then `rows.append(run_one(0.041))`, and only afterward `json.dumps(...)` raised. No Python scientific output file exists.

## MATLAB raw output identities and diagnostics

| Rate | Raw object | Bytes | SHA-256 |
|---:|---|---:|---|
| 0.040 | `matlab_out_0040.mat` | 19306 | `E723D267ABEFC16A20B4D17D6EC20554561B601FB028405FDA41D30EFAC03D00` |
| 0.041 | `matlab_out_0041.mat` | 19660 | `83B877820FEA59A655C98A4669189EEA0D3A17E4CDC1D9B334EBAF6115ED58BC` |

The MATLAB JSON summary is 1159 bytes, SHA-256 `0083726D2D3911566DE71C6A97C6DF6FD58739019B8530661809EEBA189C1FEF`.

| Diagnostic | MATLAB 0.040 | MATLAB 0.041 |
|---|---:|---:|
| `convergent` | 1 | 1 |
| `Ct-sum(C,'all')` absolute error | 0 | 0 |
| `Lt-sum(l,'all')` absolute error | 0 | 0 |
| `sum(g,'all')` | 1 | 1 |
| normalization error | 0 | 0 |
| minimum probability cell | `-2.1408321898522033e-32` | `-3.1959705335383453e-33` |
| negative-cell count | 135 | 71 |
| mass finite | true | true |
| aggregate scalars finite | true | true |

The negative cells are machine-scale signed roundoff, many orders below the accepted nonnegative tolerance used on the Python side; no material negative mass was observed. The accepted original MATLAB source exposes no additional patched-source HJB/KFE residual diagnostics: `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE`.

## Requested level table

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | 9.093838085759417 | 0.7208465448372894 |
| Python | 0.040 | NOT_PERSISTED | NOT_PERSISTED |
| MATLAB | 0.041 | 9.088797065167160 | 0.7201767277365387 |
| Python | 0.041 | NOT_PERSISTED | NOT_PERSISTED |

## Within-language response table

| implementation | Delta C_hh | %Delta C_hh | Delta L_hh | %Delta L_hh |
|---|---:|---:|---:|---:|
| MATLAB | -0.00504102059225708 | -0.0554333664698860% | -0.000669817100750647 | -0.0929209005089758% |
| Python | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |

MATLAB assets moved from `A_hh=0.4205741387968296`, `B_hh=2.162515255782729` at 0.040 to `A_hh=0.5227979944275221`, `B_hh=2.168714217374641` at 0.041.

Cross-language level differences and comparative-static response differences cannot be computed without persisted Python aggregates. No exact-native-level parity tolerance is invented; the MATLAB snapshot and Python R4 fixture remain different native calibrations/representations.

## Python blocker

The frozen Python harness was 6763 bytes, SHA-256 `018C1E0A154F32E7D62C9BF7B19F20B3EACE30126D4DF687E40EDC76A2DCBA46`. Its only change from the predecessor harness was the new artifact-root path. Static compilation and the serialized input-manifest only-difference gate passed before execution.

After both scientific solves returned, persistence failed at:

```text
json.dumps(output, indent=2, sort_keys=True, allow_nan=False)
TypeError: Object of type bool is not JSON serializable
```

No `python_pair_output.json` was created. The frozen harness was not edited after execution, the offending value was not coerced, and neither scientific run was repeated. Therefore Python validity diagnostics and aggregates are unavailable as durable evidence, and no scientific interpretation of its response is made.

## Supplementary classification

`PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

The MATLAB pair is valid and durably evidenced, but the required four-row experiment is incomplete because Python results were not persisted. This report does not convert the partial evidence into Owner acceptance and does not issue P5 acceptance.

## Forbidden-operation check

- MATLAB baseline replacement rerun: no
- MATLAB perturbation rerun: no
- Python baseline or perturbation rerun: no
- harness edit after scientific execution began: no
- P1-P4 rerun: no
- outer MATLAB equilibrium/turn/shock/multi-province routine called: no
- diagnostic-patch HJB executed: no
- MATLAB/Python production source or tests modified: no
- selected cache modified or regenerated: no
- scientific input other than `rah/r_a` changed within a pair: no
- grids, equations, FOCs, productivity law, initialization, boundary/KKT/generator/KFE logic, or tolerances changed: no
- tuning after output: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension, dynamics, or Results entered: no
- merge, rebase, reset, or force-push: no

## Recommended next gate

Publish a new exact task that decides whether a fresh Python pair may be run after correcting only the external JSON serialization of NumPy/Python boolean diagnostics and adding a mandatory synthetic serialization preflight. The task must state explicitly whether the two consumed but unpersisted Python runs may be replaced. MATLAB should not be rerun; its two persisted raw outputs can be reused only if the new task explicitly accepts their identities.
