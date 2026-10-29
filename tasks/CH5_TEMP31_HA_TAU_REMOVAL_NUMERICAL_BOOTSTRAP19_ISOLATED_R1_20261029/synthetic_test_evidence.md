# Two bounded no-HA commands

| Invocation | Command | Result |
|---|---|---|
| 1 | python -B validators/multi_province/temp31_ha_taxfree_bootstrap_isolated.py --group contract | exit0; 8/8 cases; 0 failures/errors |
| 2 | python -B validators/multi_province/temp31_ha_taxfree_bootstrap_isolated.py --group source-algebra | exit0; 8/8 cases; 0 failures/errors |

Claims precede execution; original stdout/stderr and exit/hash receipts are in evidence/test_1_* and test_2_*. Total2/2, no retry, no extra test command. Negative cases are observed expected exceptions/assertions, not unreported process failures.

Contract group: exact19 and original state preservation; real taxes/wedges retained; changed initial numbers rejected; numerical first/later calculated labels distinguished; context/order/origin bounds enforced; stale or inconsistent R5 producers and wrong source rejected; new input signature has no tax/migration parameter; legacy type and second wage wedges/global tax zeroing rejected; original12 source objects and prior R4/R5 payload bytes unchanged.

Source/algebra group: all six source sites lack tau/migration fields; mutation injection is detected; full non-tax AST equivalence passes in all three copies; initialization/root body invariance passes; old20/.05 and new19 produce28.5 at z1.5 at all six extracted expressions; later destination net5/4 produces7.5/6; pure FOC expression gives sqrt(38) for V_b4, wage marginal9.5, weight1, phi2; both mu_b expressions give9.2 for rb.02,b10,labor income19,transfer3,cost2,consumption5. Corrected import bindings and untouched operator import are checked statically.

Only actual allowed source contracts/R4/R5/bootstrap modules are definition-loaded. Historical contracts is compiled directly from authenticated Git bytes, not a substitute implementation. Anchor, HJB and policy modules are not executed. Corrected HJB/policy modules are AST-read only. NumPy/SciPy imports are libraries; no brentq, initialization, local-policy, HJB, KFE, GE, IRF, real31-province or production calls occur. No full suite or closed prior-task tests were rerun.
