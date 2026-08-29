# Chapter 5 two-asset HANK pre-P5 gamma2 rate-matched initialization execution report

## Terminal classification

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_NEEDS_DIAGNOSTIC__P5_BLOCKED`

Smallest failing object: the first and only consumed scientific run, accepted MATLAB common baseline `rah=0.040`, returned `convergent=false`. The raw output was durably persisted and read back. The task's first-failure rule then stopped the sequence; no rerun or harness change occurred.

This report does not issue P5 acceptance.

## Live authority and source identities

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh-fetched task authority / execution base: `36da4fb8bdf828182a942eed32e020e3612cdfa0` (`Authorize rate-matched gamma2 same-input HA aggregate parity`).
- Accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- MATLAB `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` (PASS).
- MATLAB `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` (PASS).
- Production MATLAB `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` (PASS).
- MATLAB `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` (PASS).

No accepted source or test was modified.

## Frozen common gamma2 manifest

| object | value |
|---|---|
| `rho` | 0.05 |
| `gamma_c / ga` | 2.0 |
| `phi / frisch_l` | 1.0 / 1.0 |
| labor weight | 1.0 |
| `chi_0`, `chi_1`, `a_bar` | 0.05, 1.0, 0.5 |
| `r_b`, `w`, `tau` | 0.03, 1.0, 0.0 |
| migration cost, `Tt`, `rb_gap` | 0.0, 0.0, 0.0 |
| `fixcost`, `fixcost2` | 0.0, 0.0 |
| `r_a / rah` pair | 0.040, 0.041 |
| `a` | [0.0, 0.5, 1.0, 1.5, 2.0] |
| `b` | [0.0, 1.25, 2.5, 3.75, 5.0] |
| `z` | [0.8, 1.3] |
| `Q_z_common` | [[-0.4, 0.4], [0.3, -0.3]] |
| state count | 50 |
| measure | `da=0.5`, `db=1.25`, `cell_weight=0.625`, no z quadrature factor |

Python contract-only values `mu_z=0.2`, `sigma_z=0.1` remain the predecessor-conformance placeholders and are bypassed by the exact O2 common-Q injection; they do not enter the scientific productivity operator.

## Corrected initialization and preflight evidence

The accepted MATLAB initialization was independently reconstructed without calling HJB for each rate. MATLAB `[b,a,z]` arrays were mapped separately to Python `[a,b,z]` by transposing axes 0 and 1.

| rate | MATLAB reconstructed `v02` SHA-256 | Python mapped initial value SHA-256 | within-rate numerical identity |
|---:|---|---|---|
| 0.040 | `57B129FABB193CBE2C2422201B506200B3D06F5447FD69E17ED7E55CE5C356CA` | `21E3878EB6F268DEA678BC92DF78F777503F185D6EEBF5B0D1BD77D55799A444` | exact array equality PASS |
| 0.041 | `7D1E445BBE1994EA927050543AA36E1A28CE21AEE4A8217565FA10D693F4F49C` | `7E6B618C8507A28D8268620E3F8DCF4045A166EDD50F2E3E2DEBCB80A8C7A503` | exact array equality PASS |

Different file hashes reflect different MAT/NPY container formats. The persisted numerical arrays were read back and compared exactly. The allowed cross-rate initial-value maximum absolute difference is `5.538445613240128e-06`; it was recorded and was not used as a gate.

Pre-scientific checks passed for:

- Python `GridSpec` and the 50-state orientation;
- gamma2 CRRA utility at positive representative consumption values;
- the common consumption FOC;
- O1 representative and predecessor 12-point conformance;
- exact O2 synthetic `G_a/G_b` equality with production `_asset_generator`;
- exact `G_z=kron(Q_z_common,I_25)`, maximum synthetic row-sum error `5.551115123125783e-17`, minimum off-diagonal `0.016`, and binding restoration;
- finite-state cell measure;
- synthetic MAT, NPZ, and strict JSON write/read-back.

No HJB, policy solve, generator-based household solve, or KFE solve occurred during preflight.

## Frozen adapters and harnesses

External artifact root: `D:\ProjectTemp\ch5-pre-p5-gamma2-rate-matched-exec-artifacts-20260829`.

| artifact | SHA-256 |
|---|---|
| O1 `matlab_o1/HANK3_FOC.m` | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` |
| O2 `python_common_q_adapter.py` | `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225` |
| `matlab_rate_matched_preflight.m` | `290FFDAB43F8899DF273BAD379954F4A351A56915460ED7CE1B023580756DFE2` |
| `python_rate_matched_preflight.py` | `64FAE6F9D97BF009F7A3AB5509D8C7C3EE28223A753DE29170493FD7656F8568` |
| `run_matlab_rate.m` | `A8FA2E02A6E20B4C48D7ABE6A6A079AA047BC11BCA2C7453FEA7BF698BAE572E` |
| `run_python_rate.py` | `A8BD1A311314B444759686D067BA0450A5FC71ADEDCDE05BE6A1D2A6FA84AC2A` |
| `compare_rate_matched.py` | `B39ECCCCD6C299DE16B0072DEFD8516159EA9A6B9F4F4046DDDE29592B5B4BF2` |
| preflight manifest | `6DC1B081621855C3A16281F05485DA3DA5C57A888F3C77F1AEAECFDC61544A60` |

