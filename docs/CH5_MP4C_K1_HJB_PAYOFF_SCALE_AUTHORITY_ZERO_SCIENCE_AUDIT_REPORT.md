# Chapter 5 MP4C K1 HJB payoff-scale authority zero-science audit report

Date: 2026-09-12

Task: `CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT`

Live-main baseline: `060b6e4afe481740a2e80288bdbfa6e0d26768af`

## Verdict

`ANNUAL_FIRM_FLOW_RETURN_AND_QUARTERLY_SOURCE_DEPRECIATION_ARE_DIMENSIONALLY_CONFLICTING__DIRECT_RA0_TO_HJB_RA_MAPPING_NOT_AUTHORIZED__PAYOFF_SCALE_AUTHORITY_REMAINS_UNRESOLVED`

The direct numerical identity `HouseholdInputs.r_a = firm ra0` is not source-authorized. The corrected-2018 firm numerator is an annual GDP/profit flow and its denominator is a capital stock, while the dissertation source explicitly describes `delta=.025` as quarterly depreciation. The active firm formula combines those objects without a period conversion. The household block is continuous-time, but its `rho`, `rb`, productivity transition intensity, wage, transfer and adjustment-cost coefficients are not assigned an explicit Chapter-5 calendar unit. The current Chapter-5 parameter table also prints `delta=.0025`, conflicting with both the `.025` code and the Chapter-4 “2.5% per quarter” statement.

This audit therefore does not freeze `/4`, compounding, logarithmic conversion, clipping, shrinkage or any other numerical map. Raw `ra0` remains the Owner-retained economic source object, but its current numerical level is not an admissible HJB payoff until calendar/model-time authority is closed.

## Scope and evidence

The audit read source text and accepted persisted documents only. It did not import or call the scientific runtime. Protected MATLAB and dissertation sources were read-only. Source hashes and asserted fragments are in `docs/evidence/ch5_mp4c_k1_hjb_payoff_scale_authority_audit/source_identity.json`.

External evidence root: `D:\ProjectTemp\ch5-k1-hjb-payoff-scale-authority-audit-evidence-20260912-001`. Its five-file manifest readback passed; manifest SHA-256 is `C0375233E5879D23A721659920DC5E80507DC2B419DBB22875A0E5D12A83E6EF`. The tracked compact evidence package has the same manifest hash. Focused zero-science tests passed `3/3`, and both the builder and focused test compiled successfully.

Key provenance:

- current dissertation `Main_Spine/c5.tex`, SHA-256 `9193FD7AEF06478F2BBF20F81BED0D14D42870DD924FF5B1CEFC296CB18C6AE9`;
- inherited continuous-time/parameter source `Main_Spine/c4.tex`, SHA-256 `0337DB686FB510EFA00E34D9B69B8D7033631C5AF302D439BC316F64C39A1DCC`;
- protected `HANK_2ASSETS_HJB.m`, SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- protected `HANK_firm.m`, SHA-256 `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5`.

## Time-unit authority table

