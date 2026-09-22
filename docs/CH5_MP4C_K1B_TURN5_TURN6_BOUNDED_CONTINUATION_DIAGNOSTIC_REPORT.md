# CH5 MP4C K1B turn5-turn6 bounded continuation diagnostic report

Date: 2026-09-22

Task: `CH5_MP4C_K1B_TURN5_TURN6_BOUNDED_CONTINUATION_DIAGNOSTIC_20260921`

## Terminal

`PASS__K1B_TURN5_TURN6_BOUNDED_CONTINUATION__TWO_TURNS_31_PROVINCE_HJB_KFE_AND_INTEGRATION_PASS__TURN7_INPUT_READY__TURN7_NOT_RUN`

Turn5 and turn6 each completed 31-province corrected household HJB/KFE and exactly one frozen-share K1B/C1 integration. The turn6 entering bundle was sealed before turn6 household execution. The deterministic turn7 K1B share, payoff, and input bundle is ready; turn7 household was not run.

This is a bounded trajectory diagnostic. Results eligibility remains `FALSE`; no convergence or steady-state claim is made. `CURRENT` was not modified and no successor was published.

## Authority and input binding

- Fresh live-main baseline and execution HEAD: `dd90f41e0daa97cf55fcb2a7a233ee8cd64297ac`.
- Baseline tree: `c9003aafe962043a74154459290d77f603029eaa`.
- Turn5 input Git blob: `7826691387916254ef55b149651d51f8438cab10`.
- Turn5 input file SHA-256: `10CDFE998FBC95F09DA682F5389F268A1569A5FEB345D61470B3E8AA415D01D1`.
- Turn5 entering `rah` SHA-256: `5CAF9166D85198E6923FFCD5A1F92D278C8A1C6CB924E8DD1B843F875E91D88E`.
- Turn5 frozen-plan Git blob: `83cee2bafb63d5f608e9d1b76480621a14077cc3`.
- Turn5 frozen-plan file SHA-256: `57A31EAA59A9E6CCD74E1DD5C18C74496829BA181866E12300CA7EB202890A70`.
- Turn5 frozen `S_K1B` SHA-256: `2BDF7B8226C8404DB9C7FFEEE3F72F7AE9CA1305905460A4E2430AABEA4D3B06`.
- Input blob, file, `rah`, prior raw-ra0, share identity, shape, finiteness, nonnegativity, and column checks: PASS.
- Source-native initialization was used for every province; no warm start was used.

The preflight verified exact live main and an empty production-source diff. SHA-256 values for all 65 files under `src/ch5_two_asset_hank/**` were frozen before execution and matched exactly after execution. Production source changes are zero.

## Turn5 household and KFE

All 31 provinces passed the frozen HJB convergence law and unique-closed-class KFE gate.

- Source-native initializations: `31`.
- Scalar labor roots attempted/returned: `24800/24800`.
- Corrected policy maps and D2/Q assemblies: `409/409`.
- Selector evaluations: `327200`.
- Direct HJB updates and post-update checkpoints: `378/378`.
- Terminal checkpoints per province: minimum `11`, maximum `13`, total `378`.
- Maximum terminal `B`: `3.5289673960825496e-11`.
- Maximum terminal `D`: `3.5288722166626485e-08`.
- SCC decompositions, restricted GESVD, normalized stationary candidates, and full-Q checks: `31/31/31/31`.
- Full-space 800x800 GESVD: `0`.
- Scientific retries and solver substitutions: `0/0`.

## Turn5 integration and sealed turn6 entry

The 31/31 gate opened exactly one integration:

- Household batch, source-faithful labor, frozen K1B allocation, and C1 construction: `1/1/1/1`.
- Firm evaluations: `31`.
- Wage, monetary, and fiscal batches: `1/1/1`.
- Completed-turn5 raw-ra0 vector: `1`.
- Same-turn share recomputation: `0`.

All frozen-share, origin-column, home-retention, national-capital, C1, finite-payoff, and lagged-timing checks passed. Origin private wealth and destination private capital were both `140310000.0`; the national private-capital residual was `0.0`. C1 total `GovInv` was `2341682906.9005513`.

