# Call725 rah=0.07 — KFE dropped-equation and mass-balance attribution

Date: 2026-09-09. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Issuer: ChatGPT Reviewer under standing authority for bounded unchanged-science diagnosis.
Accepted predecessor: e3176e9352b4f7e155c91891a4cabdd517e9e232. Record fresh live main at execution; reviewed publication baseline is f455bdb8904f92a027bf6dc4437c75d900835bbb.
Execution model: gpt-5.6-sol; reasoning effort: medium. No upgrade/downgrade is required. Do not modify global/provider settings. Record an actual model label only if exposed; do not invent runtime verification.

## 1. Question and complete work unit

Using the newly available finite .07 density and its ORIGINAL saved matrices, determine why the row-replaced KFE solve has a small residual while the unmodified stationary equation does not. Localize the discarded-equation residual and close a signed probability-mass ledger between that residual and the independently reconstructed upper-b outward rates. Identify the occupied cells responsible, and the source stages responsible for omitting boundary transitions while retaining diagonal terms.

Implement one read-only extractor/analyzer, relevant synthetic tests, deterministic saved-array arithmetic, a compact coordinate ledger and one report in this task. No model repair or new scientific run. The goal is not to repeat existing counts, manifests, price scans, annual tables, or the D1–D3 repair specification. The new quantity is density-weighted mass flow and its relationship to the row replacement, not another statement that 29 drifts point outward.

Owner retains the original MATLAB-faithful algorithm, a_bar and production parameters. The completed .07 price intervention does not authorize more interventions. Do not change any row/policy/boundary, renormalize or clip density, re-solve the linear problem, move the pin, select a new safe rate, or implement the deferred target. Interpretations such as an implicit source balanced by boundary escape are hypotheses to test, not preassigned findings.

## 2. Narrow reading and workspace

Read AGENTS, rule index, current status, this task and the predecessor REPORT/ACCEPTANCE. Reuse unchanged source certification and applicable safety/Python rules. Read the predecessor evidence decoder/analyzer, especially the two residual formulas, and the frozen export's assemble_source_axis/assemble_source_operator, post-loop assembly and contaminated-row KFE functions. Inspect only relevant protected MATLAB source lines if needed for provenance; no process startup. Do not re-audit the historical scientific gate chain.

Worktree: D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001.
New branch: codex/ch5-call725-rah-0p07-kfe-mass-balance-20260909, from valid fresh main.
New external root: D:\ProjectTemp\ch5-call725-rah-0p07-kfe-mass-balance-20260909-001; use a fresh suffix if occupied.
Read-only .07 source evidence: D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002.
Authoritative manifest SHA256: F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459; resolve its actual filename through the predecessor receipt, not by guessing a version suffix. Use science/index.jsonl and the repository science_capture_index.jsonl to locate only consumed objects. Verify external-versus-Git-copy index identity when paths differ; do not confuse a path difference with different bytes.

Required saved objects: science/binding, hjb_return_before_kfe, kfe_entry, kfe_direct_input, kfe_direct_return, kfe_return and their referenced NPZ arrays; terminal/aggregate only for context or cross-checks. All are reads, not instructions to invoke their source functions. Scoped hash verification of these consumed entries suffices; do not rehash the preceding 13,800 references or rescan whole drives. .09 has no valid density and is not needed for the core ledger. Historical .09 summaries may be cited, not regenerated.
Frozen export blob:9e7dc9556a2b76811e78f89999abecc045886106. Protected MATLAB HJB SHA256:049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE. Baseline source_runtime LF worktree, all prior science roots, original D:\ResearchCode checkout and its untracked files are preserved. No reset/clean/stash/force-push or Zotero/deep-learning-hank/global changes.

## 3. Object identity and conventions before attribution

Use Q for the saved POST-LOOP KFE operator, Qh for the saved last HJB iteration operator, T for the stored unmodified transpose, B for the stored row-replaced system, x for its raw solution, eta for source normalization, g for normalized density, omega=db*da for cell weight, p=omega*g for cell probability, and k for the replaced row. Avoid using A to mean both an asset aggregate and a matrix.
Verify shape/order and exact numerical/sparse-support identities where objects are claimed to be copies: Q is the HJB post-loop object passed to KFE; T=Q.T; saved density_vector equals the F-order flattening of density; g=x/eta and eta=omega*sum(x) reproduce source normalization within the frozen arithmetic rule. State normalization and residual recomputation precision. Do not silently sum duplicates, prune near-zero support or transpose the wrong operator to make an identity pass; preserve stored forms and explicitly distinguish storage-order from mathematical-support checks.
Verify B differs from T in only row k and matches the source's stored row/RHS replacement. Obtain k and rhs from the saved object, check against the source formula, and map k to zero-based/F-order (b,a,z) indices, MATLAB one-based indices and actual grid coordinates. The raw RHS pin such as .007 fixes a raw vector component; it is NOT automatically an injected probability-flow rate.
All reported zeroes, failures and missing objects must reflect actual saved values. On a binding/shape/phase discrepancy, preserve valid diagnostics but stop the dependent inference; do not manufacture input or rerun a model.

## 4. Dropped-equation and boundary mass ledger

