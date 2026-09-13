# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_TASK_ACTIVE`。

最新 accepted omega=0.5 diagnostic candidate：`5576ba2f921a3ed86a6fdd2205ffb46a3dc34c9a`。
Reviewer acceptance：`docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_ACCEPTANCE.md`。
Owner/Reviewer standalone convergence-domain freeze：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_CONVERGENCE_DOMAIN_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN.md`。
Results eligibility=`FALSE`。

Accepted omega=0.5 evidence is mixed only: turn1 `20/31 -> 23/31`, turn2 `2/31 -> 0/31`, all `22/62 -> 23/62`; chattering diagnostics mostly fall, but seven accepted converged calls are lost and both-converged endpoints are not generally identical. No HJB damping/relaxation is accepted as a production method, and no damping ladder/adaptive solver route is authorized.

Owner has redirected the scientific priority to the original MATLAB-faithful standalone household block. The HJB algorithm itself is not to be redesigned. The next objective is to map the healthy input domain before returning to the full multi-province model.

Active task runs exactly nine standalone points with `rb=.02`, borrowing gap `.07`, `ra ∈ {.02,.055,.09}`, household wage `w ∈ {.8,1.05,1.3}`. Grid remains `I=20`, `b∈[-2,5]`; `J=20`, `a∈[0,10]`; `Nz=2`, `z∈[.8,1.3]`; all other accepted MATLAB-faithful household parameters/numerics are fixed.

Each point first receives a MATLAB-style HJB classification: hard error/invalid transition matrix, legal HJB nonconvergence, or HJB convergence. The original value-function update, upwind/selector logic, transition-matrix construction, pseudo-time/direct solve, tolerance, iteration ceiling, derivative floor and boundary law are unchanged.

Only HJB-converged points proceed to the accepted standalone MATLAB-faithful stationary KFE solve. For those points the task records `Ct,Lt,At,Bt`, mass normalization, `a/b` marginals, exact endpoint mass shares and modal asset locations. The first scan may descriptively label converged points as boundary-converged candidate, good steady-state candidate or quality-ambiguous; no post-result numeric cutoff may be invented to force a category.

The task does not run the global multi-province model, firm block, GE, K1B/K2, annual downstream, shocks, IRFs or Results. It does not add adaptive scan points after seeing outcomes. After independent acceptance, any refinement grid near an observed boundary requires a new Owner/Reviewer gate.

Standalone KFE use in this task is limited to classifying converged household steady states with the already accepted MATLAB-faithful contaminated-row solve. The separate corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker remains unresolved and is not waived.

下一 gate：Builder完成 coarse 3×3 scan 后，由 ChatGPT Reviewer 独立 ACCEPT/REJECT，并由 Owner/Reviewer 决定下一小范围 refinement grid。