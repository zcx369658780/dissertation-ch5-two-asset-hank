# Chapter 5 MP4C K1 quarterly-HJB versus annual-firm-flow provenance closure

Date: 2026-09-12

Baseline: `331d46a3044fcff7ed089d1f88705683eb86722a`

## Classification

`COMMON_CALENDAR_BASE_NOT_SOURCE_IDENTIFIABLE__GENUINE_DEPRECIATION_CALIBRATION_CONFLICT__OWNER_RECALIBRATION_CONTRACT_REQUIRED`

Existing authority cannot establish either quarter or year as the stationary HJB model-time unit. The Chapter-5 `.0025` entry cannot safely be called a typo: Chapter 4 explicitly says `.025` per quarter and approximately `.10` per year, while protected MATLAB and active Python merely inherit `.025` without a calendar annotation. Corrected-2018 firm flow/stock operands are annual. Direct `HJB r_a = current ra0` remains unauthorized.

## Depreciation conflict

| Occurrence | Value and role | Calendar authority | Classification |
|---|---|---|---|
| protected dissertation `Main_Spine/c4.tex:247` | firm depreciation `.025`; prose also says `.10` annually | explicitly quarterly; `.10` is a simple four-quarter approximation | `SOURCE_CONFIRMED_BUT_CONVERSION_LAW_NOT_EXACT` |
| protected dissertation `Main_Spine/c5.tex:236` | Chapter-5 firm parameter `.0025` | none | `CONFLICTING` |
| protected MATLAB `multi_prov_HANK_12sts.m:69` | firm literal `.025` | none in the literal/comment | `LEGACY_INHERITED_ONLY` |
| active corrected runner `corrected_2018_single_turn/run.py:414` | firm literal `.025` | none | `LEGACY_INHERITED_ONLY` |
| corrected data contract | PIM depreciation `.096` | annual capital-stock construction | `SOURCE_CONFIRMED_DISTINCT_OBJECT` |

Result: `GENUINE_CALIBRATION_CONFLICT_REQUIRING_OWNER_FREEZE`. Source precedence does not establish that `.0025` is typographical, and neither `.10` nor `.096` may replace the firm literal automatically. The `.096` PIM coefficient constructs empirical `K`; it is not the household/firm return depreciation parameter.

Chapter 4's “10% annually” is not an exact conversion law: simple multiplication gives `.10`, whereas discrete quarterly compounding gives `1-(1-.025)^4`; a continuous-rate conversion would use a logarithm. The source does not identify which object/law is intended.

## Common time-base authority

The HJB is continuous-time and requires

`rho V = u + V_b mu_b + V_a mu_a + Q_z V`,

where `rho`, `rb`, `r_a` and generator `Q_z` share `1/model-time`; `c`, wage income, `Tt`, `d` and adjustment cost share asset/model-time. `Delta=1000` is a false-transient numerical step, not calendar time.

Authority remains:

- `rho=.05`: Chapter-5 value, no period;
- `rb=.02`, borrowing gap `.07`, `Tt=.1`: inherited literals, no period/currency-flow bridge;
- `r_a/rah`: continuous-time drift rate, but firm source has conflicting periods;
- `Q_z` off-diagonal `1/3`: generator intensity per unspecified model time, not a discrete transition probability;
- `chi0=.1`: dimensionless adjustment wedge under the implemented FOC;
- `chi1=2`: determines `d` per model time and therefore needs time calibration;
- labor disutility and consumption utility are flow utility, but their normalization is not calendar-identified.

The legacy shock comment “four quarters equal one year” identifies that shock-path clock only. It does not bind the stationary HJB clock.

## Annual-data bridge

Corrected-2018 `Y` is annual GDP flow; `K` is a stock built from annual GFCF/PIM; population/labor use `NU=100 persons`; money flow uses `MU=10万元`. Consequently `Y/K`, `rk=mt*alpha*Y/K`, profit/K and `wjt=mt*(1-alpha)*Y/L` inherit annual-flow scale. The household `a/b` grid has no source-backed MU/per-person bridge, and composite `w` is not the firm `wjt` alias.

No inspected dissertation, protected MATLAB, active Python or accepted receipt defines a complete annual firm-flow to quarterly/model-time HJB-flow conversion.

`NO_SOURCE_BACKED_ANNUAL_TO_HJB_FLOW_BRIDGE_FOUND`

## Calibration provenance summary

