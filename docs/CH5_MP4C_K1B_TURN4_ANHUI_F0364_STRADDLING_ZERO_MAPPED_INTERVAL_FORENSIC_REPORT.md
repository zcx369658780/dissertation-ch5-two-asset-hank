# CH5 MP4C K1B turn4 安徽 F0364 straddling-zero mapped-interval forensic

Date: 2026-09-21

## Result

Terminal:

`PASS__K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC__GUARD_FALSE_NEGATIVE_CONFIRMED__NO_SOURCE_CHANGE`

Classification A:

`TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_GUARD_FALSE_NEGATIVE_CONFIRMED`

The current whole-mapped-interval positivity guard rejects this exact cell even
though the persisted backward liquid derivative is finite, strictly positive,
inside the mapped interval's positive-domain intersection, and produces an
otherwise fully admissible switching candidate under the already adopted Owner
contract. Exactly one branch-local candidate is admissible.

This task made no production source change and executed no model science.

## Authority and exact bindings

- Live-main baseline: `3e11b05f497e4535e0655d64cba26a55bab9b582`.
- Exact cell: `v004_f0364_b004_a018_z000`, checkpoint 4, flat 364,
  index `(b,a,z)=(4,18,0)`.
- Cell Git blob: `7ff0c9ff12ed39df1a2c1c55d195e10048914644`.
- Cell SHA-256: `F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65`.
- Selector Git blob: `e8a1d72e23661576f14ac42b7dff6e3001837206`.
- Cost Git blob: `435705a50238aaeebe918430156bcc14df1ff794`.
- Parent evidence manifest SHA-256:
  `964E9996697698A0199F474F4AE8B9D728B8F86E3CA6C2F0F0DC7CFC3C1BB584`.
- Parent manifest/readback: 2,114 entries, 29,129,317 bytes, zero bad
  paths, PASS.

The persisted selector outcome is `NO_ADMISSIBLE_POLICY`, with zero admissible
comparisons and no root invocation for this cell.

## Persisted eight-candidate reproduction

All persisted fields, branch shadows, root status and rejection classes were
reproduced from the hash-bound receipt without calling the selector.

| # | regime | b branch | a branch | q_b | q_a | d | g_b | g_a | rejection |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 0 | negative | backward | backward | 0.0015039676061569449 | 8.895604077208148e-05 | -3.9829851584879403 | -17.72430600079171 | 1.8577376041602465 | A direction |
| 1 | negative | forward | backward | 0.008487587452625978 | 8.895604077208148e-05 | -4.21351237157745 | -0.2628305113325773 | 1.6272103910707365 | B and A direction |
| 2 | negative | backward | forward | 0.0015039676061569449 | -0.000536125311776913 | -5.951718831904533 | -18.01698424663303 | -0.11099606925634653 | A direction |
| 3 | negative | forward | forward | 0.008487587452625978 | -0.000536125311776913 | -4.56236434942103 | -0.2720201594800402 | 1.2783584132271564 | B direction |
| 4 | zero kink | backward | forward | 0.0015039676061569449 | -0.000536125311776913 | 0 | -19.634441284086584 | 5.840722762648187 | transfer KKT |
| 5 | zero kink | forward | forward | 0.008487587452625978 | -0.000536125311776913 | 0 | -2.1809914035117917 | 5.840722762648187 | B direction and transfer KKT |
| 6 | positive | backward | forward | 0.0015039676061569449 | -0.000536125311776913 | -6.899087252957164 | -18.44943327617183 | -1.0583644903089775 | transfer sign, A direction and KKT |
| 7 | positive | forward | forward | 0.008487587452625978 | -0.000536125311776913 | -5.509732770473661 | -0.42659829252214143 | 0.3309899921745254 | transfer sign, B direction and KKT |

For the backward liquid branch, the negative-transfer a-backward drift is
`1.8577376041602465` with bound `1.1059824302255312e-12`, while the a-forward
drift is `-0.11099606925634653` with bound `1.165177247639271e-12`. This is a
strict crossing. The forward liquid branch has positive a drift at both
endpoints and does not cross.

## D3 mapping and sign topology

The independent scalar reconstruction gives:

- `d_z=-effective_r_a*a=-5.840722762648187`;
- transfer regime: negative;
- `R=1-chi_0+chi_1*d_z/max(a,a_bar)=-0.3330414721146172`;
- original sorted illiquid derivative interval:
  `[-0.000536125311776913, 8.895604077208148e-05]`;
- unsorted mapped endpoint images:
  `[0.0016097854371494127, -0.000267101992455363]`;
- sorted mapped q_b interval:
  `[-0.000267101992455363, 0.0016097854371494127]`.

