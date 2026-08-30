# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_MATERIAL_MISMATCH_ROOT_CAUSE_DECOMPOSITION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / diagnostic auditor

Owner: final scientific authority

## 1. Purpose

Diagnose the exact root causes of the 11 persisted mismatches from the completed MATLAB-faithful full-HJB comparison **without rerunning MATLAB, Python HJB, or the comparator and without modifying scientific production source**.

The immediate predecessor established that:

- corrected source-extracted MATLAB HJB converged in 12 iterations;
- faithful Python HJB converged in 12 iterations;
- `V`, consumption, adjustment cost, effective illiquid return, labels, ordering, initialization, and `Bswitch` passed;
- the persisted comparator nevertheless returned `MATERIAL_MISMATCH` for five continuous arrays and six sparse-operator objects;
- the unaccepted faithful source candidate was restored and only the two reports were published.

This task must determine whether each mismatch is caused by:

1. a real MATLAB-faithful implementation gap;
2. floating-point propagation from the sparse HJB solve under otherwise identical formulas;
3. sparse-storage representation only (for example explicit stored zeros versus MATLAB sparse omission);
4. comparator-contract misclassification of mathematically identical objects;
5. or a mixture of the above.

Do not fix anything in this task. Produce a source-backed recovery design only.

## 2. Controlling live authority

Task-authoring parent observed before publication:

`c79001c032e880d6371e90f44c66483f04ced0bb`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is on live `main`;
3. read `AGENTS.md`;
4. read `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
5. read `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
6. read both immediate reports:
   - `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_REPORT.md`
   - `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
7. verify live start SHA and clean worktree.

Primary scientific authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

KFE is not authorized.

## 3. Frozen scientific objects — reuse only

Do not regenerate any of the following.

### MATLAB

Corrected source-extracted evaluator:

`F6D33348329D242AC3C7D867D455DDD0B87184C00A5AD66332A1B62F359599FE`

Persisted MATLAB HJB output:

`52CE922D7960AB77D87A226747B0B79A29AFAD0C6B9759C7A81AD937CB7E73BF`

Known facts:

- 50 states;
- converged `true`;
- 12 iterations;
- statistic `9.076792650830612e-10`.

### Python

Persisted faithful Python HJB output:

`A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`

Known facts:

- converged `true`;
- 12 iterations;
- statistic `9.07700581365134e-10`.

The unaccepted candidate source hashes captured before restoration were:

- `matlab_faithful_policy.py` `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- `matlab_faithful_hjb.py` `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`;
- `matlab_faithful_operator.py` `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`.

Recover them read-only only from the preserved predecessor dirty-worktree capture / artifact patch. Do not restore them into repository production paths in this task.

### Comparator result

Persisted comparison:

`F04B66152ED02E993020B76F01C65CD9BE6E8D2793159F037FEAA64EFE648836`

Corrected serializer-only comparator:

`615D4FC8C17D3909A8F733555C160C2EC344EFD6C1C7B243F9D2FDB5E5611CAD`

Frozen tolerances remain evidence, not modifiable authority:

- direct scalar/operator: `128*eps64*max(1,abs(x),abs(y))`;
- converged `V`: absolute `1e-7`.

## 4. Scientific execution budget

Exactly zero scientific/model reruns:

- MATLAB HJB: `0`;
- Python HJB: `0`;
- comparator: `0`;
- KFE: `0`;
- steady state: `0`.

Read-only diagnostic scripts over persisted JSON/NPZ/matrix artifacts are allowed.

Do not call any household/HJB solver from those scripts.

Create diagnostic scripts/artifacts only under a fresh no-overwrite ProjectTemp artifact root. Do not add diagnostic scripts to repository source/tests.

## 5. Mandatory mismatch decomposition

The persisted mismatch list contains exactly:

Continuous arrays:

1. `labor`;
2. `transfer`;
3. `mu_a`;
4. `mu_b`;
5. `utility`.

Sparse objects:

6. iteration `BB`;
7. iteration `AAH`;
8. iteration full `A`;
9. post-convergence `BB`;
10. post-convergence `AAH`;
11. post-convergence full `A`.

For every object, report whether the mismatch is primary or downstream.

## 6. Continuous-array root-cause audit

For each of the five continuous arrays:

