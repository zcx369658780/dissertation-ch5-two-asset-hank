# CH5 MP4C 2018 KFE D1-D3 failed-cell algebraic attribution report

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ZERO_SCIENCE_20260916`

Role: bounded Builder forensic attribution; zero scientific execution

## Verdict

`ATTRIBUTED_STRUCTURAL_INCOMPATIBILITY_OF_FROZEN_DERIVATIVE_INPUTS`

Cells 4 and 8 fail because their historical inward upper-b derivatives are negative, while the frozen consumption and upper-face KKT laws require a strictly positive liquid shadow value. Cell 10 contains an interior-a derivative-direction fixed-point conflict in its active-upper-b negative-transfer case; its other branches fail upper-b primal feasibility or transfer sign/KKT conditions. No mathematically legal frozen-contract branch is omitted by the selector.

This is a local incompatibility between the persisted historical MATLAB-faithful derivative state and the adopted corrected D1-D3 target contract. It is not evidence that an economic policy, corrected-target HJB fixed point, steady state, KFE solution, or equilibrium does not exist.

## Git and provenance

- Fresh-start `origin/main`: `4eda840d71d2d22456744558196d76b301fc6130`
- Branch: `codex/ch5-mp4c-2018-kfe-d123-failed-cell-algebraic-attribution-20260916`
- Candidate SHA: assigned by the commit containing this report; the exact non-force-pushed SHA and remote readback are returned in the final handoff. A commit cannot embed its own SHA without changing that SHA.
- Exact changed path: `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_REPORT.md`

The accepted reexecution receipt records `git_head_before_first_real_selector_call=1ec6a0b6972db18edee18c2852caa589afc8a047`. Its frozen raw-byte hashes for `selector.py` and `run_panel.py` were independently reproduced from the still-clean reexecution worktree as `CBF52641963C1DB49F91F567F54F792D4454E1DEF5AD10A659F0DAA18F48AAA8` and `EC76EEA78314352475D60CE775D7600A010E73C3C5DD7EFAB9EBBEBF75DEDD5C`. The fresh-main checkout has different raw hashes because of checkout end-of-line representation, but `git diff --no-index --ignore-space-at-eol --ignore-cr-at-eol` reports no text difference for either file, and the reviewed scientific source has no Git diff from `1ec6a0b...` to `4eda840...`. Thus the receipt is bound to the execution-time raw bytes, while the current review uses text-identical source rather than falsely claiming current-checkout raw-byte identity.

## Exact files read

Authority and task:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
- `tasks/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ZERO_SCIENCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_TEN_CELL_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_CANONICALIZATION_AND_TEN_CELL_REEXECUTION_REPORT.md`
- `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
- `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`

Persisted evidence:

- `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/cell_04_M143_corner_399.json`
- `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/cell_08_M143_corner_799.json`
- `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/cell_10_MATLAB_step57_row379.json`
- `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/pre_execution_freeze.json`
- `reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916/execution_ledger.json`

