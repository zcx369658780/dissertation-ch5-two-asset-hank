# Two explicit no-HA invocations

| Invocation | Command | Cases | Exit / result |
|---|---|---|---|
| 1 | python -B validators/multi_province/temp31_ha_wage_debug_isolated.py --group provenance | 8 | exit 0, 8/8 PASS, 0 failures/errors |
| 2 | python -B validators/multi_province/temp31_ha_wage_debug_isolated.py --group algebra | 9 | exit 0, 9/9 PASS, 0 failures/errors |

Claims were written before their calls. Exact raw stdout/stderr and byte hashes/exit codes are retained in evidence/test_1_* and test_2_* payloads. No test was skipped, rerun or replaced; budget 2/2, tool retries 0. Negative examples are expected ValueError/blocked assertions within passing tests, not real solver failures or hidden command failures.

Group 1 observes rejection before the R4 adapter (the adapter is patched only to detect accidental entry); original default (20,20) remains in diagnostics. Forged labels, observed-wage mismatch, wrong run context/order, stale/future iterations, cross-round default resets and incorrect fixed IDs are rejected. Even a first-round preparatory calculation is blocked pending Owner policy; valid prior-turn records for entering iterations 2 and 3 are accepted.

The hand fixture uses destination wages (5,10), taxes (0.2,0.6), phi all ones, sigma=((0,0.8),(0.1,0)), phi_l=alphal=1. Destination net terms are (4,3) for origin A and (0,4) for origin B, giving net composites (5,4). The independent pure-Python transcription matches the unchanged pinned wage.py. A separate three-province nonunit-elasticity comparison also matches that real source function; no 31-province model or household consumer is called.

With origin A wage 5, z=0.5, labor=2, the common proposed wage income is 5. Transfer 2, rb=0.1, liquid asset 10 and other assumed resources 3 give total 11; illustrative saving 4 gives consumption 7. z=1.5/labor=2 gives income 15 and consumption 17; origin B with z=2/labor=0.5 gives income 4 and consumption 6; zero labor gives zero wage income. z and labor are multiplied once. These are accounting checks, not actual labor or consumption policy solutions.

Wrong nonzero second tau/sigma are rejected by the real R4 data constructor. Validly constructed but numerically shifted consumer wage views, and globally zeroed original tax data, are rejected by the new proposal guard. Thirteen historical/R4 code paths pass byte-count/SHA-256/Git Blob preservation assertions; the old R4 label-only API is deliberately shown unchanged, with the new provenance guard outside it.

The loader uses a dedicated namespace to load the actual authenticated R4, new debugger and wage.py source files, without executing a production package initializer. It does not provide dummy household modules or solver results. No missing auxiliary object is imported. Actual HA, initialization, HJB boundary, local policy, KFE, GE, IRF and production/full-suite runs remain NOT_EXECUTED.
