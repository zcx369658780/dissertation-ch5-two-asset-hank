# Task — V2 cell100 interior-a zero-drift switching law zero-science scientific adjudication

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919`

## Governance

Owner has authorized this **zero-science scientific-design adjudication** after accepting the repaired V2 cell100 result.

Owner remains final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read, in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`
6. its execution report and exact repaired cell100 receipt
7. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`
9. the accepted D1/D2/D3 corrected diagnostic contracts, failed-cell algebraic attribution, and exact selector/KKT source needed for derivation.

This task does **not** adopt a new scientific law. It determines whether an interior-`a` zero-drift switching branch is mathematically required or justified strongly enough to return to Owner for adoption.

## Frozen starting facts

Accepted V2 SHA-256:

`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`

Failing state:

- flat F index `100`
- zero-based `(i_b,i_a,i_z)=(0,5,0)`
- physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`
- `a` is an interior grid node
- `b` is the lower liquid boundary.

Persisted derivatives:

- `p_b^B=p_b^F=0.012333311206716577`
- `p_a^B=0.00903315440190679`
- `p_a^F=0.008957007194295222`.

Persisted negative-transfer active-lower-b roots after the accepted selector repair:

### backward-a branch
- `q_b=0.012457851515416401`
- `d=-0.23013514168909557`
- canonical `g_b=0`
- `g_a=+0.00670682022114244`
- rejected as `A_DERIVATIVE_DIRECTION_INCONSISTENT`.

### forward-a branch
- `q_b=0.012447419227151839`
- `d=-0.2373848778103275`
- canonical `g_b=0`
- `g_a=-0.0005429159000894801`
- rejected as `A_DERIVATIVE_DIRECTION_INCONSISTENT`.

The complete eight-case frozen census contains no admissible policy. Current accepted classification is:

`ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`.

This is local evidence only and is not global HJB nonexistence.

## Central scientific question

At an **interior illiquid-`a` node**, when the policy generated with the backward `a` derivative implies `g_a>0` while the policy generated with the forward `a` derivative implies `g_a<0`, does the corrected finite-difference Hamiltonian/upwind law require an endogenous zero-drift switching case analogous in numerical role to the already adopted interior-liquid `Z` switching law?

In particular, determine whether the correct local branch should impose

`g_a = r_a a + d = 0`

and choose a shadow/value derivative `q_a` inside the appropriate interval between the one-sided derivatives, while simultaneously satisfying the transfer FOC/KKT law and the lower-`b` active equality.

Do **not** assume the answer is yes merely because the two one-sided drifts cross.

## Required derivation

Use only frozen equations, persisted evidence, static source inspection and scalar algebra.

### A. Reconstruct the interior-a Hamiltonian/upwind law

1. Write the exact local Hamiltonian terms involving `q_b`, `q_a`, transfer `d`, adjustment cost `C(d,a)`, liquid drift `g_b`, and illiquid drift `g_a=r_a a+d`.
2. State the frozen derivative-direction consistency rules for interior `a`.
3. Explain why the observed sign pattern
   - backward derivative -> `g_a>0`
   - forward derivative -> `g_a<0`
   is or is not the standard strict-crossing situation in which neither one-sided derivative is self-consistent.
4. Distinguish this from:
   - the active lower-`a` state constraint / zero-kink multiplier law;
   - the already adopted interior-liquid `Z` branch;
   - a state-boundary KKT multiplier.

### B. Derive the candidate zero-a-drift law, if mathematically justified

For a candidate `g_a=0` branch, derive without calling any solver:

1. `d_Z=-r_a a`.
2. Determine the transfer regime at cell100.
3. Under D3
   `C(d,a)=chi_0|d|+chi_1 d^2/(2 max(a,a_bar))`,
   derive the exact transfer FOC/KKT relation linking `q_a/q_b` to `d_Z`.
4. At this cell, because `a>a_bar`, simplify the relation as far as the frozen parameters permit.
5. Derive the necessary interval condition for the switching shadow derivative `q_a` relative to `p_a^F` and `p_a^B`. Explicitly state orientation and inclusivity.
6. Combine that interval with the lower-`b` active domain `q_b>=p_b`.
7. Determine whether the resulting admissible `q_b` interval is empty or nonempty.

Pure scalar substitution/arithmetic from persisted numbers is allowed. Do not invoke the selector, root routines, HJB, policy map, or another scientific evaluator.

