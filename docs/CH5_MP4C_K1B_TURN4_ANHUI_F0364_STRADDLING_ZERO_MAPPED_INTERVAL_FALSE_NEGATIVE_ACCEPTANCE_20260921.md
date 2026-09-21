# Chapter 5 K1B turn4 安徽 F0364 straddling-zero mapped-interval false-negative — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_GUARD_FALSE_NEGATIVE__NARROW_REPAIR_AUTHORIZED`

Accepted Builder terminal:

`PASS__K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC__GUARD_FALSE_NEGATIVE_CONFIRMED__NO_SOURCE_CHANGE`

Accepted classification:

`TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_GUARD_FALSE_NEGATIVE_CONFIRMED`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `3e11b05f497e4535e0655d64cba26a55bab9b582`
- candidate: `790350270d4ec07d61cc1765c042f2fd33b82b3c`
- candidate tree: `d22fea2781ff21f7174f9b732efc9f5d76667d47`
- ancestry: 1 ahead / 0 behind
- changed paths: 18
- all changed paths are task validator/test/evidence/report
- production source changes: 0
- CURRENT changes: 0
- ordinary push/readback/worktree claims: consistent with candidate report.

## Exact forensic acceptance

The exact 安徽 turn4 checkpoint4 F0364 cell is hash-bound:

- Git blob: `7ff0c9ff12ed39df1a2c1c55d195e10048914644`
- SHA-256: `F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65`.

The backward-liquid negative-transfer ordinary pair has an arithmetic-separated strict a-drift crossing:

- a-backward g_a = `1.8577376041602465`
- a-backward bound = `1.1059824302255312e-12`
- a-forward g_a = `-0.11099606925634653`
- a-forward bound = `1.165177247639271e-12`.

The forward-liquid pair does not have that crossing.

## D3 mapping

Independent arithmetic agrees with the candidate:

- `d_z=-5.840722762648187`
- `R=-0.3330414721146172`
- original illiquid derivative interval:
  `[-0.000536125311776913, 8.895604077208148e-05]`
- mapped q_b interval:
  `[-0.000267101992455363, 0.0016097854371494127]`
- sign topology: `STRADDLES_ZERO`
- accepted q_b-domain intersection:
  `(0, 0.0016097854371494127]`.

The Owner contract requires the selected liquid shadow q_b to be strictly positive. It does not require the entire mapped interval to lie inside the positive domain.

## Unique branch-local admissible candidate

Backward liquid:

- q_b = `0.0015039676061569449`
- q_a = `-0.0005008835855672058`
- q_b is finite, strictly positive, and inside the positive-domain intersection
- q_a lies inside the original closed illiquid derivative interval
- d = `-5.840722762648187`
- raw/canonical g_a = `0`
- g_b = `-17.978717494437753`
- backward direction: PASS
- D3 transfer KKT residual = `0`
- finite controls/value: PASS
- interior D2 admissibility: PASS
- Hamiltonian = `-0.06734914681687235`.

Forward liquid is outside the mapped interval, maps q_a outside the original derivative interval, and fails forward direction consistency.

Exactly one switching candidate is admissible.

## Causal source finding

Current selector blob:

`e8a1d72e23661576f14ac42b7dff6e3001837206`.

The exact strict-crossing path passes all earlier gates and exits first at:

`if implied_q_b_interval[0] <= 0.0: return None`

because the mapped lower endpoint is negative.

This is a whole-interval positivity implementation guard. It fires before the candidate can be judged by the accepted branch-local positive-q_b domain, q_a membership, direction, KKT, finite and D2 rules.

Classification A is therefore accepted as an implementation false negative, not a new economic law.

## Narrow repair authority

The next task may modify only the interior-b / interior-a / finite-negative-R strict-crossing path in `selector.py`.

For interior b and finite negative nonzero R:

1. preserve the sorted mapped q_b interval;
2. intersect its domain with q_b>0 without introducing a magnitude floor;
3. require the current branch-local persisted liquid derivative shadow p_b to be strictly positive and to lie in that positive-domain intersection;
4. require q_a=R*p_b to lie in the original closed illiquid derivative interval;
5. construct the candidate only through the existing switching candidate path;
6. preserve all existing direction, D3 KKT, finite, D2, deduplication, Hamiltonian and tie rules.

Must remain unchanged:

- active lower-b / upper-b negative-ratio behavior;
- ratio-zero fail closed;
- positive-ratio behavior;
- strict-crossing trigger;
- D1/D2/D3 equations;
- liquid-Z and joint switching;
- lower-a zero-kink;
- all tolerances, grid, Delta, solver and calibrations.

## Compatibility requirement

Because this is a production selector change, no fresh turn4 science may run until exact selected-policy identity compatibility is proven on all accepted predecessor household checkpoint paths:

- accepted turn1 run004: 408 policy maps
- accepted turn2 run005: 411 policy maps
- accepted K1B turn3: 408 policy maps
- total: 1,227 maps.

Replay uses exact persisted V and original state/scalars, selector only. No direct HJB update, D2/Q, KFE, aggregate or integration call.

Every replayed selected-policy identity must exactly match its accepted persisted identity.

Focused normal-selector parity must additionally prove both the prior Beijing F0364 candidate and the new 安徽 F0364 candidate.

## Evidence integrity

Forensic evidence root:

`reports/ch5_mp4c_k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic_20260921_run001/`

- entries: 13
- bytes: 23,826
- manifest SHA-256: `7A9DED5F12413F13E8CD827EE890A7D5BEF002EE5BC756A7476D10821B621E50`
- independent readback: PASS
- bad paths: 0
- zero production selector/root/HJB/KFE/integration calls: PASS.

## Route consequence

The next task implements the narrow correction, proves focused parity and full accepted historical policy-identity compatibility, and only then may execute one fresh bounded turn4 reexecution from the exact accepted turn4 entering state/share plan.

No turn5 household, K2, long outer path, GE or Results is authorized.
