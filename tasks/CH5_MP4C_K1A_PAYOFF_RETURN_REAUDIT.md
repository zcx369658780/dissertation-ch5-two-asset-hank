# CH5 MP4C K1A — payoff-return re-audit before K1B

Date: 2026-09-11.
Task ID: `CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: zero-science source/evidence audit; no model runtime.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Goal

Determine the scientifically defensible payoff-return candidates for the K1 capital network before any K1B runtime integration.

The immediate problem is that K1A symmetric bounded rerun preserved source-used/clipped `ra` as a transitional payoff bridge, while raw firm returns exceeded `.09` in roughly 97% of observed province-turns. This task must explain exactly what raw `ra0`, used/clipped `ra`, and household `rah` mean in the current source, what units/periodicity and numeraire information can actually be established, how clipping distorts cross-province payoff information, and which candidate payoff mappings remain scientifically viable.

This task is evidence preparation only. It must not change the active household payoff law, firm equation, bounds, K1 weights, K1B attractiveness law or any runtime route.

## 2. Mandatory authority reads

Fresh-fetch live `origin/main`. Verify this task is present and active.

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
- `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTANCE.md`
- `docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_REPORT.md`
- accepted compact receipts under `docs/evidence/ch5_mp4c_k1a_equal_share_vs_beta2_symmetric_rerun/`
- current firm / one-turn / K1A adapter source regions that define `ra0`, clipped/used `ra`, `rah`, `rk`, profit component, `delta`, and the return handoff into the next household iteration.

Also read directly relevant historical price/return forensic reports if present. Do not restart unrelated parity, KFE or data gates.

## 3. Scientific boundary

No new scientific/model execution is authorized.

Maximum new calls:

- HJB: 0
- KFE: 0
- household: 0
- firm runtime: 0
- outer-loop/trajectory: 0
- steady state: 0
- MATLAB model: 0
- GE/annual/shock/IRF/Results: 0

Allowed actions include static source inspection, hashing, parsing accepted persisted receipts, arithmetic over already-persisted accepted arrays, source-expression replay from accepted operands, compact tables produced without invoking model runtime, and documentation/tests for the audit script itself.

Do not regenerate `ra0`, `ra`, `rah`, prices, policies or distributions.

## 4. Questions that must be answered

### 4.1 Source semantics and timing

Trace exactly, with source paths/lines:

1. how `rk` is formed;
2. how profit/K enters firm return;
3. where depreciation `delta` enters;
4. exact expression for raw `ra0`;
5. exact clipping rule that produces used `ra`;
6. which return object enters household `rah` under legacy/source-faithful and K1A routes;
7. when that `rah` is consumed by the next household iteration;
8. whether `ra0`, `ra`, `rah`, `rb`, wage and production/accounting variables are intended as annual rates, levels, gross/net rates, or remain ambiguous from source.

Do not infer periodicity from filenames or plotting labels alone. If the source does not establish it, classify it unresolved.

### 4.2 Units / numeraire / scale

Establish what can and cannot be proven about:

- units of Y, Kprivate, GovInv, Ktarget and firm total K;
- MU/NU scaling already frozen for corrected-2018;
- whether `ra0` is dimensionless as a rate from the active formula;
- whether any normalization or price level is implicitly embedded in `mt`, `alpha`, Y/K or other components;
- whether `.02/.09` can be traced to an economic calibration source or only to a numerical safeguard.

If no source-backed economic rationale for `.02/.09` exists, preserve classification `EMPIRICAL_NUMERICAL_SAFEGUARD`.

### 4.3 Clipping distortion in accepted K1A evidence

Using only accepted symmetric-rerun persisted evidence, quantify separately for Path A and B:

- fraction of province-turns clipped at upper/lower bound;
- cross-sectional standard deviation of raw `ra0` vs used `ra` by turn;
- rank correlation / rank preservation raw vs used by turn;
- number of unique used-return values by turn and share exactly at `.09`;
- raw-return percentile table (`p1/p5/p25/p50/p75/p95/p99`) versus used return;
- clipping gap `ra0-ra_used` distribution;
- province-level frequency of upper clipping across 25 turns;
- whether geographic beta=2 materially changes raw-return ranking or clipping distortion relative to equal share.

The purpose is to measure information loss, not to choose a payoff formula by fit.

### 4.4 Decomposition of raw-return pressure

Using persisted K1A receipts and exact source expressions, summarize how much raw `ra0` variation is associated with:

- `rk`;
- profit/K component;
- fixed depreciation;
- total K / Ktarget and Kprivate / Ktarget;
- Y/K where available in accepted evidence.

Report exact algebraic reconstruction residuals. Descriptive correlations are allowed but must not be called causal estimates.

### 4.5 Candidate payoff mappings

Evaluate the following only as candidate contracts, without altering runtime:

A. current clipped/used `ra`;
B. raw net `ra0`;
C. a source-backed transformed/expected return only if an existing source/formula actually supports it;
D. any clearly documented alternative already present in dissertation/source materials.

For each candidate, provide a table covering:

- source fidelity;
- economic interpretability;
- preserves cross-province return dispersion?;
- compatible with current HJB payoff interface without changing model semantics?;
- numerical risk from observed magnitudes;
- whether additional Owner scientific choice is required;
- whether new calibration/estimation would be required.

Do not invent expected-return smoothing, annualization, risk adjustment or normalization absent source authority.

The standardized raw-`ra0` z-score used for future K1B attractiveness is **not** a payoff candidate and must remain separate.

## 5. Counterfactual arithmetic allowed, but no model run

It is allowed to compute static, non-feedback arithmetic receipts such as:

- what household portfolio payoff `S' * ra0` would have been for each already-persisted completed turn if raw `ra0` had replaced clipped `ra`, **holding the persisted S fixed**;
- difference between that static raw-payoff aggregation and accepted clipped-payoff aggregation;
- province/turn distribution of those differences.

