# MP4C 2018 Anhui call-725 exact HJB replay and bounded continuation diagnostic

## Terminal

`MP4C_2018_CALL725_EXACT_HJB_REPLAY_AND_BOUNDED_CONTINUATION_COMPLETE__HJB_CEILING_AND_LEGACY_KFE_CLASSIFIED__NO_GE_NO_PRODUCTION_CHANGE`

The strongest supported isolated-call classification is:

`CALL725_HJB100_REPLAY_CONFIRMED__HJB_CONVERGES_ONLY_AFTER_100__LEGACY_KFE_ON_CONVERGED_OPERATOR_ADMISSIBLE__PRODUCTION_HJB_TERMINATION_POLICY_OWNER_REVIEW_REQUIRED`

This is not a production HJB termination-policy change, a 2018 GE steady state,
an annual rerun, a MATLAB/Python same-input claim, or Results evidence.

## Authority, identity, and preserved caveat

- Live task authority: `9536639f9a9203590adca386202f66116e08ae3a`, direct
  child of `5f05c441ca8d313a7af628b0594cdfc3f12968a0`.
- The start was fresh-fetched, fast-forwarded, upstream-equal, and clean.
- The current source blobs matched task requirements: faithful household export
  `9e7dc9556a2b76811e78f89999abecc045886106`, empirical validator
  `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`, and source-postloop adapter
  `0033baee136c0328e80ffb8b794a88d4405c976c`.
- The accepted standalone export SHA-256 was
  `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`.
- The retrospective manifest and captured A/A-transpose/localization/HJB-status
  identities all matched: `D0472539...06C490`, `A17AA9...AA1B42`,
  `7C1ADE...D8FDA66`, `362872...890BD63`, and `2B2436...181CAF5`.

The permanent evidence limitation remains unchanged:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

The isolated state was exactly the preserved outer-24, global call-725 Anhui
(zero-based province index 11) state, with captured `rah=0.09`, `rb=0.02`,
`tau=0.05`, `w=16.82014806560587`, `Tt=0.1`, and `rb_gap=0.07`.  It used the
frozen 20x20x2 grid, parameters, `_source_initial_arrays` initialization, and
single-thread NumPy/SciPy environment.  No GE/controller/fiscal/migration
state update occurred.

## Phase A: source-ceiling HJB100 replay

Exactly one HJB used `delta=1000`, `crit=1e-7`, `max_iterations=100`, and
`drift_tolerance=1e-12`.

- `converged=false`, `iterations=100`, and statistic
  `0.3038218386543494` reproduced the captured binary64 status exactly.
- The post-loop operator was finite, 800x800, and had 3,106 entries.
- Canonical CSR equality with captured A passed for shape, `indptr`, `indices`,
  and binary64 data.  Both in-memory canonical digests were
  `E3D4C66E96B131FC6E4A8EB60CDEA81F8C848CF743E74A85346BBDB9ECD16EED`.

Therefore the exact-replay gate passed before the continuation budget was used.

## Phase B: same-initialization HJB500 continuation

Exactly one second HJB restarted from the same original generated value and
baseline-labor arrays.  Its only changed numerical field was
`max_iterations=500`.

- It converged at iteration 196 with final statistic
  `2.2986279546444166e-10`.
- Final value and policy fields were finite; the post-loop operator was finite
  with 3,145 entries and canonical digest
  `9504A82A7E7609D6C9E201A3B079EFDE54497F6D95BEA27801D96CB5D510CB9E`.
- Relative to the HJB100 endpoint, the continuation changed the terminal
  state materially rather than merely extending an unchanged object.  The
  maximum absolute differences in value, consumption, labor, transfer,
  `mu_a`, and `mu_b` were respectively `0.9167341351`, `998.8708787565`,
  `1.6099566972`, `5408.0492959161`, `5408.0492959161`, and
  `56039883.26258294`.

This supports an isolated ceiling diagnosis: the frozen source-faithful
call-725 HJB has not converged by 100 iterations but does converge by 196 when
only the ceiling is extended.  Algorithmic faithfulness does not itself make a
finite source ceiling adequate for every household state.

## Phase C: one unchanged legacy KFE on the converged operator

Because Phase B converged, exactly one source-faithful KFE was run on its
post-loop operator: shape 20x20x2, `db=7/19`, `da=10/19`, contaminated row
295, unit-row replacement, RHS `0.007`, and source normalization.  No G1/G2,
adaptive row, fallback, alternate solver, regularization, or retry was used.

| Diagnostic | Result |
| --- | ---: |
| Raw solve / warnings | finite / 0 |
| Normalization factor | `0.18121090513939028` |
| Density mass / error | `1.0` / `0.0` |
| Minimum / maximum density | `-1.4607167036297244e-22` / `1.0768504624070188` |
| Negative entries / weighted negative mass | `64` / `3.2881418358523654e-23` |
| Negatives below direct machine tolerance | `0` |
| Raw contaminated residual infinity norm | `7.260315660060858e-15` |
| Frozen backward-error bound / result | `1.4324551660325224e-10` / PASS |
| `||A' g||_inf` / `||A' g||_2` diagnostic | `2.4505707583350165` / `2.4505707583350165` |

The `A' g` values are recorded only as source-contract diagnostics; they are
not standalone pass gates for this boundary-truncated source-faithful operator.
The density is normalized, backward-error certified, and has no entry below
the accepted direct machine tolerance.  The isolated household aggregates are
`C_ss=10.434969443057815`, `L_ss=0.6241861388467347`,
`A_ss=9.212879584614942`, `B_ss=-1.5496915046150406`, and
`A_ss+B_ss=7.663188079999902`.  They are not 2018 GE aggregates or Results.

## Budget, evidence, and boundary

The no-overwrite evidence root is:

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-replay-and-bounded-continuation-20260904-001`

Its audit-manifest SHA-256 is
`B15FE27D8531D5A1CE65E5D881327F820D82501FABD10B789F9F8B0544C7A0CF`.
The ledger records HJB100/HJB500/legacy-KFE calls `1/1/1`, retries `0`, and
GE, stationary outer loop, MATLAB, R/PLM, shock, IRF, and annual-2018 calls
all `0`.

No production/model/test source changed.  This report is the sole authorized
repository mutation.  The evidence warrants only a new Owner/L3 review of the
production HJB termination policy; it does not authorize a production change,
GE rerun, same-input MATLAB review, or a follow-on scientific route.