| Object | Active value/form | Authority | Finding |
|---|---|---|---|
| Household discount `rho` | `.05` | `MODEL_TIME_ONLY` | Continuous-time discount intensity; Chapter 5 gives a value but no annual/quarterly label. Familiar magnitude is not period proof. |
| Liquid return `rb`; borrowing gap | `.02`; `.07` | `MODEL_TIME_ONLY` | Both enter liquid drift and must be rates per HJB model time. No calendar frequency is stated. |
| Illiquid payoff `r_a/rah` | portfolio payoff passed as scalar | `MODEL_TIME_ONLY` | It enters `mu_a`; the HJB requires a common time unit, but the firm-to-HJB calendar bridge is absent. |
| Firm depreciation `delta` | code `.025`; c5 table `.0025` | `CONFLICTING_SOURCE_AUTHORITY` | Dissertation c4: `.025` is 2.5% per quarter and 10% per year; c5 table differs by factor ten and gives no period. |
| Firm `rk`, profit/K | `mt*alpha*Y/K`; after-tax profit/K | `SOURCE_CONFIRMED_ANNUAL` for the corrected data operands | Corrected `Y` is annual GDP flow; `K` is an annual capital-stock object, hence these ratios are per-year flow/stock rates absent another normalization. |
| Firm raw `ra0` | `rk + profit/K - delta` | `CONFLICTING_SOURCE_AUTHORITY` | Annual flow/stock rates and quarterly-source depreciation are added directly. |
| Productivity generator | states `.8,1.3`; off-diagonal intensity `1/3` | `MODEL_TIME_ONLY` | It is a continuous-time generator intensity; no calendar calibration is stated. `mu_z=sigma_z=0` are unused constructor fields on this two-state route. |
| Firm `wjt`; household composite `w` | firm Y/L wage then nonlinear composite | `UNRESOLVED` | Corrected firm wage inherits annual output-flow scale; the HJB asset/consumption/wage numeraire and period bridge are absent. `wjt` and `w` are not aliases. |
| Transfer `Tt`, control `d`, `chi0/chi1` | `.1`, endogenous, `.1/2` | `MODEL_TIME_ONLY` | All are flow/drift objects in the HJB; no calendar calibration is stated. |
| Outer steady-state turn | lagged fixed-point update | `SOURCE_CONFIRMED_OTHER` | It is a numerical iteration, explicitly not economic calendar time. |

The machine-readable table is `time_unit_authority.csv` in the evidence package.

## HJB dimensional consistency

The accepted Python/MATLAB-faithful source implements the stationary continuous-time equation in the form

`rho*V = u(c,l) + V_b*mu_b + V_a*mu_a + Q_z*V`,

with an implicit false-transient step `[(1/Delta + rho)I - A]V_new = u + V_old/Delta` (`exports/matlab_faithful_two_asset_ha.py:554-556`; protected MATLAB `HANK_2ASSETS_HJB.m:240-243`). `Delta=1000` is a numerical false-transient step, not a calendar period.

Dimensional coherence requires:

- `rho`, `rb`, `r_a` and every entry of `Q_z` to have units `1 / HJB-time`;
- consumption, wage income, `Tt`, transfer `d` and adjustment cost to have asset-numeraire units `/ HJB-time`;
- `mu_b` and `mu_a` to have asset units `/ HJB-time`;
- `V_b*mu_b`, `V_a*mu_a`, flow utility and `Q_z*V` to share utility-flow units.

The implementation identities are explicit: `mu_b = rb*b + labor_income - d - cost - c` and `mu_a = r_a_effective*a + d` (`exports/matlab_faithful_two_asset_ha.py:159-166`). Thus an annual firm rate cannot be inserted into a quarterly HJB while the other rates/flows remain quarterly. The source proves the required common unit but does not consistently assign it.

## Firm-return scale finding

The active firm equations are (`src/ch5_two_asset_hank/multi_province/firm.py:103-110`):

`rk = mt * alpha / (K/Y)`

`ra0 = rk + after_tax_profit_over_K - delta`.

For corrected 2018, accepted data authority identifies `Y` as annual provincial GDP and `K` as the raw-NBS Track-A PIM capital stock in the same money unit. Common money rescaling cancels in `Y/K`, so this is a period problem, not a common currency multiplier problem. `K/Y` has units of years when `Y` is an annual flow. The positive-return components are therefore annual flow/stock rates. The source-backed `.025` depreciation interpretation is quarterly. The raw sum has no coherent period.

The capital stock is a stock-level object; its accepted construction uses annual GFCF and annual PIM depreciation `.096`, which is distinct from the firm/HJB `.025`. The PIM coefficient must not be substituted for firm depreciation. The price/base-year convention remains the accepted Track-A data contract; it does not repair the annual/quarterly mismatch.

The external market-asset numeraire remains unresolved. Internally, `Y/K` and profit/K are common-money-scale invariant, but the household grid unit and the macro `MU=10万元`, `NU=100 persons` bridge remain separately unresolved, especially for wage and transfer levels.

