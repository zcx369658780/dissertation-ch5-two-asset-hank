# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_SUPPORTED__OWNER_METHOD_ADOPTION_DECISION_REQUIRED`

Results eligibility=`FALSE`。

## Accepted Beijing evidence

Corrected HJB checkpoint 12 PASS.

Exact-positive topology:
- one unique closed communicating class;
- closed states 400;
- transient states 400.

Existing full-space 800-state KFE remains FAIL under its frozen entrywise nonnegativity gate.

The accepted support forensic proves:
- all 14 floor breaches are transient-only;
- closed-class breach count is 0;
- all 400 closed-class entries are strictly positive.

## Accepted method-candidate diagnostic

Candidate:
`bb5f2796b0d1b8a8c56dda40afa898cc7f8da315`.

Acceptance:
`docs/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACCEPTANCE_20260920.md`.

The unique-closed-class support candidate passes:

- Q_CC shape `400x400`, no positive closed-to-transient outflow, row conservation PASS;
- restricted GESVD rank/nullity `399/1` under both preregistered threshold views;
- restricted normalized mass minimum `3.4169927217543985e-07 > 0`;
- 400 transient entries embedded as exact zero;
- embedded full vector finite, normalized, nonnegative;
- exactly one full original-Q `Q.T@p` validation PASS with residual infinity norm `2.325020736918329e-16`.

## Decision state

No KFE method has been adopted.

The project is waiting for explicit Owner decision on whether to replace the current full-state-space stationary-mass method with the unique-closed-class support method defined in the accepted diagnostic.

No Builder task is active until that decision is made.

Turn 2, K1B, K2, GE and Results remain closed.
