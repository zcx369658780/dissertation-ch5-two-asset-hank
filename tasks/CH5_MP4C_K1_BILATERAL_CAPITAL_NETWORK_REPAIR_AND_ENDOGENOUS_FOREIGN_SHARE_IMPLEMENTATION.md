# Chapter 5 MP4C K1 bilateral capital-network repair and endogenous foreign-share implementation

Date: 2026-09-11

Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Implement a separately named, zero-science successor capital-allocation module that repairs the two identified legacy defects while preserving the two-asset household state space:

1. restore each origin household sector's retained domestic illiquid investment `(1-theta_i) * A_i * N_i` to destination `i` private productive capital;
2. replace the legacy inconsistent `rah` weighting with one bilateral portfolio matrix used consistently for both capital flows and household illiquid returns.

The successor must adopt the Owner-approved nested Scheme B architecture:

- Stage K1 keeps the existing `inter_prv_ratio_i = theta_i` as the *total foreign-investment share* for each origin;
- domestic share is `S[i,i] = 1-theta_i`;
- the foreign part `theta_i` is allocated across the other 30 destinations by normalized, endogenous destination weights;
- foreign destination weights are allowed to depend on a distance/friction score and a *lagged* return-attractiveness score;
- no same-turn return feedback is allowed;
- `theta_i` itself remains fixed in this task. Endogenizing the home-vs-foreign margin is a later K2 task.

This task is implementation + deterministic accounting validation only. It does not run a scientific trajectory and does not choose/calibrate portfolio-sensitivity coefficients.

Results eligibility remains FALSE.

## 2. Authority to read

