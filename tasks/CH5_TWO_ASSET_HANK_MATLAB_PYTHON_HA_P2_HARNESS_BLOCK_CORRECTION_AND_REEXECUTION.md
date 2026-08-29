# CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_HARNESS_BLOCK_CORRECTION_AND_REEXECUTION

## Task

Diagnose and correct the frozen MATLAB P2 parity-harness serialization/access defect, preserve the already accepted P1 numerical evidence, and execute exactly one corrected P2 scientific parity attempt.

This is a bounded harness-correction and P2-only execution gate. It does **not** authorize P1 rerun, P3/P4 execution, P5 Owner acceptance, MATLAB/Python production-source modification, tolerance changes, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted predecessor evidence

Numerical-parity report commit:

`1b26e9cedded11ac8c96e1deb6560cc8d200e465`

Predecessor task authority commit:

`30ce23b44f40eea621e9dd84a0d26520ad0f0a0f`

Accepted P1 status:

`P1_SHARED_INPUT_POINTWISE_NUMERICAL_PARITY_PASS__432_CASES`

P1 may be reused under this task **without rerun** if and only if all identity gates below pass.

The predecessor P2 block is classified as:

`P2_HARNESS_SERIALIZATION_ACCESS_BLOCK_BEFORE_FIRST_SCIENTIFIC_CASE`

It is not a P2 scientific numerical failure.

## Why P1 evidence is reusable

The predecessor report established before the P2 block:

- Python scientific/test source identity PASS;
- all three designated MATLAB source/helper identities PASS;
- MATLAB R2022b identity;
- frozen manifest and harness hashes;
- orientation permutation round-trip PASS;
- P1 MATLAB/Python/comparison each executed exactly once;
- all 432 P1 cases executed;
- every materially comparable P1 field had maximum mapped difference `0`;
- 144 low-`a` nonzero-transfer cases reproduced the accepted MATLAB legacy FOC counterexample while Python retained the accepted `max(a,a_bar)` contract;
- no source, tolerance, manifest, orientation adapter, or P1 harness changed afterward.

Therefore rerunning P1 would add no scientific information and would violate the desired bounded-evidence route. Reuse is authorized only if all predecessor artifacts and source identities remain exact.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- accepted Python source and case-authority tests needed for P2.

Verify accepted Python scientific/test source remains unchanged from:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

If drift exists, stop:

`BLOCKED_P2_CORRECTION_PYTHON_SOURCE_DRIFT`

## MATLAB source identity gate

Verify exact files under:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

