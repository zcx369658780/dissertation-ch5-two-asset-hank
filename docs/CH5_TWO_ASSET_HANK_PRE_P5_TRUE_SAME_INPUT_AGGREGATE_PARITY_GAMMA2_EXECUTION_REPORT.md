# Chapter 5 two-asset HANK pre-P5 gamma2 true same-input aggregate parity execution report

## Terminal classification

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_BLOCKED_SOURCE_OR_ENVIRONMENT`

Named blocker: `BLOCKED_GAMMA2_TRUE_SAME_INPUT_PARITY_INITIALIZATION_MAPPING`.

No P5 acceptance is issued. The four-run scientific sequence was not started.

## Authority and live identities

- Task authority and fetched live `origin/main`: `3e917306ea22c5603223c5e1d156d1b82a6c0991` (`Authorize gamma2 true same-input HA aggregate parity execution`).
- Predecessor adapter report commit: `c849c48dd78518dd22ffed20e6c3d9125bdd9488`.
- Accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`; `git diff --name-only <baseline> -- src tests` was empty.
- MATLAB `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` (PASS).
- MATLAB `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` (PASS).
- Production MATLAB `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` (PASS).
- MATLAB initialization helper `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

## Frozen gamma2 common manifest

| field | value |
|---|---|
| `rho` | 0.05 |
| `gamma_c / ga` | 2.0 |
| `phi / frisch_l` | 1.0 |
| labor weight | 1.0 |
| `chi_0`, `chi_1`, `a_bar` | 0.05, 1.0, 0.5 |
| `r_b`, `w`, `tau` | 0.03, 1.0, 0.0 |
| migration cost, `Tt`, `rb_gap` | 0.0, 0.0, 0.0 |
| `fixcost`, `fixcost2` | 0.0, 0.0 |
| `r_a / rah` | 0.040, 0.041 |
| `a` | [0.0, 0.5, 1.0, 1.5, 2.0] |
| `b` | [0.0, 1.25, 2.5, 3.75, 5.0] |
| `z` | [0.8, 1.3] |
| `Q_z_common` | [[-0.4, 0.4], [0.3, -0.3]] |
| state count | 50 |
| finite-state measure | `da=0.5`, `db=1.25`, `cell_weight=0.625`, no z quadrature factor |

Python `GridSpec` accepted the 50-state grid. The frozen productivity orientation was proved as `kron(Q_z_common, I_25)`.

## Utility, FOC, and adapter conformance

At representative positive consumption `[0.5, 1.0, 2.0]`, both gamma2 CRRA implementations produced `[-2.0, -1.0, -0.5]`. At marginal values `[0.25, 1.0, 4.0]`, the common consumption FOC produced `[2.0, 1.0, 0.5]`. These checks passed to machine precision without an HJB call.

The reused O1 adapter hash is `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`. Its complete scientifically material diff remains only `a -> max(a,a_bar)` in the external temporary `HANK3_FOC.m`. Path resolution proved original HJB, original cost helper, temporary O1 FOC, and original `lab_solve2` were selected.

The reused O2 adapter hash is `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`. Synthetic sparse checks proved exact production `_asset_generator` equality for `G_a` and `G_b`, exact `G_z=kron(Q_z_common,I_25)`, maximum row-sum error `5.551115123125783e-17`, minimum off-diagonal `0.016`, and restoration of the production `build_operator` binding. Neither `solve_hjb` nor KFE was called.

## Initialization mapping proof and blocker

The accepted MATLAB main constructs its initial value internally. Its initialization contains the rate-dependent terms

```matlab
raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));
Rah(i,j,nz) = raah(j);
tempMat = Rah.*raah + Rb.*bbb + Tt;
```

and then obtains `l0`, `c0`, and `v02` from that object. The preflight reconstructed this logic for both authorized rates without calling `HANK_2ASSETS_HJB`, then mapped MATLAB `[b,a,z]` to Python `[a,b,z]` by transposing the first two axes.

Both reconstructed initial values are finite, but they are not identical:

| comparison, 0.040 vs 0.041 | maximum absolute difference |
|---|---:|
| mapped initial value `v02` | `5.538445613240128e-06` |
| initialization labor `l0` | `6.745714110456547e-05` |
| initialization consumption `c0` | `5.397519804706263e-05` |

The accepted MATLAB main has no external `initial_value` argument. Consequently it is impossible, without an unauthorized production-main change or a new adapter, both to preserve the accepted MATLAB execution path and to prove/use one identical initial value for `rah=0.040` and `0.041`. This violates a mandatory pre-scientific gate. The task requires fail-closed before partially executing either implementation.

## Preflight artifacts

External artifact root: `D:\ProjectTemp\ch5-pre-p5-gamma2-same-input-exec-artifacts-20260829`.

| artifact | SHA-256 |
|---|---|
| `matlab_gamma2_preflight.m` | `83BF5575DC1C6F5752242209EB9CEA303AF646EAD1B46A520316A34281C72881` |
| `python_gamma2_preflight.py` | `A4D4C38CB1ECEE5CF8CA7D9405CE8E19DD4025800900F2059460F8577E5DA680` |
| `matlab_gamma2_initial_values.mat` | `20552557220AFE5D55DE02BCD217AA31502E251224A728576F1E0099308BA1A4` |
| `matlab_gamma2_preflight.json` | `35EA6D18F4466C61341615E1758B8275E02ACB4BD7A9D063F9B03613259DA5A8` |
| `gamma2_preflight_manifest.json` | `72925D279A2415B2F693B5B41F1DD01C3B1EB2559B867650F8B069FEC0DE3375` |

The scripts were frozen after their synthetic machine-precision comparison corrections. The planned four-output persistence/serialization preflight was not reached because the mandatory initialization gate failed first; no scientific output path was opened.

## Scientific execution, diagnostics, and parity tables

| operation | count |
|---|---:|
| MATLAB HJB, `rah=0.040` | 0 |
| Python `solve_hjb`, `r_a=0.040` | 0 |
| MATLAB HJB, `rah=0.041` | 0 |
| Python `solve_hjb`, `r_a=0.041` | 0 |
| KFE | 0 |

Because the four-run sequence was never started, there are no scientific outputs, HJB/KKT/generator/KFE validity diagnostics, mapped pointwise comparisons, stationary masses, aggregate levels, or response deltas to report. Accordingly none of the frozen aggregate, stationary-mass, or response-delta tolerances was evaluated; no tolerance was widened or tuned.

## Forbidden-operation check and next gate

- P1-P4 were not rerun.
- No MATLAB HJB, Python `solve_hjb`, or KFE was executed.
- No MATLAB log-utility adapter was added.
- MATLAB production source/helpers and Python `src/tests` were not modified.
- No consumed scientific rate exists and no scientific rerun occurred.
- No outer equilibrium, turn, shock, multi-province, dynamics, AR(1), transition, IRF, calibration extension, or Results routine was entered.
- P5 acceptance is not issued.

The next gate, if the Owner wishes to continue, must explicitly resolve the rate-dependent MATLAB initialization conflict (for example by authorizing a narrowly specified initialization adapter or by revising the identical-initial-value requirement). This report does not infer that authority.
