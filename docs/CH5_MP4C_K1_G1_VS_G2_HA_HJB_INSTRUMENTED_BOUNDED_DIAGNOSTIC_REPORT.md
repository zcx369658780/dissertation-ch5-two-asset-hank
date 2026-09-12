# CH5 MP4C K1 — G1 vs G2 HA/HJB instrumented bounded diagnostic report

Date: 2026-09-12
Task: `CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC`

## 1. Classification

`TURN2_COMMON_STATE_DIVERGENCE_BEGINS_IN_EFFECTIVE_RETURN_DRIFT_ASSEMBLY_AND_PROPAGATES_THROUGH_VALUE_DERIVATIVES_INTO_TRANSFER_CANDIDATE_EXPLOSION__OWNER_HA_NUMERICAL_CONTRACT_DECISION_REQUIRED`

This is a bounded Builder diagnostic, not scientific acceptance. Results eligibility is `FALSE`.

## 2. Authority and isolated execution

- Fresh `origin/main`: `053d04a40a8a72b2babde31bb5ab23368ca9edc4`.
- Exact task blob SHA-256: `FBE1713BE9CC6F960B9EF45305C0CAE05B9ED325F9D3383141C29BD9B1C7FBAE`.
- Branch: `codex/ch5-k1-g1-vs-g2-ha-hjb-instrumented-20260912`.
- Worktree: `D:\ProjectTemp\ch5-k1-g1-vs-g2-ha-hjb-instrumented-20260912-001`.
- Accepted input payload: `D:\ProjectTemp\ch5-k1-annual-hjb-g1-vs-g2-evidence-20260912-001\annual_g1_guarded\runtime_input_payload.json`.
- Payload SHA-256: `EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355`.
- External evidence root: `D:\ProjectTemp\ch5-k1-g1-vs-g2-ha-hjb-instrumented-evidence-20260912-001`.

The worktree began clean. No accepted production scientific source under `src/` and no accepted export was modified. The task-local HJB implementation is an observation-only clone around accepted export functions.

## 3. Frozen science and pre-run gates

The run retained annual continuous time, `rho=.05`, `rb=.02`, borrowing gap `.07`, firm/HJB `delta=.10`, `Q_z` off-diagonal `1/3`, `chi0=.1`, `chi1=2`, fixed theta, `beta_distance=2`, `beta_return=0`, accepted destination-by-origin `S`, the same `S` for capital quantity and payoff, source-faithful labor, smoothing OFF, partial adjustment OFF, and unchanged C1. K1B and K2 remained OFF.

The only treatment was the frozen HJB-interface guard:

- G1: `r_a in [-.05,.20]`;
- G2: `r_a in [-.10,.35]`;
- both paths: firm wage safeguard `wjt in [.8,1.3]`.

The instrumented pre-run gate is `PASS`. Instrumentation ON/OFF produced exact equality for value, initial value, consumption, labor, transfer, adjustment cost, effective return, both drifts, utility, policy labels, operator, post-convergence operator, iteration count, convergence flag, and convergence statistic on the focused fixture. Science calls before this gate were zero. The initial payloads, turn-1 bootstrap, same-S/K1/C1/source-faithful-labor contracts, and solver/grid/tolerance/boundary laws also passed unchanged.

Focused verification after implementation: `31 passed` across the task suite, accepted G1/G2 suite, and standalone accepted-export suite. The earlier focused run before the static finalizer was `30 passed`; the additional test covers static earliest-difference localization.

## 4. Exact runtime ledger

Exactly two trajectories were invoked; both completed 5/5 outer turns. No engineering or scientific retry occurred.

| Ledger | G1 | G2 | Total |
|---|---:|---:|---:|
| HJB calls | 155 | 155 | 310 |
| HJB direct solves | 13,362 | 13,834 | 27,196 |
| KFE calls/direct solves | 155/155 | 155/155 | 310/310 |
| labor roots / Brent attempts | 124,000 | 124,000 | 248,000 |
| province updates | 155 | 155 | 310 |
| persisted HJB traces | 155 | 155 | 310 |
| trace bytes | 793,549,712 | 893,001,932 | 1,686,551,644 |

MATLAB, standalone KFE experiment, K1B, K2, GE, annual downstream, shock, IRF, and Results calls were all zero. The trajectory budget is fully consumed; no further scientific execution is authorized.

## 5. Turn 1 equality

Turn 1 remained the common bootstrap. G1 and G2 were exactly equal in every compared HJB array and all recorded aggregate/firm/household inputs and outputs; every reported maximum absolute difference was zero. Both paths had 20/31 converged HJB calls in turn 1. This equality is not a steady-state or Results claim.