- `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m` SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m` SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

Require MATLAB R2022b and no Octave substitution.

If any identity differs, stop:

`BLOCKED_P2_CORRECTION_MATLAB_SOURCE_OR_RUNTIME_DRIFT`

## Preserved predecessor artifact root

Read-only inspect:

`D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`

Do not modify, delete, rename, regenerate, or overwrite any predecessor artifact.

Verify at minimum these frozen identities:

- `manifest.json` — 2329 bytes — SHA-256 `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449`
- `p2_matlab.m` — 1275 bytes — SHA-256 `0CB2C08ABC856FC90A5720971D230CA9CABBC7564F8A7FD7CAFC4E0F6B19815F`
- `p2_python.py` — 3820 bytes — SHA-256 `2E9F6198FD906E6703416E4F48DE6CD1DBA6F7A2EA365360890AA92CBDBED6B0`
- `compare_p2.py` — 1684 bytes — SHA-256 `4B114245AF4F5895357465A1AE41AE608F026E297B6E044C16441EC7A7AAF70B`
- `p1_matlab.json` — SHA-256 `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886`
- `p1_python.json` — SHA-256 `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD`
- `p1_compare.json` — SHA-256 `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550`
- `orientation_verification.json` — 385 bytes — SHA-256 `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2`

If any required predecessor identity differs, stop:

`BLOCKED_P2_CORRECTION_PREDECESSOR_ARTIFACT_DRIFT`

Do not rerun P1 to compensate.

## New isolated correction artifact root

Use a new root, for example:

`D:\ProjectTemp\ch5-ha-p2-harness-correction-20260829`

Copy only the immutable inputs needed for P2, preserving byte identity where no correction is authorized:

- `manifest.json` — exact byte copy;
- `p2_python.py` — exact byte copy;
- `compare_p2.py` — exact byte copy.

Do not copy P1 harnesses for execution. P1 raw evidence remains referenced from the predecessor root.

## Read-only P2 blocker diagnosis

Before creating a corrected scientific harness, inspect:

- the exact JSON schema of `manifest.json` P2 entries;
- the exact decoded MATLAB type produced by `jsondecode` for the P2 container and its elements under R2022b;
- the frozen `p2_matlab.m` access logic.

The known failing statement is:

`cse=m.p2(k); rows(k).id=cse.id; rows(k).kind=cse.kind;`

The purpose of diagnosis is only to determine the correct **container access syntax** for the already-frozen P2 data. Do not change any P2 case values, IDs, kinds, derivative inputs, economic formula, expected classification, tolerance, or case ordering.

Return one blocker diagnosis:

- `P2_JSON_CONTAINER_CELL_ACCESS_REQUIRED`
- `P2_JSON_CONTAINER_STRUCT_ARRAY_ACCESS_REQUIRED`
- `P2_JSON_CONTAINER_OTHER_ACCESS_FIX_REQUIRED`
- `P2_BLOCK_DIAGNOSIS_INCONCLUSIVE`

If inconclusive, stop without scientific P2 execution.

## Authorized pre-scientific decoder/access preflight

A minimal MATLAB preflight is authorized before the corrected P2 scientific call. It may:

- read the exact frozen `manifest.json`;
- run `jsondecode`;
- report `class`, `size`, and safe field/cell access for the P2 container;
- retrieve only metadata fields such as case `id` and `kind`;
- verify all frozen P2 case IDs/order are accessible.

It must **not** evaluate consumption, labor, transfer, cost, drifts, utility, Hamiltonians, KKT, boundary conditions, or any scientific P2 formula.

This preflight does not count as the one P2 scientific execution.

If preflight fails, stop. Do not iterate through multiple corrective variants in the same gate.

## Corrected P2 MATLAB harness authority

After diagnosis/preflight, create exactly one corrected MATLAB harness in the new artifact root:

`p2_matlab_corrected.m`

The correction may change **only** serialization/container decoding/access and output-container mechanics strictly necessary to consume the frozen P2 case manifest under MATLAB R2022b.

It must not change:

- any frozen P2 scientific input;
- formulas;
- source/helper calls;
- derivative values;
- cases or case order;
- MATLAB/Python symbol adapters;
- tolerances;
- expected legacy/redesign classification;
- scientific comparison semantics.

Before scientific execution:

- record complete textual diff between frozen `p2_matlab.m` and `p2_matlab_corrected.m`;
- prove every changed line is harness plumbing only;
- record SHA-256 and bytes of the corrected harness;
- run MATLAB `checkcode` or equivalent non-scientific syntax/static check;
- freeze the corrected harness; after this freeze it may not change.

If a second harness defect appears after the corrected scientific invocation starts, stop. Do not edit and rerun.

## Frozen P2 scientific authority

Reuse exactly the predecessor task's P2 case manifest and tolerances.

The ten required classes remain:

1. interior forward/forward comparable branch;
2. interior backward/backward comparable branch;
3. liquid zero-drift comparable case;
4. lower-`a` active state;
5. lower-`b` active state;
6. interior `mu_a=0` crossing candidate;
7. upper-`a` / lower-`b` corner;
8. upper-`a` / interior-`b` zero-liquid-drift corner;
9. dual-upper corner;
10. qualified lower-`b` F/Z near-tie representation case.

Reuse frozen tolerances from the predecessor report/task:

- `tau_fp(x,y)=128*eps64*max(1,abs(x),abs(y))` for materially comparable same-object scalar formulas;
- array analogue likewise;
- zero/drift threshold `1e-12`;
- KKT validity `1e-7`.

No tolerance change is authorized.

## Exactly-one corrected P2 execution

After all identity, diagnosis, preflight, static, and freeze gates pass:

1. invoke `p2_matlab_corrected.m` exactly once for scientific P2 evaluation;
2. if and only if MATLAB produces the complete expected P2 output for all frozen cases, invoke the byte-identical predecessor `p2_python.py` exactly once;
3. if and only if both outputs are complete, invoke the byte-identical predecessor `compare_p2.py` exactly once.

Do not run P1.
Do not run P3.
Do not run P4.

## Required P2 evidence

For every frozen case report:

- case ID and class;
- state and derivative inputs;
- MATLAB-exposed directional/candidate objects;
- Python raw/canonical candidate objects;
- consumption;
- scalar labor;
- transfer;
- adjustment cost;
- `mu_a`, `mu_b`;
- flow utility;
- Hamiltonian where materially comparable;
- direction/admissibility classification;
- boundary feasibility;
- KKT validity/evidence;
- numerical differences and frozen bounds for every comparable quantity;
- whether the case is `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`, `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`, or `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION`.

For Python-only accepted redesign cases, do not falsely require nonexistent MATLAB candidate identity. Demonstrate MATLAB omission/legacy behavior and validate Python against the already accepted analytic drift/KKT/boundary contract.

## P2 terminal classifications

If all P2 cases satisfy the frozen contract:

`MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS`

If a materially comparable P2 scientific object fails:

`MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_FAIL_CLOSED`

If the corrected harness/runtime still blocks before complete scientific P2 evidence:

`MATLAB_PYTHON_TWO_ASSET_HA_P2_CORRECTION_BLOCKED_ENVIRONMENT_OR_HARNESS`

Do not convert scientific mismatch into a harness blocker.

## P1 reuse classification

The report must explicitly return one:

- `P1_EVIDENCE_REUSED_AND_REMAINS_ACCEPTED`
- `P1_REUSE_BLOCKED_IDENTITY_DRIFT`

Under a successful identity gate, P1 remains accepted and must not be rerun.

## Report authorization

Write exactly one new repository report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_HARNESS_BLOCK_CORRECTION_AND_REEXECUTION_REPORT.md`

