# Chapter 5 Two-Asset HANK post-P5 D2 lower-a root certification diagnosis and resumption report

## Terminal verdict

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The isolated evidence supports diagnostic classification:

`LOWER_A_ACTIVE_ROOT_CERTIFICATION_SOLVER_REPRESENTATION_DEFECT`

The bounded external root refinement and its one-shot preflight passed. The authorized replacement D2 MATLAB call then persisted all ten frozen cases. The subsequent single frozen D2 Python call was consumed and failed before model evaluation because Python's default GBK text decoder could not decode the UTF-8 scientific manifest containing the Chinese MATLAB-source path. No repair or rerun was attempted. D2 comparison and D3 were therefore not reached. P5 remains Owner-accepted as `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`; the voluntary hold remains `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.

## Live authority and continuity

- Live start `origin/main`: `e5df6b54fd41fe956c09aae065d897c683022be5`.
- Branch/HEAD at execution start: `codex/ch5-adjustment-boundary-redesign` / `e5df6b54fd41fe956c09aae065d897c683022be5`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- Final `origin/main` observed immediately before report publication: `e5df6b54fd41fe956c09aae065d897c683022be5`; the publication commit SHA is recorded by the push/read-back closeout and final handoff.

## Artifact roots

- Accepted D1 root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Immediate predecessor root: `D:\ProjectTemp\ch5-post-p5-d2-categorical-terminal-resumption-artifacts-20260830-083000`.
- Fresh successor root: `D:\ProjectTemp\ch5-post-p5-d2-lower-a-root-diagnostic-artifacts-20260830-070101`.

## Reused accepted evidence

D1 hashes were re-verified from accepted continuity evidence and D1 calls remained exactly `0/0/0`:

- MATLAB: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

D1 remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maximum absolute differences `0`, and transfer-sign/a-direction/b-direction mismatches all `0`.

| Frozen artifact | SHA-256 | New engineering-preflight calls |
|---|---|---:|
| heterogeneous D2 MATLAB | `A7034181F3FC902E39EAB64CB8ED47C77BA52087B4E262325CAD33BAAECE3589` | 0 |
| D2 Python | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | n/a |
| corrected comparator | `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5` | 0 |
| D3 MATLAB | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` | n/a |
| D3 Python | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | n/a |
| scientific manifest | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` | n/a |
| accepted MATLAB heterogeneous preflight result | `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4` | 0 |
| accepted comparator preflight result | `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9` | 0 |

## Static root-path audit

The frozen `lower_a_active` inputs are `a=0`, `b=5`, `z=1.5625`, and `v_a=0.7619162076101915`. The D1 parameters used by this case are `gamma_c=1`, `phi=1`, `chi_0=0.05`, `chi_1=1`, `a_bar=0.5`, `r_a=0.04`, `r_b=0.03`, `tau=0`, `w=1`, and `labor_weight=1`.

MATLAB call chain:

`lower_a_active -> f=@(s_b) drift_b(s_b,v_a,a,b,z,p,true,-999) -> bracket_root(f,1e-10,1) -> cert_root(f,lo,hi) -> fzero(f,[lo hi],optimset('TolX',realmin)) -> abs(f(x))<=1e-12`.

Here `x=s_b` is the liquid shadow value/effective `v_b`. For a candidate `s_b`:

- `c=s_b^(-1/gamma_c)`;
- `l=(s_b*w*(1-tau)*z/labor_weight)^(1/phi)`;
- `q=v_a/s_b-1`;
- `d=max(a,a_bar)*(min(q+chi_0,0)+max(q-chi_0,0))/chi_1`, clipped to zero if negative on the active lower-`a` boundary;
- `f(s_b)=mu_b=r_b*b+w*(1-tau)*z*l-d-[chi_0*abs(d)+0.5*chi_1*d^2/max(a,a_bar)]-c`.

The bracket starts at `lo=1e-10`, `hi=1`, checks an exact zero at `lo` and a nonpositive endpoint product, and otherwise doubles `hi` for at most 80 iterations. `cert_root` first accepts either endpoint at residual `<=1e-12`; otherwise it uses exactly the `fzero` call above with only `TolX=realmin`, followed by the independent residual assertion. JSON numbers decode directly to MATLAB doubles; no explicit rounding or casting occurs before the solve. Other frozen D2 `cert_root` paths are calls through `bracket_root`, plus direct calls for `upper_a_interior_b` and `dual_upper`; none was executed in Phase A.

The corresponding Python path is `_zero_liquid_shadow` with the same `1e-10`/`1` initial bracket and 80-step upper doubling, the same controls/drift equation via `_controls_from_shadow_values` and `asset_drifts`, and `_certified_zero_drift_root`. It uses `brentq(..., xtol=np.nextafter(0.0,1.0), rtol=4*np.finfo(float).eps)` and independently evaluates the returned root's residual, rejecting nonfinite residuals or residuals above the shared `1e-12` tolerance.

## One-shot scalar diagnostic

- Harness: `lower_a_root_diagnostic.m`, SHA-256 `DC6A4B7EFD679965AFB9A9699BEB1C305CDA2DFA1098F98FCBCC9CC23AFBC6F0`.
- Frozen diagnostic ledger: `FF5B5860CE62DAD8330DC2FFA20168DBAF1DF6BC8975755AB0D8290CDD6C4555`.
- Invocation count / exit: `1 / 0`.
- Result SHA-256: `6C77624B69F1ECED1E54A216ABBA8D5BF28A031B83672AA74268774B8A26268C`.

