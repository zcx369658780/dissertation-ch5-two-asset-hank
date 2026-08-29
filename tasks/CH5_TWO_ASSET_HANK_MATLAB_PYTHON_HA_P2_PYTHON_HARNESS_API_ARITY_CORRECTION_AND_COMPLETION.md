# CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION

## Task

Correct the frozen Python P2 parity-harness `check_boundary` API-arity defect, preserve the already accepted P1 evidence and the already completed corrected MATLAB P2 output, and complete exactly one Python P2 + one P2 comparison attempt.

This is a bounded P2-completion gate. It does **not** authorize:

- P1 rerun;
- MATLAB P2 rerun;
- P3/P4 execution;
- P5 Owner acceptance;
- modification of MATLAB or Python production source/tests;
- scientific-case changes;
- tolerance changes;
- AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor evidence

Latest P2 correction report commit:

`21209b9e409f77198f6f4e97ed2c874e71966ced`

Its task-authority parent:

`394b7b2668a616c7a2c372dde678866bf41ddf6e`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted P1 status:

`P1_EVIDENCE_REUSED_AND_REMAINS_ACCEPTED`

Accepted MATLAB P2 execution status:

- corrected MATLAB harness executed exactly once;
- all 10/10 frozen P2 rows completed;
- no P2 scientific mismatch was declared because Python/comparison evidence was not reached.

The predecessor Python block is classified as:

`P2_PYTHON_HARNESS_CHECK_BOUNDARY_API_ARITY_BLOCK_BEFORE_FIRST_PYTHON_ROW`

It is a harness/API-plumbing defect, not a scientific numerical failure.

## Scientific route

The HA block remains a hard gate:

`P1 accepted -> P2 completed and accepted -> P3 generator parity -> P4 KFE/stationary parity -> Owner P5 acceptance -> only then dynamic extension`

Do not authorize or enter AR(1), transition, or IRF work from this task.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY.md`
- `tasks/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_HARNESS_BLOCK_CORRECTION_AND_REEXECUTION.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_HARNESS_BLOCK_CORRECTION_AND_REEXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- accepted Python P2-relevant source/tests, especially `src/ch5_two_asset_hank/boundaries.py`, `economics.py`, `policies.py`, and the relevant R4 case-authority tests.

Verify live Python scientific/test source remains unchanged from:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

If scientific source drift exists, stop:

`BLOCKED_P2_PYTHON_CORRECTION_SOURCE_DRIFT`

## Production API authority

The accepted production API is:

```python
check_boundary(
    i_a: int,
    i_b: int,
    n_a: int,
    n_b: int,
    mu_a: float,
    mu_b: float,
    tolerance: float,
)
```

The productivity index `i_z` is **not** an argument to `check_boundary`.

The frozen P2 Python harness incorrectly uses:

```python
check_boundary(*idx, 3, 3, ma, mb, tol)
```

where a frozen case index such as `idx=(1,1,0)` expands to `(i_a,i_b,i_z)` and therefore creates eight positional arguments.

The only authorized semantic correction to that call is to pass the two asset indices and omit the productivity index, e.g.:

```python
check_boundary(idx[0], idx[1], 3, 3, ma, mb, tol)
```

An equivalent plumbing-only expression is allowed if it is demonstrably identical. Do not alter `check_boundary` production code or any scientific input.

## MATLAB/source identity gates

Verify the three designated MATLAB files remain exact:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

Do not execute MATLAB scientific P2 again in this task.

## Required predecessor artifact identity gates

Read-only inspect both predecessor parity artifact roots:

`D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`

and

`D:\ProjectTemp\ch5-ha-p2-harness-correction-20260829`

Do not modify, rename, regenerate, or overwrite either root.

Require exact identities for at least:

### Original frozen inputs

- `manifest.json`
  - SHA-256 `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449`
- original `p2_python.py`
  - 3820 bytes
  - SHA-256 `2E9F6198FD906E6703416E4F48DE6CD1DBA6F7A2EA365360890AA92CBDBED6B0`
- original `compare_p2.py`
  - 1684 bytes
  - SHA-256 `4B114245AF4F5895357465A1AE41AE608F026E297B6E044C16441EC7A7AAF70B`
- `orientation_verification.json`
  - SHA-256 `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2`

### Accepted P1 outputs

- `p1_matlab.json`
  - SHA-256 `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886`
- `p1_python.json`
  - SHA-256 `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD`
- `p1_compare.json`
  - SHA-256 `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550`

### Completed corrected MATLAB P2 evidence

- `p2_matlab_corrected.m`
  - 1275 bytes
  - SHA-256 `EF8ADD59AF0C0AC96C8E8F2DD80FB8E4C405BB5F8C0BAEF93FEDD4E801B1103A`
- corrected MATLAB P2 output JSON
  - 3093 bytes
  - SHA-256 `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C`

If any required identity fails, stop before scientific execution:

`BLOCKED_P2_PYTHON_CORRECTION_PREDECESSOR_EVIDENCE_DRIFT`

## Evidence-reuse decision

If all identity gates pass:

- P1 is accepted and MUST NOT be rerun;
- corrected MATLAB P2 output is accepted as immutable reached evidence and MUST NOT be rerun;
- the complete 10-case MATLAB output may be copied byte-for-byte into the new correction artifact root for comparison;
- the original frozen `compare_p2.py` must remain byte-identical if it is reused.

Return in the report:

`P1_AND_CORRECTED_MATLAB_P2_EVIDENCE_REUSED`

Do not consume a second MATLAB P2 scientific call merely for convenience.

## New isolated correction artifact root

Create a new external root, for example:

`D:\ProjectTemp\ch5-ha-p2-python-harness-correction-20260829`

