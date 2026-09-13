# CH5 MP4C K1 — wage-conditional `(ra,w)` health-region and provincial return-mapping audit report

Date: 2026-09-13.

Terminal classification:

`WAGE_IDENTITY_ALIGNED__ALL_ACCEPTED_PROVINCIAL_POINTS_OUTSIDE_STANDALONE_WAGE_COVERAGE__TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`

## Scope and authority

This is a zero-science integration of accepted evidence plus a read-only MATLAB/Python source-semantic audit. The fresh-fetched baseline is `44df9bb331770a930d8ff465c23d59d6fe5cb65a`. No HJB, KFE, outer turn, MATLAB, firm, K1B/K2, GE, downstream, shock, IRF, or Results runtime was executed.

The observed map combines exactly the 27 accepted Cartesian points from the coarse, first-refinement, and narrow scans. Provincial rows come only from the accepted 62-call turn1/turn2 mechanism evidence. No unaccepted trace supplied or replaced a provincial HJB input.

## Wage semantic/scaling gate

Gate result:

`WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`

The gate subject is the standalone household wage versus the actual multi-province household-HJB consumed wage. They have the same source role and the same accepted Python API slot:

- standalone scans vary `HouseholdInputs.wages[0]`;
- MATLAB HJB reads `w = results.w` at `HANK_2ASSETS_HJB.m:26-31`;
- the accepted Python crosswalk maps `results.w` to `HouseholdInputs.wages[0]` at `household_adapter.py:43-65`, and `build_static_household_call` passes `inputs.composite_wage` as the singleton `wages` tuple at lines 200-219.

No additional unit conversion or normalization between `results.w` and `HouseholdInputs.wages[0]` is defined in the designated sources. Units are not explicit in those sources. “Directly comparable” therefore means object/API identity; it does **not** mean that the accepted numerical domains overlap.

### End-to-end wage chain

MATLAB:

1. `HANK_firm.m:66-73` guards raw firm wage `wt0` into provincial firm wage `wjt`; line 81 explicitly distinguishes provincial `wjt` from household `results.w`.
2. `wage_caculate.m:1-17` aggregates the length-`N_prov` destination vector `results{j}.wjt` into one composite wage for each origin `i`:

   `results.w(i) = alphal^(-phi_l/(1+phi_l)) * [sum_j phi_l_mat(j,i) * (results{j}.wjt * (1-results{j}.tau-sigmau_MAT(j,i)) / phi_l_mat(j,i))^(1+1/phi_l)]^(phi_l/(1+phi_l))`.

3. `HANK_mp_1turn.m:49-52` assigns this `wt_vec(i)` to `results{i}.w` for the next household turn; the HJB then consumes that scalar.

Python:

1. `multi_province/wage.py:11-76` implements the same destination-row/origin-column aggregation from guarded `firm_wages[destination]`, destination taxes, `phi[destination,origin]`, and `sigma[destination,origin]`.
2. `multi_province/steady_state.py:147-168` stores `turn.household_composite_wage[i]` as state `w`.
3. `multi_province/household_adapter.py:200-219` passes that scalar as `HouseholdInputs.wages[0]`.

Thus `guarded_wjt` is an upstream firm object, not the standalone wage coordinate. It requires the existing deterministic source mapping to become `results.w`; substituting `guarded_wjt` directly would be a semantic error. The exact formula and source hashes are preserved in `wage_mapping_receipt.json` and `source_identity.json`.

## Accepted observed standalone `(ra,w)` map

All 27 HJB calls in the three already accepted scans were legal and converged. The integrated canonical health-map counts are:

