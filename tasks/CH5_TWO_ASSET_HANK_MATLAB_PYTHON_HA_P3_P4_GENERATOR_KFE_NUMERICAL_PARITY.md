# CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY

## Task

Complete the remaining shared-input numerical parity for the two-asset HA core by executing:

`P3 generator parity -> P4 KFE/stationary-distribution/aggregate parity`

using the already accepted P1 and P2 numerical evidence without rerunning them.

This is the last numerical-evidence gate before Owner P5 acceptance. It does **not** authorize P5 acceptance itself, AR(1), transition dynamics, IRFs, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor evidence

Accepted P1 evidence:

`P1_SHARED_INPUT_POINTWISE_NUMERICAL_PARITY_PASS__432_CASES`

Accepted P2 evidence commit:

`565c6564e5e5083183c853e65bca09c3bf1b9f05`

Accepted P2 classification:

`MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS`

Accepted structural closure:

`OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted MATLAB identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

## Hard route

The HA block remains a hard prerequisite:

`P1 accepted -> P2 accepted -> P3 accepted -> P4 accepted -> independent review -> Owner P5 acceptance -> only then dynamic extension`

Do not create, issue, or execute AR(1), transition, IRF, calibration-extension, or Results tasks from this gate.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- accepted Python source required for P3/P4, including at minimum:
  - `src/ch5_two_asset_hank/contracts.py`
  - `src/ch5_two_asset_hank/generator.py`
  - `src/ch5_two_asset_hank/indexing.py`
  - `src/ch5_two_asset_hank/kfe_contract.py`
  - `src/ch5_two_asset_hank/kfe.py`

Verify live Python scientific/test source is unchanged from:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

If drift exists, stop:

`BLOCKED_P3_P4_PARITY_PYTHON_SOURCE_DRIFT`

## Evidence reuse gates

Do **not** rerun P1 or P2.

Read-only verify the exact predecessor artifact roots:

- `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`
- `D:\ProjectTemp\ch5-ha-p2-python-harness-correction-20260829`

At minimum require exact identities for:

### P1 accepted outputs

- `p1_matlab.json` SHA-256 `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886`
- `p1_python.json` SHA-256 `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD`
- `p1_compare.json` SHA-256 `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550`

### P2 accepted outputs

- reused corrected MATLAB P2 output SHA-256 `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C`
- accepted Python P2 output SHA-256 `E27F3B557123B8ED1BBFB8986B63861075C43106264EAAC4FC867797E237978A`
- accepted P2 comparison output SHA-256 `0851FD1AF8899594B21BC01F593B329918E56C06F5CEA68901A28EDD49B1AE56`

### Shared manifest/orientation authority

- `manifest.json` SHA-256 `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449`
- `orientation_verification.json` SHA-256 `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2`

If any accepted predecessor identity differs, stop:

`BLOCKED_P3_P4_PARITY_PREDECESSOR_EVIDENCE_DRIFT`

If all pass, record:

`P1_P2_EVIDENCE_REUSED_AND_ACCEPTED`

## MATLAB source/runtime identity

Verify the three accepted MATLAB source hashes exactly.

Use MATLAB R2022b; do not substitute Octave.

Record exact MATLAB executable/version and Python executable/version.

If MATLAB is unavailable or identity differs, stop before scientific execution.

## P3/P4 predecessor harness identities

Read-only inspect the predecessor frozen files under:

`D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`

Require exact identities:

- `p3_matlab.m`: 914 bytes, SHA-256 `8695C99E9E5591C5DCBC8EDF9DCA958DE9D9E2F58C4388D45FC5A0A184D92C51`
- `p3_python.py`: 985 bytes, SHA-256 `4D99C21DD95D4CEC45D627BA17ED4853EB6066EC7DD6BA26E4957739F1608622`
- `compare_p3.py`: 1200 bytes, SHA-256 `4504A7118EE222C859FF2DCA0133AE12DCF6298592019B3C8ADE7D2CA9FDE267`
- `p4_matlab.m`: 679 bytes, SHA-256 `9549C508E208D4507FC59392766D9408232371F2210ACFA487A14F8B6C3E9B34`
- `p4_python.py`: 992 bytes, SHA-256 `FE47FF72613E8E685AE6B9B107A5E6884993196CCE88B286F8ABA7B5B39A9893`
- `compare_p4.py`: 1614 bytes, SHA-256 `5533E22A60876E6B448FD938B79034E2F03F1DE51A83D65C5D7A1946E1879CDE`

These files were frozen before the original P1 run but never scientifically executed.

## Fresh workspace and correction authority

Use:

- a fresh isolated Git workspace rooted at current live `origin/main`;
- a new external artifact root, e.g. `D:\ProjectTemp\ch5-ha-p3-p4-parity-20260829`.

Copy the predecessor P3/P4 harnesses byte-for-byte into the new external root.

Before any P3 scientific execution, perform **pre-scientific compatibility review only**:

- Python static compilation;
- MATLAB `checkcode`;
- inspect current accepted production function signatures used by the harnesses;
- inspect JSON/container assumptions needed only for input/output plumbing;
- verify orientation permutation round-trip and expected matrix dimensions.

No economic formula, generator matrix, stationary mass, or aggregate may be numerically evaluated during this preflight.

### Limited harness-correction authority

If and only if preflight identifies a pure harness plumbing/API/container defect analogous to the prior P2 defects, one corrected P3 and/or P4 harness may be created before P3 begins.

Any correction must be limited to:

- API positional/keyword plumbing;
- import/path plumbing;
- JSON cell/struct/list/dict access;
- serialization/deserialization;
- array reshape/order plumbing required to implement the already-frozen orientation adapter;
- output-container formatting.

It may **not** change:

- shared grids;
- drifts;
- `Q_common`;
- formulas;
- generator construction semantics;
- stationary equations;
- case values;
- tolerance values;
- orientation permutation itself;
- comparison semantics.

For each corrected harness:

- generate the complete predecessor->corrected diff;
- prove every diff hunk is plumbing-only;
- record SHA-256/bytes;
- freeze before P3 begins;
- no edit after P3 begins.

If a required correction changes scientific semantics, stop and request new authority.

## Frozen tolerances

Reuse the predecessor numerical parity task tolerances without modification:

- zero/drift classification: `1e-12`
- generator validity: `1e-11`
- shared generator parity:
  `max_abs(G_M_mapped-G_P) <= 1e-11 * max(1,max_abs(G_M_mapped),max_abs(G_P))`
- stationary KFE residual/normalization: `1e-10`
- stationary mass parity: `max_abs(g_M_mapped-g_P) <= 1e-10`
- nonnegative mass floor: `-1e-12`
- aggregate parity:
  `abs(X_M-X_P) <= 1e-10 * max(1,abs(X_M),abs(X_P))`

Do not widen tolerances after observing results.

## Frozen P3 shared finite object

Use exactly:

- `a = [0.0, 0.5, 1.0]`
- `b = [0.0, 2.5, 5.0]`
- parity-only `z = [0.75, 1.25]`

### Frozen `mu_a`

For each `(i_a,i_b,i_z)`:

- lower `a` (`i_a=0`): `+0.020 + 0.005*i_z`
- interior `a` (`i_a=1`): `+0.015` when `i_z=0`, `-0.015` when `i_z=1`
- upper `a` (`i_a=2`): `-0.020 - 0.005*i_z`

### Frozen `mu_b`

- lower `b` (`i_b=0`): `+0.030`
- interior `b` (`i_b=1`): `+0.020` when `i_z=0`, `-0.020` when `i_z=1`
- upper `b` (`i_b=2`): `-0.030`

### Frozen common productivity adapter

For parity P3/P4 only:

`Q_common = [[-0.4, 0.4], [0.3, -0.3]]`

This is only a shared mathematical adapter object. It does not replace MATLAB production `la_mat` or Python production reflected diffusion.

## P3 execution

After all identity and preflight gates pass, execute exactly once each, in order:

1. MATLAB P3 scientific harness;
2. Python P3 scientific harness;
3. P3 comparison harness.

Do not rerun any of them.

### P3 required evidence

After the frozen MATLAB<->Python orientation adapter, compare:

- full `G_a` matrix;
- full `G_b` matrix;
- every nonzero transition destination and rate;
- every diagonal entry;
- component row sums;
- off-diagonal signs;
- common productivity component from `Q_common`;
- total common backward generator;
- component-sum identity.

Require:

- exact state-destination mapping after adapter;
- generator mapped differences within the frozen `1e-11` parity rule;
- each generator row-sum validity within `1e-11`;
- no negative off-diagonal rate below tolerance.

If P3 has any material mismatch, stop immediately:

`MATLAB_PYTHON_TWO_ASSET_HA_P3_GENERATOR_PARITY_FAIL_CLOSED`

Do not execute P4.

If P3 harness blocks before scientific output, stop with a named harness/environment block; do not edit/rerun after P3 begins.

## P4 execution

P4 is authorized only if P3 PASSes.

Use **exactly the P3-accepted common total backward generator**. Do not reconstruct a different generator.

### Common finite-state measure

- probability mass object;
- `sum(g)=1`;
- unit positive cell weights;
- density is not the primary parity object;
- `A_hh`, `B_hh` are expectations under the same mapped normalized mass.

### MATLAB P4

Use the mapped common backward generator and solve the mathematical stationary object from `G'` using the frozen parity harness. MATLAB's arbitrary production pin-row location is not itself a parity target; the resulting stationary object is.

