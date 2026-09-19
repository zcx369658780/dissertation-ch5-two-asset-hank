# Chapter 5 MP4C-2018 D123 checkpoint 10 to checkpoint 12 bounded nonlinear continuation report

Date: 2026-09-20

Task: `CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_20260920`

## Terminal verdict

`HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN`

Checkpoint 11 passed both frozen primary HJB thresholds. Execution stopped immediately. The authorized `V11 -> V12` update was not performed. Terminal topology, KFE, SVD, eigen, nullspace and `Q.T@p` were not run.

Results eligibility remains `FALSE`.

## Git and execution binding

- live `origin/main` at the execution gate: `6d6d07110b886c24aacf9ab28e77eaedb8ef0c82`;
- implementation-freeze execution HEAD: `9a0ec377358d997410fa0d7e87e34b46cda2edf6`;
- task branch: `codex/ch5-mp4c-2018-kfe-d123-checkpoint10-to-checkpoint12-bounded-nonlinear-continuation-20260920`;
- isolated worktree: `D:\ProjectTemp\c10c12`;
- worktree was clean before evidence creation;
- no `CURRENT` file was modified, main was not merged and no successor was published.

The first shell launcher omitted `PYTHONPATH=src` and exited at module discovery with `ModuleNotFoundError`, before importing the driver or creating the evidence root. It made zero scientific calls. The single entered scientific execution used the frozen implementation and produced the ledger below; its `scientific_retries` count is zero.

## Exact accepted checkpoint-10 binding

The accepted 3,249-entry checkpoint-6-to-10 manifest was fully read back before the first update. Accepted checkpoint 10 was reused without rerunning its policy map or Q assembly.

| Object | Accepted identity |
|---|---|
| V10 | `AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24` |
| P10 | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` |
| u10 | `215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38` |
| Q10 artifact | `917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD` |
| Q10 data | `B9B180F2ACF9082B5B23C1C52A27652B4FB6CD5215B7DB4816B1102400C720D2` |
| Q10 indices | `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6` |
| Q10 indptr | `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327` |
| checkpoint-10 identity | `4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D` |
| checkpoint-10 arrays | `BEA1D08A10C53E4EF3246A413A9446633DAAD6A4ACCAD4E34463BB74756C5512` |

The exact accepted V0 through V10 value history and checkpoint identities 1 through 10 were bound for cycle detection. `B10=3.874510913493001e-08` and `D10=5.8692895192891115e-06` reproduced exactly from the accepted manifest. V10 policy-map reruns and Q10 assembly reruns were both zero.

## Direct update

Exactly one frozen update, `V10 -> V11`, was performed with `Delta=1000`, F order and `scipy.sparse.linalg.spsolve`.

| Receipt | Value |
|---|---:|
| V11 SHA-256 | `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F` |
| original-equation residual infinity norm | `1.1046719095020308e-14` |
| normwise backward error | `2.426444339908083e-16` |
| inclusive threshold | `1e-12` |
| solver warnings | none |
| status | PASS |

No `V11 -> V12` solve was performed.

## Checkpoint 11

| Gate or identity | Result |
|---|---|
| fresh policy map | 800/800 cells passed |
| P11 | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` |
| u11 | `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648` |
| Q11 artifact | `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD` |
| checkpoint-11 identity | `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B` |
| D2 | PASS |
| B11 | `5.456747553811425e-11` |
| D11 | `5.4012647243695255e-08` |
| primary convergence | PASS |
| exact cycle | not evaluated after primary PASS; no exact-cycle classification |
| approximate period-2/3 | not evaluated after primary PASS; no approximate-cycle classification |

The primary gate was evaluated first. Both inclusive thresholds, `B11<=1e-8` and `D11<=1e-7`, passed at the same checkpoint.

## Policy, switching, operator and D2 diagnostics

Checkpoint 11 retained the same selected-policy identity as checkpoint 10. Active-constraint counts were: none 748, lower-b 20, upper-b 19, upper-a 12 and upper-a plus upper-b 1. Transfer branches were negative 298, positive 323 and zero-kink 179. The largest continuous-control changes were `|Delta c|=1.66437185153967e-05`, `|Delta d|=4.268296140197414e-06`, `|Delta g_b|=2.546694910066094e-05` and `|Delta g_a|=4.268296140197414e-06`.

Interior-a switching selected 29 policies from 61 attempts; one switching root converged and 60 attempts required no root. Liquid-Z and joint switching selected zero policies. Q11 had 3,118 nonzeros and the same sparsity pattern as Q10. `||Q11-Q10||_inf=0.0001457303875539162`; the maximum absolute changed entry was `7.286519377691647e-05`.

D2 recorded zero outward closed-face count and amount, exact-zero diagonal construction error, minimum off-diagonal `2.7404782515125115e-06`, and `max(abs(Q11@1))=1.7763568394002505e-15`. Liquid and illiquid coordinate-action maximum errors were `1.0658141036401503e-14` and `2.7200464103316335e-14`. Every D2 check passed.

## Exact scientific call ledger

| Operation | Count |
|---|---:|
| direct HJB solves / updates | 1 / 1 |
| fresh corrected policy maps | 1 |
| selector evaluations | 800 |
| scalar roots total | 270 |
| liquid-Z roots | 14 |
| interior-a switching roots | 1 |
| joint-switching roots | 0 |
| D2/Q assemblies | 1 |
| complete checkpoint evaluations | 1 |
| V10 policy-map reruns / Q10 reruns | 0 / 0 |
| scientific retries / solver substitutions | 0 / 0 |
| damping, relaxation, adaptive Delta or continuation calls | 0 |
| parameter continuation, clipping or artificial diffusion calls | 0 |
| topology / KFE / SVD / eigen / nullspace / Q.T@p | 0 |
| MATLAB / production / outer / firm / GE / annual / shock / IRF / Results | 0 |

Accepted V0 through V10 were each loaded once as required. Accepted P2/P3/P6/P10, u2/u3/u6/u10 and Q1/Q2/Q3/Q6/Q10 were each loaded once. No prior checkpoint policy map or Q was regenerated.

## Engineering validation and evidence seal

Focused preflight: `87 passed`. `py_compile` and `git diff --check` passed. The pre-execution and post-execution scientific-code hash maps match exactly.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_bounded_nonlinear_continuation_20260920_run001`

Sealed-manifest readback:

- SHA-256: `5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41`;
- entries: `819`;
- bytes: `13,089,592`;
- every recorded path, byte count and SHA-256 independently matched;
- manifest readback failures: `0`.

The evidence contains the accepted checkpoint-10/history binding, one direct-solve receipt, 800 checkpoint-11 cell receipts, D2/Q receipts, same-value B/D diagnostics, policy/operator/switching diagnostics, cycle-order receipt, scientific ledger and pre/post code-freeze hashes.

## Boundary

This verdict is only an HJB convergence candidate under frozen household prices and calibration. It does not establish terminal KFE admissibility, uniqueness, stationary density, market clearing, production replacement, GE, annual dynamics, shocks, IRFs, welfare or Results eligibility. A fresh independent Reviewer gate is required before any terminal topology/KFE task.
