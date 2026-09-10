# Chapter 5 MP4C multi-province steady-state calibration and initialization redesign specification

Date: 2026-09-10

## Required answers

1. **Legacy unit inconsistencies and unexplained multipliers.** `load_GDPdata.m:93-104` multiplies GDP in 亿元 and PIM capital documented in 万元 by the same `GDP_multiplier=1000`, while population in 万人 is multiplied by `100`. GDP therefore becomes a coherent “10万元” aggregate count, but capital is larger than the same-money-unit conversion by a factor of 10,000. The household-to-macro capital bridge is `HANK_mp_1turn.m:31,36`: per-household illiquid `At` is multiplied by `N` and allocated as `Kt_supply`; the implicit bridge coefficient is one and has no source-backed unit definition. `HANK_firm.m:95` also mixes aggregate firm/tax terms with household `AtTax` and `Tt` without the population multiplication used elsewhere.
2. **Successor unit contract.** Use one aggregate money unit `MU = 10万元`, one population unit `NU = 100 persons`, and one per-NU flow/stock unit `MU/NU`. Convert GDP in 亿元 by `×1000`, PIM capital in 万元 by `÷10` (equivalently capital in 亿元 by `×1000`), and population in 万人 by `×100`. Household `a/b/C/w/T/AtTax` must be explicitly declared in `MU/NU`; aggregate household stocks/flows multiply by `N_model` exactly once. This is a proposed correction, not production authority, because the current `a/b` grid has no source-backed currency normalization.
3. **Original alpha behavior.** The active `reg_method=0` route reads the last scalar from each R coefficient sheet and stores it directly (`load_GDPdata.m:113-137`); it has no clipping and no later steady-state alpha update. The only bounds are commented-out `.3/.8` lines in the inactive `reg_method=1` block (`:173-177`), and those lines target coefficient index 2 although that design matrix puts log capital at index 3. The Owner-frozen successor is separate: save `alpha_raw`, use `[.2,.8]`, save `alpha_used=clip(alpha_raw)`, flag/reason, and never tune it in the outer loop. Current `0.7380939146868483` maps bit-for-bit to itself.
4. **Legacy arbitrary starts.** `ra=.09`, `rah=.09`, `wjt=.6`, household `w=20`, plus `At=2`, `Bt=1`, `Lt=.8`, `Ct=4`, `Zt=6`, `GovInv=1000` are generic starts in `multi_prov_HANK_12sts.m:85-108`. The equilibrium initializer overwrites alpha, Zt, Kt/Kt0, N, Lt, Yt/Yt0 and GovInv before the first household solve (`mpHANK_equilibrium_2000.m:22-43`), but it does not overwrite `ra/rah/wjt/w/At/Bt/Ct`.
5. **Source-consistent initialization order.** Bind the chosen Owner-approved 2018 PIM route and same-year Y/N; convert once; set `alpha_raw/used`; compute same-year `Zt0=Y0/(Kt0^alpha Lt0^(1-alpha))`; set zero-change firm bookkeeping (`Kt_1=Kt0`, `Lt_1=Lt0`, `Yt_1=Y0`, `Zt_1=Zt0`, `pit_1=pit`) and derive raw `wjt0/ra0` from the existing firm equations; retain raw values and apply unchanged safety bounds. Then compute `rah0` and household `w0` through the existing cross-province return and wage maps. The latter two require a future bounded initialization-only probe; no arbitrary fallback is authorized.
6. **Existing damping.** Only the convergence reference is convexly damped: `tKNratio=0.6*KNratio+0.4*tKNratio` (`HANK_mp_1eq.m:60-62`). Zt is reset directly; GovInv takes undamped multiplicative `.9/1.1` steps. There is no current damping of `w`, `rah`, firm `wjt`, or firm `ra`.
7. **Proposed w/rah damping.** Preserve firm raw-price calculation and tax compensation, and always aggregate from clipped rather than pre-clip firm prices. Wage can then follow `clip current wjt → aggregate → damp`. Rah requires an explicit timing choice: source-faithful `prior clipped ra → aggregate before current firm → damp` preserves the observed extra propagation lag; canonical `clip current ra → aggregate after firm → damp` removes one lag. Use the source-faithful order as the minimal baseline and register the canonical order as a separate future candidate; do not silently conflate them. In either case, damp only the value passed to a later household: `x_next=(1-lambda_x)x_old+lambda_x*x_composite_raw`, with preregistered `lambda ∈ {1,.5,.25}`.
8. **Single-loop staging.** Keep one ordered outer loop. Stage A runs household/allocation/firm updates and price damping with calibration frozen. Stage B enables the existing Zt and GovInv controllers after pre-registered proximity gates. Stage C freezes Zt/GovInv and continues the same loop to the unchanged final convergence predicate; material destabilization reopens Stage B under hysteresis, rather than starting a nested steady state.
9. **Hysteresis candidates.** Pre-register `epsilon_enter ∈ {.10,.05,.02}`, `epsilon_exit=2*epsilon_enter`, and `min_consecutive_turns ∈ {2,3,5}` for both max K/N-reference and max Y/Y_prev gaps. Stage-C candidates use source GDP tolerance `.01`, zero GovInv-trigger provinces, relative controller changes in `{1e-3,1e-4}`, and `{3,5}` stable turns. Final tolerance remains `1e-9`; these are future validation candidates only.
10. **Choices remaining.** Owner/Reviewer must select the production PIM source route; authorize the common monetary/population normalization and explicit household asset bridge coefficient; resolve wage/transfer/tax normalization; decide whether firm depreciation `.025` remains distinct from PIM depreciation `.096`; choose source-lagged versus after-firm rah timing; select lambda and hysteresis grids after bounded validation; and decide whether GovInv receives additional damping. Exact `rah0/w0` require the approved initialization-only probe.
11. **Call confirmation.** MATLAB/HANK/HJB/KFE, Python household/HJB/KFE, firm, wage, migration, capital allocation, outer turn, steady state, GE, annual, IRF, Results, and scientific root/direct/iterative/eigen calls were all exactly zero.

