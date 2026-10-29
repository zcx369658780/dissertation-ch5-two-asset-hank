# Seven frozen price results

| Point | rah | rb | net wt | HJB iterations | HJB converged | final value change | KFE | classification |
|---|---:|---:|---:|---:|---|---:|---|---|
| P0 | 0.09 | 0.02 | 19.0 | 64 | True | 3.5073277615538245e-11 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P1 | 0.07 | 0.02 | 19.0 | 100 | False | 0.032552545009447043 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |
| P2 | 0.05 | 0.02 | 19.0 | 22 | True | 6.8680616749361434e-11 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P3 | 0.07 | 0.01 | 19.0 | 100 | False | 0.3137381136912758 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |
| P4 | 0.07 | 0.03 | 19.0 | 12 | True | 5.9733238355619278e-08 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P5 | 0.07 | 0.02 | 15.5 | 23 | True | 5.9108647754158028e-08 | KFE_NOT_CERTIFIED | KFE_NOT_CERTIFIED |
| P6 | 0.07 | 0.02 | 22.0 | 100 | False | 0.30284201302767055 | NOT_EXECUTED_HJB_NOT_CONVERGED | HJB_NOT_CONVERGED |


All points have shape(b,a,z)=(20,20,2),source delta1000,max_iterations100,tolerance1e-7,drift tolerance1e-12. Point P3 is merely a price index and does not change the BLOCKED protection baseline. P0-P4 use numerical_bootstrap19; P5/P6 use counterfactual source-validated wage witnesses. Every initialization is genuinely fresh; all actual array hashes and source contexts are in the point records.

No HJB nonconvergence was converted into KFE output or a success label. No KFE failure was repaired or retried. All complete800-state new-point arrays/rates were archived LOCAL_ONLY and bound by hashes in point evidence; they do not reconstruct any prior8-state historical matrices. Global wage/negative-input checks ran before P0 initialization with model-call counters0.
