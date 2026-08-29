# CH5 Two-Asset HANK MATLAB-Python HA P2 Harness Block Correction and Reexecution

## Terminal classifications

- P1 reuse: `P1_EVIDENCE_REUSED_AND_REMAINS_ACCEPTED`
- P2: `MATLAB_PYTHON_TWO_ASSET_HA_P2_CORRECTION_BLOCKED_ENVIRONMENT_OR_HARNESS`
- blocker diagnosis: `P2_JSON_CONTAINER_CELL_ACCESS_REQUIRED`

The corrected MATLAB P2 harness completed all ten frozen cases. The byte-identical frozen Python P2 harness then terminated on its first case before writing any Python P2 output because it passed eight positional arguments to the accepted seven-argument `check_boundary` API. Under the one-attempt rule it was not edited or rerun, the comparison harness was not invoked, and P3/P4 were not entered. This is a harness block, not a P2 scientific numerical mismatch.

## Live GitHub, source and workspace identity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live/base `origin/main`: `394b7b2668a616c7a2c372dde678866bf41ddf6e`
- accepted Python scientific/test baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- predecessor report commit: `1b26e9cedded11ac8c96e1deb6560cc8d200e465`
- predecessor task-authority commit: `30ce23b44f40eea621e9dd84a0d26520ad0f0a0f`
- isolated Git workspace: `D:\ProjectTemp\ch5-ha-p2-correction-repo-20260829`
- predecessor artifact root, inspected read-only: `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`
- new correction artifact root: `D:\ProjectTemp\ch5-ha-p2-harness-correction-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..394b7b2668a616c7a2c372dde678866bf41ddf6e -- src tests`: empty

Python scientific/test source continuity: `PASS`.

MATLAB R2022b was used; GNU Octave was not substituted. The three production-source identity gates passed:

