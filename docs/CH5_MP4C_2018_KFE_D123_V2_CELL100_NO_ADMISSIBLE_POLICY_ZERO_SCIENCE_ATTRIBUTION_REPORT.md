# CH5 MP4C 2018 KFE D1-D3 V2 cell100 zero-science attribution

Date: 2026-09-17

Task: `CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_20260917`

## Terminal classification

`ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`

The frozen selector does not completely represent the authority-backed cases at
the lower-liquid-boundary cell.  For active `lower_b` and negative transfer it
uses a pre-root derivative screen over the upper-face multiplier domain
`0 < q_b <= p_b`.  The lower-face KKT domain is instead `q_b >= p_b`.  This
screen retains only the forward-`a` derivative and omits the negative-transfer /
backward-`a` case from the persisted comparison set.

This is an enumeration/domain omission, not a `ROOT_FAILURE_NO_UNIQUE_BRACKET`
implementation omission.  Static algebra also shows that the omitted case would
not yield an admissible policy for the frozen V2 inputs: its liquid-equality root
lies, if represented, on the wrong side of the `a`-direction switch.  That
outcome-equivalence does not make the selector complete, because the actual
pre-screen excludes the case using the wrong face domain and does not establish
the required lower-face rejection.

No repair or scientific reexecution was performed.

## Startup and frozen identity

- fresh-fetched live `origin/main` baseline:
  `affee50a517f8ab688498378e9c7d4a4edafa311`;
- isolated task branch:
  `codex/ch5-mp4c-2018-kfe-d123-v2-cell100-no-admissible-policy-zero-science-attribution-20260917`;
- startup worktree: clean and `0/0` ahead/behind live `origin/main`;
- accepted V2 field SHA-256:
  `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`;
- V2 identity is repeated by the sealed checkpoint-1 direct-solve receipt and
  the checkpoint-2 derivative receipt;
- sealed continuation-manifest SHA-256:
  `FC323B9691E28F20305CF5F71DD379C445CB80A506313A67DBC1954E88A5E041`;
- exact cell-100 receipt SHA-256:
  `DA58AFDD72B836023133DAF8BF9E1F76C269BA79C4677C7D1A345BAF914F085E`,
  matching its sealed-manifest entry;
- frozen selector SHA-256:
  `C60C584A44A143CB584563ACDAA8F7E30EBC1CA45B90F8AF39728D40AC70E5E6`;
- frozen selector Git blob:
  `5008e16e37dc38d9ba1cbc44394286a1b9264915`.