- enumerate every index exceeding the frozen direct bound, not only the worst index;
- report MATLAB value, Python value, absolute difference, relative difference, frozen local bound, and ULP distance where meaningful;
- map each index to physical `(b,a,z)` and branch labels;
- identify whether the same state also has a `V` discrepancy and report the local `V`, forward/backward derivative discrepancies, and derivative-floor status;
- reconstruct the immediate formula from designated MATLAB source and the preserved Python candidate source;
- determine the earliest intermediate quantity that differs.

At minimum inspect the dependency chain:

`V -> VbF/VbB/VahF/VahB -> derivative floor -> C/l -> sc -> Ic -> four bare-a FOCs -> d_B/d_F -> sdh -> Idh -> selected d -> cost -> mu_a/mu_b -> utility`.

Categorical labels were exact in the persisted comparison. Confirm whether every continuous mismatch occurs with identical `Ic/Idh` branch selection.

### 6.1 Floating-propagation test

Perform a read-only counterfactual arithmetic audit, not a solver rerun:

- evaluate the Python/MATLAB formulas at the **same persisted derivative/input scalars** where possible;
- separately evaluate each language formula using its own persisted derivative scalars;
- distinguish formula/arithmetic-order difference from upstream `V`/derivative propagation.

Do not modify the frozen tolerance.

Classify each continuous mismatch exactly as one of:

- `PRIMARY_FORMULA_OR_ARITHMETIC_IMPLEMENTATION_GAP`;
- `DOWNSTREAM_FROM_SPARSE_SOLVER_VALUE_DIFFERENCE`;
- `MIXED_PRIMARY_AND_PROPAGATED`;
- `UNRESOLVED`.

## 7. Sparse-pattern audit — exact coordinates and stored values

For iteration `BB`, iteration `AAH`, and post `AAH`, the persisted comparison showed pattern-count differences:

- iteration `BB`: MATLAB/Python `96/97`;
- iteration `AAH`: `110/120`;
- post `AAH`: `80/90`.

For every pattern difference:

- enumerate the exact `(row,col)` coordinate;
- map to state and neighbor;
- report whether the entry is:
  - absent;
  - explicitly stored `0.0`;
  - signed zero;
  - subnormal/tiny nonzero;
  - or materially nonzero;
- report the corresponding source coefficient before sparse insertion;
- identify whether MATLAB `sparse/spdiags` drops that value while SciPy retains it;
- determine whether calling an **analysis-only** `eliminate_zeros()` on a copy makes patterns identical;
- determine whether dropping values that are exactly numerical zero (and only exact zero) makes patterns identical.

Do not use any threshold-based zero dropping in this diagnostic.

If a pattern difference is due to a nonzero value, report its magnitude and source term explicitly.

### 7.1 Full-operator cancellation/composition audit

The persisted full patterns were exact:

- iteration `A`: `217/217` exact pattern;
- post `A`: `179/179` exact pattern.

Explain exactly how component-pattern differences coexist with exact full-`A` patterns.

For every component-only discrepant coordinate, inspect `BB + AAH + Bswitch` contributions on both languages and determine whether:

- explicit-zero storage disappears on sum;
- two components occupy the same coordinate;
- cancellation or duplicate sparse summation changes storage;
- or another source-backed mechanism is responsible.

## 8. Sparse-value audit

For iteration `A`, post `BB`, and post `A`, patterns were exact but values exceeded the frozen direct bound.

Reported maxima:

- iteration `A`: `5.098144129078719e-13`;
- post `BB`: `4.773959005888173e-13`;
- post `A`: `4.773959005888173e-13`.

Also inspect values at common coordinates for component matrices even when their raw stored patterns differ.

For each operator:

- enumerate all coordinates exceeding frozen bound;
- report MATLAB/Python values, differences, local bound, ULP distance;
- map each coefficient to the exact drift/control quantity from which it is constructed;
- determine whether the operator discrepancy is entirely downstream from `labor/transfer/mu_a/mu_b` discrepancies or whether there is an independent assembly difference.

Classify each sparse mismatch as:

- `EXPLICIT_ZERO_STORAGE_REPRESENTATION_ONLY`;
- `DOWNSTREAM_FLOATING_PROPAGATION_FROM_POLICY_VALUES`;
- `PRIMARY_SPARSE_ASSEMBLY_IMPLEMENTATION_GAP`;
- `MIXED`;
- `UNRESOLVED`.

## 9. Comparator-contract audit

Do not change the comparator in this task.

Determine whether its frozen rules conflate any of the following:

- mathematical sparsity pattern versus raw stored sparse entries;
- solver-derived quantities versus direct primitive arithmetic;
- exact-zero storage representation versus scientific nonzero structure.

