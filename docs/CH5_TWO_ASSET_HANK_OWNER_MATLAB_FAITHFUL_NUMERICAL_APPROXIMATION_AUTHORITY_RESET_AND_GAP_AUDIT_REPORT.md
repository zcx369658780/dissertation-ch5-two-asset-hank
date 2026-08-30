# Chapter 5 Two-Asset HANK Owner MATLAB-faithful numerical approximation authority reset and gap audit report

## Terminal classification

`MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_PASS`

All Owner-frozen faithful contracts were mapped to exact designated MATLAB and current Python locations sufficiently to issue bounded implementation tasks. This was a static audit only: no production scientific source/test or MATLAB file was modified, and no D1/D2/D3, HJB, KFE, steady-state, asset-tail, transition, IRF, dynamics, calibration, or Results execution occurred.

## Live authority and identities

- Live start `origin/main`: `1a1c7a58d71b971657f7bb92039bb972ed5c9c43`.
- Branch/HEAD after fast-forward: `codex/ch5-adjustment-boundary-redesign` / `1a1c7a58d71b971657f7bb92039bb972ed5c9c43`.
- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Python production root: `src/ch5_two_asset_hank/`.
- Designated MATLAB root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.
- Final `origin/main` immediately before report publication: `1a1c7a58d71b971657f7bb92039bb972ed5c9c43`; publication commit is recorded by push/read-back and final handoff.

Designated hashes all matched:

| MATLAB source | SHA-256 |
|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |

The directly relevant grid setup is in `multi_prov_HANK_12sts.m`: `grid.bmin=-2` at line 36 and `grid.amin=0` at line 40. `HANK_mp_1turn.m:15` calls the designated `HANK_2ASSETS_HJB` with those grids.

## Owner authority reset

The primary reconstruction marker is now frozen as:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Supporting frozen markers:

