# Call725 rah=0.07 liquid-domain expansion — Reviewer acceptance

Date: 2026-09-09. Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Candidate: daccda4698e87ee60a76fc4ff0196468b40198d3.
Reviewed live main before integration: 8726a006ebc2d1bcb82225cb4b1062076642881b.
Task: tasks/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_SINGLE_HOUSEHOLD.md.

## Decision

Accept `diagnostic_completion=COMPLETE`, exact grid binding PASS, HJB convergence, and the bounded conclusion `EXPANSION_DOES_NOT_REMOVE_BOUNDARY_PRESSURE`.
Reviewer marker: `B_DOMAIN_EXPANSION_ACCEPTED__TRUNCATION_MATERIAL__B12_STILL_INSUFFICIENT`.

This acceptance establishes that the old b=5 upper truncation is materially consequential for this saved one-household configuration, but the one-time expansion to b=12 remains insufficient. It does NOT adopt bmax=12, establish grid convergence, validate source-free stationarity, change the production grid, approve a boundary/source law, accept corrected 2018, or make Results eligible.

Candidate is the direct descendant of the reviewed task-publication main and was integrated by non-force fast-forward before this acceptance record. Candidate writes are confined to the task-authorized diagnostic/test/report families; production/export/helper/parameter/boundary source is unchanged.

## Accepted evidence

1. The only scientific intervention is the liquid grid. The old 20 b nodes are an exact prefix; 19 nodes are appended at the captured binary64 db=0.368421052631579, producing I=39 and endpoint exactly 12.0. a, z, switch matrix and economic/numerical inputs remain unchanged. Native V0/l0 on the common 20x20x2 subgrid are 800/800 exact.
2. Expanded HJB converges in 17 updates with statistic 7.140894586754598e-08 under the unchanged strict criterion. This is a stopping result, not complete numerical validity: the final-iteration Qh still has 11 negative offdiagonals, minimum -3.464832800963844.
3. The post-loop operator still has 17 upper-b outward cells, maximum omitted rate 3.469034770311481 and unweighted sum 16.296417971077133. `Q*1+ell` closes to 2.942091015256665e-15, confirming the same finite-box omission mechanism remains.
4. KFE returns a finite row-replaced solution, but the original source-free equation fails: ||Tg||inf=0.5206986084614471, scale ratio=0.11601750528081986. The small contaminated-system residual does not replace this test.
5. Correct expanded-density region masses are b<=5 = 0.5327650526244969 and b>5 = 0.46723494737550303. The new top-face mass is 0.06835756005310577 and density-weighted upper-b escape is 0.10096648917534981. Thus a large part of this diagnostic returned density lies beyond the old b=5 cutoff, while the new b=12 face is still materially occupied. Because source-free stationarity fails, these remain diagnostic-density facts, not accepted wealth-distribution estimates.
6. The KFE pin mechanically moves with state count to k=576, F-order (30,14,0), at approximately (b,a,z)=(9.05263157894737,7.368421052631579,0.8). Therefore returned KFE density and C/L/A/B changes are not a fixed-pin pure-bmax causal comparison.
7. The row-replacement source/escape ledger again closes for the expanded saved density, but no economic source/entry/exit interpretation is adopted.

## Budget and review level

Actual new science: one Python process, one native initialization, 1560 labor roots and 1560 nested brentq entries, one HJB with 17 direct solves, one KFE/direct solve and one aggregation. Scientific restart/retry=0; old baseline, other rates/provinces, firm/one-turn/GE/annual/MATLAB/IRF/Results calls=0.

Reviewer evidence: L3 candidate/diff/code/report review plus L4 inspection of the published final 9/9 synthetic test log. Reviewer did NOT independently execute tests or scientific models, directly read the external Windows NPZ arrays, or independently rehash all 69 manifest references. Manifest/readback and complete-array identities remain Builder evidence. Published manifest SHA256: B4299EB15F616AA1DE8D40FF5B655E4BB6AB6C694E673F99695B9822663BEA38.

## Next scientific decision

Do not run multiple provinces and do not keep extending b until a PASS appears. The evidence now establishes both facts needed for the next decision: b=5 is materially truncating this one-household solution, while b=12 is still not a demonstrated adequate truncation. A further single-household truncation point, or a finite-box boundary-law choice, is a new scientific decision for Owner. No successor task is activated by this acceptance.

Results eligibility=FALSE.
