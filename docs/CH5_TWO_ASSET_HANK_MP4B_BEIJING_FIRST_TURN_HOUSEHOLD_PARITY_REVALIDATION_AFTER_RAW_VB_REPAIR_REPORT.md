# MP4B Beijing first-turn household parity revalidation after raw-Vb repair

Date: 2026-08-31

## Terminal verdict and acceptance

`MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_PARITY_REVALIDATION_AFTER_RAW_VB_REPAIR_PASS`

Established:

- `MP4B_BEIJING_FIRST_TURN_MATLAB_STANDALONE_HOUSEHOLD_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_RAW_VB_REPAIRED_MODULAR_HOUSEHOLD_AUTHORITY_ACCEPTED`
- `MATLAB_FAITHFUL_RAW_VB_REPAIRED_STANDALONE_HOUSEHOLD_AUTHORITY_ACCEPTED`

This accepts the bounded repaired household block only. It does not accept calendar-2009 multi-province stationary equilibrium, GE closure, shocks, transitions, IRFs, historical R5, or Results.

## Live continuity and starting identities

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- live task authority: `a50ed9dd4893a8de59180ed9b300b66530d6dfcb`
- direct parent: accepted wrapper-smoke completion `1ff7722a969b736ef0a801d5502e4d332e43a869`
- entry worktree: clean
- fresh fetch/direct-parent continuity: PASS

Starting rolled-back identities matched:

- `economics.py`: `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`
- standalone: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

Protected MATLAB identities matched:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Accepted wrapper and smoke evidence matched:

- wrapper SHA: `518B0F9137ADA16155EE76EA2A08B21C0B3D91D67C321A2EF89C063B1EAC5AFD`
- focused-test SHA: `24C009E1D179D6F4FC8CB8DA96C2AF3AB7D057BD902EC93F6A34B373620CFF16`
- preserved smoke manifest SHA: `99C19A4C2676E052F7D5C3F2A8C3AF0CB704EADAF29E7D87EF7E4F0A4D40023D`
- preserved smoke marker and complete zero scientific ledger: PASS
- wrapper smoke rerun: `0`

Canonical and same-input identities matched:

