# Independent Work review: outer stopping, failure and budget contract proposal

Date: 2026-09-23 (Asia/Shanghai)

Verdict: `ACCEPT__CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_QUALITY__ZERO_SCIENCE__OWNER_ADOPTION_PENDING`

## Candidate and checks

- Work dispatch `276a7e4e3594b0bbd7f6d52e83f589253505b0ad` has parent `71c4479636b729c07c3725c76a14ecd757ce55b6`. Builder candidate `1badca66f6831bddb18d6bf56cb63338206159c6` has the dispatch as parent and changes only `docs/CH5_OUTER_STOP_FAILURE_BUDGET_CONTRACT_PROPOSAL_20260923.md` and `EVIDENCE/ch5_outer_stop_failure_budget_contract_proposal_20260923/proposal_receipt.json`.
- Report SHA-256 `5D3BFE7B914DE3F6BE3B99E75E80680B18A4054FB186EBB715D865F4008DEAC6`; receipt SHA-256 `CF817DDBF9866D746E0B6A2F384314FC723A2045ACB194F09F02BAE94B477E9D`.
- Independently read back all 16 named source paths and SHA-256 values: zero mismatch. All 31 proposed budget rows satisfy per-turn times two equals two-turn ceiling. Every row bound to an existing combined-ledger ceiling matches that ceiling; categories without a comparable old ceiling are explicitly marked unresolved or identified as new proposed boundaries. The prior task's aggregate two-turn ceilings and 50 direct HJB updates per province agree with the proposal.
- Production `src` tree remains `00682b2e1a7ba23665f6e16f6acf48ad35874883`; the candidate worktree was clean and `git show --check` passed. The literal household/HJB/KFE/integration/firm/K1B/GE/turn7/other-science/retry ledger is all zero.

## Scientific scope

The dossier correctly distinguishes the Owner's accepted `1e-6` static **diagnostic** precision from a proposed stopping threshold. It preserves the nine exact formulas, same-stage checkpoint and lagged raw-return timing, and offers three routes with a conditional recommendation. It does not infer outer-map error bounds from inner residuals, float64 representation or adjacent trajectory changes. Same-frozen-state repeatability is still `UNAVAILABLE`; even a finite repeat would not prove a general error bound.

The proposed two-turn ceilings are a reviewable template, not inherited execution authority. Standalone scalar selector root invocations, total KFE calls and K1B feedback operation equivalence remain unresolved as independent budget categories. A future execution task must close or explicitly bound these before calls. C4/C5/C6 clipped-`ra` upper hits are 31/31; the new nine-component criterion cannot be represented as the original MATLAB outer predicate passing.

## Next gate

This ACCEPT covers dossier traceability and proposal quality only. It does **not** adopt the carrier as a stopping law, promote `1e-6` to a stop level, select one or two passes, approve same-state repeat, decide the clipped-`ra` boundary policy, authorize two turns or any scientific call, or confer fixed-point/GE/Results authority. Owner must choose the scientific route and budget policy; Work must then issue a separate bounded task. Turn7 household remains unrun and Results eligibility remains `FALSE`.
