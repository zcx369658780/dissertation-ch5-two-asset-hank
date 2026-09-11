# Chapter 5 MP4C G1 residual-GovInv initialization integration and isolated 25-turn diagnostic

Date: 2026-09-11

Baseline live `origin/main`: `1a20d535ff1626b8ae2108690e0acde6ded14839`. Branch: `codex/ch5-g1-residual-govinv-25turn-isolated-20260911`. External evidence root: `D:\ProjectTemp\ch5-g1-residual-govinv-25turn-isolated-evidence-20260911-001`.

Builder verdict:

`G1_RESIDUAL_GOVINV_25TURN_FAIL__INITIAL_ALIGNMENT_VALID_BUT_UNCHANGED_CONTROLLER_RECREATES_OR_WORSENS_INSTABILITY`

## Outcome

The separately named G1 route completed one `INITIALIZATION_OBSERVATION` and one 25-turn corrected-2018 trajectory. G1 aligned initial accounting capital to target in 31/31 provinces with zero maximum identity error. Outer turn 1 median total K/target was 1.0, versus accepted G0 1.0032099909906587; the initial duplication was removed.

The unchanged historical controller did not preserve the improvement. Across 25 turns it recorded decrease/increase/hold counts 0/289/486, exactly the accepted G0 totals. Repeated high-ra increases rebuilt GovInv overshoot. For the pooled 186 province-turn observations in turns 20-25, total K/target min/median/max was 1.3257022041568054/2.353363495591088/2.8512142917573127, GovInv/target was 1.3144349634860897/2.3503561274071445/2.8503483106194247, and private K/target was 0.0008487807700594351/0.0029186382400614363/0.032578861285661315. Across the six turn-level medians, total K/target rose from 2.139620420034785 to 2.823874321575053. The late overshoot is therefore overwhelmingly GovInv-driven.

## G0 comparison and dynamics

The selected-turn comparison is in `g0_vs_g1_selected_turn_comparison.csv`; G0 was read from accepted evidence and was not rerun. G1 starts closer to target, but the old controller erodes and then reverses that improvement. At every selected turn, lower/interior/upper raw-ra counts are identical to G0; boundary pressure did not improve. Pooled trajectory `rah` min/median/max is 0.04321939245328199/0.0840064134670995/0.09, versus G0 0.04301645724258693/0.08400514805131246/0.09. Thus `rah` does not collapse in G1, but it is essentially unchanged from G0 and does not establish production plausibility. KN, Y/Yprev and GDP-level gaps are slightly smaller in level at some turns but retain the same oscillatory controller-gate pattern, and the source final predicate never passes.

## Household validity

Initialization HJB convergence was 20/31; all 31 initialization KFE returns were `DIAGNOSTIC_ONLY`. Across the trajectory there were 50 HJB nonconverged-but-continued observations, including 3 in turns 20-25; all 775 KFE classifications were independently `DIAGNOSTIC_ONLY`. Finite continuation never promotes a false HJB flag or KFE blocker to scientific validity. The beta bridge remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

## Calls and boundaries

One process made 31 initialization HJB/KFE/aggregate calls and one initial At-only allocation, followed by 775 trajectory HJB/KFE/aggregate calls and 775 province firm updates over 25/25 turns. Totals were 806 HJB calls, 20093 HJB direct solves, 806 KFE direct solves, and 644800 labor-root/Brent calls. Scientific retries, second initialization passes, second trajectories, beta cells, MATLAB, steady-state, GE, annual, IRF and Results calls were zero.

Phase A ran the 40-case focused suite twice before science (80 cumulative cases), and two compile processes; all passed with zero scientific calls. After final deterministic packaging and verdict-classifier correction, the focused suite passed again at 41/41, compile and `git diff --check` passed, and manifest readback passed 20/20.

The raw runner terminal marked successful completion of the authorized 25-turn chain. Post-science deterministic classification applied the task's explicit economic verdict rule and superseded that completion marker with the FAIL verdict above. The candidate runner was then corrected only to apply the same classifier on future readback; no scientific state changed and no science was rerun. Executed and final runner hashes are both retained in `source_hash_receipt.json`.

The evidence is sufficient to justify a separately reviewed controller-redesign task, but this task does not publish one and does not change the controller. Normalized labor was not activated. Results eligibility remains FALSE.
