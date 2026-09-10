# Chapter 5 MP4C corrected-2018 25-turn K/L target reconciliation diagnostic

Date: 2026-09-10

Base `origin/main`: `fce18516169e5a85ff3267aff51643f61feae66a`

Branch: `codex/ch5-corrected-2018-25turn-kl-reconciliation-20260910`

Verdict: `CORRECTED_2018_25TURN_KL_RECONCILIATION_PARTIAL__EARLY_HARD_FAILURE_BEFORE_LATE_WINDOW`

## Outcome

The one authorized corrected-2018 trajectory started after the accepted 31/31 Track-A runtime validation, but stopped during turn 1 at Anhui before the multi-province one-turn composition. Anhui's HJB returned `converged=false` after the frozen 100 iterations with convergence statistic `0.18862667495966345`. The run therefore completed zero outer turns and produced no turn-20-to-25 K/L window.

No scientific rerun, parameter comparison, solver adjustment, tolerance change, grid change, or post-hoc tuning was performed. The PARTIAL verdict is a scientific result under the frozen contract, not an engineering failure to be retried.

## Frozen runtime receipt

The active payload passed the accepted pre-science hard validator before `science_started.json` was written:

- actual 2018 GDP and population;
- raw-NBS GFCF Track-A PIM capital;
- `delta_pim=.096`, `alpha_raw=alpha_used=.7380939146868483`;
- `MU=10万元`, `NU=100 persons`, same-year `Zt0`;
- firm depreciation `.025`;
- `GovInv0=Ktarget_2018_TrackA_MU` unchanged;
- source-lagged `rah`, `beta_a=1` labelled `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`;
- unchanged bounds, HJB/KFE, grids, `Lt_seperate`, GovInv controller, damping and hysteresis.

Runtime payload SHA-256: `909034222C8AEC58C91BD1630D6253E5C1B6BEF68C9F7FE78EB2E8DD3350D899`.

## Scientific progression and validity

One scientific process and one trajectory attempt were consumed. It entered turn 1 and reached 12 province household/HJB calls:

- Beijing through Zhejiang: 11/11 HJB converged; 11 KFE calls returned;
- Anhui: HJB returned nonconverged at iteration 100; KFE was not entered;
- remaining 19 provinces were not attempted;
- HJB direct solves: 347;
- KFE direct solves: 11;
- labor-root and Brent calls: 9,600/9,600;
- household aggregate returns: 11;
- migration, capital allocation, firm, wage, controller and completed outer-turn calls: all zero;
- scientific retries and second trajectories: zero.

Every one of the 11 reached KFE outputs is `DIAGNOSTIC_ONLY`. Their source-free normwise residual ratios range from `0.000791027204900689` to `0.146088275154476`; maximum upper-b outward leak rate is `4.24076000925756`. Thus an HJB blocker and the already-known KFE validity blocker are both present independently, although the early stop prevents a complete 31-province turn-1 validity census.

## Required K/L questions

Because no `one_turn` completed, no private `Kt_supply`, destination `firm_Lt_supply`, firm total K, or controller action was produced. Evidence strength is therefore `not estimable` for observed K/L trajectory claims:

1. Total firm K after turn 20 relative to Track-A Ktarget: **not estimable**.
2. Late-window GovInv/private-K decomposition: **not estimable**.
3. `GovInv0=Ktarget` early overshoot: the accounting identity alone implies that any positive private supply would make `firm_K_total=Ktarget+private_supply>Ktarget`; this run did not reach private-supply construction, so it did not empirically quantify the overshoot.
4. Whether the controller consumes overshoot by turns 20–25: **not estimable**; controller calls were zero.
5. Destination firm labor versus population proxy: **not estimable**; migration/Lt allocation calls were zero.
6. Largest destination gains/losses: **not estimable**.
7. Residual initialization `max(Ktarget-Kt_supply0,0)`: it is mechanically target-aligning given a known nonnegative initial private supply, but that is only an accounting implication. This task neither estimated the required supply nor implemented the rule.
8. Migration-adjusted destination labor as a future reference object: **not assessable from this run**. `N0` remains only a population/labor initialization proxy, not observed workplace employment.
9. HJB/KFE blockers: **yes, independently observed** as described above; this does not diagnose or authorize a repair.

The requested province-turn, national-turn, late-window and Anhui ledgers are present with schema headers and zero data rows. This explicitly represents unavailable evidence rather than fabricating or extrapolating turns.

## Evidence

External evidence root: `D:\ProjectTemp\ch5-corrected-2018-kl-reconciliation-25turn-20260910-001`.

Repository-safe package: `reports/mp4c_corrected_2018_25turn_kl_reconciliation_20260910/`.

Key files:

- `scientific_validity_ledger.csv`: 12 reached HJB records and 11 KFE classifications;
- `province_turn_kl_ledger.csv`: header plus zero completed-turn rows;
- `national_turn_summary.csv`: header plus zero completed-turn rows;
- `late_window_20_25_province_summary.csv`: header plus zero late-window rows;
- `anhui_trace.csv`: header plus zero completed-turn rows;
- `govinv_k_decomposition_summary.csv` and `labor_migration_proxy_summary.csv`: explicit `NOT_AVAILABLE_EARLY_HARD_FAILURE_BEFORE_LATE_WINDOW` classifications;
- `call_ledger.json`, runtime/bounded-invocation receipts, source hashes and terminal result;
- manifest/readback: 13/13 entries passed, manifest SHA-256 `5929DA489CB3A7E034EA19B4302127F5425833392789B183103E887AF22C40E6`.

Focused static tests ran in three processes with 46 cases total; latest affected suite was `22 passed`. Three Python compile checks passed. These are engineering checks only and do not change the scientific PARTIAL result.

## Boundary

This result is deterministic diagnostic evidence from one bounded trajectory attempt. There is no inferential comparison family, repeated seed, confidence interval or significance claim; no p-value-based conclusion is made. It does not establish convergence, validate K/L calibration, select a GovInv or labor redesign, repair HJB/KFE, authorize another trajectory, or make Results eligible.

Results eligibility remains `FALSE`. The next gate is independent ChatGPT Reviewer ACCEPT/REJECT of the candidate package; any rerun or scientific repair requires a new exact task.