## 6. Turn 2 common-entering-state finding

All 31 provinces passed the common-state checks before treatment:

- identical initial HJB value hash;
- identical grid hashes, parameters, numerics, and wage input;
- identical raw converted annual `rah`, household `rah`, and composite wage;
- different consumed `r_a` in every province only because of the two frozen return guards.

Every province shows the same causal ordering:

1. At HJB iteration 1, all four raw derivative hashes, derivative-floor counts/coordinates, all pre-selector transfer candidate hashes, and both liquid/transfer label hashes are identical. The only differing selected-object hashes are `effective_illiquid_return` and `mu_a`.
2. The changed return contribution therefore changes the `a`-direction drift assembly. Operator, `V_new`, and the convergence statistic differ in iteration 1 for 31/31 provinces.
3. At iteration 2, all four raw derivative objects and all persisted pre-selector candidate objects differ in 31/31 provinces. Transfer labels first differ at iteration 2 in 31/31 provinces. Liquid labels first differ at iteration 2 in 新疆 and iteration 3 in the other 30 provinces.
4. Derivative-floor activation first differs at iteration 3 in the 18 G2 upper-guard provinces and iteration 4 in the 13 G2-unsaturated provinces.

Thus the first difference is not created by derivatives, a floor, candidate construction, selector score/label, wage input, or boundary law. It begins in the expected direct response to the different frozen return input:

`effective-return contribution -> mu_a / a-direction drift -> operator -> V_new`.

The later derivative/candidate/selector behavior is feedback from that changed value path. The initiating mechanism is witnessed at the preregistered interior 湖北 cell before any floor or label difference, so it is not boundary-law initiated. The compact trace does not support a cell-count claim that all later effects are predominantly interior; it does establish that an interior path is sufficient and that a boundary or floor is unnecessary for initiation.

## 7. 湖北 turn 2 interior cell reconstruction

Cell `(i_b=1,i_a=18,i_z=0)` is interior in both asset dimensions.

At iteration 1, both paths have identical raw derivatives:

- `va_backward=4.8541208288321874e-05`;
- `va_forward=6.849193380884522e-05`;
- `vb_backward=.021572771099998885`;
- `vb_forward=.021461471811206244`;
- neither liquid derivative floor activates.

Both paths also have identical candidates and selectors:

- `d_bb=-4.252499456922124`, `d_bf=-4.248118775541967`;
- `d_fb=-4.25244418221595`, `d_ff=-4.248040782602565`;
- selected transfer `d=-4.25244418221595`, cost `2.334035245634836`;
- liquid label `F`, transfer label `F`, `mu_b=5.382326038960529`.

The return channel differs immediately:

- G1: effective return `.18770580398736797`, contribution `1.7782655114592754`, `mu_a=-2.4741786707566753`, statistic `.45309418784574973`;
- G2: effective return `.32848515697789393`, contribution `3.1119646450537317`, `mu_a=-1.1404795371622187`, statistic `.485686139706595`.

At iteration 4, both selected transfers are zero, but labels already differ: G1 `B0`, G2 `00`; `mu_a` remains different because of the return contribution.

At iteration 98, G2 has selected `d=-210,613,663.5081197`, cost `4,682,245,520,338,688`, `mu_a=-210,613,660.39615506`, `mu_b=-4,682,245,309,726,023`, labels `BB`. The raw pre-selector `d_bb=-210,847,982.086235` is already extreme.

At iteration 100:

- G1: `d=4.952212131799057`, cost `3.083908407448892`, `mu_a=6.730477643258332`, `mu_b=-8.03612053924795`, labels `0B`;
- G2: `d=-42,699,421.26005487`, cost `192,453,176,175,102.66`, `mu_a=-42,699,418.14809023`, `mu_b=-192,453,133,476,680.03`, labels `BB`;
- the G2 selected candidate is its already-extreme raw `d_bb=-42,699,421.26005487`.

Therefore selection does not transform a benign finite candidate into the extreme. Candidate construction has already exploded through the evolved value/derivative/FOC feedback, after which the B selector admits that candidate.

## 8. Other priority and worst observed checkpoints

