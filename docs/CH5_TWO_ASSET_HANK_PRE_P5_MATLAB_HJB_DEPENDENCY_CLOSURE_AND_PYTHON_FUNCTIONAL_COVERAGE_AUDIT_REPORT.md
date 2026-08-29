# Chapter 5 pre-P5 MATLAB HJB dependency closure and Python functional coverage audit

## Terminal classification

`MATLAB_HJB_DEPENDENCY_AUDIT_FINDS_MATERIAL_PYTHON_OMISSION_OR_AUTHORITY_GAP__P5_BLOCKED`

Acceptance level: read-only source/dependency closure and functional-coverage audit completed. The deferred P5 acceptance-design/evidence-sufficiency task was not executed. No implementation or scientific execution was authorized or performed.

Smallest exact gap: the designated MATLAB full HJB uses the state-dependent illiquid return

`r_a_eff(a)=rah*(1-0.1*(a/ahmax)^9)`

in the scientifically active illiquid drift `mu_a=r_a_eff(a)*a+d`, while accepted Python production uses `mu_a=r_a*a+d`. Existing O7 accepts drift signs, O12 accepts only the distinct line-90 initialization redesign, and P3/P4 operate on externally frozen drift/operator objects. No existing Owner decision explicitly adjudicates state-dependent versus constant illiquid return in the endogenous HJB. This is an equation-authority gap; this report does not decide which equation should govern.

## Live authority and source continuity

- Live start `origin/main`: `1e4721f115d3d3f153020f4909e743549cad54ba`.
- The live task explicitly deferred `CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW`; that task was not opened as execution authority or executed.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests` was empty.
- Designated MATLAB authority root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

## Complete custom dependency graph

```text
HANK_2ASSETS_HJB(param,grid,num,CHIh,results,show_result)
├── lab_solve2(l,params)
├── HANK3_FOC(results,paramchi,pa,pb,a,foreign)
├── HANK3_cost(results,paramchi,d,a,foreign)
└── HANK_gini(pp,g,value,asset,varname)    [five calls]
    └── Gini_coef2(pp,NumArr,Ntitle)
        └── fit(...,'smoothingspline')     [Curve Fitting Toolbox]