- canonical 2009 input: `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- Beijing same-input contract: `FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22`

## Candidate restoration and final authority hashes

Frozen modular patch SHA:

`0F044055DA9B4BFF22A2F8342EF189781AD3D536BFD2A67148C1182C1F9AB31D`

Frozen standalone patch SHA:

`FC4DAC660130DEB73E1A88C6638F1C4B282D511AA06875123437693FBE4C5A71`

Both patches were applied exactly once to the required starting bytes. Final accepted production/export identities:

- `economics.py`: `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`; Git object `810e0875febc873ae85bef7e88edd4de349b00b2`
- `matlab_faithful_policy.py`: `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`; Git object `2021db630f3057026ffc37d375a43aaddbccec48`
- standalone: `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`

The corrected/reference transfer-helper path and accepted HJB/operator/KFE code outside the frozen patch were unchanged.

## Source-map disposition and preflight

Source map:

`validators/multi_province/mp4b_beijing_household_source_map.json`

SHA-256: `757A39B8EFCAD2F955EE8674DC424D0FA97F0C7751B8361995AFCB7AE0A5BD4E`.

Disposition: PASS and promoted for this bounded Beijing first-turn comparison. It binds every MATLAB `param`, `grid`, `num`, `CHI`, incoming `results`, and corresponding standalone argument to the frozen contract, canonical 2009 input, or exact protected-source assignment. Ambiguous execution-critical fields: empty. Historical R5 runtime dependency: false. Second-province state: false.

Established preflight markers:

- `MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_SAME_INPUT_SOURCE_MAP_PREFLIGHT_PASS`
- `MP4B_BEIJING_FIRST_TURN_MATLAB_HOUSEHOLD_RUNNER_AND_PERSISTENCE_PREFLIGHT_PASS`
- `MP4B_BEIJING_FIRST_TURN_STANDALONE_HOUSEHOLD_RUNNER_PREFLIGHT_PASS`
- `MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_COMPARATOR_CONTRACT_FROZEN`

The MATLAB runner contains exactly one accepted-wrapper `run` call; the wrapper contains exactly one protected `HANK_2ASSETS_HJB` call after its smoke return. The Python runner contains exactly one `solve_household_steady_state` expression. Forbidden controllers/routes are unreachable.

## Frozen comparator contract

Comparator contract SHA-256:

`7BAF5520C0E52D156709FA66E00423D892F926F94462EF2E72DC0FCC382458EC`

Frozen before either household output:

`abs(M-P) <= 1e-7 * max(1, abs(M), abs(P))`

Mandatory continuous fields: `Ct`, `Lt`, `At`, `Bt`, `At+Bt`. Both convergence flags, finiteness, asset labels, and arithmetic identity closures were categorical gates. Actual term count was 800 and `gamma_n = 1.776356839400566e-13` was retained as an explanatory binary64 reduction diagnostic.

`AtTax/AhTax`: `EXCLUDED_NOT_UNIQUELY_SOURCE_BACKED`. MATLAB exposes `AtTax`, but the accepted standalone top-level result does not expose a uniquely identical tax aggregate interface; no substitute was invented.

## Local evidence package

Root:

`D:\ProjectTemp\ch5-mp4b-beijing-household-parity-20260831-001`

Output manifest SHA-256:

`DC986F4A71D14D31A72B06403982E70CCA69B6208A381F701D69761D68987AFA`

Key artifacts:

| Artifact | SHA-256 |
|---|---|
| MATLAB full result | `024B097CEAC5872B5E83421B186C8424ECA92CD06A6D5D0FAF7B220BBFAB9DFE` |
| MATLAB summary | `04499A95BD6C7DD31ADE9C535AC94DAC28F7CA60853EEE4B737494D393E71677` |
| standalone full result | `9E9967F023C89F22550AEAC3C8CD53215B70E13C3C70E16C0CCC5C3D518A0F83` |
| standalone summary | `49CE323E84B1B8DDCF873B5CD68E02C61C79BF8B45026535C790AA2D214B0101` |
| qualified comparison | `28966B73605BD82BA858C3B2A3CBC144C867377C71476B1003846C88AE6382BF` |
| call ledger | `16FDE96E65F9FDC421CC27B90F80DB9E4D37832A70B736F128D1C04C65000666` |

## Scientific results and qualified comparison

Both household calls converged. Standalone HJB completed in 73 iterations with convergence statistic `4.312505907932973e-11`. Its contaminated-row KFE residual infinity norm was `4.37485523781054e-17`; density normalization was `0.9999999999999999`.

| Field | MATLAB | Standalone | Absolute difference | Relative difference | Frozen bound | Result |
|---|---:|---:|---:|---:|---:|---|
| `Ct` | 11.400731651946101 | 11.40073165194351 | 2.5917046286849654e-12 | 2.2732792138323528e-13 | 1.1400731651946101e-6 | PASS |
| `Lt` | 0.6476235981139693 | 0.6476235981138799 | 8.93729534823251e-14 | 1.3800138497516142e-13 | 1e-7 | PASS |
| `At` | 7.274097868486163 | 7.274097868485189 | 9.743317264110374e-13 | 1.3394536945016507e-13 | 7.274097868486163e-7 | PASS |
| `Bt` | 4.698277466946523 | 4.698277466946337 | 1.865174681370263e-13 | 3.9699117272068356e-14 | 4.698277466946523e-7 | PASS |
| `At+Bt` | 11.972375335432687 | 11.972375335431526 | 1.1617373729677638e-12 | 9.703482729359136e-14 | 1.1972375335432688e-6 | PASS |

- MATLAB convergence: true
- standalone convergence: true
- NaN/Inf: none
- MATLAB `At+Bt` closure: exactly 0
- standalone `At+Bt` closure: exactly 0
- material mismatch list: empty
- comparator result: PASS

## Post-PASS standalone revalidation

- standalone candidate exact SHA: PASS
- `py_compile`: PASS
- clean-process import/API smoke without solver invocation: PASS
- required household/HJB/KFE/aggregate public API: PASS
- repo production-module runtime imports: none
- historical R5 runtime imports: none
- focused/frozen export tests plus new preflight tests: `14 passed`
- MATLAB parity runner `checkcode(...,'-id')`: 0 findings
- `git diff --check`: PASS

## Complete scientific/model call ledger

| Route | Count |
|---|---:|
| MATLAB top-level `HANK_2ASSETS_HJB` | 1 |
| repaired standalone top-level `solve_household_steady_state` | 1 |
| qualified comparator | 1 |
| MATLAB household reruns | 0 |
| standalone household reruns | 0 |
| comparator reruns | 0 |
| modular Python household | 0 |
| separate modular HJB/KFE | 0 |
| MATLAB scalar/local-policy rerun | 0/0 |
| accepted 50-state HJB rerun | 0 |
| accepted wrapper/exact-junction smoke rerun | 0/0 |
| `HANK_mp_1turn` / `HANK_mp_1eq` | 0/0 |
| second-province household | 0 |
| MATLAB/Python calendar-2009 stationary | 0/0 |
| MP2/MP3 | 0/0 |
| annual batch/shocks/transition/dynamics/IRF/R5/Results | 0 |

## Production/export and forbidden-operation disposition

Production/export mutation is retained only at the exact three accepted candidate hashes listed above. No other production or protected source changed.

Forbidden-operation audit: PASS. No second province, multi-province controller, stationary route, accepted scalar/local-policy/50-state replay, annual batch, shock, transition, dynamics, IRF, historical R5, or Results route ran. No protected MATLAB, canonical input/data/cache, accepted wrapper, or frozen patch was modified.

## Exact staged path list

- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/matlab_faithful_policy.py`
- `exports/matlab_faithful_two_asset_ha.py`
- `validators/multi_province/mp4b_beijing_household_source_map.json`
- `validators/multi_province/mp4b_beijing_household_comparator_contract.json`
- `validators/multi_province/matlab/mp4b_beijing_household_parity_runner.m`
- `validators/multi_province/mp4b_beijing_household_parity.py`
- `tests/test_mp4b_beijing_household_parity_preflight.py`
- `docs/CH5_TWO_ASSET_HANK_MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_PARITY_REVALIDATION_AFTER_RAW_VB_REPAIR_REPORT.md`

## Git closeout

Explicit-path staging, one execution commit, one non-force push, GitHub read-back of every changed path, `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree are required.

## Exactly one recommended next gate

After independent L3 review, authorize one Python-only corrected-calendar-2009 multi-province stationary execution against the already preserved MATLAB 2009 baseline, with a separately frozen one-shot budget and comparator. The preserved MATLAB stationary baseline must not be rerun.
