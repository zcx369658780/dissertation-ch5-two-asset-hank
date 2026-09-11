# CH5 MP4C K1A — 2018 distance-score mapping and static portfolio diagnostic

Date: 2026-09-11.
Task ID: `CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science data mapping / static capital-network diagnostic.
Issuer: ChatGPT Reviewer under Owner standing authorization.
Publication baseline: live main after `31ca6215fb067ffb9ce83a6a88fbae18aa39b0d7`.

## 1. Goal

Produce the first reproducible 2018 K1A spatial-capital mapping receipt without running the economic model.

The task must establish the exact province mapping and dimensionless geographical-distance matrix, validate the repaired equal-share benchmark, and show how pure-geographic foreign portfolio shares behave over the pre-registered diagnostic `beta_distance` grid.

It must also document the Owner-frozen K1B lagged raw-`ra0` z-score contract and diagnostic `beta_return` grid, but must not generate new firm returns or choose final scientific coefficients.

This task is evidence preparation only. It does not connect K1 to one-turn, C1, firm, HJB, KFE, steady-state, trajectory, annual, IRF or Results runtime.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`. Verify this task is present and has not been superseded.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_REPORT.md`
- `src/ch5_two_asset_hank/multi_province/capital_network.py`

Read source/data provenance documents only as needed to establish exact 31-province order and the protected geographical-distance workbook identity. Do not restart historical scientific gates.

## 3. Local checkout safety

The known original local `main` checkout may be far behind live main and contain many untracked files. Do not reset, clean, stash or overwrite it and do not require it to fast-forward.

If the current verified checkout is not a clean worktree based on live `origin/main`, create a fresh isolated task worktree/branch from live `origin/main` under a unique `D:\ProjectTemp\...` path. Record which worktree is actually used. Preserve the original checkout unchanged.

No work in `deep-learning-hank` or any other repository.

## 4. Frozen scientific contract for this task

Use the Owner-approved contract exactly as recorded in `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`.

### 4.1 Stage order

`K1A equal-share -> K1A pure-geographic -> K1B lagged-return -> K2`.

K1 keeps `theta_i=inter_prv_ratio_i` fixed. Source-faithful labor remains frozen for the first future K1 integration.

### 4.2 Geographical distance

First distance concept is pure geographical distance only.

Primary source candidate is protected MATLAB workbook:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\中国各省省会地理距离矩阵.xlsx`

The known logical `C:\MatlabProgram` junction may point to `D:\MatlabProgram`; verify the actual path used and read the source only. Never modify it.

Dimensionless normalization is fixed as:

`distance_score[j,i] = D[j,i] / D_max`

where `D_max` is the maximum valid off-diagonal distance in the same mapped 31-province matrix. Diagonal score is exactly zero. No row-wise or column-wise normalization.

### 4.3 Diagnostic distance grid

Evaluate only this pre-registered grid:

`beta_distance = [0.0, 0.5, 1.0, 2.0, 4.0]`

with `beta_return=0`.

These are diagnostic candidates only. Do not label any positive value as the final benchmark.

### 4.4 K1B return-score contract

Document, but do not newly execute, the future K1B score:

`z_ra0_j^(n) = (ra0_j^(n) - mean_j(ra0^(n))) / sd_j(ra0^(n))`

Allocation at outer iteration `n+1` may use only completed-iteration `n` raw, unclipped `ra0`. Same-turn return feedback is prohibited.

Diagnostic future `beta_return` grid:

`[0.0, 0.25, 0.5, 1.0, 2.0]`.

Do not use historical clipped `[0.02,0.09]` return as attractiveness. Do not pass standardized scores as household payoff returns.

The final payoff-return concept remains unresolved and blocks future `rah` runtime integration, but does not block this task.

### 4.5 Smoothing

No smoothing or partial adjustment. Do not add one.

## 5. Required source/data mapping work

### 5.1 Province order

Establish one explicit active 31-province order from repository authority. Record its source path/lines or structured object.

