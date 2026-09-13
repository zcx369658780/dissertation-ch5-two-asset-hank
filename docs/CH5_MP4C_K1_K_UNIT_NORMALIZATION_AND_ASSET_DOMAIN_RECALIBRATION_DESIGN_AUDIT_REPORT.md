# CH5 MP4C K1 — k-unit normalization and asset-domain recalibration design audit report

Date: 2026-09-14
Task ID: `CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT`

## Terminal classification

`MACRO_K_UNIT_REBASE_COHERENT__HOUSEHOLD_MONETARY_BRIDGE_UNPROVEN__BMAX_OWNER_SELECTION_REQUIRED`

This is a zero-science-runtime design result. It is not implementation authority, a calibrated steady state, or Results evidence. `Results eligibility=FALSE`.

## Repository identity and scope

- Actual fresh-fetched baseline: `d7d6d4718d27abe33a8915fd2b07ac042a125783` (`origin/main`).
- Branch: `codex/ch5-mp4c-k1-k-unit-asset-domain-design-audit-20260914`.
- Fresh isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-k-unit-asset-domain-design-audit-20260914-001`.
- Scientific model source, parameters, grids, guards and Results were not modified.
- Compact evidence: `docs/evidence/ch5_mp4c_k1_k_unit_normalization_asset_domain_design/`.

## Original MATLAB normalization

The designated source does not contain a global “divide every variable by 1000” rule. The active configuration and the adjacent comment are:

`param.GDP_multiplier=1000; param.POP_multiplier = 100; % 比较好的一个版本`

at `multi_prov_HANK_12sts.m:80-81`. The variable-level trace is:

| Object | Raw/source unit | Import/internal operation | Export operation | Source conclusion |
|---|---|---|---|---|
| Total GDP | `亿元` | `raw * 1000` | `/1000` | internal aggregate monetary unit is `10万元` |
| Capital | PIM-derived legacy series | PIM, then `*1000` | `/1000` | follows the GDP multiplier route; legacy raw-unit comment remains imperfect |
| Sector GDP | total and percentage share | `total * share / 100` | none traced | sector lines do not independently apply the GDP multiplier |
| Population | `万人` | `raw * 100` | `/100` | internal quantity unit is 100 persons |
| Firm labor | population/labor allocation | initialized from `N`, then hours/allocation | `/100` in output | aggregate quantity route, not household labor intensity |
| PIM investment | source investment series | `K0=I0/.1`; `Kt=(1-.096)Kt-1+It-1` | none traced | inherits the capital route |
| Firm investment | model capital flow | `I=K-Kprev+.025K` | none traced | same numeric unit as capital per model period |
| Government investment | `Kt0*GovInv_ratio` | enters the capital-stock route | none traced | name/stock-flow semantics require care |
| Household `C`, `Tt` | unknown real-money bridge | no GDP multiplier/divisor found | none traced | household per-capita flow scale unproven |
| Household `a,b,At,Bt` | unknown real-money bridge | grids and density means only | none traced | household per-capita stock scale unproven |
| `wjt` | firm marginal product per labor | guarded to `[.8,1.3]` | none traced | firm-wage-to-real-currency bridge unproven |
| Composite `w` | household wage input | degree-one nonlinear aggregation of 31 `wjt` values | none traced | aggregation explains numeric amplification but not a monetary unit |
| Productivity `Z` | Cobb-Douglas residual | `Y*K^-alpha*N^(alpha-1)` | none traced | scale-dependent unless money and person conversions are jointly specified |

The complete source locations and negative findings are sealed in `original_matlab_scaling_trace.json` and `source_identity.json`.

## Proposed k-unit convention

For the proven macro chain, a coherent re-expression is possible:

- one proposed monetary unit is `1k` currency;
- aggregate monetary values currently in `MU=100k` are multiplied numerically by 100;
- person quantities currently in `NU=100 persons` are also multiplied numerically by 100;
- equivalently, `GDP_multiplier` changes from 1000 to 100000 and `POP_multiplier` from 100 to 10000;
- `Y/N`, `K/N`, Cobb-Douglas `Z`, raw firm wage and rate expressions remain numerically invariant because aggregate money and person quantities receive the same factor.

This is a unit conversion, not economic recalibration. Expanding `amax` or `bmax` is economic-domain recalibration and must not be represented as a consequence of the macro unit change.

The household quantities `w`, `C`, `Tt`, `a`, `b`, `At` and `Bt` may remain numerically unchanged only if Owner accepts the missing identity that their existing numerical unit is already k per person (and per period for flows). Source evidence does not currently prove that identity. Therefore the audit returns `MONETARY_UNIT_BRIDGE_UNPROVEN`.

## Dimension classification

- Aggregate monetary stocks/flows: GDP/output, capital, firm investment, profit and aggregate tax/government flows, subject to the unresolved stock/flow role of named government objects.
- Household per-capita monetary stocks/flows: `a`, `b`, `At`, `Bt`, `C`, `Tt`, transfer control and adjustment cost, conditional on the household bridge.
- Person quantities: population and aggregate firm labor. Household labor `l` is an intensity/time choice, not headcount.
- Rates/dimensionless objects: `ra`, `rb`, borrowing gap, `rho`, depreciation, tax rates and the return guard. `chi0` and `chi1` are numerically invariant under a pure monetary rescale, while their time interpretation is a separate unresolved issue.
- Utility/value objects: CRRA/labor utility weights and the value function.
- Numerical-only objects: derivative floor, drift-direction tolerance and convergence tolerance.
- Dimension unresolved: `wjt`, composite `w`, productivity's real-unit interpretation, and the mixed-basis government account until an aggregate/per-capita reconciliation is proved.

The row-level classifications, including adjustment-cost and guard objects, are in `dimension_classification.csv`.

## Equation and parameter scaling

Let household monetary levels change as `x'=h*x`. In the canonical gauge that keeps utility and value numerically invariant:

- `alphac'=h^(gamma-1)*alphac`; `alphal` and the value function remain unchanged;
- `V_a` and `V_b` scale by `1/h`; consumption and wage scale by `h`; household labor is invariant;
- liquid and illiquid drifts scale by `h` when all monetary terms do;
- `a_bar'=h*a_bar`, derivative floor is divided by `h`, and drift tolerance is multiplied by `h`;
- `chi0` and `chi1` remain numerically unchanged for the monetary rescale; transfer cost and transfer-control FOC are homogeneous when `a_bar` follows the asset scale;
- `ra`, `rb`, borrowing gap, `rho`, `delta`, `Qz` and tax rates remain unchanged;
- the composite-wage aggregator is homogeneous of degree one in all `wjt` inputs;
- aggregate `Y`, `K`, `I`, profit/government monetary flows scale by 100, while `N/L` scale by 100, leaving `Z`, raw wage and capital-return ratios invariant;
- `Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt` mixes objects whose aggregate/per-capita basis is not proved, so no implementation may silently rescale it term by term.

For the special case `h=1`—the household bridge is accepted—the household numerical values, `alphac`, `a_bar`, derivative floor and drift tolerance do not change. For any `h!=1`, all transforms above are mandatory; merely changing grids and wages would not be unit-equivalent. Exact formulas and the parameter table are in `equation_scaling_transform.json` and `parameter_transform_table.csv`.

## Asset-domain design

`amax=100` is dimensionally coherent only conditional on the household k/person bridge. It would mean an individual illiquid-asset grid upper bound of 100k, not a provincial aggregate cap and not `At=100`. Relative to accepted `At≈7.14335–7.33469`, it is a broad safety domain, but the current evidence cannot establish its numerical precision or production adequacy without a later run.

The accepted scan has `Bt≈1.60951–4.69951`, all 9 b-marginals modal at the current `bmax=5`, and upper-bound mass about `0.130896–0.683403`. The current upper bound is therefore inadequate as a diagnostic domain. Evidence does not identify one outcome-independent replacement, so the bounded set is:

- `bmax=20`: roughly one household wage-flow magnitude and greater than four times the accepted maximum `Bt`;
- `bmax=50`: near median macro per-capita GDP (`≈51.5588k`) and greater than ten times the accepted maximum `Bt`.

