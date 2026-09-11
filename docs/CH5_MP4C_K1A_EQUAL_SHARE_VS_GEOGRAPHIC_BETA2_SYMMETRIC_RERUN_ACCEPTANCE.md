# Chapter 5 MP4C K1A symmetric equal-share vs geographic beta=2 rerun acceptance

Date: 2026-09-11.

Reviewer verdict:

`K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTED__BOTH_PATHS_25_TURNS__ACCOUNTING_AND_SCOPE_GATES_PASS__PAYOFF_RETURN_REAUDIT_REQUIRED_BEFORE_K1B`

Accepted candidate:

`ca66dd5d7364f80ed2686d4d2e77a1a6adab2ecb`

## Scope accepted

The symmetric bounded K1A rerun is accepted as a bounded scientific mechanism diagnostic. Both preregistered paths completed 25/25 outer turns from byte-identical accepted initialization under the repaired same-`S` provenance validator:

- Path A: repaired equal-share, `beta_distance=0`, `beta_return=0`;
- Path B: pure geography, `beta_distance=2`, `beta_return=0`.

The accepted evidence supports K1 capital-accounting consistency, C1 joint accounting consistency, and a genuine post-turn-1 geography transmission through network-produced `rah` into household and subsequent firm states. It does not support steady-state, KFE, K1B/K2, annual, IRF, welfare or Results claims.

## Accepted evidence

- both paths: 25 completed turns;
- total trajectory invocations: 2;
- total HJB/KFE calls: 1550 / 1550;
- scientific retries: 0;
- MATLAB/K1B/standalone-KFE/GE/annual/shock/IRF/Results calls: 0;
- source-faithful labor preserved for all 1550 province-turn observations;
- capital share-column, origin-wealth, national-conservation, home-retention and same-`S` quantity/payoff identities passed;
- destination-`theta_j` double weighting: zero;
- C1 `GovInv=max(Ktarget-Kprivate,0)` passed throughout;
- `Kprivate>=Ktarget`: 0 / 0; private-only overshoot: 0 / 0;
- total K/target remained approximately one because C1 residual public assets filled the gap;
- corrected-2018 KFE observations remain `DIAGNOSTIC_ONLY`.

## Mechanism finding accepted

Turn 1 begins from the same entering household state, and C1 offsets the immediate private-K destination differences at total firm K. From turn 2 onward, geography changes network-produced `rah`, which enters household decisions and propagates to output, wages and later firm states. This establishes a real K1A network transmission channel within the bounded route.

The effect remains quantitatively moderate under the frozen `beta_distance=2` benchmark. At turn 25 the median B-minus-A private-K/target difference is about `-9.81e-05`; total-K medians remain 1 in both paths.

## Payoff-return blocker

The transitional K1A payoff bridge remains scientifically unresolved. Raw firm returns show persistent upper-bound pressure:

- Path A: `754/775` raw `ra0` observations above `.09`;
- Path B: `755/775` above `.09`;
- lower-bound clipping: zero in both paths.

Therefore the historical clipped/used `ra` can continue only as `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`. The bounded rerun does not justify treating `[.02,.09]` as an economically identified return range, nor does it justify switching directly to raw `ra0` without a separate source/unit/payoff audit.

## Independent KFE boundary

The corrected-2018 finite-box upper-b leakage plus MATLAB-style pinning remains an independent scientific blocker. This acceptance does not upgrade any KFE observation beyond `DIAGNOSTIC_ONLY`.

## Next gate

Before K1B runtime integration, perform a zero-science payoff-return re-audit using accepted source code and already-persisted K1A evidence. The audit must determine the source semantics, units/periodicity, clipping distortion, `ra0` decomposition and candidate payoff mappings without new HJB/KFE/firm/trajectory calls and without changing the active payoff law.

Results eligibility remains `FALSE`.
