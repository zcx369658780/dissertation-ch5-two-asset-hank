# Chapter 5 interior-b negative-ratio repair / turn-1 parity / turn-2 run003 — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_FAIL__INTERIOR_B_NEGATIVE_RATIO_REPAIR_PASS__TURN1_408_POLICY_PARITY_PASS__TURN2_BEIJING_TIANJIN_HJB_KFE_PASS__HEBEI_F0005_NO_ADMISSIBLE_POLICY_FIRST_FAILURE_CONFIRMED`

Results eligibility remains `FALSE`.

## Independent Git review

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

- live-main launch baseline: `c75d0b0de075278c690bc412657a0f4f10fa32e9`
- implementation commit: `5a350ad2f1ccc62d9f8c211b740416196136cee1`
- Builder candidate: `f178ec24b9b62814d20ec4041380e07e2d878849`
- candidate tree: `125463fe73addc0b366624e3ae5e19c7f5bec9fd`
- ancestry: 2 ahead / 0 behind
- merge-base: exact launch baseline
- remote candidate branch: exact candidate SHA
- changed paths: 316 unique paths
- CURRENT paths changed by Builder: 0

The first commit changes exactly five implementation/test/validator paths. The second commit publishes the report and run003 evidence. No unrelated scientific source change was found.

## Selector repair acceptance

The only scientific-source change is in:

`src/ch5_two_asset_hank/corrected_diagnostic/selector.py`.

The change is within the authorized interior-liquid negative-ratio switching contract:

- finite negative nonzero D3 ratio is allowed when liquid `b` is interior;
- the two mapped `q_b` endpoints are divided by the ratio and then sorted;
- ratio zero remains fail closed;
- a finite negative ratio remains fail closed when a liquid face is active;
- existing D3/KKT/direction/finite/Hamiltonian laws remain unchanged.

The active-upper-b negative enumeration repair remains in force. Cost, generator, nonlinear continuation/HJB/KFE, initial-turn integration, turn-2 integration and canonical integration source blobs are unchanged from the launch baseline.

Focused tests: 15/15 PASS.

## F0364 exact normal-selector parity

Both the focused selector check and the normal Beijing checkpoint-5 runtime map reproduce the accepted F0364 switching policy exactly:

- transfer: negative
- derivative branches: `b=backward, a=zero`
- `q_b=0.006091715618507631`
- `q_a=-0.0045978913784868415`
- `d=-7.8384208979658965`
- `g_a=0`
- `g_b=-4.227123020026542`
- transfer-KKT residual: `0`
- Hamiltonian: `-0.11188508398929994`
- admissible: true
- D3 ratio: `-0.7547777451261338`
- mapped `q_b` interval: `[0.004111019263931103, 0.006526149020033277]`

The normal-map receipt was captured without an additional selector call.

## Mandatory accepted turn-1 compatibility gate

The hard gate passed before fresh turn-2 science:

- accepted maps: 408
- maps replayed: 408
- exact selected-policy identity matches: 408
- mismatches: 0
- selector evaluations: 326,400
- accepted/replayed ordered digest:
  `E23F77D21521B31C62CFEFFFFA1ACF4C39D69D577A6CFBA697DAB03AE9428B6B`

Replay-only science ledger:

- HJB direct updates: 0
- D2/Q assemblies: 0
- SCC/KFE/SVD: 0
- aggregate/integration: 0
- retries: 0

Root counts were separately preserved:

- scalar roots: 130,705
- interior-z roots: 24,265
- interior-a switching roots: 392
- joint switching roots: 49

Therefore the accepted turn-1 path remains compatible with the repaired selector and is not rewritten.

## Fresh turn-2 entering authority

The run binds exactly to:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

- accepted Git blob: `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- 31-row province order: PASS
- raw entering payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`

## Fresh turn-2 run003 acceptance boundary

Beijing and Tianjin each completed:

- corrected HJB through checkpoint 12;
- Owner-adopted unique-closed-class terminal KFE;
- stationary aggregate evaluation.

For both provinces the KFE evidence preserves the accepted terminal authority:

- one closed-class support solve;
- restricted `Q_CC` dense GESVD only;
- local and inherited rank/nullity = 39/1;
- strictly positive closed-class mass;
- transient mass exactly positive-zero;
- one original full-`Q` `Q.T@p` check;
- full-space 800x800 GESVD = 0;
- retry = 0.

The first new scientific failure is then:

- province: 河北
- province index: 2
- checkpoint: 1
- F-order flat: 5
- index: `(5,0,0)`
- cell: `v001_f0005_b005_a000_z000`
- state: `b=-0.1578947368421053, a=0, z=0.8`
- selector outcome: `NO_ADMISSIBLE_POLICY`
- attempted candidates: 15

The failing map stops before D2/Q. No rescue, tuning, new rule or further province execution occurred.

## Fresh turn-2 ledger

Accepted ledger:

- source-native initialization: 3
- labor roots: 2,400 / 2,400
- completed policy maps: 27
- D2/Q assemblies: 27
- direct HJB updates: 25
- selector evaluations: 21,600
- scalar selector roots: 9,644
- interior-z roots: 1,979
- restricted GESVD: 2
- SCC decompositions: 2
- normalized stationary candidates: 2
- `Q.T@p`: 2
- aggregate evaluations: 2
- scientific retries: 0
- full-space 800x800 GESVD: 0
- turn-3 household: 0
- K1B: 0
- K2: 0
- GE / annual / shock / IRF / welfare / Results: 0

The counts reconcile with 13 completed maps for Beijing, 13 for Tianjin and Hebei checkpoint 0, followed by the partial failing Hebei checkpoint-1 map.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921/`

- top manifest SHA-256:
  `E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403`
- manifest entries: 306
- bytes: 4,583,535
- independent readback: PASS
- bad paths: none
- pre/post execution source freeze: exact match

The generic manifest routine intentionally excludes files named `sealed_manifest.json` and `independent_readback_receipt.json`; all 306 manifest entries are present in the published candidate.

## Scientific acceptance

The Builder terminal

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

is accepted as the task's valid first-failure outcome, not as a failure of the repair itself.

Accepted conclusions:

1. the authorized interior-b finite-negative-ratio repair is implemented correctly;
2. F0364 is repaired in normal runtime;
3. accepted turn-1 policy identities remain exactly unchanged;
4. fresh turn-2 execution was therefore legally reached;
5. Beijing and Tianjin turn-2 household/KFE/aggregate blocks pass;
6. 河北 checkpoint-1 flat-5 is the first unresolved scientific object.

Not accepted:

- any diagnosis or repair of 河北 F0005;
- turn-2 completion;
- turn-3 science;
- K1B/K2/GE/Results.

## Next gate

The next task is zero-science forensic attribution of 河北 checkpoint-1 flat-5 at active lower-`a` / interior-`b`.

It must determine whether the current `NO_ADMISSIBLE_POLICY` is:

1. a composition/implementation false negative under already adopted lower-`a` zero-kink and interior-liquid `Z` switching authorities;
2. a legitimate fail-closed outcome under those authorities; or
3. a scientific-law composition ambiguity requiring an Owner decision.

No selector repair or model rerun is authorized by this acceptance.
