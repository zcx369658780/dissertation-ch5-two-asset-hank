# Chapter 5 Two-Asset HANK R4 — Steady-State Authorization

Date: 2026-08-22

## Verdict

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_PASS`

Acceptance level:

`R4_STEADY_STATE_FIXTURE_PREAUTHORIZED_IMPLEMENTATION_NOT_YET_EXECUTED`

This gate freezes one source-independent stationary-validation fixture and its
acceptance conditions before any solve. It authorizes no steady-state execution,
aggregate, calibration, or Results claim.

## Live authority and repository state

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched `origin/main`:
  `3dbb5b841911bb4130d786d9d4ac5af0f95e0f66`
- Local baseline: `46d98d140cebcefb795c14f3ba8f61a515d5f6ac`
- Start relation: 0 ahead / 29 behind
- Live task:
  `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION.md`
- No pull, checkout, merge, reset, clean, commit, or push was used.

## Files read

- live `AGENTS.md`;
- live project-rule index and routed GitHub-capability rule;
- live R4 steady-state authorization task;
- R1 final equation/KFE freeze;
- accepted reflected fixed-lower R2 HJB report;
- R3 KFE operator report;
- R3 stationary-uniqueness diagnostic and resolution reports;
- current generator, indexing, contracts, economics, policy, KFE contract, and
  KFE operator sources.

## Files written

- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_REPORT.md`

No code, test, solver, policy, generator, parameter file, or existing evidence
was modified.

## Proposed fixture design

### Scope and identity

Fixture identifier:

`R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`

The fixture is test-only and source-independent. Its values are not final
calibration, empirical units, dissertation experiment inputs, or MATLAB parity
targets.

Only the exact fixture below may be attempted in the next implementation gate.
If it fails, execution must stop. No value may be tuned after observing the
result.

### State grids

Illiquid asset:

- core grid `a=(0,0.5,1.0)`;
- `N_a=3`;
- spacing `h_a=0.5`;
- `a=0.5` is an explicit interior node;
- `a=1.0` is a computational upper truncation, not an economic upper bound.

Liquid asset:

- `b=(0,2.5,5.0)`;
- `N_b=3`;
- `b_bar=0`;
- spacing `h_b=2.5`;
- `b=5.0` is a computational upper truncation.

Productivity:

- fixed economic lower support `z_L=0.5`;
- spacing `h_z=0.0625`;
- core diagnostic domain `[0.5,1.5]`, 17 nodes;
- primary stationary-validation domain `[0.5,2.0]`, 25 nodes;
- upper-buffer verification domain `[0.5,2.25]`, 29 nodes;
- the reflected lower row and accepted computational upper closure remain
  unchanged.

Primary stationary state count:

`3*3*25=225`.

### Economic parameters

`EconomicParams`:

- `rho=0.05`;
- `gamma_c=1.0`;
- `phi=1.0`;
- `chi_0=0.05`;
- `chi_1=1.0`;
- `a_bar=0.5`;
- `mu_z=0.2`;
- `sigma_z=0.1`.

`HouseholdInputs`:

- `r_a=0.04`;
- `r_b=0.03`;
- `tau=0`;
- one province with `w_0=1`;
- `sigma_0=0`;
- labor weight `phi_0=1`.

Scientific meaning of these numbers:

- the one-percentage-point synthetic illiquid return premium gives the frozen
  transfer control an economic reason to move resources toward `a`;
- `chi_0=0.05` retains a nonzero inaction band while avoiding the prior
  test-only value `chi_0=1`, under which every accepted state selected
  `d=0`;
- all values remain explicit test inputs and must not be re-labelled as
  calibration.

### Frozen initialization

For each `(b,z)`, define:

`y=r_b*b`

`c_0=0.5*(y+sqrt(y^2+4*z^2))`

`l_0=z/c_0`

`V_0=(log(c_0)-0.5*l_0^2)/rho`

Broadcast this value across the three `a` nodes. No transfer, clipping, or
steady-state distribution is embedded in the initialization.

### Frozen numerical settings

HJB:

- pseudo-time step: `10`;
- maximum iterations: `500`;
- iteration-change tolerance: `1e-8`;
- true HJB residual tolerance: `1e-7`;
- KKT tolerance: `1e-7`;
- generator tolerance: `1e-11`;
- drift/zero tolerance: `1e-12`.

KFE diagnostics:

- stationary residual tolerance: `1e-10`;
- normalization tolerance: `1e-10`;
- non-negativity tolerance: `1e-12`;
- graph-edge tolerance: `1e-11`.