- Completed-turn5 raw `ra0` SHA-256: `D4046E8A6C95B222506C585822EA0F907DE7DFDA5CECA317393CCA4E7D297E8B`.
- Turn6 raw-ra0 population mean/std: `0.5191670168708853` / `0.19163925522950678` (`ddof=0`).
- Turn6 z-score SHA-256: `8E79D143A32A942B10CF61A91C92989D98B4327B18447DA2D41169B63DE29A1A`.
- Turn6 foreign conditional-share SHA-256: `E03BA232EB6441970F1CE45D73242A8AC0677A094412463201C9FC1914540C50`.
- Turn6 portfolio-share SHA-256: `D11CD1AD944FD04FE144DEB84BDFD2DCC93CC1B7D397B7052025C2A7D1B02435`.
- Turn6 `rah` SHA-256: `6E3EEFD0EA6920C6BCFCF70D2E06589B6388FB98C2A2A67504493F9B2A212313`.
- Turn6 input-candidate file SHA-256: `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC`.
- Turn6 frozen-plan file SHA-256: `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34`.
- Turn6 entering manifest: 4 entries / 94,728 bytes; manifest SHA-256 `A744A88E26BAF2408CBE2DC94B35908438F02E8B8FACA7A71B1F136AA03AC471`.
- The turn6 bundle was sealed before household execution; independent readback PASS with zero scientific calls.

## Turn6 household and KFE

All 31 provinces passed the same frozen HJB/KFE laws using only the sealed turn6 entry.

- Source-native initializations: `31`.
- Scalar labor roots attempted/returned: `24800/24800`.
- Corrected policy maps and D2/Q assemblies: `409/409`.
- Selector evaluations: `327200`.
- Direct HJB updates and post-update checkpoints: `378/378`.
- Terminal checkpoints per province: minimum `11`, maximum `13`, total `378`.
- Maximum terminal `B`: `3.529293524096033e-11`.
- Maximum terminal `D`: `3.529515701927721e-08`.
- SCC decompositions, restricted GESVD, normalized stationary candidates, and full-Q checks: `31/31/31/31`.
- Full-space 800x800 GESVD: `0`.
- Scientific retries and solver substitutions: `0/0`.

## Turn6 integration and turn7 preparation

The turn6 31/31 gate opened exactly one integration with the same sealed turn6 `S_K1B`:

- Household batch, source-faithful labor, frozen K1B allocation, and C1 construction: `1/1/1/1`.
- Firm evaluations: `31`.
- Wage, monetary, and fiscal batches: `1/1/1`.
- Completed-turn6 raw-ra0 vector: `1`.
- Same-turn share recomputation: `0`.

All integration checks passed. Origin private wealth was `140310000.0`, destination private capital was `140310000.00000003`, and the arithmetic conservation residual was `2.9802322387695312e-08`. C1 total `GovInv` was `2341682906.900551`.

- Completed-turn6 raw `ra0` SHA-256: `1A469B1557617F2E517B41A440A4A190F763B6503BB23959378406B3ACDF01B5`.
- Turn7 raw-ra0 population mean/std: `0.5191797648162301` / `0.19166394507681306` (`ddof=0`).
- Turn7 z-score SHA-256: `88914FBDCAE647F956842EC1CAD4E6911A5F3A3084C8A9A76A8122249871A69F`.
- Turn7 foreign conditional-share SHA-256: `C72AD8E2A038F4F5F39370CEF391C1039A9D813E0D31B0C436F7B0E1B542FEE1`.
- Turn7 portfolio-share SHA-256: `8799C525E7BB5A4943D6028C376FF595BA111C4E5EDF5A7C03049A9494DBC99A`.
- Turn7 `rah` SHA-256: `2B0A8B967CB7334DD38DB33951EE1E70B4404980C1DE9C763B41238233FFA11D`.
- Turn7 input-candidate file SHA-256: `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`.
- Turn7 frozen-plan file SHA-256: `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E`.
- Turn7 entering manifest: 4 entries / 94,730 bytes; manifest SHA-256 `1C837CBFD6262569DDAA899958F5877E703B7FE76222EB77DA9E55D23BA8C869`.
- Turn7 bundle readback: PASS with zero scientific calls.
- Turn7 household calls: `0`.

## Monotonicity-preserving relaxation

Across both turns, the adopted helper was invoked once after each of the `756` full implicit solves. It evaluated `764` alpha candidates:

- `alpha=1`: `748` accepted updates.
- `alpha=0.5`: `8` accepted updates.
- Smaller accepted alpha: `0`.
- Exhaustion: none.
- Every accepted state retained 760 finite, strictly positive raw liquid slopes and was not bitwise stagnant.

No relaxation event triggered a second solve. No derivative floor, clipping, adaptive Delta, alternate alpha schedule, or solver substitution was used.

## Combined scientific ledger

| Item | Turn5 | Turn6 | Combined |
|---|---:|---:|---:|
| Source-native initializations | 31 | 31 | 62 |
| Policy maps / D2-Q | 409 | 409 | 818 |
| Selector evaluations | 327200 | 327200 | 654400 |
| Direct HJB updates | 378 | 378 | 756 |
| SCC / restricted GESVD / stationary / full-Q | 31 each | 31 each | 62 each |
| Aggregates / firms | 31 / 31 | 31 / 31 | 62 / 62 |
| Household / labor / K1B / C1 / wage / monetary / fiscal | 1 each | 1 each | 2 each |
| Raw-ra0 / next-turn K1B preparation | 1 / 1 | 1 / 1 | 2 / 2 |

