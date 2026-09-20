# Chapter 5 turn-2 F0579 forensic serialization exception acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__F0579_FORENSIC_SERIALIZATION_EXCEPTION_AFTER_ONE_BACKWARD_ROOT_PROCEDURE__NO_SELECTOR_DECISION__FINITE_SCREEN_PERSISTENCE_REPAIR_AND_FRESH_RUN002_AUTHORIZED`

## Accepted candidate

- live-main baseline: `5bc00486955100884005530bc6d7f05fd6acd5b0`
- Builder candidate: `d104f7da14039eac36d76f81188c717df010848d`
- candidate tree reported/read back by Builder:
  `7626b64c8530f9fc7699157e7b1b106759d10d1d`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly baseline
- independently verified changed paths: 16
- no governance CURRENT files changed
- ordinary non-force push and remote SHA/tree readback passed
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main`.

## Accepted failed forensic result

Terminal:

`FAIL__TURN2_F0579_FORENSIC_ROOT_SCREEN_SERIALIZATION__NO_SCIENTIFIC_RETRY`

Classification:

`TURN2_F0579_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION`.

This classification is accepted because the requested branch-specific post-root evidence was not durably persisted.

No selector conclusion A/B/C is inferred.

## Exact exception

The forensic validator called the frozen backward active-upper-b negative branch root procedure once.

The root helper itself evaluates root-screen residuals through the accepted finite-saturation helper before sign/bracket logic.

The task-local forensic capture, however, separately appended the raw pre-saturation residual returned by `_liquid_drift_for_root`.

At least one raw forensic-capture value was `-Infinity`.

Strict JSON serialization with `allow_nan=False` therefore failed at:

`BACKWARD_BRANCH_ROOT_SCREEN_RECEIPT_SERIALIZATION`.

This is a task-local evidence-persistence defect. It does not establish a selector, root, KKT, HJB, or economic failure.

## Accepted consumption

Before the serialization exception:

- failure-cell loads: 1
- scalar branch-root procedures consumed: 1
- backward branch procedures: 1
- screen points: 513
- forward branch procedures: 0
- switching roots: 0
- full selector calls: 0
- policy maps: 0
- D2/Q: 0
- HJB reruns/direct solves: 0
- KFE/SVD: 0
- aggregate/integration: 0
- turn 3: 0
- scientific retries: 0.

Whether the consumed backward procedure executed Brent is not durably established and remains classified:

`UNRESOLVED_0_OR_1__NO_DURABLE_RETURN_RECEIPT`.

Do not reconstruct or infer that missing subcount from process memory after the failure.

## Engineering diagnosis

The forensic validator currently records:

`calls.append((q_b, raw_value))`

before the frozen root helper applies its internal finite-saturation rule.

For evidence parity, the task-local screen receipt should instead record the same finite residual representation consumed by the frozen root screen.

The repair must be evidence-only:

- do not modify `selector.py`;
- do not modify `cost.py`;
- do not change the 513-point log grid;
- do not change the root domain;
- do not change Brent tolerances;
- do not change any candidate/KKT/direction law.

## Route consequence

A fresh forensic run002 is authorized with a separately published two-branch root budget.

Historical forensic run001 consumption remains immutable and separately recorded.

The run002 repair may change only the forensic validator and its focused tests so that root-screen persistence is finite and JSON-safe while remaining exactly representative of the frozen root helper's finite-screen semantics.

After the zero-science engineering gate passes, run002 may evaluate backward and forward branches exactly once each and complete the originally requested A/B/C/D classification.

No turn-2 HJB rerun is authorized.

Results eligibility remains `FALSE`.
