# Chapter 5 corrected-2018 HJB nonconvergence propagation and 25-turn K/L rerun

Date: 2026-09-10
Builder verdict: `HJB_PROPAGATION_REPAIR_AND_25TURN_KL_PASS__LATE_WINDOW_RECONCILIATION_COMPLETE`

## Scope and authority

Live `origin/main` at task start was `bdc3631f518b0d591e799a273cb6f9262c401260`, which published `tasks/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPAIR.md`. Work used a dedicated branch/worktree and the accepted corrected-2018 Track-A runtime. No household equation, HJB/KFE equation or tolerance, grid, solver family, migration rule, GovInv rule, price bound, damping, hysteresis, or production equation was changed.

The predecessor candidate `a0e117ade98f8197bb76cd2471f7932d545afbcc` was used only as rejected historical harness evidence. Its corrected input binding remained valid; its unconditional `if not hjb.converged: raise RuntimeError(...)` policy was removed in the successor harness.

## Phase A repair and zero-science gate

The successor harness validates every required numeric HJB array, both returned sparse operators, dimensions, iteration metadata, and convergence statistic. A finite and structurally usable `converged=false` return is persisted and classified `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`; KFE and aggregation then continue. Nonfinite/malformed HJB state, an unusable operator, or malformed/nonfinite KFE state still fails closed. The false convergence flag is preserved in `PreFrozenHouseholdOutputBatch`, and the final source predicate is guarded against passing unless all 31 flags are true.

Phase A completed before `science_started.json` existed:

- focused zero-science tests: 22/22 passed in one process;
- syntax/compile check: one process covering the successor run, finalizer, and test files;
- HJB, KFE, and outer scientific calls: 0;
- corrected runtime binding: 31/31 passed;
- rejected old-scale Anhui injection: failed closed before science.

The external `phase_a_zero_science_repair_receipt.json` records this gate.

## Bounded execution

Exactly one scientific process and one trajectory ran to the authorized 25-turn ceiling. All 25 turns and all 775 province household updates completed. There were zero household failures, zero scientific retries, zero second trajectories, and zero parameter-cell comparisons.

| Call | Attempted / returned |
|---|---:|
| household | 775 / 775 |
| HJB | 775 / 775 |
| HJB direct solves | 18,950 |
| KFE | 775 / 775 |
| KFE direct solves | 775 |
| aggregate | 775 / 775 |
| migration / capital allocation / one-turn | 25 / 25 / 25 |
| firm | 775 / 775 |
| wage batches / province outputs | 25 / 775 |
| labor roots / Brent | 620,000 / 620,000 |

MATLAB, steady-state runner, GE, annual, IRF, and Results calls were all zero. Elapsed scientific process time was `2513.7189999999973` seconds.

## Premature-stop reconciliation

The prior turn-1 stop was caused by the rejected Python harness policy, not by the absence of usable returned numerical objects. In this rerun Anhui reproduced the same turn-1 HJB nonconvergence (`100` iterations, statistic `0.18862667495966345`), was classified diagnostic-only, continued through KFE/aggregate, and participated in a complete 31-province batch and downstream K/L turn. The trajectory then completed all 25 turns.

This establishes operational continuation only. It does not make a nonconverged HJB scientifically valid and does not remove the 31/31 household requirement from the final source predicate.

## HJB convergence path

There were 60 nonconverged-but-continued province-turn observations across 20 provinces. Shandong had the longest/repeated path: 10 turns (`5, 8, 10, 14, 16, 17, 18, 19, 20, 21`). Anhui and Sichuan each had five; the remaining affected provinces had one to four.

Late window:

| Turn | HJB converged | Nonconverged-but-continued |
|---:|---:|---|
| 20 | 30/31 | 山东 |
| 21 | 29/31 | 辽宁、山东 |
| 22 | 30/31 | 山西 |
| 23 | 31/31 | none |
| 24 | 31/31 | none |
| 25 | 31/31 | none |

Anhui statistics for turns 1–5 were `0.18862667495966345`, `0.009406184163712084`, `0.2388886266642105`, `0.37605318082114736`, and `0.21794176292490453`: an oscillating, not monotone-improving path. Anhui returned to converged at turn 6 (`14` iterations, `4.2789682908050963e-10`) and remained converged through turn 25; turns 7–25 used 13 iterations except turn 6.