For each such issue, classify:

- `COMPARATOR_CONTRACT_CORRECT`;
- `COMPARATOR_CONTRACT_TOO_STRICT_FOR_REPRESENTATION_ONLY`;
- `COMPARATOR_CONTRACT_TOO_STRICT_FOR_SOLVER_PROPAGATED_QUANTITY`;
- `COMPARATOR_CONTRACT_REQUIRES_OWNER_DECISION`.

Do not recommend a looser tolerance merely because the current result failed. Any future tolerance proposal must be analytically justified from source arithmetic/solver propagation and must be a separate Owner/reviewer decision.

## 10. Required root-cause decision table

Produce one table with all 11 mismatch objects and columns:

- mismatch object;
- persisted maximum difference / pattern count;
- primary or downstream;
- exact root cause;
- source evidence;
- Python-candidate evidence;
- comparator role;
- recommended recovery type;
- whether scientific source mutation is required;
- whether comparator-only normalization is sufficient;
- whether a new HJB rerun would be required after the eventual correction.

## 11. Recovery-route design

At the end, choose exactly one overall route classification:

### A. Implementation gap dominates

`FAITHFUL_HJB_MISMATCH_DIAGNOSIS_IMPLEMENTATION_CORRECTION_REQUIRED`

Use if any material/source-backed Python formula or sparse assembly differs from MATLAB.

### B. Representation/solver arithmetic only

`FAITHFUL_HJB_MISMATCH_DIAGNOSIS_REPRESENTATION_AND_FLOATING_PROPAGATION_ONLY`

Use only if no source formula/branch/assembly gap exists and all mismatches are either exact-zero sparse storage representation or bounded floating propagation from otherwise source-identical sparse solves.

### C. Mixed

`FAITHFUL_HJB_MISMATCH_DIAGNOSIS_MIXED_IMPLEMENTATION_AND_REPRESENTATION`

Use if both categories exist.

### D. Blocked

`FAITHFUL_HJB_MISMATCH_DIAGNOSIS_BLOCKED`

Use if persisted artifacts are missing/corrupt or the root cause cannot be resolved without a scientific rerun or Owner provenance.

Then propose the smallest next task only. Do not execute it.

Examples of possible next-task types, depending on evidence:

- exact Python arithmetic/order correction;
- exact sparse zero-storage canonicalization in faithful production;
- comparator mathematical-sparsity normalization;
- pre-authorized solver-propagation tolerance redesign;
- or a bounded combination.

Do not authorize KFE.

## 12. Explicit prohibitions

Do not:

- rerun MATLAB HJB;
- rerun Python HJB;
- rerun comparator;
- modify designated MATLAB source;
- modify production Python source/tests;
- restore the rejected candidate into live repository paths;
- change tolerance;
- change comparator;
- run KFE/stationary distribution/steady state;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension or Results;
- claim full-HJB parity.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_MATERIAL_MISMATCH_ROOT_CAUSE_DECOMPOSITION_REPORT.md`

The report must include:

1. terminal diagnosis classification;
2. live start/final `origin/main`;
3. all frozen artifact identities;
4. zero scientific-call ledger;
5. all continuous mismatch coordinates and dependency tracing;
6. ULP and same-input arithmetic audit;
7. all sparse pattern discrepant coordinates and exact stored values;
8. explicit-zero analysis;
9. component-to-full-operator composition analysis;
10. all sparse value mismatch coordinates/root causes;
11. comparator-contract audit;
12. complete 11-object root-cause decision table;
13. complete unresolved list;
14. exact recommended next recovery gate;
15. changed-path list;
16. git status;
17. acceptance level.

## 14. Repository closeout

Repository mutation is report-only.

No scientific source/test path may be committed.

Stage only the required report, commit once, non-force push once, read back from GitHub, require `HEAD == origin/main`, and require clean worktree.

## 15. Terminal classification

Return exactly one of:

- `FAITHFUL_HJB_MISMATCH_DIAGNOSIS_IMPLEMENTATION_CORRECTION_REQUIRED`
- `FAITHFUL_HJB_MISMATCH_DIAGNOSIS_REPRESENTATION_AND_FLOATING_PROPAGATION_ONLY`
- `FAITHFUL_HJB_MISMATCH_DIAGNOSIS_MIXED_IMPLEMENTATION_AND_REPRESENTATION`
- `FAITHFUL_HJB_MISMATCH_DIAGNOSIS_BLOCKED`