| Object | Source -> MATLAB -> Python -> use | Classification |
|---|---|---|
| `rho=.05` | c5 value without period -> literal -> `EconomicParams` -> `rho*V` | `UNRESOLVED` |
| `rb=.02`, gap `.07` | no calendar statement -> initial literals -> `HouseholdInputs` -> liquid drift | `LEGACY_INHERITED_ONLY` |
| `r_a/rah` | continuous-time asset-return concept -> direct firm-return composite -> `r_a` -> illiquid drift | `CONFLICTING` |
| `delta` | c4 quarterly `.025`; c5 `.0025` -> `.025` -> `.025` -> annual-flow `ra0` | `CONFLICTING` |
| `Q_z=1/3` | jump-process concept, no period -> generator literal -> switch matrix -> `Q_z V` | `UNRESOLVED` |
| `chi0=.1`, `chi1=2` | no time calibration -> FOC literals -> accepted FOC -> `d`/cost | `LEGACY_INHERITED_ONLY` |
| `Tt=.1` | no unit source -> literal -> transfer input -> liquid flow | `UNRESOLVED` |
| `ra [.02,.09]`, `wjt [.8,1.3]` | convergence/unknown guards -> clipping -> clipping | `NUMERICAL_SAFEGUARD` |
| `Vb>=1e-6` | no economic calibration -> HJB max -> faithful floor -> consumption/labor FOC | `NUMERICAL_SAFEGUARD` |

Full receipts are under `docs/evidence/ch5_mp4c_k1_quarterly_hjb_annual_firm_provenance_closure/`.

## Candidate conventions

| Convention | Source support | Complete conversions required | Result |
|---|---|---|---|
| Q: quarter is one HJB unit | quarterly depreciation and shock clock only; stationary HJB not identified | annual `Y/K`, profit/K, wage/profit/consumption/transfer/cost flows; separately freeze `rho`, `rb`, `Q_z`, `chi1` | `NOT_SOURCE_CLOSED` |
| A: year is one HJB unit | annual empirical firm operands only; HJB base not identified | convert quarterly depreciation using an Owner-selected law; freeze/reinterpret `rho`, `rb`, `Q_z`, wage/transfer/cost and flow utility | `NOT_SOURCE_CLOSED` |
| M: abstract model time | matches current explicit authority | Owner must freeze base period, each rate's object type, flow scaling, depreciation law, generator scaling and household numeraire | `ONLY_TRUTHFUL_CURRENT_CONVENTION` |

A common positive linear scaling of annual firm flow components would preserve their cross-province ranking, but subtracting a differently converted depreciation level changes absolute payoff levels. Compounding/log transformations can also change comparisons. These are calibration/economic decisions, not unit-only bookkeeping until object types are frozen.

## Conversion-law boundary

- Annual currency flow to quarterly flow could be linearly allocated only if the source defines within-year timing; none does.
- A simple rate `/4` or `*4` applies only to a source-defined simple rate convention.
- Discrete compounding applies to discrete net returns over identified periods.
- `log(1+r)` applies only when a discrete gross/net return is mapped to a continuous intensity.
- A generator intensity and continuous discount intensity scale linearly with the time-unit definition; they are not compounded probabilities.

No one law is endorsed here.

## Wage, transfer and adjustment-cost consistency

Converting `r_a` alone cannot close the HJB. Under Q, annual firm wage/profit and all household currency flows must be expressed per quarter; under A, every quarterly-source rate/intensity and flow must be annualized coherently. `d` has asset/time units; `chi1` carries the corresponding time normalization, while `chi0` is a dimensionless wedge. Consumption, labor income, `Tt`, `d` and cost must share the same asset/time numeraire. None of Q or A currently satisfies all links.

## Diagnostic-bound interaction

For any future convention, preserve raw/pre-conversion firm objects first, perform the Owner-frozen calendar/numeraire conversion, and apply temporary guards only to the converted objects at the receiving HJB interface. Persist raw, converted, guarded values and saturation counts separately. Applying historical bounds before conversion would mix units; `[.02,.09]` and `[.8,1.3]` remain non-structural safeguards. No bound value is set here.

## STATIC_NO_FEEDBACK

No transformed distribution is produced. Because Q and A lack source authority and no conversion law is frozen, an illustrative `/4`, `*4`, compound or log table would manufacture calibration.

## Zero-science ledger and next gate

All new trajectory, outer-turn, HJB, KFE, household, firm, MATLAB, K1B, K2, GE, annual, shock/IRF and Results calls are `0`. Only static reads, hashes, symbolic/unit analysis, receipt generation, focused tests and compilation were used.

Exactly one next gate:

`OWNER_FREEZE_COMPLETE_TIME_BASE_AND_CALIBRATION_CONTRACT`

The freeze must select Q, A or another explicit unit and define `delta`, `rho`, `rb`, `Q_z`, annual firm-flow conversion, wage/asset numeraire, transfer/consumption/cost flows, `chi1`, and the conversion law/object type. A bounded runtime diagnostic may be separately issued only afterward. This report does not publish it.

KFE remains `DIAGNOSTIC_ONLY`; upper-`b` leakage and MATLAB-style pinning remain independent blockers. Results eligibility=`FALSE`.
