# MP4B faithful raw-Vb modular candidate 50-state HJB revalidation

## Terminal verdict

`MP4B_FAITHFUL_RAW_VB_50STATE_HJB_REVALIDATION_PASS`

Established:

- `MP4B_FAITHFUL_RAW_VB_MODULAR_CANDIDATE_BYTE_IDENTITY_RESTORED_FOR_HJB_PASS`
- `MP4B_FAITHFUL_RAW_VB_HJB_CANDIDATE_STATIC_PREFLIGHT_PASS`
- `MP4B_FAITHFUL_RAW_VB_HJB_RUNNER_SOURCE_BINDING_STATIC_REVIEW_PASS`
- `MP4B_FAITHFUL_RAW_VB_HJB_RUNNER_ZERO_CALL_BOOTSTRAP_SMOKE_PASS`
- `MP4B_FAITHFUL_RAW_VB_50STATE_HJB_REVALIDATION_PREFLIGHT_PASS`
- `MATLAB_FAITHFUL_HJB_AFTER_RAW_VB_SOURCE_ORDER_REPAIR_PARITY_ACCEPTED`
- `MP4B_FAITHFUL_RAW_VB_MODULAR_CANDIDATE_50STATE_HJB_REVALIDATION_PASS`

The frozen modular patch is accepted through the faithful HJB/operator layer only. Temporary production bytes were rolled back before closeout.

## Continuity, patch and candidate identities

- Live task: `a3e94f28dcf2a5cbc3be71e10a1946c9aca2dac5`.
- Direct parent: `35ccd8a5ddf2ee99992dd4056cd689318788f5d8`.
- Entry worktree: clean.
- patch SHA-256: `0F044055DA9B4BFF22A2F8342EF189781AD3D536BFD2A67148C1182C1F9AB31D`.
- patched economics Git object/blob SHA-256: `810e0875febc873ae85bef7e88edd4de349b00b2` / `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`.
- patched policy Git object/blob SHA-256: `2021db630f3057026ffc37d375a43aaddbccec48` / `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`.
- unchanged operator: `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`.
- unchanged HJB: `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`.

The patch was applied exactly once. Candidate Git objects matched before any HJB execution; no post-patch edit or normalization occurred.

## Preserved fixture and comparator

Read-only accepted root: `D:\ProjectTemp\ch5-hjb-propagation-aware-final-20260830-001`.

- MATLAB HJB: `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94`.
- prior Python HJB: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.
- propagation-aware comparator: `E049D0B48901799A07D551978BF3C767CD326AB33034CC2C21CD2E2F815EE231`.
- comparator preflight: `6F1F12F28570B1DD846B047CD028CE150F1BDB4E32F6364421339357C33ADAA2`.
- freeze manifest: `EBF67BE53238B864BA5AEA459C164C13E9BB3F48AA79C45E4D103BED6C7E21BE`.
- parameter/grid manifest: `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A`.
- initialization: `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`.
- preserved Python runner: `CE3C320DC6D7014A692FE0B71165854236FECD0D23C0A8026C1BCD152D5FF2AC`.

The fixture remained `5 x 5 x 2`, `Delta=1000`, `crit=1e-7`, `maxit=100` with unchanged ordering, initialization, boundaries and switch matrix.

## Runner binding and zero-call smoke

Validation launcher: `validators/multi_province/mp4b_faithful_raw_vb_hjb_launcher.py`, SHA-256 `5726A22C94AE8741561F16F31D0EF72B14A8F9AE53FF8EA23CF68387A9B37980`.

It derives the repository and `src` roots from its own resolved path, inserts exact `src` before package import, verifies all `ch5_two_asset_hank` origins are inside that tree, verifies patched candidate Git objects and unchanged operator/HJB SHA values, and rejects `chapter5_model`.

One direct smoke ran from `D:\ProjectTemp`:

