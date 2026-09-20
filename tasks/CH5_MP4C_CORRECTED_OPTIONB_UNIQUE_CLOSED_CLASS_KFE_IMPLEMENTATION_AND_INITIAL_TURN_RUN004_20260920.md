# Task — unique-closed-class KFE implementation and corrected initial-turn run004

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_UNIQUE_CLOSED_CLASS_KFE_IMPLEMENTATION_AND_INITIAL_TURN_RUN004_20260920`

Status: `COMPLETED_FAIL_ACCEPTED`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACCEPTANCE_20260920.md`
7. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`
8. predecessor corrected initial-turn tasks/reports and all direct scientific authorities.

No additional scientific choice is authorized beyond the Owner adoption document.

## Objective

1. implement the Owner-adopted unique-closed-class support KFE as the corrected terminal KFE authority;
2. prove implementation parity against the accepted Beijing method-candidate evidence before running new model science;
3. execute exactly one fresh corrected initial-turn run004 from the same accepted 31-province outer-turn-1 initialization states;
4. if all 31 household blocks pass, execute exactly one K1A/C1/source-faithful-labor/firm integration turn and construct the raw next-payoff vector;
5. do not run turn 2.

## Allowed scientific-code change

Primary implementation path:

`src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`

The initial-turn integration driver may be changed only as required to consume the new terminal-KFE receipt/ledger schema:

`src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py`

Focused tests may be added/updated.

Do not alter HJB/selector/D1/D2/D3/KKT/boundary/upwind/switching science, aggregate semantics, K1A, C1, firm equations, payoff law, Delta, HJB thresholds or direct solver.

## Exact terminal KFE implementation

Implement exactly the Owner-adopted authority.

For each converged province:

1. run the accepted exact-positive topology once;
2. require exactly one closed communicating class C;
3. construct `Q_CC=Q[C,C]`;
4. require finite Q_CC, nonnegative offdiagonals, zero positive closed-to-transient outflow, and row conservation within the accepted D2 arithmetic bound;
5. run exactly one dense restricted GESVD on `Q_CC.T`;
6. persist all restricted singular values;
7. compute both rank-threshold views:
   - `gamma(m+64)*max(1,sigma_max)`
   - `gamma(864)*max(1,sigma_max)`
8. require both to produce rank/nullity `m-1 / 1`;
9. use only the smallest right-singular vector;
10. require signed-sum separation using `gamma(m)*max(1,sum(abs(v_C)))`;
11. one global sign orientation;
12. one normalization on C;
13. require every p_C entry strictly greater than zero;
14. embed exact positive zero on all transient states;
15. require full p finite, nonnegative and normalized;
16. set `g=p/OMEGA` and retain density normalization;
17. execute exactly one original full-Q `Q.T@p`;
18. apply the existing full-state stationarity/source-free arithmetic gates;
19. only then classify terminal KFE PASS and permit household aggregates.

Do not execute an 800x800 full-space GESVD.

Do not use the run003 p as an input to the new KFE construction.

## Zero-science implementation gate

Before fresh run004 model science:

- focused unit tests on synthetic Markov generators must verify:
  - unique closed class extraction uses persisted topology result without second SCC;
  - multiple closed classes fail closed;
  - restricted rank/nullity gate uses both threshold views;
  - strict-positive closed-support gate;
  - exact-zero transient embedding;
  - no full-space SVD fallback;
  - exactly one full-Q stationarity validation;
  - exception-path scientific ledger preservation;
- bind the accepted Beijing Q12 artifact and method-candidate evidence;
- execute one **implementation parity replay** using only the already accepted Beijing Q12 object:
  - no HJB/policy/D2 call;
  - one topology call, one restricted GESVD, one normalization candidate, one full-Q `Q.T@p`;
  - require exact or explicitly justified deterministic parity with accepted method-candidate invariants:
    - C membership;
    - Q_CC identity;
    - singular-spectrum identity or bitwise-equivalent values under identical environment;
    - rank/nullity 399/1 under both views;
    - strictly positive p_C;
    - exact-zero transient support;
    - full-Q stationarity PASS;
- parity replay is validation of implementation against accepted evidence, not a new household run;
- scientific retries for parity replay: 0;
- run focused tests, `py_compile`, `git diff --check`;
- verify exact authority blobs, predecessor manifests and code freeze.

If implementation parity fails, STOP before run004.

## Fresh run004 initial-state authority

Use exactly:

`reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv`

with the accepted blob and exact 31 province order.

Parse each row's exact `outer_turn_1_initial_state_json`.

Do not inject historical Path-B completed-turn-1 raw payoff as entering turn-1 rah.

## HJB contract

Unchanged from the accepted corrected initial-turn task:

- grid `20x20x2`, F-order, b fastest;
- source-native initialization exactly once per reached province;
- 800 labor roots per reached province;
- D1/D2/D3/KKT/boundary/upwind/switching unchanged;
- fixed `Delta=1000`;
- convergence iff same checkpoint `B<=1e-8 AND D<=1e-7`;
- only `scipy.sparse.linalg.spsolve`;
- backward error `<=1e-12`;
- exact/approximate cycle law unchanged;
- max 50 direct HJB updates per province;
- province order `0..30`;
- stop entire run on first scientific failure;
- scientific retries 0.

## KFE budget per reached converged province

Exactly:

- topology/SCC: 1
- restricted dense GESVD: 1
- normalized closed-support candidate: 1
- full-space 800-state dense GESVD: 0
- full-Q `Q.T@p`: 1
- KFE retries: 0.

Persist:

- topology receipt;
- closed-class index identity;
- Q_CC identity and structural receipt;
- complete restricted spectrum;
- both rank-threshold receipts;
- orientation/normalization receipt;
- p_C and embedded p/g identities;
- exact-zero transient support check;
- full-Q stationarity/source-free receipt.

## Aggregates and one-turn integration

Only after each province KFE PASS may Ct/Lt/At/Bt/total-assets/AtTax be evaluated.

Only if all 31 provinces pass:

- construct exactly one `PreFrozenHouseholdOutputBatch`;
- source-faithful labor reconstruction: 1;
- K1A allocation: 1 with `beta_distance=2`, `beta_return=0`;
- C1 residual GovInv: 1;
- firm evaluations: 31;
- composite wage batch: 1;
- monetary assignment: 1;
- fiscal diagnostic batch: 1;
- raw next-payoff same-S construction: 1.

Use raw firm `ra0`, same S orientation:

`rah_next_raw_by_origin = ra0_turn1_by_destination @ S_destination_origin`.

No clipping, rescaling, annualization, smoothing, risk adjustment or z-score of the payoff level.

Do not feed this vector into a turn-2 household solve.

## Scientific budgets for fresh run004

Initialization:
- province initializations <=31
- labor roots <=24,800
- retries 0

HJB:
- policy/D2 maps <=1,581
- selector evaluations <=1,264,800
- direct updates <=1,550
- max 50/province
- solver substitutions 0
- retries 0

Terminal KFE:
- SCC <=31
- restricted GESVD <=31
- normalized candidates <=31
- full-Q `Q.T@p` <=31
- full-space 800 GESVD =0
- KFE retries 0

Integration:
- aggregates <=31
- household batch <=1
- labor reconstruction <=1
- K1A <=1
- C1 <=1
- firms <=31
- wage/monetary/fiscal <=1 each
- raw-next-payoff <=1.

Forbidden:
- turn2 household calls 0
- second outer turn 0
- K1B 0
- K2 0
- adaptive controller 0
- MATLAB science 0
- GE/annual/shock/IRF/welfare/Results 0.

Implementation-parity replay calls must be separately ledgered from fresh run004 and must not be counted as run004 household science.

## Evidence

Use fresh run004 root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004/`

