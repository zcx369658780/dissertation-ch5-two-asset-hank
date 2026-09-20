# CH5 MP4C turn-2 Beijing F0364 negative-ratio interior-a switching forensic

Date: 2026-09-21

## Result

Terminal marker:

`PASS__TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE`

Classification:

`TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED`

This is classification A.  The persisted ordinary candidates prove a strict
interior-a drift crossing for the backward liquid derivative.  A sign-aware
mapping of the negative illiquid-derivative interval through the negative D3
ratio produces a positive liquid-shadow interval.  Exactly one persisted liquid
derivative, p_b backward, lies in that interval and passes every existing
downstream direction, D3 KKT, transfer-sign, interval, finite-value and arithmetic
zero-drift check.

No selector source was changed.  No selector, root, policy map, D2/Q, HJB, KFE,
aggregate, integration or turn-3 call was made.

## Authority and provenance

- actual live-main baseline: `fddaef785bca01373492576047d574f07761d084`
- parent evidence manifest:
  `A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`
- parent manifest readback: 430 entries, 6,449,626 bytes, zero bad paths
- exact cell Git blob: `5e6528e07998cb6fe3b571cb21c778f3acf3775a`
- exact cell SHA-256:
  `F63B2D685F02D74ED3ED560F5DBD02FE5D7FF2B80ABF6D4F64414FFE1FCC7632`
- selector Git blob: `2c674b96fa7b665dab84f0ff3d98fbc5b8b16e22`
- cost Git blob: `435705a50238aaeebe918430156bcc14df1ff794`

The cell binds to checkpoint 5, flat 364, index `(4,18,0)`, id
`v005_f0364_b004_a018_z000`, and persisted outcome
`NO_ADMISSIBLE_POLICY`.

The hash-bound JSON stores `effective_r_b=0.09000000000000001`; the task text
displays the same model input as `0.09`.  Both representations are recorded.
This scalar does not enter the `d_z` or D3-ratio calculation.

## Persisted eight-candidate reproduction

All eight ordinary candidates were loaded from the exact cell receipt.  All are
inadmissible, use no root, and reproduce the persisted rejection classes.

| ordinal | regime | b branch | a branch | g_b | g_a | rejection reasons |
|---:|---|---|---|---:|---:|---|
| 0 | negative | backward | backward | -3.4923514437101817 | 1.1624821053092704 | A direction inconsistent |
| 1 | negative | forward | backward | -0.9794484517666966 | 1.7784160012824266 | B and A direction inconsistent |
| 2 | negative | backward | forward | -4.4264320230255665 | -0.25497146700720563 | A direction inconsistent |
| 3 | negative | forward | forward | -1.497497368127659 | 0.7228095000823842 | B direction inconsistent |
| 4 | zero kink | backward | forward | -4.796279598753063 | 7.8384208979658965 | transfer KKT residual |
| 5 | zero kink | forward | forward | -2.5570665942889015 | 7.8384208979658965 | B direction and transfer KKT |
| 6 | positive | backward | forward | -5.287215759178082 | -1.2023398880598375 | transfer sign, A direction and KKT |
| 7 | positive | forward | forward | -2.1627249108622575 | -0.22455892097024766 | transfer sign, B/A direction and KKT |

## Strict-crossing proof

For negative transfer and `p_b_backward=0.006091715618507631`:

- a-backward: `g_a=1.1624821053092704`, arithmetic bound
  `6.424189292563988e-13`;
- a-forward: `g_a=-0.25497146700720563`, arithmetic bound
  `7.23403821378802e-13`.

Therefore the pair satisfies

`g_a_backward > bound_backward`

and

`g_a_forward < -bound_forward`.

For `p_b_forward=0.008179870108012337`, the two drifts are
`1.7784160012824266` and `0.7228095000823842`.  Both are positive, so this
liquid branch has no strict a-drift crossing.

## D3 ratio and sign-aware interval

The frozen equations give:

- `d_z=-effective_r_a*a=-7.8384208979658965`;
- transfer regime: negative;
- `R=1-chi_0+chi_1*d_z/max(a,a_bar)=-0.7547777451261338`;
- sorted p_a interval:
  `[-0.004925792041697845,-0.0031029058502000167]`.

