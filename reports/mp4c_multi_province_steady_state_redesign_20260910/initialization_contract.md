# Initialization contract

## Current source order and overwrite map

`multi_prov_HANK_12sts.m:85-108` copies one generic struct to all 31 provinces. Before the first household call, `mpHANK_equilibrium_2000.m:22-43` overwrites `Zt`, `alpha`, `Kt0`, `Kt`, `N`, `Lt`, `Yt0`, `Yt`, lagged K/L/Y/Z fields, `pcap`, `pgdp`, province name, and `GovInv=Kt0*GovInv_ratio`. It does not overwrite `ra=.09`, `rah=.09`, `wjt=.6`, `w=20`, `At=2`, `Bt=1`, or `Ct=4`. Those values therefore enter the first household/allocation turn; `.09` is already the firm-ra upper bound, and `.6` is below the firm-wage lower bound `.8`.

## Successor sequence

1. Bind an immutable `data_contract_id`, calendar year 2018, province order, the Owner-selected PIM route, `delta_pim=.096`, and source hashes.
2. Convert raw values once to the approved common units. Save raw and converted Y/N/K independently.
3. Save `alpha_raw=.7380939146868483`; apply the Owner bounds once. For the current value, `alpha_used=.7380939146868483`, `clip_flag=false`, `clip_reason=NONE_INSIDE_RANGE`.
4. Set target states: `Y0=Y_2018_model`, `Kt0=K_2018_model`, `Lt0=N_2018_model` as the declared population proxy, and `Zt0=Y0/(Kt0^alpha_used Lt0^(1-alpha_used))`.
5. Initialize source bookkeeping consistently: `Yt=Yt_1=Y0`, `Kt=Kt_1=Kt0`, `Lt=Lt_1=Lt0`, `Zt=Zt_1=Zt0`, and `pit=pit_1`. The zero-change NKPC terms then imply `mt0=mstar=1-1/epsilon=.9` under the current source constants.
6. Derive, without inventing an equation, `raw_wjt0=mt0(1-alpha)Zt0(Kt0/Lt0)^alpha` and the source `raw_ra0=rk0-delta_firm+divrate0`, including current price-adjustment cost, profit floor, corporate tax, and `delta_firm=.025`. Save all intermediate quantities.
7. Apply the unchanged firm safety mappings and tax compensation: `used_wjt0=clip(raw_wjt0,.8,1.3)` and `used_ra0=clip(raw_ra0,.02,.09)`. Save flags and reasons.
8. Obtain `inter_prv_ratio` from the selected 2018 per-capital contract. Use the existing portfolio formula over the full 31-vector of `used_ra0` to produce `rah_composite_raw0`; use the existing wage/migration formula over all `used_wjt0` to produce `w_composite_raw0`.
9. For turn zero, there is no prior data-consistent composite to damp against. Set `rah_household_used0=rah_composite_raw0` and `w_household_used0=w_composite_raw0`, label `INITIAL_COMPOSITE_NO_DAMPING_BASE`, then apply damping only from the first completed update onward.
10. Produce an initialization receipt for all 31 provinces before any household solve. A missing raw/used/composite field fails closed.

Steps 8–10 are `FUTURE_VALIDATION_REQUIRED`: the current task prohibits calling `HANK_firm`, `wage_caculate`, `Lt_seperate`, allocation, or any household/model function. The future probe must be an initialization-only deterministic call budget and must stop before HJB/KFE or an outer turn.

## Capital and GovInv

The production target is total `Kt0`, while the firm consumes `Kt_supply+GovInv`. Exact `Kt_supply0` depends on household illiquid assets, the explicit asset bridge, and the cross-province allocation. Therefore the successor must not repeat `GovInv0=Kt0` and then silently add private supply. After the future initialization-only allocation receipt, use the existing accounting identity to record a proposed residual `GovInv0=Kt0-Kt_supply0`. If it is negative or economically inadmissible, stop for Owner review; do not truncate it silently.

## Static Anhui illustration, not production selection

Using current canonical PIM only as an illustration of the proposed common unit:

| field | value |
| --- | ---: |
| Y0 | 34,010,900 MU |
| N/L0 | 607,600 NU |
| Kt0 | 135,731,410.82013685 MU |
| alpha raw/used | 0.7380939146868483 / 0.7380939146868483 |
| Zt0 | 1.0331694367651485 |
| raw wjt0 | 13.194363905989741 |
| clipped wjt0 | 1.3 |
| raw ra0 | 0.15648760365692777 |
| clipped ra0 | 0.09 |

The double upper-bound hit demonstrates that the source bounds and macro/household wage normalization are not yet reconciled. It must not be “fixed” by choosing another data multiplier.
