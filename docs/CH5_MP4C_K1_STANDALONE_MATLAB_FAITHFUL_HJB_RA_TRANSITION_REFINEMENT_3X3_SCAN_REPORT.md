# CH5 MP4C K1 standalone MATLAB-faithful HJB `ra` transition refinement 3×3 scan report

Date: 2026-09-13

Task ID: `CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN`

## Outcome

`ALL_HJB_LEGAL_CONVERGED__INTERIOR_ONLY_AT_RA_0P065_HIGHER_WAGES__WAGE_DEPENDENT_TRANSITION__RA_0P08_UPPER_BOUNDARY`

All nine preregistered HJB points were legal and converged. Two points, both at `ra=.065` and wages `1.05` or `1.3`, are descriptive interior-distribution candidates. The `ra=.065,w=.8` shape is transitional; `ra=.0725` changes from upper-bound pile-up at `w=.8` to ambiguous at the two higher wages; all three `ra=.08` points pile up at `amax`. Thus the transition depends materially on wage. No `ra` value is interior at all three wages, so this grid does not establish a wage-robust nondegenerate connected interior `ra` band.

Results eligibility=`FALSE`.

## Git and authority receipt

- Fresh fetched baseline: `origin/main=c58a64b65ce948f8ddc47dfe8c4fd3a3dc060921`.
- Branch: `codex/ch5-mp4c-k1-hjb-ra-transition-3x3-20260913`.
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-transition-3x3-20260913-001`.
- Exact grid only: `rb=.02`, `ra={.065,.0725,.08}`, `w={.8,1.05,1.3}`; Cartesian product, nine points.
- Oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8` (matched expected).
- Designated MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` (matched expected; MATLAB runtime was not invoked).

The input-invariance receipt records nine distinct fresh initial-value arrays and nine distinct fresh baseline-labor arrays. Only `inputs.r_a` and `inputs.wages[0]` vary; `unexpected_varying_fields=[]` and `all_non_scanned_fields_identical=true`. The accepted grid, parameters, transfer/tax construction, borrowing-rate gap, HJB/KFE numerics, derivative floor, FOC, selector, boundary laws, direct solve, convergence rule, and contaminated-row KFE remained unchanged. There was no warm start, damping, price guard, or extra point.

## Call ledger

| Item | Actual / budget |
|---|---:|
| fresh initialization constructions | 9 |
| HJB started / completed | 9 / 9 |
| KFE started / completed | 9 / 9 |
| scalar labor roots | 7200 |
| scientific retries | 0 |
| engineering retries | 0 |
| global multi-province outer turns | 0 |
| firm / MATLAB / K1B / K2 / GE | 0 / 0 / 0 / 0 / 0 |
| annual downstream / shock / IRF / Results writes | 0 / 0 / 0 / 0 |

KFE ran exactly once after each converged HJB; no point was retried.

## 3×3 classification

Every cell has HJB class `HJB_CONVERGED`; the second line is the descriptive illiquid-distribution label.

| `ra` \ `w` | `.8` | `1.05` | `1.3` |
|---|---|---|---|
| `.065` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` | `INTERIOR_A_DISTRIBUTION_CANDIDATE` | `INTERIOR_A_DISTRIBUTION_CANDIDATE` |
| `.0725` | `UPPER_A_BOUNDARY_PILEUP` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` |
| `.08` | `UPPER_A_BOUNDARY_PILEUP` | `UPPER_A_BOUNDARY_PILEUP` | `UPPER_A_BOUNDARY_PILEUP` |

Counts: HJB converged `9`, HJB nonconverged `0`, hard-error/invalid-transition-matrix `0`; interior `2`, ambiguous `3`, upper-bound pile-up `4`, lower-bound dominated `0`.

Labels use only exact modal location and top-two-bin endpoint-versus-interior ordering; no post-result numeric cutoff was fitted. An `amax` mode is upper-bound pile-up; a unique `amin` mode exceeding all interior mass is lower-bound dominated; an interior mode with both top bins interior is an interior candidate; other mixed shapes are ambiguous. Full raw marginals remain published.

## Per-point HJB and KFE evidence

All points used `rb=.02`; `amin=0`, `amax=10`. `bmin_mass` is zero or signed machine-scale (`-1.83e-18` at point 1, `-2.32e-21` at point 2, `7.14e-16` at point 3, `-7.08e-63` at point 5, `1.71e-45` at point 6); `bmax_mass=0` at every point. Total mass is `0.9999999999999998` to `1.0000000000000002`. `first_illegal_iteration` is null throughout.

| `ra,w` | HJB: iter; final statistic; max `A2max` | `Ct,Lt,At,Bt` | `amin;amax;interior-a;amax/adjacent` | modal `a`; modal `b` | top three `a:mass` | `Bt_pos;Bt_neg`; density min/count; KFE residual | label |
|---|---|---|---|---|---|---|---|---|
| `.065,.8` | 9; `3.71731e-9`; `4.71845e-15` | `1.248261; .881066; 8.996226; .947333` | `0; .229586; .770414; .937936` | `9.473684`; `.210526` | `9.473684:.244778`, `10:.229586`, `8.947368:.190778` | `.971183;-.023850`; `-3.80616e-17/145`; `3.46945e-18` | ambiguous |
| `.065,1.05` | 9; `9.42561e-9`; `3.83027e-15` | `1.452025; .878880; 8.959369; .814948` | `0; .199534; .800466; .810415` | `9.473684`; `.210526` | `9.473684:.246212`, `8.947368:.207089`, `10:.199534` | `.850610;-.035661`; `-1.74324e-17/74`; `1.56125e-17` | interior |
| `.065,1.3` | 9; `2.16712e-8`; `5.32907e-15` | `1.648583; .873877; 8.897973; .730031` | `0; .180616; .819384; .785570` | `9.473684`; `-.157895` | `9.473684:.229917`, `8.947368:.216443`, `10:.180616` | `.780931;-.050900`; `-1.40873e-17/30`; `4.33681e-18` | interior |
| `.0725,.8` | 9; `3.18686e-9`; `4.71845e-15` | `1.275759; .857608; 8.912718; 1.273164` | `0; .225952; .774048; 1.035704` | `10`; `.210526` | `10:.225952`, `9.473684:.218163`, `8.947368:.181003` | `1.298152;-.024988`; `0/0`; `1.40946e-18` | upper |
| `.0725,1.05` | 9; `9.42413e-9`; `3.83027e-15` | `1.480237; .854552; 8.943983; 1.103001` | `0; .221146; .778854; .972269` | `9.473684`; `-.157895` | `9.473684:.227453`, `10:.221146`, `8.947368:.201771` | `1.138753;-.035751`; `-9.54446e-18/119`; `4.63496e-18` | ambiguous |
| `.0725,1.3` | 9; `2.16690e-8`; `7.10543e-15` | `1.676123; .849877; 8.944664; .977588` | `0; .211991; .788009; .918694` | `9.473684`; `-.157895` | `9.473684:.230753`, `10:.211991`, `8.947368:.207585` | `1.028299;-.050711`; `-6.50227e-17/63`; `6.07153e-18` | ambiguous |
| `.08,.8` | 9; `3.17989e-9`; `3.55271e-15` | `1.299273; .839697; 8.816799; 1.554636` | `0; .213591; .786409; 1.120986` | `10`; `.210526` | `10:.213591`, `9.473684:.190538`, `8.947368:.162573` | `1.577251;-.022615`; `-3.00854e-17/9`; `4.98733e-18` | upper |
| `.08,1.05` | 9; `9.42214e-9`; `3.55271e-15` | `1.504613; .835740; 8.870514; 1.369091` | `0; .227207; .772793; 1.124191` | `10`; `-.157895` | `10:.227207`, `9.473684:.202107`, `8.947368:.164490` | `1.405196;-.036105`; `-8.32998e-20/30`; `4.82470e-18` | upper |
| `.08,1.3` | 9; `2.16660e-8`; `4.27436e-15` | `1.700167; .830533; 8.907904; 1.216980` | `0; .232910; .767090; 1.101533` | `10`; `-.157895` | `10:.232910`, `9.473684:.211441`, `8.947368:.169299` | `1.269724;-.052744`; `0/0`; `4.98733e-18` | upper |

All shapes and aggregate arrays were finite and had expected dimensions. Negative density entries are signed roundoff-scale receipts rather than clipped mass; complete 20-bin `a` and `b` marginals, point receipts, shapes, and label domains are in compact evidence.

## Interpretation and interior candidates

The refinement identifies a narrow wage-dependent transition rather than a provisional wage-robust health band. At `ra=.065`, higher wages produce the only two interior candidates while the low-wage point remains mixed because `amax` is its second-largest bin. At `ra=.0725`, the low-wage point has already moved onto `amax`, whereas higher wages remain mixed with `amax` second. At `ra=.08`, `amax` is modal at all wages. Hence wage materially shifts the lower-to-upper-bound transition within `.8–1.3`.

There is no connected coarse interior candidate band valid across all three wages. For the two observed interior candidate points only, aggregate ranges are:

- `Ct=[1.4520245248118848,1.648582665766757]`;
- `Lt=[.873876860999354,.8788801526224764]`;
- `At=[8.89797303470002,8.959369004297567]`;
- `Bt=[.7300311913729753,.8149483194036385]`.

These ranges describe the two candidates; they are not a wage-robust band and confer no production or Results authority.

## Evidence and sole next gate

- Compact evidence: `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_transition_refinement_3x3/`.
- Compact sealed-manifest SHA-256: `D212336DF265B961CF78695B92B23CCFA298D8787FE0D8DE0D7D0419F7650322`.
- External no-overwrite evidence: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-transition-refinement-3x3-evidence-20260913-001`.
- External sealed-manifest SHA-256: `466A0DFB7E31082173AA7E95C0F1C5217F4FD29045F4E1F722566BD8395D1D5E`.

Exactly one recommended next gate, not executed and not published as a successor task: `OWNER_REVIEW_NARROWER_RA_REFINEMENT_AROUND_WAGE_DEPENDENT_FRONTIER`, with candidate grid `rb=.02`, `ra={.06,.0675,.07}`, `w={.8,1.05,1.3}`. It brackets both the accepted `.055→.065` lower/interior transition and the `.065→.0725` wage-dependent upper frontier.

This standalone KFE evidence does not solve the corrected-2018 multi-province KFE blocker. Finite-box upper-`b` leakage and MATLAB-style pinning remain unresolved. No global model, firm block, GE, downstream annual run, shock, IRF, or Results claim is authorized.

Stop gate: independent ChatGPT Reviewer ACCEPT/REJECT of the candidate commit.
