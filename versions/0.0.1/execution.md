# V0.0.1 execution candidate: synthetic household bridge

Date: 2026-10-13. Candidate qualification: `SYNTHETIC_ENGINEERING` only.
Final acceptance belongs to Astra; this document does not declare ACCEPT.

## Current authority and deliverable identity

- Frozen plan: [6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8/versions/0.0.1/plan.md).
- Independent approval: [837b99dff12f1b263fd7f4b80c43e19cf4efaa48](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/837b99dff12f1b263fd7f4b80c43e19cf4efaa48/versions/0.0.1/authorization.md).
- Baseline: `a1db8c114dec0ab69d69a5576e153a7f868cba0e` in the unique authorized model worktree. The original branch, HEAD and index are retained.
- Candidate branch: `codex/ch5-v0.0.1-synthetic-household-bridge`; no merge of main or the document branch.
- Exactly three new public files: this execution report, `src/ch5_two_asset_hank/multi_province/synthetic_household_bridge.py`, and `tests/test_v001_synthetic_household_bridge.py`.
- Source Git blob: `41c0283bacef8a658be64f1cb69467f6d4a07197`; source SHA-256: `4EFBA3D1AB71EE456836A2A8662078968A7A7F692397683C6C1136FCBDD5C656`.
- Test Git blob: `e7aeba558463567971fbbc9451b724a32157915b`; test SHA-256: `3D81665EFE5EF71954AA2C36F67A52DF9C3ABB1499AD22A430F2A32FE658FAE8`.
- The final containing candidate commit/tree and its post-seal test receipt are supplied in the centralized delivery. They are not embedded as a self-referential SHA in this report.

## Implementation and factual source-to-consumer matrix

The opt-in module is not added to the package's production exports. It accepts only explicitly fictional `SYNTH_` province labels, `SYNTHETIC/NOT_REAL_SOURCE` provenance, two or three complete provinces, one declared phase and the frozen 20x20x2 F-order `(b,a,z)` fixture grid. Policy/mass inputs are independently copied. Unit-mass/nonnegative checks describe this synthetic input schema, not a replacement scientific convergence or KFE law; no renormalization is performed.

`make_synthetic_household_callback` validates the entering province/source/phase identities and allows one successful use. `run_synthetic_bridge_once` explicitly invokes it once, then calls the unchanged `OneTurnInputs` and `run_source_faithful_one_turn`. No stationary controller, K1B runner or live solver is invoked.

| Boundary | Baseline source/call evidence | This version's evidence | Remaining limitation |
|---|---|---|---|
| Solver output | `exports/matlab_faithful_two_asset_ha.py:681–705` declares result fields and real HJB/KFE calls | Simulated policy/mass output only | Real solver/source binding NOT_RUN/UNKNOWN |
| Corrected policy/mass -> aggregate | `corrected_diagnostic/optionb_turn2_household_integration.py:799–807` explicitly calls the aggregate adapter | Actual `evaluate_corrected_household_aggregates`, compared with independent scalar loops | No real checkpoint read or scientific validation |
| Aggregate -> frozen | `multi_province/corrected_household_adapter.py:114–127`; `scripts/ch5_mp4c_2018_corrected_household_aggregate_binding.py:251–254` has a local call | Actual `frozen_output()` called for each fictional province | Old binding task remains NOT_ACCEPTED/CLOSED |
| Frozen -> batch | Not located as a general factory in the bounded baseline inspection | New `build_synthetic_household_batch:110` maps five actual frozen fields into the existing constructor | No claim of global factory absence or production activation |
| Existing K1B aggregate -> batch | `validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py:215–224,479` directly constructs/consumes a batch | SOURCE_ONLY; not used by this harness | This route bypasses frozen/callback; not verified by the synthetic run |
| Callback -> one-turn | `multi_province/stationary_runtime.py:19,52–55` defines/calls the supplied batch callback | New one-use callback and explicit single-turn consumer; actual callback invocation observed | Existing stationary controller is NOT_RUN, not newly bound |
| Household Lt -> reference labor | `multi_province/one_turn.py:223`; K1B runner `:293` assigns `Lt_prev` | Original firm wrapper captures matching `Lt_prev` | Economic time/unit interpretation remains UNKNOWN |
| Ct -> migration -> current labor | `multi_province/one_turn.py:201–210,227`; `migration_labor.py:98–131` | Actual migration and original firm, independent destination/origin oracle | Not normalized labor, not verified real 31-province economics |
| Original firm | `multi_province/firm.py:44–143`, including its `Lt_prev` arithmetic | Wrapper records the inputs and delegates the original function, never fabricates a FirmResult | Pure synthetic arithmetic; no SCIENCE or production acceptance |

