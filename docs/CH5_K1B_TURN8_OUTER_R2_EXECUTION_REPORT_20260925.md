# K1B turn8 R2 one-shot execution report

Task: `CH5_K1B_TURN8_OUTER_R2_EXECUTION_20260925`.

First and only invocation: `python -B validators/multi_province/k1b_turn8_outer_r2/run.py --execute --execution-id turn8-r2-run001` from `D:\ProjectTemp\c5k1bturn56`. Invocation count `1`, process exit code `0`, first terminal `VALID__LEVEL_NOT_MET_AT_BUDGET`. The separate one-shot turn8 budget and the adopted two-turn maximum are consumed. Scientific retries `0`; turn9 household calls `0`.

## Authority and readback

Dispatch HEAD `7c88960f16ce0b7dd42bbb99b882334731895749` descends from accepted runner `7b81628a8c54088117878c666995c665935a9617`, accepted turn7 evidence `586b066e9add81fba6f2c86ed3fdd0092a3dbeea`, and Owner adoption `2d43179bc9e9348efe8f61c19217ee10be6bd5d3`. `TASK_CURRENT.md` and its archived task were byte identical, source/task/runner paths clean, and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. The default static preflight passed before the sole invocation. Its exact 39-category turn8 and cumulative budget table matched the committed runner and accepted turn7 attempted ledger.

The entering C7 JSON, NPZ, seal manifest, full output manifest, prior comparison and prior terminal matched task-bound SHA-256 values `30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A`, `E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB`, `20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `6DE97F35A8D599183F19F920A95B61CC01CE21B3E6E1AFAB19935FC44623835E` and `E4753713354D54B49716574A29424D4F709A427851DE7F1CC9B7CDAA8D31D3FB`. The protected C6-prime repeat output manifest remained `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`; it was not an input.

The new output contains 31 distinct province terminal receipts and 31 terminal KFE mass arrays. Every province's reported HJB B/D met the accepted gates; all reported KFE results are present. Exactly one full integration completed. Entering-turn9 JSON/NPZ and its seal passed readback (`bad_paths=[]`); seal manifest SHA-256 is `40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`. This is preparation of an input bundle only; turn9 household did not run. The full output manifest lists 5,141 prior artifacts and 63,801,638 bytes, passed hash readback, and has SHA-256 `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`. The manifest itself is the 5,142nd output file.

## Attempted calls and two comparisons

The turn8 source and guard ledgers agree on every adopted category, `guard_denied=[]`, and `call_ledger_resolved=true`. Actual turn8 attempted counts: 31 source-native initializations; 24,800 labor roots attempted and returned; 409 policy maps and D2 assemblies; 327,200 selector evaluations; 141,125 selector-root invocations; 378 direct HJB updates, checkpoint evaluations and relaxation helpers; 382 alpha candidates; 31 terminal KFE attempts, SCC decompositions, restricted GESVDs, normalized candidates, `Q.T@p` checks and aggregate evaluations; one household batch; one integration; 31 firm evaluations; one each of frozen K1B allocation/feedback alias, C1 residual, labor reconstruction, wage batch, monetary assignment, fiscal batch, completed raw-return vector, next K1B preparation and same-S payoff. Full-space GESVD, substitutions, K2, GE/annual/shock/IRF/welfare/Results, MATLAB scientific calls and retries were `0`.

Adding the accepted turn7 attempted ledger gives combined counts of 62 source-native initializations, 49,600 labor roots attempted and returned, 818 policy maps and D2 assemblies, 654,400 selector evaluations, 282,254 selector roots, 756 direct updates/checkpoints/relaxation helpers, 764 alpha candidates, 62 terminal KFE attempts and associated terminal operations, two household batches and integrations, 62 firm evaluations, one turn7 household batch, one turn8 household batch, zero turn9 household calls and zero retries. Every turn8 and combined count is within its exact ceiling. The machine receipt contains both complete ledgers and the combined ledger.

The legal C7→C8 differences are:

| Component | Difference | Strictly below `1e-6` |
|---|---:|---|
| `Yt` | `3.828161716512568e-7` | Yes |
| `Lt` | `1.4616551486934526e-6` | No |
| `wjt` | `8.585054638299283e-7` | Yes |
| `rk` | `5.358519392650862e-6` | No |
| `Kt_prev` | `1.4594659357174185e-16` | Yes |
| `w` | `7.039445992784721e-8` | Yes |
| `raw_ra0` | `5.358519392650862e-6` | No |
| `rah` | `4.685714629193427e-6` | No |
| `S` | `3.390217531776263e-7` | Yes |

C6→C7 had 2/9 components below the strict level; C7→C8 had 5/9. Both legal comparisons missed, so R2 is not met. C7 and C8 each had 31 clipped `ra` upper hits, report-only for the new criterion; the distinct original MATLAB zero-hit predicate is false at both checkpoints. This is a valid bounded numerical terminal, not a fixed point, GE or Results claim.

All three scientific output roots remain untracked and preserved. The only intended staged paths are this report and its machine receipt; staged `git diff --check` passed. Independent GPT Work ACCEPT/REJECT of the bounded evidence is the next gate. No scientific successor is authorized. Results eligibility remains `FALSE`.
