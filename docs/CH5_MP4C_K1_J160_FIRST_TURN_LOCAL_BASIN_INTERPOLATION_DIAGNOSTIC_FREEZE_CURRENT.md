# CH5 MP4C K1 — J160 first-turn local-basin interpolation diagnostic freeze

Date: 2026-09-15

Status: ACTIVE FREEZE.

## Scientific purpose

Map local HJB convergence-basin topology between accepted first-turn failure/success pairs that are close in standardized consumed `(ra,w)` space. This is a bounded numerical diagnostic only. It is not recalibration and does not represent an upstream economic mapping.

## Frozen household science

Use accepted practical grid and household science unchanged:

- `I=20`, `J=160`, `Nz=2`;
- `a=[0,100]`, `b=[-2,20]`;
- diagnostic bridge `h=1`;
- source-style fresh initialization;
- tolerance `1e-7`, maxit `100`, `Delta=1000`, A2max legality gate `0.01`;
- accepted equations, FOCs, selectors, boundary laws, derivative floors, sparse solver and convergence test unchanged;
- KFE=0.

## Preregistered matched pairs

Use exactly four accepted failure/success pairs from the accepted standardized nearest-success audit:

1. 山西 failure ↔ 河北 success;
2. 重庆 failure ↔ 河北 success;
3. 江西 failure ↔ 安徽 success;
4. 贵州 failure ↔ 四川 success.

天津 is excluded because its accepted standardized nearest-success distance is much larger. 甘肃 is excluded to keep the experiment bounded; 贵州 represents the high-`ra`, lower-`w` failure region and has the distinct accepted low-period selector recurrence.

## Pair authority gate

For each pair, verify from accepted repository evidence that every consumed household-call input other than `consumed ra/rah` and household composite `w` is exactly equal, including `rb`, borrowing gap, tax, transfer, model parameters, guard metadata and adapter inputs.

If any pair differs on another consumed scientific input, that pair is unauthorized and the entire task stops before science as `LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER`.

## Synthetic interpolation rule

For each authorized pair define failure endpoint `F=(ra_F,w_F)` and success endpoint `S=(ra_S,w_S)`.

Do not rerun endpoints. Reuse their accepted outcomes.

Run exactly three synthetic points per pair:

- `t=0.25`: `(1-t)F + tS`;
- `t=0.50`;
- `t=0.75`.

Only `ra` and composite `w` are interpolated. All other consumed inputs use the pair-common accepted values.

Total new HJB calls: exactly 12 after clean preflight. KFE=0. Scientific retries=0.

These points are numerical interpolation probes only. They are not claimed to be feasible provincial equilibrium states, calibrated states, or outputs of the upstream wage/return mappings.

## Observational diagnostics

Reuse accepted observation-only instrumentation. For every synthetic point record at minimum:

- HJB terminal class: converged, legal nonconverged, illegal operator, hard error;
- iterations/final convergence statistic/max A2max;
- first selector switching, first value-stat non-decrease, first derivative-floor hit when available;
- broad temporal mechanism label for nonconverged points using the accepted preregistered taxonomy;
- no KFE.

Do not modify scientific control flow.

## Local-basin interpretation

For each pair report the ordered endpoint/interpolation outcome sequence at `t={0,.25,.5,.75,1}`.

Preregistered pair-level labels:

- `SINGLE_TRANSITION_FAILURE_TO_SUCCESS` — one ordered switch from failure/nonconvergence to convergence;
- `ALL_INTERIOR_PROBES_CONVERGE`;
- `ALL_INTERIOR_PROBES_FAIL`;
- `NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN` — outcome switches more than once or convergence/failure is interleaved;
- `PAIR_NUMERICAL_INVALIDITY_BLOCKER` — illegal/hard-error probe prevents basin interpretation.

Panel label exactly one:

- `LOCAL_BASIN_BOUNDARIES_SIMPLE_AND_PAIR_SPECIFIC`;
- `LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`;
- `LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED`.

No result authorizes a calibration threshold. No post-result adaptive bisection is allowed in this task.

## Hard prohibitions

No new pair, no extra `t`, no bisection, no maxit extension, no damping/relaxation/line search, no tolerance/Delta/floor/selector/FOC/boundary/solver/grid/domain change, no upstream firm/wage/return call, no KFE, no outer/GE/downstream/Results runtime.

Results eligibility=`FALSE`.
