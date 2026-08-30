# CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_COMPONENT_ADJUDICATION_AND_HJB_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resolve the single blocker from the first full MATLAB-faithful HJB parity attempt: the frozen Python candidate assumed every iteration-`BB` off-diagonal component must be nonnegative, while the already accepted one-shot MATLAB HJB output contains a negative iteration-`BB` off-diagonal entry and still converges with exact row closure.

This task must first determine from the designated MATLAB source and the frozen MATLAB output whether that negative entry is an **intended source-faithful signed iteration coefficient** or evidence of a source-extraction/assembly contradiction.

Only if the source audit proves that signed iteration-`BB` off-diagonal coefficients are genuinely produced by the designated MATLAB formulas may the faithful Python candidate be rebuilt with the corresponding signed-coefficient contract and receive one replacement Python HJB execution plus one comparator execution.

The already successful MATLAB HJB batch MUST NOT be rerun.

This task stops before KFE, stationary distribution, steady-state aggregates, asset-tail, transition, IRF, dynamics, calibration extension, or Results.

## 2. Controlling accepted authority

Read and obey:

- `docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HOUSEHOLD_PRIMITIVES_BARE_A_FOC_IMPLEMENTATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_AND_DRIFT_GENERATOR_PLUMBING_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_POLICY_LOCAL_INTEGRATION_AND_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_REPORT.md`

Accepted predecessor terminal:

`MATLAB_FAITHFUL_FULL_HJB_DRIVER_AND_CONVERGED_OPERATOR_PARITY_BLOCKED`

Primary authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted faithful primitives/local-policy evidence remain frozen.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`ece691df430fb1855ce7982e1f3c54043a8dd924`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all controlling reports exist on live `main`;
3. record live start SHA;
4. verify designated MATLAB hashes;
5. verify accepted faithful production/local-policy files have not drifted;
6. verify the predecessor report commit is the direct accepted parent of this task authority;
7. record clean worktree state.

Do not begin from uncommitted scientific source changes.

## 4. Reuse-only frozen predecessor evidence

The following predecessor scientific artifact MUST be reused read-only and MUST NOT be regenerated:

MATLAB converged HJB output SHA-256:

`3457F51AC0F910EA40FC35A832518B9068456E22DEA4E4783F487976432DDC0A`

Predecessor artifact root:

`D:\ProjectTemp\ch5-matlab-faithful-full-hjb-parity-20260830-001`

Frozen predecessor identities:

- parameter/grid manifest `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A`
- ordering adapter `52EB994358F07767AD8859D737C3D7A89BC7FB04DC063754027CA80386F2926D`
- initialization artifact `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`
- MATLAB HJB-only evaluator `E81AB34611E3C31DAF2400ED6A34B58F91C4FA0E0FBCCEE843828F5A6588DCBA`
- Python runner `CE3C320DC6D7014A692FE0B71165854236FECD0D23C0A8026C1BCD152D5FF2AC`
- comparator `4471CCC837A66245DCB8D2CA1D45F1BD79CBEE5EAE80874B14933E06C75F9A92`
- tolerances `915B3539828F42099182A9145E64B4A353D0D049AF1674549C1031C923CEF72D`
- predecessor frozen policy candidate `58CD63AC847E7D241B39CE687D25BCA9DB82E515007F205AC4E01B37D7ED53AF`
- predecessor frozen operator candidate `D946C8DEB251DA06C1859FBFD7E6BEE12B53F3891BE55F79D66DD7E8B50367A7`
- predecessor frozen HJB candidate `D96231B44C5BA45C694C0A943C308EF0CF5CFAFE93E0DE6C8E0ED736278F35DA`

The valid MATLAB batch is already consumed:

- MATLAB HJB calls in this task: exactly `0`.

Historical predecessor result:

- 50 states;
- converged `true`;
- 9 iterations;
- convergence statistic `3.882012578060312e-08`;
- iteration `BB` minimum off-diagonal `-0.45465503938313373`;
- iteration `BB` row-sum maximum absolute value `0`;
- post-convergence `BB` minimum off-diagonal `0.19141418136524457`.

Do not alter any predecessor scientific artifact.

## 5. Designated MATLAB source identity