### Python P4

Use accepted production pathways where compatible:

- `make_kfe_input(...)` / accepted KFE input contract;
- `solve_stationary_kfe(...)`.

Do not modify the production KFE solver.

### Exact P4 execution counts

Execute exactly once each:

1. MATLAB P4 harness;
2. Python P4 harness;
3. P4 comparison harness.

No reruns.

### P4 required evidence

Compare/report:

- mapped forward operator transpose relation;
- mapped stationary mass vector;
- `||G^T g||_inf` on each side;
- normalization error;
- minimum mass and negative-mass count;
- maximum mapped mass difference;
- exact/frozen mass-parity bound;
- `A_hh` and `B_hh` on each side;
- aggregate absolute differences and bounds.

P4 PASS requires:

- both stationary residuals `<=1e-10`;
- both normalization errors `<=1e-10`;
- no mass below `-1e-12`;
- mapped mass difference `<=1e-10`;
- `A_hh/B_hh` differences within frozen relative `1e-10` rule.

If P4 fails, stop fail-closed and do not repair/rerun.

## Final classifications for this task

Return exactly one P3 classification:

- `MATLAB_PYTHON_TWO_ASSET_HA_P3_GENERATOR_PARITY_PASS`
- `MATLAB_PYTHON_TWO_ASSET_HA_P3_GENERATOR_PARITY_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P3_BLOCKED_ENVIRONMENT_OR_HARNESS`

