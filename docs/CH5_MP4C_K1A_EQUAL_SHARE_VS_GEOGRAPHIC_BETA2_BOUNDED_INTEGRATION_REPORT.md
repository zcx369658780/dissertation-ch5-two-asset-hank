# Chapter 5 MP4C K1A equal-share vs geographic beta=2 bounded integration report

## Outcome

Verdict: `K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_BOUNDED_INTEGRATION_PARTIAL__PATH_A_STOPPED_AFTER_TURN1_ON_LEGACY_VALIDATOR_ASSERTION__PATH_B_COMPLETED_25_TURNS`.

The K1A adapter and all observed capital/C1 accounting gates passed, and Path B completed the authorized 25-turn ceiling. Path A completed turn 1, then stopped at turn-2 entry because the reused G1 validator still asserted the legacy `rah` formula. Because scientific state had advanced, Path A was not retried. The task therefore cannot claim the full two-path bounded-integration PASS; the only direct A/B comparison is the common completed turn 1.

Results eligibility remains `FALSE`. This is a bounded mechanism diagnostic, not a steady state, KFE closure, K1B/K2 result, annual result, IRF, welfare result, or dissertation Results claim.

## Authority and implementation

- Live-main baseline: `386594886bec9e42d3dc18791f7f1be212d3b5c9`.
- Worktree: `D:\ProjectTemp\ch5-k1a-equal-share-vs-beta2-20260911-001`.
- Path A: `beta_distance=0`, `beta_return=0`; Path B: `beta_distance=2`, `beta_return=0`.
- Accepted distance canonical-LF SHA-256: `30401B7754A0126D544D54ABB36C6CB662E3E386663E3110EF3F68E417FDA084`.
- Legacy `capital_allocation.py` remained byte-identical at `BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40` and remains separately callable.
- K1A payoff bridge: `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`. Quantity and `rah` use the same destination-by-origin `S`; lagged-return attractiveness, smoothing, and partial adjustment are off.
- Source-faithful labor remained active; normalized bilateral labor was not selected.
- C1 remained `GovInv=max(Ktarget-Kprivate,0)`.

## Pre-run checks

Focused zero-science tests passed 50/50, compile and diff checks passed, A/B runtime payloads were byte-identical, roots were distinct/no-overwrite, and the two configs differed only in `beta_distance`. Accepted initialization was reused with zero new initialization HJB/KFE solves.

After Path A stopped, a zero-science repair replaced only the task wrapper's legacy `rah` provenance assertion with validation against the prior completed K1A allocation using the same `S`. Path A evidence was preserved and not retried. The repair gate passed the same 50/50 focused tests before Path B started.

## Call ledger

| Item | Path A | Path B | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 1 | 25 | 26 |
| province updates | 31 | 775 | 806 |
| HJB calls | 31 | 775 | 806 |
| HJB direct solves | 1596 | 19836 | 21432 |
| KFE calls | 31 | 775 | 806 |
| KFE direct solves | 31 | 775 | 806 |
| labor-root/Brent calls | 24800 | 620000 | 644800 |

Scientific retries were 0. MATLAB, standalone KFE experiments, K1B, GE, annual, IRF, and Results calls were all 0.

## Capital and C1 accounting

Across the 806 observed province-turn rows, Path A/Path B maximum share-column gaps were `1.3322676295501878e-15` / `3.3306690738754696e-16`; maximum origin-capital residuals were `1.210719347000122e-08` / `3.725290298461914e-09` MU; maximum national conservation residuals were `1.4901161193847656e-08` / `4.470348358154297e-08` MU. Home retention identities passed, quantity/`rah` used the same `S` throughout, and destination-theta double-weighting count was zero.

Path A private K/target min/median/max was `0.01417783318060686 / 0.0460609698890771 / 0.09974948873095775`; Path B pooled was `0.01451147062307415 / 0.04193969784937715 / 0.0993234425547495`. Path B turns 20-25 was `0.01478844149564718 / 0.0419390624277001 / 0.08132349571936068`. `Kprivate>=Ktarget` occurred 0 times in A and 0 times in B; nonzero GovInv among such cases was zero. Private-only overshoot was zero in all observed rows. Total K/target pooled min/median/max was `0.9999999999999999 / 1.0 / 1.0000000000000002` for A and `0.9999999999999998 / 1.0 / 1.0000000000000002` for B; any tiny deviation from one is floating-point accounting noise. Overshoot was not created by GovInv.

