# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Close the MATLAB-faithful full-HJB parity gate after the accepted root-cause diagnosis proved that the prior 11 mismatches contain **no formula, branch, ordering, nonzero sparse-placement, or scientific-assembly implementation gap**.

This task must:

1. restore the previously rejected faithful HJB candidate **byte-identically** from preserved artifacts;
2. redesign the HJB comparator contract so that it distinguishes:
   - direct/source-local arithmetic parity;
   - independently solved HJB fixed-point propagation;
   - mathematical sparse support versus explicit stored exact zeros;
3. perform one fresh, pre-frozen MATLAB/Python HJB acceptance pair and one comparator;
4. accept the faithful full-HJB production route only if every redesigned, pre-authorized gate passes.

This is not authority to loosen tolerances after observing a failed result. The acceptance logic is frozen here before execution.

This task stops before KFE, stationary distribution, steady-state aggregates, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

## 2. Controlling accepted evidence

Read and obey:

- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSeOUT_REPORT.md` if that exact path exists; otherwise read the live path with `CLOSEOUT` spelling
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_MATERIAL_MISMATCH_ROOT_CAUSE_DECOMPOSITION_REPORT.md`

Accepted predecessor diagnosis:

`FAITHFUL_HJB_MISMATCH_DIAGNOSIS_REPRESENTATION_AND_FLOATING_PROPAGATION_ONLY`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`27c30d7a761203b0abb8a5ef9b36e740b7098080`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. verify it is a direct child of the predecessor diagnosis commit;
4. verify all controlling reports exist;
5. verify clean worktree;
6. verify designated MATLAB hashes;
7. verify accepted faithful primitive/local-policy sources have not drifted.

Do not begin from uncommitted scientific source changes.

## 4. Frozen scientific diagnosis and authority decision

The predecessor diagnosis established:

- 21 sparse-pattern differences were all Python-stored exact signed `-0.0` values;
- dropping **exact numerical zero only** makes the mathematical sparse supports identical;
- no tiny/material nonzero support mismatch exists;
- all 36 continuous failures and all 342 common-coordinate sparse-value failures are downstream of independent sparse HJB solves;
- same-input formula/arithmetic-order differences are at most `4.440892098500626e-16` and do not independently exceed the direct machine bound;
- branch labels are exact and no derivative-floor regime differs;
- no source formula, branch, index, boundary-placement, or nonzero sparse-assembly gap exists.

Freeze the following acceptance authorities:

`MATLAB_FAITHFUL_HJB_MATHEMATICAL_SPARSE_SUPPORT_IGNORES_EXACT_STORED_ZEROS`

`MATLAB_FAITHFUL_HJB_PARITY_SEPARATES_FIXED_POINT_SOLVER_PROPAGATION_FROM_SAME_INPUT_FORMULA_PARITY`

Interpretation:

### 4.1 Sparse support

For parity purposes, mathematical sparse support is the set of coordinates whose stored numerical value is **not exactly zero**.

Before comparing sparse patterns, comparator copies may canonicalize by removing only values satisfying exact binary64 `value == 0.0`.

Allowed:

- remove `0.0`;
- remove `-0.0`.

Forbidden:

- threshold-based dropping;
- `isclose` zeroing;
- epsilon clipping;
- magnitude-based pruning.

Raw stored NNZ counts must still be reported diagnostically.

### 4.2 Direct/source-local arithmetic

Objects evaluated from the same exact input scalars and source formula remain subject to the strict machine-scaled rule:

`128*eps64*max(1,abs(x),abs(y))`.

This includes same-input replay of:

- consumption/labor formulas;
- bare-`a` transfer FOCs;
- adjustment cost;
- effective illiquid return;
- drift formulas;
- utility;
- source `BB/AAH` coefficient formulas;
- post-convergence coefficient formulas;
- sparse placement values after identical source inputs are supplied.

No broad tolerance increase is authorized for these same-input checks.

### 4.3 Independently solved HJB fixed-point objects

Cross-language raw differences in solver-derived downstream policy/drift/operator values must **not** be tested as if they were same-input primitive arithmetic.

For a solver-derived field/operator to pass, all of the following must hold:

1. both HJBs converge under the unchanged source convergence contract;
2. iteration count is identical;
3. converged `V` satisfies the already frozen absolute `1e-7` bound;
4. all categorical branch/indicator labels are exact;
5. derivative-floor activation pattern is exact;
6. same-input source-formula replay at every compared state/coefficient satisfies the direct `128*eps64*max(...)` bound;
7. every raw cross-language difference is traced to the independently solved `V/derivative` discrepancy with no unexplained residual;
8. mathematical sparse support, after exact-zero-only canonicalization, is exact;
9. no source formula/assembly/indexing discrepancy is detected.

When all nine conditions hold, the raw cross-language downstream difference is reported as `SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE` and is **not itself a parity failure**.

This is not tolerance loosening. It is a separation of a fixed-point solver output from a same-input formula-equivalence test.

If any same-input replay exceeds the direct bound, or any unexplained residual remains, parity fails.

### 4.4 Objects that retain direct gates

The following remain direct/exact gates as previously frozen:

- grid/state count;
- state ordering;
- initialization identity;
- convergence boolean;
- iteration count;
- liquid labels;
- transfer labels;
- derivative-floor activation pattern;
- `Bswitch` pattern and values;
- direct primitive helpers;
- source coefficient replay;
- mathematical sparse support after exact-zero-only canonicalization.

## 5. Designated MATLAB source identity

Designated root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required hashes:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Stop BLOCKED if any differs.

## 6. Faithful Python candidate restoration — byte identity only

The previously rejected candidate was preserved before restoration with hashes:

- `matlab_faithful_policy.py` `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`
- `matlab_faithful_hjb.py` `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`
- `matlab_faithful_operator.py` `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`

Preserved patch:

`7EEE8E46B70FAC23C68725B548B6E7FDC957F4ED6B26DD7A50CCD73EA9E62677`

Restore these sources only from the preserved predecessor artifact/patch.

Required condition:

- restored source bytes must reproduce all three exact hashes above.

No scientific source edit beyond byte-identical restoration is authorized.

Do not modify/repurpose:

- corrected/reference `policies.py`;
- corrected/reference `hjb.py`;
- corrected/reference `generator.py`;
- KFE/steady-state modules.

If exact candidate restoration cannot be achieved, stop BLOCKED.

## 7. Comparator redesign

Create a new successor comparator artifact; do not overwrite predecessor comparator artifacts.

The comparator must implement the frozen authorities in Section 4 and nothing broader.

Required changes relative to the prior corrected comparator:

1. exact-zero-only sparse canonicalization on copies before mathematical support comparison;
2. raw NNZ retained as diagnostics, not support gate;
3. same-input replay gates for solver-derived continuous fields;
4. same-input replay gates for solver-derived sparse coefficients;
5. explicit result classes:
   - `DIRECT_PARITY_PASS`;
   - `SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE`;
   - `REPRESENTATION_ONLY_EXACT_ZERO_DIFFERENCE`;
   - `MATERIAL_MISMATCH`;
6. persisted decomposition showing that each solver-propagated raw difference has no unexplained same-input residual.

The comparator must not:

- change source formulas;
- change the `1e-7` converged-V gate;
- change the direct `128*eps64*max(...)` rule;
- add a new broad raw policy/operator tolerance;
- prune nonzero sparse values;
- suppress categorical mismatches;
- suppress mathematical sparse-support mismatches.

The prior NumPy-scalar JSON normalization may be retained unchanged.

## 8. Engineering-only comparator preflight

Before any scientific HJB rerun, use frozen persisted predecessor outputs only.

Run exactly one no-science comparator-contract preflight over:

- MATLAB output `52CE922D7960AB77D87A226747B0B79A29AFAD0C6B9759C7A81AD937CB7E73BF`;
- Python output `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.

This preflight is not final acceptance evidence.

It must prove:

- all 21 raw pattern differences classify representation-only and disappear under exact-zero-only canonicalization;
- no nonzero support difference is hidden;
- same-input replay for all previously failed continuous objects passes the direct machine bound;
- same-input replay for all previously failed common sparse coefficients passes the direct machine bound;
- the comparator still deliberately fails a synthetic material formula mismatch;
- the comparator still deliberately fails a synthetic nonzero sparse-support mismatch;
- the comparator still deliberately fails a categorical mismatch;
- unsupported serialization objects fail closed.

If any preflight condition fails, stop BLOCKED before HJB rerun.

## 9. Freeze final acceptance fixture and artifacts

Use exactly the prior source-valid fixture:

- `5 b × 5 a × 2 z = 50` states;
- same parameter/grid manifest `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A`;
- same ordering adapter `52EB994358F07767AD8859D737C3D7A89BC7FB04DC063754027CA80386F2926D`;
- same initialization contract/artifact `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`;
- same `Delta=1000`;
- same `crit=1e-7`;
- same `maxit=100`;
- same economic parameters;
- same corrected source-extracted MATLAB boundary/spdiags semantics.

Before scientific execution freeze/hash/read back in a fresh no-overwrite artifact root:

- restored faithful Python sources;
- corrected MATLAB evaluator;
- final comparator;
- comparator diff and contract audit;
- parameter/grid manifest;
- ordering;
- initialization;
- acceptance contract;
- execution ledger.

No post-output edits are allowed.

## 10. Final scientific call budget

After freeze/preflight PASS:

- MATLAB HJB: at most `1`;
- Python faithful HJB: at most `1`;
- final comparator: at most `1`.

Use exactly the frozen fixture.

If either HJB fails, do not repair or rerun in this task.

If comparator fails for any source/environment reason, do not repair or rerun in this task.

## 11. Final comparator acceptance requirements

PASS requires all of the following:

- both HJBs converge;
- iteration count exact;
- `V` within absolute `1e-7`;
- grid/order/initialization exact;
- liquid/transfer labels exact;
- derivative-floor activation exact;
- bare-a FOC/taper/cost direct same-input checks pass;
- same-input replay for labor/transfer/mu_a/mu_b/utility passes direct machine bound everywhere;
- Bswitch exact;
- iteration/post-convergence mathematical sparse supports exact after exact-zero-only canonicalization;
- source coefficient same-input replay for iteration/post operators passes direct machine bound everywhere;
- every remaining raw cross-language downstream difference is classified only as solver-propagated diagnostic difference with zero unresolved scientific residual;
- complete material mismatch list is empty.

Raw stored NNZ differences caused solely by `0.0/-0.0` are not material mismatches, but must remain reported.

## 12. Repository acceptance and closeout

If PASS:

Accept and publish the restored faithful source route:

- `src/ch5_two_asset_hank/matlab_faithful_policy.py`
- `src/ch5_two_asset_hank/matlab_faithful_operator.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`

Freeze:

`MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`

`MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`

and recognize the earlier local/primitive faithful chain as integrated into the accepted HJB route.

If MATERIAL_MISMATCH or BLOCKED:

- preserve candidate patch/hashes;
- restore unaccepted faithful source paths to task-authority state;
- publish report only;
- do not authorize KFE.

In all cases:

- explicit-path staging only;
- one commit;
- one non-force push;
- GitHub read-back;
- `HEAD == origin/main`;
- clean worktree.

## 13. Explicit prohibitions

Do not:

- modify designated MATLAB source;
- alter economics, grid, initialization, ordering, Delta, crit, or maxit;
- alter faithful scientific formulas or branch rules;
- introduce any new raw downstream tolerance;
- use threshold-based sparse zero pruning;
- run KFE;
- run stationary distribution;
- run steady-state aggregates;
- run D1-D3;
- run asset-tail;
- run transition/IRF/dynamics;
- run calibration extension;
- run Results.

## 14. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_REPORT.md`

Include at minimum:

1. terminal classification;
2. live GitHub continuity;
3. designated source hashes;
4. exact restored source hashes;
5. comparator-contract implementation/diff/hash;
6. no-science preflight results;
7. frozen final artifact identities;
8. MATLAB/Python scientific call ledger;
9. convergence/iterations/statistics;
10. V comparison;
11. categorical/direct parity results;
12. exact-zero sparse representation summary;
13. same-input continuous replay results;
14. same-input sparse-coefficient replay results;
15. raw solver-propagated diagnostic differences;
16. mathematical support comparison;
17. complete material mismatch list;
18. complete unresolved list;
19. changed-path list;
20. git status;
21. acceptance level;
22. exact next gate recommendation.

## 15. Terminal classifications

Return exactly one:

### PASS

`MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_PASS`

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_MATERIAL_MISMATCH`

### BLOCKED

`MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_AND_FINAL_ACCEPTANCE_RERUN_BLOCKED`

If and only if PASS, recommend only:

**MATLAB-faithful stationary KFE contaminated-row implementation and same post-convergence operator density parity.**

Do not authorize full steady-state aggregates or dynamics from this task alone.