## Verdict

`STEADY_STATE_REDESIGN_SPEC_PARTIAL__OWNER_OR_UNIT_DECISION_REMAINS`

The source map, alpha correction, ordered-update contract, staged calibration, and preregistered numerical candidates are ready. The package is PARTIAL rather than PASS because the protected source does not define the currency value of one household `a/b` grid unit, current wage bounds are not reconciled to the 2018 macro flow unit, and the accepted canonical-investment versus raw-NBS-GFCF production capital route remains an Owner scientific choice. No conversion was chosen to improve convergence.

## Authority and classification

The active authority is `tasks/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md` on fresh live `origin/main=5c7f49bb2ed8445f85b0c97c60a6727ecd7697c9`. The rule index activates this task; the more general status and handoff files still say no active task and are treated as stale, narrower evidence rather than execution authority.

The four required classifications are used throughout the package:

- `UNCHANGED_SOURCE_LOGIC`: equation/order retained exactly.
- `OWNER_FROZEN_CORRECTION`: explicit Owner decision, including correct 2018 Y/N, PIM timing, and alpha `[.2,.8]`.
- `NUMERICAL_PATH_STABILIZATION_PROPOSAL`: path-only damping/staging candidate that must preserve the fixed point.
- `FUTURE_VALIDATION_REQUIRED`: no production value or runtime behavior is claimed here.

## Source-backed unit diagnosis

The full ledger is `unit_contract.csv`. The proposed common unit makes GDP and capital comparable before Cobb–Douglas evaluation. It does not by itself calibrate household grid units. The exact bridge must be explicit:

`At_macro_MU = At_grid × asset_bridge_MU_per_NU_per_grid × N_model_NU`.

