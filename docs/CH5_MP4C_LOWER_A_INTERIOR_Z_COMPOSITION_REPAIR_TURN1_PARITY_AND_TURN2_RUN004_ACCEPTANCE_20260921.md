# Chapter 5 lower-a / interior-Z composition repair, turn-1 parity, turn-2 run004 — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_FAIL__LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_PASS__TURN1_408_POLICY_PARITY_PASS__TURN2_FIRST_7_PROVINCES_HJB_KFE_PASS__HEILONGJIANG_F0063_NO_ADMISSIBLE_POLICY_FIRST_FAILURE_CONFIRMED`

Results eligibility remains `FALSE`.

## Independent Git review

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

- live-main launch baseline: `79649059282540d6bdd4192ecc3b01771a7152bc`
- implementation commit: `2fbf268f938ac5cb76c33c008f99ae67a18a8a21`
- Builder candidate: `4cbd4261be31c237a99cade68ccb35a13c9306b9`
- candidate tree: `dfe2a8085960685870b5f7587265b51cf733e7ee`
- ancestry: 2 ahead / 0 behind
- merge-base: exact launch baseline
- changed paths: 1,161 unique paths
- implementation/test/validator paths before execution: 5
- evidence/report publication paths: 1,156
- production scientific source changed: exactly `selector.py`
- CURRENT paths changed by Builder: 0

Remote branch SHA/tree readback matches the candidate.

## Composition repair acceptance

The production source change is confined to the authorized active-lower-a + zero-kink + interior-liquid-Z composition logic.

The repair introduces a helper that reconstructs the raw liquid drift and the existing prospective floating-point bound at a lower-a / zero-kink endpoint when the full endpoint candidate had already been rejected by an empty lower-a kink/multiplier intersection.

That helper:

- keeps `d=0`;
- uses the existing derivative endpoint `q_b`;
- uses the existing deterministic lower-a shadow only for the existing arithmetic-bound construction;
- does not make the ordinary endpoint candidate admissible;
- does not alter the ordinary candidate's persisted rejection semantics.

`_interior_z_candidate` uses this raw endpoint screen only for the exact active-lower-a + zero-kink family when endpoint full-candidate data are unavailable. It otherwise preserves the prior path.

After a strict crossing, the repair calls the existing `_one_interior_z_root` and then the existing `_candidate(...,q_b_override=root,...)` path. Therefore the lower-a kink interval, deterministic `q_a`, multiplier, KKT, feasibility, direction, finite and Hamiltonian checks are recomputed at the switching shadow exactly as already adopted.

No new equation, KKT law, boundary law, root method, model tolerance, calibration or solver is introduced.

Cost, boundary/generator, nonlinear HJB/KFE, initial-turn integration, turn-2 integration and canonical integration source blobs remain unchanged.

## Focused and regression gates

Focused tests: 22/22 PASS.

Accepted regressions:

- active liquid faces unchanged;
- ratio zero remains fail closed;
- no-crossing lower-a family invokes no interior-Z root;
- ordinary endpoint rejection semantics unchanged;
- F0364 focused parity PASS;
- F0364 normal-runtime parity PASS without an additional selector call.

## 河北 F0005 production-root result and Reviewer contract correction

The repaired normal selector and the actual runtime map both select the already-authorized combined policy:

- active constraints: lower-a
- transfer: zero-kink
- branches: `a=forward, b=zero`
- `d=0`
- `g_a=0`
- `g_b=0`
- transfer-KKT residual: 0
- lower-a complementarity residual: 0
- admissible: true.

The frozen production root path returns:

- `q_b=0.012085132579009492`
- `q_a=0.010876619321108543`
- `lambda_a=0.0002848986323410619`
- Hamiltonian `-0.12808167052185432`
- raw zero-drift residual `1.7763568394002505e-15`
- inherited arithmetic bound `2.901541422966794e-13`.

The earlier zero-science forensic's independently reconstructed Decimal root rounds to the nearby reference:

`0.012085132579009488`.

The production result is 2 binary64 ULP above that reference.

Reviewer ruling:

`FORENSIC_DECIMAL_REFERENCE_IS_NOT_A_PRODUCTION_BITWISE_ROOT_ORACLE__FROZEN_ROOT_LAW_CONTROLS`.

The prior task's literal binary64 target is corrected on review: the scientifically authoritative production result is the output of the already frozen 513-point log-screened Brent path under its unchanged configuration and model tolerance. Requiring the independent Decimal-rounded bit pattern would conflict with the explicit instruction not to alter that root law.

This acceptance does not relax or change a model/root tolerance. The original production residual is preserved and is far inside the already frozen arithmetic bound. The runtime receipt also preserves the original value rather than rewriting it to the forensic reference.

The policy branch, active set, KKT objects and Hamiltonian semantics match the accepted forensic.

## Mandatory turn-1 compatibility gate

The hard gate passed before fresh turn-2 science:

- accepted maps: 408
- maps replayed: 408
- exact selected-policy identity matches: 408
- mismatches: 0
- accepted/replayed ordered digest:
  `E23F77D21521B31C62CFEFFFFA1ACF4C39D69D577A6CFBA697DAB03AE9428B6B`

