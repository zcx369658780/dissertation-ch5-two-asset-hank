# CH5 MP4C K1 — J160 coordinate-resolved selector/floor matched-control diagnostic freeze

更新：2026-09-15。

状态：`FREEZE_ACTIVE`。

## Scientific purpose

Previous accepted six-failure spatial localization is heterogeneous at the level of value-update argmax coordinates, but selector changed-cell coordinates and derivative-floor hit coordinates are unavailable. The next diagnostic asks whether selector/floor activity is concentrated at specific boundaries/interior regions and whether those footprints distinguish failed HJBs from nearby accepted successful first-turn HJBs.

This is an observational-instrumentation diagnostic. It does not authorize any scientific-source modification, recalibration, boundary-law change, grid/domain change, or convergence tuning.

## Frozen household science

- Grid: `I=20,J=160,Nz=2`.
- `a=[0,100]`, `b=[-2,20]`.
- Diagnostic bridge `h=1`.
- Source-faithful HJB equations, FOCs, selectors, boundary laws, derivative-floor logic, `Delta=1000`, tolerance `1e-7`, maxit `100`, A2max legality gate `0.01`, economic parameters, exact province household-call inputs, wage/return mappings and guards all remain unchanged.
- Fresh source-style initialization for every replay; no warm starts.
- KFE=0.

## Exact matched panel

Failure representatives are selected before execution to span accepted mechanism/spatial classes:

1. 天津 — chatter + mixed value-argmax footprint.
2. 江西 — floor-amplified + liquid-upper-bound-concentrated value-argmax footprint.
3. 贵州 — period-2 joint-selector recurrence + mixed value-argmax footprint.
4. 甘肃 — chatter + liquid-upper-bound-concentrated value-argmax footprint.

Matched accepted successful controls are fixed from the prior nearest-successful-neighbor authority:

5. 湖南 — matched control for 天津/山西 neighborhood.
6. 上海 — matched control for 江西/重庆 neighborhood.
7. 福建 — matched control for 贵州/甘肃 neighborhood.

Exactly these seven province inputs may be replayed. No other province or synthetic `(ra,w)` point is authorized.

## Observational instrumentation

Task-owned instrumentation may observe, at each HJB iteration:

- exact coordinates of liquid-selector changed cells;
- exact coordinates of transfer/illiquid-selector changed cells;
- exact coordinates of derivative-floor hits, separated by floor type if the accepted implementation has distinct floor classes;
- counts and hashes already available in prior accepted instrumentation;
- value-update argmax coordinates for cross-reference.

Coordinates must be reported as grid indices and state values `(b,a,z)`.

Instrumentation must not feed back into scientific control flow, modify arrays used by the HJB, alter selector decisions, alter floor application, change solve order, change convergence checking, or retain state between provinces.

## Spatial bins

For descriptive summaries, spatial bins are fixed before execution:

- exact lower endpoint;
- near-lower boundary: exactly one grid index inside the lower endpoint;
- interior;
- near-upper boundary: exactly one grid index inside the upper endpoint;
- exact upper endpoint.

For joint `(b,a)` summaries, report liquid-boundary, illiquid-boundary, dual-boundary, and double-interior shares without inventing post-result thresholds.

## Matched-control interpretation

The key comparison is descriptive:

- failure versus its fixed successful control(s);
- mechanism class versus selector/floor spatial footprint;
- value-argmax footprint versus selector/floor footprint.

A boundary concentration seen in failures but also equally present in converged controls is not failure-specific evidence. Conversely, failure-specific concentration is still diagnostic evidence only, not causal identification and not repair authority.

## Runtime budget

- HJB exactly 7 after a clean preflight.
- KFE=0.
- Scientific retries=0.
- Engineering retry <=1 and only before the first HJB for path/import/serialization/instrumentation plumbing; science unchanged.
- Outer/firm/wage recalculation/return recalculation/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results all 0.

## Hard stops

No maxit increase, tolerance change, Delta change, damping, relaxation, line search, policy freezing, floor change, selector change, FOC change, boundary change, solver change, grid/domain change, price/input change, recalibration, KFE, outer model, or new synthetic state.

Results eligibility=`FALSE`.