Historical acceptance and the source call-site evidence above remain separate from this invocation's `SYNTHETIC_ENGINEERING`. RUNTIME_REAL, SCIENCE, RESULTS and production eligibility are not promoted.

## Test coverage and observable results

The complete two- and three-province paths each run in one integration test. Independent scalar loops verify Ct/Lt/At/Bt/AtTax; an independent migration formula verifies destination-row/origin-column values. Arrays and immutable scalar outputs are compared at each boundary. The observation wrapper invokes the original firm function.

Two-province observation:

- Household Lt and captured Lt_prev: `[1.0252500000000002, 1.084]`.
- Migration lt_supply and actual current firm Lt: `[7.20976890327738, 7.046523460292032]`.
- One callback, two actual aggregate calls and two delegated original firm calls.

Three-province observation:

- Household Lt/Lt_prev: `[1.0252500000000002, 1.084, 1.1427500000000002]`.
- Current firm labor: `[11.574390451955678, 11.353673471988284, 11.174162999700059]`.
- One callback, three aggregate calls and three delegated original firm calls.

Changing only synthetic household labor doubles Lt_prev without changing migration supply. Changing only Ct by a factor of two leaves household Lt unchanged and reduces migration supply by the unchanged fixture formula's factor of two. These tests preserve the distinct inputs rather than force them to agree.

Rejection tests cover real/missing source labels, province duplicates/missing/order, duplicate source IDs, entering phase/source mismatch, wrong shapes and F-order mappings, nonfinite mass/density and p-g disagreement, invalid synthetic mass/grid, invalid flags/vector lengths/levels, negative migration power bases, and invalid firm alpha. A same-shaped finite transpose is checked by a non-symmetric oracle; it is not falsely described as automatically rejected by the production guard.

Mutation tests verify that changing original source arrays cannot change the record/batch snapshot, batch vectors reject normal assignment, and diagnostics are read-only. Entry sentinels and a profile guard prohibit the scientific/controller/normalized entries during a guarded synthetic call. These tests are bounded engineering checks, not a general filesystem sandbox or source-authentication guarantee.

## Candidate isolation and reproduction

Each test process uses a fresh restricted view exported from its exact Git tree. The exporter follows the static package import closure, writes original Git blob bytes, and includes only the selected test and baseline `pyproject.toml`. It does not copy reports, protected data, old EVIDENCE, or the dirty workspace modules. The unchanged package initializers import some scientific module definitions; no solver function is executed. The government_assets dependency in the view comes from the baseline blob, not the existing dirty file.

Every loaded `ch5_two_asset_hank` module and the test file are checked to be below the corresponding candidate_view. Absolute module readbacks, exact argv/environment, PID, UTC/monotonic timing, stdout/stderr, exit codes, JUnit, view hashes and sampled kernel peak working set are retained LOCAL_ONLY. Original private path inventories are not published.

Interpreter/dependency metadata at intake: Python 3.11.9, NumPy 2.4.6, SciPy 1.17.1, pytest 8.2.1. The final test also emits runtime metadata. No dependency install or shared configuration change occurred.

The exact command has local absolute paths in the private receipt. Its path-redacted reproducible form, run from the exported candidate view, is:

```powershell
$env:PYTHONPATH = "$view/src"
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = '1'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:CH5_V001_CANDIDATE_VIEW = $view
python -B -m pytest -c "$view/pyproject.toml" "$view/tests/test_v001_synthetic_household_bridge.py" -q -s -p no:cacheprovider --basetemp="$run/tmp" --junitxml="$run/junit.xml"
```

Those overrides apply only to the actual child process. No full-suite, historical artifact, real-data or scientific test is selected. The final exact containing tree is exported/tested after report sealing and before its one authorized non-force push; the centralized delivery supplies that receipt and the final commit/tree identity. This post-seal check also verifies the added runtime-metadata/entry-guard diagnostics.

## Failed attempts, repair and Owner authorization

