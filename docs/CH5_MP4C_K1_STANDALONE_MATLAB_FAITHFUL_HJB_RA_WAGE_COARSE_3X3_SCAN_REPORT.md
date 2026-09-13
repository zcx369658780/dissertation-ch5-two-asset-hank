# CH5 MP4C K1 standalone MATLAB-faithful HJB `ra × wage` coarse 3×3 scan report

Date: 2026-09-13

## Outcome

`ALL_HJB_CONVERGED__LOW_AND_MID_RA_LOWER_BOUND_AMBIGUOUS__HIGH_RA_UPPER_A_BOUNDARY_PILEUP`

All nine preregistered standalone HJB points converged under the unchanged accepted MATLAB-faithful algorithm. No iteration violated the designated MATLAB legality test `A2max=max(abs(sum(A,2))) <= homecrit=.01`; the largest observed value was `0.007712953842301029` at `(ra,w)=(.09,1.3)`. All nine therefore proceeded once to the accepted contaminated-row standalone KFE.

The KFE evidence does not identify a GOOD coarse point. At `ra=.02` and `.055`, essentially all probability is at the structural lower illiquid-asset bound `a=0`; because this is a genuine state constraint rather than an artificial upper truncation, and because several contaminated-row receipts also contain small signed numerical mass or material raw-system residual, these six points are conservatively `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED`. At `ra=.09`, `a=10` is the mode and carries `18.71%–20.94%` of mass, exceeding the adjacent bin; these three points are `BOUNDARY_CONVERGED_CANDIDATE`.

Results eligibility=`FALSE`.

## Authority, baseline, and frozen inputs

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh-fetched baseline: `45f0e3aedeb88e0dc9ca5e35e1e79664cedf2909`.
- Builder branch: `codex/ch5-mp4c-k1-hjb-ra-wage-3x3-20260913`.
- Isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-3x3-20260913-001`.
- Accepted standalone oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`.
- Protected MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.
- Exact Cartesian grid: `rb=.02`; `ra={.02,.055,.09}`; household wage `w={.8,1.05,1.3}`.
- Grid: `b=linspace(-2,5,20)`, `a=linspace(0,10,20)`, `z=[.8,1.3]`, `Q=[[-1/3,1/3],[1/3,-1/3]]`.
- Other fixed inputs: `tau=.05`, `Tt=.1`, borrowing gap `.07`, `rho=.05`, `gamma=2`, `phi=5`, `chi0=.1`, `chi1=2`, `a_bar=1e-6`, zero diffusion parameters/migration cost, labor weight `1`.
- Numerics: `Delta=1000`, convergence tolerance `1e-7`, maximum iterations `100`, drift tolerance `1e-12`, MATLAB legality `homecrit=.01`.

The input receipt contains all nine configurations and proves that only `inputs.r_a` and `inputs.wages[0]` vary. Nine distinct `V0` objects and nine distinct baseline-labor objects were constructed by the accepted `_source_initial_arrays` route before HJB entry; no warm start was used.

## 3×3 classification matrix

Rows are `ra`; columns are household wage. `HC` means `HJB_CONVERGED`, `QA` means `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED`, and `BC` means `BOUNDARY_CONVERGED_CANDIDATE`.

| `ra \ w` | `.8` | `1.05` | `1.3` |
| --- | --- | --- | --- |
| `.02` | HC / QA | HC / QA | HC / QA |
| `.055` | HC / QA | HC / QA | HC / QA |
| `.09` | HC / BC | HC / BC | HC / BC |

Counts: HJB hard error/invalid matrix `0`; HJB nonconverged `0`; HJB converged `9`; GOOD `0`; ambiguous `6`; boundary-converged `3`.

## HJB and transition-matrix receipts

The observer temporarily wrapped only the accepted operator assembler. It recorded the source-equivalent row-sum statistic after each accepted assembly and never supplied a value to HJB control flow. The accepted HJB callable, update equation, direct solve, floor, selector, boundary laws, tolerance, and ceiling were not modified. Negative stored iteration off-diagonals are an already accepted MATLAB-faithful feature and are published separately from the designated `A2max` legality test.

| `ra` | `w` | class | iterations | final `max|ΔV|` | max `A2max` | first illegal iteration | min stored off-diagonal |
| ---: | ---: | --- | ---: | ---: | ---: | --- | ---: |
| .02 | .8 | HJB_CONVERGED | 9 | 3.201666487e-09 | 2.942091015e-15 | none | -3.973126557 |
| .02 | 1.05 | HJB_CONVERGED | 9 | 9.428269721e-09 | 3.830269435e-15 | none | -3.627135776 |
| .02 | 1.3 | HJB_CONVERGED | 9 | 2.167512747e-08 | 3.830269435e-15 | none | -3.292160250 |
| .055 | .8 | HJB_CONVERGED | 9 | 5.451752827e-09 | 3.552713679e-15 | none | -3.973139833 |
| .055 | 1.05 | HJB_CONVERGED | 9 | 9.426891268e-09 | 3.608224830e-15 | none | -3.627147103 |
| .055 | 1.3 | HJB_CONVERGED | 9 | 2.167311663e-08 | 5.384581669e-15 | none | -3.292170144 |
| .09 | .8 | HJB_CONVERGED | 9 | 3.167492935e-09 | 3.552713679e-15 | none | -3.973222379 |
| .09 | 1.05 | HJB_CONVERGED | 9 | 9.418450020e-09 | 3.552713679e-15 | none | -3.627217656 |
| .09 | 1.3 | HJB_CONVERGED | 11 | 1.948366624e-08 | 0.007712953842 | none | -3.292231854 |

