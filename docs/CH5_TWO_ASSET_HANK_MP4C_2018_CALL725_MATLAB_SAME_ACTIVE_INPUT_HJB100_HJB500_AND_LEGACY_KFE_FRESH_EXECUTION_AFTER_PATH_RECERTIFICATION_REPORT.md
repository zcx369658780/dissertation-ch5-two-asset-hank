# MP4C 2018 Call-725 MATLAB Termination Replay After Path Recertification

## Terminal result

`MP4C_2018_CALL725_MATLAB_FRESH_TERMINATION_REPLAY_COMPLETE__CROSS_LANGUAGE_HJB_CEILING_AND_LEGACY_KFE_CLASSIFIED__NO_GE_NO_PRODUCTION_CHANGE`

Scientific classification:

`MATLAB_CALL725_HJB100_NONCONVERGED_AND_HJB500_CONVERGED__LEGACY_KFE_OR_AGGREGATE_PARITY_FAILS__CROSS_LANGUAGE_TERMINATION_POLICY_NOT_YET_ACCEPTED`

The isolated MATLAB replay confirms the qualitative 100-to-500 ceiling pattern, but it does not establish cross-language termination-policy acceptance: HJB stopping diagnostics differ, and all five requested legacy-KFE household aggregates fail the existing machine-scale comparisons. No production `maxit` change, annual/GE rerun, shock/IRF, or Results work is authorized by this result.

## Authority, source, and path identity

- Live task: `de55daf037141e1b666157bf263e705a021037ce`, direct child of `b5c45a8f0dbef7919d8e9dee1b672a889fd4605d`.
- External no-overwrite evidence root: `D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001`.
- Evidence audit-manifest SHA-256: `87500FF3121ECBBEE1E18A0A574371E06AC2B03B6B24B13465FCFBBF1E02457B`; readback passed for all 32 listed artifacts.
- Reused path-recertification manifest SHA-256: `A94A24DD4C32B9DE816B7E3A9B8E507CDC755BEB2759E472FD139BDEDBAD5F75`.
- Reused Python predecessor manifest SHA-256: `B15FE27D8531D5A1CE65E5D881327F820D82501FABD10B789F9F8B0544C7A0CF`.

The certified finite pair was reused without a new collector campaign:

