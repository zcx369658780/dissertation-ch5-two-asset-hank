# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Integrate the already accepted MATLAB-faithful household primitives and local policy/upwind selector into a distinct **full HJB driver**, then perform one pre-frozen, same-input, converged MATLAB–Python HJB/operator parity experiment.

The scientific target is the designated working MATLAB implementation, not the corrected-equation/reference Python HJB.

The task must preserve the corrected/reference route unchanged while establishing a separate MATLAB-faithful route.

This task stops before stationary KFE, stationary distribution, aggregates, steady state, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

## 2. Controlling accepted authority

Read and obey:

- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`

Accepted predecessor terminal:

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_PASS`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted faithful primitives:

- `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`
- `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

Historical corrected-equation route remains reference-only:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

Historical P5 scope remains:

`P5_ACCEPTED_FOR_CORRECTED_EQUATION_TRACK_NOT_FINAL_MATLAB_FAITHFUL_PARITY`

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`73274e29d98dbe9a18d10aa172a87270315a0a16`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all four controlling reports exist on live `main`;
3. record live start SHA;
4. verify designated MATLAB hashes;
5. verify accepted faithful primitive/local-policy source identities;
6. verify corrected/reference `policies.py` and `hjb.py` have not been silently repurposed;
7. begin from a clean worktree.

## 4. Designated MATLAB authority

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Verify at minimum:

- `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m` SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m` SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Do not modify designated MATLAB source.

## 5. Mandatory full-HJB source audit before implementation

Before changing Python production code, map the complete designated HJB path from parameter/grid inputs through the last converged HJB value/operator **up to but excluding the stationary KFE solve**.

The map must include exact source locations/formulas for:

1. parameter extraction relevant to household HJB;
2. `b`, `a`, and productivity grid construction/shape/order;
3. borrowing-rate treatment (`rb`, `rb_gap`, state-dependent `Rb`);
4. `raah`/`Rah` taper;
5. productivity-state generator/switch object (`Bswitch`) including exact state ordering and intensities;
6. initialization path, including `tempMat`, `lab_solve2`, baseline labor, baseline consumption, and initial value;
7. forward/backward finite differences and boundary derivative substitutions;
8. derivative floor(s);
9. local `Ic`/`Idh` policy/upwind block already audited;
10. exact HJB asset operator assembly (`BB`, `AAH`) as used during iteration;
11. exact relationship, if any, between HJB operator rates and the final net drifts `s`/`mh`;
12. implicit update matrix, RHS, pseudo-time/Delta value, discounting, iteration limit, convergence statistic, and stop rule;
13. final post-convergence policy/operator reconstruction before KFE;
14. all reshape/flatten/index-order conventions.

### Critical operator audit

Do **not** assume the existing corrected/reference `generator.py` is the faithful HJB operator.

Explicitly determine from MATLAB whether:

- liquid `BB` rates are assembled from separate `Ic*sc` and `Idh*sdh` components rather than from the sign of the final net `mu_b` alone;
- illiquid `AAH` rates use derivative-side `MhB/MhF` objects rather than the sign of final net `mu_a` alone;
- both backward and forward contributions can coexist in a row before diagonal closure;
- the source-faithful local selector must expose additional component/rate fields for full HJB assembly.

If exact HJB `BB/AAH` cannot be represented by the current `MatlabFaithfulLocalPolicy` output, extend the faithful result/module only as required by the source. Do not force the existing net-drift generator to serve as an oracle.

### Productivity-process audit

The faithful route must reproduce the designated MATLAB productivity process used in `Bswitch`.

Do not reuse the corrected/reference reflected-diffusion `build_z_generator` unless static source inspection proves exact equivalence for the frozen parity fixture.

If MATLAB uses a finite-state switch process, implement that finite-state switch process in the faithful route.

### Initialization audit

The full HJB parity run must not bypass initialization by supplying an arbitrary Python initial value unless the MATLAB parity evaluator is frozen to the exact same supplied value through an explicitly source-preserving entry point.

Preferred route: faithfully reproduce the designated MATLAB initialization, including `lab_solve2`, so both implementations begin from the same source-defined value array.

If an exact same-value injection is materially safer and source-faithful, document and freeze it before execution; do not choose it after seeing results.

If any required full-HJB source object is ambiguous, return BLOCKED with the smallest exact ambiguity. Do not guess.

## 6. Architecture requirement

Preserve corrected/reference modules as historical diagnostics.

Preferred new modules:

- `src/ch5_two_asset_hank/matlab_faithful_operator.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`

Equivalent narrow names are allowed if consistent with repository style.

Do not silently convert `src/ch5_two_asset_hank/hjb.py` or `generator.py` into the faithful route.