1. Initial export supervisor failed before any pytest launch: a 14,927,094-byte temporary index placed in EVIDENCE caused 15,908,461 bytes against the 10MiB evidence cap. The preflight-size omission and stop remain recorded; it is not retrospectively classified as compliant or PASS.
2. Owner subsequently wrote: “没问题，我授权并且批准。后续有类似轻度的任务修正问题都视为我授权，你只要在报告中详细保留相关问题、处理方法和我的授权批准记录即可。” The approved remedy relocated the index, with matching before/after SHA-256, to the model worktree's dedicated Git administration path. It is operational Git state, separate from the retained <=10MiB synthetic evidence. The original checkout index was not touched. The full index's bytes/hash/storage are recorded privately; no deletion was used to conceal the failure.
3. The same original 4-hour wall and 8-process counter continue; neither was reset. This approval is applied to mild engineering/storage repairs only, not scientific laws, real data, protected original files or explicit hard stops.
4. run01: expected test-first missing-module collection error, exit 2; 4.437s, peak working set 87,339,008 bytes.
5. run02: 40 passed/1 failed, exit 1; 1.547s, peak 84,815,872 bytes. The assertion incorrectly demanded an mt response while the synthetic fixture's pit=0 cancels the Lt_prev term. No old model/calibration was tuned.
6. Repair: directly observe Lt_prev propagation, assert the zero-pit cancellation, and add a separate explicitly synthetic nonzero-pit probe with an independent oracle for the original formula's response. The assembly source did not need changing for this failure.
7. run03: 42 passed, exit 0; 1.391s, peak 83,644,416 bytes. Tested tree `9802161f3b3c505df78519a14bea0e6c56c06897`. Final runtime/entry-guard diagnostics were then added; the post-seal exact-tree test covers them without broadening test scope.

The final delivery reports the actual aggregate process count, final test timing and current evidence size, including any failed attempts. No fabricated final duration or self-referential candidate identity is stored here.

## Protection and frozen-standard completion

- Original checkout index SHA-256 at intake: `28058A7E2D9AB773C5813205C75999E6C221533AEAE0B9BB094B9A83451BF7CC`.
- Original eight tracked dirty files are never edited or included in the candidate. Their terminal hashes, original HEAD/branch/index and staged status are checked before/after publication.
- Original 5,234 untracked and 4,553 ignored paths are preserved. Their contents were neither inspected nor rehashed, so this is path-preservation and no-overwrite evidence, not independent content validation.
- Temporary index only adds the three approved public paths from the exact baseline. Final diff/whitespace/blob checks and remote commit/tree readback are prerequisites to centralized delivery. EVIDENCE and local operational helpers are not pushed.
- Scientific/model/real-data/controller/C8/C9/C10/GE/Results/deployment calls remain zero. No production defaults or original scientific source/guards are modified. C9 PAUSED, CALL_LEDGER_UNRESOLVED, Objective A16 FAIL_CLOSED, model_activation=False and Results FALSE remain.
- Population/per-capita retained, household-average sealed, no N=P/3. Labor persons/hours/efficiency, real provenance, full population denominator/scaling, price and calendar meaning remain UNKNOWN. This synthetic MP2 composition is not K1B S/raw-ra0/C1/network/feedback/GE verification.

| Frozen section | Candidate evidence and limit |
|---|---|
| A/G1 | Exact identity and bounded fact matrix; source sites/historical evidence/synthetic execution separated |
| A/G2 and B | Only the approved new opt-in module/test/report; original APIs, science and defaults preserved |
| A/G3 and C1–C4 | Same-test real component chain, independent oracles, distinct labor paths and key refusal cases |
| C5 | Exact-tree restricted export and loaded-module origin assertions; final receipt delivered separately |
| C6/G4 | Private original streams/receipts plus public redacted results/failure matrix |
| D | Original index-size violation preserved; Owner-approved operational-storage remedy; original time/process caps retained |
| E | Engineering candidate only; one allowed non-force publication after validation, then WAIT_ASTRA_FINAL_ACCEPTANCE |

Acceptance and retrospective documents are left to Astra. No V0.0.2, Work, automation, background monitoring or deployment is started.

---

## Preserved historical initial stop record

The following original report describes the stop before Owner's explicit correction/resumption approval. Its NOT_IMPLEMENTED/NOT_RUN status is historical, not the current candidate outcome. It remains intact to preserve the actual failure.

# V0.0.1 execution: BLOCKED before candidate validation

Date: 2026-10-13. Status: `BLOCKED__EVIDENCE_RESOURCE_CAP_EXCEEDED`.
This is an execution failure/stop record, not Astra final acceptance.

## Authority and source identity

