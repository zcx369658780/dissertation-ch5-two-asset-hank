# CH5 MP4C K1 — J160 local-basin A2max receipt repair and controlled reexecution freeze

Status: ACTIVE.

## Purpose
Repair only the task-owned A2max receipt boundary and reexecute exactly the same 12 synthetic local-basin probes from the accepted blocked run.

## Frozen science
- Grid: `I=20,J=160,Nz=2`, `a=[0,100]`, `b=[-2,20]`, `h=1`.
- `Delta=1000`, tolerance `1e-7`, maxit `100`, A2max legality gate `0.01`.
- Accepted HJB equations, FOCs, selectors, boundary laws, derivative floors, sparse solve, initialization and convergence test unchanged.
- KFE=0.

## Exact pairs and probes
Use the same accepted pair authority and exactly the same synthetic points:
1. 山西→河北 at `t=.25,.50,.75`.
2. 重庆→河北 at `t=.25,.50,.75`.
3. 江西→安徽 at `t=.25,.50,.75`.
4. 贵州→四川 at `t=.25,.50,.75`.

Endpoints remain reuse-only. No new pair, no new t, no adaptive bisection.

## Receipt repair
The task-owned observer/aggregator must persist **source-generator A2max only for actual scientific HJB iterations**. The post-convergence implicit system matrix, any terminal solve object, or any `iterations+1` observational object must never enter scientific A2max maxima or legality classification.

Per probe persist at least:
- per-scientific-iteration A2max sequence;
- exact scientific maximum A2max;
- iteration of maximum;
- first scientific illegal iteration, if any;
- explicit count proving the recorded A2max sequence length equals the number of scientific HJB iterations.

If a separate post-convergence/system-matrix diagnostic is retained, it must be separately named and explicitly excluded from scientific legality.

## Invariance gate
Focused tests must prove the receipt repair is observational only and does not alter scientific arrays, selector decisions, solve order, convergence statistics, iteration count or terminal outcome. No scientific HJB call may be added solely for parity testing.

## Reproducibility
The 12 reexecuted terminal outcomes must be compared against the accepted blocked raw outcomes. Any unexpected terminal-class or iteration-count divergence must be reported; no retry is allowed.

## Runtime cap
- HJB exactly 12 after clean preflight.
- KFE=0.
- endpoint HJB=0.
- scientific retries=0.
- engineering retry <=1 and only before first HJB for path/import/serialization/receipt plumbing.
- outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results all 0.

## Interpretation
Only if all 12 scientific A2max receipts are valid may the pair topology be classified. Synthetic points remain numerical probes, not equilibrium states, calibrated states, mapping outputs, or counterfactuals.

Results eligibility=`FALSE`.
