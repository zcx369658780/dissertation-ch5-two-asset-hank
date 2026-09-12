# CH5 MP4C K1 — G1 vs G2 HA/HJB mechanism zero-science diagnostic report

Date: 2026-09-12

Task: `CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC`

Baseline: `origin/main` at `eb3109920cca0650fa3f83eef92422f070c332e9`

Prior accepted candidate: `ab6b19022d920a8929a2ee66cc5511be6f602557`

## 1. Verdict

`G2_STRESS_MIXED_ACROSS_NEWLY_UNSATURATED_AND_STILL_SATURATED_RETURN_REGIMES__PATH_HISTORY_AND_WAGE_INTERACTION_NOT_IDENTIFIABLE_FROM_PERSISTED_EVIDENCE__BOUNDED_INSTRUMENTATION_TASK_REQUIRED`

The persisted treatment evidence does not support a single-channel explanation. Newly unsaturated G2 observations are uniformly nonconverged, but the largest HJB statistic and the global cell extrema occur in the still-upper-saturated partition. Stress is predominantly interior in the top-cell and threshold views, while important worst-statistic cases remain boundary-linked. G1 already contains very large cell-level stress, and several of its worst cells improve under G2. Because treatment paths diverge after turn 1 and the accepted evidence does not persist derivatives, pre-selector candidates, or iteration traces, the return, wage, selector, and path-history channels cannot be separated causally.

Results eligibility: `FALSE`.

## 2. Authority, scope, and evidence integrity