The current code silently sets `asset_bridge=1` at `HANK_mp_1turn.m:31,36`. Until the grid normalization is justified, it is `FUTURE_VALIDATION_REQUIRED`. The same declaration must cover `Bt*N` in the national fiscal diagnostic. Per-household `AtTax` and `Tt` must be multiplied by N exactly once before being added to aggregate `Corptax`, labor tax, and government-capital income.

The accepted Anhui 2018 values illustrate, but do not select, the route. Under the proposed common unit, Y=`34,010,900 MU`, N=`607,600 NU`, and canonical PIM K=`135,731,410.82013685 MU`. With `alpha=.7380939146868483`, the same-year identity gives `Zt0=1.0331694367651485`. Under the source zero-change firm bookkeeping with `mt=mstar=.9`, raw `wjt0=13.194363905989741` and raw `ra0=.15648760365692777`, which clip to `1.3/.09`. This is evidence that wage/rate safety normalization still needs validation, not permission to rescale the data or widen the bounds.

## Alpha contract

Successor metadata must persist `alpha_raw`, `alpha_lower=.2`, `alpha_upper=.8`, `alpha_used`, `alpha_clip_flag`, and `alpha_clip_reason`. The only allowed reasons are `NONE_INSIDE_RANGE`, `CLIPPED_TO_LOWER_OWNER_BOUND`, and `CLIPPED_TO_UPPER_OWNER_BOUND`. Alpha is immutable during one steady-state run. The current estimate produces `raw=used=.7380939146868483`, `flag=false`, `reason=NONE_INSIDE_RANGE`.

## Initialization and ordered updates

Detailed initialization and update contracts are in `initialization_contract.md` and `update_order_contract.md`. Current first-household prices remain the generic `.09/.09/.6/20`; the data initializer does not replace them. The successor must refuse to start a household solve until the cross-province initialization receipt contains raw, clipped, composite, and next-household-used prices for every province.

The source one-turn order is: old state → household outputs → migration labor → `At*N` capital allocation → `rah` from old clipped firm rates → firm raw/clipped prices → household wage aggregation → monetary/fiscal diagnostics → convergence → optional Zt then GovInv controller → damped K/N reference. The successor preserves the one-turn lag but names every raw/used state explicitly.

`clip firm price → aggregate composite price → damp household-used composite price` is the semantic rule. For wage, the source already uses current clipped wjt. For rah, the source aggregates prior clipped ra before the current firm call; preserving that lag is the minimal baseline, while moving aggregation after the current firm is a separately labelled future candidate. Damping a pre-clip firm price would change the current Corptax compensation and safety semantics and is not an equivalent path-only change.

## Single-loop calibration and GovInv

The detailed state machine is `calibration_stage_contract.md`. Existing final convergence remains: max K/N-reference gap `<1e-9`, max Y/Y_prev gap `<1e-9`, all 31 household convergence flags, and zero ra lower/upper-bound hits.

The source GovInv controller runs only after a nonconverged turn, when max K/N-reference gap `<.1` and `steady_state==1`. It reads already-clipped ra: below `.04` multiplies GovInv by `.9`; above `.07` multiplies it by `1.1`; otherwise holds. Zt is reset first when the GDP gap exceeds `.01`, then GovInv updates, then the K/N reference is damped. The `.9/1.1` rule is a bounded multiplicative controller step, not convex under-relaxation.

Minimal integration: execute those same Zt/GovInv proposals only in Stage B, record old/raw-proposed/used values and reasons, freeze both in Stage A/C, and preserve Zt-before-GovInv ordering. Additional GovInv damping is a future choice, not part of this specification.

## Scientific and Git boundary

This package changes no production scientific source and runs no model function. It does not select a production capital series, alter price bounds, freeze damping coefficients or gates, prove convergence, repair KFE boundaries, or make Results eligible. `Results eligibility=FALSE`.
