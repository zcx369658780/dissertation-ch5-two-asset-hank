# MP4C 2018 captured-operator nullspace, contaminated-row, and HJB-trajectory forensic

## Terminal

`MP4C_2018_CAPTURED_OPERATOR_NULLSPACE_AND_CONTAMINATED_ROW_FORENSIC_COMPLETE__PROXIMAL_CAUSE_CLASSIFIED_OR_BOUNDED__CAPTURE_TIME_HASH_GAP_EXPLICIT__NO_REPAIR_NO_RERUN`

This is a read-only forensic of already captured objects.  It neither changes a
model/diagnostic/test source nor runs 2018, stationary, household, HJB, KFE,
MATLAB, R/PLM, shock, IRF, postmortem, a density solve, or `spsolve`.

## Authority, continuity, and provenance

- Live task authority at analysis start: `3f847afc970d794e59e3cb3a2422cb1664b05ba9`, direct child of
  `e3f1fdc56c30bc094aa66b997dcadb3147b652c2`.
- Start continuity: `HEAD == origin/main == 3f847afc970d794e59e3cb3a2422cb1664b05ba9`, ahead/behind `0/0`,
  and clean tracked worktree.
- Preserved source root:
  `D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`.
- The required `retrospective_execution_evidence_manifest.json` hashes to
  `D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490` and is classified
  `RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`.

The permanent provenance limitation is retained verbatim:

`CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`

The retrospective certification validates the current preserved bytes and their
internal/report-anchor consistency.  It does not establish that bytes without a
capture-time published hash never changed before retrospective certification.
No `audit_manifest.json` was created, sought, or imputed in the original
execution root.

## Evidence identity

All mandatory current source-artifact hashes passed before this analysis:

| Artifact | SHA-256 |
| --- | --- |
| A | `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42` |
| A transpose | `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66` |
| B (captured contaminated matrix) | `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4` |
| RHS | `C8ADAA98B7B1B7484CAF2A1C4E44D7FD0106D62BCC8FB10084D11CD877CDABFB` |
| Raw solve vector | `F4D51DC00DBAB73F63322A73692EBEA13CAEC2D0A1204A514CBE39329DF8B8E2` |
| Localization | `3628725A54B97344F501C0E44D32338A0B5CF6733D6022B9DD7A4C82C890BD63` |
| HJB status | `2B2436E575BB057C9C4BD51F1F6CC5979CBBDACB78D9C9A452BFE90B6181CAF5` |
| Warning/traceback | `45C63691B33BEB75F651DD15F09E725D4B919EB78222DD09812473290B72141D` |
| Household ledger | `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F` |
| HJB ledger | `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F` |

The independent, no-overwrite analysis root is
`D:\ProjectTemp\ch5-mp4c-2018-captured-operator-nullspace-forensic-reissue-20260903-001`.
Its `audit_manifest.json` hashes to
`507EBE9DB8A186E18895E42796EEDD5DA6034C42E97DC5AD466748926B989D2D`;
all 15 listed forensic outputs re-hashed to their manifest values.  Its ledger
records zero scientific calls and lists `spsolve`, density solve, model execution,
and postmortem rerun as forbidden operations not called.

## Fixed faithful row and captured objects

The source-faithful expression `floor(0.37 * 800) - 1` gives zero-based row
`295` (one-based `296`).  Under the required Fortran order
`b_index + a_index*20 + z_index*20*20`, this is:

| b index / value | a index / value | z index / value |
| --- | --- | --- |
| `15` / `3.526315789473684` | `14` / `7.368421052631579` | `0` / `0.8` |

The captured A is 800 by 800 with 3,106 stored entries.  The captured RHS has
one nonzero at row 295, value `0.007`; the captured raw vector has 800 nonfinite
entries.  The faithful source replaces row 295 of `A.transpose()` with its unit
row, so its additional condition on a candidate null direction is `v[295] = 0`.

## Nullspace geometry and rank-only row checks

