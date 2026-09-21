# CH5 MP4C K1B turn4 Anhui F0364 positive-domain-intersection repair, historical parity, and reexecution report

Date: 2026-09-21

Task: `CH5_MP4C_K1B_TURN4_ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR_HISTORICAL_PARITY_AND_REEXECUTION_20260921`

## Terminal

`PASS__ANHUI_F0364_POSITIVE_DOMAIN_INTERSECTION_REPAIR__HISTORICAL_POLICY_PARITY_PASS__K1B_TURN4_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN5_K1B_INPUT_READY__TURN5_NOT_RUN`

The narrow selector repair passed focused parity, all 1,227 historical policy-map identities, 31 fresh turn4 household/KFE blocks, and exactly one frozen-share K1B/C1 integration. Deterministic turn5 share, payoff, and input artifacts were prepared. Turn5 household was not run.

Results eligibility remains `FALSE`. `CURRENT` was not modified and no successor was published.

## Authority and source binding

- Live-main baseline: `1843bd413ee019b04c6937abd1e89cf044e62241`.
- Pre-repair selector blob: `e8a1d72e23661576f14ac42b7dff6e3001837206`.
- Turn4 input blob: `ee779174c614980a0e6182d710ea5aaec8afb6f5`.
- Turn4 input SHA-256: `35CA47135CF3B17ADACDD6C39FBA30CC0E55AE1C103C5F42064D6722AF28310C`.
- Entering `rah` SHA-256: `7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.
- Frozen share-plan blob: `a37647bb68ed1bec6259071d7035f8de07591c9f`.
- Frozen share-plan SHA-256: `41B7DDA4DE2C33C6EADFAB3F324C3592D119B0E91DC7AE8E23968653A881522A`.
- Frozen turn4 `S_K1B` SHA-256: `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.
- No failed-run warm start was used.

## Production change

The only production file changed is `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`.

Within `_interior_a_switching_candidate`, the repair applies only when the liquid node is interior and the finite nonzero D3 ratio is negative. It preserves the complete sorted mapped `q_b` interval, intersects admissibility with the open domain `q_b>0` through branch-local membership, requires finite positive branch-local `p_b`, and checks `q_a=R*p_b` against the original closed illiquid derivative interval. The admitted branch then follows the existing direction, D3 KKT, finite, D2, deduplication, Hamiltonian, and tie rules.

Positive-ratio behavior, ratio-zero fail-closed behavior, active liquid-face negative-ratio behavior, strict crossing, D1/D2/D3, liquid-Z and joint switching, lower-a zero-kink, grid, Delta, solver, tolerances, and calibration are unchanged.

## Focused selector parity

Focused selector tests: 5/5 PASS. The combined related regression set: 14/14 PASS.

### Anhui F0364

- Unique selected branch: negative transfer, backward liquid, zero/switching illiquid.
- `q_b=0.0015039676061569449`.
- `q_a=-0.0005008835855672058`.
- `d=-5.840722762648187`.
- `g_a=0`.
- `g_b=-17.978717494437753`.
- Hamiltonian: `-0.06734914681687235`.
- Interior-b switching root calls: 0.
- Raw transfer KKT residual: `1.0842021724855044e-19`.
- Existing arithmetic tolerance: `1.1564470160853633e-12`.
- KKT gate: PASS.

The task's mathematical target writes the KKT residual as zero. Frozen production floating-point operation order represents it as the one-ulp-scale value above; no cost or KKT arithmetic was changed to force a displayed zero.

The fresh runtime reached the same checkpoint-4 cell and derivatives. Its normal selector call selected the same candidate. The in-path receipt records `no_additional_selector_call=true`.

### Prior Beijing F0364

- `q_b=0.006091715618507631`.
- `q_a=-0.0045978913784868415`.
- `d=-7.8384208979658965`.
- `g_a=0`.
- `g_b=-4.227123020026542`.
- KKT residual: `0`.
- Hamiltonian: `-0.11188508398929994`.
- Root calls: 0.

Positive-ratio focused cases, active-liquid-face negative-ratio cases, and ratio-zero fail-closed cases all passed unchanged-behavior tests.

## Mandatory historical policy identity replay

| Accepted path | Maps | Exact matches | Mismatches |
|---|---:|---:|---:|
| Turn1 run004 | 408 | 408 | 0 |
| Turn2 run005 | 411 | 411 | 0 |
| Turn3 accepted | 408 | 408 | 0 |
| **Total** | **1,227** | **1,227** | **0** |