MATLAB path resolution before execution selected the accepted original main, accepted original cost helper, exact external O1 FOC, and accepted original `lab_solve2`. No third scientific adapter was active or created.

## Exact execution sequence and persistence

| sequence item | authorized rate | attempts | completed/persisted | disposition |
|---|---:|---:|---:|---|
| MATLAB baseline | 0.040 | 1 | 1 | returned `convergent=false`; terminal stop |
| Python baseline | 0.040 | 0 | 0 | not entered |
| MATLAB perturbation | 0.041 | 0 | 0 | not entered |
| Python perturbation | 0.041 | 0 | 0 | not entered |

The accepted MATLAB main internally proceeded through its stationary solve before returning the completed result. Python KFE count is 0.

Persistence identities for the consumed run:

- attempt marker: `32F0AA4388D06C2EF5731AF9B917ACD510D09CCD04BF502EA7FF3676305A3063`;
- `matlab_raw_0040.mat`: `D2B44C85B4FF2D74D6DDDAF9B1B33904933005235AFD5EFE3B1B2DF66F42A3D5`;
- `matlab_summary_0040.json`: `1098DCFFB75F02A384A37F2400E04520C2B7089BFA3B296461A2BD65FBA8F1EC`.

The raw MAT was saved immediately after `HANK_2ASSETS_HJB` returned and before summary construction, then read back successfully. MATLAB emitted a near-singular-matrix warning at its stationary linear solve (`HANK_2ASSETS_HJB.m:340`), with `RCOND = 1.280574e-18`; the function nevertheless returned a finite exposed result.

## Completed-run validity diagnostics

| diagnostic | MATLAB 0.040 |
|---|---:|
| `convergent` | **false (FAIL)** |
| exposed arrays finite | true |
| stationary mass sum | 1.0 |
| minimum mass | `-1.3896874805456546e-18` |
| mass below `-1e-12` | 0 |
| HJB iterations/change/residual | `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE` |
| KKT residual | `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE` |
| generator row-sum/off-diagonal | `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE` |

Because `convergent=false` is a required validity failure, the task prohibited starting the next scientific run. No parity classification can be inferred from the finite aggregates or normalized returned mass.

## Aggregate levels and responses

The following values are persisted descriptive evidence from the failed-convergence MATLAB run, not accepted parity evidence.

| implementation | r_a | C_hh | H_hh | L_hh | A_hh | B_hh |
|---|---:|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | 1.0489158011797988 | 0.9842018950457534 | 1.0489158011797988 | -2.714734856761404e-18 | -1.636268099514860e-17 |
| Python | 0.040 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| MATLAB | 0.041 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Python | 0.041 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

For the completed MATLAB row, native `Ct/Lt/At/Bt` equal the independently derived common-mass `C_hh/L_hh/A_hh/B_hh`. `H_hh` was independently derived from the exposed mass-weighted effective-labor array using the frozen z states.

No within-language response delta, cross-language level difference, stationary-mass parity comparison, or response-delta comparison exists because the mandated stop occurred after run 1. Therefore none of the frozen parity tolerances was evaluated, widened, or tuned.

## Pointwise parity diagnostics

No cross-language pointwise comparison was executed. Python did not run. The accepted MATLAB output exposes stationary mass and mass-weighted consumption/effective labor, but does not expose its value function, transfer `d`, adjustment cost, `mu_a`, `mu_b`, generator, or policy/direction classes. Those objects are recorded as `NOT_EXPOSED_BY_ACCEPTED_ORIGINAL_SOURCE`; none was invented or recovered by adding an unauthorized adapter.

## Forbidden-operation check and next gate

- MATLAB production main/helpers modified: no.
- Python `src/tests` modified: no.
- third scientific adapter added: no.
- cross-rate common initial value forced: no.
- P1-P4 rerun: no.
- consumed MATLAB baseline rerun: no.
- frozen harness/adapters edited after scientific execution began: no.
- Python baseline, either perturbation run, or Python KFE entered: no.
- tolerance/input tuning after result observation: no.
- P5 acceptance issued: no.
- AR(1), transition, IRF, calibration extension, dynamics, or Results entered: no.

P5 remains blocked. The smallest successor must be a narrowly authorized diagnostic of why the accepted MATLAB gamma2 common baseline fails its own `convergent` flag under the frozen 50-state fixture. This report does not authorize that diagnostic, any harness repair, or any rerun.
