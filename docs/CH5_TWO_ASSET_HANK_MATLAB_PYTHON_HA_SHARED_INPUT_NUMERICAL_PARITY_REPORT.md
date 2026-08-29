# CH5 Two-Asset HANK MATLAB–Python HA Shared-Input Numerical Parity

## Primary classification

`MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT`

P1 completed and passed. P2 was blocked by the already-frozen MATLAB harness before any P2 scientific case was evaluated. Under the fail-closed task rule, the harness was not edited or rerun, P2 Python/comparison were not invoked, and P3–P4 were not entered.

This report does not issue final Owner parity acceptance.

## Live/source/workspace identity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched live/base `origin/main`: `30ce23b44f40eea621e9dd84a0d26520ad0f0a0f`
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Isolated Git workspace: `D:\ProjectTemp\ch5-ha-shared-input-parity-repo-20260829`
- Parity artifact root: `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..30ce23b44f40eea621e9dd84a0d26520ad0f0a0f -- src tests`: empty

Python scientific/test source continuity: `PASS`.

Verified MATLAB source identities:

| File | Bytes | SHA-256 |
|---|---:|---|
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m` | 12227 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_cost.m` | 691 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m` | 565 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |

All required source identities passed before numerical execution. GNU Octave was not used.

## Executable identities

- MATLAB executable: `C:\Program Files\MATLAB\R2022b\bin\matlab.exe`
- MATLAB version: `9.13.0.2049777 (R2022b)`; release `2022b`
- Python executable: `C:\Users\zcxve\AppData\Local\Programs\Python\Python311\python.exe`
- Python version: `3.11.9`

## Files read and written

Required live task/rules, accepted structural/parity reports, accepted P1–P4 Python sources and relevant R4 policy/truncation case-authority tests were read. The three designated MATLAB sources above were read and fingerprinted.

The only repository file written is:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`

All manifest, harnesses and raw outputs were written only under the separate artifact root.

## Frozen manifest and harness inventory

These identities were frozen before P1 began and were not changed afterward.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `manifest.json` | 2329 | `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449` |
| `p1_matlab.m` | 1247 | `21E6D453C8F41F6101216F677ED775ACA1ADB12F88AFE61D641D3A94BB83834F` |
| `p1_python.py` | 1243 | `B5724E6F3ED4023AB7AF29A396F1A4B328BF271C5812E8A10449448120F016E8` |
| `compare_p1.py` | 1672 | `75DF9A7CF2C1F595D02DD54D88287E23E4141BF91A15D9A42B4C31DBA1C98278` |
| `p2_matlab.m` | 1275 | `0CB2C08ABC856FC90A5720971D230CA9CABBC7564F8A7FD7CAFC4E0F6B19815F` |
| `p2_python.py` | 3820 | `2E9F6198FD906E6703416E4F48DE6CD1DBA6F7A2EA365360890AA92CBDBED6B0` |
| `compare_p2.py` | 1684 | `4B114245AF4F5895357465A1AE41AE608F026E297B6E044C16441EC7A7AAF70B` |
| `p3_matlab.m` | 914 | `8695C99E9E5591C5DCBC8EDF9DCA958DE9D9E2F58C4388D45FC5A0A184D92C51` |
| `p3_python.py` | 985 | `4D99C21DD95D4CEC45D627BA17ED4853EB6066EC7DD6BA26E4957739F1608622` |
| `compare_p3.py` | 1200 | `4504A7118EE222C859FF2DCA0133AE12DCF6298592019B3C8ADE7D2CA9FDE267` |
| `p4_matlab.m` | 679 | `9549C508E208D4507FC59392766D9408232371F2210ACFA487A14F8B6C3E9B34` |
| `p4_python.py` | 992 | `FE47FF72613E8E685AE6B9B107A5E6884993196CCE88B286F8ABA7B5B39A9893` |
| `compare_p4.py` | 1614 | `5533E22A60876E6B448FD938B79034E2F03F1DE51A83D65C5D7A1946E1879CDE` |
| `verify_manifest.py` | 494 | `69029AEDC6987FBFCC254F73C45702C8AA4AA5B00AECC0C599E246760725C7FC` |

Pre-freeze static checks passed. MATLAB `checkcode` returned no issues for P2–P4; P1 had five indentation/alignment warnings for same-line nested loops, not syntax errors.

## Frozen tolerances

- `tau_fp(x,y) = 128*eps64*max(1,abs(x),abs(y))`
- array analogue: `128*eps64*max(1,max(abs(A)),max(abs(B)))`
- zero/drift classification: `1e-12`
- KKT validity: `1e-7`
- generator validity: `1e-11`
- generator parity: `1e-11*max(1,max_abs(G_M),max_abs(G_P))`
- stationary residual/normalization: `1e-10`
- stationary mass parity: `1e-10`
- nonnegative mass floor: `-1e-12`
- aggregate parity: `1e-10*max(1,abs(X_M),abs(X_P))`

No tolerance was changed or widened.

## Orientation permutation

MATLAB `[b,a,z]`, `b`-fast indices map to Python `(a,b,z)`, `a`-fast indices through the zero-based permutation:

`[0,3,6,1,4,7,2,5,8,9,12,15,10,13,16,11,14,17]`.

The inverse is the same permutation for the frozen `3×3×2` shape. Exact forward/inverse round-trip identity passed before P1.

Raw verification artifact:

- `orientation_verification.json`: 385 bytes; SHA-256 `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2`

## Stage execution counts