- logical root: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`
- physical root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

A fresh pre-call 8/8 logical/physical source-hash check passed for `HANK_2ASSETS_HJB.m`, `HANK3_FOC.m`, `HANK3_cost.m`, and `lab_solve2.m`, using the frozen task SHA-256 values. No protected MATLAB file or repository production/model/test/validator source changed.

## Frozen same-HJB-active-input contract

The execution scope is isolated Anhui call 725 (zero-based province index 11, outer iteration 24), with captured active inputs `rah=0.09`, `rb=0.02`, `rb_gap=0.07`, `tau=0.05`, `w=16.82014806560587`, and `Tt=0.1`. It is a same-HJB-active-input diagnostic, not a reconstructed annual or GE input state.

The protected source audit froze `num.maxit` as the HJB ceiling, `num.crit=1e-7`, `num.Delta=1000`, the 20x20x2 grid (`b=[-2,5]`, `a=[0,10]`, `z=[0.8,1.3]`), the source switch matrix, `ga=2`, `alphap=1`, `alphal=1`, `rho=0.05`, `frisch_l=0.2`, `chi0=0.1`, `chi1=2`, `a_bar=1e-6`, and zero `fixcost` fields.

The evaluator is the byte-identical accepted source-extracted HJB evaluator, SHA-256 `F6D33348329D242AC3C7D867D455DDD0B87184C00A5AD66332A1B62F359599FE`, mapped to `HANK_2ASSETS_HJB.m` lines 2–261 with the previously accepted sparse-boundary assembly. The fresh adaptation is limited to the external JSON active-input manifest and no-overwrite persistence paths.

`results.rb`, `results.rah`, `results.w`, `results.rb_gap`, `results.tau`, and `results.Tt` are HJB-active. The protected source reads preceding `results.Ct/At/Bt/Lt` only to publish output differences; they do not affect HJB iteration, post-loop KFE, or the requested aggregate formulas. `prvname`, `Zt`, `Kt`, `Kt0`, `alpha`, and `wjt` are display-only when `show_result=0`. No missing execution-critical field was guessed.

## Exactly-once MATLAB execution

| Phase | Budget | MATLAB result | Python frozen comparator | Classification |
| --- | ---: | --- | --- | --- |
| HJB100 | 1/1 | nonconverged; 100 iterations; statistic `1.179090496462085`; 800x800 post-loop A, 3,133 nnz | nonconverged; 100 iterations; statistic `0.3038218386543494` | convergence and iteration match; statistic differs by `0.8752686578077356` |
| HJB500 | 1/1 | converged; 275 iterations; statistic `2.8165643151112363e-9`; 800x800 post-loop A, 3,141 nnz | converged; 196 iterations; statistic `2.2986279546444166e-10` | convergence matches; iterations and statistic differ |
| Legacy KFE | 1/1 | finite direct solve on HJB500 post-loop operator | Python frozen HJB500 legacy KFE reused only | admissible density, but aggregate parity fails |

Each HJB phase created its own original source initialization; HJB500 was not warm-started from HJB100. Both persisted value/policy arrays and post-loop operator values are finite. MATLAB emitted near-singular-matrix warnings during HJB solves; these warnings and all stdout/stderr are retained in the evidence root. No post-call instrumentation failed and no scientific phase was repeated.

The frozen propagation-aware contract remains the applicable comparator. The compact Python predecessor does not persist the full field/operator arrays needed to recompute its direct per-cell formula/coefficient replay in this task, so no new direct-formula-parity pass is asserted. The recorded status, iteration, statistic, persisted MATLAB operator objects, and aggregate comparison are the supported comparison evidence.

## Legacy KFE and aggregates

The unchanged source-faithful KFE used 800 states, MATLAB row 296, a unit-row replacement, RHS `0.007`, direct full solve, `db=7/19`, `dah=10/19`, and source normalization. It used no G1/G2, adaptive row, mass gauge, regularization, pseudoinverse, fallback, clipping, or retry.

| KFE diagnostic | MATLAB result |
| --- | ---: |
| Normalized mass / error | `0.9999999999999998` / `2.220446049250313e-16` |
| Raw residual infinity norm | `2.8790861635410482e-17` |
| Backward-error bound / result | `7.80160038643087e-11` / PASS |
| Minimum / maximum density | `-2.6926525458407159e-31` / `0.97243439345346494` |
| Negative entries / weighted negative mass | `309` / `5.3112795854050162e-32` |
| Entries below direct machine tolerance | `0` |

The density is admissible under the frozen source-faithful KFE certificate. It does not rescue aggregate parity:

| Aggregate | MATLAB | Python reuse | Absolute difference |
| --- | ---: | ---: | ---: |
| `C` | `10.348917406683825` | `10.434969443057815` | `0.0860520363739905` |
| `L` | `0.6299111335699775` | `0.6241861388467347` | `0.005724994723242838` |
| `A` | `9.158607546031737` | `9.212879584614942` | `0.05427203858320517` |
| `B` | `-0.5923242681529719` | `-1.5496915046150406` | `0.9573672364620687` |
| `A+B` | `8.566283277878766` | `7.663188079999902` | `0.9030951978788639` |

Every aggregate exceeds its existing `128*eps64*max(1,abs(MATLAB),abs(Python))` machine-scale bound. No broader tolerance was introduced after observation.

## Ledger and boundary

| Call category | Count |
| --- | ---: |
| MATLAB source-extracted HJB100 | 1 |
| MATLAB source-extracted HJB500 | 1 |
| MATLAB source-faithful legacy KFE | 1 |
| MATLAB protected `HANK_2ASSETS_HJB` function calls | 0 |
| Retries | 0 |
| Python scientific calls | 0 |
| GE, annual 2018, stationary outer loop, R/PLM, shock, IRF, Results | 0 each |

The permanent predecessor caveat remains: `CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED`.

This task is complete. The next decision requires Owner/L3 review; it may not be inferred from this report, and this result does not authorize a production repair or any 2018 rerun.
