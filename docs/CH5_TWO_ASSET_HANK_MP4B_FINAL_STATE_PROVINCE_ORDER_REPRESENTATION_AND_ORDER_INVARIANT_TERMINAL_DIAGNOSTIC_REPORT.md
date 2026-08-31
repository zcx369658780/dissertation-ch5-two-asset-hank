# MP4B final-state province-order / representation and order-invariant terminal diagnostic

## Terminal verdict

`MP4B_FINAL_STATE_PROVINCE_ORDER_REPRESENTATION_AND_ORDER_INVARIANT_TERMINAL_DIAGNOSTIC_PASS`

Primary classification: `VALIDATION_COMPARATOR_MATLAB_STORAGE_ORDER_OR_STRING_REPRESENTATION_ERROR`.

The durable Python sequence is exactly the canonical 2009 sequence.  The MATLAB
`st.results` cell order is likewise that sequence by position, but its persisted
`prvname` strings use administrative suffixes for 25 entries.  The frozen helper
uses those raw strings unchanged, so its exact-name gate rejects the otherwise
positionally aligned terminal.  This is a string-representation failure, not a
discovered Python final-state reorder or a MATLAB cell-storage permutation.

This task does not claim corrected-calendar-2009 stationary parity.  In particular,
the independently extracted wage-boundary counts differ and remain material.

## Live continuity and immutable identity gate

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live task authority / HEAD at start: `72153e9b56bac067cbe78dffa4f2ebf05f456c75`
- Required direct parent: `ffd5b6a0437ea5699bd90f1ef02c0dc87800f9c0` (confirmed)
- Branch: `codex/ch5-adjustment-boundary-redesign`; fresh-fetch showed `HEAD == origin/main` and `0/0` ahead/behind before the diagnostic.
- Corrected entry-test Git blob: `89ff42fb99f24ed89ff162e69f2d6c3e01a052eb`.

All required SHA-256 identities matched exactly:

| Object | SHA-256 |
| --- | --- |
| `economics.py` | `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1` |
| `matlab_faithful_policy.py` | `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC` |
| MATLAB-faithful export | `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3` |
| MP2 one-turn | `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D` |
| MP3 steady-state | `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C` |
| stationary runtime | `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0` |
| source-semantics map | `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028` |
| source-postloop adapter | `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06` |
| validation driver | `9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E` |
| comparator contract | `E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A` |
| final-state field map | `A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB` |
| frozen comparator helper | `A6F7D2BBF7EE0936A6A0A45880B41D7AC77DB5AA7C3CA4B0F207F2D2A2DC08CF` |
| canonical 2009 input | `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48` |
| MATLAB stationary output | `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B` |
| MATLAB profile | `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C` |
| MATLAB terminal status | `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270` |
| Python run manifest | `030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774` |
| Python terminal summary | `CE943372D0F313A33E1D326747683F47CC3065B502A8B2646B492FF3B64A8F01` |
| Python turn-184 household output | `70442A793408DCDE20C84F83CA4795FA3EB95865052714F9FE9A31ABFC350442` |

The fresh no-overwrite evidence artifact is
`D:\ProjectTemp\ch5-mp4b-final-state-province-order-representation-order-invariant-diagnostic-20260831-001.json`
with SHA-256 `D4AF68622ECF3526784BC4C86AE1D1A08604A4D7F06D145A4D36DE013F0B941B`.
It contains every raw string, every canonical-string codepoint/UTF-8 hash, all 25
raw representation-mismatch codepoint/UTF-8 records, each reference path, and the
complete no-normalization comparison results.

## Raw province sequences and storage evidence

`st/results` and `st/grids` are each `(31, 1)` HDF5 object-reference arrays.  C
and F reference flattening therefore have the same 31-object sequence.  Each
`prvname` is a `uint16` `(2, 1)` or `(3, 1)` matrix; C and F character flattening
also agree.  Thus no reference-orientation permutation is present.

The field map explicitly identifies `st.results{i}.prvname`; MATLAB linear cell
indexing is column-major, so F traversal represents logical `i=1..31`.  The frozen
helper uses exactly `np.asarray(handle["st/results"]).reshape(-1, order="F")`,
then `np.asarray(dataset).reshape(-1)` for characters.  For this `(31,1)` / `(n,1)`
storage, the helper sequence is exactly the raw logical sequence below.

| i | Canonical input = Python manifest = Python terminal | MATLAB raw C order = F order = helper |
| ---: | --- | --- |
| 1 | 北京 | 北京市 |
| 2 | 天津 | 天津市 |
| 3 | 河北 | 河北省 |
| 4 | 山西 | 山西省 |
| 5 | 内蒙古 | 内蒙古 |
| 6 | 辽宁 | 辽宁省 |
| 7 | 吉林 | 吉林省 |
| 8 | 黑龙江 | 黑龙江 |
| 9 | 上海 | 上海市 |
| 10 | 江苏 | 江苏省 |
| 11 | 浙江 | 浙江省 |
| 12 | 安徽 | 安徽省 |
| 13 | 福建 | 福建省 |
| 14 | 江西 | 江西省 |
| 15 | 山东 | 山东省 |
| 16 | 河南 | 河南省 |
| 17 | 湖北 | 湖北省 |
| 18 | 湖南 | 湖南省 |
| 19 | 广东 | 广东省 |
| 20 | 广西 | 广西 |
| 21 | 海南 | 海南省 |
| 22 | 重庆 | 重庆市 |
| 23 | 四川 | 四川省 |
| 24 | 贵州 | 贵州省 |
| 25 | 云南 | 云南省 |
| 26 | 西藏 | 西藏 |
| 27 | 陕西 | 陕西省 |
| 28 | 甘肃 | 甘肃省 |
| 29 | 青海 | 青海省 |
| 30 | 宁夏 | 宁夏 |
| 31 | 新疆 | 新疆 |

