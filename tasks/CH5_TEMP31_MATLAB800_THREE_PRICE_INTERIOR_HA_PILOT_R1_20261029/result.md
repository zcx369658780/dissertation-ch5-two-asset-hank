# TEMP31 MATLAB-reference800-state seven-price interior HA pilot

TASK_ID=CH5_TEMP31_MATLAB800_THREE_PRICE_INTERIOR_HA_PILOT_R1_20261029
COMPLETED=all seven frozen points, exactly once in order, on the original20x20x2 asset limits and immutable fixed Python source.
CERTIFIED_INTERIOR_HA_CANDIDATES=0
LOCAL_MEASUREMENT_TERMINAL=SEVEN_POINTS_COMPLETE__NO_CERTIFIED_INTERIOR_HA_CANDIDATE
DELIVERY_AT_PAYLOAD_CREATION=PENDING_PAYLOAD_AND_SINGLE_FILE_SEAL_REMOTE_READBACK

| Point | rah | rb | net wt | HJB iterations | HJB converged | final value change | KFE | classification |
|---|---:|---:|---:|---:|---|---:|---|---|
| P0 | 0.09 | 0.02 | 19.0 | 64 | True | 3.5073277615538245e-11 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P1 | 0.07 | 0.02 | 19.0 | 100 | False | 0.032552545009447043 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |
| P2 | 0.05 | 0.02 | 19.0 | 22 | True | 6.8680616749361434e-11 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P3 | 0.07 | 0.01 | 19.0 | 100 | False | 0.3137381136912758 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |
| P4 | 0.07 | 0.03 | 19.0 | 12 | True | 5.9733238355619278e-08 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P5 | 0.07 | 0.02 | 15.5 | 23 | True | 5.9108647754158028e-08 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P6 | 0.07 | 0.02 | 22.0 | 100 | False | 0.30284201302767055 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |


The four HJB-converged points genuinely ran the unchanged MATLAB-faithful KFE on the exact returned post_convergence_operator.full. All four failed the original-post-operator stationarity residual gate1e-7, despite finite normalized density, small negative probability mass and tiny contaminated raw linear-system residual. Their At/Bt/Lt/Ct and internal probabilities are retained as unverified numerical diagnostics only. None is a certified stationary/interior household solution. The three nonconverged HJB points made zero KFE calls.

Exactly7 fresh initializations,5600 source root/brentq calls,7 HJB drivers,421 source iterations,336800 HJB policy cells,428 source operator assemblies and4 KFE calls.7 supervised commands all exited0 without timeout; each had180s hard timeout,one active child,1GiB committed-memory cap and six BLAS environment limits1. Native thread counts were not measured; RSS not separately capped. No retry or eighth point.

NOT_COMPLETED=certified interior HA candidate, continuous three-price feasibility region, full MATLAB source parity, nonlinear Bellman optimality or stages2/3. No convergence inference was imported from8-state or historical expanded-grid runs. Existing source/economic parameters/history remain unchanged; no empirical files,firm,GE,IRF or province model runs.
NEXT_ACTION=STOP after exact remote delivery; await GPT independent A/B/C. P3 protection BLOCKED,FORMAL_SOURCE_FREEZE FALSE,V010 UNCHANGED,V011 NOT_STARTED,Results FALSE,model_activation FALSE,REAL_GE FALSE,FULL_RUNNER_IO_CLOSURE BLOCKED. No automatic Issue/PR/merge/cleanup/next.
