# CH5 MP4C 2018 KFE D1-D3 simultaneous two-axis zero-drift switching implementation and V2 checkpoint-2 reexecution

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919`

## Terminal classification

`PASS__ADOPTED_JOINT_SWITCHING_V2_MAP_COMPLETE__CHECKPOINT2_NONCONVERGED__NO_V3_UPDATE`

The Owner-adopted joint switching law closes cell185 and the single fresh accepted-V2 policy map completes all 800 cells. One Q2 was assembled and one checkpoint-2 diagnostic evaluation was performed. Checkpoint 2 is not an HJB convergence candidate because both primary metrics fail their frozen inclusive thresholds. No V2-to-V3 update and no terminal topology/KFE/SVD operation was performed. Results eligibility remains `FALSE`.

## Git and frozen identities

- fresh live-main baseline: `0033e61b7bfbb3080c1aeac43b66a78d669d4571`;
- task branch: `codex/ch5-mp4c-2018-kfe-d123-simultaneous-two-axis-zero-drift-switching-implementation-v2-checkpoint2-20260919`;
- implementation/helper/test freeze commit used for the scientific run: `6c2bac9`;
- accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`;
- pre-adoption selector SHA-256: `3175FBBC99120A9735287594A27602205505048BADD11A989CEAC682BE6390D8`;
- implemented selector SHA-256: `7473C670DB67DB05B123D13755D0BFF503113C7FE65D6FB856DC137BC1DDE5DD`;
- Owner-adoption SHA-256: `0F2F66E67E2DC892551D12689B377E2350958806DBBBC8A01B2A23A73A1B689C`;
- post-execution scientific-code freeze matched the pre-execution freeze exactly;
- `deep-learning-hank` was never entered, read, searched, used or modified.

## Implemented scope

Only the corrected-diagnostic route changed. The selector now:

1. evaluates ordinary and existing one-axis candidates before considering a joint fallback;
2. restricts the joint candidate to interior-interior nodes with no asset-face active set;
3. requires two legal liquid-`Z` receipts in one transfer regime whose post-liquid `a` drifts form the adopted strict backward-positive / forward-negative crossing;
4. suppresses the joint fallback when an ordinary or one-axis candidate is already admissible;
5. sets `d_ZZ=-r_a*a`, uses unchanged D3, maps the closed illiquid derivative interval into `q_b`, and intersects it exactly with the closed liquid interval;
6. reuses the existing 513-point log screen and `brentq` tolerance on exactly that intersection, with one separately counted joint root;
7. reconstructs controls, KKT objects and Hamiltonian from the joint shadows, canonicalizing `g_b` and `g_a` only within the existing arithmetic bound;
8. creates one candidate with derivative identity `{b: zero, a: zero}` and no sequential liquid-`Z` or interior-`a` receipt duplication.

D1, D2, D3, ordinary upwinding, liquid-`Z`, one-axis interior-`a`, lower-`a` zero-kink, root algorithm/tolerance, grid, calibration, HJB law and production/source-faithful paths remain unchanged. The nonlinear mapper received only a backward-compatible joint-root ledger hook. The checkpoint-2 runner was rebound to this task, Owner adoption, selector identity, evidence root and terminal markers.

## Focused engineering gate

The final focused suite passed before scientific entry:

- `64 passed`, `0 failed`, `0 errors`, `0 skipped`;
- final pytest elapsed time: `0.97 s`;
- copied JUnit SHA-256: `F1C760E5A5FE8BE076BD7B24E24ECFA6A7087358C898A5B933EB924886E25BFA`;
- Python compilation: PASS;
- `git diff --check`: PASS.

Coverage includes exact cell185 interval/root/D3/residual closure, one-axis-first precedence, no boundary trigger, no cross-regime pairing, no sequential duplicate, exact cell100 one-axis selection, liquid-`Z`, lower-`a` zero-kink, upper/lower liquid-boundary behavior, unchanged D2 zero-drift consumption, and the affected D1/D3/KKT/selector/nonlinear-contract tests.

The first launcher command failed before module import because `src` was absent from `PYTHONPATH`. No evidence root was created, no accepted artifact was loaded, and no scientific counter advanced. The authorized pre-science launcher correction set `PYTHONPATH=src`; the one and only scientific map then ran. This was not a scientific retry.

## Exact cell185 joint-switch receipt

Durable receipt: `cell185_joint_switching_receipt.json`, SHA-256 `455933A7B1395B657DB73669735C46258E1B6B77F93BB52F1969B9D557C55282`.

- flat/index/state: `185`, `(5,9,0)`, `(b,a,z)=(-0.1578947368421053,4.7368421052631575,0.8)`;
- liquid derivative interval: `[0.009574726769001294,0.013362109688537174]`;
- illiquid derivative interval: `[0.008489317330830281,0.00857557540065246]`;
- post-liquid `a` drifts: backward `+0.009287240997760404`, forward `-0.005170298666228812`;
- `d_ZZ=-0.42626460578345887`, negative-transfer D3 ratio `q_a/q_b=0.7200216108914285`;
- exact joint `q_b` interval: `[0.011790364625750628,0.011910163904713082]`;
- fixed-transfer liquid endpoint values: `[-0.023007467717380714,+0.041147374843733764]`;
- root status/method: `ROOT_CONVERGED` / `BRENTQ_UNIQUE_LOG_SCREENED_EXACT_INTERVAL`;
- joint shadows: `q_b=0.0118331456615342`, `q_a=0.00852012060113076`;
- raw drifts: `g_b=3.33066907387547e-16`, `g_a=0`; canonical drifts: `g_b=0`, `g_a=0`;
- transfer-KKT residual: `0`;
- Hamiltonian: `-0.126060157849957`;
- D2 assembler admissible: `true`;
- selector outcome: `SELECTED_ADMISSIBLE`, selected uniquely.

