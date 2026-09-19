# CH5 MP4C 2018 KFE D1-D3 V2 cell100 interior-a zero-drift switching adjudication acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__ZERO_SCIENCE_ADJUDICATION_ACCEPTED__INTERIOR_A_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`

## Accepted candidate

- baseline live main before adjudication: `a4c1a70b928e1c47b6c402f452d3c8423e73f870`
- Builder candidate: `d4ed09015f184ab8e4a39e1de019c33b8868cd20`
- candidate tree: `f27be98c91396ed978764956f24e0b6faeff40ab`
- candidate is exactly `1 ahead / 0 behind` baseline
- changed path is exactly one new report:
  `docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_REPORT.md`
- no source, task, CURRENT file, parameter, tolerance, receipt or accepted evidence was modified
- Results eligibility remains `FALSE`

## L3 acceptance

The adjudication is accepted as:

`ADJUDICATED__INTERIOR_A_ZERO_DRIFT_SWITCHING_BRANCH_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`.

The accepted V2 cell100 state is interior in illiquid `a` and lies at the lower liquid boundary. Under the repaired complete eight-case selector census:

- active lower-b / negative-transfer / backward-`a` produces `g_a=+0.00670682022114244`, contradicting the backward direction;
- active lower-b / negative-transfer / forward-`a` produces `g_a=-0.0005429159000894801`, contradicting the forward direction.

This is a strict interior-`a` upwind crossing: neither one-sided derivative is self-consistent.

## Accepted static derivation

Imposing a prospective zero-illiquid-drift branch gives:

`d_Z=-r_a a=-0.23684196191023801`.

This is a negative-transfer regime. Under frozen D3,

`q_a/q_b = 1-chi_0-chi_1 r_a = 0.72000010894821909`.

The closed one-sided derivative interval

`q_a in [p_a^F,p_a^B]`

therefore maps to

`q_b in [0.012440285887428097, 0.012546045881996438]`.

The entire interval satisfies the active lower-b multiplier domain

`q_b >= p_b = 0.012333311206716577`.

For fixed `d_Z`, the frozen lower-b liquid equality is continuous and strictly increasing on `q_b>0`. Its values at the candidate interval endpoints are:

- lower endpoint: `-0.0039748658728543454`;
- upper endpoint: `+0.048890867998731984`.

The sign change plus strict monotonicity proves one and only one compatible crossing in the prospective D3/upwind/lower-b interval. No root call is needed for this existence-and-uniqueness conclusion.

## Authority boundary

The proposed branch is compatible with the accepted D1/D2/D3 contracts:

- D3 supplies the adjustment technology and transfer KKT;
- D1 permits the corresponding lower-b multiplier domain;
- D2 can consume exact zero `g_a` and, when active, exact zero `g_b` without adding asset drift transitions.

However, existing authority does not itself create an interior-`a` switching shadow between one-sided derivatives. The previously adopted liquid `Z` law is liquid-axis specific and was itself Owner-adopted. The lower-`a` zero-kink multiplier law is a state-boundary construction and is not an interior derivative-selection rule.

Therefore the adjudicated branch is **scientifically supported but not yet adopted**. Explicit Owner adoption is required before implementation or runtime.

## Prospective contract accepted for Owner review

The Builder report's ten-point prospective contract is accepted as the minimal adoption candidate:

1. trigger only at interior `a` nodes with strict arithmetic-bound-separated backward-positive / forward-negative `g_a` crossing under the same frozen `b` branch/active set and transfer regime;
2. impose `g_a=0` via `d_Z=-r_a a`;
3. obtain `q_a` from unchanged D3 KKT/subgradient;
4. require `q_a` in the closed sorted interval between `p_a^F` and `p_a^B`;
5. intersect the implied `q_b` interval with the relevant liquid-face multiplier domain, with a compatible `g_b=0` root required for an active liquid face;
6. reconstruct controls and KKT objects from candidate shadows without endpoint interpolation;
7. include the candidate in the existing Hamiltonian comparison only after all frozen legality checks pass;
8. D2 consumes canonical zero drift only within the prospectively frozen arithmetic residual rule;
9. persist full crossing/interval/root/KKT/Hamiltonian receipt evidence;
10. preserve existing backward/forward branches, liquid-`Z`, lower-`a` zero-kink, D1/D2/D3, solver, grid, calibration, convergence law and production routes.

This acceptance does not itself adopt those ten points as scientific law.

## Alternative explanations

The report's assessment is accepted:

- pure finite-`a` boundary truncation is weak as the immediate local mechanism because cell100 is interior in `a`;
- the lower-`b` boundary is material but statically compatible with the prospective branch;
- grid spacing/one-sided discretization may generate or move the strict crossing;
- V2 trajectory/initialization dependence remains a real limitation because V2 is not a converged fixed point.

These caveats do not overturn the local switching-law support, but they prohibit interpreting the finding as an economic discontinuity or global HJB existence result.

## Zero-science ledger

Accepted as all-zero for selector/root/policy-map/D2/Q/Bellman/HJB/graph/KFE/MATLAB/downstream/Results/scientific retry.

## Owner gate

No implementation task is authorized by this acceptance.

Owner must explicitly adopt, modify or reject the prospective interior-`a` zero-drift switching contract before Reviewer may publish an implementation/single-cell/bounded-remap successor.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain closed.