If and only if P3 PASSes, return exactly one P4 classification:

- `MATLAB_PYTHON_TWO_ASSET_HA_P4_KFE_STATIONARY_PARITY_PASS`
- `MATLAB_PYTHON_TWO_ASSET_HA_P4_KFE_STATIONARY_PARITY_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P4_BLOCKED_ENVIRONMENT_OR_HARNESS`

If P1-P4 evidence is all accepted after this execution, return overall evidence status:

`MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_EVIDENCE_COMPLETE__OWNER_P5_ACCEPTANCE_PENDING`

Do **not** issue final Owner parity acceptance from this task.

## Report authorization

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`

The report must include:

- live/source/runtime identities;
- predecessor evidence/hash verification;
- P1/P2 reuse decision;
- predecessor P3/P4 harness hash verification;
- any pre-scientific harness corrections and complete diffs;
- exact P3/P4 execution counts;
- complete P3 matrix/destination/rate/row-sum/off-diagonal comparison evidence;
- complete P4 mass/residual/normalization/nonnegativity/aggregate evidence;
- all frozen bounds and observed differences;
- terminal failure/block if any;
- forbidden-operation check;
- acceptance level;
- recommended next gate.

## Commit/push authorization

Whether PASS, FAIL_CLOSED, or BLOCKED, if the new report is the only repository change:

- explicitly stage only the report;
- create one commit;
- fresh-fetch remote before push;
- fast-forward push only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Record P3 P4 generator KFE HA numerical parity`

## Forbidden operations

Do not:

- rerun P1 or P2;
- modify accepted predecessor outputs;
- modify MATLAB production source/helpers;
- modify Python production source/tests;
- alter shared grid/drifts/`Q_common`/orientation/tolerances after authority freeze;
- tune after seeing output;
- continue to P4 after P3 failure;
- rerun a failed/blocked scientific stage;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If P3 and P4 both PASS and independent review accepts the evidence:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

Only that future gate may record the Owner's final HA parity decision and decide whether dynamic extension can be unlocked.
