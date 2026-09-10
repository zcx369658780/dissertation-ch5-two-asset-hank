# Chapter 5 MP4C raw-NBS 2018 rebuild — Reviewer acceptance

Date: 2026-09-10.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `3bd6343011f17d1b2273386732f06e6da6bf84e9`.

## Verdict

Reviewer marker:

`RAW_NBS_2018_REBUILD_ACCEPTED_PARTIAL__SAME_YEAR_GDP_POP_AND_LAGGED_FLOW_CAPITAL_REBUILT__SOURCE_ROUTE_DIFFERENCE_REMAINS`

Builder verdict accepted as appropriately cautious:

`RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY`.

## Accepted findings

1. The four raw NBS files do not jointly provide a full 2018 four-source panel. GDP is complete for 1992–2022, population for 2000–2022, fixed-capital formation for 1996–2017, and depreciation for 1992–2017. The supplied investment/depreciation files contain no 2018 province observations.
2. No 2018 investment or depreciation values were filled, interpolated, or fabricated. Under the frozen lagged-flow timing, complete 2017 flows are sufficient to construct `K_2018`.
3. Track A is accepted only as the primary comparable PIM rebuild under the frozen formula `K0=I0/0.1`, `Kt=(1-.096)K(t-1)+I(t-1)` using raw NBS gross fixed capital formation. It is not yet promoted over the existing canonical investment-route capital because the underlying investment concept/source route differs.
4. Track B is accepted only as a diagnostic accounting capital sequence using observed depreciation: `Kt=K(t-1)+I(t-1)-D(t-1)`, with the same initial-stock assumption. It is not production authority.
5. The pooled 2009–2018 regression result is accepted as a reproducible calibration estimate: `alpha=0.7380939146868483`, SE `0.03825774803543075`, t `19.292664952555352`, p `7.094017371850083e-55`, R² `0.6924937537873637`, N=310. The legacy alpha `0.772866243094144` remains a comparison object.
6. Same-year 2018 productivity values are accepted as deterministic calculations conditional on each capital track. No 2020 level enters the rebuilt 2018 Z object.
7. Anhui raw-NBS 2018 GDP and population match the current accepted canonical values (`34010.9` 亿元 and `6076` 万人). Anhui Track-A K2018=`70182.43335888097` 亿元, Track-B K2018=`84616.8` 亿元, Track-A Z2018=`0.0018759632501672073`, Track-B Z2018=`0.0016340686739896946`.
8. Relative to the legacy mixed-year MATLAB object, Anhui differences are material: GDP `+213.040973%`, capital Track A `+207.653399%`, Z Track A `+192.410443%`, while population differs by only `-0.897080%`. Anhui is material but not the unique or largest cross-province outlier.
9. Relative to the current canonical capital route, Anhui Track-A capital is about `48.293%` lower. This difference is not a numerical inconsistency by itself; it reflects a source/concept route difference (raw gross fixed capital formation versus the accepted canonical investment route) plus the shared PIM assumptions. It must be resolved scientifically before production promotion.
10. All HANK/HJB/KFE/firm/wage/migration/allocation/outer-turn/steady-state/GE/annual/IRF/Results calls were zero. This task establishes calibration/data evidence only and does not prove model convergence or explain the prior asset collapse causally.

## Scientific boundary

The accepted result supports further discussion of which investment/capital data concept should be the Chapter 5 production calibration authority. It does not authorize replacing the current canonical capital series, changing the HANK algorithm, or running a new steady state.

Results eligibility=`FALSE`.
