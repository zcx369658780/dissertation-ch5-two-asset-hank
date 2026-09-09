# Chapter 5 corrected-2018 five-turn KFE leakage attribution

## Verdict

`FIVE_TURN_KFE_ATTRIBUTION_PASS__SAME_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`

Mechanism classification: `SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`. This is zero-science saved-array attribution, not a KFE rerun or repair.

## Nationwide attribution

| turn | material residual provinces | pin approximately all L1 | positive upper-b escape | leak cells lower-b/upper-b/lower-a/upper-a | escape min/median/max | upper-b face mass min/median/max |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 31 | 31 | 31 | 0/620/0/0 | 0.00016096598019326992/0.00030060317559792605/0.00036914183148832873 | 0.23205904219661561/0.26609006707455685/0.27309414064648962 |
| 5 | 31 | 31 | 31 | 0/620/0/0 | 0.00016085190930939703/0.00030031484303678728/0.00036883498560473082 | 0.2319649833644512/0.26597126239748875/0.27296935799953342 |

All 62 turn4/5 objects preserve exact Q/T orientation, F-order density mapping, row replacement and normalization convention. The material residual is concentrated at the dropped pin equation; off-pin terms and both signed mass-balance corrections are floating-point scale. The implied source balances upper-b finite-box escape algebraically. It is not an implemented household entry process.

- Turn 4 signed residual-vs-escape identity error min/median/max: `1.9569849213363355e-17 / 6.722053469410127e-17 / 1.577514160966409e-16`; implicit-source-vs-escape discrepancy: `1.3227266504323154e-17 / 1.3986208025063007e-16 / 3.9741430632456165e-16`.
- Turn 5 signed residual-vs-escape identity error min/median/max: `1.4257258568184383e-17 / 8.760353553682876e-17 / 1.7932703932910243e-16`; implicit-source-vs-escape discrepancy: `6.505213034913027e-19 / 1.0695654431569501e-16 / 4.565575348336459e-16`.
- Across turn 4–5, pin-row L1 shares range from `0.9999999999869693` to `0.9999999999982326`; maximum individual off-pin residual is `5.352822169074709e-15`, below the frozen componentwise `128 eps` bound.
- Highest escape in both turns: `广西`, followed by `海南`, `贵州`, `广东`, `甘肃`. Highest upper-b face mass: `河南`, followed by `湖南`, `安徽`, `湖北`, `山西`.

## Call725 mechanism comparison

Call725 and corrected turn4/5 share the same post-loop mechanism: the finite-box assembler omits the outside-grid upper-b offdiagonal while retaining its diagonal rate; KFE uses the transpose, replaces row `k=295`, sets `rhs[k]=.007`, and normalizes the returned vector. Call725 pin share was `0.9999999999999966`, escape `0.6697587443279651`, and upper-b face mass `0.6758361975609537`. Corrected turn4/5 have smaller flows but the same algebraic closure. Their HJB-loop operators have 19 negative offdiagonals while post-loop KFE operators have zero; the HJB-loop object is not substituted into this mass ledger.

Turn3 shows the same mechanism while Anhui A+B collapses from the prior turn. Turn4/5 A+B remains near 1.893. These are temporally coincident diagnostic quantities; the saved evidence does not identify leakage as the causal source of the asset collapse.

All scientific/model/solver calls are zero. Turn6+, new KFE solves, steady state, GE, annual, IRF, Results and production repair remain unauthorized. Results eligibility is FALSE.