| Stage | MATLAB scientific harness | Python scientific harness | Comparison | Scientific cases reached | Status |
|---|---:|---:|---:|---:|---|
| P1 | 1 | 1 | 1 | 432 | PASS |
| P2 | 1 invocation | 0 | 0 | 0 | BLOCKED before first case |
| P3 | 0 | 0 | 0 | 0 | not reached |
| P4 | 0 | 0 | 0 | 0 | not reached |

MATLAB version/checkcode invocations occurred only in the pre-scientific runtime/harness gate and are not P-stage scientific calls.

## P1 full frozen-case result

The full Cartesian set was evaluated: `4 a × 3 b × 4 z × 3 v_b × 3 q = 432` cases, with no omission.

For each `(a,q)` row below, all `3 b × 4 z × 3 v_b = 36` combinations passed the stated rule.

| `a` | `q` | Cases | MATLAB `d` | Python `d` | Required treatment | Result |
|---:|---:|---:|---|---|---|---|
| 0.0 | -0.20 | 36 | `0` | approximately `-0.075` | frozen bare-`a` counterexample plus accepted `max(a,a_bar)` proof | PASS |
| 0.0 | 0.00 | 36 | `0` | `0` | zero subgradient/common control | PASS |
| 0.0 | 0.20 | 36 | `0` | approximately `0.075` | frozen bare-`a` counterexample plus accepted `max(a,a_bar)` proof | PASS |
| 0.25 | -0.20 | 36 | approximately `-0.0375` | approximately `-0.075` | frozen legacy difference | PASS |
| 0.25 | 0.00 | 36 | `0` | `0` | zero subgradient/common control | PASS |
| 0.25 | 0.20 | 36 | approximately `0.0375` | approximately `0.075` | frozen legacy difference | PASS |
| 0.5 | -0.20 | 36 | same | same | machine-scale equality | PASS |
| 0.5 | 0.00 | 36 | `0` | `0` | machine-scale equality | PASS |
| 0.5 | 0.20 | 36 | same | same | machine-scale equality | PASS |
| 1.0 | -0.20 | 36 | same | same | machine-scale equality | PASS |
| 1.0 | 0.00 | 36 | `0` | `0` | machine-scale equality | PASS |
| 1.0 | 0.20 | 36 | same | same | machine-scale equality | PASS |

There were 144 explicit nonzero-transfer low-`a` legacy counterexamples. They were expected and authorized, not hidden or treated as parity failures.

Maximum mapped difference for every materially comparable P1 field was exactly zero:

| Field | Maximum difference |
|---|---:|
| consumption | 0 |
| scalar labor | 0 |
| labor income | 0 |
| liquid interest component | 0 |
| transfer `d` for `a>=a_bar` | 0 |
| adjustment cost at a common `d` | 0 |
| `mu_a` under the corresponding authorized control | 0 |
| `mu_b` under the corresponding authorized control | 0 |

For `a<a_bar`, MATLAB transfer matched its bare-`a` analytic formula, Python transfer matched the accepted `max(a,a_bar)` analytic formula, adjustment cost matched cross-language at each common control, and each language's drift calculation matched the common budget identities. Downstream differences caused solely by the authorized legacy FOC scale were retained as O1 redesign evidence.

P1 raw artifacts:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `p1_matlab.json` | 146443 | `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886` |
| `p1_python.json` | 217784 | `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD` |
| `p1_compare.json` | 26665 | `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550` |

## P2 terminal block

P2 MATLAB was invoked once. It terminated at `p2_matlab.m:2`, before entering or evaluating the first frozen scientific case, at:

`cse=m.p2(k); rows(k).id=cse.id; rows(k).kind=cse.kind;`

MATLAB's localized error output reported that dot indexing was unsupported for the decoded variable type. The heterogeneous `p2` JSON entries decoded into a container for which the frozen harness's `cse.id` access was invalid.

This is a frozen-harness serialization/access defect, not observed numerical evidence about any P2 policy case. Per task authority:

- the frozen harness was not edited;
- P2 was not rerun;
- no P2 output JSON was created;
- P2 Python and comparison calls remained zero;
- P3 and P4 remained zero.

Because scientific case evaluation never began, this is classified as a harness/source-environment BLOCKED state rather than `MATLAB_PYTHON_TWO_ASSET_HA_P2_FAIL_CLOSED`.

## P3 and P4

Not reached. No generator, KFE, stationary mass, or parity aggregate evidence was produced. The already-frozen P3/P4 harness identities above are preparation evidence only and must not be interpreted as execution.

## Complete raw artifact inventory

All reached raw evidence remains outside the repository under `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`. The inventory consists of the 14 frozen manifest/harness files, `orientation_verification.json`, and the three P1 JSON files listed above. No P2–P4 raw numerical output exists.

## Forbidden-operation check

- MATLAB source/helpers modified: no
- Python source/tests modified: no
- Octave substituted: no
- frozen manifest/harness changed after P1 began: no
- P1 rerun: no
- P2 harness edited or rerun after block: no
- P2 Python/comparison run: no
- P3/P4 entered: no
- tolerance widened or case tuned: no
- O1–O12 decisions changed: no
- final Owner parity acceptance claimed: no
- AR(1), transition, IRF, calibration extension or Results work entered: no
- merge, rebase, reset or force-push: no

## Recommended next gate

A new live GitHub **P2 harness-block diagnostic/correction authorization** is required. Its exact task name must be issued by the reviewer; this report does not invent execution authority. It should inspect the frozen `p2_matlab.m`/manifest serialization mismatch, authorize a corrected immutable harness baseline, and define whether P1 evidence may be reused or must be rerun under a new bounded task.

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE` is **not** authorized or recommended because P2–P4 evidence is incomplete. Dynamic extension remains blocked.
