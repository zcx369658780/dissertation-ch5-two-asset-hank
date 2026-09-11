# Chapter 5 MP4C K1A symmetric equal-share vs geographic beta=2 rerun report

## Outcome

Verdict: `K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_COMPLETED__BOTH_PATHS_25_TURNS__ACCOUNTING_AND_SCOPE_GATES_PASS`.

Both preregistered paths were rerun from byte-identical accepted initialization under the repaired same-`S` provenance validator. Path A completed 25/25 turns and Path B completed 25/25 turns. Results eligibility remains `FALSE`.

## Authority and pre-run gate

- Live-main baseline: `1822b1a8b4786699e9137899e020cec37d15aa1d`.
- External evidence root: `D:\ProjectTemp\ch5-k1a-symmetric-rerun-evidence-20260911-001`.
- Path A: `beta_distance=0`, `beta_return=0`; Path B: `beta_distance=2`, `beta_return=0`.
- Validator accepts valid prior-completed K1A same-`S` `rah` and rejects a deliberately corrupted value.
- Focused zero-science tests, compile, protected-source diff and byte-identical input checks passed before science.
- No production-science source, equation, parameter, bound, tolerance, grid or solver semantic changed.

## Call ledger

| Item | Path A | Path B | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 25 | 25 | 50 |
| province updates | 775 | 775 | 1550 |
| HJB calls | 775 | 775 | 1550 |
| HJB direct solves | 19667 | 19836 | 39503 |
| KFE calls | 775 | 775 | 1550 |
| KFE direct solves | 775 | 775 | 1550 |
| labor-root/Brent calls | 620000 | 620000 | 1240000 |

Scientific retries were 0. MATLAB, K1B, standalone KFE experiments, GE, annual, shock/IRF and Results calls were all 0.

## Capital accounting and C1

Across the full 25-turn common prefix, Path A/Path B maximum share-column gaps were `1.3322676295501878e-15` / `3.3306690738754696e-16`. Maximum origin-capital residuals were `1.30385160446167e-08` / `3.725290298461914e-09` MU and maximum national residuals were `5.960464477539063e-08` / `4.470348358154297e-08` MU. Home retention and quantity/`rah` same-`S` identities passed throughout; destination-theta double weighting was zero.

C1 formula residual maxima were `2.9802322387695312e-08` / `2.9802322387695312e-08` MU. `Kprivate>=Ktarget` cases were 0 / 0; private-only overshoot maxima were `0.0` / `0.0`. Total K/target remained `0.9999999999999998 / 1.0 / 1.0000000000000002` for A and `0.9999999999999998 / 1.0 / 1.0000000000000002` for B.

## Symmetric A/B comparison

Pooled private K/target was `0.012678089017778033 / 0.04203715164074451 / 0.09974948873095775` for A and `0.01451147062307415 / 0.04193969784937715 / 0.0993234425547495` for B. Pooled GovInv/target was `0.9002505112690422 / 0.9579628483592556 / 0.987321910982222` / `0.9006765574452505 / 0.9580603021506228 / 0.9854885293769259`. At turn 25, B-minus-A median private K/target was `-9.808921304086532e-05`, while total-K medians were `1.0` / `1.0`.

The geography-induced portfolio difference propagated after turn 1 through network-produced `rah`, entering household `rah`, household outcomes and subsequent firm states. The complete turn-by-turn comparison is preserved in `common_prefix_comparison.csv`.

## Raw returns and convergence

Path A raw `ra0` min/median/max was `0.08782916734939869 / 0.26311547310366346 / 1.126705099083405` with 754 observations above `.09` and 754 upper clips. Path B was `0.08783627904873736 / 0.26309688368435974 / 1.1244507269044166` with 755 above `.09` and 755 upper clips. Lower clips were 0 / 0.

At turn 25, frozen final predicates were `False` / `False`; maximum `nk` gaps were `1.9399624129334825e-09` / `1.8619512598405663e-09`. HJB nonconverged-but-continued observations were 88 / 92.

## Boundaries and recommendation

Source-faithful labor remained active for every completed province-turn. All 1550 KFE observations remain `DIAGNOSTIC_ONLY`; corrected-2018 finite-box upper-b leakage plus MATLAB-style pinning remains an independent blocker.

Owner/Reviewer should prioritize a payoff-return re-audit before K1B; the persistent clipping pressure means the transitional clipped-ra payoff bridge still lacks final economic authority. The independent KFE boundary blocker remains open and is not resolved by this bounded comparison.

External manifest SHA-256: `DC3FAAD6FD919891F6EEF492B27100265998625907CA76A42F5C6663BE68512D`; readback checked 4981 files with status `PASS`. No successor task is published here.