Dense float64 SVD of captured `A.transpose()` found the numerical null direction
after normalizing `max(abs(v)) = 1` and choosing positive sign at the maximum.
Its smallest singular value is `2.1488433480633367e-08`; the rank tolerance is
`3.821460885301736e-05`, yielding rank 799 and nullity 1.  The residual is
`||A'v|| = 1.2795425290966635e-12`, or
`2.8229220401128884e-21` after the reported scale normalization.

| Dense-null statistic | Value |
| --- | --- |
| min / median / max `abs(v)` | `0` / `1.3588855553351861e-15` / `1` |
| sign counts (positive / negative / exact zero) | `340` / `459` / `1` |
| `v[295]` | `-3.739201849614122e-14` |
| `abs(v[295]) / max(abs(v))` | `3.739201849614122e-14` |
| components below `1e-14`, `1e-12`, `1e-10`, `1e-8` | `613`, `770`, `776`, `776` |

The exact zero-based index arrays for each threshold are persisted in
`nullspace_geometry.json` under `dense_method.relative_threshold_indices` and
are bound by its forensic-root manifest entry
`A2E2CD34BD1F6A460741D195236BAD3855AF7673A2E281DBFFDAC06BAF380235`.
This avoids an abbreviated hand transcription of the 613--776-element sets.

For B, `||Bv|| = 1.2789121616897769e-12`, normalized
`2.821531325849158e-21`; its unit-row residual is
`Bv[295] = -3.739201849614122e-14`.  Thus the captured null direction satisfies
the new row condition to null-scale precision and survives the faithful row
replacement.

An attempted independent sparse method,
`scipy.sparse.linalg.svds(which='SM')`, returned
`ArpackNoConvergence` after 100,001 iterations with zero converged vectors.  It
was recorded and not retried.  Dense SVD is therefore the completed numerical
null-direction method; sparse nonconvergence is not presented as confirmation.

Only in-memory rank/singular-value checks were made for row replacements:

| Replacement row | `abs(v[row])` | Rank / nullity | Smallest singular value | Result |
| --- | ---: | ---: | ---: | --- |
| faithful 295 | `3.739201849614122e-14` | 799 / 1 | `6.140548357084362e-16` | singular |
| `argmax(abs(v)) = 620` | `1` | 800 / 0 | `0.0009447160055667784` | full numerical rank |
| dominant closed-SCC high-support row 620 | `1` | 800 / 0 | `0.0009447160055667784` | full numerical rank |
| near-zero row 0 | `0` | 799 / 1 | `4.221401492922475e-16` | singular |
| near-zero row 28 | `1.137518029574275e-22` | 798 / 2 | `5.205557863861225e-15` | singular / more deficient at this tolerance |

No row was changed in production and no counterfactual density was computed.

## Conservation and topology

The maximum absolute compensated row residual is `5.209558481541731` at row
779; its row-scale relative residual is `0.266499494867899`.  The largest
relative residual is `0.6977482242708176` at row 785.  The maximum operator
rate is `152113673.94362345`, so the absolute maximum divided by that global
maximum rate is `3.424779867898335e-08`.  This small global-rate ratio does not
make the material row-scale residuals floating cancellation: compensated and
ordinary sums agree for the listed high-relative-residual rows.

| Relative residual quantile | Value |
| --- | ---: |
| median | `2.721300960200666e-17` |
| 90th percentile | `6.402243893638829e-17` |
| 99th percentile | `0.2793798499948078` |
| maximum | `0.6977482242708176` |

The faithful row itself is conservative to this calculation: residual
`6.106226635438361e-16`, scale `22.20644030475451`, and relative residual
`2.7497548241133398e-17`.  This forensic records the mixed scale picture, not
a generator-defect or repair conclusion.