The frozen cell is flat F index `100`, zero-based `(i_b,i_a,i_z)=(0,5,0)`,
physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`.  Its persisted inputs are:

| Quantity | Value |
|---|---:|
| `p_b^B = p_b^F` | `0.012333311206716577` |
| `p_a^B` | `0.00903315440190679` |
| `p_a^F` | `0.008957007194295222` |
| `R_a` | `0.08999994552589044` |
| `R_a*a` | `0.236841961910238` |
| net wage | `12.783312529860462` |
| `R_b*b + transfer_income` | `-0.08` |
| `chi_0, chi_1` | `0.1, 2.0` |
| `gamma_c, phi` | `2.0, 5.0` |

The persisted selector result is `NO_ADMISSIBLE_POLICY`, with seven candidates,
three scalar-root invocations, zero interior-Z roots and zero admissible
comparisons.

## Frozen lower-b and transfer law

At `b=b_lower`, the boundary axis uses the inward `forward` derivative.  The
lower-face KKT law is

`g_b >= 0`, `lambda_b = q_b-p_b >= 0`, and `lambda_b*g_b = 0`.

Thus a slack lower-b case has `q_b=p_b`; an active lower-b case has `g_b=0`
and must search the multiplier domain `q_b>=p_b`.  There is no second liquid
derivative branch at a boundary node.

The illiquid axis is interior.  With `R_a*a>0`, the frozen enumeration requires:

- negative transfer: both backward-`a` and forward-`a` derivative cases;
- zero kink: forward-`a` only;
- positive transfer: forward-`a` only.

For inactive `a`, `q_a=p_a` and

`d(q_b)=a/2*(q_a/q_b-0.9)` in the negative regime,

`d=0` at the kink, and

`d(q_b)=a/2*(q_a/q_b-1.1)` in the positive regime.

All candidates must additionally satisfy derivative direction, transfer sign,
the D3 KKT relation `0 in q_a-q_b*(1+partial_d C)`, and finite arithmetic.

The Owner-adopted liquid `Z` branch is not legal here.  It applies only at an
interior liquid node after backward/forward liquid drifts form a strict crossing.
The frozen implementation exits the Z constructor whenever a `b` face exists,
and the cell receipt correctly records zero interior-Z invocations.

## Complete authority-case census versus actual receipt

The authority-backed census has eight cases: lower-b slack/active crossed with
negative-backward-`a`, negative-forward-`a`, zero-forward-`a`, and
positive-forward-`a`.  Seven appear in the receipt.

| # | lower-b status | transfer / `a` derivative | Persisted values and exact rejection |
|---:|---|---|---|
| 1 | slack | negative / backward | `d=-0.2205010020056987`, `g_b=-0.06991332232882219`, `g_a=0.01634095990453932`; lower-b primal infeasible, forward-`b` direction inconsistent, and backward-`a` direction inconsistent. Transfer KKT residual is `0`. |
| 2 | slack | negative / forward | `d=-0.22862482962558264`, `g_b=-0.06398835338853426`, `g_a=0.00821713228465537`; lower-b primal infeasible and forward-`b` direction inconsistent. Transfer and `a` direction pass. |
| 3 | slack | zero / forward | `g_b=-0.2498883612174545`, `g_a=0.236841961910238`; lower-b primal infeasible and forward-`b` direction inconsistent. `q_a=0.008957007194295222` lies below the kink target `[0.01109998008604492,0.013566642327388237]`, giving KKT residual `0.0021429728917496983`. |
| 4 | slack | positive / forward | recovered `d=-0.4917827243624249`, contradicting positive transfer; `g_a=-0.2549407624521869` contradicts forward-`a`; `q_a=0.008957007194295222` exceeds the point target `0.006490344952951905`, giving KKT residual `0.0024666622413433165`. `g_b=0.10081299647582295` itself is lower-face feasible. |
| 5 | active | negative / forward | root `q_b=0.012447419227151839`, `lambda_b=0.00011410802043526104`, canonical `g_b=0`, KKT residual `0`; but `g_a=-0.0005429159000894801` contradicts forward-`a`. |
| 6 | active | zero / forward | root `q_b=0.012837941893151112`, `lambda_b=0.0005046306864345349`, canonical `g_b=0`, `g_a=0.236841961910238`; `q_a=0.008957007194295222` is below `[0.011554147703836,0.014121736082466224]`, giving KKT residual `0.002597140509540779`. |
| 7 | active | positive / forward | persisted `ROOT_FAILURE_NO_UNIQUE_BRACKET`; the no-root audit below proves the liquid equation has no root on the legal lower-face domain, and positive transfer is independently impossible there. |
| 8 | active | negative / backward | **not emitted**.  The selector's pre-screen uses `0<q_b<=p_b`, retains only forward-`a`, and invokes one root for row 5.  The correct lower-face domain is `q_b>=p_b`. |

The receipt's `face_active_set_count=2` and `regime_attempt_count=6` therefore do
not prove derivative-case completeness.  The comparison set has seven rows
rather than the eight required by the frozen interior-`a` branch law.

## The omitted active-negative/backward case

For the omitted case,

`d_B(q)=a/2*(p_a^B/q-0.9)` and
`g_a(q)=R_a*a+d_B(q)`.

Backward-`a` direction becomes valid only above

`q_switch^B = p_a^B/(0.9-2*R_a) = 0.012546045881996438`.

This is inside the legal lower-b multiplier domain because
`q_switch^B-p_b=0.0002127346752798607>0`.  Consequently the source's screen on
`0<q<=p_b` cannot legally eliminate the branch: it does not inspect the portion
of the lower-face domain where backward-`a` is direction-consistent.

The frozen inputs nevertheless imply that this omitted case would be rejected:

- at `q=p_b`, the persisted same-form slack arithmetic has
  `g_b=-0.06991332232882219` while `g_a>0`;
- at `q=q_switch^B`, direct substitution gives
  `g_a=-8.326672684688674e-17` and
  `g_b=0.048890867998732046`;
- for `q>=q_switch^B`, `d_B'(q)<0` and
  `1+C'(d_B)=0.9+2*d_B/a=p_a^B/q>0`.  Consumption and labor contributions to
  `g_b'(q)` are positive, and `-(1+C'(d_B))*d_B'(q)>0`, so `g_b` is strictly
  increasing throughout the backward-direction-valid interval.

