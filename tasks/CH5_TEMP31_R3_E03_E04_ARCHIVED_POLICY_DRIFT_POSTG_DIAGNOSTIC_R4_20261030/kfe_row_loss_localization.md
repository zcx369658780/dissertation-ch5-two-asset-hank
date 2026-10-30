# Original KFE algebra and row-loss localization

All indices are zero based. Grid is (b,a,z)=(20,20,2), Fortran state index=b_index+20*a_index+400*z_index; db=7/19, da=10/19. No scientific source or production entry changed.

PURE_ARCHIVE_ALGEBRA: original post.T @ original g only; no KFE rerun, matrix repair, row replacement or g adjustment.

| point | residual at destination295 | other799 max | source295 row sum | source295 g*row sum | nonconserving source rows tol1e-12 | mass-weighted sum residual | identity abs error |
|---|---|---|---|---|---|---|---|
| E03 | -0.321696958416105 | 1.2490009027033e-16 | 5.55111512312578e-17 | 3.23456068060152e-18 | 20 | -0.062378911604231 | 5.55111512312578e-16 |
| E04 | -2.94452058421148 | 7.49696761225809e-16 | 4.44089209850063e-16 | 1.68090314946045e-16 | 29 | -0.570959670068709 | 4.44089209850063e-16 |

The identity sum(G.T@g)=g@(G@ones) holds to the recorded floating-point errors. The sum of source contributions g_i*sum_jG_ij is unweighted density-flow algebra; multiplication by db*da gives mass-rate units.

| point | source-row partition | sum g*row sum |
|---|---|---|
| E03 | b_upper__a_lower__z1 | -0.000270051739589187 |
| E03 | b_upper__a_interior__z1 | -0.321426906676516 |
| E04 | b_upper__a_lower__z0 | -5.24204865154639e-08 |
| E04 | b_upper__a_lower__z1 | -5.23332952676217e-08 |
| E04 | b_upper__a_interior__z0 | -2.7489332657639 |
| E04 | b_upper__a_interior__z1 | -0.195587213693803 |

Substantive weighted row loss is at b upper boundary. E03 is concentrated at z1, interior a; E04 adds a much larger z0 interior-a contribution. These are exact archived algebra locations, not a source-algorithm causal diagnosis.

Top source losses and destination residuals are separately listed in evidence/kfe_residual_metrics.json. In E03 main source losses occur at699,679,659; E04 at299,279,259. Destination295 has the largest equation residual, yet its own source-row sum is numerical zero. Therefore the residual at equation295 must not be called loss originating entirely at source295.

STRICT_ECONOMIC_STATIONARITY_CERTIFIED=FALSE at both points. These are conditional original-source outputs, not certified economic steady states. Full MATLAB-Python parity NOT_CERTIFIED; full nonlinear Bellman residual NOT_EVALUATED.

Original source KFE status remains SOURCE_KFE_COMPUTED_WITH_STATIONARITY_WARNING. The prior pin-row method status is inherited from authenticated R3, not reproduced with a new solve.
