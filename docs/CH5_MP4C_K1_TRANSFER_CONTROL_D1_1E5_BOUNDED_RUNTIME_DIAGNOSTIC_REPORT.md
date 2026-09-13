# CH5 MP4C K1 — transfer-control D1=1e5 bounded runtime diagnostic report

Date: 2026-09-13
Task: `CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC`

## 1. Classification and decision

`D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_COMPLETE__TAIL_STRESS_REDUCED__HJB_CONVERGENCE_NOT_IMPROVED__INDEPENDENT_L3_REVIEW_REQUIRED`

D1 implemented the frozen post-FOC eligibility rule exactly and sharply reduced the extreme selected-transfer, adjustment-cost and drift tails. It did not improve HJB convergence: turns 2–5 produced `6/124` converged calls under control and `5/124` under D1. Turn 2 itself remained `2/31` versus `2/31`; later differences are path-history propagation, not same-state causal effects.

No new NaN/Inf, scientific exception or accounting/provenance failure appeared. However, one fewer HJB call converged overall and D1 did not remove binding return/wage safeguards. This bounded evidence therefore does **not** support a longer provisional D1 continuation or a wider D stage without fresh Reviewer/Owner authority.

Results eligibility=`FALSE`.

## 2. Authority, baseline, isolation and scope

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh live baseline: `4826b18044df84cee7323bf34bf7fd5d05045223`.
- Branch: `codex/ch5-mp4c-k1-transfer-d1-1e5-20260913`.
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-transfer-d1-1e5-20260913-001`.
- External evidence: `D:\ProjectTemp\ch5-mp4c-k1-transfer-d1-1e5-evidence-20260913-001`.
- `D:\Zotero-Analytical-Workflow` was not cleaned or modified.

The shared oracle change is an optional D1 eligibility filter defaulting to OFF. The instrumented HJB adds the optional limit and a local OFF-policy comparison observer. All runner, receipt and finalization logic is task-owned. No D2/D3/OFF, G3, K1B, K2 or Results work was performed.

## 3. D1 implementation and pre-run gates

The exact contract is inclusive: `abs(d_raw)<=1e5` remains admissible and `abs(d_raw)>1e5` is excluded from selector competition after the raw FOC candidate is preserved. There is no clipping and no manufactured endpoint. Existing feasibility/boundary status remains separate; the existing zero option and other admissible nonzero branches remain available.

Pre-run evidence passed:

- D1 OFF versus the accepted oracle: exact scientific parity;
- D1 ON/OFF raw candidates before eligibility: exact identity;
- a no-hit fixture: exact scientific output equality;
- pure selector fixtures: inclusive endpoint, unchanged raw values, no clipped endpoint, separate boundary feasibility, zero-option availability and other-admissible-branch availability;
- official fixture budget: `3` HJB calls and `0` trajectory advancements.

Focused suite at candidate closeout: `8 passed`.

## 4. Scientific runtime ledger

| Ledger | Control C | D1 | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 5 | 5 | 10 |
| HJB calls | 155 | 155 | 310 |
| HJB iterations/direct solves | 13,834 | 13,921 | 27,755 |
| KFE calls | 155 | 155 | 310 |
| raw branch receipts | 44,268,800 | 44,547,200 | 88,816,000 |
| scientific retries after advancement | 0 | 0 | 0 |

MATLAB, standalone KFE, K1B, K2, GE, annual downstream, shock/IRF and Results calls were all `0`.

One permitted pre-state engineering retry occurred because the initial Control receipt filename/output shape was invalid. That attempt stopped before any HJB, KFE or trajectory-state advancement. Both completed runtimes exited normally with 155 chunks, five turns and empty terminal errors.

## 5. Turn-1 equality and turn-2 common entering state

The common-state gate passed. Runtime payload bytes, turn-1 entering state, completed turn-1/entering-turn-2 state, all 558 compared turn-1 HJB scientific arrays, turn-2 grids, HJB `r_a`/wage inputs and wage-guard status, raw annual/conversion/same-S provenance, and turn-2 first-iteration raw candidates were exact-equal.

The first D1 rejection occurred in Beijing, turn 2, HJB iteration 4, zero-based grid cell `[19,17,1]`, branch `d_bf`, with raw `d=-183542.63913872826`. The branch was in the control winning direction but was not the selected contributor. Both local policies therefore remained label `B`, selected `d=-85015.44837383348`, with identical cost, drifts, operator, value update and HJB statistic at that event. The raw value matched the control trajectory exactly and was not rewritten.

This is `COMMON_ENTERING_STATE_D1_IMMEDIATE_RESPONSE`. Turns 3–5 are `PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`.

## 6. D1 hits, rejected winners and replacement modes

D1 was active only in turns 2–5. It inspected `39,440,000` active raw branch-candidates and rejected `15,330` (`0.0388692%`): positive `7,742`, negative `7,588`.

| Turn | active raw | rejected | winner changes | to existing zero | to other nonzero |
|---:|---:|---:|---:|---:|---:|
| 2 | 9,888,000 | 3,842 | 903 | 602 | 301 |
| 3 | 9,920,000 | 4,308 | 928 | 590 | 338 |
| 4 | 9,852,800 | 3,728 | 800 | 486 | 314 |
| 5 | 9,779,200 | 3,452 | 828 | 478 | 350 |

Of all rejected raw branches, `8,678` (`56.6080%`) were never in the control winning direction and `6,652` were in that direction. There were `3,468` rejected control-contributor branch events spanning `3,459` iteration-cell winner changes; every changed cell had a rejected control contributor and no changed cell occurred without one. The `3,459` changes split exactly into `2,156` fallbacks to the existing zero option and `1,303` switches to another admissible nonzero branch.

At final HJB iterations only, `21/99,200` cells differed: `13` moved to existing zero and `8` to another admissible nonzero branch. No selected D1 transfer exceeded `1e5`.

Hits were concentrated in nonconverged calls: `15,186/15,330` hits (`99.0607%`) and `3,435/3,459` winner changes (`99.3062%`). This is descriptive concentration, not proof that rejection causes convergence.

## 7. Turn-2 locality and discrete-rejection stability

The local same-derivative selector comparison shows that all `3,459` immediate winner changes occur exactly where a control-selected raw contributor is D1-inadmissible. Thus the direct selector response is strictly localized to would-be-competitive `|d_raw|>1e5` candidates. Within the iterative HJB, an earlier local change can propagate through later derivatives, operators and values; those later within-call differences are not claimed to remain cell-local.

No clipping, endpoint manufacture, nonfinite output, scientific exception or hard stop occurred. Turn-2 convergence was unchanged at `2/31`, so there is no same-state evidence of a new hard instability. The later path produced one fewer converged call overall, so there is also no evidence of a stability improvement.

## 8. HJB convergence and statistics

| Turn | C converged / ceiling | D1 converged / ceiling | C median / max statistic | D1 median / max statistic |
|---:|---:|---:|---:|---:|
| 1 | 20 / 11 | 20 / 11 | `2.827e-8 / 0.3588` | exact equal |
| 2 | 2 / 29 | 2 / 30 | `0.6547 / 50.94` | `0.5895 / 12.87` |
| 3 | 1 / 30 | 0 / 31 | `1.877 / 170.46` | `0.7725 / 22.39` |
| 4 | 3 / 28 | 1 / 30 | `0.6687 / 203.21` | `1.0485 / 63.26` |
| 5 | 0 / 31 | 2 / 29 | `0.7902 / 31.83` | `1.0527 / 85.48` |

All-turn convergence was `26/155` for C and `25/155` for D1. D1 used 87 more HJB iterations. Lower maxima in turns 2–4 and two turn-5 convergences do not offset the aggregate failure to improve convergence; turns 3–5 cannot be interpreted as same-state causal comparisons.

## 9. Transfer, cost and drift stress

Across saved turns 2–5 outputs, D1 reduced selected-transfer absolute maximum from `4.26994e7` to `9.98835e4`, adjustment-cost absolute maximum from `1.92453e14` to `3.79116e9`, `mu_a` absolute maximum from `4.26994e7` to `9.98828e4`, and `mu_b` absolute maximum from `1.92453e14` to `3.79106e9`.

The reduction is strongest in the far tail. Pooled absolute p99.9 moved from `44,332.6` to `23,758.8` for transfer, from `3.74733e8` to `8.72949e7` for cost, from `44,334.0` to `23,755.8` for `mu_a`, and from `3.74768e8` to `8.72687e7` for `mu_b`. Central quantiles do not uniformly improve: transfer median and p90 are slightly higher under D1, and turn-2 p99 transfer/cost are higher. D1 therefore truncates extreme stress but does not provide a monotone distribution-wide improvement.

Consumption remained finite with the existing maximum `1000`; labor remained finite. Material outward boundary counts persist in both paths and are not erased by D1.

## 10. Priority checkpoints

All required checkpoints were recorded. D1 hit/winner-change counts were: 湖北 T2 `170/41`, 山东 T2 `348/76`, 广东 T2 `79/21`, 辽宁 T2 `36/7`, 吉林 T2 `13/3`, 四川 T4 `282/29`, 云南 T4 `141/36`. Only 辽宁 T2 converged among these D1 calls; no checkpoint is interpreted as proof that D1 ensures HJB convergence.

## 11. Return/wage monitoring

Binding price safeguards persist.

- Return turns 2–5: both paths had upper/unsaturated province counts `18/13`, then `22/9`, `22/9`, `22/9`; lower hits were zero. Raw upper extrema reached about `0.9747`, while guarded `r_a` remained at most `0.35`.
- Wage turns 1–4: both paths had lower/upper/unsaturated counts `4/24/3`. At turn 5, C had `13/12/6` and D1 had `14/12/5`. Raw wage extrema remained roughly `0.042–7.57`, while guarded wage remained in `[0.8,1.3]`.

The long-run target `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` is not met.

## 12. K1, C1, same-S and provenance

Across all 310 province-turns:

- same-S quantity/payoff identity passed;
- same-turn household feedback remained false;
- source-faithful labor remained true and normalized labor remained off;
- maximum capital-column residual was `3.725290298461914e-9` MU;
- maximum national private-capital conservation residual was `2.9802322387695312e-8` MU;
- maximum C1 accounting residual was `2.9802322387695312e-8` MU;
- maximum raw-`ra0` reconstruction residual was `5.551115123125783e-17`.

Scientific NaN/Inf hard-stop count=`0`; scientific exceptions=`0`.

## 13. KKT, KFE and Results boundary

Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`. All 310 KFE calls returned, but every result remains `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers. D1 tail reduction is not KFE admissibility, steady-state acceptance or Results authority.

Results eligibility=`FALSE`.

## 14. Evidence closure

External sealed manifest:

- path: `D:\ProjectTemp\ch5-mp4c-k1-transfer-d1-1e5-evidence-20260913-001\sealed_manifest_sha256.json`;
- entries excluding manifest: `1,678`;
- bytes excluding manifest: `4,256,953,327`;
- SHA-256: `C60C353FE1ABC24509F5753E808F837BA19C9856B98FAE9998AB59DAC9BCE6BE`;
- every listed entry was read back and rehashed successfully.

Compact evidence is under `docs/evidence/ch5_mp4c_k1_transfer_control_d1_1e5/`.

The first external finalizer output had correct boundary hit counts but used the full active population as every boundary denominator. The external seal was preserved without mutation. Before candidate publication, the finalizer was corrected and the compact summary denominators were recomputed from the exact boundary masks; `finalization_correction_receipt.json` records this zero-science correction.

## 15. Longer-D1 and wider-D assessment

The evidence supports the narrow claim that D1 removes extreme selected controls and associated far-tail cost/drift stress without a hard failure. It does not support a longer provisional D1 continuation because convergence did not improve and binding price safeguards persist.

The current run also establishes no positive numerical case for a wider D stage. A future wider-threshold sensitivity could be considered only as a fresh Owner/Reviewer decision; this report neither selects nor authorizes D2/D3/OFF.

## 16. Exactly one next gate

`INDEPENDENT_GPT_L3_ACCEPT_OR_REJECT_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_CANDIDATE`

Stop. Do not merge main, publish a successor task, or enter D2/G3/K1B/K2/Results.