The graph used the required source orientation `i -> j` for positive stored
offdiagonal `A[i,j]` values.  Across thresholds `>0`, predecessor
`3.37760206345069e-08`, max-rate times `1e-14`
(`1.5211367394362346e-06`), and max-rate times `1e-12`
(`0.00015211367394362345`), it has 139 SCCs and three closed SCCs of sizes
2, 24, and 4.  At max-rate times `1e-10` (`0.015211367394362347`), it has
145 SCCs but the same three closed sizes and memberships.  Row 295 is in no
closed SCC at every threshold.

The closed memberships are `[19,419]`,
`[140,141,160,161,180,181,200,201,220,221,240,241,540,541,560,561,580,581,600,601,620,621,640,641]`,
and `[299,319,699,719]`.  The 24-state class carries
`0.9999999999938031` of absolute null mass and has subblock smallest singular
value `3.9017424942823294e-16`; the 2- and 4-state classes carry respectively
`2.7844856518239376e-12` and `2.914305870290716e-13` of that mass.  This
reconciles robust reducible topology with numerical nullity one: the null
direction is concentrated in the 24-state closed class, rather than assigning
one independent numerical null direction to every graph-closed class.

## Existing Anhui HJB trajectory

The ledger-only trajectory has 24 Anhui rows.  There are 14 earlier
nonconverged Anhui HJB calls before the captured singularity.  At outer 23,
call 694 was nonconverged after 100 iterations with statistic
`0.12567033828017027`; its KFE path was
`MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE` and execution continued.
At outer 24, call 725 (安徽, index 11) was likewise nonconverged after 100
iterations, with statistic `0.3038218386543494`, and is the first captured
singularity.

| Anhui field | Outer 23 / call 694 | Outer 24 / call 725 |
| --- | ---: | ---: |
| `rah`, `rb`, `tau`, `Tt`, `rb_gap` | `0.09`, `0.02`, `0.05`, `0.1`, `0.07` | unchanged |
| `w` | `16.82268097415326` | `16.82014806560587` |
| `Yt` | `36608534.52765006` | `36636882.21977386` |
| `Lt` | `3199759.315398926` | `3210665.858026796` |
| `Kt` | `115362287.79356368` | `115362461.89160682` |
| `Zt` | `0.7163967429125945` | `0.6650485431957093` |
| `GovInv` | `115261012.11434016` | `126787113.32577418` |

The exact outer-24 call window 714--725 is preserved in
`outer24_local_call_window.csv`: calls 714--724 are HJB-converged and call 725
is Anhui's nonconverged capture.  The full 24-row trajectory, including every
requested state and HJB field, is in `anhui_hjb_trajectory.csv`; both files are
covered by the new forensic manifest.  These records show recurrence and
association, not that HJB nonconvergence is sufficient to produce this KFE
singularity.

## Causal ladder and boundary

1. **Proximal algebraic cause:**
   `FIXED_CONTAMINATED_ROW_FAILS_TO_REMOVE_UNIQUE_NULL_DIRECTION__ZERO_OR_NEAR_ZERO_NULL_COMPONENT_AT_SOURCE_ROW`.
   The captured B retains the dense-SVD null direction at null-scale residual,
   and a row with unit null component lifts numerical rank while the faithful
   row does not.
2. **Captured-operator structural classification:**
   `CAPTURED_OPERATOR_NULLSPACE_SUPPORT_AND_REDUCIBILITY_EXPLAIN_ROW_GAUGE_FAILURE`.
   The support concentration, repeatable closed-class topology, and rank-only
   replacements explain why this source row is an ineffective gauge for the
   captured operator.  Conservation findings are recorded but are not a repair
   diagnosis.
3. **Upstream HJB association:**
   `HJB_NONCONVERGENCE_ASSOCIATED_WITH_FAILURE_BUT_NOT_SUFFICIENTLY_CAUSAL`.
   Earlier Anhui HJB nonconvergence occurred before the first captured KFE
   singularity; no upstream complete root-cause claim is made.

Accordingly, no HJB/KFE/diagnostic repair, altered row, second execution,
postmortem, coverage/parity/Results claim, or follow-on scientific route is
authorized by this report.  Any repair review requires a new live task and
separate L3/Owner authority.
