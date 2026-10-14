# V0.0.6 joint synthetic binding — execution report (PRE_FINAL/PRE_SEAL)

Authority: freeze `4857d9222580b491676cdf75951527eb06d16b49`, plan blob
`5c96485f9b70c4c4033675134768b1ff4fe2d188`; separate authorization
`ASTRA_APPROVED_EXECUTION__CH5_V0.0.6__SOURCE_ONLY_AND_SYNTHETIC_JOINT_BINDING_ONLY`.
Governance readback: `5bf594094c95f6fd093bfe53a559276e53d13d0b`.
Single parent baseline: `cf74384f151427f0b7071ac0461cede6ad6cdf11`, tree
`372c693ca3dccea716ae8caef382f513e5a2316e`. This document cannot contain its
future enclosing commit/tree or a test executed after that commit.

## Implemented behavior

The existing C8 synthetic integration seam now requires joint preparation and
the explicit prepared synthetic middle stage before any consumer ledger action.
The new source contract reuses ArchiveDeclaration, InputDeclaration, the
five-field archive adapter, fixed-C8 model0/annual1/external-ID mapping, accepted
annual context/array and V001/V002's SYNTHETIC/NOT_REAL_SOURCE restriction.
V003's documentary producer/context/return/access distinctions are retained.
The V001/V002 modules are not imported through their scientific one_turn chain;
their accepted source-kind restrictions are referenced without activating it.

The check is functional: it rejects missing bt/other fields, nonfinite/bool
scalars, wrong axes/IDs/stages/checkpoints/source declarations/units, mismatched
annual context/master/parameters/distance, invalid S or field encoding, evidence
promotion and expired/reused preparations. It fingerprints all five vectors,
original scalar states, parameters, S and migration wedge including signed zero.
Rechecks run after labor, before wage and after wage. One attempted run closes
the preparation on completion or failure; attempted/completed/failed are separate.
These checks are ordinary engineering checks, not a hostile security seal.

## Static source crosswalk and boundaries

| Link | Unchanged accepted source | Candidate binding |
|---|---|---|
| C8 caller | k1b_turn8_outer_r2/run.py::_execute_after_gate | documented only; historical execution identity unknown |
| Terminal writer | optionb_turn2_household_integration.py::_solve_province | already-parsed invented terminals only |
| Five mass-form fields | k1b_turn5_turn6_bounded_continuation/run.py::_batch | existing archive adapter selects Ct/Lt/At/Bt/AtTax verbatim |
| 31 three-axis mapping | fixed_c8_input_binding.py::validate | same declarations and exact full-name external-ID join |
| Annual master | annual_observed_labor_context.py and annual_labor_array_adapter.py | same prepared immutable array at both synthetic boundaries |
| Labor then S/C1/firm then wage | integration.py + unchanged middle_stage.py | explicit synthetic callbacks only; no original callbacks loaded |

Original mass aggregation, HJB/KFE, grids, tolerances, payoff/timing, S law,
C1 formula, production exports and historical runners are unchanged. The
candidate does not absorb either original dirty source modification.

## Economic and evidence separation

Preserve population/per-person, no N=P/3. Runtime NU/MU conversion declarations
are not proof of household At/Lt/wage/period compatibility. Original units remain
ECONOMIC_UNIT_UNVERIFIED. All scalar units used in tests are explicitly invented.
The model0/annual1/canonical full-name map is checked as static contract text;
invented numerical fixtures do not pretend to be real province observations.

Annual phi uses origin q minus destination q, not the old Yt/Lt broadcast.
Migration receives old destination wages and origin tau; the wage boundary
receives new destination wages and destination tau. Independent asymmetric
scalar oracles check these roles, S quantities, same-S prior-raw payoff direction,
C1 residual, order and frozen original input values.

2017 observation/2018 target is retrospective. Methodological current-price
attribution remains adopted, direct_price_verified=False, price_verified=False,
release UNKNOWN, baseyear None. The executed annual fixtures use synthetic_fixture
price provenance; they cannot certify the methodological observed source bundle.
All source_authenticated/original-live/science/runtime/activation/Results claims
remain False or UNKNOWN. This is fixed-C8 conditional design, not a new GE.

## Development tests and exact final-tree gate