All returned scientific arrays were finite, had expected `(20,20,2)` shapes, and both label arrays remained inside `{B,F,0}`.

## KFE aggregates, boundaries, and modes

Every converged point received exactly one KFE. `Bt_neg` is the signed contribution from `b<0`. Boundary columns are probability mass shares at the exact endpoint.

| `ra` | `w` | `Ct` | `Lt` | `At` | `Bt` | `Bt_pos` | `Bt_neg` | `bmin` | `bmax` | `amin` | `amax` | modal `b` | modal `a` | label |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| .02 | .8 | .895518 | 1.049588 | 2.35e-15 | .304715 | .422760 | -.118046 | .000110 | 1.14e-21 | 1.000000 | 0 | .210526 | 0 | QA |
| .02 | 1.05 | 1.111231 | 1.016679 | -2.33e-15 | .369278 | .516302 | -.147024 | .001210 | -1.05e-20 | 1.000000 | 0 | .210526 | 0 | QA |
| .02 | 1.3 | 1.319829 | .990518 | -4.55e-15 | .432800 | .605903 | -.173103 | .003807 | -1.28e-19 | 1.000000 | 0 | .210526 | 0 | QA |
| .055 | .8 | .895506 | 1.049573 | 2.08e-07 | .304707 | .422753 | -.118046 | .000110 | 0 | .999999976 | 2.87e-09 | .210526 | 0 | QA |
| .055 | 1.05 | 1.111229 | 1.016677 | -9.40e-09 | .369277 | .516300 | -.147023 | .001209 | 0 | 1.000000001 | -1.13e-10 | .210526 | 0 | QA |
| .055 | 1.3 | 1.319825 | .990515 | -1.62e-10 | .432801 | .605902 | -.173100 | .003805 | 0 | 1.000000000 | -1.73e-12 | .210526 | 0 | QA |
| .09 | .8 | 1.322769 | .823498 | 8.726639 | 1.832535 | 1.853780 | -.021246 | 0 | 0 | 0 | .187136 | 3.157895 | 10 | BC |
| .09 | 1.05 | 1.532227 | .819014 | 8.766416 | 1.671264 | 1.703998 | -.032734 | 0 | 0 | 0 | .199299 | 2.789474 | 10 | BC |
| .09 | 1.3 | 1.730844 | .813189 | 8.803586 | 1.529903 | 1.576754 | -.046851 | 0 | 0 | 0 | .209437 | -.157895 | 10 | BC |

Total mass lies in `[.9999999999999998,1.0000000000000002]`. Full 20-bin `b` and `a` marginals are preserved in compact `marginals.json` and in each external point receipt. At `ra=.09`, `amax/adjacent-bin` ratios are `1.078309`, `1.103425`, and `1.110400`. At lower `ra`, `a=0` carries essentially all mass. The contaminated-row raw-system residual ranges from `9.76e-19` to `7.86e-03`; negative density entries range from none to signed numerical values with minimum `-2.78e-10`. Those continuous receipts are retained and are part of the conservative ambiguous labels; no post-result threshold was fitted.

## Scientific answers and only next gate

1. All nine HJBs converge and none is matrix-illegal. Six low/mid-`ra` KFE results are ambiguous because of complete lower-bound concentration plus mixed numerical receipts; all three `ra=.09` results are upper-`a` boundary-converged candidates. There are no GOOD points.
2. No connected coarse GOOD region exists, so GOOD aggregate ranges are not applicable.
3. HJB failure never appears. Artificial upper-bound behavior first appears along the `ra` direction between `.055` and `.09`; no analogous transition is identified along the three tested wages.
4. GOOD-candidate `Ct,Lt,At,Bt` ranges are unavailable because GOOD count is zero. All converged-point values remain published above, without upgrading them to GOOD evidence.
5. Exactly one later Owner/Reviewer gate is recommended, not run: `OWNER_REVIEW_STANDALONE_RA_TRANSITION_REFINEMENT_3X3`, with `rb=.02`, `ra={.065,.0725,.08}`, and `w={.8,1.05,1.3}`. It brackets the observed lower-to-upper illiquid-boundary transition while preserving wage coverage.

This standalone accepted MATLAB-faithful contaminated-row KFE evidence does not resolve or waive the separate corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning blocker. No global trajectory, firm, MATLAB, K1B/K2, GE, annual downstream, shock, IRF, or Results runtime occurred.

## Call ledger and evidence

- HJB calls: `9/9`; KFE calls: `9/9`; initialization constructions: `9`; scalar initialization labor roots: `7200`; scientific retries: `0`.
- Global outer turns, firm, MATLAB, K1B, K2, GE, annual downstream, shock, IRF, Results: all `0`.
- External no-overwrite evidence root: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-3x3-evidence-20260913-001`.
- External sealed manifest: 32 entries; manifest SHA-256 `061CB52D5C5C1F2268DDFFA0A526FEF2454274C169805CE2EADBA5F7ACD746D0`.
- Compact evidence: `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_coarse_3x3/`.
- Compact sealed manifest SHA-256: `52495617E2069CD1095DEBE78CC1262E0EB2FEDFCF4BE8AEFBA02010DABC4B96`.

Stop for independent ChatGPT Reviewer ACCEPT/REJECT. No successor task is published.