### C. Liquid equality compatibility

If B yields a nonempty candidate interval:

1. Write the exact frozen lower-`b` active liquid equality for `g_b=0` with `d=d_Z`.
2. Use persisted scalar values and static algebra to determine whether the equality can be shown:
   - to have no root in the candidate interval;
   - to have a unique compatible crossing in the candidate interval;
   - or to remain unresolved without a new scientific root evaluation.
3. You may use already-persisted neighboring/root endpoint values as inequalities or brackets.
4. Do not execute a root finder or selector.
5. Do not infer admissibility solely from the two existing branch roots; prove what they do and do not imply.

### D. Compare against accepted authority

Audit whether a zero-`a)-drift switching branch is:

1. already implied by the accepted D3 Hamiltonian/upwind semantics but missing from the selector;
2. a genuinely new scientific law analogous to, but not entailed by, the accepted liquid-`Z` law;
3. incompatible with existing D1/D2/D3 authority;
4. or unresolved because the accepted documents do not specify the necessary viscosity/upwind selection rule.

Read the actual accepted authority. Do not transfer the liquid-`Z` rule to the `a` axis by analogy alone.

### E. Alternative explanations

Explicitly test, at the level possible without runtime:

- finite-`a` domain truncation as an explanation;
- lower-`b` boundary interaction;
- grid-spacing / one-sided derivative discretization;
- V2 trajectory/initialization dependence;
- whether cell100 being interior in `a` weakens a pure `a`-domain-boundary explanation.

These alternatives may remain future hypotheses, but the report must rank them by what the frozen evidence actually supports, without turning that ranking into an unapproved repair.

### F. Scope if a zero-a branch is proposed

If the evidence supports an interior-`a` zero-drift branch, specify a **prospective scientific contract** for Owner review only:

- trigger condition;
- required derivative interval;
- `g_a=0` equality;
- transfer regime and FOC/KKT;
- interaction with lower/upper `b` active faces;
- how Hamiltonian comparison would work;
- D2 consumed-drift representation;
- receipt fields required for audit;
- what existing branches remain unchanged.

Do not implement it.

## Required classification

Return exactly one primary classification:

- `ADJUDICATED__INTERIOR_A_ZERO_DRIFT_SWITCHING_BRANCH_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`
- `ADJUDICATED__INTERIOR_A_ZERO_DRIFT_SWITCHING_NOT_SUPPORTED__FROZEN_LOCAL_INCOMPATIBILITY_STANDS`
- `ADJUDICATED__FINITE_DOMAIN_OR_BOUNDARY_INTERACTION_CONTROLS__OWNER_DOMAIN_DECISION_REQUIRED`
- `BLOCKED__ACCEPTED_AUTHORITY_INSUFFICIENT_TO_ADJUDICATE_INTERIOR_A_SWITCHING`
- `BLOCKED__PERSISTED_EVIDENCE_INSUFFICIENT_FOR_STATIC_ADJUDICATION`

A secondary note may identify unresolved alternatives, but do not invent a sixth primary classification.

## Zero-science ledger

All of the following must remain exactly zero:

- selector evaluations;
- scalar root calls;
- interior-Z or proposed a-Z root calls;
- policy maps;
- D2/Q assemblies;
- Bellman/checkpoint scientific evaluation;
- HJB solves/updates;
- graph/SCC;
- KFE/SVD/eigen/nullspace/`Q.T@p`;
- MATLAB;
- outer/firm/wage-return/GE/annual/shock/IRF/Results;
- scientific retries.

Allowed work:
- static Git/source/doc reads;
- persisted JSON/NPZ metadata reads without scientific recomputation;
- hashing;
- text parsing;
- symbolic derivation;
- direct scalar arithmetic/substitution of persisted values.

No source code, selector, solver, grid, parameter, tolerance, scientific receipt or accepted evidence may be modified.

## Deliverable

Write exactly one new report:

`docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_REPORT.md`

The report must contain:

- authority/evidence inventory;
- exact equations;
- cell100 scalar derivation;
- interval/sign proof;
- comparison with liquid-`Z` and lower-`a` zero-kink laws;
- alternative-explanation assessment;
- prospective contract if supported;
- zero-call ledger;
- one required primary classification.

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish a successor task.
Do not modify CURRENT status/handoff/roadmap/index.
Do not adopt the proposed law on behalf of Owner.

Results eligibility remains `FALSE`.
