# Actual bounded KFE-only replays

| Point | raw/density max difference | normalization difference | original residual | non-pin residual | raw pinned-system residual | strict certified |
|---|---:|---:|---:|---:|---:|---|
| P0 | 0 | 0 | 4.686593832556138 | 1.6518372191536135e-15 | 2.8456122435781354e-17 | FALSE |
| P2 | 0 | 0 | 0.32557163336740258 | 1.0148132334464322e-16 | 1.3064636178450328e-17 | FALSE |
| P4 | 0 | 0 | 3.7634433046985296 | 9.4368957093138306e-16 | 1.4619788669609224e-17 | FALSE |
| P5 | 0 | 0 | 3.4077708099368875 | 1.5569143196891844e-15 | 1.9827347229328662e-17 | FALSE |

- P0: exit0, 2.296000s, peak process committed bytes 90718208; raw/density exact, normalization factor 0.017226953180266767; At 7.2740978684863942, Bt 4.6982774669466716; negative mass 7.2768608767739868e-17; total 0.99999999999999978.
- P2: exit0, 0.625000s, peak process committed bytes 90873856; raw/density exact, normalization factor 0.11570771109142623; At 5.0722995536457365, Bt 1.8147088284647883; negative mass 0; total 1.0000000000000002.
- P4: exit0, 0.641000s, peak process committed bytes 90767360; raw/density exact, normalization factor 0.018255522382932515; At 7.2688448772635486, Bt 4.7097431300129102; negative mass 1.6893356816383517e-16; total 1.
- P5: exit0, 0.656000s, peak process committed bytes 90910720; raw/density exact, normalization factor 0.016963996265069475; At 7.3037783353426775, Bt 4.6887577964605072; negative mass 9.6177918267864433e-17; total 1.

Each replay reconstructs only the authenticated archived CSR, calls real frozen core once, and checks it against an independent dense transposed/unit-row construction without a second solve. All original800-vector raw entries, density entries, factors, F reshapes, 20 a/b marginal bins and At/Bt were compared. Source and matrix hashes are checked before and after. Runtime counts: KFE4, spsolve4, row-index helper4; forbidden calls0. No export execution, MATLAB runtime, HJB, policy, initializer, root or price search.

Each point has claim, receipt, result, public stdout/stderr and redaction record. Raw logs and binary snapshots stay LOCAL_ONLY. Timeout30s and Windows Job process committed memory1GiB, active child limit1 and six BLAS environment keys1 were applied before GO/import. Peak committed memory is measured; native library thread counts were not independently measured. There were no timeout or retry events. Exact point order P0→P2→P4→P5 consumed4/4 and budget is closed.
