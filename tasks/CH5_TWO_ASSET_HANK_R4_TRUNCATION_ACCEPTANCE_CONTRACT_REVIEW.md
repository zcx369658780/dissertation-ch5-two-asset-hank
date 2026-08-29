# CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW

## Task

Perform a planning-only scientific acceptance-contract review for the R4 25-vs-29 common-core truncation comparison after the diagnosed machine-scale candidate-identity instability.

This task decides what the truncation compatibility contract should mean scientifically. It does not implement, patch, rerun, or accept the steady state.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Authority state

The following evidence is accepted for review:

- consumed-run provenance baseline commit:
  `546b88be6316526682c5a02ef4671021d0f387c3`
- common-core candidate-identity diagnostic report commit:
  `524690c6ab82b0f42758c48c157406d53863d98e`
- primary diagnosis:
  `TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`

The diagnostic found 4 candidate-ID mismatches among 153 common-core states. In all 4 cases:

- both candidate identities exist and are admissible in both solves;
- values/derivatives differ only around machine scale;
- consumption, labor, transfer, adjustment cost, `mu_a`, `mu_b`, feasibility, and KKT quality are equivalent within the frozen numerical contracts;
- `|mu_b| <= 4.996e-15`, far below the frozen `1e-12` zero-drift threshold;
- Hamiltonian gaps are only `2.22e-16` to `1.55e-15`;
- the observed difference is between lower-liquid-boundary `F/Z` representations;
- exact raw `candidate_id` equality was diagnosed as overly strict for these observed states.

## Required live read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_REPORT.md`
- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/policies.py`
- relevant boundary/KKT contracts needed to interpret `F/Z`, zero drift, and multipliers.

Do not run Python, pytest, HJB, KFE, fixture, MATLAB, or any numerical model.

## Review question

Determine the scientifically correct replacement for the existing hard check:

`candidate_id_25 == candidate_id_29` at every common-core state.

The replacement must preserve detection of materially different policy selection while not failing solely because two machine-equivalent lower-boundary representations exchange rank under floating-point perturbation.

## Required alternatives to assess

Assess at least the following approaches:

### A. Keep exact raw identifier equality

Evaluate whether exact `candidate_id` equality remains scientifically defensible after the diagnostic.

### B. Canonical candidate-equivalence classes

Evaluate treating lower-boundary `F/Z` aliases as equivalent only when their physical policy is equivalent under frozen tolerances.

The review must define whether equivalence may depend on:

- candidate direction label;
- zero-drift classification;
- active/slack lower-boundary representation;
- multiplier representation;
- transfer suffix / zero-transfer identity.

Do not automatically declare all `F` and `Z` candidates equivalent.

### C. Physical-policy compatibility contract

Evaluate replacing raw-ID equality with a contract that compares common-core:

- consumption;
- labor;
- transfer;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- boundary feasibility;
- KKT residual quality;
- multiplier/complementarity disposition;
- selected Hamiltonian or Hamiltonian-equivalence margin.

### D. Near-tie canonicalization before selection

Evaluate whether a future implementation should canonicalize Hamiltonian near-ties before the deterministic identifier tie-break, rather than only changing the steady-state truncation acceptance check.

This is planning only. Do not implement canonicalization.

## Hard scientific constraints

Any proposed contract MUST:

1. continue to fail when 25/29 select materially different controls or drifts;
2. continue to fail on different boundary feasibility or KKT validity;
3. not hide a candidate-construction availability switch;
4. not convert a nonzero economically meaningful liquid drift into zero merely for convenience;
5. preserve the frozen `1e-12` drift/zero tolerance unless a separate future scientific task explicitly changes it;
6. preserve existing HJB residual, KKT, generator, and `1e-3` scalar truncation-change guards;
7. distinguish physical policy equivalence from multiplier-representation equivalence;
8. define deterministic behavior for machine-scale Hamiltonian near-ties;
9. remain testable state-by-state and auditable in a report;
10. not use a broad tolerance that could mask material truncation sensitivity.

## Required multiplier decision

The diagnostic showed that the `F` and `Z` representations may have different `lambda_b` while sharing machine-equivalent controls/drifts and excellent KKT residuals.

The report must explicitly decide among:

- multiplier must also match numerically;
- multiplier may differ if both representations satisfy the same lower-boundary complementarity/KKT contract and the physical policy is equivalent;
- another precisely defined rule.

Explain the economic reason.

## Required Hamiltonian near-tie decision

The report must propose a precise deterministic near-tie rule for future implementation review.

It must state:

- whether near-tie comparison should use an existing tolerance or a derived machine-precision-scaled rule;
- why the proposed rule cannot mask economically material policy differences;
- which candidate wins within a near-tie equivalence class;
- whether canonical selection should prefer `Z` when `|mu_b| <= frozen zero tolerance`, prefer `F`, or use another economic criterion.

Do not implement the rule in this task.

## Required output

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`

The report must contain:

- evidence read;
- diagnosis accepted/rejected;
- comparison of alternatives A-D;
- proposed scientific truncation contract;
- precise state-level equivalence conditions;
- multiplier decision;
- Hamiltonian near-tie decision;
- what must still fail;
- what may be treated as equivalent;
- exact implementation surface that a later patch would be allowed to change;
- regression tests required for a later implementation gate;
- whether the existing consumed failure should be interpreted as a scientific model failure, a numerical contract failure, or remain unresolved;
- recommended next gate.

## Classification

Return exactly one primary classification:

- `KEEP_EXACT_CANDIDATE_ID_EQUALITY`
- `REPLACE_WITH_CANONICAL_PHYSICAL_POLICY_EQUIVALENCE`
- `REQUIRE_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_PHYSICAL_EQUIVALENCE`
- `CONTRACT_DECISION_BLOCKED_NEEDS_MORE_DIAGNOSTIC_EVIDENCE`

## GitHub mutation authorization

Only the new review report may be created.

If and only if it is the sole repository change:

- explicitly stage only that report;
- commit once;
- fresh-fetch before push;
- fast-forward push to live `main` only if remote main has not moved.

Suggested commit subject:

`Review R4 truncation acceptance contract`

No source/test/task/rule modification is authorized.

## Forbidden operations

Do not:

- modify source, tests, fixture, parameters, tolerances, equations, policy contracts, rules, or existing reports;
- run Python, pytest, HJB, KFE, steady state, fixture, MATLAB, or any diagnostic solver;
- rerun the consumed fixture;
- implement selector canonicalization;
- implement alias mapping;
- change the `1e-12` zero-drift threshold;
- proceed to connectivity/KFE/aggregates;
- create artificial transitions, recurrent-class selection, invariant mixtures, transition solver, AR(1), IRF, or Results;
- claim MATLAB-Python parity.

## Acceptance meaning

PASS means only that the scientific/numerical acceptance contract has been reviewed and a precise next implementation contract is available.

It does not make R4 steady state accepted and does not authorize a rerun.

## Final response requirements

Report:

- verdict;
- primary classification;
- files read/written;
- accepted diagnosis;
- chosen truncation-contract design;
- multiplier decision;
- Hamiltonian near-tie decision;
- future implementation surface;
- future regression-test requirements;
- forbidden-operation check;
- git status;
- report commit/push identity if published;
- acceptance level;
- recommended next gate.