Do not overwrite run001/run002/run003 or method-candidate evidence.

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_UNIQUE_CLOSED_CLASS_KFE_IMPLEMENTATION_AND_INITIAL_TURN_RUN004_REPORT.md`

Persist at minimum:

- Owner-adoption binding;
- implementation-diff contract;
- focused tests;
- Beijing implementation-parity replay receipt and separate ledger;
- pre-execution code freeze;
- 31-state initialization receipt;
- per-province initialization/HJB histories;
- per-province unique-closed-class KFE receipts;
- aggregates;
- household batch;
- one-turn integration/accounting;
- raw-next-payoff receipt;
- next-state candidate;
- run004 scientific ledger;
- predecessor historical-consumption lineage;
- terminal receipt;
- sealed manifest and independent readback.

## Terminal markers

If all 31 household blocks and one-turn integration pass:

`PASS__OWNER_ADOPTED_UNIQUE_CLOSED_CLASS_KFE__CORRECTED_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_K1A_C1_INTEGRATION__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

If any scientific gate fails, stop at the exact first failing object and preserve the specific fail-closed terminal.

A run004 PASS establishes one corrected initial multi-province turn under the newly adopted terminal KFE authority only. It does not establish outer convergence, K1B, GE or Results.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.


## Reviewer closure — 2026-09-20

Run004 candidate `af770c1fb787098569df2a25471cdc8101eda3a3` is accepted as failed evidence.

Accepted result:
- Owner-adopted unique-closed-class KFE implementation parity PASS;
- 31/31 corrected household HJB PASS;
- 31/31 adopted terminal KFE PASS;
- 31/31 stationary aggregates PASS;
- accepted household batch identity `8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`.

The one integration turn stopped at a bitwise comparison between two mathematically identical same-S floating-point reduction orders. This is accepted as an engineering/numerical identity-guard defect, not a payoff-law failure.

Acceptance:
`docs/CH5_MP4C_RUN004_31PROVINCE_HOUSEHOLD_KFE_PASS_RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_ACCEPTANCE_20260920.md`

Next active task:
`tasks/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_20260920.md`
