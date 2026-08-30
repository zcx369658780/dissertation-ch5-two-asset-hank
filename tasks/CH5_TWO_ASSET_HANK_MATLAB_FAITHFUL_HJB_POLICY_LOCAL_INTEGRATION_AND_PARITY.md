# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Implement the first **source-faithful HJB/policy layer** for Chapter 5 without yet running a converged HJB or KFE.

The objective is not to continue the corrected-equation/KKT redesign. The objective is to map the designated MATLAB `HANK_2ASSETS_HJB.m` policy/upwind block exactly enough to construct the same one-step household controls, drifts, branch/upwind selections, utility/Hamiltonian objects, and asset-generator inputs from the same local derivative/state inputs.

This task must integrate both already accepted faithful primitives:

- bare-`a` transfer FOC;
- MATLAB `raah` illiquid-return taper.

It must also resolve the deferred question of whether the current corrected-track shadow/KKT/corner machinery belongs in the faithful production route. The answer must come from exact designated MATLAB source inspection, not mathematical preference.

This task stops before full HJB iteration/convergence, stationary KFE, steady state, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

## 2. Controlling accepted authority

Controlling reports:

- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`

Accepted predecessor terminal:

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_PASS`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Frozen primitives:

- `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`
- `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

Historical corrected-equation evidence remains reference-only:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

Historical P5 remains:

`P5_ACCEPTED_FOR_CORRECTED_EQUATION_TRACK_NOT_FINAL_MATLAB_FAITHFUL_PARITY`

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`e05c1005bf627d3c3539e7b6a0924125681f9ccd`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all three controlling reports exist on live `main`;
3. record live start SHA;
4. verify designated MATLAB source identity;
5. verify accepted faithful bare-`a` and taper primitives are present unchanged;
6. start from a clean worktree with no uncommitted scientific source mutation.

## 4. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- all three controlling reports
- designated MATLAB `HANK_2ASSETS_HJB.m`
- designated MATLAB `HANK3_FOC.m`
- designated MATLAB `HANK3_cost.m`
- designated MATLAB `lab_solve2.m`
- any directly called MATLAB helper needed by the policy/upwind block
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/generator.py`
- `src/ch5_two_asset_hank/hjb.py`
- relevant policy/HJB tests and historical local-parity reports

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required source hashes:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

If any required source identity fails, stop before mutation.

## 5. Phase A — mandatory exact MATLAB policy/upwind source map

Before authoring a faithful Python policy implementation, inspect the designated MATLAB HJB source block that produces household controls and the backward generator. At minimum cover the source region containing:

- `raah` / `Rah` construction;
- forward/backward derivatives in both asset dimensions;
- boundary derivative substitutions;
- consumption and labor controls;
- all `HANK3_FOC` calls;
- all `HANK3_cost` calls;
- liquid and illiquid drifts;
- forward/backward/zero-drift indicator construction;
- upwind derivative/control selection;
- utility / Hamiltonian flow term used in the HJB update;
- construction of `AAH`, `BB`, and their dependence on the selected drifts;
- any zero-drift or boundary formulas that bypass the ordinary FOC;
- any use of `rah`, `raah`, `Rah`, `ahmax`, `a_bar`, or a fixed adjustment-cost scale in these steps.

Record exact MATLAB variable names, exact line ranges, formulas, and array dimensions/orientations. Do not rely on old report interpretations where the new Owner authority supersedes them.

### Required branch matrix

Produce a branch matrix with at least:

- interior `a`, interior `b`;
- lower `a=0`;
- upper `a=a_max`;
- lower liquid boundary `b=b_min`;
- upper liquid boundary `b=b_max`;
- positive illiquid drift;
- negative illiquid drift;
- zero/near-zero illiquid drift if MATLAB has a specific branch;
- positive/negative/zero liquid drift;
- combinations actually represented by MATLAB's indicator/upwind algebra.

For each branch report:

- derivative used;
- transfer FOC/control used;
- return used (`Rah`/`raah`/`rah`);
- drift formula;
- boundary substitution if any;
- selection/indicator condition;
- whether an explicit multiplier/KKT/candidate-enumeration veto exists in MATLAB.

## 6. Corrected-track KKT/corner disposition — source decides

The current Python corrected/reference policy code contains:

- explicit candidate enumeration;
- lower/upper state-constraint candidates;
- endogenous zero-illiquid-drift candidates;
- multiplier recovery;
- KKT residual certification/vetoes;
- lower-`b` F/Z canonicalization;
- max-scale shadow relations in `policies.py` and `boundaries.py`.

Do **not** mechanically port those rules into the faithful route.

After Phase A, classify each such Python mechanism as exactly one of:

- `MATLAB_FAITHFUL_EQUIVALENT_REQUIRED`
- `MATLAB_FAITHFUL_DIAGNOSTIC_ONLY`
- `CORRECTED_TRACK_REFERENCE_ONLY`
- `OWNER_PROVENANCE_REQUIRED`

If designated MATLAB does not use an equivalent multiplier/KKT veto to choose its production policy, the faithful production selector must not reject/replace a MATLAB-selected policy merely because the corrected-track KKT diagnostic dislikes it. Such diagnostics may be computed after selection, but must be non-vetoing in the faithful path.

If this disposition cannot be resolved from source plus frozen Owner authority, stop before implementation with BLOCKED rather than guessing.

## 7. Implementation architecture — preserve corrected/reference route

If Phase A closes without ambiguity, implement an **explicit MATLAB-faithful local policy path** rather than silently rewriting the corrected/reference machinery.

Preferred architecture:

- add a narrowly named module such as `src/ch5_two_asset_hank/matlab_faithful_policy.py`, or an equivalently explicit faithful entry point if repository style strongly favors `policies.py`;
- keep existing corrected/reference policy machinery available for historical regression;
- do not add a mutable global mode flag or environment route switch.

The faithful local selector must consume the same fundamental local state/derivative objects needed by MATLAB and must use:

- production bare-`a` `transfer_candidate`;
- `matlab_faithful_illiquid_return` / `asset_drifts_matlab_faithful`;
- exact MATLAB boundary/upwind logic established in Phase A;
- the same asset-grid upper bound `a_max=grid.a[-1]` wherever the taper enters.

Do not duplicate taper coefficients or formulas in the policy module; call the accepted economics helper.

### Threading rule

Every branch that forms an illiquid drift or imposes `mu_a=0` must use the same effective tapered return appropriate to that state. In particular, any faithful zero-drift transfer must be based on:

`d = -r_a_effective(a,a_max) * a`

when and only when the MATLAB branch actually imposes zero illiquid drift.

Do not leave a mixture of tapered and constant-`r_a` branches in the faithful path.

## 8. Full HJB driver boundary

This task does **not** authorize switching `solve_hjb` to the new faithful selector or running a converged HJB.

`src/ch5_two_asset_hank/hjb.py` may be statically audited, but should remain unchanged unless a minimal type/import addition is strictly required for a non-iterative local parity test. Prefer no `hjb.py` mutation.

The output of this task is a validated local faithful policy/upwind implementation suitable for the next full-HJB integration gate.

## 9. Local MATLAB–Python parity fixture

After the faithful local selector is frozen, construct a fresh external parity fixture before execution.

The fixture must be source-backed and must not tune cases after seeing results.

### 9.1 Frozen case coverage

Freeze a case manifest covering at minimum:

- `a=0`;
- `0<a<a_bar`;
- `a=a_bar`;
- interior `a>a_bar`;
- `a=a_max`;
- negative liquid asset / borrowing state;
- interior and both liquid boundaries;
- positive and negative transfer regimes;
- positive and negative illiquid drift regimes;
- positive and negative liquid drift regimes;
- every MATLAB boundary/upwind branch actually reachable in the source map.

Use the smallest sufficient batch; do not inflate the fixture merely to search for passing cases.

### 9.2 MATLAB side

Do not modify designated MATLAB source.

Preferred evidence order:

1. if the designated function exposes a bounded one-step/local policy path that can be called without convergence, invoke that exact path;
2. otherwise create an external **source-extracted local evaluator** that copies only the exact designated policy/upwind formulas and calls the designated helpers (`HANK3_FOC`, `HANK3_cost`, `lab_solve2`) as applicable.

If option 2 is required, label the evidence exactly:

`MATLAB_SOURCE_EXTRACTED_LOCAL_POLICY_PARITY`

and record the extracted MATLAB source line provenance for every formula. Do not claim it is a full native-HJB execution.

Freeze/hash the MATLAB local evaluator before execution.

### 9.3 Python side

Run the faithful local selector on the exact same manifest once.

### 9.4 Comparison objects

Compare every common source-backed object available, including at minimum where defined:

- selected forward/backward derivative labels or indicator masks;
- consumption;
- labor;
- transfer `d`;
- adjustment cost;
- effective illiquid return;
- `mu_a`;
- `mu_b`;
- utility / flow payoff;
- selected asset drift directions;
- resulting local transition rates in `a` and `b` where the MATLAB source exposes them.

Categorical branch/indicator mismatches are terminal.

For directly identical scalar formulas, require exact equality when arithmetic ordering is identical; otherwise use a pre-frozen machine-precision bound such as `128*eps64*max(1,abs(x),abs(y))`. Do not choose tolerances after results are seen.