Designated root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Required hashes:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Stop BLOCKED if identities do not match.

## 6. Mandatory negative-component adjudication — no HJB execution

Before rebuilding any production candidate, perform a read-only source/artifact audit.

### 6.1 Locate every negative iteration-BB off-diagonal

From the frozen MATLAB HJB output:

- enumerate every negative off-diagonal entry of the **iteration `BB`** matrix that is persisted in the valid MATLAB object;
- report matrix row/column in MATLAB one-based and Python zero-based indexing;
- map each entry back to `(b-index, a-index, z-index)` and physical `(b,a,z)`;
- report whether it is backward or forward liquid-neighbor coupling;
- report the exact coefficient value.

If the frozen output does not preserve enough component data to diagnose the source term, use the frozen parameter/grid/initialization artifacts and designated source formulas in a **read-only algebraic diagnostic**. Do not rerun the HJB iteration.

### 6.2 Decompose each negative entry into MATLAB source terms

For each negative iteration-BB entry, recover or recompute without HJB iteration the exact local terms that feed the source coefficient:

- `Ic_B`, `Ic_F`;
- `sc_B`, `sc_F`;
- `Idh_B`, `Idh_F`;
- `sdh_B`, `sdh_F`;
- `db`;
- boundary state flags, especially `b==b_max` / `b==b_min`;
- selected transfer-side derivative objects needed to establish `sdh` sign.

Then identify the exact designated MATLAB line/formula that generates the signed entry.

The audit must explicitly test the source hypothesis suggested by the predecessor source map:

- MATLAB normally defines `Idh_B` through `sdh_B < -1e-12`, which would make `-Idh_B*sdh_B/db >= 0`;
- but at the upper liquid boundary MATLAB forcibly sets `Idh_B=1` and `Idh_F=0`;
- determine whether a negative off-diagonal arises because the forced upper-`b` branch retains an `sdh_B > 0` term, or from some other exact source-backed mechanism.

Do NOT assume this hypothesis is correct. Prove or reject it from the designated source and frozen object.

### 6.3 Distinguish iteration matrix from post-convergence generator

The report must explicitly distinguish:

- **iteration `BB` / iteration `A`** used inside the implicit HJB update;
- **post-convergence `BB` / `AAH` / `A`** reconstructed from final net drift immediately before KFE.

Do not call a signed HJB iteration coefficient a Markov transition rate unless the designated MATLAB source treats it as such.

## 7. Adjudication classifications

Return exactly one internal adjudication before any candidate rebuild.

### A. Source-faithful signed iteration coefficient

`MATLAB_ITERATION_BB_SIGNED_COEFFICIENT_SOURCE_CONFIRMED`

Use only if every observed negative iteration-`BB` entry is reproduced by exact designated MATLAB source algebra and is not an extraction/indexing error.

If A holds, freeze the following authority:

`MATLAB_FAITHFUL_HJB_ITERATION_BB_MAY_CONTAIN_SIGNED_OFFDIAGONAL_COEFFICIENTS`

Interpretation:

- the HJB iteration `BB` matrix is a source-faithful discretization/update operator, not automatically a valid continuous-time Markov generator;
- nonnegativity is NOT an acceptance condition for iteration `BB` or iteration full `A`;
- exact source algebra and row closure ARE the faithful acceptance conditions;
- this authority applies ONLY to the HJB iteration operator;
- it does NOT authorize negative off-diagonals in the post-convergence pre-KFE operator;
- post-convergence `BB/AAH/A` must continue to match MATLAB and must satisfy whatever signs the designated MATLAB reconstruction actually produces.

### B. Extraction/indexing contradiction

`MATLAB_ITERATION_BB_NEGATIVE_COMPONENT_EXTRACTION_OR_INDEXING_CONTRADICTION`

Use if the frozen negative entries cannot be reproduced from exact source algebra or are caused by an ordering/assembly error.

If B holds, do not rebuild Python HJB in this task. Stop BLOCKED with the exact source-extraction correction needed for a future task. Do not rerun MATLAB.

### C. Unresolved source ambiguity

`MATLAB_ITERATION_BB_NEGATIVE_COMPONENT_OWNER_PROVENANCE_REQUIRED`

