# Chapter 5 MP4C K1 bilateral capital-network implementation acceptance

Date: 2026-09-11

Reviewer verdict:

`K1_BILATERAL_CAPITAL_NETWORK_ACCEPTED__HOME_CAPITAL_RESTORED__PORTFOLIO_AND_CAPITAL_CONSERVATION_ENFORCED__LAGGED_ENDOGENOUS_FOREIGN_SHARE_ENGINE_READY_FOR_PARAMETER_FREEZE`

Accepted candidate:

`742ae11dbb057c7d33650ed4bc8d4db59b90d435`

## Scope accepted

The new separately named K1 capital-network module is accepted as a zero-science implementation capability. It remains disconnected from active one-turn, C1, firm, steady-state, and trajectory routes.

The accepted network orientation is destination-by-origin. For each origin province `i`, total private illiquid wealth is `W_i=A_i*N_i`. The currently frozen total foreign share `theta_i=inter_prv_ratio_i` remains exogenous in K1. The full portfolio matrix satisfies:

- `S[i,i]=1-theta_i`;
- `S[j,i]=theta_i*P[j,i]` for `j != i`;
- `sum_j S[j,i]=1`;
- bilateral private-capital flow `M_K[j,i]=S[j,i]*W_i`;
- destination private productive capital `Kprivate_j=sum_i M_K[j,i]`;
- household illiquid portfolio return `rah_i=sum_j S[j,i]*portfolio_return_j`.

Thus the same matrix `S` governs both quantity allocation and household return aggregation.

## Accepted repairs

1. The previously omitted retained home capital `(1-theta_i)*A_i*N_i` is restored exactly to the diagonal capital flow.
2. National private capital is conserved: destination private productive capital sums to total household illiquid wealth under the current bridge.
3. The legacy `rah` destination-`theta_j` double-weighting is removed in the repaired successor.
4. The repaired equal-foreign-share special case (`beta_distance=beta_return=0`) reduces to the Owner's intended old design: fixed total outward share `theta_i`, equal allocation over other provinces, but with correct home retention and normalized payoff weights.
5. Foreign destination shares are implemented by a stable foreign-only softmax using explicit distance and lagged-return score inputs.
6. Return attractiveness signal and realized/payoff return are explicitly separate API objects.
7. Same-turn `firm -> return -> share -> capital -> firm` feedback is prohibited by the lagged-return provenance contract.

## Evidence accepted

Focused tests: `29/29` final PASS. Compile, `git diff --check`, and `git show --check` passed. Manifest readback passed `15/15`. No scientific/model/runtime call occurred.

The asymmetric fixture is accepted as accounting evidence:

- origin wealth `[20,60,120]`, national `200`;
- legacy destination K `[63,50,17]`;
- repaired destination K `[79,80,41]`;
- repaired-minus-legacy `[16,30,24]`, exactly the omitted retained home capital;
- legacy implied `rah` weight sums `[0.93,0.75,0.48]`;
- repaired weight sums `[1,1,1]`;
- national conservation residual `0`.

Legacy `src/ch5_two_asset_hank/multi_province/capital_allocation.py` remains byte-identical at SHA-256 `BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40`.

## Scientific boundary

This acceptance does **not** identify or authorize:

- `beta_distance`;
- `beta_return`;
- distance/friction normalization;
- lagged-return-score normalization or source;
- portfolio smoothing/partial-adjustment speed;
- endogenous `theta_i`;
- the final payoff-return concept (`ra0`, clipped `ra`, normalized return, or expected return);
- integration into steady-state runtime;
- a scientific trajectory;
- Results eligibility.

The accepted K1 route is an engineering and accounting foundation only.

## Next gate

Before any bounded scientific run, Owner/Reviewer must freeze the K1 economic scoring contract. The lowest-risk sequence remains:

1. freeze distance/friction data map and normalization;
2. freeze lagged-return signal definition and normalization;
3. freeze explicit `beta_distance` and `beta_return` values or a data-backed identification protocol;
4. decide whether K1 initially keeps `theta_i` fixed or progresses to endogenous home/foreign allocation only after the conditional foreign-share route is validated;
5. freeze payoff-return mapping separately from the attractiveness signal;
6. only then authorize one bounded integration trajectory.

Results eligibility remains `FALSE`.