- root: `D:\ProjectTemp\ch5-mp4b-raw-vb-hjb-smoke-20260831-001`;
- smoke SHA-256: `14778712A4E66DAFA78C5705455D15D47FB4B355DD544593DE6CB8519B754484`;
- exact economics/policy/operator/HJB origins: PASS;
- HJB calls/iterations: `0/0`.

Fresh scientific root: `D:\ProjectTemp\ch5-mp4b-raw-vb-50state-hjb-20260831-001`. Preflight ledger SHA-256: `A185EF73B4A47815D757921483B96635A95BFE1447594B7A33884785DF50C900`.

## HJB and propagation-aware comparison

- repaired Python HJB output SHA-256: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.
- comparison SHA-256: `F7C1A55341C403535081C97195C082CB6B10702BE8A59982E3A7F37EFE5A717C`.
- Python converged: true.
- iterations: `12`, exact to MATLAB.
- Python convergence statistic: `9.07700581365134e-10`.
- maximum `V` difference: `2.0961010704922955e-13`, frozen bound `1e-7`: PASS.
- grid/order/initialization: exact.
- liquid/transfer labels: exact.
- derivative-floor pattern: exact.
- `Bswitch`: exact, raw maximum difference `0`.
- same-input continuous formula replay: PASS under `128*eps64*max(1,abs(x),abs(y))`.
- same-input sparse coefficient replay: PASS under the unchanged direct machine bound.
- mathematical sparse support: exact after removal of exact stored `0.0/-0.0` only.

Raw sparse diagnostics:

| operator | MATLAB/Python raw NNZ | raw pattern difference | exact-zero representation | raw max difference |
|---|---:|---:|---:|---:|
| BB | 96/97 | 1 | 1 | `4.769518113789672e-13` |
| AAH | 110/120 | 10 | 10 | `1.432187701766452e-13` |
| Bswitch | 100/100 | 0 | 0 | `0` |
| A | 217/217 | 0 | 0 | `5.098144129078719e-13` |
| BB_post | 89/89 | 0 | 0 | `4.773959005888173e-13` |
| AAH_post | 80/90 | 10 | 10 | `1.432187701766452e-13` |
| A_post | 179/179 | 0 | 0 | `4.773959005888173e-13` |

Total raw pattern differences/exact-zero representation differences: `21/21`. No nonzero support difference occurred.

Solver-propagated diagnostic maxima were labor `6.661338147750939e-14`, transfer and `mu_a` `7.16093850883226e-14`, `mu_b` `1.1934897514720433e-13`, and utility `1.0746958878371515e-13`. All are fully classified fixed-point propagation diagnostics with no same-input residual.

- material mismatches: `[]`.
- unresolved scientific residuals: `[]`.
- source/environment failures: `[]`.
- comparator: PASS.

## Calls, rollback and checks

| call | count |
|---|---:|
| zero-HJB bootstrap smoke | 1 |
| smoke HJB calls | 0 |
| repaired modular Python HJB | 1 |
| propagation-aware comparator | 1 |
| MATLAB HJB | 0 |
| MATLAB/Python local policy | 0/0 |
| MATLAB/Python KFE | 0/0 |
| standalone/Beijing/second-province household | 0 |
| MATLAB/Python stationary | 0/0 |
| MP2/MP3/annual/shocks/transition/dynamics/IRF/R5/Results | 0 |

Rollback identities:

- economics: `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`;
- faithful policy: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- standalone: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`;
- operator/HJB remained at their accepted hashes.

Final production/export mutation: `0`.

Checks: Python compile PASS; focused regressions `18 passed`; static route/source review PASS; `git diff --check` PASS. One nonexistent historical test-path probe returned no tests before the actual focused suite was run; it executed no scientific/model code and did not affect the one-shot ledger. Forbidden-operation audit: PASS.

## Exactly one recommended next gate

Reconstruct the accepted modular patch plus a source-identical standalone raw-`Vb` repair, then perform one Beijing first-turn MATLAB/standalone household parity and standalone export revalidation; do not yet authorize calendar-2009 multi-province stationary execution.
