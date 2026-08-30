# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the immediately preceding MATLAB-faithful full-HJB parity task from its exact preserved dirty worktree and persisted MATLAB/Python scientific outputs, correct only the comparator's `numpy.int64` JSON-serialization boundary, execute exactly one replacement comparator, and close out the repository without rerunning either HJB.

This task exists because the predecessor replacement MATLAB and replacement Python HJBs both converged under the same frozen 50-state fixture in 12 iterations, but the one consumed comparator call failed while persisting `comparison.json` because a NumPy integer scalar was not JSON serializable.

This task must not infer parity from the failed persistence. PASS requires one valid persisted comparator result under unchanged scientific comparison rules.

This task stops before KFE, stationary distribution, steady-state aggregates, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

## 2. Live authority and predecessor state

Task-authoring parent observed before publication:

`1285abfac4548743f8b7f15a7e59923118c32120`

The predecessor task is:

`tasks/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY.md`

The predecessor report currently exists only in the preserved execution worktree and is not yet on live GitHub main:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_REPORT.md`

At successor execution start, the expected existing worktree is:

`D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`

It is expected to contain exactly four predecessor-task dirty paths and to have no predecessor commit/push after the failed comparator.

## 3. Special dirty-worktree continuation authority

This task explicitly authorizes controlled continuation from that exact preserved predecessor dirty worktree. Do not discard, reset, clean, checkout-away, or overwrite those changes before capturing them.

Before `git fetch`, record and persist to a fresh no-overwrite artifact root:

- current `HEAD`;
- `git status --short`;
- `git diff --name-status`;
- full `git diff` patch;
- SHA-256 of every dirty file;
- SHA-256 of the uncommitted predecessor report;
- exact path list.

Freeze marker:

`PREDECESSOR_DIRTY_WORKTREE_CAPTURED_BEFORE_SUCCESSOR_AUTHORITY_SYNC`

Required precondition:

- local `HEAD` must be the predecessor authority commit `1285abfac4548743f8b7f15a7e59923118c32120`;
- the dirty-path set must be exactly the predecessor-authorized faithful-route implementation/report paths described by the local predecessor report and execution ledger;
- there must be no unrelated path.

If the dirty set differs, stop BLOCKED and do not mutate it.

Then `git fetch origin` and verify live `origin/main` contains this exact successor task as the direct child of `1285ab...`.

Because the successor GitHub commit adds only this task file, attempt a safe `git merge --ff-only origin/main` while preserving the captured dirty files. If Git refuses because the dirty state would be overwritten, stop BLOCKED. Do not stash/reset/force-clean as a workaround.

## 4. Required reads and frozen scientific evidence

Read:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
- all controlling faithful-route reports named by the predecessor task;
- the uncommitted predecessor BLOCKED report;
- predecessor artifact manifests and execution ledgers;
- predecessor comparator source and traceback/log.

Extract from the preserved predecessor report/artifacts and record exact hashes for:

- corrected replacement MATLAB HJB output;
- replacement Python faithful HJB output;
- corrected MATLAB evaluator;
- Python faithful candidate sources;
- comparator;
- parameter/grid manifest;
- ordering adapter;
- initialization artifact;
- tolerance artifact;
- execution ledger.

The predecessor scientific facts are reuse-only:

- replacement MATLAB HJB call already consumed `1/1` and converged in 12 iterations;
- replacement Python HJB call already consumed `1/1` and converged in 12 iterations;
- predecessor comparator call already consumed `1/1` but failed during JSON persistence;
- no scientific HJB rerun is authorized here.

## 5. Mandatory comparator-failure audit before correction

Before changing the comparator, prove from the frozen comparator source and traceback that the predecessor failure is confined to output serialization.

At minimum establish:

1. the exact exception type and object type (`numpy.int64` or equivalent exact NumPy integer scalar);
2. the exact line/call where JSON persistence failed;
3. whether all numerical/categorical/sparsity comparison logic had already executed before serialization;
4. whether the failure occurred before or after the terminal PASS/FAIL aggregation was computed in memory;
5. every NumPy scalar type that can reach the persisted comparison payload under the current comparator;
6. that no scientific input, field set, tolerance, ordering, sparsity rule, category rule, or PASS/FAIL logic needs to change.

Use classification:

`COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`

only if the failure is strictly a persistence-type incompatibility.

If any scientific comparison logic would need modification, stop BLOCKED and do not execute a replacement comparator.

Do not use the partially computed in-memory predecessor result as acceptance evidence.

## 6. Authorized comparator correction

Create a corrected comparator in a fresh successor artifact root. Do not overwrite the predecessor comparator.

The correction must be limited to converting NumPy scalar values at the JSON serialization boundary to their native Python scalar equivalents.

Preferred narrow behavior:

```python
if isinstance(obj, np.generic):
    return obj.item()
