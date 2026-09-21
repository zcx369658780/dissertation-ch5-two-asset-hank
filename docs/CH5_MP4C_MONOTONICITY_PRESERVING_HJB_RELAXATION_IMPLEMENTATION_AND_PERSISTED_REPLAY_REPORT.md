# Chapter 5 MP4C monotonicity-preserving HJB relaxation implementation and persisted replay

Date: 2026-09-21

Terminal:

`PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED__EXACT_PERSISTED_REPLAY_PASS__FRESH_HJB_NOT_RUN`

Results eligibility remains `FALSE`.

## Result

The Owner-adopted deterministic halving invariant-domain backtrack is implemented in the two authorized corrected-diagnostic HJB update paths. One shared production helper is defined in `nonlinear_continuation.py` and reused by `optionb_turn2_household_integration.py`; no production helper module was added.

The helper passed the exact accepted 黑龙江 persisted replay and all required negative tests. No fresh HJB solve, HJB update, selector map, Q rebuild, KFE, integration or turn2 runtime was executed.

## Git and authority binding

Live-main baseline:

`94e174ef2c500b246106a848713c1af232c1cd80`

Owner authority:

`OWNER_ADOPTED__MONOTONICITY_PRESERVING_HJB_RELAXATION__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK`

Accepted inputs were rebound exactly:

- run004 manifest: `1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`;
- design-gate manifest: `F54EDEAA8FC351981CD2CBD44F17FA58950155F12953B7983E174D5EAC0D2803`.

## Production implementation

The shared helper:

`monotonicity_preserving_relaxation(V_old,Vhat,b_nodes)`

implements the exact adopted contract:

1. require finite arrays of corrected shape `(20,20,2)` and 20 finite strictly increasing b nodes;
2. test the represented full candidate unchanged at `alpha=1`;
3. if needed, test exactly `alpha=2^-k`, `k=1,...,52`;
4. construct every relaxed candidate as `(1-alpha)*V_old+alpha*Vhat`;
5. require all 760 raw b slopes finite and strictly `>0`;
6. reject a candidate bitwise identical to `V_old`;
7. accept the first passing candidate;
8. otherwise raise exactly `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

No positive slope magnitude floor, clipping, alternate schedule, adaptive Delta, second solve or tolerance change was added.

### Integration ordering

Both HJB paths call the helper only after the existing unique direct solve passes its backward-error gate.

The existing `direct_update_arrays.npz` and direct-solve receipt continue to describe the full linear-system solution `Vhat`. A separate `relaxation_receipt.json` records:

- old and full candidate identities;
- full candidate edge census;
- every attempted alpha and represented candidate identity;
- finite, positive, zero and negative edge counts;
- stagnation result;
- accepted alpha/halvings;
- accepted next-state identity and value-change norm.

The accepted relaxed value, rather than `Vhat`, becomes the next nonlinear state.

## Production diff and source freeze

Production changes are exactly the two authorized paths:

- `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`.

Exact unchanged Git blobs:

| Authority | Path | Blob |
| --- | --- | --- |
| selector | `selector.py` | `e8a1d72e23661576f14ac42b7dff6e3001837206` |
| D3 cost/KKT | `cost.py` | `435705a50238aaeebe918430156bcc14df1ff794` |
| D2 generator | `generator.py` | `f86234340c6e09c7129225da1677614669754177` |
| D1 and derivative law | `option_a_step.py` | `e0fcbf01af9b1778d245d960fe85c592f55c032c` |
| terminal KFE support | `q1_kfe_validation.py` | `45f4b95024c4441809dba3fe27044f25b3339f0f` |

The `_terminal_kfe` function resides in the changed nonlinear file but its exact source hash is unchanged before/after:

`AB33B740159E9C499D82F7BEED0368761A6DA451CD4E43B4A242D22F547B094A`.

## Exact persisted replay

Only accepted saved `V_old` and `direct_update_arrays.npz::next_value` were loaded. The new production helper was called exactly once per pair.

| Update | Alpha | Halvings | Accepted SHA-256 | Full candidate equal | Minimum slope | Positive edges | Value-change inf |
| --- | ---: | ---: | --- | --- | ---: | ---: | ---: |
| 0→1 | `1.0` | 0 | `74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32` | yes, bitwise | `0.0042677403061128745` | 760 | `0.6230457816987043` |
| 1→2 | `1.0` | 0 | `2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA` | yes, bitwise | `0.004513872937454847` | 760 | `0.27122303476390464` |
| 2→3 | `0.5` | 1 | `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF` | no, relaxed | `0.005032838660371801` | 760 | `0.017682618173863407` |

For 2→3, negative edges=`0` and zero edges=`0`. Every replay identity and scalar matches the accepted design-gate evidence exactly.

## Focused and negative tests

Focused result: `10 passed`.

Covered:

- alpha=1 exact passthrough;
- one-halving exact 黑龙江 replay;
- nonfinite old/full input rejection;
- wrong-shape rejection;
- bitwise stagnation rejection;
- signed-zero representation is distinguished by the bitwise check;
- 53-attempt exhaustion with the exact terminal;
- zero slope rejected by strict positivity;
- an arbitrarily small represented positive slope accepted, proving no magnitude floor.

`py_compile` passed for both changed production files, the focused test and validator.

## Scientific-call ledger

- persisted NPZ loads: 6;
- persisted JSON loads: 1;
- production relaxation-helper persisted replay calls: 3;
- new direct linear solves: 0;
- HJB update executions: 0;
- selector maps: 0;
- production root-helper calls: 0;
- D2/Q rebuilds: 0;
- KFE/SVD: 0;
- aggregates/integration: 0;
- turn2 replay/rerun: 0;
- turn3: 0;
- MATLAB: 0;
- GE/Results: 0;
- scientific retry/tuning: 0;
- fresh scientific runtime calls: 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_implementation_persisted_replay_20260921_run001/`

- manifest SHA-256: `A2C9310E7BA2EB284F2D14B5E270739CC2CCDC9DD39A8FFEC2B0F362D3A3C51F`;
- entries: 10;
- bytes: 20,147;
- independent readback: `PASS`;
- bad paths: none.

CURRENT was not modified and no successor was published.
