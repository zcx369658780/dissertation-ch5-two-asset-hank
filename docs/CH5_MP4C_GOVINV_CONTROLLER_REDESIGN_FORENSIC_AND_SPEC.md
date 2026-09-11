# Chapter 5 MP4C GovInv controller redesign forensic and specification

Date: 2026-09-11

Builder verdict:

`GOVINV_CONTROLLER_REDESIGN_SPEC_PASS__HISTORICAL_CONTROLLER_FAILURE_MECHANISM_QUANTIFIED_AND_CANDIDATES_SEPARATED`

## Outcome and boundary

This package is a zero-science forensic of the accepted G1 ledger and a controller design specification. It made no household, HJB, KFE, migration, firm, controller-runtime, outer-turn, steady-state, root/Brent, MATLAB-runtime, GE, annual, IRF, or Results call. It neither implements nor selects a production controller. `Results eligibility=FALSE`.

The historical C0 formula was replayed from the accepted 775-row G1 ledger with zero mismatches. Across all 775 province-turns, **258 (33.290323%)** were statically directionally inconsistent with the contemporaneous capital-level gap. All 258 were `total K above target + HIGH_RA_INCREASE_1P1`. The remaining 517 are classified closing-or-neutral, not dynamically beneficial. Window counts are: turns 1-5 `0/155`, 6-10 `92/155`, 11-15 `56/155`, 16-20 `73/155`, and 21-25 `37/155`.

## Exact C0 semantics and failure mechanism

Firm capital is private productive supply plus GovInv. The firm computes raw `ra0` and clips it before returning `ra`. After a nonconverged turn, `max(abs(KNratio/tKNratio-1))<0.1` opens adaptation. Zt correction occurs first; then clipped `ra<ramin+0.02` reduces GovInv by 10%, clipped `ra>ramax-0.02` increases it by 10%, and the interior holds. Finally `tKNratio` is updated by `0.6*current KNratio+0.4*old target`.

C0 recreates overshoot after G1 because its trigger and target are different objects. G1 makes `Kprivate+GovInv=Ktarget` only at initialization. C0 never reads Ktarget or that residual. When the clipped high-return signal crosses its upper trigger, it compounds the GovInv stock by 1.1 even when current total K is already above target. Clipping preserves boundary direction but discards raw exceedance magnitude; the intermittent KN gate alternates adjustment and hold turns; Zt and tKNratio feedback can alter future signals but contains no explicit K-level correction. These are source and static-ledger facts, not a dynamic causal decomposition.

The accepted path contains 289 increases and no decreases. Thirty-one increases occur while total K is below target (closing direction); 258 occur above target (worsening direction). Holds include above-, below-, and exactly-at-target observations and are conservatively neutral. Multiplicative 1.1 actions can compound, explaining the arithmetic channel by which the GovInv level grows; the ledger does not identify a causal effect of any single action on later endogenous states.

Detailed source order is in `controller_source_timing_map.md`; row-level classifications are in `g1_static_directional_forensic.csv`; window summaries are in `controller_direction_summary.json`.

## Candidate comparison

- **C0 historical return-bound:** source-authorized benchmark only. It is fundamentally a clipped return-bound controller, not a capital-target controller.
- **C1 capital-target residual:** `GovInv_next=max(GovInv+lambda_K*(Ktarget-(Kprivate+GovInv)),0)`. It is dimensionally and structurally coherent with G1 because both use the same capital accounting residual and preserve nonnegativity. No `lambda_K`, timing, adaptation gate, or dynamic-stability claim is authorized. `lambda_K=1` describes only one-step static accounting residual replacement.
- **C2 raw return-target:** cannot be instantiated or replayed because neither an interior `ra_target` nor a gain is source-authorized. It adds more unverified tuning than C1 and would couple strongly to labor and firm normalization.
- **C3 staged/hybrid:** conceptually separates stage 1 K-level closure from later return/GDP/KN correction. It requires the most decisions: K-gap transition tolerance, hysteresis, damping, secondary targets/gains, raw-versus-clipped return, and whether Zt/GovInv may change together.

The full comparison matrix reports objective, signal, target, sign, units, positivity, evidence authority, interactions, tuning risk, and minimum future test budget. No candidate is promoted to production.

## Required answers

1. **Why does C0 recreate overshoot after G1?** G1 corrects only initial accounting. C0 ignores Ktarget and responds to clipped return bounds; 1.1 multipliers therefore compound GovInv even above the capital target.
2. **How often is C0 directionally inconsistent?** 258/775, or 33.290323%, overall. The requested five-turn-window counts are 0, 92, 56, 73, and 37 out of 155.
3. **Is C0 a return-bound rather than capital-target controller?** Yes. Source inspection shows no Ktarget, total-K residual, or private-K residual in the controller.
4. **Is C1 coherent with accepted G1 initialization?** Yes, algebraically and dimensionally: it carries the same residual identity forward. This is design coherence, not dynamic validation.
5. **What choices precede C1 implementation?** GovInv economic meaning, primary objective, fixed Ktarget authority, positive gain, timing/gate, projection behavior, Zt sequencing, damping/hysteresis, and preregistered stopping/evaluation rules.
6. **Do C2/C3 require more unverified tuning?** Yes. C2 adds an unidentified return target and gain; C3 adds those plus state-transition gates and interaction rules.
7. **Should initialization and controller remain separate?** Yes. The accepted G1 result empirically demonstrates that initial alignment and subsequent control are distinct mechanisms; separate named components preserve attribution and rollback.
8. **Lowest-risk next experiment?** After Owner selects GovInv meaning and a K-level primary objective, implement only a separately named C1 diagnostic pure function. First test algebra, positivity, units, sign, and static replay with zero science. A later exact task may authorize one bounded trajectory while freezing G1 initialization, source-faithful labor, HJB/KFE, Zt logic, and all unrelated rules. This task does not publish that successor.

## Owner decisions and stop

The unresolved choices are isolated in `owner_decision_matrix.csv`. PASS means the C0 failure mechanism is quantified and C0/C1/C2/C3 are cleanly separated. It does not authorize coefficient selection, runtime implementation, a trajectory, steady-state acceptance, or Results. The next gate is independent ChatGPT Reviewer fresh-fetch ACCEPT/REJECT of the candidate commit.
