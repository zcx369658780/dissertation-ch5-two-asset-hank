# Chapter 5 corrected-2018 five-turn KFE leakage attribution — Reviewer acceptance

Date: 2026-09-10.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `ea4ac44fe3c65c506ff7fdfbdbf29d96078cc5c6`.

## Verdict

Reviewer marker:

`FIVE_TURN_KFE_ATTRIBUTION_ACCEPTED__SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED__OWNER_BOUNDARY_DECISION_REQUIRED`

Accept Builder verdict:

`FIVE_TURN_KFE_ATTRIBUTION_PASS__SAME_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`.

## Accepted findings

1. This is zero-science saved-artifact attribution. All scientific/model/solver calls are zero.
2. All 62 turn4/5 province-turn objects preserve the same post-loop KFE orientation and closure convention: post-loop `Q`, transpose, F-order density mapping, row replacement at `k=295`, `rhs[k]=.007`, and normalization.
3. Turn4/5 material source-free residual is concentrated in the dropped pin equation: pin-row L1 share ranges `0.9999999999869693–0.9999999999982326`; maximum individual off-pin residual is `5.352822169074709e-15`, below frozen componentwise `128 eps≈2.842e-14`. No additional material residual source is established.
4. Every province in turns4/5 has positive upper-b escape and material source-free residual. Leak-cell counts by face are `0/620/0/0` for lower-b/upper-b/lower-a/upper-a in each turn.
5. Density-weighted upper-b escape min/median/max: turn4 `.00016096598019326992/.00030060317559792605/.00036914183148832873`; turn5 `.00016085190930939703/.00030031484303678728/.00036883498560473082`.
6. Upper-b face mass min/median/max: turn4 `.23205904219661561/.26609006707455685/.27309414064648962`; turn5 `.2319649833644512/.26597126239748875/.27296935799953342`.
7. Signed residual-vs-escape identity closes at floating-point scale. Maximum absolute discrepancy is about `1.58e-16` in turn4 and `1.79e-16` in turn5.
8. Implicit-source-vs-escape balance also closes at floating-point scale. Maximum discrepancy is about `3.97e-16` in turn4 and `4.57e-16` in turn5.
9. Machine-scale negative density mass cannot explain the material source-free residual. The blocker is finite-box mass leakage plus dropped-equation/pinning algebra, not density negativity.
10. Highest escape in both turns: 广西、海南、贵州、广东、甘肃. Highest upper-b face mass: 河南、湖南、安徽、湖北、山西.
11. The corrected-2018 turn4/5 mechanism matches the accepted call725 `rah=.07` mechanism: upper-b outside-grid offdiagonal omitted while diagonal rate is retained; KFE uses the post-loop transpose and replaces one source-free equation; the dropped equation is algebraically equivalent to a balancing source for upper-b escape.
12. This algebraic source equivalence is not an adopted economic household entry/exit process. Source code does not explicitly implement such an economic mechanism.
13. HJB-loop operators remain a distinct issue: turn4/5 HJB-loop operators have 19 negative offdiagonals while post-loop KFE operators have zero. The mass-balance ledger uses the post-loop KFE operator only.
14. Turn3 asset collapse is temporally coincident with the same invalid-density/leakage mechanism, but saved evidence does not causally identify leakage as the sole source of the collapse. C/L/A/B remain diagnostic quantities, not accepted economic moments.
15. Source attribution is accepted to the frozen paths identified in the report, including upper-b finite-box assembly and KFE row-replacement/pinning code paths.

## Scientific boundary

The mechanism is now confirmed broadly across provinces and turns. Do not continue turn6+, steady state, GE, annual, IRF, Results, or new KFE solves. Do not implement a production boundary/grid/source/pinning repair automatically.

The next step requires an Owner scientific decision about finite-box/KFE closure. D1–D3 remain deferred redesign proposals and are not adopted by this acceptance.

Results eligibility=`FALSE`.
