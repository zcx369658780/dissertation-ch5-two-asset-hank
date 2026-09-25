# Independent GPT Work review — C8 timing budget proposal Repair1

Reviewer: GPT Work
Verdict: ACCEPT__C8_SEPARATE_TIMING_BUDGET_PROPOSAL_REPAIR1__DESIGN_ONLY

The Repair1 candidate is `0a669329fe9e91078e14d01bdb28bcee97f351b8`, parent `d1c9e73f9a89d6c521b1dd999a763d3c5537a52f`, tree `e5916a9df89cb882615d35b10e3c418586190745`. It changes exactly the two task-allowlisted proposal and receipt paths. Its sole substantive correction replaces the proposed budget namespace with `SEPARATE_C8_TIMING_ONLY`, matching both the accepted wrapper's `future_gate` contract literal and its attempt-journal literal.

Independent readback matched the receipt's report SHA-256 and every listed source SHA-256. JSON parsed; the new receipt's 39 proposed total ceilings, five explicit per-province guards, 39 historical C8 actuals, source/protected identities and all-zero task call ledger match the rejected predecessor `7b145046aedaad32451b8ce5e336d65118fa6306` exactly. `git diff d1c9e73f..0a669329 --check` passed. At review start, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, no tracked dirt, exactly protected C6-prime/C7/C8 untracked roots, and no measurement output root.

This ACCEPT establishes proposal quality only. The Owner has not adopted the separate budget, selected a finite process wall-clock cap or overrun policy, or authorized a scientific measurement. A resource cap is a risk limit, not a measured duration bound. One C8 observation is not automatically a C9/C10 duration upper bound. C9/C10 prelaunch remains `BLOCKED__DURATION_BOUND_UNAVAILABLE`; Results eligibility remains `FALSE`.
