# Freeze — first-turn provincial input/outcome envelope audit

Status: CURRENT.

This is a zero-science-runtime offline audit. No HJB/KFE/firm/wage/return/outer/MATLAB/GE/Results execution is authorized.

## Objective

Use accepted sealed first-turn evidence for all 31 provinces to determine whether the six legal HJB nonconvergences are descriptively associated with a simple input/guard/mapping envelope, or whether failure remains interleaved with successful provinces in accepted input space.

## Fixed authority

Use only accepted repository evidence. At minimum recover, when available, for every province:

- province id/index and accepted HJB outcome;
- consumed household `ra/rah`;
- household composite `w`;
- `rb`, borrowing gap, tax and transfer;
- return-guard state and raw pre-guard return if sealed;
- wage-guard state and raw provincial `wjt` if sealed;
- any already sealed upstream mapping receipts needed to distinguish consumed household inputs from upstream provincial prices;
- iterations, final convergence statistic and max A2max.

Do not reconstruct missing fields from chat memory or rerun any mapping. Missing fields must be reported as unavailable.

## Analysis rules

This audit is descriptive, not causal and not a classifier-fitting exercise. Do not train ML models, optimize thresholds, or select cutoffs after seeing outcomes.

Pre-register simple summaries only:

1. success/failure ranges and quantiles for `ra` and composite `w`;
2. rank positions of failures within the 31-province `ra` and `w` distributions;
3. guard-state contingency tables;
4. nearest success for each failure in standardized `(ra,w)` coordinates using full-sample mean/std computed once;
5. convex-hull / bounding-box descriptive inclusion where deterministic and robust;
6. whether any single one-dimensional threshold on `ra` or `w` can separate all six failures from all 25 successes; report only existence/nonexistence, not a tuned production rule;
7. whether failures form one connected region in a fixed k-nearest-neighbor graph with `k=3` on standardized `(ra,w)`, compared descriptively with successes;
8. if sealed raw upstream return/wjt values exist, repeat only analogous descriptive ranks/overlap checks; do not recompute mappings.

## Interpretation gates

Choose exactly one terminal class:

- `SIMPLE_INPUT_ENVELOPE_SEPARATION_SUPPORTED`
- `FAILURE_SUCCESS_INPUT_ENVELOPES_OVERLAP_SUBSTANTIALLY`
- `UPSTREAM_GUARD_OR_MAPPING_STATE_ASSOCIATION_SUPPORTED`
- `INPUT_OUTCOME_ENVELOPE_EVIDENCE_INSUFFICIENT`

If multiple observations coexist, choose the strongest class that is directly supported and describe caveats.

No result from this audit authorizes recalibration. Any change to `wjt→w`, return→`ra`, guards, economic parameters, or structural equations remains a later Reviewer/Owner decision.

Results eligibility remains `FALSE`.