## Legacy MATLAB and dissertation evidence

| Source | Exact evidence | Consequence |
|---|---|---|
| dissertation `Main_Spine/c4.tex:8,24-29,40-69` | Declares a continuous-time HANK basis, uses `dt`, asset drifts and rate terms. | HJB is continuous-time; all flow rates/generator intensities require one common base time. |
| dissertation `Main_Spine/c4.tex:247` | “每个季度资本折旧为2.5%，每年资本折旧率为10%”. | `.025` depreciation has explicit quarterly authority. |
| dissertation `Main_Spine/c5.tex:144-151` | Defines `r_a=r_k-delta+profit/K` and household portfolio return. | Confirms the economic algebra, not compatible numerical periods. |
| dissertation `Main_Spine/c5.tex:224,236` | `rho=.05`; `delta=.0025`, neither with a period label. | `rho` period remains open; `delta` conflicts with code/c4. |
| dissertation `Main_Spine/c5.tex:274-280` | Uses a single period drawn from annual provincial data and iterates a numerical steady state. | Annual data frequency is proven; an outer iteration is not a calendar step. |
| protected `main.m:36` | Four policy periods are described as one year, one quarter each. | Legacy shock clock is quarterly, but this alone cannot annualize stationary HJB objects. |
| protected `multi_prov_HANK_12sts.m:47,65,69,86-93` | `Q_z` intensity `1/3`, `rho=.05`, `delta=.025`, `rb=.02`, gap `.07`, initial `rah=.09`; no conversion. | Parameters are passed as model-time literals. |
| protected `HANK_firm.m:44-55` | Computes annual-data `Y/K`, subtracts `.025`, and labels `ra` clipping a convergence guard. | The legacy implementation contains the frequency conflict; fidelity is not scientific authority. |
| protected `HANK_mp_1turn.m:35-40` | Aggregates lagged firm `ra` directly into `rah` with no transformation. | Direct wiring is historical provenance only. |

No inspected dissertation or protected source supplies an annual-to-quarterly firm-flow transformation, a discrete/gross-return interpretation, an external market-price mapping, or a statement that every HJB primitive is annual. Sources therefore cannot be reconciled silently.

## Current hard-bound inventory

| Object | Bound/device | Active status | Authority |
|---|---|---|---|
| used firm `ra` | `[.02,.09]` | active legacy/reference route | `EMPIRICAL_NUMERICAL_SAFEGUARD`; protected firm comment says it prevents convergence crashes |
| firm `wjt` | `[.8,1.3]` | active legacy/reference route | unresolved safeguard; absolute money/time calibration absent |
| firm profit `PIt` | floor `0` | active | unresolved structural/numerical floor |
| liquid derivative `Vb` | floor `1e-6` | active faithful HJB | numerical safeguard; with `gamma=2` it implies a maximum FOC consumption of `1000`, not an economic consumption cap authority |
| consumption | no direct numeric floor/cap | active | nonpositive values fail closed; any induced cap comes from the derivative floor |
| adjustment-cost denominator | `max(a,a_bar)`, `a_bar=1e-6` | active faithful/legacy | numerical singularity safeguard |
| asset grids | `b in [-2,5]`, `a in [0,10]` | active faithful/legacy | finite-domain numerical boundaries; not empirical wealth support authority |
| productivity grid | `z in [.8,1.3]` | active faithful/legacy | unresolved calibration support |
| transfer/control `d` | no finite hard cap | active | `chi0=.1` soft threshold, `chi1=2`, and boundary sign guards are FOC/numerical devices |
| labor | no explicit hard upper bound | active | nonnegative formula/domain only |
| effective illiquid return | taper from `1.0*rah` to `.9*rah` over the `a` grid | active faithful/legacy | source-faithful boundary taper, not a firm-to-HJB scale mapping |
| C1 `GovInv` | floor `0` | active successor route | Owner-frozen structural accounting residual |

Exact source locations are in `hard_bound_inventory.csv`. No bound was activated, changed or recommended numerically.