- Fresh live baseline: `eb3109920cca0650fa3f83eef92422f070c332e9`.
- Exact task blob: `e458647566d34529f04049e188f6c68f1c2ea497`.
- Analysis population: treatment turns 2–5 only, `124` matched province-turn observations; turn 1 is common-bootstrap context only.
- Cell population: `99,200` saved cells per path, matched by province, turn, and zero-based `(i_b,i_a,i_z)` on `b=linspace(-2,5,20)`, `a=linspace(0,10,20)`, `z=(.8,1.3)`.
- Comparison scope: `MATCHED_PROVINCE_TURN_AND_GRID_CELL_WITH_PATH_HISTORY_DIVERGENCE__NOT_CAUSAL`.
- Immutable external evidence root: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-vs-g2-evidence-20260912-001`.
- External manifest readback: `PASS`, `1,041` entries, zero mismatches; manifest SHA-256 `FC176A6B2809A012D36BE79428630C9E371C9262ABCA4AF1CFAA57295B9676CB`.
- Accepted material drift tolerance: `1e-12`.

All statistics below are computed from already persisted JSON/CSV/NPZ and inspected source. They are descriptive and do not turn unmatched path states into same-state causal experiments.

## 3. Zero-science execution ledger

| Call class | New calls |
|---|---:|
| trajectory | 0 |
| outer turn | 0 |
| HJB | 0 |
| KFE | 0 |
| household runtime | 0 |
| firm runtime | 0 |
| MATLAB runtime | 0 |
| K1B | 0 |
| K2 | 0 |
| GE | 0 |
| annual downstream | 0 |
| shock/IRF | 0 |
| Results | 0 |

Only static reads, hashing, NumPy/SciPy summaries, focused tests, and report/evidence generation were performed. No `src/` science, equation, parameter, guard, grid, tolerance, or solver was modified.

## 4. Convergence-switch localization

Across 124 treatment province-turns:

| Switch | Count |
|---|---:|
| both converged | 0 |
| G1 converged -> G2 nonconverged | 18 |
| G1 nonconverged -> G2 converged | 6 |
| both nonconverged | 100 |

G1 hit the 100-iteration ceiling in `106/124` observations; G2 in `118/124`.

Switches by turn:

- Turn 2: losses `内蒙古, 河南`; gains `重庆, 贵州`.
- Turn 3: losses `北京, 广西, 宁夏`; gain `江西`.
- Turn 4: losses `北京, 河北, 福建, 广西, 四川, 宁夏, 新疆`; gains `安徽, 广东, 重庆`.
- Turn 5: losses `河北, 内蒙古, 辽宁, 吉林, 四川, 新疆`; no gains.

Repeated losses, twice each: `内蒙古, 北京, 四川, 宁夏, 广西, 新疆, 河北`.

The worst five G2 HJB statistics are led by 四川 turn 4 (`203.2133848859883`, G1 `5.6053643393561003e-08`, still upper, wage upper, loss), 甘肃 turn 3 (`170.45507307121323`, still upper, wage unsaturated), 重庆 turn 3 (`68.33`, still upper, wage upper), 安徽 turn 3 (`65.34`, still upper, wage upper), and 山东 turn 2 (`50.93586949139517`, newly unsaturated, wage upper). This ordering itself shows that losses and large statistics are not confined to the newly unsaturated return regime.

## 5. Return-regime partition

No lower-return hits occur.

| G2 return regime | n | G2 converged | G2 ceiling | HJB statistic min / median / max |
|---|---:|---:|---:|---:|
| A: still upper-saturated at `.35` | 84 | 6 | 78 | `1.3264e-10 / 1.034304 / 203.213385` |
| B: newly unsaturated after G1 upper hit | 40 | 0 | 40 | `0.002091 / 0.639330 / 50.935869` |

Convergence-switch composition is A: 9 losses, 6 gains, 69 both nonconverged; B: 9 losses, 0 gains, 31 both nonconverged. Thus B is uniformly nonconverged but does not contain the maximum HJB statistic or global transfer/cost/drift cell. A and B both carry material stress, so the correct localization is mixed.

## 6. Wage-guard interaction

The wage guard is unchanged at `[.8,1.3]`.

| Return × wage regime | n | G2 converged | HJB median | HJB max |
|---|---:|---:|---:|---:|
| A + upper | 61 | 6 | `0.790203` | `203.213385` |
| A + lower | 16 | 0 | `1.070201` | `7.508101` |
| A + unsaturated | 7 | 0 | `1.805993` | `170.455073` |
| B + upper | 23 | 0 | `0.668705` | `50.935869` |
| B + lower | 9 | 0 | `0.551361` | `4.480200` |
| B + unsaturated | 8 | 0 | `0.540224` | `25.710620` |

Still-binding wage upper observations contain both all six G2 convergences and the global cell extrema, while a wage-unsaturated A observation contains the second-largest HJB statistic. These are descriptive clusters, not evidence that either the wage guard or its relaxation is the causal remedy. The persisted path comparison cannot identify return × wage × history interactions.

## 7. Cell-level localization

The global G2 maxima for all four required metrics occur at the same interior cell: 湖北 turn 2, index `(1,18,0)`, coordinate `(b=-1.6315789474,a=9.4736842105,z=.8)`, liquid transition `0->B`, transfer transition `B->B`, still-upper return and wage-upper regime.

| Metric | G1 | G2 | G2-G1 |
|---|---:|---:|---:|
| transfer `d` | `4.952212` | `-42,699,421.260055` | `-42,699,426.212267` |
| adjustment cost | `3.083908` | `192,453,176,175,102.66` | `192,453,176,175,099.56` |
| `mu_a` | `6.730478` | `-42,699,418.148090` | `-42,699,424.878568` |
| `mu_b` | `-8.036121` | `-192,453,133,476,680.03` | `-192,453,133,476,672.00` |

Worst-HJB local context is different: 四川 turn 4 has statistic `203.2133848859883`; its local reported extreme at `(19,16,1)`, coordinate `(b=5,a=8.4210526316,z=1.3)`, is upper-b and changes `FB->BB`, with `d=52,642.3606` versus G1 `-2.6098` and cost `329,087,416.93` versus `1.0698`.

Across each metric's global G2 top 100, transfer and `mu_a` have `93` interior and `7` boundary rows; adjustment cost and `mu_b` have `95` interior and `5` boundary rows. Combined, that is `376/400` interior and `24/400` boundary. The corresponding face count is upper-a `6` and upper-b `22`; corners may count on two faces.

The absolute-cell distributions also show heavy tails rather than a uniformly shifted body. For example, transfer median moves from G1 `1.513810` to G2 `3.082981`, while the maximum moves from `11,880,590.2634` to `42,699,421.2601`. Adjustment-cost median moves from `.597188` to `2.271544`, while the maximum moves from `2.9798002022668e13` to `1.9245317617510e14`.

## 8. Policy-branch transitions

The accepted letters are source-faithful upwind/control indicators, not independent economic labels.

Liquid transitions over 99,200 matched cells are: `FF 49,666`, `FB 20,873`, `BF 9,547`, `BB 9,092`, `F0 4,282`, `0F 2,138`, `B0 1,442`, `0B 1,436`, `00 724`. Changed cells: `39,718/99,200 = 40.0383%`.

Transfer transitions are: `BB 25,748`, `FB 24,216`, `FF 17,966`, `BF 9,195`, `00 7,805`, `F0 4,786`, `0B 4,212`, `B0 2,989`, `0F 2,283`. Changed cells: `47,681/99,200 = 48.0655%`.

Across the 400 G2 top-100 rows pooled over four metrics, every destination liquid and transfer label is `B`: liquid `F->B 264`, `B->B 110`, `0->B 26`; transfer `F->B 194`, `B->B 194`, `0->B 12`. This localizes the saved extreme policies but does not reconstruct a missing pre-selector/KKT residual.

## 9. Boundary versus interior

Material outward face hits at tolerance `1e-12`, denominator `4,960` per face/path:

| Path | lower-a | upper-a | lower-b | upper-b | total |
|---|---:|---:|---:|---:|---:|
| G1 | 0 | 1,113 | 0 | 3,249 | 4,362 |
| G2 | 0 | 1,580 | 0 | 2,215 | 3,795 |

The total decreases by `567` under G2, so the deterioration is not a pure outward-boundary failure. Threshold sensitivity is also predominantly interior: for adjustment cost above `1e6`, G1 has `739` interior/`64` boundary cells and G2 has `847`/`93`; for `|mu_b|>1e6`, the same counts apply. Nevertheless, the worst HJB observation has an upper-b extreme and several top-100 rows lie on upper faces. Attribution is therefore primarily interior extreme amplification with material boundary-linked worst-statistic cases: a mixed interaction, not a boundary-only classification.

## 10. Source-law trace

- `src/ch5_two_asset_hank/multi_province/household_adapter.py:43-65,200-219` maps `results.rah` to `HouseholdInputs.r_a`, maps the composite wage to `HouseholdInputs.wages`, freezes the accepted grid/call interface, and does not itself call the solver.
- `src/ch5_two_asset_hank/economics.py:58-71` defines the tapered effective illiquid return; `:25-41` defines the transfer FOC from raw `v_b`; `:10-13` defines adjustment cost; `:118-137` places effective return and `d` in `mu_a`, and labor income, `d`, cost, and consumption in `mu_b`. Wage enters through labor income.
- `src/ch5_two_asset_hank/matlab_faithful_policy.py:127-155` selects liquid `B/F/0`; `:159-222` constructs and selects transfer `F/B/0`; `:224-267` applies effective return, builds `mu_a/mu_b`, and maps drift directions/rates.
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py:83-116` constructs directional value derivatives, selects local policies, assembles the operator, performs the direct update, and defines the convergence statistic as `max(abs(value-old))`.