- Frozen plan: `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`, `versions/0.0.1/plan.md`; full document read, sections A–E authoritative.
- Independent authorization: `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`, `versions/0.0.1/authorization.md`; full document read.
- Document branch readback: `131b74e262dde1d77f199c75dff9a4caea5b740a`.
- Code baseline and unchanged original HEAD: `a1db8c114dec0ab69d69a5576e153a7f868cba0e`.
- Original branch: `codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922`.
- Unique repository: `zcx369658780/dissertation-ch5-two-asset-hank`; origin identity confirmed.

## Work performed and exact stop

Only the authorized new test file was written; the assembly module has not been implemented.
The test specifications cover the complete synthetic call chain, independent arithmetic oracles, separate household Lt/Lt_prev and migration/current Lt, input rejection, snapshot protection and candidate module origins.
These are unexecuted specifications, not passing evidence.

A separate temporary index was initialized from the approved baseline and populated only with the new test file. Its size was **14,927,094 bytes**. The implementation placed this operational file inside the new evidence root. Together with local intake and supervisor files, the evidence root reached **15,908,461 bytes** before candidate export, above the frozen **10,485,760-byte** ceiling.

The supervisor rejected the candidate export with `RuntimeError: candidate export would exceed evidence cap`, exit code 1. No candidate_view was created and no pytest subprocess was launched. The omission was failure to preflight the full temporary index size before constructing it. It was not a model failure or a test failure.

The test-only intermediate tree `73b0dc96f6ac4118ef8fd95ca36d6ee01ff26411` is a local Git object, not an implementation candidate commit and not a published branch. No candidate commit, branch or push was produced. It must not be accepted as delivery of the version.

## Preservation and budget

- Original index SHA-256: `28058A7E2D9AB773C5813205C75999E6C221533AEAE0B9BB094B9A83451BF7CC`; terminal check unchanged.
- Staged paths remain empty; the original eight tracked dirty files retain their byte hashes.
- Original untracked 5,234 and ignored 4,553 paths remain present. Their contents were not read or independently rehashed; there was no overwrite or cleanup operation.
- Focused pytest processes: **0/8**. Candidate-export supervisor attempts: **1**, failed before launch. No test output/JUnit exists.
- Scientific solver, HJB/KFE, C8/C9/C10, real-data consumer, GE, Results, deployment and push calls: **0**.
- Start clock sample: `2026-10-13T00:39:38.6344826Z`; exact terminal clock and resource accounting are retained in the local stop receipt.
- No repair by deletion, relocation, accounting exclusion, budget increase or source modification was attempted after the cap failure.

## Source-to-consumer matrix and frozen standards

The read-only proposal established explicit source call sites for corrected aggregate/frozen and K1B aggregate/batch/firm, and an existing stationary callback consumer. Those remain `SOURCE_ONLY` in this invocation; old acceptance is historical evidence only. None was executed here.

| Frozen requirement | Current outcome |
|---|---|
| A/G1 identity, exact scope and preservation | Identity/preservation checked; no implemented candidate |
| B/G2 opt-in assembly module | NOT_IMPLEMENTED |
| C/G3 same-test synthetic chain and rejection/oracles | Tests written, NOT_RUN; no SYNTHETIC_ENGINEERING PASS |
| C5 exact candidate_view validation | BLOCKED before export |
| G4 execution evidence | Resource failure and preservation recorded; successful-test evidence unavailable |
| D resource ceiling | NOT_MET: temporary index in evidence exceeded 10 MiB |
| E centralized candidate delivery | INCOMPLETE; no GitHub candidate publication |

RUNTIME_REAL, SCIENCE, RESULTS and production acceptance remain unavailable. C9 PAUSED, CALL_LEDGER_UNRESOLVED, Objective A16 FAIL_CLOSED, model_activation=False and Results FALSE remain unchanged. Population/per-capita is retained, household-average remains sealed, no N=P/3; labor units, real sources, population denominator, prices and calendar semantics remain UNKNOWN.

## Owner/Astra resource decision required

Preserve the failure and existing files. A fresh explicit revision is needed to define a safe storage/accounting rule for the full temporary Git index, whose single file already exceeds the evidence ceiling. A possible bounded revision is an explicitly authorized operational-index location plus a clearly defined evidence quota, or a reviewed quota increase covering that index and the limited candidate view. This record authorizes neither option, removal of the existing index, nor resumption of the closed attempt.

Local receipts and inventories remain LOCAL_ONLY under the authorized evidence root. This report is a redacted local stop record; it was not pushed. Waiting for Owner/Astra resource decision, with implementation stopped.