Such calculations must be explicitly labeled `STATIC_NO_FEEDBACK_COUNTERFACTUAL`. They are not a trajectory and cannot establish what the model would converge to under raw payoff.

Do not feed these counterfactual returns back into HJB, KFE, firm or outer iteration.

## 6. Required outcome classification

The report must end with one of these evidence-based classifications, or a more precise truthful variant:

1. `CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_PAYOFF_REQUIRES_OWNER_FREEZE`
2. `RAW_RA0_IS_SOURCE_CONSISTENT_PAYOFF_CANDIDATE__RUNTIME_SAFETY_DIAGNOSTIC_REQUIRED_BEFORE_USE`
3. `PAYOFF_RETURN_AUTHORITY_REMAINS_UNRESOLVED__ADDITIONAL_SOURCE_EVIDENCE_REQUIRED`

A classification does not itself authorize changing runtime payoff.

## 7. Next-stage recommendation

Based on the audit, recommend exactly one next Owner/Reviewer gate:

- freeze a payoff-return contract and then design a bounded runtime safety test;
- perform an additional zero-science source/provenance closure;
- or defer payoff redesign and address a more fundamental blocker first.

Do not publish K1B or K2 runtime task from Builder side.

## 8. Allowed tracked changes

Authorized paths are limited to:

- one reproducible audit script under `scripts/` if useful;
- focused zero-science tests for that script if useful;
- `docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_REPORT.md`;
- compact receipts under `docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/`;
- CURRENT status/index/handoff only at truthful closeout.

Do not modify production-science source, accepted K1 formulas, legacy allocator, firm equations, HJB/KFE, labor, C1, bounds, calibration, solver semantics, grids or tolerances.

## 9. Pre-publication checks

Before publication:

1. verify all quantitative audit inputs come from accepted persisted evidence or explicitly cited static source constants;
2. verify no model runtime was imported/executed accidentally;
3. verify raw and used return arrays are mapped to the same province/turn identities;
4. verify static counterfactual payoff uses the already-persisted K1 share matrix for that same completed turn;
5. verify no scientific parameter or bound was changed;
6. run only focused zero-science tests/static checks needed for the audit.

## 10. Publication

Use a fresh isolated worktree/branch from live main. Preserve stale/dirty original checkouts.

Write one coherent report with outcome first, source semantics, unit/periodicity findings, clipping-distortion tables, raw-return decomposition, static no-feedback payoff counterfactual, candidate-payoff comparison, unresolved evidence and next Owner gate.

Stage explicit authorized paths only. No `git add .` or `git add -A`.

Create one coherent commit, non-force push task branch, read back the remote report/commit once, and stop. Do not merge main and do not publish successor task.

Results eligibility remains `FALSE`.

## 11. Required final answer to Reviewer

Return concisely:

- verdict/classification;
- actual live-main baseline;
- worktree/branch/commit;
- source paths/lines for `ra0`, clipping and `rah` timing;
- what is established vs unresolved about units/periodicity/numeraire;
- clipping-distortion summary for both paths;
- raw-return decomposition summary;
- static no-feedback raw-payoff vs clipped-payoff summary;
- candidate payoff-contract comparison;
- scientific/model call ledger confirming zero;
- changed paths;
- exact recommended next Owner/Reviewer gate;
- Results eligibility.