Use only if the designated source itself is ambiguous and exact treatment cannot be determined. Do not guess.

## 8. Conditional Python candidate rebuild — only after classification A

If and only if A is proven, rebuild the faithful full-HJB candidate from the frozen predecessor candidate architecture.

Preferred production modules remain distinct faithful-route modules, e.g.:

- `src/ch5_two_asset_hank/matlab_faithful_operator.py`
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py`

and only the minimal extension to accepted `matlab_faithful_policy.py` needed for faithful component construction.

Do not modify or repurpose:

- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/generator.py`
- corrected/reference KFE/steady-state routes.

### 8.1 Exact correction scope

Relative to the frozen predecessor candidate, the scientific correction must be limited to the false nonnegativity assumption for **iteration MATLAB component coefficients** and any naming/assertion changes necessary to reflect that they are signed coefficients rather than guaranteed transition rates.

Do not change:

- source formulas for `BB`;
- source formulas for `AAH`;
- `Bswitch`;
- initialization;
- parameter/grid fixture;
- ordering;
- HJB matrix/RHS;
- convergence rule;
- bare-`a` FOC;
- taper;
- local policy rules;
- tolerances;
- post-convergence net-drift operator formulas.

Every changed line relative to the predecessor frozen candidate must be classified:

`SIGNED_ITERATION_COEFFICIENT_FAITHFULNESS_ONLY`

### 8.2 Required engineering tests before replacement HJB

Create/freeze a fresh no-overwrite successor artifact root.

Before replacement Python HJB execution, freeze/hash/read back:

- rebuilt policy/operator/HJB faithful candidate sources;
- complete predecessor-candidate-to-successor diff;
- negative-component adjudication artifact;
- targeted engineering tests;
- reused MATLAB HJB output identity;
- unchanged manifest/grid/initialization/ordering/comparator/tolerance artifacts;
- successor execution ledger.

Run targeted engineering tests only. They must include:

1. exact reproduction of at least one source-confirmed negative iteration-`BB` coefficient;
2. exact iteration-`BB` row closure after signed coefficient assembly;
3. exact synthetic positive-coefficient case from predecessor tests still passes;
4. `AAH` assembly unchanged;
5. `Bswitch` unchanged;
6. post-convergence net-drift operator retains its existing sign contract and is not affected by the signed-iteration authority;
7. predecessor faithful primitive/local-policy regressions remain passing.

No full/converged HJB is allowed during these engineering tests.

If engineering tests fail, do not repair/rerun beyond ordinary non-scientific coding iteration before freeze. Once the successor scientific artifacts are frozen, no further scientific-source change is allowed in this task.

## 9. Replacement Python HJB execution — only after A and preflight PASS

The predecessor Python batch was consumed before a valid HJB object existed because of the false guard. This task authorizes exactly one replacement Python faithful HJB batch after successor freeze.

Use EXACTLY the predecessor frozen scientific fixture and inputs:

- same parameter/grid manifest;
- same 50 states;
- same ordering adapter;
- same initialization artifact;
- same `Delta=1000`, `crit=1e-7`, `maxit=100`;
- same comparator;
- same frozen tolerances.

Scientific call budget in this task:

- MATLAB HJB: exactly `0`;
- replacement Python HJB: at most `1`;
- comparator: at most `1`, only after valid Python HJB persistence.

If replacement Python HJB fails for any reason, do not repair or rerun it in this task.

## 10. Comparator and acceptance contract

If a valid Python HJB object is persisted, run the existing frozen comparator exactly once against the reused MATLAB HJB output.

Compare all predecessor-authorized objects:

### Identity/convergence

- grid/state count;
- ordering;
- initialization identity;
- convergence boolean;
- iteration count;
- convergence statistic.

### Full arrays

- converged `V`;
- consumption;
- labor;
- transfer;
- adjustment cost;
- effective illiquid return;
- `mu_a`;
- `mu_b`;
- utility;
- liquid labels;
- transfer labels.

### Iteration operators

- iteration `BB` sparsity pattern and every value, including negative entries;
- iteration `AAH` sparsity pattern and every value;
- `Bswitch` sparsity pattern and every value;
- iteration full `A` sparsity pattern and every value;
- diagonal values;
- row-sum closure.

