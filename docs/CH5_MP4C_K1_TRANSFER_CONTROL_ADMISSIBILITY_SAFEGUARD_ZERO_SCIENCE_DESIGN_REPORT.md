# CH5 MP4C K1 — transfer-control admissibility safeguard zero-science design report

Date: 2026-09-13
Task: `CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN`

## 1. Classification

`TRANSFER_CANDIDATE_EXPLOSIVE_FINITE_TAIL_CONFIRMED__RAW_CELL_DISTRIBUTION_NOT_PERSISTED__NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED`

The accepted traces prove that finite explosive raw candidates exist, but they do not persist the cell-level raw candidate arrays required to compute exact raw hit shares, branch-specific hit shares, requested full raw percentiles, or cell-level raw sign frequencies. A numeric ladder is therefore not frozen or recommended as uniquely identified.

Preferred semantics, conditional on a later numeric freeze:

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`

This means preserving every raw FOC receipt, excluding an out-of-range raw branch from selector competition, and retaining only the already existing zero-transfer option rather than manufacturing a clipped FOC candidate.

Results eligibility=`FALSE`.

## 2. Authority, baseline, and isolation

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh live `origin/main`: `72529267b9f923411bdbbe7c423e15d55114a3f9`.
- Exact task SHA-256: `B49B891EB655BDE52BBF807776F8E1E95C13287AE0907BDA8816E0B4CCFAE038`.
- Branch: `codex/ch5-mp4c-k1-transfer-control-admissibility-zero-science-design-20260913`.
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-transfer-control-design-20260913-001`.
- Worktree started clean from live main.
- Accepted external evidence root: `D:\ProjectTemp\ch5-k1-g1-vs-g2-ha-hjb-instrumented-evidence-20260912-001`.
- Accepted external manifest SHA-256: `741DBF595C0DF6698F40A8FA2625102759190291B27937B88F02D6FFE9EC973A`.
- Manifest entries excluding itself: `1,357`; consumed identities reverified: `630/630`.
- Instrumented traces: `310`; grid-hash checks: `310/310`; HJB-iteration summaries: `27,196`.

The repository named in the prior local skill-governance session was not reused. The dirty `D:\Zotero-Analytical-Workflow` checkout was not cleaned or modified by this task.

## 3. Zero scientific-call ledger

| Call family | New calls |
|---|---:|
| trajectory / outer turn | 0 / 0 |
| HJB / KFE | 0 / 0 |
| household / firm runtime | 0 / 0 |
| MATLAB runtime | 0 |
| K1B / K2 / GE | 0 / 0 / 0 |
| annual downstream / shock-IRF / Results | 0 / 0 / 0 |

Only static JSON/NPZ reads, SHA-256 checks, NumPy analysis, symbolic adjustment-cost evaluation, focused tests, and report/evidence generation were performed.

## 4. What the accepted evidence actually persists

For each HJB iteration and each raw branch `d_bb`, `d_bf`, `d_fb`, `d_ff`, the accepted trace persists:

- count and nonfinite count;
- min, median, p95, p99, max and absolute max;
- array SHA-256;
- one absolute-maximum witness with grid-cell identity;
- selected checkpoint cells and dynamic extrema.

It does **not** persist the full raw branch arrays. Array hashes cannot be inverted, and per-array summaries cannot be pooled into exact cell-level quantiles or threshold counts. By contrast, each accepted `hjb_return.npz` persists the full selected `d` array for the final HJB iteration of that province call. Selected-control statistics below are therefore exact for that explicitly limited population.

Population distinction:

- raw summary receipts represent `87,027,200` branch-cell candidate evaluations: `27,196 iterations × 800 cells × 4 branches`;
- exact selected population contains `248,000` final-iteration cell controls: `310 calls × 800 cells`;
- turn 1 is retained once under each accepted path because both accepted G1 and G2 evidence trees persist the common bootstrap separately;
- no summary is relabelled as a raw cell observation.

## 5. Raw pre-selector candidate diagnostics