Dividing both p_a endpoints by the negative ratio and sorting the results gives:

`q_b in [0.004111019263931103,0.006526149020033277]`.

Thus `p_b_backward` is inside this positive interval and `p_b_forward` is
outside it.  The current selector stops earlier at
`ratio <= 0 -> return None`, so it never reaches this sign-aware image.

## Backward-liquid diagnostic candidate

- q_b: `0.006091715618507631`
- q_a: `-0.0045978913784868415`
- q_a inside original p_a interval: yes
- d: `-7.8384208979658965`
- c: `12.812391173518428`
- l: `0.6039121294085991`
- cost: `7.269264319239375`
- raw/canonical g_b: `-4.227123020026542`
- raw/canonical g_a: `0.0`
- switching arithmetic bound: `6.983597944658697e-13`
- b-direction: PASS for backward derivative
- transfer sign: PASS
- transfer KKT: PASS, residual `0.0`
- finite-value check: PASS
- utility: `-0.08613465266685111`
- raw Hamiltonian: `-0.11188508398929994`
- Hamiltonian: `-0.11188508398929994`
- rejection reasons: none
- admissible: true

No liquid root is needed because F0364 is interior in b and q_b is the persisted
backward liquid derivative shadow.

## Forward-liquid diagnostic candidate

- q_b: `0.008179870108012337`
- q_a: `-0.0061739839155502164`
- q_a inside original p_a interval: no
- q_b inside sign-aware mapped interval: no
- d: `-7.8384208979658965`
- c: `11.056732338640717`
- l: `0.6405825584663372`
- cost: `7.269264319239375`
- raw/canonical g_b: `-1.9879100155623801`
- raw/canonical g_a: `0.0`
- switching arithmetic bound: `6.140637648264874e-13`
- b-direction: FAIL for forward derivative because g_b is negative
- transfer sign: PASS
- transfer KKT: PASS, residual `8.673617379884035e-19`
- finite-value check: PASS
- utility: `-0.10195857472763234`
- raw Hamiltonian: `-0.1182194204413494`
- Hamiltonian: `-0.1182194204413494`
- rejection reasons: shadow outside derivative interval; B direction inconsistent
- admissible: false

## Scientific-authority audit

The Owner-adopted interior-a switching contract explicitly requires:

- `q_b>0`;
- unchanged D3 KKT
  `0 in q_a-q_b(1+partial_d C)`;
- q_a membership in the closed sorted interval between the two one-sided
  illiquid derivatives.

The cost implementation likewise requires q_b to be positive and does not impose
q_a positivity.  The designated accepted authority contains no independent
requirement that q_a, the D3 ratio, or the interior-a switching ratio be positive.
This conclusion is tied to the positively stated Owner contract and is not based
on absence alone.  The `ratio<=0` condition is present in selector.py as an
implementation guard.

Consequently the unique backward-liquid diagnostic candidate satisfies the
Owner-adopted domain and downstream laws, supporting classification A.

## Zero-root ledger and evidence

- F0364 cell loads: 1
- persisted candidate reproductions: 1
- deterministic scalar diagnostics: 2
- full selector calls: 0
- scalar roots: 0
- interior-a switching roots: 0
- policy maps: 0
- D2/Q assemblies: 0
- HJB solves/updates: 0
- KFE/SVD: 0
- aggregate/integration: 0
- scientific retries: 0
- turn-3 household calls: 0

Evidence root:

`reports/ch5_mp4c_turn2_beijing_f0364_negative_ratio_switching_forensic_20260920_run001/`

Sealed manifest SHA-256:

`6FF469F423A7D5D321A59E1DC4031B04E967E3EE4A03E58865824D8B5D8CE1D0`

The manifest contains 11 entries and 21,408 bytes.  Independent readback passed
with zero bad paths.  Pre/post code-freeze hashes match, including unchanged
selector.py and cost.py.

CURRENT files were not modified.  Main was not merged and no successor was
published.
