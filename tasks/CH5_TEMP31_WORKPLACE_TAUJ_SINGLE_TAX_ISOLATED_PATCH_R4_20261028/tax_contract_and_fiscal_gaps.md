# Mathematical and scientific contract

Owner-approved goals: wage earned at destination j uses tau_j; one labor-income tax application. Matrix axes are destination j rows, origin i columns. For the isolated candidate:

q_ji = C_i^(-gamma_c/phi_l) * [w_j*(1-tau_j-sigma_ji)/phi_ji]^(1/phi_l).

The source-like quantity is M_ji=q_ji*N_i, with L_supply_j=sum_i M_ji. It does not impose household origin-mass conservation. The explicitly separate normalized route uses s_ji=q_ji/sum_k q_ki and M_ji=s_ji*(ell_i*N_i). Thus sum_j M_ji=ell_i*N_i and national sums match. Neither route inserts an extra z_i, population factor or new elasticity. Normalized labor is not wired to production.

The declared net composite already incorporates tau_j and sigma_ji, so the proposed single-class data has tau_for_HA=0, sigma_for_HA=0, labor_weight_for_HA=1 and effective_wage=net_composite. This is not a decision that real taxes or migration costs disappear: their original vectors/matrices remain separate mechanism data. The semantic label is a required caller contract, not proof that a default production wage is net. Both future consumer phases must bind to this same data; actual initialization and HJB execution remain unverified.

## Explicit unresolved scientific decisions

1. **Labor units and z/N**: historical kernel has no explicit individual efficiency z_i. Whether Lt_mat, household ell or destination L already embodies efficiency, population, employment or hours is unresolved. N is multiplied once algebraically, but its empirical definition is not certified.
2. **Fiscal tax base**: fixed firm.py line 135 retains Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt. Conditional tau_j*w_j*L_j assumes L is already effective and population aggregated, and wages have compatible units. That assumption is not adopted. Diagnostic national tax is only the sum of conditional province terms.
3. **Sigma and incidence**: sigma is treated algebraically as a migration wedge, not added to government revenue. Its private cost, resource cost, destination/residence incidence and transfers require an economic contract.
4. **Wage clipping**: the relationship between clipped actual paid wages, the composite wage and the fiscal wage base is not resolved.
5. **First production round**: empirical entry-state code sets w from a scalar default; production's actual first w has not been certified NET_COMPOSITE. R4 does not relabel that state or wire this adapter into production.
6. **Real consumer equivalence**: auxiliary HA objects are locally absent. Planner static facts identify potential repeated wedges, but actual initialization/HJB/KFE integration is NOT_EXECUTED.
7. **Real empirical provenance/canonical**: no raw wage adoption, 31-province identifier/year binding, source freeze, real convergence or Results claim is authorized or produced.

All fiscal diagnostics remain SCIENTIFIC_PENDING. Formal fiscal, HA/HJB/KFE, V010, ORACLE_SHA, annual production entrypoints and historical sources are unchanged.
