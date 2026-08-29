# CH5 Two-Asset HANK MATLAB-Python HA P2 Python Harness API-Arity Correction and Completion

## Terminal result

`MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS`

Evidence reuse decision: `P1_AND_CORRECTED_MATLAB_P2_EVIDENCE_REUSED`.

The corrected Python P2 harness completed all ten frozen cases in its single authorized invocation. The byte-identical frozen comparison harness then completed once with `pass=true`, all ten cases passing, and an empty failure list. P1 and MATLAB P2 were not rerun. This P2 PASS does not authorize P3, P4, P5, or any dynamic extension.

## Live/source/workspace identity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live/base `origin/main`: `d22c7a3e40817ad2f22ee0e07163a2792879fcc7`
- accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- latest predecessor report commit: `21209b9e409f77198f6f4e97ed2c874e71966ced`
- predecessor task-authority parent: `394b7b2668a616c7a2c372dde678866bf41ddf6e`
- isolated Git workspace: `D:\ProjectTemp\ch5-ha-p2-python-correction-repo-20260829`
- new external artifact root: `D:\ProjectTemp\ch5-ha-p2-python-harness-correction-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..d22c7a3e40817ad2f22ee0e07163a2792879fcc7 -- src tests`: empty

Python scientific/test source continuity: `PASS`. The accepted seven-argument `check_boundary(i_a,i_b,n_a,n_b,mu_a,mu_b,tolerance)` API was read directly and not modified.

The designated MATLAB identities all passed; MATLAB production code was not executed or modified:

