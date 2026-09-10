# Chapter 5 MP4C firm-price normalization and household-to-macro bridge forensic

Date: 2026-09-10

Base `origin/main`: `d9faf96d75db5a561b562700a10f075ff36eddff`

Verdict: `FIRM_PRICE_NORMALIZATION_FORENSIC_PASS__WAGE_UNIT_MISMATCH_AND_RETURN_LEVEL_EFFECTS_SEPARATED`

## Required conclusions

- Wage: `PRICE_BOUND_HITS_PRIMARILY_UNIT_NORMALIZATION_MISMATCH`.
- Return: `PRICE_BOUND_HITS_PRIMARILY_ECONOMIC_RATIO_LEVELS` under the frozen Track-A annual Y/K object; common money rescaling cannot repair it.
- Household currency: `HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED`.
- Asset bridge: `beta_a` remains unidentified; `beta_a=1` ratios are descriptive only.

## Firm wage forensic

Imposing the same Cobb-Douglas identity used to construct `Zt0`, protected `HANK_firm.m:30,43` collapses exactly to:

`w_raw = mt*(1-alpha)*Y/L = .92*(1-.7380939146868483)*Y/L`.

Across 31 provinces, Y/L min/median/max is `32.22306163021869 / 51.5588270640548 / 151.0310218978102 MU/NU` (Gansu minimum, Beijing maximum). Raw wage min/median/max is `7.7642626541050035 / 12.423284914909623 / 36.39146820961234`; all 31 exceed `1.3`. This is a direct constant multiple of ordinary cross-province Y/L variation, not a separate Z anomaly.

With `MU=10万元` and `NU=100 persons`, one macro `MU/NU` is 1,000 yuan/person/period. Numerical wage transforms as `s_M/s_N`, whereas the legacy bounds have no source-defined absolute currency or period mapping. The broad wage hit is therefore primarily a unit/numeraire mismatch; this does not authorize rescaling data or bounds to force an interior result.

## Firm return forensic

At `mt=.92`, `pit=.02`, `theta=100`, and `corptau=.25`, the price-adjustment cost is `.02Y`, profit after the floor is `.06Y`, and the after-tax dividend component is `.045Y/K`. Hence protected `HANK_firm.m:45-54` becomes:

`ra_raw = .92*alpha*Y/K - .025 + .045*Y/K = .7240464015119004*Y/K - .025`.

The MPK component min/median/max is `0.10615407045353614 / 0.2185687699720253 / 0.3828487147313371`; dividend component is `0.007034766931645991 / 0.014484422017173095 / 0.0253711559689463`; depreciation is exactly `-.025`; other additive terms are zero. Each varying component is lowest in Qinghai and highest in Beijing. MPK supplies about `93.7849%` and dividends `6.2151%` of the positive Y/K coefficient.

Raw return min/median/max is `0.08818883738518214 / 0.2080531919891984 / 0.38321987070028335`; 30/31 exceed `.09`. The `.09` boundary corresponds to `K/Y≈6.296055665320873`; only Qinghai has a slightly larger K/Y and remains inside. Because Y/K and every return component are invariant to common Y/K money rescaling, the high returns arise primarily from the frozen annual economic ratio levels relative to a historically numerical bound. A separate period/capital-definition convention may still matter, but it is not identified by this task.

## Household normalization and bridge

The HJB source puts `a`, `b`, `c`, `w`, `Tt`, adjustment costs, and returns into an internally relative system, but provides no yuan, deflator, or period conversion for a grid unit. Its literal initialization income even uses `Rah.*raah` after filling `Rah` from `raah`, while later illiquid drift uses `Rah.*aaah`; this unresolved return-times-return versus return-times-asset inconsistency is recorded, not repaired. `a/b` therefore have undefined absolute currency normalization; `c/w/Tt/AtTax` have only implied relative units. Firm `wjt` and household `w` are not aliases: the latter is a nonlinear, unnormalized 31-destination composite. Legacy `wjt=.6` and `w=20` do not prove a shared absolute unit.

The literal capital bridge multiplies household mean `At` by N inside cross-province allocation, then adds GovInv before the firm. A dimensionally valid successor requires `K_private_MU=At_grid*beta_a*N_NU`. The source does not define `beta_a`. Under the historical `At=2`, descriptive `beta_a=1` AtN/K0 ratios span `0.004282158069342776–0.019977992688578954`, but no coefficient is selected.

## Legacy bounds and authority

The ra range has direct safeguard evidence: `HANK_firm.m:55` says it prevents failure during convergence, and the outer convergence predicate rejects ra boundary hits. This supports the Owner's description of the rate range as a numerical/HJB-convergence safeguard, not an empirical economic interval. The wage bound performs clipping/tax compensation and has a commented earlier upper value, but no inspected source states its economic or historical calibration; its provenance remains unknown. The generic `.09/.09/.6/20` starts likewise have no source-backed calibration citation.

Across the complete task session, two deterministic builders decomposed 62 province rows; two focused-test processes executed 10 cases; one compile-check and two evidence-finalization processes ran. The first evidence root `-001` is preserved as a preliminary audit package and `-002` is final. MATLAB/model calls, HJB/KFE/control, `HANK_firm` runtime, `Lt_seperate`, capital-allocation runtime, outer turns, steady state, root/direct/iterative/eigen solves, GE, annual, IRF, Results, and tuning were zero. `Results eligibility=FALSE`.

This PASS does not change bounds, choose `beta_a`, modify any production source, or authorize a household/outer/steady-state run. The next gate is independent ChatGPT Reviewer ACCEPT/REJECT of the dedicated candidate commit.