- `MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`;
- `MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`;
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_SOLVE_IS_REQUIRED`.

The adjustment-cost `max(a,a_bar)` is frozen specifically as a numerical denominator floor. It is not a general instruction to replace every FOC occurrence of `a` with the floor. Illiquid assets satisfy `a>=0`; liquid assets may be negative for borrowing.

Prior P1-P5, D1, and post-P5 D2 evidence is preserved and reclassified as:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

Historical P5 scope is now:

`P5_ACCEPTED_FOR_CORRECTED_EQUATION_TRACK_NOT_FINAL_MATLAB_FAITHFUL_PARITY`

No historical report or evidence was deleted or rewritten. The prior wrapper-aware D2 route was not resumed.

## MATLAB-faithful gap matrix

| # | Object | Exact MATLAB source | Current Python source | Classification | Required production mutation | Test treatment |
|---:|---|---|---|---|---|---|
| 1 | Cost denominator floor | `HANK3_cost.m:24`: `chi0.*abs(d) + chi1.*d.^2/2.*(max(a,a_bar)).^(-1)` | `economics.py:10-13`: `scale=np.maximum(a,params.a_bar)` and quadratic term `/scale` | `ALIGNED` | None to `adjustment_cost`; preserve floor only in denominator | Retain cost-floor assertions; separate them from the currently coupled FOC assertion |
| 2 | Transfer FOC below `a_bar` and at `a=0` | `HANK3_FOC.m:20`: threshold expression multiplied by bare `a/chi1`; called with `aaah` at `HANK_2ASSETS_HJB.m:137-140` | `economics.py:16-21`: `max(a,params.a_bar)*threshold/chi_1`; consumed by `policies.py:136,526` | `FAITHFUL_GAP` | Change faithful production `transfer_candidate` scaling to bare `a`; audit max-scale shadow/KKT reconstructions in `policies.py:247,300,365,429,448` and `boundaries.py:85,146` in the HJB parity gate rather than mechanically replacing them | Split `test_adjustment_cost_and_foc_share_frozen_max_scale`; faithful assertions must cover `0<a<a_bar` and exact zero at `a=0`; retain old max-scale behavior only as corrected-track reference evidence |
| 3 | `raah` taper and drift/operator entry | `HANK_2ASSETS_HJB.m:81`: `raah=rah.*(1-0.1*(ahmax./ah).^(-9))`; broadcast into `Rah` at 82-87; illiquid drift uses `Rah.*aaah` at 193-194 | `economics.py:64`: `mu_a=inputs.r_a*a+transfer`; `HouseholdInputs.r_a` is scalar; `generator.py:48` consumes resulting `policy.mu_a` | `FAITHFUL_GAP` | Add grid-aware faithful effective illiquid return using the exact coefficient/exponent/`a_max/a`; feed it into policy illiquid drift before `G_a` construction; preserve constant-return implementation as corrected-track reference helper/fixture | Add taper endpoint/interior equivalence tests, `a=0` finite-limit handling consistent with MATLAB grid evaluation, drift integration tests, and generator-rate tests; reclassify constant-`r_a` parity fixtures |
| 4 | Asset lower bounds | `multi_prov_HANK_12sts.m:36,40`: `bmin=-2`, `amin=0`; `HANK_2ASSETS_HJB.m:46-49` constructs both grids; borrowing aggregates use `bbb<0` at 349-350,367-368 | `contracts.py:33-36`: requires `a[0]==0`, requires `b[0]==b_bar` but does not require nonnegative `b`; negative-`b` fixtures in `test_indexing_and_derivatives.py` and `test_generators_and_kfe_contract.py` | `ALIGNED` | None; do not add `b>=0` | Retain explicit negative-liquid-grid and zero-illiquid-lower-bound tests; add a faithful domain regression if implementation tasks introduce new grid factories |
| 5 | Stationary KFE linear system | `HANK_2ASSETS_HJB.m:333-340`: `A=BB+AAH+Bswitch`, `AT=A'`, full `M x M` row-contaminated solve `AT\vec` | `kfe.py:46,94-116`: transposed shared generator, recurrent-class detection, restricted-class system, last-row unit normalization and `np.linalg.solve` | `FAITHFUL_GAP` | Implement a production faithful full-transpose contaminated-row solver; retain shared-generator construction, but do not restrict to recurrent class or substitute nullspace methods | Add exact small-matrix contaminated-row solve tests; move recurrent-class solver expectations to explicitly named clean/reference diagnostics tests |
| 6 | Contaminated-row index | `HANK_2ASSETS_HJB.m:334,337,339`: `M=I*J*Nz`, `iFix=floor(0.37*M)`, replace row `iFix` by unit row | No equivalent; `kfe.py:108-109` replaces the last row of a restricted recurrent system | `FAITHFUL_GAP` | Implement MATLAB one-based rule faithfully when mapping to Python zero-based storage: MATLAB `iFix=floor(0.37*M)` corresponds to Python row index `iFix-1`; validate `iFix>=1` for faithful supported grids | Add index conversion tests over representative designated sizes and assert exact unit-row replacement |
| 7 | Contaminated-row RHS | `HANK_2ASSETS_HJB.m:336,338`: zero vector with `vec(iFix)=0.007` | `kfe.py:107,109`: restricted zero RHS with terminal value `1.0` | `FAITHFUL_GAP` | Use exact full-system RHS value `0.007` at the faithful contaminated row; no rescaling before solve | Add exact RHS construction and scale-invariance-after-density-normalization tests; keep old `1.0` clean solver behavior only under reference API tests |
| 8 | Stationary normalization measure | `HANK_2ASSETS_HJB.m:341-345`: divide density by `g_stacked'*ones(M,1)*db*dah`; productivity states are already jointly represented through `Bswitch`, with no explicit `dz`/trapezoid factor | `kfe.py:115-135`: solves probability mass normalized by `sum(mass)=1`, then `density=mass/cell_weights`; `steady_state.py:241-248` uses trapezoidal `a*b*z` weights | `FAITHFUL_GAP` | Faithful path must solve for stacked density and normalize with uniform `db*dah` exactly; do not apply productivity quadrature or endpoint trapezoidal half weights in the faithful MATLAB parity path | Add exact `db*dah` density-integral tests and aggregate checks; retain general cell-weight/mass accounting as clean/reference diagnostics, not faithful-production acceptance |
| 9 | Clean/reference diagnostics | MATLAB production directly applies contaminated-row solve; it does not use recurrent-class selection, left-nullity veto, unmodified stationary residual veto, or pin-free nullspace solver in this path | `kfe.py:49-103,118-131`; `steady_state.py:251-267,333-346`; `diagnostics.py:11-37` | `DIAGNOSTIC_ONLY_DIFFERENCE` | Retain these tools as explicitly diagnostic/reference APIs; remove their ability to replace or automatically veto a MATLAB-faithful contaminated-row production result | Rename/split API and acceptance labels so diagnostics remain visible; tests for SCC/nullity/residual/nonnegativity remain diagnostic tests, not faithful solver equivalence gates |
| 10 | Corrected-track tests/fixtures | MATLAB faithful contracts above use bare-`a`, tapered return, and contaminated-row density | `test_economics_boundaries.py:14-18`; `test_kfe_operator.py:52-119`; `test_r4_steady_state.py:33-39`; `test_r4_policy_fixture_resolution.py`; `test_r4_truncation_acceptance_contract.py`; `test_r2_rerun_evidence.py` | `DIAGNOSTIC_ONLY_DIFFERENCE` for retained historical fixtures; `FAITHFUL_GAP` for missing faithful tests | Do not delete fixtures; introduce explicit faithful-vs-corrected track naming and route-specific entry points | Split mixed primitive test; retain D1/P2/R2/R4 fixtures as corrected-track regression evidence; add new faithful primitive/taper/HJB/KFE/steady-state fixtures and prevent corrected-track tests from claiming final faithful acceptance |

