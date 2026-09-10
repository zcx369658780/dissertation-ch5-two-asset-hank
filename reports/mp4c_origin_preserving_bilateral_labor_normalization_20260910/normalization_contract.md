# Origin-preserving bilateral labor normalization contract

- Schema: `origin-preserving-normalized-migration-labor/v1`.
- Orientation: rows are destinations `j`; columns are origins `i`.
- Raw kernel: `q[j,i] = C_i^(-gamma_c/phi_l) * (wjt_j * (1-tau_i-sigma[j,i]) / phi[j,i])^(1/phi_l)`.
- Origin mass: `L_origin[i] = household_labor_per_capita[i] * population[i]`; population is multiplied exactly once.
- Shares: `s[:,i] = q[:,i] / sum(q[:,i])`; each finite positive origin column sums to one.
- Bilateral flow: `M[j,i] = s[j,i] * L_origin[i]`.
- Destination firm labor: `L_firm[j] = sum_i M[j,i]`.
- Net flow: `net[i] = L_firm[i] - L_origin[i]`.
- Conservation: every flow column equals its origin mass and national destination labor equals national origin labor.
- Invalid, non-finite, negative, or zero-total attractiveness fails closed; there is no equal-share fallback.
- The legacy `reconstruct_migration_labor` and `run_source_faithful_one_turn` contracts remain unchanged.

The result preserves `q`, `s`, `L_origin`, `M`, destination labor, column sums, net flow, and the national residual. It therefore retains the origin column needed for a later wage-provenance task without changing the current wage aggregation rule.
