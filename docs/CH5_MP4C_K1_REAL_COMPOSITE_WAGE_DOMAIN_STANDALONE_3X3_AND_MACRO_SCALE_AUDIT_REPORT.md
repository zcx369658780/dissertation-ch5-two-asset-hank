# CH5 MP4C K1 real composite-wage standalone 3×3 and macro-scale audit report

Date: 2026-09-13

Terminal classification: `REAL_WAGE_SCAN_COMPLETE__MACRO_DIMENSIONAL_RELATION_UNRESOLVED__JOINT_RECALIBRATION_OWNER_REVIEW_REQUIRED`.

Results eligibility=`FALSE`.

## Scope and invariance

Actual baseline was `f1f95f11effa3bfc22e2045da2b04030eb9891a9`. The exact Cartesian grid was `rb=.02`, `ra={.06,.0675,.07}`, household composite `w={13,15.5,18}`. All nine fixtures used fresh MATLAB-style initialization. Nine distinct initial-value objects and nine distinct baseline-labor objects were constructed; only `inputs.r_a` and `inputs.wages[0]` varied.

The accepted oracle SHA-256 was `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`; protected `HANK_2ASSETS_HJB.m` was `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`. HJB/KFE equations, initialization, grid, FOC, selector, derivative floor, boundary law, solver, tolerances, transition legality and contaminated-row KFE were unchanged.

## Exact 3×3 result

| `ra` | `w` | HJB | iter | final max change | max A2max | KFE label | `Ct` | `Lt` | `At` | `Bt` |
|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| .0600 | 13.0 | CONVERGED | 13 | 7.636e-8 | .003837 | INTERIOR | 8.5743 | .6732 | 7.1434 | 1.6095 |
| .0600 | 15.5 | CONVERGED | 23 | 1.741e-10 | .003847 | INTERIOR | 9.7899 | .6943 | 7.2901 | 4.6813 |
| .0600 | 18.0 | CONVERGED | 21 | 7.231e-8 | .003854 | INTERIOR | 11.1028 | .6784 | 7.2704 | 4.6972 |
| .0675 | 13.0 | CONVERGED | 24 | 2.239e-8 | .004856 | INTERIOR | 8.3184 | .7089 | 7.3301 | 4.6630 |
| .0675 | 15.5 | CONVERGED | 24 | 1.590e-9 | .004868 | INTERIOR | 9.6479 | .6900 | 7.3052 | 4.6828 |
| .0675 | 18.0 | CONVERGED | 23 | 1.156e-10 | .004878 | INTERIOR | 10.9503 | .6742 | 7.2868 | 4.6994 |
| .0700 | 13.0 | CONVERGED | 24 | 7.120e-11 | .005222 | INTERIOR | 8.2778 | .7076 | 7.3347 | 4.6629 |
| .0700 | 15.5 | CONVERGED | 24 | 1.915e-9 | .005236 | INTERIOR | 9.6036 | .6887 | 7.3102 | 4.6830 |
| .0700 | 18.0 | CONVERGED | 23 | 1.678e-8 | .005246 | INTERIOR | 10.8999 | .6729 | 7.2911 | 4.6995 |

All 9 HJB calls were legal and converged, with no first illegal iteration, no hard error, finite expected-shape arrays, valid label domains, and `A2max<homecrit=.01`. Exactly one KFE followed each converged HJB. All nine illiquid marginals have mode `a=7.3684210526`, `amin` mass zero, `amax` mass zero up to about `3.5e-18`, and interior-a mass one up to floating-point rounding. Therefore all nine are `INTERIOR_A_DISTRIBUTION_CANDIDATE`; lower/upper/ambiguous/pathological counts are zero.

Interior-candidate ranges are `Ct=8.27777–11.10279`, `Lt=.672871–.708939`, `At=7.14335–7.33469`, and `Bt=1.60951–4.69951`. Every tested `ra` is interior at all three wages.

Raw KFE evidence was not clipped. Total mass is one to floating-point precision; residual infinity norms are `6.94e-18–1.76e-17`. Eight points contain negative density entries only `1.23e-17–1.07e-16` in magnitude, inside the fixed `100·machine-epsilon` rounding band and not materially non-probabilistic. The b marginal nevertheless has mode at `bmax=5` at all points, with `bmax` mass about `.131–.683`; this is a material caveat, not an admissibility claim.

## Comparison with the old wage domain

At the same `ra`, the accepted old `w={.8,1.05,1.3}` narrow map had 2 interior, 2 lower, 4 ambiguous and 1 upper point, with no wage-robust interior `ra`. The new map has 9/9 interior and all three wage-robust `ra` values. Observed health labels therefore change materially with wage domain. The unobserved gap between `1.3` and `13` prevents a continuous-frontier or monotonicity claim.

## Macro quantity and scale audit

The accepted corrected-2018 initialization-only receipt supplies a same-state 31-province table for GDP, population, capital, productivity, raw/guarded firm wage and initial household composite wage. It is diagnostic evidence, not a full-model result.