Replay ledger:

- selector evaluations: 326,400
- scalar roots: 130,794
- interior-Z roots: 24,354
- interior-a roots: 392
- joint roots: 49
- HJB direct updates: 0
- D2/Q: 0
- SCC/KFE/SVD: 0
- aggregate/integration: 0
- retries: 0.

Thus the accepted turn-1 policy path remains exactly unchanged and fresh turn-2 run004 was legitimately reached.

## Fresh turn-2 entering authority

The run binds to the exact accepted entering-state artifact:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

- accepted Git blob: `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- raw entering payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- 31-row province order: PASS.

## Fresh turn-2 run004 accepted progress

The first seven provinces in canonical order completed household HJB, Owner-adopted unique-closed-class terminal KFE and stationary aggregate evaluation:

1. 北京
2. 天津
3. 河北
4. 山西
5. 内蒙古
6. 辽宁
7. 吉林

For those seven provinces the accepted ledger records:

- SCC decompositions: 7
- restricted closed-class GESVD: 7
- normalized stationary candidates: 7
- full-Q `Q.T@p`: 7
- full-space 800x800 GESVD: 0
- KFE retries: 0.

The next province, 黑龙江, reaches the first new scientific failure before D2 at checkpoint 3 / flat 63.

## First new scientific failure

Exact object:

- province: 黑龙江
- province index: 7
- checkpoint: 3
- F-order flat: 63
- index: `(3,3,0)`
- cell: `v003_f0063_b003_a003_z000`
- cell SHA-256:
  `17C5808B073AF454172EA0478EB144CE1E6145F7657EF0C06C78C747E953F6D3`
- selector outcome: `NO_ADMISSIBLE_POLICY`
- stage: selector outcome
- geometric faces: none.

Persisted state:

- `b=-0.8947368421052633`
- `a=1.5789473684210527`
- `z=0.8`
- `p_a^B=0.026049395991859955`
- `p_a^F=0.024439409021974706`
- `p_b^B=-0.0002428532863339202`
- `p_b^F=0.014463823441006161`.

The negative backward liquid derivative is the most important new structural feature.

Persisted candidates show:

- every backward-liquid ordinary family rejects immediately because the liquid shadow is nonpositive under the existing no-derivative-floor rule;
- forward-liquid candidates have finite positive liquid shadows but are not admissible under current direction/KKT conditions;
- no interior-Z candidate is emitted;
- no active geometric face exists.

No diagnosis or repair of this object is accepted by run004 itself.

## Fresh turn-2 scientific ledger

Accepted consumption up to the first failure:

- source-native initializations: 8
- labor roots attempted/returned: 6,400 / 6,400
- selector evaluations: 80,800
- completed policy maps: 101
- D2/Q assemblies: 101
- direct HJB updates: 94
- converged province aggregate evaluations: 7
- scalar selector roots: 34,735
- interior-Z roots: 7,477
- SCC: 7
- restricted GESVD: 7
- normalized stationary candidates: 7
- full-Q checks: 7
- full-space GESVD: 0
- scientific retries: 0
- solver substitutions: 0
- household batch/integration: 0
- K1A/C1/firm/wage/monetary/fiscal: 0
- canonical next payoff: 0
- turn3/K1B/K2/GE/annual/shock/IRF/welfare/Results: 0.

The Builder stopped exactly at the first new scientific failure. No rescue, tuning or retry occurred.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/`

- manifest entries: 1,146
- total bytes: 16,835,962
- top manifest SHA-256:
  `1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`
- independent readback: PASS
- bad paths: none
- pre/post execution source freeze: exact match.

All 1,146 top-manifest entries are present in the published candidate. As in the established evidence routine, the top manifest excludes itself, the detached independent readback, and the seven nested terminal-KFE sealed manifests by filename.

## Scientific acceptance

Builder terminal:

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

is accepted as the valid first-failure terminal.

Accepted conclusions:

1. lower-a / interior-Z composition repair is scientifically and implementation-wise accepted;
2. 河北 F0005 is repaired under the frozen production root law;
3. F0364 remains accepted;
4. accepted turn-1 selected-policy identities remain 408/408 exact;
5. fresh turn-2 run004 legally progressed through seven complete province household/KFE blocks;
6. 黑龙江 checkpoint3 / flat63 is the new first unresolved scientific object.

Not accepted:

- any diagnosis of 黑龙江 F0063;
- any derivative floor or replacement;
- any one-sided or extrapolated interior-Z rule;
- turn-2 completion;
- integration;
- turn3;
- K1B/K2/GE/Results.

## Next gate

The next task is a zero-science forensic of 黑龙江 F0063.

It must determine whether the current `NO_ADMISSIBLE_POLICY` is:

1. supported by existing q_b-domain, upwind and interior-Z authority;
2. another implementation omission under already adopted authority; or
3. a case where continuation would require a substantive Owner decision to extend the interior-Z law to a nonpositive one-sided liquid derivative/shadow.

No production repair or model rerun is authorized by this acceptance.
