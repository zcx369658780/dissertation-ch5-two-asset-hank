# Distinct convergence diagnostics

| Arm | delta | iterations | converged | final deltaV | stale-policy residual | implicit identity error |
|---|---:|---:|---|---:|---:|---:|
| A | 1000.0 | 80 | False | 0.031119609835753792 | 3.1119609835636441e-05 | 1.0489384968254134e-15 |
| B | 100.0 | 80 | False | 0.016079079861198942 | 0.00016079079861245488 | 5.0848404263212355e-16 |
| C | 10.0 | 80 | False | 0.16462851608474538 | 0.016462851608474036 | 1.087671619437458e-15 |


DeltaV is the source's actual adjacent-iteration supnorm, read after its statistic assignment and independently checked against V_new-V_old. Every arm's full80-scalar trajectory is preserved. It is distinct from the frozen last-policy residual R_stale=norm_inf(rho*V_new-u_last-G_last@V_new). G_last is result.operator.full, the operator actually used in the last implicit solve; result.post_convergence_operator is not substituted.

The source Fortran flatten order is used throughout. Read-only tracing captures last V_old,utility,G,matrix,rhs in memory. No raw value-function arrays are saved or extra policies/solves called. The vector identity R=(V_old-V_new)/delta and scalar norm relation are audited. Actual captured matrix is compared with (1/delta+rho)I-G and rhs with u+V_old/delta; both comparison errors are zero in all arms. Linear residuals and vector-identity errors are at most about1.1e-15, below the frozen1e-10*(1+scale) roundoff bound.

All three have finite8x8 sparse operators. A/B/C nnz=26/24/26. Maximum signed row sums are about5.55e-17/5.55e-17/0, but the row-sum absolute maximum is0.00045691399330394233 in every arm. Minimum offdiagonal entries are approximately-0.2891145162423588/-0.081/-0.27379287506930644, including implicit zeros. These are source generator/scientific risks; a small signed maximum does not establish zero row sums or a valid Markov generator. No operator was altered.

The final deltaV and stale residual do not improve monotonically as delta is reduced. A/B/C negative update cosines:40/38/15; growth-ratio>1 counts:38/35/40. No finite iteration budget can establish that the scientific model will never converge. No complete nonlinear Bellman/optimality residual was evaluated, because it would require policy reoptimization beyond this diagnostic contract. No arm receives PASS_BOUNDED_NUMERICAL_FIXED_POINT.
