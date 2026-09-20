# CH5 MP4C turn-2 Hebei F0005 lower-a / interior-liquid switch forensic

Date: 2026-09-21

## Terminal and classification

`PASS__TURN2_HEBEI_F0005_FORENSIC__ACTIVE_LOWER_A_INTERIOR_Z_COMPOSITION_FALSE_NEGATIVE_CONFIRMED__NO_CODE_CHANGE`

Classification:

`IMPLEMENTATION_COMPOSITION_FALSE_NEGATIVE_UNDER_ALREADY_ADOPTED_AUTHORITY`

The Owner-adopted generic interior-liquid `Z` law and the already adopted
active-lower-`a` zero-kink multiplier law uniquely imply one admissible combined
candidate at the persisted Hebei cell. The current selector omits that combined
family before Hamiltonian comparison. The persisted `NO_ADMISSIBLE_POLICY` is
therefore an implementation/composition false negative. This forensic does not
authorize a repair or a scientific rerun.

## Binding

- fresh live-main baseline: `3473ada0d9d6d8767383969dc5fe268763cebf54`
- accepted predecessor: `f178ec24b9b62814d20ec4041380e07e2d878849`
- accepted run003 manifest: `E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403`
- cell Git blob: `c65495d43560c35ea789a3048c2b1440ed35735a`
- cell SHA-256: `8912DB5CB51FC02466E924A5ADC3FF44755FBD0A97AF1BEB42D19BF8200043B1`
- predecessor independent readback: PASS, zero bad paths

Exact cell:

- province: Hebei
- checkpoint: 1
- F-order flat index: 5
- index: `(5,0,0)`
- cell id: `v001_f0005_b005_a000_z000`
- state: `b=-0.1578947368421053`, `a=0`, `z=0.8`
- active face: lower-`a`; liquid `b` is interior
- `p_a^B=p_a^F=0.010591720688767481`
- `p_b^B=0.016103423470140932`
- `p_b^F=0.008913524380688508`
- persisted outcome: `NO_ADMISSIBLE_POLICY`
- persisted candidates: 15; admissible candidates: 0
- persisted active-lower-`a` + interior-`Z` candidates: 0

## Legal family under adopted authority

At active lower-`a`, the equality requires

`d=-r_a*a=0`.

Consequently the negative and positive transfer families are illegal for the
active lower-`a` equality. The unique legal transfer family is `zero_kink`, with
the inward a derivative branch `forward`. Its lower-face shadow law is

`q_a in [p_a,+infinity) intersect [q_b(1-chi_0),q_b(1+chi_0)]`,

using the deterministic minimum of that nonempty intersection. The liquid axis
may use backward, forward, or the Owner-adopted interior `Z` branch.

The interior-a switching prohibition does not apply: `a` is on an active lower
face and uses the pre-existing lower-face equality/multiplier law. This
candidate creates no new interior-a switching shadow and no simultaneous
two-interior-axis switching law.

## Endpoint liquid crossing

For the same active-lower-`a`, a-forward, zero-kink family, `d=0`, cost is zero,
and the raw liquid drift depends on `q_b` but not on the selected kink-interval
`q_a`:

| liquid endpoint | q_b | c | l | raw g_b |
|---|---:|---:|---:|---:|
| backward | `0.016103423470140932` | `7.880266285299264` | `0.7318719392018086` | `+1.7486866578989382` |
| forward | `0.008913524380688508` | `10.591934138791665` | `0.6502215286191101` | `-2.027652723229073` |

This is a strict arithmetic-bound-separated direction crossing. The backward
endpoint has a nonempty lower-a kink intersection. The forward endpoint's full
ordinary candidate has an empty endpoint intersection, but the adopted `Z` law
requires the a-side KKT and multiplier objects to be recomputed at the switching
shadow. Endpoint full admissibility is not substituted for that final switching
test; the liquid drift equation at `d=0` remains defined from persisted operands.

## Independent zero-liquid reconstruction

No production selector or root helper was imported or called. With the frozen
parameters `gamma_c=2`, `phi=5`, and labor weight one,

```text
c(q)   = q^(-1/2)
l(q)   = (q*w_net)^(1/5)
g_b(q) = w_net*l(q) + r_b*b + T - c(q)
```

where

`m=r_b*b+T=0.085789473684210521421052631578947`.