## Candidate mapping table

| Candidate | Source fidelity | Dimensional result | Ranking / scale | Decision and later test |
|---|---|---|---|---|
| A. `r_a=ra0` identity | historical wiring and dissertation algebra | fails under current annual-flow plus quarterly-delta operands | ranking preserved; level unchanged | `NOT_AUTHORIZED`; cannot proceed to runtime |
| B. convert annual firm-flow components to quarterly HJB flow before subtracting quarterly delta | motivated by annual `Y/K` and quarterly `.025` evidence | conditionally coherent only if HJB base time, flow conversion convention, and every other HJB flow are frozen quarterly | a common linear conversion preserves ranking of the positive firm-flow component but changes levels; delta placement matters | Owner/source freeze required; then a new bounded runtime diagnostic would be required |
| C. discrete/gross to continuous (`log`) conversion | no source identifies `ra0` as a gross or discrete compounded return | unsupported | unknown | excluded |
| D. dissertation `rk-delta+profit/K` | exact economic equation exists | same current frequency conflict as A | algebraically preserves ranking/level | equation authority does not authorize the current numerical identity |
| E. temporary return/wage hard bounds | Owner permits future diagnostic scaffolding | not an economic mapping | clips levels and can destroy ranking | fresh exact runtime task only after scale authority; never a final mapping |

No arbitrary shrinkage, z-score payoff, smoothing, cap, risk adjustment or normalization is admissible. The K1B standardized score remains a distinct attractiveness signal and cannot substitute for the payoff level.

## `STATIC_NO_FEEDBACK`

No numerical transformed-distribution table is produced. There is no fully source-backed non-identity mapping to apply to the accepted `ra0/rah` evidence. Even a seemingly mechanical `/4` requires a prior authority decision about whether the HJB base unit is a quarter, whether `Y` is a uniformly allocable annual flow, and how `rho`, `rb`, `Q_z`, wage, transfer and adjustment costs are converted. Manufacturing those assumptions would exceed this audit.

## Diagnostic-bound governance

Future diagnostic guards are admissible only under a fresh exact runtime task after payoff-scale authority closes. That task must preregister the bounded object and exact limits, persist province/turn (and where available cell) hit counts, label guards diagnostic rather than structural, preserve raw/unbounded receipts where design permits, prohibit post-result tuning, use a preregistered relaxation ladder, keep any bound-dependent steady state provisional, and widen/remove guards before scientific/Results acceptance. This audit sets no values and activates no guard.

## Zero-science call ledger

| Call class | Count |
|---|---:|
| trajectory / outer turn | 0 |
| HJB / KFE / household runtime / firm runtime | 0 / 0 / 0 / 0 |
| MATLAB runtime | 0 |
| K1B / K2 / GE / annual / IRF-shock / Results | 0 / 0 / 0 / 0 / 0 / 0 |

Allowed operations were static text reads, hashes, symbolic dimensional algebra, receipt writing, focused unit tests and Python compilation. The ledger is persisted in `zero_science_call_ledger.json`.

## Exactly one next gate

`ADDITIONAL_ZERO_SCIENCE_SOURCE_AND_CALIBRATION_PROVENANCE_CLOSURE_FOR_QUARTERLY_HJB_VS_ANNUAL_FIRM_FLOW`

Owner/Reviewer must issue a fresh exact zero-science task that resolves the c4/c5/code depreciation conflict and freezes one common calendar/model-time convention for `rho`, `rb`, `r_a`, `Q_z`, annual `Y/K`, wage, transfer and adjustment-cost flows. It must either source-authorize a complete conversion or explicitly recalibrate the model-time primitives. No Builder runtime follows from this report, and no successor task is published here.

## KFE and Results boundary

KFE remains `DIAGNOSTIC_ONLY`. Corrected-2018 finite-box upper-`b` leakage and MATLAB-style pinning are independent unresolved blockers; a payoff-scale decision cannot upgrade them.

Results eligibility=`FALSE`.