- `INTERIOR_A_DISTRIBUTION_CANDIDATE`: 4;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`: 7;
- `LOWER_A_BOUNDARY_DOMINATED`: 7;
- `UPPER_A_BOUNDARY_PILEUP`: 8;
- `KFE_NUMERICALLY_PATHOLOGICAL`: 1.

The four interior candidates are the accepted coordinates `(.065,1.05)`, `(.065,1.3)`, `(.06,1.3)`, and `(.0675,1.3)`. There is no scalar `ra` that is interior at all three tested wages.

The coarse legacy labels were converted only from their preserved endpoint geometry: modal `a=0` became lower-bound dominated and modal `a=10` became upper-bound pileup. No interpolation or fitted boundary was used.

At `(.06,.8)`, the modal label remains `LOWER_A_BOUNDARY_DOMINATED`, but its health-map label is overridden by `KFE_NUMERICALLY_PATHOLOGICAL`: `amin mass=1.0377993910487715`, `amax mass=-.007111658675254044`, `interior-a mass=-.030687732373517258`, `At=-.3383306787869177`, density minimum `-.01258986461524459`, and 340 negative density entries. Nothing was clipped, and this point is not a healthy/admissible steady state.

## Provincial projection

The wage gate passes, so the accepted 31 provinces × two turns were projected using their exact consumed `ra` and exact consumed composite wage. Exact coordinate matching uses decimal values; nearest points are descriptive only.

| Turn | HJB converged | HJB failed | Exact observed matches | Unobserved |
|---|---:|---:|---:|---:|
| 1 | 20 | 11 | 0 | 31 |
| 2 | 2 | 29 | 0 | 31 |

Every row is `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`. The accepted provincial composite wage ranges are `13.837477514705718–18.519697907284154` in turn1 and `12.842642802904619–17.480975827270356` in turn2, whereas the standalone map observes only `.8`, `1.05`, and `1.3`. Therefore no provincial state receives an interior, unhealthy, ambiguous, or pathological standalone label.

For transparency, the projection records closest tested wage slice, separate absolute `ra` and wage distances, nearest observed point, and return ordering at that slice. All such fields are `DESCRIPTIVE_ONLY__NOT_ADMISSIBILITY_CLASSIFICATION`.

Accepted compact evidence does not expose the raw `wt0` that originally produced each entering-state `wjt`; these cells are explicitly marked `UNAVAILABLE_IN_ACCEPTED_COMPACT_PROVINCIAL_INPUT_EVIDENCE`. It does expose authoritative guarded `wjt`, corrected wage-guard state, and the exact consumed composite wage. No raw wage was guessed or reconstructed.

## Turn1/turn2 associations and guards

For the 20 provinces that converged in turn1 and failed in turn2:

- consumed `ra` rises in 20/20, with mean change `+0.2337584032013225125`;
- consumed composite wage falls in 20/20, with mean change `-1.00767182264504985`.

This is descriptive co-movement only. Both endpoints remain outside the standalone wage coverage, so the evidence cannot establish that these provinces crossed an observed unhealthy frontier or that return mapping caused the turn2 failures.

Return guard:

- turn1 is bootstrap input: raw and consumed `ra` are equal for 31/31;
- turn2 has 18 upper-guarded calls, all consumed at `.35`; their raw `ra` ranges from `.354147848317954` to `.820104799024125`, with mean consumed-minus-raw change about `-.1685172032`;
- of the 29 turn2 failures, 16 are upper-guarded and 13 are unsaturated; both turn2 converged calls are also upper-guarded.

Wage guard:

- turn1 entering-state `wjt` is upper-bound classified in 31/31, while 20 converge and 11 fail;
- turn2 has 4 lower, 3 unsaturated, and 24 upper classifications; all 4 lower and all 3 unsaturated calls fail, while the upper group contains 22 failures and both converged calls;
- guard state therefore does not uniquely separate convergence from failure. The guard applies to `wjt`, not to the much larger consumed composite wage.

Within turn2, failed calls have mean consumed `ra≈.32094` and mean composite wage `≈16.33657`; the two converged calls both consume `ra=.35` and have mean composite wage `≈16.66929`. With only two converged calls, overlapping guard states, and no standalone wage coverage at this scale, the accepted evidence does not support concentration at a proven high-`ra`, low-wage, high-wage, or guard-saturation health boundary.

## Answers to the task questions

1. Standalone `w` and provincial HJB consumed `w` are the same source role/API object. Their accepted numerical coverage is disjoint.
2. Guarded firm `wjt` maps to household `results.w` only through the existing deterministic wage aggregation shown above; no outcome-fitted rescaling is allowed or used.
3. The supported standalone map contains 27 observed points and the five canonical labels/counts above. It supports a two-dimensional, wage-dependent observed map, not a continuous admissibility region.
4. Turn1: 31/31 unobserved; turn2: 31/31 unobserved, because the exact wage coordinate never matches.
5. The 20/20 transition set moves to higher `ra` and lower composite wage, but no observed-frontier crossing can be classified.
6. Return and wage guards do not uniquely separate outcomes. The primary unresolved issue is insufficient standalone health-map coverage at the provincial composite-wage scale, not a source-proven wage normalization inconsistency.

## Runtime ledger and boundaries

`HJB=0; KFE=0; outer=0; MATLAB=0; firm=0; K1B=0; K2=0; GE=0; annual downstream=0; shock=0; IRF=0; Results=0; scientific retries=0`.

No model source, calibration, guard, derivative floor, grid, tolerance, or scientific evidence was modified. Results eligibility=`FALSE`.

## Exactly one next Owner gate

`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`

This is a recommendation only. No successor task is published or executed. Stop for independent ChatGPT Reviewer acceptance; do not merge main.