| Variable | Transformation | Accepted min / median / max | Comparability |
|---|---|---:|---|
| GDP raw | statistical `亿元` | 1,548.4 / 22,716.5 / 99,945.2 | raw GDP only |
| `Y0_MU` | GDP raw ×1000; `MU=10万元` | 1.5484e6 / 2.27165e7 / 9.99452e7 | with capital in MU |
| Population raw | statistical `万人` | 354 / 3,931 / 12,348 | raw population only |
| `N0_NU` | population raw ×100; `NU=100 persons` | 35,400 / 393,100 / 1,234,800 | denominator for `Y/N` |
| `Y0_MU/N0_NU` | model output/population ratio | 32.2231 / 51.5588 / 151.0310 | algebraically 1000 yuan/person/model period; wage mapping unproven |
| Track-A `K0_MU` | corrected capital raw 亿元 ×1000 | 6.3257e6 / 6.7307e7 / 2.10017e8 | with GDP in MU |
| `Zt0` | `Y0*K0^-alpha*N0^(alpha-1)` | .6960 / 1.2420 / 2.4379 | derived productivity |
| raw firm `wt0` | marginal-product formula | 7.7643 / 12.4233 / 36.3915 | model scale, not proven RMB |
| guarded `wjt0` | clip to `[.8,1.3]` | 1.3 / 1.3 / 1.3 | model scale; 31/31 upper guard |
| household `w0` | source wage aggregation | 13.8375 / 17.8746 / 18.5197 | `MODEL_NORMALIZED_SCALE__MONETARY_UNIT_NOT_PROVEN` |

The wider accepted provincial trajectory envelope is about `12.8426–18.5197`; the table is the same-state corrected-2018 initialization-only subset.

### Scaling and normalization trace

- `load_GDPdata.m:93-104`: GDP and capital use `GDP_multiplier=1000`; population uses `POP_multiplier=100`; sector GDP shares divide percentages by 100.
- Corrected runtime: `Y0_MU=GDP_raw*1000`, `K0_MU=K_raw*1000`, `N0_NU=POP_raw*100`, `Ztratio=1`, `GovInv_ratio=1`.
- `It_to_Kt.m:6-10`: `K0=I0/.1`; `K_t=(1-.096)K_(t-1)+I_(t-1)`. Firm-flow investment is separately `I=K-K_prev+.025K` (`HANK_firm.m:47`). Accepted province investment magnitudes are unavailable without a forbidden run.
- `load_GDPdata.m:126-137`: per-capita objects are GDP/population and capital/population; productivity uses `Y*K^-alpha*N^(alpha-1)`, accepted `alpha=.7380939146868483`.
- `mpHANK_equilibrium_2000.m:25,29-40`: `Zt=IND_Zt*Ztratio`, `L0=N0` as population proxy, `GovInv0=K0*GovInv_ratio`. `L0=N0` is not household labor; `GovInv0=K0` remains pending redesign.
- `mpHANK_equilibrium_2000.m:46-50`: inter-province asset share is normalized to `[0,.3]`; `load_distdata.m:6-8` divides distance by its maximum and multiplies by `.5`.
- `HANK_firm.m:30,43,47,66-74`: output, raw wage, investment and `wjt` guard formulas are source-traced.
- `wage_caculate.m:1-17`: destination wage nonlinearly aggregates `wjt_j*(1-tau_j-sigmau_ji)/phi_ji` across 31 origins with an `alphal` normalization. This explains O(1) `wjt` to O(10) composite `w`, not a monetary unit.
- Legacy-only evidence records a capital source documented as 万元 multiplied by GDP's ×1000 factor without dimensional rationale. It is not active Track-A authority.
- Legacy writers divide `Yt0/Yt/Kt0/Kt` by 1000 and `N/Lt` by 100 for exported statistical-scale tables. No separate nominal-to-real deflator or ×10000/×1e4/×1e8 monetary conversion was established in the designated accepted chain.

## GDP vs per-capita GDP vs household wage scale

The receipt permits same-state side-by-side reporting but not direct comparison. `Y0/N0` has an algebraic MU/NU ratio; `w0` inherits utility/labor and cross-province aggregation normalizations whose mapping to the macro money unit and period is unproven. Conclusion: `DIMENSIONAL_RELATION_UNRESOLVED`.

It is not scientifically defensible to change `wjt` bounds directly. Missing evidence is a joint calibration of `wjt→w`, return/asset bridge→`ra/rah`, household-wage-to-macro-money/time mapping, and consistent GDP, population, investment, capital, productivity and labor scales.

Exactly one next Owner gate: `OWNER_REVIEW_JOINT_WJT_RA_MACRO_SCALE_RECALIBRATION`.

The gate was not executed or published as a successor task.

## Runtime and evidence

HJB=9/9; KFE=9/9; scientific retries=0; engineering retries=0; global outer=0; firm runtime=0; MATLAB runtime=0; K1B=0; K2=0; GE=0; downstream=0; shock=0; IRF=0; Results writes=0.

Compact evidence: `docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/`. External sealed evidence: `D:\ProjectTemp\ch5-mp4c-k1-real-composite-wage-macro-scale-evidence-20260913-001`.

KFE caveat: standalone contaminated-row KFE does not resolve corrected-2018 multi-province finite-box upper-b leakage or MATLAB-style pinning and establishes no equilibrium, calibration, admissibility, steady-state or Results authority.