Compute from saved objects only:
- e=B*x-f, r=T*g, q=Q*ones. Save all800 rows of r with coordinates; report maxima, signed sum, r[k], largest off-pin residual and its coordinates, and residual concentration at k. Off-pin relation r[i]=e[i]/eta for i!=k must be checked. Report the residual of the replaced normalization equation separately.
- Reproduce prior contaminated raw and unmodified stationary norms/denominators; retain their different units and scaling. The prior ratio .149889... is not a mass-loss percentage. Use ordinary sparse arithmetic and a separately labelled math.fsum accumulation to expose cancellation where useful; no high-precision solve or alternative factorization.
- Reconstruct directional omitted rates ell from SAVED mu_b/mu_a and actual grid spacings only: lower-b max(-mu_b,0)/db; upper-b max(mu_b,0)/db; lower-a max(-mu_a,0)/da; upper-a max(mu_a,0)/da, on their respective boundary faces. Sum directions at corners when computing loss. Keep exact drift signs, and separate tiny arithmetic row-sum discrepancies from these physical boundary contributions.
- Let delta=q+ell. Check the scalar mass identity
  omega*sum(r) = dot(q,p) = -dot(ell,p)+dot(delta,p).
  Report every term, absolute discrepancy, denominator, and frozen-rule status. Include signed, positive-density and negative-density contributions separately without altering x/g/p. Do not assume the roughly1e-16 negative mass explains an O(1) residual; quantify it.
- Compare the candidate balancing source -omega*r[k] with density-weighted escaped mass dot(ell,p), retaining the corrections from off-pin residuals and delta. Derive and test the sign; never infer source strength directly from the raw RHS pin. If non-pin residuals are material, the simple one-source interpretation is not established and must not be forced.

Output a per-cell ledger with indices/coordinates, face labels, g,p,mu, each directional ell, q,delta,r,weighted outward flux and pin indicator. Provide the largest contributors and complete small CSV, not a huge array dump. Report mass on each face and on the union of boundary cells. Face masses overlap at corners; do not sum them as disjoint probabilities. All cell masses and fluxes remain signed; near-zero diagnostics supplement rather than replace exact counts.

## 5. Source attribution and decision-relevant conclusion

Trace the concrete implicated upper-b source assembly: which stored drift becomes an outward rate, where an outside-grid offdiagonal is omitted, and whether its diagonal contribution remains. Use source lines and saved arithmetic; do not rerun the policy selector, initializer or assembler as a hidden model evaluation. The existing report already establishes q+ell near zero, so focus on density-weighted effect and pin-row localization rather than repeating that finding as new work.

Clearly separate Q from Qh: Q's nonnegative offdiagonals do not remove the21 negative offdiagonals of Qh. Qh must not be interpreted as a valid probability generator or substituted into the mass ledger. Do not claim full nonlinear HJB validity from its stopping statistic.

Answer, with evidence: (a) does the published diagnostic use the correct original transpose/order/normalization; (b) is most or all material stationarity failure the equation discarded by row replacement; (c) does its signed source balance actual density-weighted upper-b escape; (d) which occupied cells account for it; (e) which precise numerical statement remains invalid despite solver return. A confirmed source/escape balance is an interpretation of the finite-box algebra, NOT a newly adopted economic entry/exit law.
Do not claim no stationary distribution can exist for every possible density from failure of this one g alone. No eigenvalue/rank/nullspace computation is authorized or needed. Do not propose changing rho/rah/a_bar or pinning rows merely to make residuals smaller. Finish with the smallest necessary next scientific decision or evidence gap, referring to existing specifications rather than writing them again. No deferred repair is approved by this task.

## 6. Budget and checks

NEW initializer/root/HJB/KFE/direct/iterative/eigen/optimization/condition solves, policy/evaluator calls, firm/one-turn/controller/GE/annual/dynamics/IRF/Results calls and MATLAB startups: ALL0. Scientific retries0. No ODE/forward-distribution stepping or re-solution of either original or modified systems. Python saved-array postprocessing, matrix-vector products, source reading and synthetic hand-constructed IO/identity tests are allowed and are not model runs.
Complete task<=90 minutes. No repeated full-history hashing or broad regressions. Ordinary decoder/path/report/test fixes may repeat within scope; preserve failures, use existing outputs, and do not call models to replace missing data.
Relevant tests must exercise the ACTUAL new ledger functions: F-order pin mapping, exact B/T row difference, raw-to-density normalization, conservative source-free hand example and nonconservative hand example where a fixed normalized vector has an off-pin-balanced source/escape residual, directional corner accounting, signed small negative-density contribution, sparse orientation mismatch detection, and no import-time science/solver calls. Supply analytical vectors directly rather than solving synthetic linear systems. Keep original frozen identity rule abs(x-y)<=128*eps64*max(1,abs(x),abs(y)); never relax it after results. Report any failure and arithmetic scale instead of silently changing tolerance.

## 7. Allowed paths and publication

Allowed repository writes only:
- validators/multi_province/call725_kfe_mass_balance/
- tests/test_mp4c_call725_kfe_mass_balance.py
- reports/call725_kfe_mass_balance_20260909/ (compact JSON/CSV/Markdown, logs, receipts)
- docs/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION_REPORT.md

Keep all predecessor raw files and production/export/helper code unchanged. One report, compact summary, coordinate/flux ledger, source-line map, actual zero-new-science ledger, test logs and one finite scoped manifest/readback suffice. Exclude the manifest and its final readback from self-hashing. Preserve raw Windows bytes versus repository LF identity; do not upload private data or large arrays.
Report independent fields: diagnostic_completion=COMPLETE/PARTIAL_EVIDENCE, identity_checks, pin_residual_localization, signed_mass_balance, source_escape_interpretation=SUPPORTED/NOT_SUPPORTED/UNRESOLVED, remaining_scientific_decision, Results_eligible=FALSE. Do not label MODEL_PASS or production repair.
Explicitly stage allowed paths, commit and non-force push branch, verify remote SHA. Return findings, consumed evidence scope, true invocation counts, test/manifest receipt, report/evidence path and commit. Builder does not merge main, run a successor or change models/provider configuration.