It must remain outside the repository and outside the designated MATLAB source tree.

Copy into it, byte-for-byte:

- `manifest.json`;
- original frozen `p2_python.py`;
- original frozen `compare_p2.py`;
- completed corrected MATLAB P2 output JSON;
- any read-only metadata needed to verify case order.

Record hashes immediately after copy.

## Corrected Python harness authority

Create exactly one new corrected harness:

`p2_python_corrected.py`

The diff against original frozen `p2_python.py` may change **only** the invalid `check_boundary` argument plumbing needed to conform to the accepted seven-argument production API.

It MUST NOT change:

- the 10 scientific cases;
- state coordinates;
- derivative/shadow inputs;
- case ordering;
- policy formulas;
- candidate construction/selection;
- boundary/KKT thresholds;
- output fields;
- JSON semantics;
- orientation adapter;
- tolerances;
- expected classifications;
- production imports or production code.

Before execution:

1. generate a full textual diff original -> corrected;
2. verify only the authorized arity/plumbing line changed;
3. run static syntax compilation only;
4. record corrected file bytes and SHA-256;
5. freeze it immutable.

If any further harness defect is visible before scientific execution, stop and request new authority; do not broaden the correction.

After the corrected Python scientific invocation begins, the corrected harness must never be edited or rerun in this task.

## Frozen P2 comparison contract

Retain exactly the predecessor frozen P2 case set, classifications and numerical tolerances.

For comparable cases, the predecessor tolerance remains:

`tau_fp(x,y) = 128 * eps_float64 * max(1, abs(x), abs(y))`

with the frozen array analogue where applicable.

Also retain:

- zero/drift classification `1e-12`;
- KKT validity `1e-7`.

Do not widen or replace these thresholds.

The 10 frozen case order remains exactly:

1. `interior_ff`
2. `interior_bb`
3. `liquid_zero`
4. `lower_a_active`
5. `lower_b_active`
6. `interior_mu_a_zero`
7. `upper_a_lower_b`
8. `upper_a_interior_b`
9. `dual_upper`
10. `lower_b_fz_near_tie`

The first three include directly comparable MATLAB/Python local objects. The remaining accepted redesign cases require Python analytic/KKT/boundary validation and explicit MATLAB legacy/omission evidence as already frozen by structural authority.

## Exact execution budget

After all pre-execution gates pass:

### P1

- MATLAB: `0`
- Python: `0`
- comparison: `0`

P1 is reuse-only.

### MATLAB P2

- scientific harness: `0`

Reuse the exact completed predecessor MATLAB P2 JSON.

### Python P2

Execute corrected `p2_python_corrected.py` exactly **once**.

If it fails before producing complete 10-case output:

- stop;
- do not edit;
- do not rerun;
- do not run comparison;
- classify as harness/environment block unless reached numerical evidence proves a material scientific mismatch.

### Comparison P2

Only if the corrected Python output is complete for all 10 cases, execute the byte-identical original `compare_p2.py` exactly **once** against:

- reused completed corrected MATLAB P2 JSON; and
- newly produced corrected Python P2 JSON.

If comparison itself has a harness/plumbing defect, stop without editing or rerunning it.

### P3/P4/P5

- P3: `0`
- P4: `0`
- P5: not authorized

## Required P2 evidence

Report for all 10 cases:

- frozen state and derivative inputs;
- MATLAB reached output or explicit legacy omission;
- Python controls/policy evidence;
- consumption;
- labor;
- transfer `d`;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- utility;
- Hamiltonian where materially comparable;
- boundary feasibility;
- KKT validity and residual evidence where available;
- raw/canonical Python candidate identity where relevant;
- mapped numerical difference and frozen bound for every comparable object;
- exact redesign classification for Python-only cases.

For cases 1–3, comparable quantitative fields must pass the frozen `tau_fp` rule. Qualitative similarity is insufficient.

For cases 4–10, a PASS requires the Python redesign candidate to satisfy its accepted analytic zero-drift/boundary/KKT contract and the MATLAB side to be correctly classified as legacy omission/incomplete representation where applicable.

## Terminal classifications

Return exactly one P2 classification:

- `MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS`
- `MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P2_PYTHON_CORRECTION_BLOCKED_ENVIRONMENT_OR_HARNESS`

A PASS means only P2 is accepted for later P3/P4 parity work. It does not authorize P5 or dynamics.

## Report authorization

Write exactly one repository file:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`

The report must include:

- live/source identity;
- predecessor artifact verification;
- explicit P1 and MATLAB-P2 reuse decision;
- original/corrected Python harness diff;
- corrected harness SHA-256/bytes;
- exact execution counts;
- complete P2 10-case evidence if reached;
- comparison result if reached;
- terminal P2 classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the new report may be added to the repository.

Whether PASS, FAIL_CLOSED, or BLOCKED, if that report is the sole repository change:

- explicitly stage only the report;
- create one commit;
- fresh-fetch remote before push;
- fast-forward push only if remote `main` has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Complete P2 parity after Python harness API correction`

## Forbidden operations

Do not:

- rerun P1;
- rerun MATLAB P2;
- modify predecessor artifacts;
- modify MATLAB production source/helpers;
- modify Python production source/tests;
- change scientific cases, case order, formulas, expected classifications, orientation, or tolerances;
- edit/retry a scientific harness after its authorized invocation begins;
- enter P3/P4/P5;
- authorize or enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If P2 returns `MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS` and is independently accepted:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY`

That future gate should reuse accepted P1/P2 evidence, execute only P3 then P4 in bounded fail-closed order, and still require explicit Owner P5 acceptance before any dynamic extension.