```

No other project custom function is called directly or transitively. `fzero`, `optimset`, `linspace`, `zeros`, `speye`, `sparse`, `spdiags`, `reshape`, `min`, `max`, `sum`, `abs`, `floor`, `ones`, `prod`, `sort`, `length`, `fit`, `trapz`, `round`, and optional plotting calls are MATLAB built-in/toolbox functions. Apparent calls such as `VbF(...)`, `Rah(...)`, `results.<field>`, cell-array `BBi{nz}`, and grid/policy array indexing are array/index expressions, not custom functions.

### Exact source identities and signatures

| Node | Exact designated-tree path | Bytes | Lines | SHA-256 | Signature |
|---|---|---:|---:|---|---|
| root | `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m` | 12227 | 427 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | `function results = HANK_2ASSETS_HJB(param, grid, num, CHIh, results, show_result)` |
| direct | `...\lab_solve2.m` | 287 | 11 | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | `function eq = lab_solve2(l,params)` |
| direct | `...\HANK3_FOC.m` | 565 | 22 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | `function d = HANK3_FOC(results,paramchi,pa,pb,a,foreign)` |
| direct | `...\HANK3_cost.m` | 691 | 25 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | `function eq = HANK3_cost(results,paramchi,d,a,foreign)` |
| direct | `...\HANK_gini.m` | 713 | 21 | `CF8ABE1EC9495E5167CA1B5254BB6C36524CBC59F7E4FF6F196C9081317F706E` | `function Gini = HANK_gini(pp, g, value, asset, varname)` |
| transitive | `...\Gini_coef2.m` | 936 | 54 | `4DBF06B30713A1875199EE3422F1D27507440853B0837A15E292724077FA8A70` | `function Gini=Gini_coef2(pp, NumArr, Ntitle)` |

### Duplicate and path-resolution audit

Recursive exact-name searches under the complete designated tree found one file each for `HANK_2ASSETS_HJB`, `lab_solve2`, `HANK3_FOC`, `HANK3_cost`, `HANK_gini`, and `Gini_coef2`; duplicate count is zero for every dependency. All custom nodes reside in the same designated directory as the root solver. Therefore, when that designated directory supplies the root HJB, ordinary MATLAB same-directory search resolves every custom edge to the exact paths above; no same-name ambiguity exists inside the authority tree. This was established statically without invoking MATLAB `which` or any runtime.

## Dependency effects

| Dependency | Initialization | policy/HJB | convergence | generator | stationary distribution | aggregates | post-processing |
|---|---|---|---|---|---|---|---|
| `lab_solve2` | yes | yes, via zero-liquid-drift/boundary candidate `l0` | indirectly | indirectly through selected policy | indirectly | indirectly | no |
| `HANK3_FOC` | no | yes, transfer candidates | yes | yes through `d` and drifts | indirectly | yes | no |
| `HANK3_cost` | no | yes, liquid drift and Hamiltonian budget | yes | yes | indirectly | yes | adjustment-cost statistics |
| `HANK_gini` | no | no | no | no | consumes solved distribution only | no feedback | yes only |
| `Gini_coef2` | no | no | no | no | no feedback | no feedback | yes only |

## MATLAB-to-Python functional coverage matrix

| Scientific function/behavior | MATLAB source and behavior | Active in domestic two-asset call? | Python coverage | Existing authority/materiality | Classification |
|---|---|---|---|---|---|
| CRRA utility/labor disutility | main 112,136,366 | yes | `economics.flow_utility` | required HA core; gamma/labor mapping previously accepted | EXACT_PYTHON_EQUIVALENT |
| consumption FOC | main 124–125 | yes | `economics.consumption_from_vb` | required policy primitive; P1/P2 | EXACT_PYTHON_EQUIVALENT |
| labor FOC from shadow value | main 127–128 | yes | `economics.labor_from_vb` | required policy primitive; P1/P2 | EXACT_PYTHON_EQUIVALENT |
| zero-liquid-drift labor/root relation | `lab_solve2`, main 100–113,117–119,126,134–135 | yes | labor FOC plus certified zero-drift shadow/root construction in `policies.py` | same equilibrium relation, different initialization/design | FUNCTIONALLY_INLINED_IN_PYTHON |
| adjustment cost | `HANK3_cost:22`, `chi0|d|+.5chi1*d^2/max(a,a_bar)` | yes, `foreign=0` | `economics.adjustment_cost` | O1 helper review | EXACT_PYTHON_EQUIVALENT |
| domestic transfer FOC above `a_bar` | `HANK3_FOC:19` | yes | `economics.transfer_candidate` | O1 | EXACT_PYTHON_EQUIVALENT |
| domestic low-a transfer FOC | MATLAB scales by `a`; Python by `max(a,a_bar)` | yes near lower a | accepted Python equation/KKT | explicit O1 decision | MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT |
| liquid budget/drift signs | main 263,352–353 | yes | `economics.asset_drifts` | O7 accepts sign structure; MATLAB-only `Tt/rb_gap` separately known | AUTHORIZED_REDESIGN_ALREADY_ACCEPTED |
| state-dependent illiquid return magnitude | main 81,85,193–194,264,365 | yes | absent; Python uses scalar `inputs.r_a` | not explicitly decided by O7/O12 or P1–P4 | UNRESOLVED_EQUATION_AUTHORITY_REQUIRED |
| line-90 initialization `Rah.*raah` | main 90 | initialization only | not inherited | O12 explicit Owner ACCEPT | AUTHORIZED_REDESIGN_ALREADY_ACCEPTED |
| state constraints/KKT/corners | main 117–154,194–195 | yes | `boundaries.py`, `policies.py` | O3–O6 accepted redesign | AUTHORIZED_REDESIGN_ALREADY_ACCEPTED |
| upwind asset generator | main 155–232,263–333 | yes | `generator._asset_generator` / `build_operator` | P3 and O9 | EXACT_PYTHON_EQUIVALENT under orientation/common input |
| productivity generator | main 64–66 two-state block | yes | production diffusion plus accepted common-Q adapter evidence | O2/P3 | AUTHORIZED_REDESIGN_ALREADY_ACCEPTED |
| implicit HJB update/convergence | main 240–260 | yes | `hjb.solve_hjb` | same numerical object under accepted contracts | FUNCTIONALLY_INLINED_IN_PYTHON |
| stationary transpose/solution | main 334–345 arbitrary pin | yes | `kfe_contract.py`, `kfe.py` with uniqueness/residual checks | O9/O10 and structural diagnostic | MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT |
| mass/density/aggregates | main 341–354,387–403 | yes | `kfe.py`, `steady_state.py`, policy snapshot | O11/P4 | AUTHORIZED_REDESIGN_ALREADY_ACCEPTED |
| inequality/Gini | main 420–424; `HANK_gini` -> `Gini_coef2` | after solve only | absent | no feedback to HA core | POSTPROCESSING_NOT_REQUIRED_FOR_HA_CORE |
| MPC/borrowing/tax/accounting statistics | main 355–372,399–411 | after solve only | partial primitives available, no full output API | Results/reporting, not HJB/KFE correctness | POSTPROCESSING_NOT_REQUIRED_FOR_HA_CORE |

## `lab_solve2` finding

`lab_solve2` solves

`l = [(alphac/alphal)(1-tau)wz]^frisch_l * [(1-tau)wz*l + tempMat]^(-ga*frisch_l)`.

Equivalently, with `c=(1-tau)wz*l+tempMat`, it enforces

`alphal*l^(1/frisch_l) = alphac*(1-tau)wz*c^(-ga)`.

It is not merely dead initialization code. MATLAB calls it in every state to build `l0`, `c0`, and `v02`; later `l0` enters liquid-boundary derivative closures (117/119), the zero-liquid-drift consumption candidate `C_0` (126), and the selected labor whenever `Ic_0` is active (134–135). It therefore supplies a scientifically active zero-liquid-drift labor condition.

Python has no literal `lab_solve2`, but it implements the same labor stationarity through `labor_from_vb` and solves the liquid zero-drift condition through `_zero_liquid_shadow`, `_certified_zero_drift_root`, and boundary/corner candidates in `policies.py`; KKT labor residuals are independently checked in `boundaries.py`. Python accepts an explicit initial value rather than embedding this legacy initializer. O12 and the rate-matched initialization tasks already reject literal initializer identity as a production requirement. Result: `FUNCTIONALLY_INLINED_IN_PYTHON`, not a missing scientific equation.

## `HANK3_FOC` / `HANK3_cost` domestic and inherited-foreign finding

Every main-HJB invocation passes `foreign=0` (FOC lines 137–140; cost lines 148–149,263,352–353,369). Thus only:

- `d=S(pa/pb)*a/chi1` in production FOC; and
- `chi0*abs(d)+chi1*d^2/(2*max(a,a_bar))` in cost

are reachable. The foreign branches' `price=PFt*et/Pt` (all hard-coded one), `fixcost`, `fixcost2`, and price conversion cannot become active in this two-asset domestic HJB. `fixcost`/`fixcost2` are read locally but only foreign cost/FOC logic uses them materially; zero values in accepted fixtures are neutral. O1 already adjudicates the domestic low-a inconsistency between bare-`a` FOC and `max(a,a_bar)` cost in favor of the accepted Python equation. No foreign/third-asset branch is a Python omission.

## `HANK_gini` and complete transitive closure

The five calls compute Ginis for liquid assets, illiquid assets, consumption, effective labor, and income after policies and stationary density have already been solved. `HANK_gini` reshapes and sorts the supplied distribution/value arrays, builds a cumulative value-share curve, then calls `Gini_coef2`. `Gini_coef2` sorts again, normalizes the curve, fits a smoothing spline, integrates it with `trapz`, and rounds the resulting coefficient to four decimals. With `pp=0`, its plotting branch is inactive.

Neither function mutates input state or feeds any result back into policies, `convergent`, generator, stationary solve, or household aggregates. Their absence in Python is a future Results/post-processing gap only. The transitive graph closes at MATLAB/Curve Fitting toolbox functions; no source is missing.

## Three-asset inheritance residue

| Residue | Source evidence | Two-asset status | Classification |
|---|---|---|---|
| `alphap` | read main line 3, never subsequently referenced | dead | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| `VafF`,`VafB` | allocated lines 71–72, never read/written afterward | dead | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| `Raf` | allocated line 75, never used | dead | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| FOC `foreign==1` | no caller passes one | unreachable | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| cost `foreign==1` | no caller passes one | unreachable | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| `PFt/Pt/et/price` | local constants used only by foreign branch | inactive | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| `fixcost/fixcost2` foreign changes | only active in unreachable foreign branch | inactive; accepted values zero | UNUSED_OR_INACTIVE_THREE_ASSET_RESIDUE |
| `alphac` | hard-coded one and scientifically active in utility/FOCs | active, not a three-asset state | FUNCTIONALLY_INLINED_IN_PYTHON |

Dead residues should not be ported merely for filename/line similarity.

## State-dependent `raah/Rah` equation-authority finding

MATLAB line 81 defines

`raah(a)=rah*(1-0.1*(ahmax/ah)^(-9)) = rah*(1-0.1*(a/ahmax)^9)`.

At `a=0`, MATLAB's limiting/numeric value is `rah`; at the upper bound it is `.9*rah`; it decreases monotonically between them. The active illiquid return flow is

`raah(a)*a = rah*a - 0.1*rah*a^10/ahmax^9`.

Therefore the difference from Python's constant-return flow is zero at `a=0`, equals `-0.1*rah*ahmax` at the upper bound, and is nonzero at every positive interior node. For the native `ahmax=10` and `rah=.04`, the upper-node flow is `.36` versus Python `.4`, an exact difference of `-.04`.

Complete uses:

| Lines | Use | Scientific status |
|---|---|---|
| 81,82–88 | build and broadcast the schedule into `Rah` | active input to policies/operator |
| 90 | `tempMat=Rah.*raah+Rb.*b+Tt`, effectively `raah^2` rather than return times assets | initialization-only; O12 legacy redesign |
| 193 | `MhF=max(dhF,0)+Rah.*aaah` | active HJB illiquid forward drift/generator |
| 194 | upper-a backward boundary `dhB+Rah*ahmax` | active boundary policy/generator |
| 264 | final `mh=dh+Rah.*aaah` | active stationary generator |
| 365 | `AhTax=Aht*rah-sum(a*raah*g...)` | post-solve statistic, but reflects the same schedule |

Authority search result:

- O7 states that budget/drift **signs** align and contains no decision on the state-varying return magnitude.
- O12 explicitly accepts only line 90's `Rah.*raah` initialization as legacy behavior not inherited.
- O2 concerns the productivity process, not the illiquid-asset return schedule.
- The earlier parity-prep matrix explicitly recorded `confirm return schedule (Rah)` as pending, while a broad “legacy shortcuts” row mentioned the taper without an equation-level Owner decision.
- P1/P2 did not establish full-grid endogenous return-schedule equivalence; P3/P4 used frozen drifts/common operators and therefore cannot adjudicate how each HJB generates `mu_a`.

Accordingly, neither “copy the taper into Python” nor “discard it as legacy” is authorized. The smallest gap is the equation choice between state-dependent `r_a_eff(a)` and constant `r_a`. Classification: `UNRESOLVED_EQUATION_AUTHORITY_REQUIRED` and `MATERIAL_PYTHON_OMISSION_CANDIDATE`; P5 remains blocked pending Owner/reviewer decision.

## Output/statistics coverage

| MATLAB output | Meaning | Python coverage | Scope classification |
|---|---|---|---|
| `g` | stationary probability mass (`gg`) | KFE mass | HA_CORE_REQUIRED, covered |
| `C`,`l` | mass-weighted consumption/effective labor cells | policy plus stationary mass | HA_CORE_REQUIRED, covered by components |
| `Ct,Lt,At,Bt` | core household aggregates | stationary expectations | HA_CORE_REQUIRED, covered |
| `convergent` | HJB convergence flag | HJB diagnostics | HA_CORE_REQUIRED, covered more strictly |
| `aaah`,`rb_neg`,`min_Household_Income` | grid/rate/min-income convenience outputs | primitives available | diagnostic/convenience, not missing core |
| `Bt_pos`,`Bt_neg`,`Borrow`,`Borrowint` | borrowing composition/statistics | not exposed as final API | later Results/post-processing |
| `Ut`,`St`,`Bdotres`,`UC_new` | utility/saving/budget/marginal-utility summaries | primitives/diagnostics partly available | diagnostics or later Results |
| `AtTax` | taper-return wedge statistic | absent | post-processing, but exposes the unresolved active return equation |
| `CHI_H`,`CHI_F` | adjustment-cost totals | policy cost exists; no aggregate field | later Results/post-processing (`CHI_F` domestic zero) |
| `At_1,Bt_1,Lt_1,Ct_1` and dots | prior-period bookkeeping/differences | absent | outer-model bookkeeping, not household HA core |
| Gini fields | five smoothed/rounded inequality statistics | absent | later Results/post-processing |
| MPC | computed locally but not written (commented output) | absent | inactive output / future Results |
| `Borrowint`, Ginis rounded/smoothed | reporting conventions | absent | must not be treated as core parity requirements |

Python's richer KKT, generator, recurrent-class, left-nullity and KFE residual diagnostics are accepted redesigns and need not reproduce MATLAB's output schema.

## Contradiction audit against O1–O12 and P1–P4

| Accepted evidence | New closure result | Contradiction? | Narrow effect |
|---|---|---|---|
| O1 low-a FOC limitation | exact helper closure confirms domestic formula and inactive foreign branches | no | reinforces O1 |
| O7 drift signs | MATLAB and Python retain the same `+return*a + d` sign | no direct contradiction | does not cover state-dependent return magnitude |
| O12 initialization | exact `lab_solve2`/line-90 closure confirms separate initializer | no | O12 remains accepted; not authority for lines 193/194/264 |
| P1 primitives | helper equations otherwise map or are accepted redesigns | no | `raah(a)` was not an explicitly frozen primitive comparison |
| P2 local policy | transfer/cost/KKT evidence remains accepted | no | return schedule changes `mu_a` outside the isolated helper comparison |
| P3 generator | common externally frozen drift matrices match | no | does not prove endogenous HJB drift construction matches |
| P4 KFE | same frozen generator gives same stationary object | no | downstream evidence remains valid conditional on the generator |

No accepted result is revoked. The smallest affected sufficiency claim is only the inference that O7 plus P1–P4 had closed **all endogenous illiquid-drift magnitudes**. They did not adjudicate the taper. Therefore the deferred P5 review cannot resume yet.

## Files read/written and external artifacts

Read: live task; `AGENTS.md`; both project rules; five required GitHub reports; all accepted Python files under `src/ch5_two_asset_hank/` relevant to economics, policies, boundaries, HJB, generator, KFE, steady state, productivity and contracts plus relevant tests; the complete designated MATLAB root solver and all five closed custom dependency nodes; directory-wide duplicate-name inventory.

Repository write: only this report. External artifacts written: none.

## Forbidden-operation check

PASS:

- MATLAB invocation/model/HJB/KFE calls: 0.
- Python invocation/model/HJB/KFE/steady-state calls: 0.
- P1–P4 and R4 reruns: 0.
- Deferred P5 review executed: no.
- MATLAB or Python production/tests modified: no.
- Adapter/functionality/statistics implemented: no.
- Equations/tolerances/parameters changed: no.
- Parameter tuning, AR(1), transition, IRF, calibration extension, dynamics or Results entered: no.
- P5 acceptance issued: no.

## Recommended next gate

Publish the smallest Owner/reviewer equation-authority decision task, limited to one question: should the Chapter 5 accepted illiquid drift use MATLAB's tapered `rah*(1-0.1*(a/amax)^9)*a+d`, Python's constant `r_a*a+d`, or an explicitly cited dissertation equation? The gate must inspect/cite the authoritative economic equation, state whether the MATLAB taper is intended economics or legacy numerical code, and decide whether existing P1–P4 need only a scope annotation or a new bounded primitive test. Do not authorize implementation until that decision is published. The deferred P5 acceptance-design review remains deferred.