Reviewed corrected-diagnostic source:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/cost.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/boundary.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/contracts.py`

## Frozen law used in the attribution

The consumption FOC requires

\[
q_b=c^{-\gamma}>0.
\]

At a finite-box face the frozen stationarity convention is

\[
q_x=p_x+t_x\lambda_x,\qquad \lambda_x\ge 0,
\]

with `t_x=-1` at an upper face. A boundary axis uses only its inward derivative: backward at an upper face and forward at a lower face. An inactive face has `lambda_x=0`; an active upper face therefore has `q_x=p_x-lambda_x<=p_x`. The transfer KKT uses `s(a)=max(a,a_bar)` and, here where `a>a_bar`,

\[
d=\frac{a}{\chi_1}\left(\frac{q_a}{q_b}-(1-\chi_0)\right)\quad(d<0),
\]

\[
d=\frac{a}{\chi_1}\left(\frac{q_a}{q_b}-(1+\chi_0)\right)\quad(d>0),
\]

and `q_a/q_b in [1-chi_0,1+chi_0]` at `d=0`. Directional consistency requires a backward derivative for negative asset drift and a forward derivative for positive asset drift. These conditions are applied without a derivative floor, cap, alternate cost, or tolerance change.

## Cells 4 and 8: algebraic exhaustion of upper-b possibilities

Both cells are `(upper_b, upper_a)` corners. The frozen upper-b derivative is therefore the inward/backward derivative. The positive historical forward derivative is an exterior-direction derivative and is not a legal alternative under the frozen state-constraint contract.

| Cell | index `(b,a,z)` | `p_b_backward` | `p_b_forward` | inactive upper-b | active upper-b |
|---|---|---:|---:|---|---|
| 4 / `M143_corner_399` | `(19,19,0)` | `-0.0013293412236023347` | `0.012279274991057089` | `q_b=p_b_backward<0` | `q_b=p_b_backward-lambda_b<=p_b_backward<0` |
| 8 / `M143_corner_799` | `(19,19,1)` | `-0.0007096211894771973` | `0.005399680244454879` | `q_b=p_b_backward<0` | `q_b=p_b_backward-lambda_b<=p_b_backward<0` |

Therefore no inactive or active upper-b candidate in either cell can satisfy `q_b>0`. This conclusion is independent of root search, numerical tolerance, upper-a status, and transfer regime.

For completeness, both cells have `a=10` and `R_a=0.081`, so upper-a equality forces `d=-R_a*a=-0.81`. Only the negative-transfer regime can match that equality; zero and positive are rejected by the frozen sign/kink law. The persisted comparison sets cover four face active sets times three transfer regimes:

| Active set | negative | zero-kink | positive |
|---|---|---|---|
| none | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` | same | same |
| `upper_a` | `q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR` | `ACTIVE_A_EQUALITY_NOT_ZERO_KINK` | `ACTIVE_A_EQUALITY_WRONG_TRANSFER_SIGN` |
| `upper_b` | `UPPER_B_ACTIVE_HAS_NO_Q_B_POSITIVE_MULTIPLIER_DOMAIN` | same | same |
| `upper_a+upper_b` | `UPPER_B_ACTIVE_HAS_NO_Q_B_POSITIVE_MULTIPLIER_DOMAIN` | `ACTIVE_A_EQUALITY_NOT_ZERO_KINK` | `ACTIVE_A_EQUALITY_WRONG_TRANSFER_SIGN` |

Each receipt records 12 regime attempts, zero root invocations, zero admissible candidates, and `NOT_RUN_NO_SELECTED_POLICY` for D2. Some upper-a-active candidates stop first on their transfer sign, but the upper-b inequality above independently rules out every one. The two recorded upper-b failure codes exhaust the frozen active and inactive possibilities; they do not hide a legal branch.

## Cell 10: complete frozen-contract branch accounting

Cell 10 is at upper-b and interior-a, with

- `a=9.473684210526315`, `R_a=0.08446761179431557`, and `R_a*a=0.8002194801566738`;
- `p_b_backward=0.019561551438254172>0`;
- `p_a_backward=0.00814619404677024`;
- `p_a_forward=-0.016278031249598923`.

The frozen contract requires consideration of eight combinations: upper-b slack/active crossed with negative-backward-a, negative-forward-a, zero-forward-a, and positive-forward-a. Zero uses forward-a because `g_a=R_a*a>0`; positive uses forward-a because `d>0` implies `g_a=R_a*a+d>0`. Negative must test both directions. The receipt explicitly stores seven candidates; active-negative-forward-a is eliminated before a counted root by a global direction inequality, as shown in row 6.

| # | upper-b | transfer / a derivative | Persisted or algebraic result | Decisive rejection |
|---:|---|---|---|---|
| 1 | slack | negative / backward | `d=-2.2905518322685587`, `g_a=-1.490332352111885`, `g_b=4.246227858746812` | backward-a is consistent, but `g_b>0` is outward at upper-b (`upper_b_PRIMAL_INFEASIBLE`, liquid-direction conflict) |
| 2 | slack | negative / forward | `d=-8.204893500794233`, `g_a=-7.404674020637559`, `g_b=3.0169167848740015` | outward upper-b and forward-a direction conflict |
| 3 | slack | zero / forward | `d=0`, `g_a=0.8002194801566738`, `g_b=2.7385419109821543`; required kink interval `[0.017605396294428755,0.02151770658207959]` is positive while `q_a<0` | outward upper-b plus transfer KKT failure |
| 4 | slack | positive / forward | recovered `d=-9.152261921846863`, `g_a=-8.35204244169019`, `g_b=2.1338328215572613` | outward upper-b, positive-transfer sign failure, forward-a direction failure, and transfer KKT failure |
| 5 | active | negative / backward | unique recorded equality root `q_b=0.011097998989333606`, `lambda_b=0.008463552448920567`, `d=-0.7862036261815912`, canonical `g_b=0`, but `g_a=0.014015853975082537` | backward-a direction conflict at the liquid-equality root |
| 6 | active | negative / forward | pre-screened, not emitted as a receipt candidate | for every `0<q_b<=p_b`, `g_a=R_a*a+(a/2)(p_a_forward/q_b-0.9)<a(R_a-0.45)<0`; forward-a can never be direction-consistent |
| 7 | active | zero / forward | root `q_b=0.012274257683565253`, `g_b=0`, `g_a=0.8002194801566738`; KKT requires `q_a` in `[0.011046831915208728,0.01350168345192178]`, but `q_a=-0.016278031249598923` | transfer KKT failure |
| 8 | active | positive / forward | root `q_b=0.015987108852681377`, but recovered `d=-10.033566211521293` and `g_a=-9.23334673136462` | positive-transfer sign failure, forward-a direction failure, and transfer KKT failure |