The faithful HJB driver must call the accepted faithful policy/primitives and exact faithful operator objects.

No KKT/multiplier/candidate-Hamiltonian veto may be introduced into faithful policy selection unless the designated MATLAB HJB source contains an equivalent production veto.

## 7. Faithful HJB operator implementation requirements

Implement exact source-backed HJB operator construction.

At minimum:

- exact MATLAB `BB` liquid rates;
- exact MATLAB `AAH` illiquid rates;
- exact MATLAB productivity `Bswitch`;
- exact diagonal closure;
- exact logical state ordering, with an explicit MATLAB `(b,a,z)` ↔ Python faithful storage adapter if Python stores `(a,b,z)`;
- exact boundary rate overrides;
- exact grid-spacing divisions.

Required diagnostics before scientific execution:

- row sums at machine precision;
- nonnegative off-diagonal rates where MATLAB construction implies them;
- exact sparsity/index-neighbor orientation on synthetic micro-cases;
- equivalence of local operator rates to the already accepted local policy parity cases where applicable.

These diagnostics may identify implementation defects but must not redesign the MATLAB operator.

## 8. Faithful HJB driver implementation requirements

Implement the exact designated source iteration contract, including:

- source-defined initialization or pre-frozen exact same-value injection;
- derivative recomputation each iteration;
- faithful local policy/upwind selection over every grid cell;
- faithful `BB + AAH + Bswitch` operator;
- source-defined implicit linear system and RHS;
- source-defined pseudo-time step / `Delta`;
- source-defined convergence measure and threshold;
- source-defined maximum iteration count;
- final policy/operator reconstruction using the converged value.

Do not add corrected-route KKT/residual acceptance as a production veto if MATLAB does not use it.

You may compute additional residuals after convergence as diagnostics, but label them `DIAGNOSTIC_ONLY` and do not replace the MATLAB convergence criterion.

## 9. Same-input converged parity design

After implementation and all static/unit preflights pass, freeze **one** bounded same-input parity fixture before either scientific language run.

The fixture must be source-valid for the designated MATLAB HJB and large enough to exercise:

- lower/interior/upper liquid nodes;
- lower/interior/upper illiquid nodes;
- all designated productivity states;
- negative liquid asset/borrowing region if supported by the source-valid grid;
- the `raah` taper across at least lower/interior/upper `a` nodes.

Do not choose an ultra-degenerate fixture that disables the major HJB blocks merely to obtain a PASS.

Freeze and hash before execution:

- exact parameter manifest;
- exact grid manifest;
- exact MATLAB↔Python ordering adapter;
- initialization contract and initial-value hash if externally frozen;
- MATLAB HJB-only evaluator/harness;
- Python faithful HJB runner;
- comparator;
- call ledger;
- comparison tolerances.

### MATLAB execution object

Because the designated `HANK_2ASSETS_HJB` continues into KFE after HJB convergence, this task must not use its KFE output as evidence.

Preferred bounded evidence is an external **source-extracted HJB-only evaluator** that reproduces the designated source exactly through the final converged HJB/operator and stops immediately before the stationary KFE block.

Label this evidence:

`MATLAB_SOURCE_EXTRACTED_CONVERGED_HJB_PARITY`

The evaluator may call the designated helpers but must not modify them.

If a native source-supported HJB-only exit exists, it may be used instead and should be preferred.

## 10. Scientific call budget

After freeze:

- MATLAB converged HJB batch: at most `1`;
- Python faithful converged HJB batch: at most `1`;
- comparator: at most `1`.

No scientific rerun or tuning after observing either result.

Engineering-only syntax/serialization/unit preflights are allowed before freeze but must not solve the HJB fixture.

## 11. Required parity outputs

Compare at minimum:

### Identity/convergence

- grid/state count and ordering;
- initialization identity/hash or pointwise equality;
- convergence boolean;
- iteration count;
- MATLAB convergence statistic and Python faithful counterpart.

### Value/policy arrays

- full converged value array;
- consumption;
- labor;
- transfer;
- adjustment cost;
- effective illiquid return;
- final `mu_a`;
- final `mu_b`;
- utility;
- liquid policy/upwind labels;
- transfer/illiquid policy labels.

### HJB operator

- `BB` sparsity pattern and nonzero values;
- `AAH` sparsity pattern and nonzero values;
- `Bswitch` sparsity pattern and nonzero values;
- full `A=BB+AAH+Bswitch` sparsity pattern and nonzero values;
- diagonal entries;
- maximum absolute row sum;
- selected representative transition rates at lower/interior/upper nodes.

### Optional diagnostic-only outputs