Read the geographical-distance workbook labels. Produce an explicit source-label -> active-label mapping receipt. Mapping must be label-backed; do not silently assume worksheet position equals model position.

Special naming variants such as `内蒙古/内蒙古自治区`, `广西/广西壮族自治区`, `宁夏/宁夏回族自治区`, `新疆/新疆维吾尔自治区`, municipalities, or any other workbook naming differences must be documented and resolved transparently. Do not silently drop or reorder provinces.

### 5.2 Raw distance matrix checks

Record:

- source path and SHA-256;
- workbook sheet/range actually read;
- mapped matrix shape;
- units stated or inferable from source metadata; if units are not explicit, mark them unresolved rather than inventing them;
- finite/missing counts;
- negative-value count;
- exact diagonal values;
- symmetry residual `max |D-D.T|`;
- minimum and maximum off-diagonal distance and corresponding province pair(s).

If source asymmetry or other material data defects exist, preserve/report them. Do not symmetrize, impute or otherwise repair scientific data under this task.

### 5.3 Frozen normalized matrix

Compute `D_score=D/D_max` after exact mapping. Confirm:

- shape `31x31`;
- diagonal exactly zero if raw source supports it;
- off-diagonal range within `[0,1]`;
- maximum off-diagonal score exactly/within machine tolerance 1;
- symmetry residual inherited from raw source;
- province orientation is `destination x origin` for K1 use.

## 6. Static K1 portfolio diagnostics

Use the accepted pure `capital_network.py` module only as a zero-science algebra utility. Calling this pure mapping function does **not** count as an HJB/KFE/firm/model-runtime call, provided no active model runtime is invoked.

Identify the source of the 31-vector `inter_prv_ratio` / `theta_i` used by the source-faithful multi-province route. Record provenance and exact province mapping. Do not estimate or tune theta.

If an authoritative mapped theta vector cannot be established without model execution, stop theta-dependent real-31 diagnostics, report the blocker, and still complete the distance-only evidence. Do not fabricate a vector.

When theta is available, use unit origin wealth `W_i=1` for every province for static accounting diagnostics. This is deliberately a mathematical receipt, not a 2018 economic quantity claim.

For each `beta_distance` in `[0,0.5,1,2,4]`, with `beta_return=0` and a zero lagged-return score vector carrying explicit lagged/completed provenance:

1. build foreign conditional shares `P[j,i]`;
2. build full portfolio shares `S[j,i]` with the frozen theta;
3. verify each foreign conditional column sums to 1 over `j!=i`;
4. verify each full portfolio column sums to 1;
5. verify `S[i,i]=1-theta_i` exactly within the accepted tolerance;
6. verify unit-wealth origin and national capital conservation;
7. verify `beta_distance=0` gives `1/(N-1)` foreign conditional shares;
8. report no destination-`theta_j` double weighting.

For foreign `P` (not the full home-biased `S`), summarize for each beta:

- mean/min/max column entropy and entropy normalized by `log(N-1)`;
- mean/min/max largest foreign destination share;
- mean/min/max effective number of foreign destinations `exp(entropy)`;
- median distance of the top foreign destination, plus a concise list of top destination for at least 5 geographically diverse origins;
- whether higher beta monotonically weakly reduces entropy for every origin; if not, report exact exceptions.

Also create one compact table showing, for a representative set of origins, top-3 foreign destinations and shares at beta `0`, `1`, and `4`. Choose the representative origins by a deterministic rule stated before inspecting share outcomes (for example fixed province indices spanning north/east/central/west/southwest), not by choosing visually interesting results after computation.

Do not call these matrices estimated bilateral capital holdings. They are static implied allocation weights under diagnostic coefficients.

## 7. K1B coefficient interpretation receipt

No new `ra0` may be generated.

For the frozen standardized score, document the pure logit interpretation of the diagnostic beta-return grid. At minimum report the multiplicative foreign-attractiveness odds factor `exp(beta_return * Δz)` for `Δz=1` and `Δz=2` standard deviations for each candidate beta.

This is algebra only; it is not coefficient identification or a model result.

