# CH5 MP4C 2018 KFE D1-D3 Q1 source-free operator validation acceptance

Date: 2026-09-16

Reviewer verdict:

`PASS__Q1_UNIQUE_SOURCE_FREE_INVARIANT_MASS_ACCEPTED__OPERATOR_LEVEL_GATE_CLOSED__NONLINEAR_HJB_FIXED_POINT_DESIGN_REQUIRED_NEXT`

Accepted candidate: `580a48c2aa4d969f471293d6022c3cdf3bc1425e`.

## Accepted findings

The exact accepted Q1 artifact SHA-256 `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E` passed the frozen pin-free/source-free KFE operator contract.

Accepted evidence:

- exact-positive graph has exactly one closed communicating class with membership `[5,6,405,406]`;
- numerical rank/nullity is `799/1` from exactly one dense full `gesvd`;
- second-smallest singular value `0.01704325702964291` is strictly above frozen `tau_rank=5.728066976324905e-12`;
- `||Q1.T @ p||_inf = 1.927355525830249e-15` is below frozen stationarity bound `3.076397750501459e-12`;
- `math.fsum(p)=0.9999999999999999`;
- minimum stored mass `-7.838997498725127e-15` is inside the frozen arithmetic nonnegativity allowance; values were not clipped;
- no retry, tolerance tuning, solver substitution, row replacement, pin, source RHS, iterative eigensolver, selector/policy remap, D2 reassembly, HJB/V2, MATLAB or downstream call occurred.

The accepted Q1 stationary mass is therefore unique for this finite Q1 operator, source-free, normalized and nonnegative within the preregistered floating-point allowance.

## Interpretation boundary

This acceptance does **not** establish nonlinear HJB convergence, a joint HJB-KFE fixed point, a stationary economic equilibrium, production replacement, calibration validity beyond the frozen diagnostic inputs, or Results eligibility.

Q1 is the operator induced by one remap of the accepted one-step value function V1. The next scientific gate must determine how to test nonlinear HJB convergence and a joint fixed point without silently equating the current Q1 invariant mass with an equilibrium distribution.

Results eligibility remains `FALSE`. Production/source-faithful paths remain unchanged.
