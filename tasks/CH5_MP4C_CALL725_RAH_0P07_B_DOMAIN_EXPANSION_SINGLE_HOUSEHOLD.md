# Call725 rah=0.07 — single-household upper-b domain expansion diagnostic

Date: 2026-09-09. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Issuer: ChatGPT Reviewer. Owner explicitly approved a SMALL-SCALE liquid-asset-domain diagnostic and explicitly prohibited jumping to a multi-province run.
Execution model preference: gpt-5.6-sol / medium. Do not modify provider/global settings; do not claim the host actually used that label unless exposed.

## 1. Scientific question and scope

Use the already accepted 2018 Anhui call725 rah=0.07 single-household input as the only economic state. Test whether the previously observed upper-b truncation/source-escape problem materially changes when the liquid-asset domain is extended while preserving the original liquid-grid resolution and all non-grid economics.

This is ONE new household diagnostic, not a multi-province, firm, GE, annual, calibration, policy, IRF or production-grid change. Do not run any other province or rate. Do not search over bmax values. Do not change a_bar, rah, ramax, equations, boundary law, selector, solver, tolerance or HJB max iterations.

The original production household grid supplied by Owner is:
- I=20, bmin=-2, bmax=5;
- J=20, amin=0, amax=10;
- Nz=2, zmin=0.8, zmax=1.3.
The accepted rah=.07 baseline used this 20x20x2 grid and is read-only.

The sole new grid intervention is:
- b domain extended from [-2,5] to approximately [-2,12];
- preserve db exactly from the captured baseline: db = baseline_b[1]-baseline_b[0] = 7/19 mathematically;
- use I=39 so there are 19 additional upper-b nodes;
- preserve the first 20 b nodes byte-for-byte from the captured baseline and append 19 nodes at that same binary64 spacing; record the actual final binary64 endpoint and its deviation from mathematical 12;
- keep a and z arrays byte-for-byte identical to the baseline, hence J=20, amin=0, amax=10, Nz=2, zmin=.8, zmax=1.3.

This nested-grid construction is a diagnostic device to isolate domain extension from coarsening or common-node roundoff. It does NOT change the production grid constructor and is not a proposal to adopt I=39/bmax=12 in the final model.

## 2. Authority and required reads

Start from fresh live main. Read AGENTS.md, project_rules/PROJECT_RULE_INDEX_CURRENT.md, docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md, this task, and the relevant local-safety/Python rules.
Read predecessor evidence:
- docs/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_{REPORT,ACCEPTANCE}.md;
- docs/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION_{REPORT,ACCEPTANCE}.md;
- reports/call725_rah_0p07_sensitivity_20260908/{intervention_binding,operator_diagnostics,distribution_diagnostics,manifest_readback}.json;
- only the needed source contracts for native initialization, post-loop household adapter, frozen export, and evidence decoding.
Do not re-audit the 725-call prefix or historical annual tables.

Repository work directory: D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001.
Suggested branch: codex/ch5-call725-rah-0p07-b-domain-expansion-20260909.
New external evidence root: D:\ProjectTemp\ch5-call725-rah-0p07-b-domain-expansion-20260909-001; if occupied, use a fresh suffix.
Read-only rah=.07 baseline root: D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002.
Baseline manifest SHA256: F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459.
Use the actual science index/manifest bindings; do not reconstruct scientific inputs from chat numbers.

Frozen scientific source anchors remain:
- exports/matlab_faithful_two_asset_ha.py blob 9e7dc9556a2b76811e78f89999abecc045886106;
- protected MATLAB HANK_2ASSETS_HJB.m SHA256 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE;
- native initializer, post-loop adapter and worker-mapping blobs must equal the accepted rah=.07 predecessor identities before science.

## 3. Exact intervention binding

Load the saved call725 rah=.07 household state/parameters and grid from accepted evidence. Create an independent diagnostic copy.

Economic/state fields must be unchanged from the accepted .07 run, including rah/r_a=.07, carried firm ra=.09, production ramax=.09, wage, rb, rb_gap, tau, Tt, rho, gamma, phi, chi0, chi1, a_bar, migration/labor objects, Delta=1000, convergence tolerance=1e-7, maxit=100 and drift tolerance=1e-12.

Only the grid object may differ, and only its liquid dimension:
- baseline b first 20 elements exact copy;
- 19 appended upper nodes at the same captured db;
- a exact copy;
- z exact copy;
- switch_matrix exact copy;
- resulting shape (39,20,2), state_count=1560.
Persist a machine-readable grid diff and common-node identity check BEFORE scientific entry.

The source KFE pin formula depends on state_count. Do not freeze the old pin. With 1560 states, source formula floor(.37*N)-1 should produce k=576; verify from source and record its F-order indices and physical coordinates. This automatic pin movement is a companion numerical change induced by state_count, so KFE-density/aggregate changes must NOT be described as a pure fixed-pin bmax effect.

## 4. One scientific execution

Regenerate the native initializer ONCE on the expanded grid using the unchanged original initializer and the same rah=.07 state. Do not warm-start from the old 20-point V0/l0 and do not interpolate the old final value function.

Then invoke the unchanged original post-loop household adapter ONCE on this expanded grid. Preserve original behavior: if HJB returns converged=False, the adapter may still enter its original KFE path; do not add a convergence gate or fallback. Persist the native initialization, complete HJB return before KFE, KFE direct input/raw return, KFE return/aggregate if reached, warnings, exception and counters. No scientific restart after native initialization begins.

