# Reviewer route decision — J160 bounded cross-state post-science finalization blocker

Date: 2026-09-15

Reviewer verdict:

`J160_CROSS_STATE_RAW_SCIENCE_PROVISIONALLY_ACCEPTED__POST_SCIENCE_FINALIZATION_BLOCKER__ZERO_SCIENCE_REPAIR_REQUIRED`

Results eligibility=`FALSE`.

## Repository state

The active exact task remains the J160 bounded cross-state confirmation. The Builder did not create a candidate commit because the first offline finalizer failed after all four authorized science points had completed.

The reported execution used baseline `78deaeac5e2c8eaa9d0c10dbfd322cd0240e5b86`, branch `codex/ch5-mp4c-k1-j160-bounded-cross-state-confirmation-20260915`, worktree `D:\ProjectTemp\ch5-mp4c-k1-j160-bounded-cross-state-confirmation-20260915-001`, and raw evidence root `D:\ProjectTemp\ch5-mp4c-k1-j160-cross-state-evidence-20260915-001`.

Because no Builder candidate exists, this document does **not** accept any uncommitted code or report. It accepts only the route decision that the completed raw science should be preserved and finalized without rerunning HJB/KFE, subject to fresh integrity checks in the successor exact task.

## Reported completed science

Four fresh J160 corner states were reported as HJB legal/converged and KFE completed exactly once each, with scientific retries=0:

- `ra=.06,w=13`: HJB 14 iterations, final stat `4.4464e-9`, `At=85.6697`, `Bt=4.82888`, modal `a=90.5660`, modal `b=2.63158`, amax mass=0, bmax mass about `1.6225e-5`.
- `ra=.06,w=18`: HJB 68 iterations, final stat `8.0469e-8`, `At=81.1883`, `Bt=5.97040`, modal `a=75.4717`, modal `b=1.47368`, amax mass=0, bmax mass about `0.0162997`.
- `ra=.07,w=13`: HJB 11 iterations, final stat `2.1906e-10`, `At=90.7323`, `Bt=5.78054`, modal `a=94.3396`, modal `b=2.63158`, amax mass=0, bmax mass about `0.00015548`.
- `ra=.07,w=18`: HJB 17 iterations, final stat `3.1747e-8`, `At=89.6487`, `Bt=6.15232`, modal `a=95.5975`, modal `b=2.63158`, amax mass=0, bmax mass about `0.00282348`.

The reported KFE total mass is 1 at all four points, residuals are approximately `1.77e-17` to `1.38e-13`, density minima are numerical-scale negatives near `-1.51e-18` to `-2.83e-18`, and no J640-style HJB nonconvergence occurred.

These values are not yet promoted to accepted compact evidence because the Builder did not create a candidate. The successor task must verify the raw sealed evidence before using them.

## Finalization blocker

The first offline finalizer failed with:

`ValueError: CDF comparison requires a common support`

The failure occurred because accepted J20 comparison references use `a=[0,10], b=[-2,5]`, while J160 uses `a=[0,100], b=[-2,20]`.

This is a post-science comparison/finalization defect. It is not HJB failure, KFE failure, or evidence against the J160 practical grid.

The old exact task allowed an engineering retry only before the first HJB, so the Builder correctly did not repair or rerun the finalizer after science.

## Reviewer route

Publish a fresh exact task with **zero scientific runtime**. It must:

1. verify the existing raw evidence integrity, frozen inputs, call ledger, and four completed HJB/KFE calls;
2. repair only the task-owned offline CDF comparison/finalizer so different supports can be compared deterministically;
3. preserve the already accepted same-support CDF-distance semantics exactly;
4. define different-support comparison on the union support with deterministic exterior CDF extension and no clipping/renormalization;
5. label J20→J160 marginal distances as **domain-plus-grid response distances**, not pure precision distances;
6. generate the missing report, compact evidence, sealed manifest, and candidate commit without rerunning any science.

No HJB, KFE, J320/J640/J1280, global, firm, MATLAB, GE, downstream, shock, IRF, or Results call is authorized.

Exactly one next gate after the repair candidate:

`REVIEWER_J160_CROSS_STATE_ROUTE_DECISION`