The accepted chain is therefore `r_a -> effective illiquid return -> derivative/Hamiltonian inputs -> transfer FOC -> d -> adjustment cost -> mu_a/mu_b -> policy/boundary selector -> HJB operator/update/statistic`. The source trace shows where stress can propagate; it does not identify which missing intermediate first destabilizes a particular divergent path.

## 11. Descriptive associations

Every number in this section is `DESCRIPTIVE_ONLY_NOT_CAUSAL` (`n=124`):

- consumed `Δr_a` versus G2 HJB statistic: Pearson `.077882`, Spearman `.065471`;
- consumed `Δr_a` versus G2 iteration ceiling: Pearson `-.131637`, Spearman `-.151771`;
- converted raw `rah` versus G2 HJB statistic: Pearson `.063139`, Spearman `-.020406`.

These weak/mixed associations do not support a monotone return-level explanation.

## 12. Required attribution split

### A. Stress already present under G1

G1 has `106/124` ceiling hits and extreme saved cells. Its largest transfer/cost/`mu_a`/`mu_b` cell is 云南 turn 4, interior `(10,9,0)`: `|d|=11,880,590.2634`, cost `2.9798002022668e13`, `|mu_a|=11,880,589.3161`, and `|mu_b|=2.9797990143076e13`.

### B. G2 incremental stress