- Selector evaluations: `981600`.
- Accepted ordered digest: `31C7D784B2AB023E115DB40E1F74003D2FF91572877CD50F26B116BDBC37848B`.
- Replayed ordered digest: `31C7D784B2AB023E115DB40E1F74003D2FF91572877CD50F26B116BDBC37848B`.
- Scalar roots: `413039`.
- Interior-Z roots: `85155`.
- Interior-a switching roots: `392`.
- Joint switching roots: `49`.
- HJB direct solve/update, D2/Q, KFE/SVD, aggregate/integration, retry/tuning: all `0` during historical replay.

## Fresh turn4 household and KFE

All 31 provinces passed the frozen HJB convergence law and unique-closed-class terminal KFE gate. Maximum terminal `B` was `3.5233607698081926e-11`; maximum terminal `D` was `3.523143110584215e-08`.

- Source-native initializations: `31`.
- Scalar labor roots attempted/returned: `24800/24800`.
- Corrected policy maps and D2/Q assemblies: `409/409`.
- Selector evaluations: `327200`.
- Direct HJB updates: `378`.
- SCC, restricted GESVD, normalized stationary candidates, full-Q checks: `31/31/31/31`.
- Full-space 800x800 GESVD: `0`.
- Scientific retries and solver substitutions: `0/0`.

The accepted monotonicity-preserving relaxation helper was called `378` times. It accepted `alpha=1` on 374 updates and `alpha=0.5` on 4 updates, evaluating 382 alpha candidates. There was no exhaustion. The minimum accepted raw b slope across provinces was `0.00026126022961525663` in Guangxi.

## Exactly one turn4 integration and turn5 preparation

The 31/31 household gate opened exactly one integration:

- Household batch: `1`.
- Source-faithful labor: `1`.
- Frozen turn4 K1B quantity allocation: `1`.
- C1 residual `GovInv`: `1`.
- Firm evaluations: `31`.
- Wage, monetary, and fiscal batches: `1/1/1`.
- Completed-turn4 raw `ra0` vectors: `1`.
- Same-turn share recomputation: `0`.

Integration checks passed for frozen-share identity, origin-column conservation, home retention, nonnegative finite shares, national private capital, C1 residual construction, and lagged payoff timing.

- Completed-turn4 raw `ra0` SHA-256: `0312EBE6C2764DB3A834F1233712186ED1B6CE0C3E8BC01E58EFF6A0E8DCD267`.
- Frozen turn4 share SHA-256 used by integration: `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.
- Turn5 raw-ra0 population mean: `0.5190899802806576`.
- Turn5 raw-ra0 population standard deviation: `0.1915047411123845`.
- Turn5 z-score SHA-256: `2B8B8543BF810BF92BF32EBE1CD43DD72FD4D686BFFAF27D9E3054C92ECE7D24`.
- Turn5 foreign conditional-share SHA-256: `D22CD9F936909DF74D3E322ED32F39F680D5FDD15B1044F073BE4C5A2A1779B8`.
- Turn5 portfolio-share SHA-256: `2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06`.
- Turn5 household `rah` SHA-256: `5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E`.
- Turn5 input-candidate file SHA-256: `10CDFE998FBC95F09DA682F5389F268A1569A5FEB345D61470B3E8AA415D01D1`.
- Turn5 household calls: `0`.

The turn3-versus-turn4 panel is descriptive only. It records 377 versus 378 direct updates, raw-ra0 changes in all 31 provinces, and changed foreign shares; no direction or improvement is an acceptance condition.

## Scientific boundary ledger

- K2 calls: `0`.
- MATLAB calls: `0`.
- GE, annual, shock, IRF, welfare, and Results calls: `0`.
- Adaptive controller, clipping, artificial diffusion, alternate continuation: `0`.
- Turn5 household: `0`.
- Retry/tuning: `0`.

## Evidence integrity

- Evidence root: `reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001/`.
- Sealed manifest entries: `4748`.
- Sealed bytes: `64640636`.
- Manifest SHA-256: `1C4F6BB5423471F126B0670BBC48A486CAE2B25ECC8B79B944C8827D29D4F93B`.
- Independent readback: PASS.
- Readback bad paths: `0`.
- Readback scientific calls: `0`.

## Boundary

The task stops before turn5 household. It does not authorize K2, MATLAB, GE, Results, a long outer path, `CURRENT` modification, main merge, or successor publication.
