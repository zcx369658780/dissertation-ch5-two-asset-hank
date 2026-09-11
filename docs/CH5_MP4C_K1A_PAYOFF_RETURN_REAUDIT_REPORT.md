# Chapter 5 MP4C K1A payoff-return re-audit

Date: 2026-09-12.

## Outcome

Classification:

`CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_IS_SOURCE_CONSISTENT_CANDIDATE_REQUIRING_OWNER_PERIOD_NUMERAIRE_FREEZE`

The accepted K1A evidence confirms that raw `ra0` is the source-computed net firm return, while used `ra` is that object clipped to the historical `[.02,.09]` safeguard. K1A aggregates the source-used return through the same destination-by-origin portfolio matrix `S` that allocates quantities. The clip removes almost all observed cross-province payoff information: `754/775` Path-A and `755/775` Path-B province-turns are upper-clipped, with 30 provinces clipped in every turn. Raw `ra0` is therefore a source-consistent payoff candidate, but its calendar period and absolute economic numeraire remain unresolved and its observed magnitude creates material runtime risk. This audit does not authorize changing the payoff law.

The only recommended next gate is an **Owner/Reviewer payoff-return contract freeze**. If the Owner selects raw `ra0`, a fresh exact task must separately design a bounded runtime-safety diagnostic. Builder must not run that diagnostic, K1B, K2 or any successor from this classification.

Results eligibility remains `FALSE`.

## Authority and evidence identity

- Fresh live-main baseline: `9cf0a2bb0dc6994a1f9670eb78b30c684aad35fe`.
- Accepted symmetric-rerun candidate: `ca66dd5d7364f80ed2686d4d2e77a1a6adab2ecb`.
- Accepted input root: `D:\ProjectTemp\ch5-k1a-symmetric-rerun-evidence-20260911-001`.
- Accepted manifest: `DC3FAAD6FD919891F6EEF492B27100265998625907CA76A42F5C6663BE68512D`; `4981/4981` readback `PASS`.
- Final external audit evidence: `D:\ProjectTemp\ch5-k1a-payoff-return-reaudit-evidence-20260912-002`. The earlier `-001` output is preserved as a preliminary pre-hardening package and was not overwritten.
- New `reaudit_summary.json` SHA-256: `8606A4E6BBDC2A225615D1A393D0BE23DD8B8F2F1BDD9EE9B72A321BC5D5FB8B`; six tracked copies matched their external files byte-for-byte.
- Every quantitative input was one of the accepted 50 per-turn observable CSVs or 50 persisted allocation JSONs. The script records all 100 input hashes.

## Source semantics and timing

Firm return production is separate from portfolio aggregation and household consumption:

1. `firm.py:86-110` forms `Yt`, `mt`, `rk = mt*alpha/(Kt/Yt)`, floors `profit=(1-mt)Yt-Thetat` at zero, and computes `ra0 = rk - delta + profit*(1-corptau)/Kt`. The active corrected route supplies `delta=.025` at `validators/multi_province/corrected_2018_hjb_propagation_25turn_kl/run.py:419-421`. The `.025` term is a fixed model-period depreciation deduction; the source does not establish that the model period is annual.
2. `firm.py:112-125` clips `ra0` to `[ramin,ramax]` and records the excess/shortfall in corporate tax. The resulting `ra` is the source-used firm return.
3. Legacy `capital_allocation.py:83-108` takes entering `old_firm_return_ra`, supplied from `province["ra"]` at `one_turn.py:212-217`, and constructs its historical own-plus-foreign `rah` expression. This file remains byte-unchanged, but the active K1A route replaces that allocation result through its selectable adapter; K1A does **not** use the legacy `rah` weighting law.
4. The K1A adapter passes the same entering used-`ra` vector as `portfolio_return_by_destination` (`k1a_runtime_adapter.py:108-127`). `capital_network.py:289-312` constructs full portfolio shares and calculates `rah = return_by_destination @ S_destination_origin`; lines 328-342 return the same `S` for quantities and payoff.
5. The active K1A runner's `k1a_rah_provenance` (`validators/multi_province/k1a_equal_share_vs_beta2/run.py:381-397`) requires the prior completed K1A network, rebuilds entering `rah` from `household_portfolio_return_by_origin`, records the formula `current_source_used_ra_by_destination @ S_destination_origin`, and validates `quantity_and_rah_same_S=True`. Lines 399-405 install the K1A allocator and replace the generic provenance hook for this run.
6. `steady_state.py:147-167` writes the network-produced `rah` into post-turn state. At the next turn, `g1_residual_govinv_25turn_isolated/run.py:397-408` starts the household pass and lines 185-190 pass state `rah` as HJB `r_a`. `exports/matlab_faithful_two_asset_ha.py:111-124` then applies the accepted finite-grid illiquid-return taper.