```

used only as a JSON `default=` serializer or an equivalently narrow persistence helper.

Do not automatically convert NumPy arrays unless the static audit proves the frozen comparison payload contains an array at the persistence boundary and that array handling was already part of the predecessor serializer contract. The known `numpy.int64` issue alone does not authorize broader coercion.

Do not change:

- comparator input files;
- comparison field lists;
- matrix sparse-pattern comparison;
- categorical mismatch logic;
- state/order comparison;
- tolerance logic;
- `128*eps64*max(1,abs(x),abs(y))` direct bound;
- absolute `1e-7` converged-`V` bound;
- PASS/FAIL aggregation;
- failure/mismatch semantics.

Every changed comparator line must be classified:

`COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`

## 7. No-science serializer preflight

Before replacement comparison, freeze/hash/read back:

- predecessor comparator;
- corrected comparator;
- exact comparator diff;
- serializer-only audit;
- persisted MATLAB and Python output identities;
- unchanged comparator inputs/tolerances;
- successor execution ledger.

Run exactly one no-science serializer preflight. It must prove:

- native `int`, `float`, `bool` persist unchanged;
- `np.int64` persists as the same integer value;
- other NumPy scalar types actually present in the frozen comparison payload, if any, persist with identical scalar value;
- unsupported non-scalar shapes still fail closed unless already supported by the predecessor comparator;
- serialization normalization does not change row/case/order counts, field names, numerical values, mismatch counts, or PASS/FAIL logic.

No MATLAB or Python model execution is allowed in the preflight.

If the preflight fails, stop BLOCKED. Do not repair and rerun a scientific comparator in the same task.

## 8. Replacement comparator budget

After the corrected comparator and successor artifacts are frozen:

- MATLAB HJB calls in this task: exactly `0`;
- Python HJB calls in this task: exactly `0`;
- replacement comparator: at most `1`.

Run the corrected comparator exactly once against the already persisted replacement MATLAB and Python HJB outputs from the predecessor task.

Do not regenerate either output.

If the comparator fails again because of another source/environment/persistence issue, stop BLOCKED. Do not perform a second correction/rerun.

If the comparator completes and reports any frozen numerical/categorical/order/sparsity mismatch, classify MATERIAL MISMATCH. Do not tune tolerance or scientific code.

## 9. PASS acceptance contract

PASS requires the one replacement comparator to persist a valid `comparison.json` and pass every predecessor-authorized object:

- state/grid count and ordering;
- initialization identity;
- convergence boolean;
- iteration count and convergence statistic;
- `V`;
- consumption;
- labor;
- transfer;
- adjustment cost;
- effective illiquid return;
- `mu_a`;
- `mu_b`;
- utility;
- liquid labels;
- transfer labels;
- iteration `BB`, `AAH`, `Bswitch`, full `A` patterns/values/diagonals/boundary rows/row sums;
- post-convergence pre-KFE `BB`, `AAH`, full `A` patterns/values/row sums/signs.

On PASS, freeze:

`MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_PASS`

and:

`MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`

This accepts the MATLAB-faithful HJB/operator layer only. It does not accept KFE, stationary distribution, steady-state aggregates, or dynamics.

## 10. Repository closeout

The predecessor task ended before commit/push. This task must close the repository deterministically.

### If replacement comparator PASS

- preserve the captured predecessor dirty patch in the artifact root;
- retain the predecessor BLOCKED report unchanged and record its SHA-256;
- retain only predecessor-authorized faithful production/test changes plus this successor's report in the repository;
- do not commit the external comparator artifact unless the predecessor task explicitly placed comparator code under repository authority;
- include the previously uncommitted predecessor report in the closeout so its BLOCKED provenance is not lost;
- write the successor report described below;
- stage only explicitly authorized paths;
- commit once;
- push once, non-force, to `main`;
- GitHub read-back all published scientific source/report paths;
- require `HEAD == origin/main` and clean worktree.

### If MATERIAL MISMATCH or BLOCKED

- first preserve hashes and full patches of all uncommitted faithful candidate changes in the successor artifact root;
- restore unaccepted scientific source/test paths to live task-authority state;
- keep the predecessor BLOCKED report unchanged;
- write the successor report;
- commit/push reports only, unless a source path was already independently accepted before this full-HJB task chain;
- require clean closeout.

Do not silently leave a dirty worktree again.

## 11. Required successor report

Write:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`

Include at minimum:

1. terminal classification;
2. live GitHub continuity;
3. predecessor dirty-worktree capture and hashes;
4. predecessor report hash and unchanged status;
5. exact MATLAB/Python output hashes and 12-iteration convergence facts;
6. comparator traceback/failure audit;
7. exact comparator diff and line classifications;
8. serializer preflight result/hash;
9. scientific call ledger (`MATLAB 0`, `Python 0`, comparator <=1 in this task);
10. replacement comparison output hash;
11. complete parity summary and maxima/worst cases;
12. sparse pattern/value mismatch counts;
13. categorical mismatch counts;
14. complete mismatch list;
15. complete source/environment failure list;
16. repository changed-path list;
17. final git status and GitHub read-back;
18. acceptance level;
19. exact next gate.

## 12. Terminal classifications

Return exactly one:

### PASS

`MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_PASS`

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_MATERIAL_MISMATCH`

### BLOCKED

`MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_BLOCKED`

## 13. Explicit prohibitions

Do not:

- rerun MATLAB HJB;
- rerun Python HJB;
- change any scientific source after the predecessor scientific outputs;
- change fixture, parameters, grids, initialization, ordering, Delta, crit, maxit;
- change comparator scientific fields/tolerances/PASS logic;
- modify designated MATLAB source;
- run KFE;
- run stationary distribution;
- run steady-state aggregates;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension or Results;
- use stash/reset/clean to bypass dirty-worktree continuity checks.

## 14. Next gate

If and only if PASS, recommend only:

**MATLAB-faithful stationary KFE contaminated-row implementation and same post-convergence operator density parity.**

Do not authorize full steady-state aggregate parity or dynamics from this task alone.