For iteration `BB/A`, negative off-diagonals are not mismatches if and only if they match the MATLAB source/frozen object under classification A.

### Post-convergence pre-KFE operators

- post-convergence `BB`;
- post-convergence `AAH`;
- post-convergence full `A`;
- sparsity patterns and values;
- row sums;
- minimum off-diagonal values.

Do NOT weaken the post-convergence sign expectations because of the iteration-operator adjudication.

### Tolerances

Reuse unchanged predecessor frozen tolerances:

- direct scalar/rate/operator arithmetic: `128*eps64*max(1,abs(x),abs(y))`;
- converged solver-derived `V`: absolute `1e-7` as pre-frozen in predecessor task.

Do not tune or loosen tolerance after observing replacement output.

Categorical/state-order/sparsity mismatches are terminal.

## 11. Terminal classifications

Return exactly one overall terminal.

### PASS

`MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_ADJUDICATION_AND_HJB_RESUMPTION_PASS`

Use only if:

- adjudication A is proven;
- successor candidate change is strictly signed-iteration-coefficient faithfulness;
- no MATLAB rerun occurs;
- replacement Python HJB persists a valid converged object;
- comparator passes all frozen HJB/policy/operator objects;
- no prohibited change/rerun occurs.

This PASS also closes the predecessor full-HJB parity gate and authorizes the next gate to be MATLAB-faithful stationary KFE contaminated-row same-operator density parity.

### MATERIAL MISMATCH

`MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_ADJUDICATION_AND_HJB_RESUMPTION_MATERIAL_MISMATCH`

Use if valid MATLAB and Python HJB objects exist and the frozen comparator reports any material mismatch.

### BLOCKED

`MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_ADJUDICATION_AND_HJB_RESUMPTION_BLOCKED`

Use if:

- adjudication B or C occurs;
- successor correction cannot remain within signed-iteration-coefficient scope;
- engineering preflight cannot be qualified;
- replacement Python HJB fails before valid persistence;
- source/environment prevents comparison.

## 12. Explicit prohibitions

Do not:

- rerun MATLAB HJB;
- modify designated MATLAB source;
- change the frozen 50-state fixture;
- change parameters, grids, ordering, initialization, Delta, crit, maxit, or tolerances;
- reinterpret the post-convergence operator as allowing signed off-diagonals without source evidence;
- modify corrected/reference `policies.py`, `hjb.py`, `generator.py`, KFE, or steady-state routes;
- resume corrected D1/D2/D3;
- run KFE;
- run stationary distribution;
- run steady-state aggregates;
- run asset-tail;
- run transition/IRF/dynamics/calibration/Results;
- tune a negative coefficient away;
- clip signed iteration coefficients to zero;
- take absolute values of signed coefficients;
- net component coefficients before the source-defined matrix assembly;
- change boundary indicators to restore nonnegativity.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_COMPONENT_ADJUDICATION_AND_HJB_RESUMPTION_REPORT.md`

The report must include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. designated MATLAB identities;
4. predecessor frozen artifact/hash re-verification;
5. exact list of negative iteration-`BB` entries;
6. state/index mapping for each negative entry;
7. exact source-term decomposition for each negative entry;
8. adjudication A/B/C with evidence;
9. explicit distinction between iteration signed coefficients and post-convergence pre-KFE generator;
10. if A: exact successor candidate diff and line classifications;
11. successor artifact hashes and engineering preflight results;
12. complete scientific call ledger including historical consumed MATLAB/Python calls;
13. replacement Python HJB output hash/convergence details if reached;
14. comparator output hash and full comparison summary if reached;
15. iteration operator minima/row sums in both languages;
16. post-convergence operator minima/row sums in both languages;
17. full-array maximum differences/worst states if reached;
18. scientific mismatch list;
19. source/environment failure list;
20. prohibited-operation check;
21. changed paths;
22. git status;
23. acceptance level;
24. exact recommended next gate.

## 14. Next gate boundary

Only if overall PASS, recommend:

**MATLAB-faithful stationary KFE contaminated-row implementation and same-operator density parity.**

Do not authorize full steady-state aggregates or dynamics yet.