Include:

- live GitHub/source identity;
- predecessor report/commit identity;
- predecessor artifact fingerprint verification;
- P1 reuse decision;
- blocker diagnosis;
- decoder/access preflight result;
- frozen vs corrected P2 MATLAB harness diff and identities;
- exact execution counts;
- complete P2 case evidence if reached;
- P2 classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the new report may be added to the repository.

Whether PASS, FAIL_CLOSED, or BLOCKED, if it is the sole repository change:

- stage only the report;
- create one commit;
- fresh-fetch remote;
- fast-forward push only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Correct P2 parity harness block and record evidence`

## Forbidden operations

Do not:

- rerun P1;
- modify predecessor raw evidence;
- modify MATLAB source/helpers;
- modify Python production source/tests;
- modify byte-frozen `p2_python.py` or `compare_p2.py`;
- change P2 case values/order/semantics;
- change tolerances;
- execute P3/P4;
- issue P5 Owner parity acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results;
- edit and rerun the corrected P2 scientific harness after its first scientific invocation;
- merge, rebase, reset, or force-push.

## Acceptance meaning

A P2 PASS means only that P1 remains accepted and P2 numerical evidence is complete and accepted for independent review. It does not establish P3/P4 or final HA parity.

## Recommended next gate

If P2 PASS and independently accepted:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY`

That future gate may reuse P1/P2 accepted evidence and execute only P3 then P4 under the already frozen shared-grid/common-generator contract. P5 and dynamic extension remain blocked until P3/P4 pass and Owner explicitly accepts the complete P1–P4 evidence.
