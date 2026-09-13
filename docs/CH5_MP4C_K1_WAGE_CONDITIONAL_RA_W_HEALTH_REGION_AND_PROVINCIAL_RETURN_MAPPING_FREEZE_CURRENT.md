# CH5 MP4C K1 — wage-conditional `(ra,w)` household-health region and provincial return-mapping freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_TWO_DIMENSIONAL_HEALTH_REGION_AND_PROVINCIAL_MAPPING_REVIEW`.

## 1. Owner decision

The accepted standalone scans establish that no universal scalar `ra` health band exists across the tested household wage range. Do not continue automatic one-dimensional `ra` refinement.

The next task must:

1. consolidate the accepted standalone MATLAB-faithful evidence into a provisional two-dimensional `(ra,w)` household-health map without inventing interpolation-based certainty;
2. audit the semantic and scaling identity between the standalone scanned wage variable and the actual wage quantity entering the current multi-province household HJB;
3. only if that identity/mapping is proven, project accepted provincial return/wage states onto the provisional health map and identify which provinces/turns lie in or near unhealthy regions;
4. if the wage variables are not directly comparable, stop the projection and report the exact mapping/normalization blocker rather than forcing a comparison.

No HJB/KFE algorithm redesign is authorized.

## 2. Accepted standalone evidence

Use only accepted standalone scans and their sealed evidence as household-domain authority. Relevant accepted points include the accumulated grids over `rb=.02`, household wage proxy `w∈{.8,1.05,1.3}`, and `ra` values spanning `.02,.055,.06,.065,.0675,.07,.0725,.08,.09` where available.

The accepted narrow-frontier result is:

- `.06`: lower at `w=.8/1.05`, interior at `w=1.3`;
- `.0675`: ambiguous at `w=.8/1.05`, interior at `w=1.3`;
- `.07`: upper at `w=.8`, ambiguous at `w=1.05/1.3`;
- no tested `ra` is interior at all three wages.

The point `(.06,.8)` has severe signed contaminated-row KFE pathology and is not admissible despite its descriptive lower-bound label.

## 3. Provisional health-map semantics

The map is evidence-supported only at observed grid points. Allowed point labels:

- `INTERIOR_A_DISTRIBUTION_CANDIDATE`;
- `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED`;
- `LOWER_A_BOUNDARY_DOMINATED`;
- `UPPER_A_BOUNDARY_PILEUP`;
- `KFE_NUMERICALLY_PATHOLOGICAL` where raw KFE receipts are materially signed/nonphysical.

Do not infer an unobserved point as healthy solely by interpolation. You may display adjacency/frontier relations, but any unobserved region must be labelled `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED` unless directly supported by accepted evidence.

## 4. Wage-semantic gate

Before projecting any province, prove what scalar/object the standalone scan's `w` represents relative to the current multi-province household HJB.

At minimum trace:

- original MATLAB `wjt`;
- any `wage_caculate` / provincial aggregation or migration-weighting step;
- the exact scalar/vector passed into the accepted Python household HJB;
- any wage safeguard/guard variable;
- units/scaling/normalization.

A direct projection using `wjt` is forbidden if the HJB actually consumes a differently scaled composite household wage. A direct projection using a composite wage is forbidden if the standalone scan used a different object.

Classification for this gate:

- `WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`;
- `WAGE_VARIABLE_MAPPING_PROVEN_REQUIRES_TRANSFORMATION`;
- `WAGE_VARIABLE_NOT_COMPARABLE_OR_SCALING_BLOCKER`.

If a transformation is proven from accepted source logic, apply it transparently and persist the exact mapping receipt. Do not fit a transformation from outcomes.

## 5. Provincial-state source

Do not run a new full multi-province model in this task. Reuse accepted existing evidence for provincial HJB input states, prioritizing the latest accepted/controlled baseline evidence that contains per-province `ra/rah` and wage inputs for turn 1 and turn 2.

No synthetic replacement, interpolation, parameter tuning or guessed wage values.

If accepted evidence does not contain sufficient exact provincial inputs for a truthful projection, stop at a documented evidence blocker and recommend the smallest later extraction/replay task.

## 6. Projection outputs if wage gate passes

For each available province and turn, report:

- province;
- turn;
- exact `ra/rah` entering household HJB;
- exact comparable household wage after any proven source transformation;
- source raw wage object(s), including `wjt` where available;
- whether `ra` or wage was guard-limited;
- nearest observed accepted standalone grid points by coordinates, for descriptive context only;
- direct observed-point label if exact match exists;
- otherwise `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED` plus signed distance to nearby accepted frontier points;
- whether the state lies below/above the observed return frontier at the closest tested wage slices, without claiming a formal continuous boundary unless source evidence supports it.

Summarize by turn and province count: exact observed healthy/interior matches, exact unhealthy matches, ambiguous/unobserved states, wage-semantic blockers, and guard-hit states.

## 7. Scientific questions

The task must answer:

1. Is the standalone `w` directly comparable to the multi-province HJB wage input? If not, what exact mapping/scaling separates them?
2. What provisional two-dimensional health map is directly supported by accepted standalone evidence?
3. Where do accepted provincial turn-1 and turn-2 `(ra,w)` states fall relative to observed healthy/ambiguous/boundary/pathological points?
4. Do the turn-2 failures cluster on one side of the observed `(ra,w)` frontier more than turn-1 converged states?
5. Are current return/wage guards masking the raw state and, if so, which raw versus consumed values matter for household HJB health?
6. What exactly one next Owner gate is justified: return-mapping redesign, wage-mapping correction, bounded provincial-input replay, or unresolved review?

## 8. Forbidden changes/runtime

No new standalone grid points. No HJB calls. No KFE calls. No full multi-province outer turns. No MATLAB runtime. No firm runtime. No K1B/K2/GE/downstream/shock/IRF/Results. No changes to HJB/KFE, prices, guards, solver, tolerance, grid, FOC, selector, boundaries or economic parameters.

This is an evidence-integration and mapping-audit task only.

Results eligibility=`FALSE`.
