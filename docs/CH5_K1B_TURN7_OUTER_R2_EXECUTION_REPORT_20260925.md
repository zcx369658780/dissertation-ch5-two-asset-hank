# K1B turn7 R2 one-shot execution report

Task: `CH5_K1B_TURN7_OUTER_R2_EXECUTION_20260925`.

First and only invocation: `python -B validators/multi_province/k1b_turn7_outer_r2/run.py --execute --execution-id turn7-r2-run001` from `D:\ProjectTemp\c5k1bturn56`. Invocation count `1`, process exit code `0`, first terminal `VALID__NINE_COMPONENT_LEVEL_NOT_MET`. The one-shot turn7 budget is consumed. Scientific retries `0`; turn8 household calls `0`.

## Authority and readback

Dispatch HEAD `6172163893afca5edd555fc2f211824cb85f3cdd` descends from accepted runner `740f06648a3be7f3d571d5bb2f8ff6668a193b90` and Owner adoption `2d43179bc9e9348efe8f61c19217ee10be6bd5d3`. `TASK_CURRENT.md` and the archived execution task were byte identical, source/task/runner paths clean, and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. The default static preflight passed before the sole scientific invocation. The entering C6 JSON, NPZ and sealed manifest matched their task-bound SHA-256 values `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`, `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E` and `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127`.

The new output root contains 31 distinct province terminal receipts and 31 terminal KFE mass arrays. The runner recorded one full integration, a complete entering-turn8 JSON/NPZ plan, and a passing sealed-bundle readback (`bad_paths=[]`). The entering-turn8 manifest SHA-256 is `20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E`. The new full output manifest lists 5,141 prior artifacts, 63,794,713 bytes, and passed hash readback; its SHA-256 is `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`. The manifest itself is the 5,142nd file. The protected C6-prime repeat manifest remained `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61` and was not used as input.

## Literal call ledger and comparison

The source and guard ledgers agree for every adopted category, the guard denied no entry, and `call_ledger_resolved=true`. Key actual attempted counts: 31 source-native initializations; 24,800 labor roots attempted and returned; 409 policy maps and D2 assemblies; 327,200 selector evaluations; 141,129 selector-root invocations; 378 direct HJB updates, checkpoint evaluations and relaxation helper invocations; 382 alpha candidates; 31 terminal KFE attempts, SCC decompositions, restricted GESVDs, normalized candidates, `Q.T@p` validations and aggregate evaluations; one household batch; one integration; 31 firm evaluations; one each of frozen K1B allocation, feedback alias, C1 residual, labor reconstruction, composite wage batch, monetary assignment, fiscal batch, completed raw-return vector, next K1B preparation and same-S payoff. Full-space GESVD, substitutions, K2, GE/annual/shock/IRF/welfare/Results, MATLAB scientific calls and retries were all `0`. The maximum province-local observations were 14 policy maps, 11,200 selector evaluations, 4,978 selector roots and one terminal topology gate, below their per-province ceilings. The machine receipt includes the full source and guard ledgers.

The legal C6→C7 component differences are:

| Component | Difference | Strictly below `1e-6` |
|---|---:|---|
| `Yt` | `2.120754606371733e-6` | No |
| `Lt` | `8.097409959662016e-6` | No |
| `wjt` | `6.637411149812422e-6` | No |
| `rk` | `2.8018973721621876e-5` | No |
| `Kt_prev` | `1.5887487027717394e-16` | Yes |
| `w` | `5.057762422211454e-7` | Yes |
| `raw_ra0` | `2.8018973721621876e-5` | No |
| `rah` | `2.4549538655715963e-5` | No |
| `S` | `1.686716673422739e-6` | No |

Both C6 and C7 had 31 clipped `ra` upper hits. These are report-only for the adopted nine-component criterion; the separate original MATLAB zero-hit predicate is false at both checkpoints. This legal first comparison missed the strict level and does not establish R2, a fixed point, GE or Results eligibility.

No turn8 household or other successor was run. Both scientific output roots remain untracked and preserved. The only intended staged paths are this report and its machine receipt. Independent GPT Work ACCEPT/REJECT of this bounded execution is the next gate. Results eligibility remains `FALSE`.