No MATLAB call. No production source edit. No alternative boundary treatment. No added source term. No pin relocation beyond the source formula. No second bmax. No 500-step extension.

## 5. Hard new-call budget

One Python scientific process/worker with OMP/MKL/OPENBLAS/NUMEXPR threads all 1.

| Category | Maximum new calls |
| --- | ---: |
| Native household initialization | 1 |
| Original labor-root entries | 1560 |
| Nested brentq entries | 1560 |
| Household adapter / HJB | 1 each |
| HJB updates / direct solves | 100 |
| KFE / original direct solve | 1 each if naturally reached |
| Aggregate | 1 if naturally reached |
| Baseline bmax=5 rah=.07 rerun | 0 |
| Other bmax/rate/province | 0 |
| Firm/one-turn/controller/GE/annual/R-PLM/dynamic/IRF/Results | 0 |
| MATLAB startup | 0 |
| Extra policy/evaluator/assembler/selector/diagnostic solves | 0 |

Count failed entries. Scientific wall time <=15 minutes; whole task <=90 minutes. One external launch retry is allowed only with proof of zero scientific entry and a repaired import/path/environment fault. Scientific nonconvergence or an unfavorable diagnostic is not a retry reason.

## 6. Predefined diagnostics and interpretation

Primary comparison is old accepted b-domain versus the one expanded-domain household. Reuse the old .07 results; do not recompute them.

### A. Grid/initializer controls
- prove original 20 b nodes are exact prefix of the new grid;
- prove a/z/switch/economic inputs are exact;
- report actual db and final b endpoint;
- compare new versus old native V0/l0 ONLY on the shared 20x20x2 subgrid; equality/near-equality here is an implementation diagnostic, not a requirement to force by editing formulas.

### B. HJB
Report converged flag, iteration count/statistic, finite arrays, controls/drifts, labels, last-iteration Qh negative-offdiagonal count/minimum, row sums and scale. Compare old and new outputs on the common b<=5 subgrid descriptively; do not apply same-input parity semantics across different domains.

### C. Post-loop boundary/truncation
Using saved final drifts and post-loop Q only:
- report omitted/outward rates on all four faces;
- especially new upper-b face at the actual b≈12 endpoint: exact outward-cell count, max/sum rate;
- compare to old upper-b b=5 count=29/max≈4.00987 only as accepted predecessor context;
- compute Q*1 row-sum relation to omitted rates using the frozen arithmetic rule;
- distinguish Q from Qh.

### D. KFE/distribution if returned
Do not assume the row-replaced density is valid merely because it is finite.
- verify original T=Q.T, row-replaced system, pin location and normalization;
- report unmodified ||Tg||inf and its scale ratio separately from contaminated Bx-f residual;
- compute density-weighted boundary escape and the pin/source mass ledger using saved arrays only;
- report total signed mass in old region b<=5, added tail b>5, and top face b=bmax; report negative density count/mass without clipping;
- report whether source-free stationarity Tg≈0 passes the pre-existing 128-eps componentwise zero comparison; do not invent a looser tolerance.

Because the source pin moves with state_count when Q is nonconservative, KFE density and aggregate comparisons are SECONDARY and potentially pin-dependent. State this prominently unless source-free stationarity is actually satisfied. Aggregates C,L,A,B,A+B may be reported only as diagnostic integrals.

### E. Decision labels
Return independent fields:
- diagnostic_completion;
- exact_grid_intervention_binding;
- HJB_status;
- expanded_upper_b_truncation_status;
- source_free_stationarity_status;
- pin_companion_change;
- distribution_tail_diagnostics;
- aggregate_diagnostics;
- truncation_sensitivity_conclusion;
- Results_eligible=false.

Allowed conclusions include, for example, EXPANSION_REDUCES_BOUNDARY_PRESSURE, EXPANSION_DOES_NOT_REMOVE_BOUNDARY_PRESSURE, HJB_FAILURE_PERSISTS, or PARTIAL_EVIDENCE. Do not label MODEL_PASS. One expanded grid point cannot establish grid convergence or production adoption.

A reduction in boundary mass/leak supports that the original bmax=5 truncation is influential at this one household. Persistence of material upper-bound pressure suggests simple domain extension is insufficient. Neither result authorizes changing production bmax, a_bar, ramax, boundary law, pin/source economics, or multi-province runs.

## 7. Tests, allowed writes and delivery

Relevant synthetic tests only: nested b-grid exact prefix and spacing, input diff limited to grid-liquid dimension, new state-count/pin mapping, budget counters, native initializer single delegation, no warm start/interpolation, save-before-KFE, shared-subgrid slicing/order, directional boundary accounting, mass-ledger formulas, and no import-time scientific/solver calls. Synthetic tests must not invoke real roots/HJB/KFE.

Allowed repository writes only:
- validators/multi_province/call725_b_domain_expansion/
- tests/test_mp4c_call725_b_domain_expansion.py
- reports/call725_b_domain_expansion_20260909/
- docs/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_REPORT.md

Raw large arrays stay in the external evidence root. Keep predecessor evidence immutable. Preserve actual failed/final test logs. Create one finite scoped manifest/readback covering consumed baseline objects and new relevant outputs, not itself/final receipt. Stage only allowed paths, commit, non-force push dedicated branch and verify remote SHA. Do not merge main or launch a successor.

Return the headline HJB result, upper-b rate/mass result, source-free stationarity result, pin coordinate, tail mass, true call ledger, tests/manifest, report/evidence paths and commit. Results eligibility remains FALSE.