## Raw return audit and A/B comparison

Path A observed raw `ra0` min/median/max was `0.2502570646414367 / 0.4763263686225738 / 0.9645303327953562`; Path B pooled was `0.08783627904873736 / 0.26309688368435974 / 1.1244507269044166`. Counts below `.02` / above `.09` were `0 / 31` for A and `0 / 755` for B. Lower/upper clipping counts were `0 / 31` and `0 / 755`. Path B `rk` min/median/max was `0.06684313180646158 / 0.2863443871665985 / 1.1494507269044165` and raw profit/K was `0.0 / 0.0 / 0.10247442189807941`; the active after-tax profit component was `0.0 / 0.0 / 0.07685581642355956`. Maximum `ra0 = rk + after-tax profit/K - delta` reconstruction residual was `5.551115123125783e-17`.

On the only common completed comparison turn (turn 1), B-minus-A private-K/target median was `-0.00012218834694291414`, raw-`ra0` median was `0.0`, and raw-`ra0` cross-sectional standard deviation changed from `0.16654744447723807` to `0.16654744447723807` (delta `0.0`). This supports only a turn-1 mechanism comparison; a 25-turn A/B conclusion is unavailable.

| Turn-1 metric | Path A median | Path B median | B minus A |
|---|---:|---:|---:|
| private K/target | 0.0460609698890771 | 0.04593878154213418 | -0.00012218834694291414 |
| GovInv/target | 0.9539390301109228 | 0.9540612184578658 | 0.0001221883469429974 |
| total K/target | 1.0 | 1.0 | 0.0 |
| raw `ra0` | 0.4763263686225738 | 0.4763263686225738 | 0.0 |
| used `ra` | 0.09 | 0.09 | 0.0 |
| entering household `rah` | 0.08488059053640952 | 0.08488059053640952 | 0.0 |
| K1A network-produced `rah` | 0.08999627356269584 | 0.08999741539645487 | 1.1418337590302086e-06 |
| output Y | 45590499.75519855 | 45590499.75519855 | 0.0 |
| used wage | 1.3 | 1.3 | 0.0 |
| nk gap | 3.0932046513694003 | 3.0932046513694003 | 0.0 |
| yt gap | 0.9988299299081169 | 0.9988299299081169 | 0.0 |

Turn-1 HJB converged counts were `20 / 20` and both source final predicates were false. C1 exactly offset the A/B private-K destination differences at the firm-capital level, so turn-1 firm raw returns, output and wages were unchanged; the network-produced `rah` is the forward channel that would affect the next household pass.

For Path B pooled rows, correlation of Kprivate with raw `ra0` was `0.21191153007858532` and correlation of Y/total-K with raw `ra0` was `0.9976114704150845`. These are descriptive pressure diagnostics, not causal estimates.

## Bounded behavior and blockers

Path A did not reach a scientific convergence assessment: it stopped after one completed turn on a task-wrapper legacy-formula assertion. Path B reached turn 25 but the existing final predicate remained false, so it is explicitly nonconverged at the ceiling. Path B contained 92 HJB nonconverged-but-continued observations; all 775 KFE observations remained `DIAGNOSTIC_ONLY`.

Path B HJB converged counts by turns 1-5 were `20, 13, 10, 10, 10`; turns 6-25 were `31/31`. The terminal nonconvergence was instead driven by the existing outer predicate (`max_nk_gap=1.8619512598405663e-09` at turn 25 versus the frozen `1e-9` threshold), not by a false HJB flag at the terminal turn.

The corrected-2018 empirical finite-box upper-b leakage plus MATLAB-style pinning remains an independent scientific blocker. A running bounded trajectory does not establish KFE admissibility, steady-state acceptance, or Results eligibility.

## Evidence and next gate

External evidence root: `D:\ProjectTemp\ch5-k1a-equal-share-vs-beta2-evidence-20260911-001`. Manifest SHA-256: `A6275F06A8449FD663CA2E42299F9F428CE3861C5C1DCEBE15A8DD3660D7E59A`; readback checked 2606 files with status `PASS`. Compact tracked receipts are under `docs/evidence/ch5_mp4c_k1a_equal_share_vs_beta2`.

Owner/Reviewer must decide whether a fresh exact task should authorize a clean two-path rerun after the task-wrapper provenance defect, and separately retain authority over K1B/K2 and the unresolved KFE boundary. No successor is published here.
