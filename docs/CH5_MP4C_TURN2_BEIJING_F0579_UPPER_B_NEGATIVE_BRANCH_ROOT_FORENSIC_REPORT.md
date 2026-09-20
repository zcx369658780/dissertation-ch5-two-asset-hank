# Chapter 5 turn-2 Beijing F0579 upper-b negative-branch root forensic report

Date: 2026-09-20

## Terminal verdict

`FAIL__TURN2_F0579_FORENSIC_ROOT_SCREEN_SERIALIZATION__NO_SCIENTIFIC_RETRY`

Classification:

`TURN2_F0579_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION` (D)

The requested successful forensic terminal marker was not earned. The single
authorized scientific execution reproduced the persisted seven-candidate state
and consumed the backward branch root procedure once, but failed while
serializing its root-screen receipt. The raw forensic capture contained
`minimum_residual=-Infinity`; strict JSON serialization rejected that value.
The frozen root helper itself applies finite saturation internally, but its
return and any Brent subcount were not durably persisted before the failure.
Scientific retries were fixed at zero, so execution stopped immediately.

## Repository and authority binding

- actual fresh-fetched live-main baseline:
  `5bc00486955100884005530bc6d7f05fd6acd5b0`
- code-freeze commit before science:
  `8d8aa7c8979cedd1feb329f837c79584859d1bf9`
- predecessor run001 sealed manifest:
  `50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`
- exact failure-cell Git blob:
  `799294deb8119e4581486d279bbf5704784588b2`
- exact failure-cell SHA-256:
  `290630D26A63F2BEF3FFF1C9C6EE014E95ED5B3B470A7A5EC0FC8F3129178700`
- selector Git blob:
  `7e13fb53138788ec71541316a9e9815b5eb7c1f4`
- cost Git blob:
  `435705a50238aaeebe918430156bcc14df1ff794`

The predecessor manifest passed its complete 612-entry deterministic readback.
The exact cell identity, scalars, derivatives, selector parameters, selector
source, and cost source matched the task authority before the scientific call.

## Current-candidate reproduction

The persisted F0579 seven-candidate state reproduced successfully without a
full selector call:

- all inactive candidates remained rejected for their recorded reasons;
- active upper-b zero-kink remained `ROOT_FAILURE_NO_UNIQUE_BRACKET`;
- active upper-b positive remained inadmissible for the recorded transfer-sign
  and transfer-KKT reasons;
- active upper-b negative reached
  `DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT`;
- all seven persisted candidates remained inadmissible under the current
  pre-root record.

## Branch forensic status

### Backward illiquid derivative branch

- persisted derivative: `p_a=-0.00014542975673859096`
- root-screen points evaluated: 513
- scalar branch-root invocations consumed: 1
- root result: unavailable because it was not durably persisted
- Brent solve count:
  `UNRESOLVED_0_OR_1__NO_DURABLE_RETURN_RECEIPT`
- failure stage: backward branch root-screen receipt serialization

The procedure was consumed exactly once. Its result cannot be reconstructed or
treated as evidence after the serialization failure.

### Forward illiquid derivative branch

The forward branch was not run. Its root-screen, root status, and downstream
admissibility remain unresolved.

### Post-root and switching checks

No branch-specific post-root admissibility result was completed. The admissible
branch count, policy distinctness, Hamiltonian comparison, and selector decision
remain unresolved. The interior-a switching prerequisite was not evaluated, and
no switching root was called.

These incomplete receipts require classification D. They do not support A, B,
or C and do not change the accepted turn-2 KFE or Results status.

## Exact scientific ledger

- failure-cell JSON loads: 1
- scalar branch-root invocations: 1
- backward branch-root invocations: 1
- forward branch-root invocations: 0
- Brent solves: `UNRESOLVED_0_OR_1__NO_DURABLE_RETURN_RECEIPT`
- interior-a switching roots: 0
- full selector calls: 0
- policy maps: 0
- D2/Q assemblies: 0
- HJB direct solves or reruns: 0
- KFE/SVD calls: 0
- aggregate/integration calls: 0
- turn-3 household calls: 0
- scientific retries: 0

## Evidence and code freeze

Evidence root:

`reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run001/`

- sealed manifest SHA-256:
  `5EB92DEFF02D591A4E72FD2B19E1EF3DF6D4D2D45F13CE7B2A13311C6CD99247`
- entries: 11
- bytes: 8,405
- independent readback: PASS; bad paths 0
- pre/post execution source and validator code freeze: exact match
- selector source modified: false
- cost source modified: false
- pre-science focused tests: PASS
- pre-science selector/switching regressions: 21 passed
- final focused tests: 5 passed
- final related selector/switching regressions: 19 passed
- `py_compile`: PASS
- `git diff --check`: PASS

The evidence closure was deterministic post-processing only and made zero
additional scientific calls.

## Scope closure

The selector and cost source were unchanged. No HJB rerun, D2/Q assembly, KFE,
aggregate, integration, or turn-3 execution occurred. CURRENT files were not
modified, no successor was published, and main was not merged.