- Bellman residual under each implementation's converged value/operator;
- nonnegativity/minimum off-diagonal;
- condition estimate if cheaply available without changing solver.

Diagnostic-only outputs cannot override a source-faithful PASS/FAIL criterion unless they reveal an actual construction contradiction.

## 12. Comparison rules

Categorical/state-order/sparsity-pattern mismatches are terminal.

For quantities produced by identical scalar arithmetic and explicit rate formulas, use exact equality where bitwise representation is identical; otherwise use the pre-frozen bound:

`128 * eps_float64 * max(1, abs(x), abs(y))`.

For outputs passing through a sparse/direct linear solve, do **not** invent or loosen a tolerance after execution.

Before scientific execution, freeze a separate strict solver-output rule. Preferred rule:

- compare converged value/update arrays using a predeclared absolute/relative bound justified from the source-defined stopping tolerance and solver arithmetic;
- the bound must be no looser than the MATLAB source convergence scale unless the task report proves before execution that a tighter machine-bound comparison is numerically well-defined.

If MATLAB and SciPy sparse factorization produce a discrepancy above the pre-frozen strict bound while all source formulas/operators are identical, return BLOCKED or MATERIAL_MISMATCH as appropriate. Do not tune tolerance in-task.

The user target is same-parameter MATLAB-faithful reproduction; visible aggregate/value discrepancies are not acceptable.

## 13. Test scope

Allowed production/test mutation only on new faithful-route modules and narrowly targeted faithful tests, plus minimal extensions to `matlab_faithful_policy.py` if source-required.

Do not modify corrected/reference `policies.py`, `hjb.py`, `generator.py`, `kfe.py`, or `steady_state.py` unless a live task contradiction proves a minimal adapter is necessary; if so stop and report rather than broadening scope.

Run only targeted faithful tests needed for:

- operator micro-assembly;
- productivity switch construction;
- initialization/helper equivalence;
- one-step implicit HJB update on synthetic data;
- predecessor faithful primitive/local-policy regressions.

Do not run the full historical suite unless explicitly necessary for import integrity; if run, report it but do not treat corrected-track failures as authority to change faithful production semantics.

## 14. Explicit prohibitions

Do not:

- resume corrected D1/D2/D3;
- modify designated MATLAB source;
- run stationary KFE;
- compute stationary density/aggregates;
- run steady state;
- run asset-tail diagnostics;
- run transition/IRF/dynamics;
- enter calibration extension or Results;
- reintroduce corrected-route KKT/corner candidate selection into faithful production without source authority;
- replace MATLAB `Bswitch` with reflected diffusion unless exact equivalence is proven;
- replace source HJB operator with a net-drift generator if source component rates differ;
- change taper/FOC/cost-floor coefficients or rules;
- tune cases, parameters, iteration settings, tolerances, or solver settings after seeing scientific output.

## 15. Terminal classifications

Return exactly one.

### PASS

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_PASS`

Use only if the source-faithful full HJB driver is implemented and the one frozen same-input converged HJB/operator comparison passes all required categorical/operator/policy/value criteria under pre-frozen rules.

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_MATERIAL_MISMATCH`

Use if both implementations validly execute the same frozen source-defined object but produce a material policy/operator/value mismatch under the pre-frozen criteria.

### BLOCKED

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_BLOCKED`

Use if exact source mapping is unresolved, implementation cannot remain within faithful-route scope, one language fails before a valid comparable HJB object exists, or sparse-solver representation prevents a qualified comparison without a new explicitly authorized diagnostic task.

## 16. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. designated MATLAB hashes;
4. complete full-HJB source map through pre-KFE boundary;
5. exact faithful architecture and changed paths;
6. explicit disposition of corrected/reference modules;
7. `Bswitch` source formula and faithful implementation;
8. initialization/`lab_solve2` source formula and faithful implementation/injection contract;
9. exact `BB`/`AAH` construction and why net drift is or is not sufficient;
10. unit/preflight results;
11. frozen parity fixture and all hashes;
12. scientific call ledger;
13. convergence/iteration comparison;
14. full value/policy maximum differences and worst-state locations;
15. operator sparsity-pattern result and max nonzero-value differences for `BB`, `AAH`, `Bswitch`, and full `A`;
16. representative rate comparisons;
17. full mismatch/failure list;
18. diagnostic-only residual/operator checks;
19. prohibited-operation confirmation;
20. git status;
21. acceptance level;
22. exact recommended next gate.

## 17. Next gate boundary

If PASS, recommend only:

**MATLAB-faithful stationary KFE contaminated-row implementation and same-operator density parity.**

Do not authorize full steady-state aggregates or dynamics from this task alone.