- 山东 turn 2 is retained as the previously unsaturated high-statistic case. Its final HJB statistic is `.05841642710343087` in G1 and `50.93586949139517` in G2. The per-province earliest sequence is the universal turn-2 sequence above. At iteration 72 its selected adjustment-cost abs-max is `3,437,689.8551448723` in G1 versus `91,098,681,098,903.66` in G2, a finite ratio of about `26,499,970.89`; each path's dynamic witness coordinate is preserved where the candidate table was available.
- The largest observed cross-path factor among per-iteration selected `|d|`, adjustment-cost, `|mu_a|`, and `|mu_b|` abs-max summaries occurs for 广东 turn 2, iteration 82, adjustment cost: G2/G1 ratio `598,278,007,699.0404`. This is a descriptive maximum over persisted summaries, not a pass threshold; the two path abs-max witnesses may be different cells.
- 四川 turn 4 is later-history evidence only. At the upper-`b` checkpoint `(19,16,1)`, G1 converges in 57 iterations with final statistic `5.6053643393561003e-08`; G2 reaches iteration 100 with statistic `203.2133848859883` and selected `d=52,642.36058490023`, cost `329,087,416.930199`, labels `BB`.
- 云南 turn 4 is also later-history evidence only. At interior checkpoint `(10,9,0)`, G1 iteration 100 has selected `d=-11,880,590.263368346` and cost `29,798,002,022,668.055`; G2 has `d=1,535.8153347795585` and cost `498,107.4271816658`. G2 therefore sharply reduces this particular G1 extreme even though neither path converges at that call and no global stability claim follows.

Where a dynamic selected-object abs-max witness cell was not among the persisted candidate tables, compact evidence states `UNAVAILABLE__DYNAMIC_SELECTED_OBJECT_WITNESS_CELL_NOT_IN_PERSISTED_CANDIDATE_TABLES`; no hidden reconstruction or re-solve was performed.

## 9. Turns 3-5 propagation boundary

All turns 3-5 comparisons are classified exactly as:

`PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`

The paths enter those turns from different endogenous histories. No same-state replay was run. HJB convergence counts for turns 3/4/5 are G1 `3/7/6` and G2 `1/3/0`; corresponding maximum final statistics are G1 `41.719558173353654 / 12.450374112878029 / 70.4255064062228` and G2 `170.45507307121323 / 203.2133848859883 / 31.831377523922477`. These are descriptive propagation outcomes, not direct later-turn causal estimates of the guard.

## 10. Price monitoring

Turn 1 used the common bootstrap and did not apply the treatment guard. Across treatment turns 2-5 (124 province-turns per path):

- G1 return: 124 upper hits, 0 unsaturated, 0 lower;
- G2 return: 84 upper hits, 40 unsaturated, 0 lower;
- G1 wage: 96 upper, 12 unsaturated, 16 lower;
- G2 wage: 84 upper, 15 unsaturated, 25 lower.

At turn 2 specifically, the HJB wage input is identical in all 31 pairs, with the same wage statuses: 24 upper, 3 unsaturated, 4 lower in each path. The earliest turn-2 difference therefore does not coincide with a wage-input difference. `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` is false for both paths.

## 11. Accounting, provenance, finiteness, and KFE caveat

All 310 province updates retain same-S quantity/payoff provenance, source-faithful labor, zero same-turn feedback, capital conservation, and unchanged C1 accounting. Total `K/target` stays between `0.9999999999999998` and `1.0000000000000002`; maximum recorded capital-column residual is `3.725290298461914e-09 MU`, and maximum C1 residual is `2.9802322387695312e-08 MU`.

All 310 HJB traces have zero NaN/Inf. No scientific exception or hard-stop condition was triggered. Finite continuation is not HJB convergence: many calls terminate nonconverged at the iteration ceiling, as recorded above.

All 310 KFE calls remain `DIAGNOSTIC_ONLY`. Finite direct solve and downstream completion do not establish KFE admissibility, density acceptance, steady state, or Results authority. A standalone KKT residual is `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`; no object is relabelled as a KKT residual.

The sealed external manifest contains 1,357 files excluding itself. Its SHA-256 is `741DBF595C0DF6698F40A8FA2625102759190291B27937B88F02D6FFE9EC973A`; the accepted full readback receipt is `PASS`, and static finalization rechecked that the current manifest file hash still matches that receipt.

## 12. Exactly one next gate

`OWNER_HA_NUMERICAL_CONTRACT_DECISION`

The Owner should adjudicate the smallest plausible next scientific contract: whether the accepted HA transfer/adjustment-cost candidate admissibility law, including its use of the existing liquid-derivative safeguard in the transfer FOC, is adequate under the already frozen price-interface return range. This evidence does not authorize changing `chi0/chi1`, the derivative floor, return guard, boundary law, grid, tolerance, or solver. It does not authorize another runtime.

No G3/G4, wage relaxation, longer G2, K1B/K2, GE, steady-state acceptance, downstream model, IRF, or Results gate is opened. The next action is fresh independent Reviewer ACCEPT/REJECT of this candidate; the Builder does not self-accept or merge `main`.