No broad `1e-7` agreement tolerance is authorized for local policy parity.

## 10. One-shot execution discipline

Before scientific local parity execution, freeze/hash:

- case manifest;
- MATLAB local evaluator;
- Python faithful local-selector revision;
- comparator;
- execution ledger.

Engineering-only syntax/container preflights are allowed, but must not evaluate scientific cases.

Scientific call budget:

- MATLAB local policy batch: at most `1`;
- Python local policy batch: at most `1`;
- comparator: at most `1`.

If any scientific batch or comparator fails, do not tune cases, equations, branches, or tolerances and rerun in the same task. Stop fail-closed.

## 11. Authorized repository mutations

Preferred production mutation:

- new `src/ch5_two_asset_hank/matlab_faithful_policy.py`

Conditional/minimal mutation if needed by explicit architecture:

- `src/ch5_two_asset_hank/policies.py` only to expose/reuse non-scientific shared plumbing without changing corrected-track semantics;
- `src/ch5_two_asset_hank/contracts.py` only if a new immutable faithful local-policy result contract is strictly required;
- `src/ch5_two_asset_hank/__init__.py` only if repository export style requires it.

Tests may add one narrowly named file such as:

- `tests/test_matlab_faithful_policy.py`

Do not modify:

- `src/ch5_two_asset_hank/economics.py` except for a source-proven bug in the already accepted faithful primitive, in which case stop and report instead of repairing here;
- `src/ch5_two_asset_hank/generator.py`;
- `src/ch5_two_asset_hank/kfe.py`;
- `src/ch5_two_asset_hank/steady_state.py`;
- MATLAB source.

Do not broadly rewrite existing corrected-track tests.

## 12. Verification allowed

Allowed:

- static compilation/import checks;
- targeted new faithful-policy tests;
- source-extracted local MATLAB parity batch under the one-shot budget;
- targeted generator-local rate checks using the selected faithful drifts;
- read-only corrected/reference regression checks if they require no scientific solver rerun.

Not allowed:

- full pytest suite;
- converged/full HJB solve;
- R4 rerun;
- D1/D2/D3 corrected-track rerun;
- stationary KFE;
- steady state;
- asset-tail;
- transition;
- IRF;
- dynamics;
- calibration extension;
- Results.

## 13. Acceptance requirements

PASS requires all of the following:

1. all designated MATLAB hashes match;
2. exact MATLAB policy/upwind source map is complete enough to implement without unresolved provenance;
3. corrected-track KKT/corner mechanisms are explicitly classified relative to MATLAB;
4. a distinct faithful local policy path exists without destroying corrected/reference code;
5. bare-`a` FOC and taper are threaded consistently through every faithful local branch;
6. no faithful branch uses constant `r_a` where MATLAB uses `Rah`/`raah`;
7. local MATLAB–Python parity fixture is frozen before execution;
8. all comparable continuous outputs pass exact/machine bounds;
9. all branch/indicator/direction selections match exactly;
10. no forbidden full-HJB/KFE/steady-state/dynamics work occurs.

This PASS does **not** authorize or claim full HJB convergence parity.

## 14. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`

The report must include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. designated MATLAB identities;
4. exact policy/upwind MATLAB source map with line ranges;
5. full branch matrix;
6. corrected-track KKT/corner disposition table;
7. production architecture and complete changed-path list;
8. faithful taper/bare-`a` threading audit;
9. exact local parity case manifest and hashes;
10. MATLAB evaluator provenance and whether native or `MATLAB_SOURCE_EXTRACTED_LOCAL_POLICY_PARITY`;
11. scientific call ledger;
12. per-field maximum difference and worst case;
13. all categorical/branch/direction mismatch counts;
14. complete mismatch/failure list;
15. targeted test results;
16. forbidden-operation check;
17. git status;
18. acceptance level;
19. exact recommended next gate.

## 15. Terminal classifications

Return exactly one.

### PASS

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_PASS`

### Material mismatch

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_MATERIAL_MISMATCH`

Use only after valid source-backed MATLAB and Python local outputs exist and a frozen comparison finds a real numerical/categorical mismatch.

### BLOCKED

`MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_BLOCKED`

Use if source identity/provenance cannot be resolved, faithful architecture cannot remain bounded, or a source/environment blocker prevents valid local comparison.

## 16. Next gate boundary

If PASS, recommend only:

**MATLAB-faithful full HJB driver integration and converged same-input HJB/operator parity.**

That next gate may switch the HJB driver to the accepted faithful selector and compare full value/policy/operator outputs under identical MATLAB/Python inputs.

Do not authorize stationary KFE, steady state, or dynamics from this task alone.