Probability mass is normalized by `sum(g)=1`, without quadrature weighting.
If density is reported for the fixture, use tensor-product trapezoidal cell
weights: half spacing at each finite endpoint and full spacing at interior
nodes. Density is `g/omega`; it must not be used to renormalize mass.

## Required endogenous connectivity conditions

The next implementation gate must derive every `a` transition from the final
selected policy through:

`mu_a=r_a*a+d`.

It must prove all of the following:

1. `G_a` has at least one positive upward off-diagonal edge;
2. `G_a` has at least one positive downward off-diagonal edge;
3. all `G_a` rates equal the accepted directional `mu_a/h_a` construction;
4. no cross-`a` edge comes from `G_b`, `G_z`, or a regularization matrix;
5. the combined selected-policy generator has exactly one closed recurrent
   class;
6. the closed class spans at least two distinct `a` indices and includes the
   interior node `a=0.5`;
7. the unique class is not solely the computational upper `a=1.0` layer;
8. numerical left nullity is one, or an equivalent independent uniqueness check
   agrees with the graph result.

Bidirectional motion need not occur at every state. Transient states are
permitted. The conditions prevent both the old invariant `a` layers and a
spurious absorbing computational-upper layer from qualifying as success.

## Compatibility with existing gates

The next implementation must retain without modification:

- canonical logical shape `(N_a,N_b,N_z)` and a-fast flattening;
- Chapter 5 budgets, controls, transfer sign, and adjustment cost;
- lower-bound active-set/KKT construction;
- computational upper no-outflow handling;
- reflected fixed lower productivity row;
- one shared `G=G_a+G_b+G_z` for HJB and KFE;
- deterministic candidate selection;
- true final HJB residual;
- the accepted 25-versus-29-node productivity truncation comparison.

The primary and upper-buffer HJB solves must both satisfy all existing R2
residual, KKT, generator, candidate-identity/tie, and common-core thresholds.
Stationary KFE evaluation is permitted only after those checks and the
connectivity conditions pass.

## Stationary acceptance conditions

On the final primary selected-policy generator:

- one closed recurrent class;
- left nullity one;
- direct `||G^T g||_infinity<=1e-10`;
- `|sum(g)-1|<=1e-10`;
- minimum mass `>=-1e-12`;
- negative-mass count zero below the declared tolerance;
- finite mass and density;
- `sum(density*omega)=1`;
- separate `A_hh=sum(a*g)` and `B_hh=sum(b*g)`.

These aggregates are synthetic fixture diagnostics only. They are not Chapter 5
Results and must not be interpreted economically beyond validating accounting.

## Scientific rationale

The prior fixture used two `a` nodes, both boundaries, `r_a=0`, and
`chi_0=1`. Its converged policy selected `d=0` everywhere, so
`mu_a=0` and every `a` layer was invariant.

The new fixture changes only test-only configuration that the R1 freeze left for
later authority:

- an interior `a` node exposes unconstrained illiquid movement;
- a modest illiquid return premium supplies an endogenous saving incentive;
- a smaller but positive inaction band permits both action and inaction to be
  observed;
- three liquid nodes retain an interior liquid state;
- the accepted fixed-lower productivity family preserves the already validated
  diffusion/truncation contract.

The mechanism remains the frozen household control `d`; no new shock or
economic equation is introduced. Structural support does not guarantee the
solve will pass. That uncertainty is intentional and must be resolved by the
next one-shot implementation gate.

## Failure policy

The next gate must stop at the first terminal failure and report evidence if:

- HJB, KKT, generator, productivity, or truncation acceptance fails;
- the final policy lacks either upward or downward endogenous `a` movement;
- the chain has zero or multiple closed classes;
- the only closed class lies solely on computational `a_max`;
- left nullity is not one;
- stationary residual, normalization, non-negativity, finiteness, density, or
  separate asset accounting fails.

After any failure, do not change a grid, return, cost, wage, wedge, tolerance,
initialization, or candidate rule in the same gate.

## Forbidden-operation check

- no HJB or steady-state solve was run;
- no recurrent class was selected;
- no invariant mixture was constructed;
- no row was pinned;
- no artificial transition was added;
- no calibration, equation, policy, generator, source, or test was modified;
- no transition solver or AR(1) engine was implemented;
- no IRF or dissertation experiment was run;
- no Results prose or MATLAB-Python parity claim was produced;
- MATLAB and protected scientific sources were not read, run, or modified;
- no successor task was created;
- all existing untracked evidence was preserved.

## Recommended next gate

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION`

That task may authorize exactly one execution of
`R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1`. It must forbid adaptive tuning,
retain every acceptance condition above, and stop without R4 acceptance or
Results claims on any failure.

This authorization report does not itself authorize the solve.