All represented raw candidates are finite: NaN=`0`, `+Inf=0`, `-Inf=0`.

| Raw branch | Represented count | Global min | Global max | Median of per-array medians | Median of per-array p99 |
|---|---:|---:|---:|---:|---:|
| `d_bb` | 21,756,800 | -2.785464010e9 | 1.714597479e12 | -1.024213 | 483.885499 |
| `d_bf` | 21,756,800 | -2.710347230e9 | 4.190962675e9 | -1.082552 | 510.216473 |
| `d_fb` | 21,756,800 | -2.623956919e9 | 1.611417707e12 | -1.004089 | 513.867920 |
| `d_ff` | 21,756,800 | -2.292697579e9 | 4.185028038e9 | -1.084542 | 460.823407 |

The last two columns summarize already persisted **per-array summaries**. They are not pooled raw percentiles.

Largest accepted raw witnesses include:

- G2 辽宁 turn 2 iteration 25: `d_bb=1.714597479e12` at `(i_b=1,i_a=11,i_z=1)` and `d_fb=1.611417707e12` at `(0,11,1)`;
- G2 江苏 turn 2 iteration 15: `d_bf=4.190962675e9`, `d_ff=4.185028038e9`;
- G1 吉林 turn 2 iteration 24: `d_bb=-2.785464010e9`, `d_fb=-2.623956919e9`;
- G2 内蒙古 turn 3 iteration 25: `d_bf=-2.710347230e9`, `d_ff=-2.292697579e9`.

These are per-array absolute-maximum witnesses. They prove a finite explosive tail but are not a random sample and cannot establish raw sign frequencies.

## 6. Exact selected-control diagnostics

Population: final HJB iteration selected `d` from all 310 accepted province calls.

| Statistic | Signed `d` | `abs(d)` |
|---|---:|---:|
| count / finite | 248,000 / 248,000 | 248,000 / 248,000 |
| min / max | -42,699,421.2601 / 2,800,319.82925 | 0 / 42,699,421.2601 |
| p50 | -0.436096 | 1.379676 |
| p75 | 0 | 6.588244 |
| p90 | 3.492004 | 87.049875 |
| p95 | 12.083788 | 127.457658 |
| p97.5 | 86.537204 | 404.789588 |
| p99 | 376.416915 | 1,621.104369 |
| p99.5 | 1,140.281671 | 4,420.632794 |
| p99.9 | 6,558.284817 | 37,156.244332 |

Shares among finite selected controls:

- positive: `22.446774%`;
- negative: `60.054839%`;
- zero: `17.498387%`.

Separate sign tails:

| Percentile | Positive `d` | `abs(negative d)` |
|---|---:|---:|
| p50 | 2.821137 | 2.064923 |
| p75 | 9.388602 | 15.307441 |
| p90 | 94.424649 | 95.739934 |
| p95 | 318.796405 | 134.965030 |
| p97.5 | 956.693650 | 422.670333 |
| p99 | 2,920.901063 | 1,704.349632 |
| p99.5 | 5,673.403205 | 5,635.012518 |
| p99.9 | 41,347.411843 | 48,255.731967 |
| max | 2,800,319.829253 | 42,699,421.260055 |

All selected hits for `D>=1,000` occur under transfer label `B`; the accepted `F` and `0` selected populations have zero hits at those diagnostic thresholds. This is descriptive selector evidence, not a proposal to change the selector.

Adjustment-cost selected population under the frozen formula has median `0.542204`, p90 `1,061.531660`, p95 `2,625.152666`, p99 `392,001.390406`, p99.9 `212,274,871.723382`, and max `192,453,176,175,102.66`.

## 7. Ordinary region versus explosive tail

Classification: `DESCRIPTIVE_NUMERICAL_CONTINUATION_DESIGN`.

- selected `abs(d)` median=`1.379676`;
- p99=`1,621.104369`;
- p99.9=`37,156.244332`;
- max=`42,699,421.260055`;
- max/median ratio=`30,948,875.69`;
- p99.9/p99.5=`8.4052`; max/p99.9=`1,149.19`;
- raw accepted witness max=`1.714597479e12`.