Combined ledger breaches: none. Full-space GESVD, K1A allocation, adaptive controller, artificial diffusion, clipping, smoothing/rescaling, scientific retry, solver substitution, K2, MATLAB, GE/annual/shock/IRF/welfare/Results, and turn7 household were all `0`.

## Turn3-through-turn6 trajectory diagnostic

Classification for every transition and every successive ratio:

`DESCRIPTIVE_ONLY__NO_CONTRACTION_OR_CONVERGENCE_ACCEPTANCE_CONDITION`

The panel sets `fixed_point_tolerance=null`, `convergence_claim=false`, and acceptance condition `NONE__BOUNDED_TRAJECTORY_DIAGNOSTIC_ONLY`.

| Transition | raw ra0 max / L2 | rah max / L2 | S max / Frobenius | new z mean / pop SD | updates old -> new | provinces with checkpoint change | new C1 total | new capital residual |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| turn3 -> turn4 | `0.004025704005734321 / 0.005510286646555688` | `0.003565201539826868 / 0.005161781998611691` | `0.0001708967297973651 / 0.0002936100333500836` | `0.5190899802806576 / 0.1915047411123845` | `377 -> 378` | 4 | `2341682906.900551` | `2.9802322387695312e-08` |
| turn4 -> turn5 | `0.0007664942733158764 / 0.0009829144959085849` | `0.0006755443013624074 / 0.0009075749448952141` | `0.000038570139761919 / 0.000065412076402559` | `0.5191670168708853 / 0.1916392552295068` | `378 -> 378` | 0 | `2341682906.9005513` | `0` |
| turn5 -> turn6 | `0.0001468810847089497 / 0.0001819817043498871` | `0.0001290310060115818 / 0.0001667695790141566` | `0.000008122347528478 / 0.000013640143450284` | `0.5191797648162301 / 0.1916639450768131` | `378 -> 378` | 0 | `2341682906.900551` | `2.9802322387695312e-08` |

For the requested aggregate panel, the turn5 -> turn6 maximum absolute / mean signed changes were:

| Variable | Maximum absolute change | Mean signed change |
|---|---:|---:|
| `Ct` | `0.004077179613416249` | `-0.0002712555345231218` |
| `Lt` (`Lt_supply`) | `263.9059808589518` | `26.6608903000672` |
| `At` | `0` | `0` |
| `Bt` | `0.0001770851721296651` | `0.00001090810806307048` |
| `AtTax` | `0.0006755443013624074` | `0.0000889860310105209` |
| `Kt` | `2.9802322387695312e-08` | `1.20170654789094e-09` |
| `Kt_supply` | `830.6433400935493` | `1.4270265256204913e-10` |
| `GovInv` | `830.6433400958776` | `-9.01279910918205e-11` |
| `Yt` | `202.4450707733631` | `70.253999025621` |
| `w` | `0.00005559990870906972` | `0.00001554917918391144` |

All three transitions, all requested state series, their complete SHA identities, and their maximum, mean, and Euclidean changes are preserved in `turn3_through_turn6_trajectory_diagnostic.json`.

Successive L2 change ratios from turn4 -> turn5 relative to turn3 -> turn4, followed by turn5 -> turn6 relative to turn4 -> turn5, include:

| Series | First ratio | Second ratio |
|---|---:|---:|
| raw `ra0` | `0.17837810606876045` | `0.18514500000497722` |
| `rah` | `0.17582589600632392` | `0.1837529561081166` |
| portfolio shares | `0.2227855623876619` | `0.2085263792321792` |
| `Ct` | `0.1768353519258731` | `0.19231071917593315` |
| `Lt` | `0.14851819799796928` | `0.17470356140808738` |
| `Kt_supply` | `0.2293932632629588` | `0.22201513915977006` |
| `GovInv` | `0.2293932632630664` | `0.22201513916106544` |
| `Yt` | `0.10317728078043963` | `0.2643689764923893` |
| `w` | `0.068444749632349` | `0.24550176477875868` |

These ratios are descriptions of three bounded transitions only. They are not a contraction test, convergence gate, fixed-point tolerance, or Results claim.

## Tests and evidence integrity

- Focused tests: `5 passed`, failures `0`, errors `0`.
- Validator and focused test `py_compile`: PASS.
- Evidence root: `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/`.
- Sealed manifest entries: `9470`.
- Sealed bytes: `127796794`.
- Manifest SHA-256: `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127`.
- Independent full readback: PASS.
- Readback bad paths: `0`.
- Readback scientific calls: `0`.

## Boundary

The task stops before turn7 household. It does not authorize K2, MATLAB, GE, Results, annual dynamics, shocks, IRFs, welfare, a long outer path, `CURRENT` modification, main merge, or successor publication.