The full map naturally produced two legal joint-root calls and selected joint policies at flat indices `185` and `205`. It produced seven one-axis interior-`a` candidates, of which four were admissible and three were selected at `100`, `120`, and `140`.

## Complete checkpoint 2

The 800-cell policy map completed and unchanged D2 assembly passed.

### P2 / u2 / Q2 identities

- P2 identity SHA-256: `EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`;
- u2 field SHA-256: `C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`;
- Q2 artifact SHA-256: `346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`;
- Q2 CSR data SHA-256: `3278FFDA5ABA29E8C8E7ECC84649DF7A787AD7BDA5E936657F585B65A9844BEB`;
- Q2 CSR indices SHA-256: `6FF05054740279B563416E942AFEC958804FBD1AF63C660C9877D3175FB5B066`;
- Q2 CSR indptr SHA-256: `180A552000B935F15F1934266DE86FF9E3D7550005366AB92B312793648F0200`;
- checkpoint-2 identity SHA-256: `71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`.

### D2 generator gate

- status: PASS;
- minimum offdiagonal: `1.5861421037712475e-08`;
- diagonal construction error: `0`;
- `max(abs(Q2 @ 1))=1.7763568394002505e-15`;
- maximum liquid coordinate-action error: `1.021405182655144e-14`;
- maximum illiquid coordinate-action error: `2.375877272697835e-14`;
- outward closed-face count/amount: `0 / 0`.

### Bellman/value convergence

- `B2=||rho*V2-u2-Q2*V2||_inf=0.006582827785543588`, above `1e-8`;
- value-change `D2=||V2-V1||_inf=0.05439336697877817`, above `1e-7`;
- frozen conjunctive inclusive convergence law: FAIL;
- disposition: checkpoint 2 is complete but nonconverged; no V3 update is authorized in this task.

### Policy/operator stability and cycle diagnostics

- policy identity changes versus checkpoint 1: `800/800`;
- maximum continuous changes: `c=3.6142618856952833`, `l=0.06228603610225203`, `d=1.9672263434019068`, `g_b=4.723128872129969`, `g_a=1.9672263434019066`, `q_b=0.0037659097466205323`, `q_a=0.0056126991338732325`, `utility=0.023374461508609515`;
- Q2 nnz: `3081`; Q2-Q1 difference nnz: `2813`;
- Q2-Q1 infinity norm: `24.371242907988112`; maximum absolute changed entry: `12.185621453994056`;
- sparsity pattern changed: `true`;
- exact-cycle period: none; an exact-cycle window is not yet available;
- approximate period-2/3: not evaluated as a positive cycle because the required four/six-checkpoint windows are unavailable.

Policy/operator stability is diagnostic only under the Owner law. These changes do not override the failed primary convergence metrics.

## Exact scientific ledger

| Operation | Calls |
|---|---:|
| accepted V1 artifact loads | 1 |
| accepted V2 artifact loads | 1 |
| accepted Q1 loads | 1 |
| fresh corrected V2 policy-map attempts | 1 |
| selector evaluations | 800 |
| total scalar-root invocations | 383 |
| existing interior-liquid `Z` root invocations | 157 |
| adopted interior-`a` switching root invocations | 2 |
| adopted joint-switching root invocations | 2 |
| D2/Q2 assemblies | 1 |
| checkpoint-2 diagnostic evaluations | 1 |
| direct HJB solves | 0 |
| V2-to-V3 HJB updates | 0 |
| ordinary graph/SCC summaries | 0 |
| terminal topology gates | 0 |
| terminal dense SVD | 0 |
| terminal normalized stationary candidates | 0 |
| terminal `Q.T@p` | 0 |
| scientific retries | 0 |
| solver substitutions | 0 |
| damping/relaxation/adaptive-Delta/continuation calls | 0 |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results calls | 0 |

Engineering fixture calls and the pre-import launcher failure are not scientific calls and are recorded separately from this ledger.

## Durable evidence and changed paths

Fresh no-overwrite evidence root:

`reports/ch5_mp4c_2018_kfe_d123_simultaneous_two_axis_zero_drift_switching_implementation_v2_checkpoint2_reexecution_20260919_run001`

- sealed-manifest schema: `CH5_D123_JOINT_SWITCHING_V2_CHECKPOINT2_REEXECUTION_V1`;
- sealed entries: `816`; sealed bytes: `13,114,324`;
- sealed-manifest SHA-256: `B3CC70792E41E0EBDDE138057406C86D07063AD44959B595FA1B503B9D5AE2EA`;
- scientific-code pre/post freeze: exact match;
- checkpoint evidence contains exactly 800 durable cell receipts, derivative receipt, P2/u2 arrays, Q2, D2 receipt, checkpoint metrics and cycle receipt.

Changed paths are limited to:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/checkpoint2_reexecution.py`;
- `tests/test_mp4c_2018_kfe_d123_joint_two_axis_zero_drift_switching.py`;
- the fresh evidence root above;
- this report.

No CURRENT file, task, source-faithful/production path, D1/D2/D3 equation, calibration, grid, tolerance, solver, convergence law or accepted artifact was modified. Main was not merged and no successor task was published.