The accepted evidence therefore shows a central selected region and a finite explosive tail separated by many orders of magnitude. It does **not** locate a stable raw-candidate cutoff because raw cell values between the persisted order statistics are unavailable. No threshold is chosen because it would have changed an observed convergence outcome.

## 8. Symmetry audit

Selected controls are sign-asymmetric: negative selections are more frequent, and the largest negative selected magnitude is `15.25×` the largest positive selected magnitude. At the p99.9 sign tails the scales are closer (`48,255.73` negative-absolute versus `41,347.41` positive), so asymmetry itself changes across the tail.

Raw extrema point in the opposite most-extreme direction: the largest positive raw witness is `615.55×` the absolute largest negative raw witness. Across `108,784` per-array absolute-max witnesses, `47,226` are positive and `61,558` are negative. Those witness counts are not raw cell sign frequencies.

Conclusion:

`EXTREME_SCALE_ASYMMETRY_VISIBLE__CELL_LEVEL_RAW_SIGN_FREQUENCIES_UNAVAILABLE`

A symmetric interval is only a simplification candidate requiring Owner approval. The evidence is insufficient to freeze either symmetric or asymmetric numeric limits.

## 9. Asset/grid and annual-flow scale context

- `a` grid: `[0,10]`, 20 points, span `10` asset-model units;
- `b` grid: `[-2,5]`, 20 points, span `7` asset-model units;
- `z`: `[0.8,1.3]`;
- under the frozen annual continuous-time contract, `d` is interpreted as asset-model units per year;
- selected median `abs(d)` is `0.138×` the entire `a` span, selected p99 is `162.1×` the span, and selected max is about `4.27 million×` the span.

Persisted/derived annual-flow context for the same final-iteration cells:

- consumption: min `0.054166`, median `7.800320`, p99/max `1,000/1,000`;
- labor income derived from persisted wage/tax/migration/labor receipts: min `0.966479`, median `10.866655`, p99 `25.294668`, max `93.138637`;
- exogenous transfer income: `0.1` in all 310 province-call receipts;
- selected transfer flow: median `-0.436096`, p99 `376.416915`, min/max `-42,699,421.260055/2,800,319.829253`.

With `chi0=.1`, `chi1=2 years`, and the frozen scale floor, the static cost is:

`0.1*abs(d) + d^2/max(a,1e-6)`.

At 湖北 turn 2 iteration 98, G2 `d_bb=-210,847,982.086235` at `a=9.473684` implies cost `4.692669795789844e15`; the selected `d=-210,613,663.508120` has persisted cost `4.682245520338688e15`. This is a numerical-scale observation, not an economic turnover restriction or a claim about a discrete one-year portfolio change.

## 10. A/B/C safeguard semantics