Fresh-fetch `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current project status / roadmap / handoff;
- `src/ch5_two_asset_hank/multi_province/capital_allocation.py`;
- current `one_turn.py`, `c1_residual_public_asset.py`, `firm.py`, `wage.py`;
- accepted C1 residual-public-asset reports/acceptances;
- accepted price/numeraire/raw-ra forensic and acceptance;
- accepted origin-preserving bilateral labor normalization implementation/acceptance;
- protected MATLAB `HANK_mp_1turn.m` if locally available, read-only.

The existing literal `allocate_productive_capital` remains source-faithful legacy authority and must not be edited into the successor silently.

## 3. Frozen economic interpretation

For origin province `i`:

- household aggregate illiquid wealth available for productive ownership is `A_i * N_i` under the existing diagnostic asset bridge;
- `theta_i = inter_prv_ratio_i` is the total share invested outside the origin province;
- `(1-theta_i)` is the retained home share;
- public/government productive capital is not part of this private ownership matrix;
- liquid `Bt` is excluded from productive capital;
- public `GovInv` remains a separate C1 residual-government-asset object.

Do not reinterpret `theta_i` as a destination attractiveness parameter.

## 4. Bilateral portfolio orientation

Use one explicit 31x31 matrix:

`S[destination, origin]`.

For each origin column `i`:

- `S[i,i] = 1 - theta_i`;
- for `j != i`, `S[j,i] = theta_i * P[j,i]`;
- `P[i,i] = 0`;
- `sum_{j != i} P[j,i] = 1`;
- therefore `sum_j S[j,i] = 1` exactly within deterministic tolerance.

The same `S` must drive both capital quantities and household returns.

## 5. Foreign conditional-share engine

Implement a separately named pure function for `P[destination,origin]` using explicit caller-provided *dimensionless* scores:

`foreign_log_attractiveness[j,i] = - beta_distance * distance_score[j,i] + beta_return * lagged_return_score[j]`

for `j != i`, with diagonal excluded before normalization.

Then use a numerically stable softmax over destinations within each origin column:

`P[j,i] = exp(score[j,i] - max_foreign_score_i) / sum_{k != i} exp(score[k,i] - max_foreign_score_i)`.

Important boundaries:

- `beta_distance` and `beta_return` are explicit inputs;
- this task must NOT choose, estimate, fit, or supply scientific default values for them;
- tests may use synthetic coefficients, including zero, solely to verify algebra;
- `distance_score` must be caller-provided and dimensionless. Do not decide here whether it is pure geographic distance, pgdp distance, or a composite friction;
- `lagged_return_score` must be caller-provided and explicitly labelled as *old-turn / lagged* information;
- do not read same-turn firm `ra0` inside this module;
- do not use clipped-return bounds as portfolio attractiveness by default;
- do not standardize or rescale returns internally without an explicit future normalization contract.

## 6. Corrected capital-flow matrix

Given aggregate origin private wealth:

`W_i = A_i * N_i`

construct:

`M_K[j,i] = S[j,i] * W_i`.

Then destination private productive capital is:

`Kprivate_j = sum_i M_K[j,i]`.

Required conservation identities:

- each origin column: `sum_j M_K[j,i] = W_i`;
- national: `sum_j Kprivate_j = sum_i W_i`;
- retained domestic component: `M_K[i,i] = (1-theta_i) * W_i`;
- foreign origin flow: `sum_{j!=i} M_K[j,i] = theta_i * W_i`.

This explicitly repairs the legacy omission of retained home capital.

## 7. Corrected household illiquid return

For a caller-provided destination payoff vector `portfolio_return_by_destination[j]`, define:

`rah_i = sum_j S[j,i] * portfolio_return_by_destination[j]`.

Required properties:

- weights sum to one by origin;
- the same matrix `S` used for quantities is used for returns;
- no additional multiplication by destination `theta_j`;
- no unnormalized `tempra` construction;
- if all destination returns are equal, every `rah_i` equals that common return;
- if `theta_i=0`, `rah_i` equals the home return exactly;
- if `theta_i=1`, `rah_i` is the foreign conditional weighted average with zero home weight.

Do not decide in this task whether `portfolio_return_by_destination` should eventually be raw `ra0`, clipped `ra`, or a normalized expected-return object. Keep it explicit at the API boundary because price/return normalization remains a separate unresolved gate.

## 8. Required APIs and audit objects

Create a separately named module, e.g. `capital_network.py`, containing pure dataclasses/functions with no scientific runtime imports.

At minimum expose:

- nested portfolio inputs;
- foreign conditional shares `P`;
- full portfolio shares `S`;
- origin wealth `W`;
- bilateral capital matrix `M_K`;
- destination private productive capital;
- domestic retained capital by origin;
- foreign outflow by origin;
- foreign inflow by destination;
- household portfolio return `rah`;
- column share sums;
- column capital sums;
- national conservation residual;
- orientation/schema/version labels;
- lagged-signal provenance label.

All returned arrays must be read-only.

## 9. Legacy special-case receipts

Provide deterministic receipts showing:

### 9.1 Equal-foreign-share repaired special case

Set synthetic `beta_distance=0`, `beta_return=0`.

Then for each origin:

`P[j,i] = 1/(N-1)` for `j != i`.

This should reproduce the Owner's intended simplified legacy economic idea, but with both defects repaired:

- home retained capital included;
- `rah` foreign payoff averaged without destination `theta_j` double weighting.

### 9.2 Old legacy discrepancy

Using a small asymmetric synthetic fixture, compare the current legacy function against the repaired equal-share successor and explicitly show:

- legacy destination private K misses retained home capital;
- legacy `rah` portfolio weights generally sum below one when `0<theta_j<1`;
- repaired successor satisfies both capital conservation and portfolio-weight conservation.

Do not modify the legacy function.

## 10. Lagged-return timing contract

Encode the timing contract explicitly in docs/API:

- household block at numerical iteration `n` uses portfolio return inherited from the previously completed firm state;
- foreign-share update for iteration `n+1` may use a lagged return-attractiveness score from completed iteration `n`;
- same-turn `firm -> return -> share -> capital -> firm` circular feedback is prohibited in this K1 module;
- a future runtime integration must preserve this lagged ordering.

This is a steady-state numerical-iteration device, not a claim about literal calendar-time portfolio adjustment.

## 11. No new scientific coefficients in this task

Do not select or infer:

- `beta_distance`;
- `beta_return`;
- portfolio adjustment speed;
- home-bias parameter beyond the existing fixed `theta_i`;
- pgdp coefficient;
- industrial-distance coefficient;
- expected-return smoothing coefficient.

Do not fit anything to convergence, Ktarget, ra, or historical outcomes.

## 12. Required tests

At minimum verify:

1. exact destination x origin orientation;
2. every `P` foreign column sums to one over `j != i`;
3. every full `S` column sums to one;
4. domestic retained share exactly `1-theta_i`;
5. foreign outflow exactly `theta_i * W_i`;
6. origin capital conservation;
7. national private-capital conservation;
8. destination private K equals bilateral row sums;
9. household `rah` uses the identical `S` matrix;
10. common-return invariance;
11. `theta=0` home-only edge case;
12. `theta=1` foreign-only edge case;
13. beta-distance=beta-return=0 gives equal foreign shares;
14. increasing one destination lagged return score raises that destination foreign share for all eligible origins, holding other scores fixed;
15. increasing one bilateral distance score lowers only the corresponding destination attractiveness before renormalization;
16. no same-turn return object is imported or queried;
17. invalid/nonfinite scores fail closed;
18. invalid theta outside `[0,1]` fails closed;
19. exact province-order / shape checks;
20. legacy `allocate_productive_capital` source file remains byte-identical;
21. no HJB/KFE/firm/wage/controller/trajectory scientific calls occur.

## 13. Strict prohibitions

Do not:

- run a scientific trajectory;
- run steady state;
- run HJB/KFE/household/firm/wage/migration runtime;
- call MATLAB runtime;
- activate normalized labor;
- modify C1 GovInv residual-public-asset code;
- alter return or wage clips;
- alter price/numeraire normalization;
- alter `beta_a`;
- endogenize `theta_i` yet;
- choose portfolio coefficients;
- connect the new module to active steady-state runtime.

## 14. Required outputs

At minimum:

- new pure capital-network source/module;
- tests;
- `docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_REPORT.md`;
- `reports/mp4c_k1_bilateral_capital_network_20260911/portfolio_contract.md`;
- `.../synthetic_asymmetric_trace.csv`;
- `.../legacy_vs_repaired_equal_share_receipt.json`;
- `.../conservation_receipt.json`;
- `.../lagged_return_timing_contract.md`;
- `.../api_schema_receipt.json`;
- `.../legacy_capital_allocation_unchanged_receipt.json`;
- `.../zero_scientific_call_ledger.json`;
- `.../source_hash_receipt.json`;
- `.../focused_test_receipt.json`;
- `.../manifest.json`;
- `.../manifest_readback.json`.

## 15. Required report answers

Answer directly:

1. Does the successor restore retained home private capital exactly?
2. Does national private capital equal total household illiquid wealth under the current bridge?
3. Do capital-flow weights and household-return weights use the same matrix?
4. Does the repaired equal-foreign-share special case remove the legacy `theta_j` double weighting in `rah`?
5. Is lagged-return timing encoded without same-turn circular feedback?
6. Can the architecture support later distance + lagged-return endogenous foreign shares without increasing HJB asset dimensions?
7. Which coefficient/data decisions remain for Owner before any scientific trajectory?
8. Is engineering evidence sufficient for a later separately authorized bounded K1 trajectory?

## 16. Allowed verdicts

- `K1_BILATERAL_CAPITAL_NETWORK_PASS__HOME_CAPITAL_RESTORED_PORTFOLIO_WEIGHTS_CONSERVED_AND_ENDOGENOUS_FOREIGN_SHARE_ENGINE_IMPLEMENTED`
- `K1_BILATERAL_CAPITAL_NETWORK_PARTIAL__ACCOUNTING_REPAIR_VALID_BUT_ENDOGENOUS_SHARE_ENGINE_INCOMPLETE`
- `K1_BILATERAL_CAPITAL_NETWORK_BLOCKED__CURRENT_ARCHITECTURE_CANNOT_PRESERVE_CAPITAL_AND_RETURN_WEIGHT_IDENTITY_WITHOUT_BROAD_REDESIGN`

PASS does not authorize scientific runtime integration.

## 17. Git boundary

Use dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit + non-force push;
- do not merge main;
- do not publish successor task;
- Results eligibility remains FALSE.

Return to Reviewer with verdict, branch, candidate SHA, changed files, focused tests, conservation receipts, legacy discrepancy receipt, lagged-timing receipt, zero-call ledger, and report path.