# CH5 MP4C K1 — J160 bounded cross-state confirmation acceptance

Date: 2026-09-15

Reviewer verdict:

`J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTED__PRACTICAL_DIAGNOSTIC_GRID_SUPPORTED__LIQUID_I_PRECISION_NEXT`

Results eligibility=`FALSE`.

## Candidate

Accepted Builder candidate: `0430057603da6fb83ae4731ce4139def149c090c`.

Baseline: `1c2d2b0bc0167b1821315164356e461a0f3c05fa`.

The candidate is exactly one commit ahead of baseline and modifies only the task report, compact evidence, focused test, and task-owned offline finalizer package. Protected HJB/KFE scientific source is unchanged.

## Finalizer repair acceptance

The unequal-support comparison repair is accepted as engineering-only. Same-support semantics are preserved. For unequal supports, the raw signed CDFs are compared over the union interval with zero extension below support and raw-total-mass extension above support. No clipping, renormalization, smoothing, rebinning, or solver import is introduced.

All J20→J160 marginal metrics are correctly named `DOMAIN_PLUS_GRID_CDF_DISTANCE`; they are not grid-only precision measures because both support and discretization changed.

## Science acceptance

Raw-evidence integrity passed for the four authorized fresh J160 corner states. Preserved science ledger is HJB `4/4`, KFE `4/4`, scientific retries `0`, accepted center/J20 reuse runtime `0`, and all forbidden runtime categories `0`.

Accepted five-state facts:

- `(.06,13)`: HJB converged in 14 iterations; `At≈85.6697`, `Bt≈4.82888`, modal `a≈90.5660`, modal `b≈2.63158`, `amax mass=0`, `bmax mass≈1.62e-5`.
- `(.06,18)`: HJB converged in 68 iterations; `At≈81.1883`, `Bt≈5.97040`, modal `a≈75.4717`, modal `b≈1.47368`, `amax mass=0`, `bmax mass≈0.01630`.
- center `(.0675,15.5)` reused: `At≈89.2978`, `Bt≈5.81025`, modal `a≈94.3396`, modal `b≈2.63158`.
- `(.07,13)`: HJB converged in 11 iterations; `At≈90.7323`, `Bt≈5.78054`, modal `a≈94.3396`, modal `b≈2.63158`, `amax mass=0`, `bmax mass≈0.000155`.
- `(.07,18)`: HJB converged in 17 iterations; `At≈89.6487`, `Bt≈6.15232`, modal `a≈95.5975`, modal `b≈2.63158`, `amax mass=0`, `bmax mass≈0.00282`.

All four fresh HJBs are legal/converged and all four KFE receipts are valid/nonpathological. Tiny signed density entries remain at floating-point scale and are preserved raw.

## Scientific interpretation

`a=[0,100]` is nonbinding for the tested bounded states: every fresh `amax mass=0` and every modal `a` is interior.

`b=[-2,20]` is nonbinding in the bounded-diagnostic sense for the tested states: no modal `b` sits at `bmax`; the largest fresh `bmax` mass is about `0.01630` and remains a nonmodal tail.

The five-state results are finite and scientifically interpretable. The slower 68-iteration `(.06,18)` point is still within the frozen HJB gate and does not reproduce J640 nonconvergence.

Therefore `I=20,J=160` is accepted as a **practical bounded diagnostic grid** for the household block. This does **not** establish continuum convergence, production-final precision, GE validity, or Results eligibility.

## Remaining numerical authority gap

Illiquid-grid escalation above J320 is closed under the current MATLAB-faithful HJB because J640 enters policy/selector chatter with value oscillation.

The remaining local precision gap is the liquid dimension: `I=20` implies `db=22/19≈1.1578947368`. Although `bmax=20` is nonbinding across the tested J160 states, no dedicated I-grid sensitivity has yet established whether `Bt` and the b-marginal are stable when `I` is refined.

Reviewer route: run a bounded representative-state liquid-grid precision sensitivity at fixed `J=160`, without reopening the finer-J route.