### Interior-a fixed-point conflict

For active-negative-backward-a, directional consistency requires

\[
g_a=R_a a+\frac{a}{2}\left(\frac{p_a^B}{q_b}-0.9\right)<0,
\]

or

\[
q_b>q_{switch}=\frac{p_a^B}{0.9-2R_a}=0.011142916892752.
\]

The upper-b equality instead has its recorded root at `0.011097998989333606<q_switch`, where `g_a=0.014015853975082537>0`. At the switch, a direct arithmetic evaluation gives `g_b=0.03640965111366>0`, not equality.

There is no unobserved second equality root in the direction-valid interval. In the negative regime,

\[
d(q)=\frac{a}{2}\left(\frac{p_a^B}{q}-0.9\right),\qquad d'(q)<0,
\]

and

\[
g_b'(q)=\frac{w l}{5q}+\frac{1}{2q^{3/2}}-\left(0.9+\frac{2d}{a}\right)d'(q).
\]

On `[q_switch,p_b]`, `0.9+2d/a` stays positive (its value at `p_b` is `0.416439057632193`), so every term in `g_b'(q)` is positive. Thus `g_b` is strictly increasing after the direction switch and cannot return to zero. The liquid equality and the backward-a direction region do not intersect: this is the requested interior-a derivative-direction fixed-point conflict.

## Selector enumeration completeness

No mathematically legal frozen-contract branch is missing.

- Cells 4/8 enumerate all four active sets and all three transfer regimes. The boundary contract admits only the inward/backward upper-b derivative. Active and slack upper-b are both algebraically impossible because `p_b_backward<0`.
- Cell 10 covers both upper-b active states and all three transfer regimes. Its four admissibility-relevant a-direction cases per upper-b state are fully accounted for above. The one case not emitted as a full receipt candidate, active-negative-forward-a, is correctly eliminated over the entire multiplier domain before a root call; it is not a legal omitted branch.
- Not persisting a separate candidate record for that pre-screened branch is an audit-visibility limitation, not an enumeration or scientific-law omission. This task does not authorize changing it.

Cell 10 combines several algebraic failure mechanisms—slack upper-b feasibility, active-negative direction fixed point, and zero/positive transfer KKT/sign failures—but there is no specific repairable selector omission. Therefore the task's `MIXED_FAILURE_CLASSES_WITH_SPECIFIC_REPAIRABLE_OMISSION` category does not apply.

## Historical-derivative interpretation boundary

The three `NO_ADMISSIBLE_POLICY` outcomes mean only that the frozen historical derivative arrays cannot support a candidate satisfying the adopted corrected D1-D3 KKT, direction, and closed-face laws at these cells. Those arrays were produced by the historical MATLAB-faithful path, not by a corrected-target HJB fixed point.

The evidence does not establish economic nonexistence, corrected-HJB nonexistence or convergence, KFE admissibility, a steady state, calibration validity, GE, annual results, shocks, IRFs, or Results authority. Repeating the same historical-derivative selector panel cannot change the Cells 4/8 sign contradiction or the Cell 10 fixed-point mismatch.

## Zero-call ledger

| Operation | Calls |
|---|---:|
| real selector evaluations | 0 |
| synthetic selector evaluations | 0 |
| scalar root invocations | 0 |
| HJB maps / iterations / direct solves | 0 |
| KFE solves | 0 |
| MATLAB | 0 |
| outer / firm / wage-return recalculation | 0 |
| GE / annual / shock / IRF / Results | 0 |

Only persisted JSON parsing, source/text review, Git identity checks, and independently written pure arithmetic were used. No scientific code, tests, calibration, grids, tolerances, or prior evidence were modified.

## Smallest next gate recommendation

Do not rerun the same historical-derivative selector panel. If Reviewer and Owner choose to proceed, the smallest scientifically meaningful next gate is a separately authorized **single corrected-target HJB policy-map/direct-step gate** that generates a derivative state consistent with the corrected D1-D3 target and defines its own exact inputs, solve budget, fail-closed conditions, and evidence contract.

This report recommends but does not authorize that gate. No successor task was published, and no merge to `main` is authorized by this result.
