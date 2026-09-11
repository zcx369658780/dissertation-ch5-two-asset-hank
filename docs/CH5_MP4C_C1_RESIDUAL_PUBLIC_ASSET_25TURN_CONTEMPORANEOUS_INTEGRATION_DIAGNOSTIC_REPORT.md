# Chapter 5 MP4C C1 residual public-asset contemporaneous integration and 25-turn diagnostic

Date: 2026-09-11

Builder verdict: `C1_RESIDUAL_PUBLIC_ASSET_25TURN_PASS__CAPITAL_TARGET_HELD_AND_BOUNDED_PATH_QUANTIFIED`

## Outcome

The separately named C1 route completed exactly one initialization observation and one 25-turn corrected-2018 trajectory. Initialization retained the accepted G1 observation contract and aligned 31/31 firm accounting capital levels. Across all 775 province-turn observations, the contemporaneous identity passed 775/775 with maximum absolute residual 1.4901161193847656e-08 MU and zero historical C0 GovInv actions.

Private capital reached or exceeded target in 0 province-turn observations. The residual floor bound in exactly the same 0 observations, setting public assets to zero and preserving private overshoot. For pooled turns 20-25, total K/target min/median/max was 1.0/1.0/1.0; private K/target was 0.0009228940306782008/0.0031258439318608737/0.03398061369972668. The accepted C0 late-window two-to-three-times overshoot therefore disappeared whenever private capital remained below target; any remaining total overshoot is mechanically private, not GovInv-driven.

## Prices and outer adjustment

The selected-turn three-route comparison is in `baseline_selected_turn_comparison.csv`; G0 and G1+C0 were read from accepted evidence and were not rerun. At turn 25 C1 raw-ra lower/interior/upper counts were 0/1/30, versus G0 0/21/10 and G1+C0 0/21/10. Holding total capital at target therefore increased, rather than reduced, upper-bound raw-ra pressure. Pooled C1 `rah` min/median/max was 0.06490308001333485/0.08488047609984661/0.09, and turns 20-25 were 0.06490309855747681/0.08488047609984661/0.09; it remained high/boundary-proximate rather than becoming more interior.

KN and GDP paths improved materially relative to both C0 baselines. At turn 25 max KN gap was 2.0177068904558837e-09 and max GDP-level gap was 0.007556323724974279, versus G0 0.12229540553631124/0.07220163208908015 and G1+C0 0.12099132683728997/0.07255439940204123; max Y/Yprev gap was 1.3322676295501878e-15. Zt adjusted 54 province-turns, only on turns 4, 6, 7 (31, 17, 6 provinces respectively), and zero times in turns 20-25. It was an early transition channel, not the dominant late-window adjustment source. GovInv was recomputed only by the residual identity and was never overwritten by Zt.

The remaining direct numerical convergence blocker is price/numeraire/raw-ra upper clipping: 30/31 provinces remain above the raw-ra upper bound at turn 25, while KN is also still just above the frozen `1e-9` threshold. KFE validity remains an independent scientific blocker. All HJB returns converged from turn 6 onward, so late-window HJB is not the immediate blocker. Source-faithful labor remains a known interpretation limitation, but this isolated C1 run provides no evidence that normalized labor should be stacked next before the price/numeraire boundary is diagnosed. No normalized-labor route was activated and no workplace-employment claim is made.

## Household validity and calls

There were 46 finite HJB nonconverged-but-continued trajectory observations; their false flags remain diagnostic-only. All 775/775 trajectory KFE returns were independently `DIAGNOSTIC_ONLY`. One scientific process used 31 initialization HJB/KFE/aggregate calls plus one At-only allocation, then 775 trajectory household updates over 25/25 turns. Scientific retry, second initialization, second trajectory, turn 26+, beta cells, MATLAB, production steady-state, GE, annual, IRF, and Results calls were zero. Results eligibility remains FALSE.

Phase A completed 40/40 focused cases before science, plus compile and diff checks, with zero scientific calls. The legacy source-faithful one-turn, C0 controller, firm, and capital-allocation sources remained unchanged from the live baseline.
