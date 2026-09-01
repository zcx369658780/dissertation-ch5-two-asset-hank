# CH5 TWO ASSET HANK MP4B L3 FORMAL CORRECTED2009 STATIONARY PARITY ACCEPTANCE REPORT

Date: 2026-09-01

## Terminal verdict

`MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED`

Acceptance level:

`CORRECTED2009_MULTI_PROVINCE_STATIONARY_PARITY_ACCEPTED__MULTIYEAR_AND_DYNAMICS_NOT_YET_ACCEPTED`

## Authority and continuity

- L3 acceptance task authority: `de935a183a4891628b9506cd549dac48a656320b`.
- Required predecessor comparator execution: `4daf9afcb242f38613e850d430baf9768783dca5`.
- Predecessor comparator terminal: `MP4B_POST_LT_PREV_REPAIR_COMPARATOR_ONLY_FORMAL_PARITY_EVIDENCE_PASS`.
- Predecessor comparator classification: `MP4B_POST_LT_PREV_REPAIR_CORRECTED2009_FINAL_COMPARATOR_PASS__L3_STATIONARY_PARITY_ACCEPTANCE_PENDING`.
- Comparator artifact SHA-256: `7E88B3A4F342B1870AFD56CB4789C621643A3C163E916B02601E4BD1A35F39E5`.

The L3 review is read-only. No MATLAB, Python stationary/HJB/KFE/household/MP2/MP3, comparator replay, other year, shock, AR(1), transition/IRF, R5 or Results execution was performed.

## Accepted scientific chain

The acceptance is based on the complete corrected-2009 evidence chain:

1. household-level MATLAB/Python parity was previously accepted under a frozen same-input comparator;
2. corrected-2009 source binding and province identity were audited and frozen;
3. instrumented MATLAB chronology was demonstrated bitwise identical to the preserved MATLAB baseline across the frozen final-state fields;
4. a Python source-layer defect was isolated under same-input evidence: same-turn household `Lt` was not mapped into the firm reference `Lt_1/Lt_prev` role;
5. the source-faithful repair mapped `household.household_lt[index]` into `firm_source["Lt_prev"]`, while preserving current destination firm labor as `migration.lt_supply[index]` and preserving same-turn `AtTax`;
6. after the repair, one and only one corrected-2009 Python stationary execution completed with `SOURCE_CONVERGED`, 184 turns, 5704 household calls, and final household convergence 31/31;
7. previously material branch differences disappeared: the turn-8 Shanghai/Qinghai reset exchange was removed, the turn-154 Zhejiang MATLAB-only low action disappeared, and final wage-boundary categories aligned;
8. the separately authorized final comparator completed once with no rerun and reproduced the post-repair read-only final-state evidence.

## Exact categorical acceptance evidence

The final comparator establishes exact MATLAB/Python equality for all frozen terminal categories:

- outer turns: `184 / 184`;
- household converged count: `31 / 31`;
- `ra` upper count: `0 / 0`;
- `ra` lower count: `0 / 0`;
- wage upper count: `7 / 7`;
- wage lower count: `17 / 17`.

Province identity is accepted for all 31 provinces after only the previously frozen reversible MATLAB terminal `省`/`市` suffix projection. There is no province permutation, fuzzy matching, or hidden reorder.

## Continuous final-state acceptance evidence

The frozen field map contains 31 provinces by 20 continuous fields:

`Ct, At, Bt, Lt, Lt_supply, Kt_supply, rah, Kt, Yt, mt, KNratio, w, wjt, rk, ra, GovInv, rb, it, Zt, Govinc`.

The final comparator reports overall maximum normalized difference:

`3.835889478194021e-11`

at 湖北 `At`.

National comparator evidence:

| Field | MATLAB | Python | Normalized difference |
|---|---:|---:|---:|
| `Ct` | 283.3909431582526 | 283.39094315824553 | `2.487229782359025e-14` |
| `At` | 47.95553248807161 | 47.95553248833114 | `5.41179965626544e-12` |
| `Bt` | 65.2831672243048 | 65.28316722428993 | `2.279111985436448e-13` |
| `Yt` | 350556701.89460325 | 350556701.8946058 | `7.311227289308414e-15` |

No new tolerance was invented and no accepted threshold, grid, equation, solver algorithm, comparator formula or scientific tolerance was loosened to obtain these results.

The remaining continuous non-bitwise differences are therefore accepted as source-faithful cross-language numerical non-identity at the frozen evidence level, not as a remaining scientific implementation defect.

## Formal L3 acceptance decision

The evidence is sufficient to accept corrected-calendar-2009 MATLAB/Python multi-province stationary parity.

Accepted marker:

`MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED`

This acceptance closes the corrected-2009 stationary forensic-debugging gate. A new 2009 stationary rerun is not required for parity acceptance unless future code changes invalidate a frozen scientific identity.

## Scope not accepted by this decision

This acceptance does not establish or approve:

- other calendar years;
- multi-year/annual batch parity;
- controller-threshold sensitivity;
- AR(1) shock semantics or execution;
- transition dynamics or IRFs;
- historical R5 results;
- dissertation or journal-paper Results claims.

Those require separate tasks and evidence.

## Recommended next route

Proceed to a bounded multi-year annual steady-state parity route using corrected-2009 as the frozen anchor. The batch design should avoid repeating full forensic diagnostics for every year: run each year independently with immutable manifests and fail-isolate only anomalous years. After annual steady-state coverage is accepted, move to the Python shock/AR(1) route and then return the project emphasis to paper reconstruction and improvement.