G2 increases convergence losses net of gains (`18` versus `6`), raises ceiling hits from `106` to `118`, increases changed policy cells, and creates the 湖北 turn-2 global maxima shown above. G2 also increases counts above `1e6` for cost/`|mu_b|` from `803` to `940`.

### C. G2 improvements relative to G1

G2 is not uniformly worse. At the G1 global 云南 turn-4 extreme, matched G2 falls to `d=1,535.8153` and cost `498,107.4272`. Other G1 extremes improve sharply: 天津 turn 3 from `d=-9,646,879` and cost `1.1788e13` to `-22.76` and `67.91`; 陕西 turn 2 from `-6,678,970` and `6.5197e12` to `-1.55` and `.508`; 广东 turn 5 from `-6,344,935` and `4.2495e12` to `0/0`.

### D. Return-unsaturated association

All `40/40` newly unsaturated observations are nonconverged and hit the ceiling, but their HJB maximum (`50.94`) is below the A-partition maximum (`203.21`). They are associated with stress, but do not contain all or the worst stress.

### E. Still-binding wage association

Wage-upper rows are common (`84/124`) and contain the global cell maxima and worst HJB statistic, but also contain all six G2 convergences. Wage binding therefore does not uniquely classify the outcome.

### F. Unresolved interaction

The accepted evidence lacks value derivatives, directional derivatives, pre-selector candidate/raw drifts, iteration-by-iteration traces, and a standalone faithful-route KKT residual. Saved final policy arrays precede the saved updated `value` solve in the last HJB iteration, so exact policy derivatives must not be reconstructed from saved final `V`. These omissions, combined with post-turn-1 path divergence, prevent separation of return, wage, branch-selection, boundary, and history channels.

## 13. KKT, KFE, and Results boundaries

- Standalone KKT residual: `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`; no proxy PASS/FAIL was constructed.
- KFE caveat: `ALL_PRIOR_KFE_RESULTS_REMAIN_DIAGNOSTIC_ONLY`.
- Results eligibility: `FALSE`.
- This report does not authorize G3/G4, longer G2, wage relaxation, K1B, K2, GE, steady-state acceptance, IRF, or Results.

## 14. Exactly one recommended next gate

`BOUNDED_DIAGNOSTIC_RUNTIME_WITH_ADDITIONAL_DERIVATIVE_PRESELECTOR_AND_ITERATION_TRACE_INSTRUMENTATION__NO_SCIENCE_PARAMETER_CHANGE`

The gate must remain separately authorized and bounded. This task does not publish it, execute it, or change any scientific parameter.

## 15. Deliverables

- `validators/multi_province/k1_g1_vs_g2_ha_hjb_mechanism/__init__.py`
- `validators/multi_province/k1_g1_vs_g2_ha_hjb_mechanism/analyze.py`
- `tests/test_mp4c_k1_g1_vs_g2_ha_hjb_mechanism.py`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/province_turn_panel.csv`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/province_turn_panel.json`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/cell_extremes.json`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/global_top100_cells.json`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/descriptive_associations.json`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/source_availability.json`
- `docs/evidence/ch5_mp4c_k1_g1_vs_g2_ha_hjb_mechanism/summary.json`
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_REPORT.md`

No successor task is created. Independent Reviewer acceptance remains required.