| Quantity | Result |
|---|---:|
| `lo` / `hi` | `1e-10` / `1` |
| `f(lo)` | `-1.4512907695477412e19` |
| `f(hi)` | `1.59140625` |
| finite / sign-changing | `true / true` |
| original `fzero` candidate | `1` |
| original `fzero` residual | `1.59140625` |
| exit flag / iterations / function count | `1 / 1 / 3` |
| solver algorithm | `bisection, interpolation` |
| frozen-bisection candidate | `0.62824691073672034` |
| frozen-bisection residual | `9.2237328885858e-13` |
| iterations | `41` |
| final bracket width | `9.0949470177292824e-13` |
| no interior midpoint | `false` |

The valid identical bracket, uncertified original `fzero` result, and certified pre-declared bisection result satisfy classification A exactly: `LOWER_A_ACTIVE_ROOT_CERTIFICATION_SOLVER_REPRESENTATION_DEFECT`.

## Conditional external cert_root refinement

Corrected harness SHA-256: `A0E3426F1FB58563821C429A119445B659933D7E321E0EFBD3A7EED4690D8E51`. Complete frozen diff SHA-256: `512D4D9CE4E230C3F876D35E62495A495AEF1A763C370B52CDE9C2E949E6BE89`.

The complete change is confined to `cert_root`: retain the original endpoint checks and original `fzero` call; return the `fzero` candidate only if finite and residual-certified; otherwise run the same original-bracket, 256-step, sign-preserving ordinary bisection; return only a residual-certified candidate; otherwise raise `cert_root:UncertifiedRoot`. Every added or replaced line is classified `ROOT_CERTIFICATION_NUMERICAL_REFINEMENT_ONLY`. No root target, bracket construction, equation, case, parameter, state, KKT rule, output field, or tolerance changed.

Corrected-root preflight:

- harness SHA-256: `50259BD2B228EC0AC358CC7A2E3527D90548F02E9CBD71DDF0BE345EBFEF77C0`;
- invocation count / exit: `1 / 0`;
- result SHA-256: `2B01AD00F0CCF151D6BDC3EE46E476DA4BEC63FEE3A98B34CF299B0B5EEE8AB6`;
- same target/bracket: PASS;
- fallback used: `true`;
- candidate/residual: `0.62824691073672034` / `9.2237328885858e-13`;
- certification at unchanged `1e-12`: PASS.

## D2/D3 execution and call ledger

Historical D2 MATLAB calls remain separately recorded:

1. input-container blocker: `1`;
2. zero-field output-container blocker: `1`;
3. schema/comparator authority tasks: `0` scientific calls;
4. comparator-terminal task root-certification blocker: `1`;
5. current replacement D2 MATLAB: `1`.

Current replacement D2 MATLAB exited zero and persisted `d2_matlab.json`, SHA-256 `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`. Independent read-back found exactly ten records in frozen order, nine native 16-field normal rows and one native 10-field `lower_b_fz_near_tie` row, with no fabricated union fields.

The single D2 Python call exited `1` before producing `d2_python.json`:

`UnicodeDecodeError: 'gbk' codec can't decode byte 0xb4 in position 288: illegal multibyte sequence`

The failure occurred at `json.load(open(...manifest.json))`, before case evaluation. Per the no-repair/no-rerun boundary, no encoding adjustment or second call was attempted.

| Stage | Calls | Result |
|---|---:|---|
| D1 MATLAB/Python/compare | `0/0/0` | accepted reuse |
| Phase B scalar diagnostic | `1` | PASS |
| corrected-root preflight | `1` | PASS |
| current replacement D2 MATLAB | `1` | valid persistence |
| D2 Python/compare | `1/0` | Python source/environment blocker |
| D3 MATLAB/Python/compare | `0/0/0` | not reached |

D2 numerical maxima, worst cases, near-tie comparison, and categorical mismatch counts are unavailable because comparison was not reached. D3 360-case statistics are unavailable because D3 was not reached. Scientific mismatch list: empty. Source/environment failure list: the single default-GBK manifest decode failure above.

## Prohibition and Git closeout checks

- Production MATLAB/Python source, tests, helpers, and cache: unchanged.
- D1 and accepted engineering preflights: not rerun.
- No case/order/equation/parameter/shadow/state input/bracket/tolerance/KKT/output/comparator change.
- No taper, `Tt/rb_gap` adapter, hard-coded Python answer, HJB, KFE, steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results execution.
- Failed D2 Python stage was not repaired or rerun.
- Repository change before closeout: exactly this report; explicit-path staging only.
- Acceptance level: bounded diagnostic A and external correction/preflight accepted as evidence; full supplementary parity not accepted because D2 comparison and D3 were not reached.

Exact recommended next gate: publish only the smallest source/environment task that authorizes a frozen D2 Python manifest-text decoding correction or invocation-level UTF-8 environment contract, proves it without changing scientific inputs/equations/tolerances, and explicitly authorizes one replacement D2 Python call followed conditionally by the existing comparator and frozen D3. D1, the MATLAB replacement output, diagnostic, corrected-root preflight, and accepted engineering preflights must remain reuse-only.