The persisted timing check is explicit. Allocation `n` contains the entering, lagged payoff; turn `n` then produces new firm returns. For turns 1-24 the audit verified that the same `S` persisted at allocation `n+1` and that `S' * used_ra_n` equals the next allocation's persisted household payoff within `1e-12`. Turn 25 has no next allocation because the authorized ceiling was reached, so its next-allocation validation is truthfully `NOT_AVAILABLE_AUTHORIZED_CEILING`; its same-`S` arithmetic remains available without feedback.

## Units, periodicity and numeraire

Data scale and return periodicity are distinct. Corrected-2018 retains `MU=10万元` and `NU=100 persons`; this does not identify a return calendar.

| Object | Source meaning | Authority classification | Period / numeraire finding |
|---|---|---|---|
| `Y` | firm production-output level | `SOURCE_CONFIRMED` formula; macro scale `DERIVED_FROM_FROZEN_DATA_CONTRACT` | Implied macro MU level; calendar period and common price-level mapping remain `UNRESOLVED`. |
| `Ktarget` | corrected-2018 capital target level | `SOURCE_CONFIRMED` frozen data contract | MU; an empirical capital level, not a return-period authority. |
| `Kprivate` | `sum_i S[j,i] A_i N_i` | `DERIVED_FROM_FROZEN_DATA_CONTRACT` | MU under the accepted K1 contract. |
| `GovInv` | `max(Ktarget-Kprivate,0)` residual public productive asset | `DERIVED_FROM_FROZEN_DATA_CONTRACT` | MU; not a return controller. |
| firm total `K` | `Kprivate+GovInv` in this route | `DERIVED_FROM_FROZEN_DATA_CONTRACT` | MU; approximately equal to target by C1 accounting. |
| `ra0` | `rk + after-tax profit/K - delta` | `SOURCE_CONFIRMED` net computed rate-like object | Algebraically dimensionless; annual/quarterly/other period and empirical price numeraire are `UNRESOLVED`. |
| used `ra` | clipped `ra0` | `SOURCE_CONFIRMED` runtime object | Inherits unresolved period/numeraire. `[.02,.09]` remains `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economic interval. |
| `rah` | portfolio-weighted used `ra` | `SOURCE_CONFIRMED` aggregation | Same rate-like scale as input payoff; period and final economic authority remain `UNRESOLVED`. |
| `rb` | liquid-return coefficient passed to HJB as `r_b` | `SOURCE_CONFIRMED` runtime rate-like input | Calendar period, gross/net naming authority and empirical numeraire remain `UNRESOLVED`. |
| wage | firm marginal-product wage and a separate household composite | formula `SOURCE_CONFIRMED`; absolute mapping `UNRESOLVED` | Raw firm wage has implied MU/NU per model period. Used wage bounds have unresolved economic unit; household `w` is a nonlinear, unnormalized cross-destination composite and is not directly comparable to one firm wage. |

No inspected source supports annualizing, smoothing, risk-adjusting, normalizing or replacing the payoff cap.

## Clipping distortion

Pooled accepted evidence:

| Metric | Path A: equal share | Path B: geographic beta=2 |
|---|---:|---:|
| upper clips | 754/775 = 0.972903 | 755/775 = 0.974194 |
| lower clips | 0/775 | 0/775 |
| raw `ra0` min / mean / median / max | 0.087829 / 0.277625 / 0.263115 / 1.126705 | 0.087836 / 0.277641 / 0.263097 / 1.124451 |
| used `ra` min / mean / median / max | 0.087829 / 0.089945 / 0.09 / 0.09 | 0.087836 / 0.089945 / 0.09 / 0.09 |
| gap `ra0-ra` median / mean / p95 / p99 / max | 0.173115 / 0.187680 / 0.500108 / 0.699983 / 1.036705 | 0.173097 / 0.187696 / 0.499401 / 0.699013 / 1.034451 |

Pooled raw percentiles `p1/p5/p25/p50/p75/p95/p99` are:

- A: `0.0878369 / 0.0966336 / 0.184252 / 0.263115 / 0.328945 / 0.590108 / 0.789983`.
- B: `0.0878433 / 0.0967833 / 0.184265 / 0.263097 / 0.328315 / 0.589401 / 0.789013`.

The corresponding used-return percentiles are `p1≈0.08784` and `.09` at every percentile from `p5` through `p99` for both paths.

Across turns, raw cross-sectional standard deviation ranges are `0.081725-0.198285` (A) and `0.081707-0.197885` (B), while used-return standard deviation ranges are `0-0.0003836` and `0-0.0003823`. Each turn has only 1 or 2 unique used-return values; the share exactly at `.09` is `0.967742-1`. When used returns are not constant, raw-versus-used Spearman is only `0.306186`; it is undefined in 4 A turns and 5 B turns because all 31 used values are identical. Thus the clip preserves at most the identity of the lone low-return province and destroys the ordering among the remaining tied provinces.

Thirty provinces are upper-clipped in all 25 turns. Qinghai is the only exception: 4/25 turns in A and 5/25 in B. By contrast, A-versus-B raw-return ranking is almost unchanged: same-turn Spearman min/mean/max is `0.999194 / 0.999968 / 1`. Geographic beta=2 therefore does not materially change raw-return ranking, dispersion or clipping information loss in this bounded evidence.

## Raw-return decomposition — descriptive, not causal

The exact active identity is `ra0 = rk + after_tax_profit_over_K - delta`. Maximum persisted reconstruction residual is `5.551115123125783e-17` in each path. Implied `delta` has mean `0.02500000000000001` and standard deviation about `1.66e-17`, i.e. `.025` up to binary64 arithmetic.

| Component | Path A median / mean / max | Path B median / mean / max |
|---|---:|---:|
| `rk` | 0.287481 / 0.301392 / 1.151705 | 0.286344 / 0.301412 / 1.149451 |
| profit/K | 0 / 0.001645 / 0.102688 | 0 / 0.001639 / 0.102474 |
| after-tax profit/K | 0 / 0.001234 / 0.077016 | 0 / 0.001229 / 0.076856 |
| depreciation deduction | 0.025 / 0.025 / 0.025 | 0.025 / 0.025 / 0.025 |

Pooled Pearson correlations with raw `ra0` are descriptive only:

- `rk`: `0.999127 / 0.999129` (A/B);
- after-tax profit/K: `-0.09396 / -0.09428`;
- private K/target: `0.149998 / 0.186160`;
- Y/total K: `0.997608 / 0.997611`.

Total K/target is approximately one by the frozen C1 identity, so its tiny floating-point variation makes its reported correlation (`-0.0177/-0.0068`) economically uninformative. These associations do not identify causal effects and do not authorize parameter changes.

## STATIC_NO_FEEDBACK_COUNTERFACTUAL

For each persisted completed turn, the audit holds that turn's accepted `S` fixed and computes `S' * ra0` versus `S' * used_ra`. It does not feed either counterfactual into HJB, KFE, firm, capital allocation or another iteration.

| Difference `S'ra0 - S'ra_used` | Path A | Path B |
|---|---:|---:|
| median | 0.172004 | 0.172596 |
| mean | 0.189549 | 0.189797 |
| p95 | 0.496142 | 0.496009 |
| max | 0.952995 | 0.947811 |

The largest province-level 25-turn median differences are Beijing (`0.291470/0.290699` A/B), Shanghai (`0.277851/0.280113`), Guangdong (`0.275530/0.276302`), Anhui (`0.249600/0.249811`) and Zhejiang (`0.228695/0.230276`). Matched B-minus-A static differences have min/median/mean/p95/max `-0.005532 / 0.000389 / 0.000249 / 0.002037 / 0.002842`. The raw-payoff level effect is therefore large relative to the clipped bridge, while the A/B difference is small. This is arithmetic only and says nothing about convergence of a raw-payoff trajectory.

## Candidate payoff contracts

| Candidate | Source fidelity / interpretation | Dispersion | Current HJB interface | Numerical risk | Owner / calibration need |
|---|---|---|---|---|---|
| A. current clipped used `ra` | Exact current runtime bridge, but the interval is a numerical safeguard rather than an identified economic return range | Almost none in accepted K1A evidence | Already compatible | Historically bounded; scientific information loss is severe | Owner required for any claim beyond transitional use; no evidence supports treating the bounds as calibration |
| B. raw net `ra0` | Exact source pre-clip firm object: MPK-like `rk` plus after-tax profit/K minus depreciation | Preserves observed cross-province ranking and dispersion | Scalar rate-like shape is compatible, but switching changes model semantics | High: observed max about 1.13 and static payoff differences up to about .95; runtime behavior untested | Owner must freeze period/numeraire and payoff meaning; then a new bounded safety task is required |
| C. transformed / expected return | No source-backed payoff transformation was found | Not evaluable | Not authorized | Not evaluable | New scientific contract and calibration/estimation would be required |
| D. other documented payoff object | No dissertation/source object with existing authority to replace `rah` was found | Not evaluable | Not authorized | Not evaluable | Additional authority required |

The future K1B z-scored raw-`ra0` signal is excluded: it is authorized only for destination attractiveness and is not a payoff return. `beta_return=.5` remains preregistered but runtime-unauthorized.

## Zero-science verification and boundary

The audit script uses only the Python standard library and imports no project/model module. Final focused tests: `5 passed`, including tamper rejection for a used return that is not the exact source clip and for a CSV lagged payoff that disagrees with its current persisted allocation. The final audit parsed only persisted files and produced six receipts. Two earlier engineering parses failed closed before creating an output root: first on the accepted CSV BOM, then on detecting the lagged-versus-current payoff timing mismatch; both were corrected with focused tests. The successful `-001` package was then preserved, and the hardened final script produced the new non-overwriting `-002` package.

New scientific/model call ledger for this task:

| HJB | KFE | household | firm runtime | trajectory / outer | steady state | MATLAB | GE | annual | shock/IRF | Results |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

No production-science source, capital network, legacy allocator, firm/HJB/KFE/labor/C1 rule, parameter, bound, grid, tolerance, solver semantic, K1B/K2 route or Results artifact was changed. No successor task is published and main is not merged.