| File | Bytes | SHA-256 |
|---|---:|---|
| `HANK_2ASSETS_HJB.m` | 12227 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_cost.m` | 691 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `HANK3_FOC.m` | 565 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |

## Predecessor artifact fingerprint verification and P1 decision

All required predecessor identities matched exactly:

| Artifact | Bytes where frozen | SHA-256 |
|---|---:|---|
| `manifest.json` | 2329 | `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449` |
| `p2_matlab.m` | 1275 | `0CB2C08ABC856FC90A5720971D230CA9CABBC7564F8A7FD7CAFC4E0F6B19815F` |
| `p2_python.py` | 3820 | `2E9F6198FD906E6703416E4F48DE6CD1DBA6F7A2EA365360890AA92CBDBED6B0` |
| `compare_p2.py` | 1684 | `4B114245AF4F5895357465A1AE41AE608F026E297B6E044C16441EC7A7AAF70B` |
| `p1_matlab.json` | 146443 observed | `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886` |
| `p1_python.json` | 217784 observed | `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD` |
| `p1_compare.json` | 26665 observed | `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550` |
| `orientation_verification.json` | 385 | `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2` |

The copied `manifest.json`, `p2_python.py`, and `compare_p2.py` in the new root retained the exact same bytes and hashes. Therefore P1 was reused without execution and remains accepted: `P1_EVIDENCE_REUSED_AND_REMAINS_ACCEPTED`.

## Decoder/access diagnosis and preflight

Exactly one non-scientific MATLAB decoder/access preflight was run. It evaluated no economic formula. MATLAB R2022b decoded `m.p2` as a `10 x 1 cell`; every cell element was a `struct`. All metadata IDs and kinds were retrieved in the exact frozen order using brace access, and the complete-order assertion passed.

- preflight script: 918 bytes, SHA-256 `BB22C966D87A93E93FC0714059D9F91DEFAC27038826AA362500930CEF5D9BE4`
- container: `cell`, size `[10 1]`, elements: `struct`
- exact order: `interior_ff`, `interior_bb`, `liquid_zero`, `lower_a_active`, `lower_b_active`, `interior_mu_a_zero`, `upper_a_lower_b`, `upper_a_interior_b`, `dual_upper`, `lower_b_fz_near_tie`
- result: `PASS`

## Frozen-to-corrected MATLAB harness

The complete scientific-harness diff was one plumbing-only token change:

```diff
-for k=1:numel(m.p2); cse=m.p2(k);rows(k).id=cse.id;rows(k).kind=cse.kind;
+for k=1:numel(m.p2); cse=m.p2{k};rows(k).id=cse.id;rows(k).kind=cse.kind;
```

No case, derivative, formula, adapter, tolerance, classification, order, source call or scientific comparison semantics changed.

- corrected harness: `p2_matlab_corrected.m`
- bytes: 1275
- SHA-256: `EF8ADD59AF0C0AC96C8E8F2DD80FB8E4C405BB5F8C0BAEF93FEDD4E801B1103A`
- MATLAB `checkcode`: PASS, no issues
- frozen before scientific execution and not edited afterward: yes

## Exact execution counts and terminal blocker

| Action | Count | Result |
|---|---:|---|
| P1 MATLAB/Python/comparison | 0 | accepted predecessor evidence reused |
| decoder/access metadata preflight | 1 | PASS |
| corrected MATLAB P2 scientific harness | 1 | complete, 10/10 rows |
| byte-identical Python P2 scientific harness | 1 | blocked on first case before output |
| byte-identical P2 comparison harness | 0 | prerequisite Python output absent |
| P3 | 0 | forbidden/not entered |
| P4 | 0 | forbidden/not entered |

MATLAB P2 output: 3093 bytes; SHA-256 `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C`.

The Python traceback terminates in frozen `p2_python.py` at:

```python
check_boundary(*idx, 3, 3, ma, mb, tol)
```

For the first case `idx=(1,1,0)`, expansion supplies three index values plus two grid sizes, two drifts and tolerance: eight positional arguments. Accepted `src/ch5_two_asset_hank/boundaries.py` defines:

```python
check_boundary(i_a, i_b, n_a, n_b, mu_a, mu_b, tolerance)
```

The production API therefore accepts seven arguments and has no productivity-index parameter. The exact terminal error was `TypeError: check_boundary() takes 7 positional arguments but 8 were given`. No `p2_python.json` or `p2_compare.json` was created. Because the frozen Python harness may not be modified and its sole invocation was consumed, no further execution was authorized.

## Reached P2 case evidence

The MATLAB harness reached every frozen case. Python comparable controls, boundary/KKT evidence, raw/canonical identity, numerical differences and frozen-bound comparisons were not produced because the Python harness blocked before its first row was recorded. They are marked `NOT_REACHED_HARNESS_BLOCK`, not scientific failures.

| # | Case/classification | Frozen state/derivative inputs | MATLAB reached evidence | Python/comparison evidence |
|---:|---|---|---|---|
| 1 | `interior_ff`; `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` | `a=1,b=2.5,z=1,v_a=2.4,v_b=2` | available; `c=0.5,l=2,d=0.15,cost=0.01875,mu_a=0.19,mu_b=1.40625,u=-2.6931471805599454,H=0.575352819440055`; directions `F/F` | `NOT_REACHED_HARNESS_BLOCK` |
| 2 | `interior_bb`; `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` | `a=1,b=2.5,z=1,v_a=0.6,v_b=0.75` | available; `c=1.3333333333333333,l=0.75,d=-0.15,cost=0.01875,mu_a=-0.11,mu_b=-0.3770833333333332,u=0.006432072451780846,H=-0.3423804275482191`; directions `B/B` | `NOT_REACHED_HARNESS_BLOCK` |
| 3 | `liquid_zero`; `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` | `a=1,b=2.5,z=1,v_a=v_b=0.9632028779812717` | available; `c=1.0382028779812718,l=0.9632028779812717,d=0,cost=0,mu_a=0.04,mu_b=0,u=-0.4263886755810247,H=-0.38786056046177386`; directions `F/Z` | `NOT_REACHED_HARNESS_BLOCK` |
| 4 | `lower_a_active`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=0,b=5,z=1.5625,v_a=0.7619162076101915` | unavailable; legacy masks only, no explicit accepted candidate/KKT audit | `NOT_REACHED_HARNESS_BLOCK` |
| 5 | `lower_b_active`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=1,b=0,z=0.8125,v_a=1.3407408769313847,v_b=1.249395172408839` | unavailable; legacy masks only | `NOT_REACHED_HARNESS_BLOCK` |
| 6 | `interior_mu_a_zero`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=0.5,b=0,z=0.75,a_F=1.1703333447650266,a_B=1.2263220986701668,v_b=1.269836394939054` | unavailable; legacy masks only | `NOT_REACHED_HARNESS_BLOCK` |
| 7 | `upper_a_lower_b`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=1,b=0,z=0.6875,v_a=1.3096756237319624,v_b=1.2588632353149407` | unavailable; legacy masks only | `NOT_REACHED_HARNESS_BLOCK` |
| 8 | `upper_a_interior_b`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=1,b=2.5,z=0.8125,v_a=1.0900614604620955,b_F=1.0850659085568666,b_B=1.235872027778018` | unavailable; legacy masks only | `NOT_REACHED_HARNESS_BLOCK` |
| 9 | `dual_upper`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `a=1,b=5,z=1.5,v_a=0.5713121926071842,v_b=0.903756799527612` | unavailable; legacy masks only | `NOT_REACHED_HARNESS_BLOCK` |
| 10 | `lower_b_fz_near_tie`; `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `H=1`, raw IDs `FF/FZ` | unavailable; legacy masks only | raw/canonical Python alias evidence `NOT_REACHED_HARNESS_BLOCK` |

The frozen comparable-object bound remains `tau_fp(x,y)=128*eps64*max(1,abs(x),abs(y))`; zero/drift and KKT bounds remain `1e-12` and `1e-7`. No cross-language numerical differences or pass/fail claims are made because the Python/comparison evidence does not exist.

## Files read and written

Read: the live task and required governance files; predecessor numerical task/report; accepted Owner helper-source audit; accepted P2 Python source and policy/case-authority files; three designated MATLAB sources; frozen predecessor manifest, P2 harnesses, P1 outputs and orientation evidence.

Repository write: only this report. External artifact writes were limited to the immutable P2 input copies, one metadata-only decoder preflight, one corrected MATLAB harness, and the reached MATLAB P2 JSON output.

## Forbidden-operation check

- P1 rerun: no
- predecessor artifact modified, renamed, regenerated or overwritten: no
- MATLAB production source/helper modified: no
- Python production source/test modified: no
- byte-frozen `p2_python.py` or `compare_p2.py` modified: no
- P2 case/order/derivative/adapter/tolerance/semantics changed: no
- corrected MATLAB scientific harness edited or rerun after invocation: no
- failed Python P2 harness edited or rerun: no
- comparison invoked without complete Python output: no
- P3/P4 or P5 entered: no
- AR(1), transition, IRF, calibration extension or Results entered: no
- merge, rebase, reset or force-push: no

## Acceptance and recommended next gate

P1 remains accepted. P2 parity evidence is incomplete and not accepted; this report does not authorize P3/P4, P5, or dynamic extension.

A new exact live GitHub task is required to reconcile the frozen P2 Python harness/API arity defect and decide whether the already completed corrected MATLAB P2 output may be reused. This report does not invent the successor task name or execution authority.
