# Independent Work review: outer state unit, scale, and precision evidence

Date: 2026-09-23 (Asia/Shanghai)

Verdict: `ACCEPT__CH5_FULL_OUTER_STATE_UNIT_SCALE_PRECISION_EVIDENCE__ZERO_SCIENCE__OWNER_CONVERGENCE_LAW_PENDING`

## Reviewed local candidate

- Work dispatch: `1e12ac1bff3a770ab7ba8df12201bf276a9c188f` from `4d80d992e0d5f537a400f586cb526b584342adc0`.
- Builder candidate: `f93407460e79f93c3781f258b856e55bb1ee3a15`. Its only changed paths are `docs/CH5_FULL_OUTER_STATE_UNIT_SCALE_PRECISION_EVIDENCE_20260923.md` and `EVIDENCE/ch5_full_outer_state_unit_scale_precision_20260923/evidence_receipt.json`.
- Document SHA-256: `63F4989CD906A1A446E6ACCEC774E2E8ABE523F7468ACB558FD301D0EA331906`. Receipt SHA-256: `473EF69670BDFF2766BBC1DFBC495DC24913553030045EADEBEBC3B1336B6E81`.
- The worktree is clean; `git show --check` passes; production `src` tree remains `00682b2e1a7ba23665f6e16f6acf48ad35874883`. Independent readback of all 39 receipt input paths and SHA-256 values found zero mismatches.

## Independent findings

- All nine candidate carrier components have an explicit evidence status. Source literals bind initial GDP/capital to `MU_10WAN_YUAN` (10 万元) and population to `NU_100_PERSONS` (100 人). Dynamic firm output units, effective labor, and both wage objects require stated assumptions or remain `UNRESOLVED`; the report does not silently call the observed levels unit authority.
- The receipt preserves C4/C5/C6 as distinct, sealed inputs and separates level ranges and float64 ULP from economic scales and outer-map error bounds. Independent C6 checks confirm 3 enterprise wages at the lower bound, 25 at the upper bound, and 3 interior; `Kt_prev==Kt0` bitwise for 30/31 provinces; the reported `Lt/N` range agrees with the sealed 31 rows. These are descriptive facts, not convergence evidence.
- The static JSON/NPZ bit-value checks and share-column residuals cover stored representation. Accepted turn5/6 HJB/KFE, direct-solve and capital-identity gates cover their own legality. None is a same-frozen-state repeated evaluation or a propagated error bound for the nine-component outer map. The receipt correctly marks the outer noise floor `UNAVAILABLE` and all nine outer tolerances `UNRESOLVED`.
- The report flags the earlier design's ambiguous Chinese gloss for MU and the unresolved labor/population and wage scales for later decision. It proposes no numerical tolerance and makes no turn7, fixed-point, GE, or Results claim.
- The literal call ledger is zero for household, HJB, KFE, integration, firm, network, GE, turn7, other science and retries. No source, sealed result, or numerical file was changed.

## Boundary and next gate

This ACCEPT covers evidence quality only. Owner must still decide the carrier and its economic precision target, scales, zero-near-zero rule, tolerances, stopping count, maximum turns, call ceilings, and failure behavior before a scientific execution task can exist. A future same-frozen-state repeat would require a separate explicit model-call budget. The project remains at `Results eligibility=FALSE`.
