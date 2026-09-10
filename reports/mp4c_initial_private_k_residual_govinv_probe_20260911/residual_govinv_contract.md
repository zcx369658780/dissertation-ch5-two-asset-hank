# Residual GovInv initialization probe contract

This package compares two accounting initializations without changing production runtime state.

- `K_private(beta=1)` is produced once by the existing At-only cross-province allocation.
- `Bt` is absent from the allocation API and does not enter productive capital.
- `G0 = Ktarget`; therefore `K_firm_G0 = Ktarget + K_private`.
- `G1 = max(Ktarget - K_private, 0)`; therefore `K_firm_G1 = max(Ktarget, K_private)`.
- `Kt_supply_initial(beta) = beta * Kt_supply_initial(beta=1)` follows algebraically because every source contribution is linear in `beta * At * N` and the destination exclusion/average is linear. No second allocation or beta cell was run.
- `beta_a_star = Ktarget / K_private(beta=1)` is diagnostic geometry, not an estimated or accepted bridge.
- `beta_a=1` remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

The probe does not call or modify migration, normalized migration, firm, wage, GovInv controller, outer-turn, steady-state, GE, annual, IRF, or Results routes. It does not wire G1 into the active runtime.
