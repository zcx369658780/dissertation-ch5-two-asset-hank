# Separate method execution and scientific certification

Layer1 MATLAB_KFE_METHOD_EXECUTED: fixed post G, transpose, source row replacement, rhs .007, sparse solve, finite raw solution, finite nonzero normalization and finite density. No clipping, matrix repair or external stationarity criterion is inserted into KFE.

Layer2 ORIGINAL_STATIONARITY_DIAGNOSTIC: report ||G.T@g||inf on untouched G, its location and non-pin remainder, row sums, offdiagonal minimum, signed density/negative probability, mass, boundary/marginal mass and raw/normalized pinned-system residuals. Warning threshold is1e-7. Normalized pinned equation is C*g=rhs/factor, not C*g=rhs. These are different from the original stationarity equations.

Layer3 STRICT_ECONOMIC_STATIONARITY_CERTIFIED: the displayed bounded strict checks require finite density, mass error<=1e-8, negative probability<=1e-8, original stationarity<=1e-7, and raw pinned-system residual<=1e-7. Passing these numerical checks alone would still not certify economic consistency, all source parity or production readiness. Here original stationarity fails in all four cases, so strict certification is FALSE.

Compatibility=SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING (contract alias SOURCE_METHOD_COMPUTED_WITH_STATIONARITY_WARNING). This is an added interpretation in the new validator/reports only. Historical KFE_NOT_CERTIFIED stays unchanged; no caller or future outer workflow is rewired. At/Bt are unverified diagnostic moments. No formal31-province Results or next price search is authorized by this delivery.