Even when all household flags were true at turns 23–25, the complete final source steady-state predicate did not pass; the run stopped at the authorized ceiling, not at steady state.

## Turns 20–25 K reconciliation

Across all 186 province-turn late-window observations:

| Ratio to Track-A K target | Min | Median | Mean | Max |
|---|---:|---:|---:|---:|
| firm total K | 1.3422659595802506 | 2.359983542526 | 2.2763698592304 | 2.866669200187509 |
| private K supply | 0.0008481231331185131 | 0.00291675418808339 | 0.0046427334268523 | 0.03308214700740542 |
| GovInv before controller | 1.3310000000000002 | 2.3579476910000015 | 2.27172712580354 | 2.8531167061100033 |

By province late-window mean, 29/31 provinces were `K_SEVERELY_HIGH` and 2/31 were `K_MODERATELY_HIGH`; none were near or below target. Turn-level median total-K ratios rose from `2.145773745027009` at turn 20 to `2.853982006571298` at turn 25.

The overshoot is dominated by GovInv, not private supply. At turn 1, with `GovInv/Ktarget=1`, every province already had positive private supply and therefore total K above target (median ratio `1.0032099909906587`, maximum `1.034865162027094`). This is direct observation of the accounting implication `firm_K_total=private_K_supply+GovInv` under `GovInv0=Ktarget`.

The current controller did not digest the overshoot in this prefix. In turns 20–25 GovInv decrease counts were always zero; increase counts were `22, 0, 21, 0, 16, 0`. Median GovInv/target rose from `2.143588810000001` at turn 20 to `2.8531167061100016` at turn 25. Under the frozen high-return action, it amplified rather than reduced the accounting gap.

Pure accounting therefore implies that `max(Ktarget-private_supply,0)` would be closer to Ktarget at initialization than `GovInv0=Ktarget` when private supply is positive. This is analysis only; no residual-GovInv rule was implemented or accepted.

## Turns 20–25 labor comparison

Destination firm labor divided by the 2018 population proxy had pooled minimum `4.589147349109114`, median `14.2307874070677`, mean `24.9546473786008`, and maximum `153.05180501585224`. All 31 province late-window means were classified `L_RELATIVE_TO_POPULATION_PROXY_SEVERELY_HIGH`.

All provinces showed positive destination-labor minus population-proxy differences, so there were no net outflow provinces under this particular proxy comparison. Beijing had the largest late-window mean difference (`5,641,318.76` NU); Guangdong had the smallest (`4,448,617.79` NU). These are not observed migration flows or workplace-employment gaps. `N0` is a population/labor proxy only, so the magnitudes reveal a severe scale/reference mismatch but do not by themselves validate destination labor as a calibration target.

## Anhui K/L trace

Anhui total-K/target rose from `1.003119032234857` at turn 1 to `2.146500112591523` at turn 20 and `2.855937407689818` at turn 25. At turn 25, private-K/target was only `0.0028207015798153426`, while GovInv/target was `2.8531167061100025`. Its firm-labor/population-proxy ratio was `9.706549949274317` at turn 25. The detailed requested turns are in `anhui_trace.csv`.

## Independent scientific blockers

All 775 KFE returns were classified `DIAGNOSTIC_ONLY`; all 186 late-window KFE returns remained diagnostic-only. Across the full run, source-free normwise ratios ranged from `3.4499496104998805e-25` to `0.18589722817202836`, and upper-b maximum outward-leak rates ranged from `0.0043272207643659955` to `5.473765943971329`.

HJB and KFE blockers remain independent: HJB nonconvergence appeared in 60 province-turn observations, while KFE remained diagnostic-only even in turns 23–25 when HJB convergence was 31/31.

## Evidence and boundaries

- External evidence root: `D:\ProjectTemp\ch5-corrected-2018-hjb-propagation-kl-rerun-20260910-001`
- Repository package: `reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/`
- Package manifest readback: 15/15 entries passed
- Manifest SHA-256: `A26A72509CFB3AEC4A34D0BDF0424264D5FBC6AB3E83997B868638EF67583C2D`

The verdict means the bounded diagnostic and late-window reconciliation completed. It is not steady-state acceptance, KFE/HJB scientific acceptance, production calibration authority, or Results evidence. `Results eligibility=FALSE`.