Hence any liquid-equality crossing lies between `p_b` and `q_switch^B`, where
`g_a>0` and backward-`a` is invalid; no crossing exists after the direction
switch.  This proves local outcome-equivalence, but it was not the domain used
by the selector's pre-root elimination.

## `ROOT_FAILURE_NO_UNIQUE_BRACKET` audit

The only persisted root failure at cell 100 is active lower-b / positive
transfer / forward-`a`.  Its frozen liquid equation is

`g_b(q)=w*(q*w)^(1/5)-0.08-q^(-1/2)-d(q)-C(d(q),a)=0`,

with

`d(q)=a/2*(p_a^F/q-1.1)` and legal lower-face domain `q>=p_b`.

Positive transfer requires

`q < p_a^F/1.1 = 0.008142733812995656`,

which is disjoint from `q>=p_b=0.012333311206716577`.  Thus no root could be a
legal positive-transfer candidate.

The raw liquid equation also has no root on the screened lower-face domain.  At
the lower endpoint its persisted value is
`g_b(p_b)=0.10081299647582295>0`.  Let `y=1.1-p_a^F/q`.  Because `d<0`, the
transfer contribution `-d-C(d,a)` is
`a*(0.45*y-0.25*y^2)`.  From `p_b` until
`q=p_a^F/0.2=0.04478503597147611`, both the consumption/labor net term and this
transfer contribution increase; at that point the direct frozen arithmetic is
`g_b=7.161562370826097`.  Thereafter the consumption/labor net term continues
to increase, while the transfer contribution can fall by at most
`a*0.01=0.026315789473684213`.  Therefore `g_b(q)>0` for every `q>=p_b`.

The root routine's status string conflates zero and multiple brackets when it
does not see exactly one bracket, and the receipt does not persist its 513 raw
samples.  The algebra above disambiguates this cell: it is a genuine no-root
case, not a missed bracket or authorized-root implementation omission.

## Static comparisons

The accepted V1 receipt at the same coordinate had different derivatives:
`p_b=0.015465106344126105`, `p_a^B=0.005139642044264378`, and
`p_a^F=0.0051179172410759765`.  It selected the slack negative/backward policy
with `d=-0.7469237240225457`, `g_b=1.5826140870178937`, and
`g_a=-0.5100817621123077`.  Its active-negative/backward row was emitted before
returning a root failure.  This confirms that the V2 omission is caused by the
derivative-sensitive pre-screen, not by a general absence of the branch label.

The persisted V2 spatial neighbor `(0,4,0)` at flat `80` selected active
lower-b / negative / forward-`a` with root
`q_b=0.012526603697256871` and `g_a=0.0011764062980116896`.  It has the same
seven-row receipt shape.  Neighbor success does not validate the missing
backward case at cell 100 or repair the lower-face screen domain.

## Minimal obstruction and boundary of the finding

The frozen cell inputs exhibit real local KKT/direction conflicts in all seven
persisted rows, and the omitted eighth row is also algebraically incompatible.
However, the task requires proof that every authority-backed branch is covered.
That proof fails at the implementation boundary: the active lower-b negative
case is reduced with an upper-b-only multiplier-domain screen.  The minimal
forensic defect is therefore the selector's omitted lower-b
negative/backward-`a` representation, which controls the terminal
classification above.

This report does not authorize a repair, rerun, tolerance change, alternative
root procedure or scientific successor.  It does not establish nonlinear HJB
convergence or nonexistence, P2/u2/Q2, terminal KFE, GE, production replacement
or Results eligibility.  Results eligibility remains `FALSE`.

## Zero-science ledger

| Operation | Calls |
|---|---:|
| selector evaluations | 0 |
| scalar roots | 0 |
| interior-Z roots | 0 |
| policy maps | 0 |
| D2 assemblies | 0 |
| HJB solves/updates | 0 |
| graph/SCC | 0 |
| KFE/SVD/eigen/nullspace/`Q.T@p` | 0 |
| MATLAB | 0 |
| outer/firm/wage-return/GE/annual/shock/IRF/Results | 0 |
| scientific retries | 0 |

Only static source/evidence reads, SHA-256/Git-blob checks, JSON parsing and
closed-form algebraic substitutions were used.  No test importing or executing
the selector was run.
