# MP4D shock/IRF source-semantics audit and Python route freeze

## Verdict

`MP4D_SHOCK_AND_IRF_SOURCE_SEMANTICS_AUDIT_AND_PYTHON_ROUTE_FREEZE_PASS`

Protected-source classification: `SEQUENTIAL_STATIONARY_COMPARATIVE_STATICS_RESPONSE_PATH_CONFIRMED`.

This is a zero-science source audit. MATLAB, Python stationary/household/HJB/KFE,
comparator, shock/AR(1)/transition/IRF, R5, and Results calls were all zero.

## Source-backed route

`main.m` initializes `T=20`, a 1-percent deterministic path
`0.01*exp(-0.5*(t-1))`, and shock vectors. `multi_prov_HANK` maps calendar year
to `nst=styear-2008`, loads `st=multi_prov_HANK_12sts(nst,0)`, and invokes
`mpHANK_shock_2000(st,shocks{j},T)` for each selected origin province.

At each date, `mpHANK_shock_2000` reloads the migration matrix, resets
`Zt`, `GovInv`, `tau`, and `corptau` from the frozen baseline `st.results`, then
calls `HANK_mp_1turn` once and stores the carried `results` as `IRF{iter}`.
`HANK_mp_1turn` calls contemporaneous `HANK_2ASSETS_HJB`, KFE-bearing household
logic, migration, firm, wage, fiscal, and monetary blocks. There is no finite
horizon terminal condition, backward time-indexed HJB, forward time-indexed KFE,
expectations law, or transition-path convergence solve.

Thus the time path carries the response `results` aggregate/state container, while
the named exogenous objects are re-based on the frozen annual steady state each
date. The source does not implement a literal AR(1) recursion or stochastic
innovation process; its active path is deterministic exponential decay.

## Frozen Python contract

Python must reconstruct one selected annual checkpoint into a source-semantic
response state, form the deterministic source shock vector, reset the named
exogenous baseline objects each date, reload the migration support, and apply one
source-faithful one-turn analogue to carried response results. It must preserve raw
response fields and the source plotting normalization (`response / baseline - 1`)
explicitly. The Python MAT checkpoint remains a source-backed checkpoint, not a
legacy MATLAB `st` drop-in; legacy `param`, `num`, `CHI`, and full `results` schema
need explicit materialization rather than an identity claim.

## Evidence and next gate

The no-overwrite evidence package is
`D:\ProjectTemp\ch5-mp4d-shock-irf-source-semantics-audit-20260902-001` and
contains the call graph, shock matrix, transition diagnostic, checkpoint and output
contracts, freeze, validation design, ledger, and manifest.

Exactly one recommended next gate:

`MP4D_REPRESENTATIVE_YEAR_SHOCK_RESPONSE_IMPLEMENTATION_AND_VALIDATION`

The prescribed first candidate is 2020 productivity shock, one selected origin,
20 dates, with a protected MATLAB reference artifact required before comparison.
No full-sample shock route is authorized by this audit.