Neither candidate is selected. Terminal decision: `BMAX_OWNER_SELECTION_REQUIRED`. Preserve `bmin=-2` only for the first diagnostic; its interpretation as -2k/person is also conditional on the household bridge.

With `I=J=20`:

| Domain | Spacing |
|---|---:|
| current `a=[0,10]` | `da=10/19=0.5263157895` |
| proposed `a=[0,100]` | `da=100/19=5.2631578947` |
| current `b=[-2,5]` | `db=7/19=0.3684210526` |
| candidate `b=[-2,20]` | `db=22/19=1.1578947368` |
| candidate `b=[-2,50]` | `db=52/19=2.7368421053` |

Keeping 20×20 is acceptable only for a first bounded domain diagnostic. It makes the a-grid ten times coarser and the b-grid about 3.14 or 7.43 times coarser. A separate precision-sensitivity gate is mandatory before production use.

## Macro and household reconciliation

Accepted same-state evidence gives:

| Object | Accepted numerical range | Proposed k-unit result | Authority |
|---|---:|---|---|
| provincial GDP | 1,548,400–99,945,200 MU | multiply by 100 to total k | proven |
| population | 35,400–1,234,800 NU | multiply by 100 to persons | proven |
| per-capita GDP | 32.2231–151.0310 | unchanged k/person; median 51.5588 | proven macro ratio |
| capital | 6,325,734–210,016,973 MU | multiply by 100 to total k | proven |
| raw firm wage | 7.7643–36.3915 | numerically unchanged k/person/period in macro algebra | household bridge unproven |
| guarded `wjt` | 1.3 | conditionally unchanged | monetary bridge unproven |
| composite `w0` | 13.8375–18.5197 | conditionally unchanged | monetary bridge unproven |
| `At` | 7.14335–7.33469 | conditionally unchanged | monetary bridge unproven |
| `Bt` | 1.60951–4.69951 | conditionally unchanged | monetary bridge unproven |

Thus per-capita GDP around 50 maps coherently to approximately 50k in the macro chain. It does not prove that `wjt=1.3`, household composite wage around 13–18 and household assets share that same real monetary and period basis. No factor 10, 1000 or 10000 may be introduced merely to align them.

## Bounded implementation proposal — not executed

After Owner freezes the household bridge and selects one b-domain candidate, a future exact task may:

1. Add a named normalization/domain adapter rather than alter the MATLAB-faithful export.
2. Convert aggregate `Y/K/I/GovInv/profit/tax` objects by 100 and aggregate `N/L` by 100; preserve rates.
3. Apply the conditional household transform consistently, including `alphac`, `a_bar`, derivative floor and drift tolerance if `h!=1`.
4. Set `amin=0`, `amax=100`, preserve `bmin=-2` for the first diagnostic, set only the Owner-selected `bmax`, and retain `I=J=20`.
5. Before any HJB, require 31/31 raw-to-k identities, invariant `Y/N`, `K/N`, `Z`, raw wage and return identities, composite-wage homogeneity, government-account basis closure, household symbolic/unit parity, and exact fresh grid receipts.
6. Only after all pre-science checks pass, run a fresh standalone 9-point grid at `rb=.02`, `ra={.06,.0675,.07}`, `w={13,15.5,18}` with the selected domain.
7. Stop before HJB on any identity/bridge mismatch; stop on any need to alter rates, HJB/KFE equations, guards, `ra` mapping or the time base; do not tune scaling or bounds to outcomes.

Candidate future implementation paths are limited to the corrected-2018 runtime/validator plus task-owned adapter/tests. The protected MATLAB-faithful export, MATLAB source and scientific equation/guard semantics remain unchanged unless separately authorized.

## Zero-runtime ledger and next gate

HJB=0; KFE=0; global outer=0; firm runtime=0; MATLAB runtime=0; K1B=0; K2=0; GE=0; downstream=0; shock=0; IRF=0; Results=0; scientific retries=0; parameter/grid changes=0. Deterministic offline audit builds=1.

Exactly one next Owner gate: `OWNER_REVIEW_HOUSEHOLD_K_UNIT_BRIDGE_AND_BMAX_SELECTION`.

STOP for independent ChatGPT Reviewer acceptance. No merge and no successor task publication.