Both the original interval and its negative-R image straddle zero. The
intersection with the adopted `q_b>0` domain is
`(0, 0.0016097854371494127]`; it is nonempty. No clipping, epsilon, derivative
floor or altered tolerance was used.

## Branch-local domain and downstream audit

### Backward liquid branch

- `q_b=0.0015039676061569449`: finite, strictly positive, and inside both the
  full mapped interval and its positive-domain intersection.
- `q_a=R*q_b=-0.0005008835855672058`: inside the original closed illiquid
  derivative interval.
- `d=-5.840722762648187`: negative-transfer sign PASS.
- `raw g_a=0.0`; switching bound `1.15640352888927e-12`; canonical `g_a=0`.
- `g_b=-17.978717494437753`: backward direction PASS.
- D3 KKT target `-0.0005008835855672058`, residual `0.0`: PASS.
- Controls/value finite: PASS.
- D2 assembler admissibility: PASS.
- Hamiltonian: `-0.06734914681687235`.
- Admissible: true.

### Forward liquid branch

- `q_b=0.008487587452625978`: finite and positive, but outside the mapped
  interval and its positive-domain intersection.
- `q_a=-0.0028267186199241096`: outside the original derivative interval.
- `g_b=-0.5252676138629608`: inconsistent with the forward derivative branch.
- Although its algebraic D3 KKT residual is zero and its values are finite, it
  fails the branch-local domain and direction rules.
- Admissible: false.

Therefore the backward branch is the unique fully admissible switching
candidate.

## Earliest causal exit

Static inspection of the current `_interior_a_switching_candidate` path proves
that the following checks pass first:

1. interior-a status;
2. backward-liquid strict crossing;
3. negative regime matching `d_z`;
4. finite, nonzero negative ratio;
5. the negative-ratio active-liquid-face guard is inapplicable because b is
   interior.

The next check is:

`if implied_q_b_interval[0] <= 0.0: return None`

It triggers because the mapped lower endpoint is
`-0.000267101992455363`. This is the earliest causal exit. It tests whole
interval positivity before the existing path can apply branch-local `q_b>0`,
mapped-interval membership, q_a membership, direction, KKT, finite and D2
checks.

## Comparison with accepted Beijing F0364

The two cells share the same scientific authority: interior-b/interior-a
strict-crossing switching, finite negative R, `q_b>0`, q_a membership in the
original closed derivative interval, unchanged D3 KKT, direction, finite, D2
and Hamiltonian rules.

Beijing's illiquid interval was entirely negative, so its negative-R mapped
q_b interval was entirely positive:
`[0.004111019263931103, 0.006526149020033277]`.

安徽's original interval and mapped interval both straddle zero. The accepted
contract requires the selected branch-local q_b to be positive; it does not
require every point of the mapped interval to be positive. The Beijing
acceptance supplies the law, while the present arithmetic independently proves
that the 安徽 backward branch satisfies it.

## Design-only narrow consequence

Because classification A is proven, the narrow repair design is:

1. limit scope to interior-b/interior-a finite-negative-R strict crossings;
2. intersect the sorted mapped interval with the open positive domain `q_b>0`;
3. require the persisted branch-local liquid derivative to be strictly
   positive and a member of that intersection;
4. require `q_a=R*q_b` to remain in the original closed illiquid derivative
   interval;
5. pass the candidate through all unchanged direction, D3 KKT, finite, D2,
   deduplication and Hamiltonian checks.

Active liquid-face behavior remains unchanged, and ratio zero remains fail
closed. This task did not implement the design.

## Zero-science ledger

- Persisted cell loads: 1.
- Persisted candidate reproductions: 1.
- Deterministic scalar branch diagnostics: 2.
- Production selector calls: 0.
- Scalar/root calls: 0.
- Policy maps: 0.
- D2/Q calls: 0.
- HJB/direct solves: 0.
- KFE/SVD: 0.
- Aggregates and household batches: 0.
- Labor/K1B/C1/firm integration: 0.
- Turn5, MATLAB, K2, GE/Results: 0.
- Retry/tuning: 0.

## Evidence and checks

Evidence root:

`reports/ch5_mp4c_k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic_20260921_run001/`

- Manifest entries: 13.
- Manifest bytes: 23,826.
- Manifest SHA-256:
  `7A9DED5F12413F13E8CD827EE890A7D5BEF002EE5BC756A7476D10821B621E50`.
- Independent readback: PASS, zero bad paths.
- Focused tests: 6 passed.
- `py_compile`: PASS.
- Selector and cost pre/post hashes: exact, unchanged.
- Production source changes: 0.
- CURRENT changes: 0.
- Successor published: no.

This forensic does not authorize implementation, turn4 rerun, integration,
turn5 household, K2, GE or Results.