## Detailed affected Python surfaces

### Household primitives and policy selection

- `economics.adjustment_cost`: already faithful for the denominator floor; do not change its scale.
- `economics.transfer_candidate`: direct faithful gap; bare `a` is required.
- `economics.asset_drifts`: currently uses scalar constant `inputs.r_a`; it must receive the faithful effective illiquid return in the grid-aware route.
- `policies._controls_from_shadow_values` and candidate enumeration call `transfer_candidate`, so the primitive change propagates to ordinary candidates.
- `policies._interior_zero_illiquid_controls`, `_upper_a_lower_b_controls`, `_upper_a_interior_b_controls`, `_dual_upper_corner_controls`, `_budget_roots`, and `boundaries.compute_multipliers/kkt_residuals` contain max-scale algebra from the corrected track. The Owner contract forbids blindly changing every such occurrence. They require a bounded faithful HJB/policy derivation-and-parity task after the primitive is split, with corrected-track versions retained for regression.

### Return taper and operator

- `HouseholdInputs.r_a` is currently a scalar contract.
- `asset_drifts` computes `mu_a=r_a*a+d`.
- `policies.select_policy` builds `mu_a` through those primitives.
- `generator.build_operator` correctly builds `G_a` from `policy.mu_a`; the generator need not invent the taper itself. The dependency should be injected upstream into the faithful illiquid drift so the operator receives the MATLAB-faithful drift.
- `generator._asset_generator` is aligned as a directional drift-to-rate constructor and should not be rewritten merely to add the taper.

### KFE and steady state

- `kfe.build_forward_operator` correctly transposes the backward generator and can be reused.
- `kfe.solve_stationary_kfe` is currently a clean recurrent-class probability-mass solver and is not faithful production authority.
- `kfe_contract.KFEInput` already carries the shared generator and weights, but the faithful solver needs explicit uniform `db`, `dah`, and designated dimensions/indexing or an equivalent grid-derived contract.
- `steady_state.run_frozen_r4_steady_state` performs SCC, recurrent-support, left-nullity, trapezoidal-weight, strict residual, and nonnegativity gates. Preserve them as corrected/reference diagnostics; they cannot remain the faithful production route's automatic vetoes.