| File | Bytes | SHA-256 |
|---|---:|---|
| `HANK_2ASSETS_HJB.m` | 12227 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_cost.m` | 691 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `HANK3_FOC.m` | 565 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |

## Predecessor evidence verification and reuse

Both predecessor roots were inspected read-only:

- `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`
- `D:\ProjectTemp\ch5-ha-p2-harness-correction-20260829`

All required identities matched:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `manifest.json` | 2329 | `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449` |
| original `p2_python.py` | 3820 | `2E9F6198FD906E6703416E4F48DE6CD1DBA6F7A2EA365360890AA92CBDBED6B0` |
| original `compare_p2.py` | 1684 | `4B114245AF4F5895357465A1AE41AE608F026E297B6E044C16441EC7A7AAF70B` |
| `orientation_verification.json` | 385 | `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2` |
| `p1_matlab.json` | 146443 | `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886` |
| `p1_python.json` | 217784 | `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD` |
| `p1_compare.json` | 26665 | `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550` |
| `p2_matlab_corrected.m` | 1275 | `EF8ADD59AF0C0AC96C8E8F2DD80FB8E4C405BB5F8C0BAEF93FEDD4E801B1103A` |
| completed corrected `p2_matlab.json` | 3093 | `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C` |

The copied manifest, original Python/comparison harnesses, and completed MATLAB JSON retained these exact identities. P1 remains accepted without rerun, and corrected MATLAB P2 evidence was reused without rerun.

## Original-to-corrected Python harness

The complete diff contains only the authorized API-arity plumbing change:

```diff
-bc=check_boundary(*idx,3,3,ma,mb,tol)
+bc=check_boundary(idx[0],idx[1],3,3,ma,mb,tol)
```

The productivity index `idx[2]` is omitted exactly as required by the production API. No import, case, state, derivative, formula, adapter, classification, order, output field, orientation or tolerance changed.

- corrected harness: `p2_python_corrected.py`
- bytes: 3829
- SHA-256: `93516B30F727C8768A6F006FD3C4B4BFBCEC8197DA19D2A2D068E00E9D1BE26A`
- Python static compilation: PASS
- frozen before execution and not edited afterward: yes

## Execution counts and raw outputs

| Action | Count | Result |
|---|---:|---|
| P1 MATLAB/Python/comparison | 0 | predecessor evidence reused |
| MATLAB P2 scientific harness | 0 | completed predecessor JSON reused |
| corrected Python P2 scientific harness | 1 | complete, 10/10 rows |
| byte-identical frozen P2 comparison | 1 | PASS, 10/10, no failures |
| P3 | 0 | not entered |
| P4 | 0 | not entered |

| New/reused output | Bytes | SHA-256 |
|---|---:|---|
| reused `p2_matlab.json` | 3093 | `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C` |
| new `p2_python.json` | 5647 | `E27F3B557123B8ED1BBFB8986B63861075C43106264EAAC4FC867797E237978A` |
| new `p2_compare.json` | 2366 | `0851FD1AF8899594B21BC01F593B329918E56C06F5CEA68901A28EDD49B1AE56` |

Frozen thresholds were unchanged: `tau_fp=128*eps_float64*max(1,abs(x),abs(y))`, drift/zero `1e-12`, KKT `1e-7`.

## Comparable case evidence

For all three comparable cases, every MATLAB-Python mapped difference for `d`, cost, consumption, labor, `mu_a`, `mu_b`, utility and Hamiltonian was exactly zero. Directions also agreed exactly.

### 1. `interior_ff` — `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`

- inputs: `a=1`, `b=2.5`, `z=1`, `v_a=2.4`, `v_b=2`
- MATLAB = Python: `c=0.5`, labor `2`, `d=0.14999999999999997`, cost `0.018749999999999992`, `mu_a=0.18999999999999997`, `mu_b=1.4062500000000002`, utility `-2.6931471805599454`, Hamiltonian `0.575352819440055`, directions `F/F`
- Python boundary: feasible, violation `0`; KKT max `0`; multipliers `lambda_a=lambda_b=0`
- differences: all `0`
- field bounds: base fields `2.842170943040401e-14`; labor `5.684341886080802e-14`; `mu_b` `3.996802888650564e-14`; utility `7.654384661918656e-14`
- result: PASS

### 2. `interior_bb` — `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`

- inputs: `a=1`, `b=2.5`, `z=1`, `v_a=0.6`, `v_b=0.75`
- MATLAB = Python: `c=1.3333333333333333`, labor `0.75`, `d=-0.15000000000000008`, cost `0.018750000000000017`, `mu_a=-0.11000000000000007`, `mu_b=-0.3770833333333332`, utility `0.006432072451780846`, Hamiltonian `-0.3423804275482191`, directions `B/B`
- Python boundary: feasible, violation `0`; KKT max `1.1102230246251565e-16`; multipliers zero
- differences: all `0`
- bounds: consumption `3.789561257387201e-14`; every other compared field `2.842170943040401e-14`
- result: PASS

### 3. `liquid_zero` — `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`

- inputs: `a=1`, `b=2.5`, `z=1`, `v_a=v_b=0.9632028779812717`
- MATLAB = Python: `c=1.0382028779812718`, labor `0.9632028779812717`, `d=0`, cost `0`, `mu_a=0.04`, `mu_b=0`, utility `-0.4263886755810247`, Hamiltonian `-0.38786056046177386`, directions `F/Z`
- Python boundary: feasible, violation `0`; KKT max `0`; multipliers zero
- differences: all `0`
- bounds: consumption `2.950750052779289e-14`; every other compared field `2.842170943040401e-14`
- result: PASS

## Accepted Python redesign evidence

For cases 4–10 MATLAB correctly records `available=false` with legacy evidence: `No explicit accepted candidate/KKT audit in HANK_2ASSETS_HJB.m lines 131-154; legacy masks only`. No nonexistent MATLAB candidate identity is claimed.

| # | Case and frozen inputs | Python controls/policy evidence | Boundary/KKT and identity evidence | Result |
|---:|---|---|---|---|
| 4 | `lower_a_active`: `a=0,b=5,z=1.5625,v_a=0.7619162076101915` | `c=1.5917308671324435`, labor `0.9816357980258912`, `d=0.08138277291081655`, cost `0.010692294372194364`, `mu_a=0.08138277291081655`, `mu_b=4.440892098500626e-16`, utility `-0.01698240016066077`, `H=0.045024453540350284`, `F/Z` | feasible; violation `4.44e-16`; KKT max `0`; lambdas zero | PASS, `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` |
| 5 | `lower_b_active`: `a=1,b=0,z=0.8125,v_a=1.3407408769313847,v_b=1.249395172408839` | `c=0.8003872770470178`, labor `1.0151335775821817`, `d=-0.04`, cost `0.0028`, `mu_a=0`, `mu_b=0.0616087547385048`, utility `-0.7379076623096531`, `H=-0.660933981561245`, `Z/F` | feasible; violation `0`; KKT max `0`; `lambda_a=0.20379127003934117`, `lambda_b=0` | PASS, redesign |
| 6 | `interior_mu_a_zero`: `a=0.5,b=0,z=0.75,a_F=1.1703333447650266,a_B=1.2263220986701668,v_b=1.269836394939054` | `c=0.7593576577837201`, labor `0.9876768770449598`, `d=-0.02`, cost `0.0014`, `mu_a=0`, `mu_b=-2.220446049250313e-16`, utility/H `-0.7630351969251046/-0.7630351969251049`, `Z/Z` | feasible; violation and KKT max `2.22e-16`; `lambda_a=0`, `lambda_b=0.04706610778755893` | PASS, redesign |
| 7 | `upper_a_lower_b`: `a=1,b=0,z=0.6875,v_a=1.3096756237319624,v_b=1.2588632353149407` | `c=0.7063515612486823`, labor `0.9733113618162653`, `d=-0.04`, cost `0.0028`, `mu_a=0`, `mu_b=1.1102230246251565e-16`, utility/H `-0.8213097068425832/-0.8213097068425831`, `Z/Z` | feasible; violation `0`; KKT max `1.2301269817963023e-17`; positive multipliers `0.021365312091524258/0.15686238187235424` | PASS, redesign |
| 8 | `upper_a_interior_b`: `a=1,b=2.5,z=0.8125,v_a=1.0900614604620955,b_F=1.0850659085568666,b_B=1.235872027778018` | `c=0.8705344418060916`, labor `0.9333346976074973`, `d=-0.04`, cost `0.0028`, `mu_a=0`, `mu_b=-1.1102230246251565e-16`, utility/H `-0.5742047838915825/-0.5742047838915826`, `Z/Z` | feasible; violation/KKT `0`; `lambda_a=0.04472659914169852`, `lambda_b=0` | PASS, redesign |
| 9 | `dual_upper`: `a=1,b=5,z=1.5,v_a=0.5713121926071842,v_b=0.903756799527612` | `c=1.5965174827647721`, labor `0.9395449885098484`, `d=-0.04`, cost `0.0028`, `mu_a=0`, `mu_b=4.440892098500626e-16`, utility/H `0.026452291078356616/0.026452291078357018`, `Z/Z` | feasible; violation `4.44e-16`; KKT max `2.7816119437728316e-16`; positive multipliers `0.0013215662445429377/0.27739347385437974` | PASS, redesign |
| 10 | `lower_b_fz_near_tie`: frozen `H=1`, raw IDs `FF/FZ` | Python raw `FF`, canonical `FZ`, alias available; `mu_a=0.2`, `mu_b=0` | gap `0` <= `tau_H=3.552713678800501e-15`; boundary feasible; KKT max `0` | PASS, redesign |

All redesign cases satisfy the frozen comparison contract. Where zero drift is required, observed drift is zero or within `1e-12`; all boundary checks are feasible and all KKT residuals are below `1e-7`.

## Files read and written

Read: the live task and required governance files; both predecessor tasks/reports; accepted Owner source-audit report; P2-relevant accepted Python source/tests; the three MATLAB production files for hashing; and all required artifacts in both predecessor roots.

Repository write: only this report. External writes: byte-identical copied inputs, exactly one corrected Python harness, its static bytecode cache, and the single-run Python/comparison JSON outputs.

## Forbidden-operation check

- P1 rerun: no
- MATLAB P2 rerun: no
- predecessor artifact modified: no
- MATLAB production source/helper modified: no
- Python production source/test or `check_boundary` modified: no
- scientific case, order, derivative, formula, adapter, expected classification, orientation or tolerance changed: no
- corrected Python harness edited or rerun after invocation: no
- frozen comparison edited or rerun: no
- P3/P4/P5 entered or authorized: no
- AR(1), transition, IRF, calibration extension or Results entered: no
- merge, rebase, reset or force-push: no

## Acceptance and recommended next gate

P1 remains accepted and P2 numerical parity evidence is complete and passes the frozen contract. This is not final HA or Owner acceptance.

Recommended next gate, only after independent acceptance of this report:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY`

That gate must reuse P1/P2 evidence, execute only P3 then P4 in bounded fail-closed order, and retain the P5/HA hard gate before any dynamic extension.
