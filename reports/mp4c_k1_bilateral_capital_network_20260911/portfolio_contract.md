# K1 bilateral portfolio contract

- Schema: `CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_V1`
- Orientation: `S[destination,origin]` and `M_K[destination,origin]`.
- Origin wealth: `W_i=A_i*N_i`; liquid assets and public/GovInv capital are excluded.
- Fixed home/foreign nest: `S[i,i]=1-theta_i`; `S[j,i]=theta_i*P[j,i]` for `j!=i`.
- Foreign score: `-beta_distance*distance_score[j,i] + beta_return*lagged_return_score[j]` with a stable foreign-only softmax.
- Quantity: `M_K[j,i]=S[j,i]*W_i`; destination private K is the row sum.
- Payoff: `rah_i=sum_j S[j,i]*portfolio_return_by_destination[j]` using the identical `S`.
- `lagged_return_score` selects attractiveness; `portfolio_return_by_destination` supplies payoff. They are separate required API objects.
- `beta_distance` and `beta_return` are required explicit inputs with no defaults. No coefficient, normalization, distance definition, or payoff-return concept is selected here.
- All returned arrays are read-only. The successor is not imported by active one-turn, steady-state, or trajectory code.