If a previously accepted, manifest-bound completed-iteration raw-`ra0` vector is readily available through an already documented path, it may be **read only** and its z-score summarized as an optional receipt, with exact provenance. Do not search arbitrary temp directories, regenerate returns, or make such a vector a required condition for PASS.

## 8. Allowed implementation/output paths

Authorized tracked changes are limited to:

- `tasks/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC.md` (authority; do not rewrite except an explicitly necessary typo correction);
- one reproducible zero-science script under `scripts/` named for this task, if needed;
- focused tests for that new script only if useful and strictly zero-science;
- `docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_REPORT.md`;
- compact CSV/JSON receipts under `docs/evidence/ch5_mp4c_k1a_distance_mapping/` if needed;
- CURRENT status/index/handoff updates only at closeout, and only to record the truthful outcome and next Owner gate.

Do not modify:

- protected MATLAB source/data;
- `capital_network.py` unless a pure engineering defect prevents the task and a correction is demonstrably representation/plumbing-only; if a scientific formula change appears necessary, stop instead;
- legacy `capital_allocation.py`;
- one-turn, C1, firm, wage, labor, HJB, KFE, steady-state, trajectory, annual, IRF or Results code;
- scientific tolerances, grids, calibration or solver settings.

## 9. Scientific/model call budget

Maximum new calls:

- MATLAB model/HJB/firm/steady-state: `0`;
- Python HJB/KFE/household/firm/outer-loop/steady-state/trajectory: `0`;
- GE/annual/shock/IRF/Results: `0`.

Allowed zero-science actions include workbook reads, hashing, mapping, NumPy/pandas arithmetic, calling the isolated pure capital-network algebra, focused pure unit tests, serialization/readback and static code inspection.

Do not relabel a model call as a test. If a required operation would invoke the economic runtime, stop before it.

## 10. Acceptance gates

PASS requires all applicable conditions:

1. protected distance source identity and exact province-label mapping documented;
2. no unresolved missing/duplicate province mapping;
3. raw distance integrity checks reported without silent repair;
4. frozen `D/D_max` matrix reproduced and validated;
5. equal-share limit reproduced at beta-distance zero;
6. static pure-geographic grid diagnostics completed without choosing a final beta;
7. theta provenance established for theta-dependent diagnostics, or a precise partial blocker reported without fabrication;
8. all applicable K1 share/origin/national conservation identities pass at the accepted tolerance;
9. K1B z-score timing/normalization and beta-return interpretation receipt documented without generating returns;
10. no production scientific/runtime source changed;
11. scientific/model call ledger remains zero;
12. report clearly separates source data, mathematical diagnostics, pending Owner decisions and future scientific work.

A truthful `PARTIAL` is acceptable if protected distance/theta data cannot be accessed or mapped. Do not weaken the gates to obtain PASS.

## 11. Deliverable and publication policy

Write the report named above with outcome first, actual worktree/baseline, source identities, mapping receipt, diagnostic tables, checks, changed paths, call ledger and unresolved decisions.

Use one task branch from fresh live main, for example:

`codex/ch5-k1a-distance-mapping-20260911`

or a unique safe suffix if it already exists.

Stage explicit authorized paths only. No `git add .` or `git add -A`.

Create one coherent commit for the Builder deliverables and non-force push the task branch. Do not merge to main. Read back the remote commit/report once and return branch + commit SHA.

Stop after report publication. Do not start a K1 scientific trajectory and do not choose final `beta_distance`, `beta_return`, payoff return or K2 form.

## 12. Required final answer to Reviewer

Return concisely:

- verdict: PASS or PARTIAL with reason;
- actual fetched live-main baseline;
- actual worktree/branch;
- distance workbook SHA, sheet/range, exact mapping status, `D_max`, symmetry residual;
- theta provenance/mapping status;
- key static beta-distance concentration table;
- conservation/equal-share checks;
- K1B beta-return algebra table;
- scientific/model call ledger confirming zero;
- changed paths;
- pushed branch and commit;
- exactly which Owner decisions remain before K1 runtime integration.