Only three new pytest files are collected. Run01: 35 passed, exit0, 1.3141413 s,
sampled peak working set 45,056,000 B. Static review then added signed-zero
fingerprinting, explicit S/layout/payoff roles and further rejection oracles.
Run02: 40 passed, exit0, 0.8950739 s, peak 45,301,760 B. No failed pytest
process or retry has occurred at sealing. Telemetry printing was added after
run02 and is covered only by the pending final-tree run, not retrospectively.

Final exact commit/tree test is PENDING at sealing. Its source-view hashes,
process receipt, stdout/stderr hashes, runtime versions, resource measurements
and final Git remote readback are recorded outside this candidate in LOCAL_ONLY
delivery receipts. A pre-seal pass is not final-tree evidence. Maximum permitted
pytest processes remains six, not six per candidate or session.

## Import/output and protection review

Only reviewed engineering leaf bytes plus installed Python/pytest/NumPy and
their runtime closure are loaded. No package initializer, conftest, old test,
runner, scipy, exports or original scientific callback is loaded. Tests block
those import roots, trap observed-source preparation, and check each leaf against
the candidate-view hash manifest. Accepted helper bytes are preloaded explicitly;
its ordinary source-loader branch is not entered. No original data is exported.

Bytecode/cache and plugin autoload are disabled. Exact test paths, temporary
directory, stdout/stderr and source manifests are confined to the new local
candidate task root. Full command/process details are LOCAL_ONLY. No installation,
network client, scientific/native model backend or protection experiment is used.
Normal runtime NumPy native dependencies are the expressly allowed NumPy runtime,
not a claim to have audited every installed binary or established A16 isolation.

Original worktree HEAD/index/eight dirty bytes and untracked/ignored path lists
are checked against the intake snapshot; the final comparison is external to
this pre-seal report. No original untracked/ignored payload or B3 object is read.
No original checkout operation, cleanup, deletion, main merge or force push.

Budget: eight hours; six pytest processes, 600 s each; 512MiB per-process memory
target; 256MiB operational + 32MiB local receipts + 2MiB public = 290MiB total.
Actual cumulative storage and time are reported in the final external receipt;
no storage class is exempted. RSS is sampled working set, not a universal bound
on all transient allocation or historical processes.

## One consolidated future Owner read request — REQUEST_ONLY

No real file below was opened, parsed or newly hashed. Existence, actual size
and trusted source binding remain UNKNOWN. Only after new exact Owner authority,
independent protection/final-chain review and an independently supplied historical
anchor, request one attempt per file, retry0, 37 attempted reads maximum:

- Under reports/ch5_k1b_turn8_outer_r2_20260925_run001/: execution_artifact_manifest.json
  <=1MiB; preflight.json <=256KiB; turn8/household_batch_receipt.json <=64KiB.
- Exactly 31 turn8/household/p{index:02d}_{short_name}/stationary_aggregate_receipt.json
  leaves, index 0..30 and canonical PROVINCE_ORDER short names, <=16KiB each.
  No recursive following of other manifest members. The independent anchor must
  bind leaf path/hash to batch province/checkpoint and historical producer code.
- Under reports/ch5_k1b_turn7_outer_r2_20260925_run001/:
  turn8_k1b_input_candidate.json <=2MiB and
  turn8_k1b_frozen_share_payoff_plan.npz <=64KiB.
- docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv
  <=64KiB, only if separately included in the exact authority.

Combined maximum 4,112,384 B (4,016KiB). Permissions must distinguish byte read,
one identity hash, JSON/NPZ/CSV parse and numeric field extraction; none is
implicit. Allowed extraction would be five mass_form scalars, declared
province/stage/checkpoint associations, entering states/parameters/population,
exact S/prior raw payoff members and the fixed distance transform. No solver,
aggregation recomputation, consumer call, unrelated receipt follow or output
export is requested. Full values stay LOCAL_ONLY in the authorized process and
expire after that bounded preparation; only redacted verdicts may be shared.
If independent provenance or access protection is absent, STOP before opening;
do not replace the source, expand caps or reopen old read budgets. This request
does not itself resolve A16/window or grant any future read.

## Terminal scope

This candidate requests independent SOURCE_ONLY_IMPLEMENTATION and
SYNTHETIC_ENGINEERING review only. It is not self-accepted. Preserve A16
FAIL_CLOSED, window UNACCEPTED, C9 PAUSED, CALL_LEDGER_UNRESOLVED,
model_activation=False, Results=False and all old CLOSED budgets.
Stop after one candidate push/readback and concentrated delivery:
WAIT_ASTRA_V006_IMPLEMENTATION_ACCEPTANCE / STOP. No V0.0.7.