Setting `l=l(q)` gives the independent monotone polynomial

`F(l)=(w_net*l+m)^2*l^5-w_net=0`.

Decimal bisection on the exact derivative bracket gives

- `l*=0.6910376936366837138249106065318478345811409009933540569851599911...`
- `c*=9.0964992997271010935927706502569827544355093028204915765110851229...`
- `q_b*=0.0120851325790094875041402945557588462734692022962404697375483941...`
- Decimal residual: `-3E-89`

The root lies strictly inside
`[0.008913524380688508,0.016103423470140932]`.
For every positive `q`, `g_b'(q)>0`, while the limits at zero and infinity have
opposite signs. The positive root is therefore unique.

## Lower-a KKT reconstruction at the switching shadow

Using the current binary64 operation order at `q_b*`:

- `q_b=0.012085132579009488`
- zero-kink target interval:
  `[0.01087661932110854,0.013293645836910438]`
- `p_a=0.010591720688767481`
- deterministic `q_a=0.01087661932110854`
- lower-a multiplier:
  `lambda_a=q_a-p_a=0.00028489863234105843`
- `d=0`, cost `=0`
- raw/canonical `g_a=0/0`
- raw/canonical `g_b=0/0`
- transfer-KKT residual: `0`
- lower-a slack: `0`
- lower-a complementarity residual: `0`
- candidate arithmetic tolerance: `2.0960674472970927e-13`
- interior-Z arithmetic bound: `2.901541422966794e-13`
- utility and Hamiltonian: `-0.1280816705218543`

All domain, finite-value, active equality, multiplier, feasibility,
complementarity, transfer-KKT, direction and zero-drift-bound checks pass. Since
all 15 persisted candidates are inadmissible, this combined candidate would be
the unique admissible policy entering the unchanged Hamiltonian comparison.

## Exact selector omission

The current control flow performs these steps:

1. At selector line 799 it constructs the active lower-a zero-kink interval for
   each ordinary liquid endpoint.
2. At line 808 the forward endpoint returns early because that endpoint's
   interval is empty; controls are computed only later at line 817. The rejected
   object therefore has `g_b=None`.
3. At line 1092 the interior-Z constructor requires both endpoint `g_b` values
   and arithmetic bounds. It returns before the call site at line 1612 can
   reconstruct a `Z` root for this active family.
4. The combined family never reaches the Hamiltonian comparison at line 1677.

If the already adopted `Z` root is reached, the existing `_candidate` route
would recompute the lower-a kink interval at the root before applying the
unchanged feasibility, KKT, direction, finite and Hamiltonian checks. The
omission is therefore control-flow composition, not an absent scientific law.

## Verification and ledger

- focused tests: 4 passed
- `py_compile`: PASS
- `git diff --check`: PASS
- production source modifications: 0

Two formal pure-arithmetic evidence generations were performed. The first
unpublished draft was regenerated once to distinguish the high-precision
mathematical `q_a=0.9q_b` from the current binary64 operation order. This was a
serialization/arithmetic-reporting correction, not a scientific retry.

Zero-science ledger:

- persisted cell loads: 6 total, including 4 focused-test loads and 2 formal runs
- independent Decimal equation reconstructions: 4 total, including 2 tests and 2 formal runs
- binary64 scalar spot checks: 1
- production selector calls: 0
- production root-helper calls: 0
- HJB/direct updates: 0
- D2/Q: 0
- SCC/KFE/SVD: 0
- aggregate/integration: 0
- firm/K1A/C1/wage/monetary/fiscal: 0
- turn-2 replay: 0
- turn 3: 0
- MATLAB: 0
- GE/annual/shock/IRF/welfare/Results: 0
- retry/tuning: 0

## Evidence closure

- root:
  `reports/ch5_mp4c_turn2_hebei_f0005_lower_a_liquid_switch_forensic_20260921_run001/`
- sealed manifest SHA-256:
  `039E74760D6FFAC8DD3177723B6F7EE9FFC9CFE2BD6C192EF4EB34160DAD026A`
- entries: 11
- bytes: 23,993
- independent readback: PASS
- bad paths: none
- scientific calls recorded by readback: 0

No selector repair, Hebei rerun, turn-2 continuation, turn 3, CURRENT change,
main merge, or successor publication was performed. Results eligibility remains
`FALSE`. The next gate is independent Reviewer acceptance of this forensic.