| Semantics | Raw receipt | Ranking/selector effect | Threshold continuity | FOC fidelity | Main risk | Owner decision |
|---|---|---|---|---|---|---|
| A. candidate rejection | preserved | removes inadmissible branch before competition | discrete eligibility change | high for retained candidates | a formerly winning branch disappears | required |
| B. candidate clipping | raw and clipped must both persist | ranks threshold-valued surrogate | control continuous, derivative/ranking kink | low outside interval | fabricates a candidate that does not solve the accepted FOC | required |
| C. fallback to existing zero | preserved | rejects inadmissible branch while retaining existing zero option | possible discrete switch to zero/another admissible branch | high; no clipped surrogate | must not create a new zero law or suppress other admissible branches | required |

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION` is the preferred semantic design. It is compatible with the accepted `F/B/0` structure, preserves raw FOC evidence, and avoids evaluating cost/drift on a manufactured clipped candidate. This preference does not choose a bound or authorize implementation.

## 11. Numeric sensitivity grid and why it is not a ladder

The following symmetric thresholds are an audit grid only. They are not preregistered stages.

### Exact selected-control hits

| Interval | Overall hits / 248,000 | G1 hits / 124,000 | G2 hits / 124,000 | turn-2 hits / 49,600 |
|---|---:|---:|---:|---:|
| `[-1e3,1e3]` | 3,468 (1.398387%) | 1,581 (1.275000%) | 1,887 (1.521774%) | 934 (1.883065%) |
| `[-1e4,1e4]` | 682 (0.275000%) | 350 (0.282258%) | 332 (0.267742%) | 190 (0.383065%) |
| `[-1e5,1e5]` | 110 (0.044355%) | 56 (0.045161%) | 54 (0.043548%) | 35 (0.070565%) |
| `[-1e6,1e6]` | 19 (0.007661%) | 10 (0.008065%) | 9 (0.007258%) | 6 (0.012097%) |

### Raw-candidate hit-share bounds from min/max receipts

| Interval | Represented raw count | Definite inadmissible lower bound | Possible inadmissible upper bound | Definite preserved unchanged |
|---|---:|---:|---:|---:|
| `[-1e3,1e3]` | 87,027,200 | 173,492 (0.199354%) | 73,969,600 (84.995955%) | 13,057,600 |
| `[-1e4,1e4]` | 87,027,200 | 110,890 (0.127420%) | 56,355,200 (64.755846%) | 30,672,000 |
| `[-1e5,1e5]` | 87,027,200 | 35,402 (0.040679%) | 23,338,400 (26.817363%) | 63,688,800 |
| `[-1e6,1e6]` | 87,027,200 | 7,138 (0.008202%) | 5,332,800 (6.127739%) | 81,694,400 |

The bounds are too wide to satisfy the task's exact raw hit-share requirement. Only bounded option bands can be handed to Owner/Reviewer:

1. tighter option: `D in [1e3,1e4]`;
2. intermediate option: `D in [1e4,1e5]`;
3. looser option: `D in [1e5,1e6]`;
4. `OFF` comparator.

These are ranges for additional design, not a 3–4-stage preregistered ladder. No exact candidate interval is scientifically frozen.

## 12. Priority-checkpoint adjudication

Each count below is the number of four raw branches outside a symmetric audit interval. Under A the counted branches are excluded; under B they are clipped to the relevant endpoint; under C they are excluded while the existing zero option remains. No row implies HJB convergence under any semantic.

| Checkpoint | Evidence role | Raw branch extrema used | D=1e3 | D=1e4 | D=1e5 | D=1e6 |
|---|---|---|---:|---:|---:|---:|
| 湖北 t2 G1 iter100 interior | common-state path | `[17.51,4.95,-140.53,-65.21]` | 0 | 0 | 0 | 0 |
| 湖北 t2 G2 iter98 interior | common-state extreme | `[-2.108e8,2.343e5,2.834e4,-35.77]` | 3 | 3 | 2 | 1 |
| 湖北 t2 G2 iter100 interior | common-state final | `[-4.270e7,-1.062e7,-70.44,-20.72]` | 2 | 2 | 2 | 2 |
| 山东 t2 G1 iter72 | per-branch abs-max witnesses | `[8.222e3,5.546e3,6.620e3,6.035e3]` | 4 | 0 | 0 | 0 |
| 山东 t2 G2 iter72 | per-branch abs-max witnesses | `[-2.864e7,8.846e4,-2.943e7,1.029e5]` | 4 | 4 | 3 | 2 |
| 广东 t2 G1 iter82 | per-branch abs-max witnesses | `[-68.89,-23.42,-23.45,-10.03]` | 0 | 0 | 0 | 0 |
| 广东 t2 G2 iter82 | per-branch abs-max witnesses | `[-5.820e6,-2.914e5,-6.155e6,-2.632e5]` | 4 | 4 | 4 | 2 |
| 四川 t4 G1 iter57 upper-b | later-history, converged | `[-2.61,-2.92,-0.19,-1.12]` | 0 | 0 | 0 | 0 |
| 四川 t4 G2 iter100 upper-b | later-history, nonconverged | `[-493.32,5.314e4,-16.81,1.408e3]` | 2 | 1 | 0 | 0 |
| 云南 t4 G1 iter100 interior | later-history, G1 extreme | `[-1.188e7,-7.050e3,-7.279e5,-433.97]` | 3 | 2 | 2 | 1 |
| 云南 t4 G2 iter100 interior | later-history, G2 improved | `[2.413e3,1.536e3,441.67,280.35]` | 2 | 0 | 0 | 0 |

山东 and 广东 rows pair per-branch abs-max witnesses with the accepted iteration-level selected-cost summary; the raw witnesses need not occupy the selected-cost witness cell. They are not silently presented as same-cell reconstructions. 四川/云南 turn 4 remains `PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`.

## 13. Return/wage cross-tabs

Classification: `DESCRIPTIVE_ONLY_NOT_CAUSAL`.

At selected-control threshold `D=1e4`:

| Province-call price status | Selected hits / cells | Share |
|---|---:|---:|
| return upper | 562 / 166,400 | 0.337740% |
| return unsaturated | 96 / 32,000 | 0.300000% |
| return not-applied bootstrap | 24 / 49,600 | 0.048387% |
| wage upper | 518 / 182,400 | 0.283991% |
| wage unsaturated | 75 / 26,400 | 0.284091% |
| wage lower | 89 / 39,200 | 0.227041% |

Raw candidate cross-tabs cannot be exact. At the same `D=1e4`, min/max-only lower-to-upper hit bounds are:

- return upper: `83,004–42,185,600` of `64,012,800` represented raw candidates;
- return unsaturated: `18,946–9,435,200` of `12,800,000`;
- return bootstrap/not-applied: `8,940–4,734,400` of `10,214,400`;
- wage upper: `80,126–41,023,200` of `64,489,600`;
- wage unsaturated: `12,414–6,261,600` of `9,270,400`;
- wage lower: `18,350–9,070,400` of `13,267,200`.

Extreme transfer candidates occur under both saturated and unsaturated return/wage statuses. A transfer-control safeguard cannot be used to hide the independently unresolved price-bound saturation problem.

## 14. Final decision table

| Design | Numeric interval | Raw hit share | Selected hit evidence | Branch coverage | Symmetry | FOC / selector fidelity | Complexity | Strongest caveat |
|---|---|---|---|---|---|---|---|---|
| A rejection | unresolved option bands only | unavailable; bounded only | exact audit grid available | all four raw branches | unresolved | high FOC; competitor set changes | low-medium | discontinuous eligibility and unknown raw hit rate |
| B clipping | unresolved option bands only | unavailable; bounded only | exact audit grid available | all four raw branches | unresolved | low outside interval; surrogate competitor | medium | clipped value does not satisfy accepted FOC |
| C reject + existing zero | unresolved option bands only | unavailable; bounded only | exact audit grid available | all four raw branches plus unchanged zero option | unresolved | highest conditional fidelity | low-medium | discrete fallback and unknown raw hit rate |

Preferred semantic design: `C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`.

Unique numeric design: `NOT_SUPPORTED`.

## 15. Exactly one next gate

`ADDITIONAL_ZERO_SCIENCE_DESIGN_TO_OBTAIN_CELL_LEVEL_RAW_CANDIDATE_DISTRIBUTIONS_BEFORE_OWNER_NUMERIC_FREEZE`

Reviewer/Owner should decide how a subsequent zero-science evidence gate will obtain or persist the full accepted raw branch populations needed for exact hit shares, sign-tail quantiles, branch/price/boundary cross-tabs and a defensible numeric ladder. This report does not authorize a model rerun, safeguard implementation, or runtime.

## 16. KFE and Results boundary

KFE remains `DIAGNOSTIC_ONLY`. Finite-box upper-`b` leakage and MATLAB-style pinning remain independently unresolved. Static transfer-candidate analysis does not establish KFE admissibility, steady-state acceptance, or Results authority.

Results eligibility=`FALSE`.