## Items aligned and not to be changed

- The adjustment-cost denominator floor in `economics.adjustment_cost`.
- Economic lower bound `a=0` and the ability for `b` to be negative in `GridSpec`.
- Shared backward generator composition and transpose interface as construction plumbing.
- Directional grid-generator logic, provided it receives faithful drift inputs.
- Historical corrected-equation artifacts and diagnostics, which remain useful reference evidence.
- MATLAB coefficient `0.1`, exponent `-9`, and `ahmax/ah` construction.
- MATLAB contaminated row rule, RHS `0.007`, and `db*dah` normalization.

## Owner clarification status

No required frozen contract remains unresolved. `OWNER_CLARIFICATION_REQUIRED`: none.

The MATLAB line `tempMat = Rah.*raah + Rb.*bbb + Tt` at `HANK_2ASSETS_HJB.m:90` appears separate from the actual illiquid drift entries `Rah.*aaah` at lines 193-194. This audit does not reinterpret or repair that auxiliary minimum-income calculation; faithful HJB implementation should preserve or isolate it according to its actual use, but it does not block the Owner contracts audited here.

## Ordered implementation task chain

1. **Faithful household primitives.** Add an explicit faithful track/API: preserve cost denominator floor, change faithful transfer candidate to bare `a`, add below-`a_bar` and `a=0` tests, and retain corrected-track helper/tests under unambiguous names. No HJB run yet.
2. **Faithful illiquid-return taper.** Implement exact `r_a(a)=rah*(1-0.1*(a_max/a)^(-9))` on the designated grid, including the MATLAB-consistent lower-grid limit, and inject it into `mu_a` before operator construction. Test pointwise taper and generator drift plumbing without full HJB.
3. **Faithful HJB/policy construction.** Audit and split max-scale shadow/KKT/corner logic against `HANK_2ASSETS_HJB.m:116-232`; establish bounded state/candidate parity using the faithful primitive and taper. Corrected-track policy fixtures remain regression-only.
4. **Faithful contaminated-row KFE.** Implement full `A.T` row contamination at Python index `floor(0.37*M)-1`, RHS `0.007`, direct linear solve, and exact `db*dah` density normalization. Keep recurrent-class/nullity/residual/nonnegativity analysis as non-vetoing diagnostics.
5. **Faithful steady-state distribution and aggregates.** Compare density, mass integrals, borrowing, illiquid holdings, labor, consumption, and other source-backed aggregates against designated MATLAB with identical grids/operators. Do not substitute trapezoidal productivity weights in the faithful path.
6. **Faithful dynamics gate.** Only after faithful household, HJB, KFE, steady-state distribution, and aggregate parity are accepted may a new Owner task authorize transition/IRF/dynamics work.

Dependencies require this order: the HJB operator depends on faithful transfer/taper drifts; the contaminated-row KFE consumes that exact operator; steady-state aggregates consume its density; dynamics consumes the accepted faithful steady state.

## Closeout and acceptance level

- Production Python source mutation: none.
- Production tests mutation: none.
- MATLAB mutation: none.
- Scientific execution: none.
- Prior D2 comparator chain resumed: no.
- Repository change before closeout: exactly this report, with explicit-path staging only.
- Acceptance level: Owner authority reset frozen and static faithful-gap audit complete; no faithful implementation or numerical parity is yet accepted.

Exact recommended next gate: issue only the first bounded implementation task for faithful household numerical primitives. It should introduce an explicit production-faithful bare-`a` transfer FOC while preserving the aligned cost denominator floor, split/reclassify corrected-track tests without deleting them, add exact `a=0` and `0<a<a_bar` regressions, and stop before taper integration, HJB, KFE, steady state, or dynamics.