Canonical, manifest, and Python terminal each have length 31, uniqueness 31,
exact name-set equality, exact order equality, no first mismatch, and identity
permutation `[1, …, 31]`.  Each raw MATLAB traversal has length 31 and uniqueness
31, but raw set/order equality to canonical is false; the first mismatch is index
1, `北京` (`U+5317 U+4EAC`, UTF-8 `e58c97e4baac`) versus `北京市`
(`U+5317 U+4EAC U+5E02`, UTF-8 `e58c97e4baace5b882`).  It has no raw
permutation because the raw name sets differ.

After the raw facts were recorded, an explicit non-mutating terminal-administrative-
suffix projection (`省`/`市` only) was evaluated as evidence: all 25 affected raw
names project position-by-position to canonical, yielding exact set/order equality
and identity permutation `[1, …, 31]`.  This is a diagnostic representation proof,
not a mutation, reordering, or comparator retry.

The raw representation mismatch indices are `1, 2, 3, 4, 6, 7, 9–19, 21–25,
27–29`.  In each record, the canonical codepoints are exactly the MATLAB raw
codepoints with one terminal `U+5E02` (municipality) or `U+7701` (province) added:
`1 北京/北京市: U+5317 U+4EAC / +U+5E02`; `2 天津/天津市: U+5929 U+6D25 / +U+5E02`;
`3 河北/河北省: U+6CB3 U+5317 / +U+7701`; `4 山西/山西省: U+5C71 U+897F / +U+7701`;
`6 辽宁/辽宁省: U+8FBD U+5B81 / +U+7701`; `7 吉林/吉林省: U+5409 U+6797 / +U+7701`;
`9 上海/上海市: U+4E0A U+6D77 / +U+5E02`; `10–19` respectively add `U+7701` to
`江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东`; `21 海南` adds `U+7701`;
`22 重庆` adds `U+5E02`; `23–25` respectively add `U+7701` to `四川、贵州、云南`; and
`27–29` respectively add `U+7701` to `陕西、甘肃、青海`.  The JSON records every
full codepoint list, UTF-8 byte sequence, and SHA-256 value individually.

## Order-invariant terminal facts

These are `ORDER_INVARIANT_DIAGNOSTIC_ONLY`: no tolerance was applied and they do
not constitute an aligned qualified comparator replay.

| Fact | MATLAB | Python |
| --- | ---: | ---: |
| Outer turns | 184 | 184 |
| Final household converged | 31 | 31 |
| `ra_upper_count` | 0 | 0 |
| `ra_lower_count` | 0 | 0 |
| `wage_upper_count` | 7 | 5 |
| `wage_lower_count` | 17 | 17 |

`MP4B_FINAL_WAGE_BOUNDARY_CATEGORY_MISMATCH_CONFIRMED_ORDER_INVARIANT` is
established directly from the immutable artifacts: Python wage upper/lower is
`5/17`; MATLAB is `7/17`.

| National sum | MATLAB raw | Python raw | Absolute | Relative | Normalized |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ct | 283.3909431582526 | 276.52720698365306 | 6.863736174599524 | 0.02422002657567868 | 0.02422002657567868 |
| At | 47.95553248807161 | 47.11415467808319 | 0.8413778099884226 | 0.017544958137993893 | 0.017544958137993893 |
| Bt | 65.2831672243048 | 65.21538414270965 | 0.06778308159515234 | 0.0010382933990052618 | 0.0010382933990052618 |
| Yt | 350556701.89460325 | 350585612.6035657 | 28910.70896244049 | 0.00008246404850370191 | 0.00008246404850370191 |

Representation mismatch list: the 25 terminal administrative-suffix differences
above, with no storage-order permutation.  Material scientific mismatch list:

- Confirmed order-invariant wage-upper category difference, `7` MATLAB versus `5` Python.
- The displayed order-invariant national raw differences, retained without a tolerance or acceptance claim.

## Execution audit and closeout

- No diagnostic helper was added, so `py_compile` and focused helper tests were not applicable.
- No Python stationary, adapter, HJB, KFE, household aggregation, MP2/MP3 scientific execution, qualified comparator/`compare_terminal`, MATLAB, Shanxi replay, other year/batch, shocks/AR1/transition/dynamics/IRF, historical R5 runtime, or Results activity was run: every zero-model ledger category is `0`.
- Historical-R5 scan found no active `chapter5_model`/R5 runtime dependency; matches were only deliberate static guards/tests and inactive forbidden-string checks.
- No scientific, validation-driver, adapter, comparator-helper/contract/field-map, export, MATLAB, canonical-data, or project-rule file was modified.
- The only repository change is this report; the only local artifact write was the fresh no-overwrite JSON named above.
- `git diff --check`, explicit-path commit/push, GitHub read-back, final `HEAD == origin/main`, `0/0`, and clean-worktree verification follow this report creation.

Recommended next gate: one zero-science comparator-helper representation-contract remediation plus one separately authorized comparator-only replay against these already durable terminals, explicitly preserving the confirmed order-invariant wage-boundary mismatch and without a stationary rerun.
