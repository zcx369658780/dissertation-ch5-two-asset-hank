# MP4B instrumented MATLAB corrected-calendar-2009 one-shot trace

## Terminal verdict

`MP4B_INSTRUMENTED_MATLAB_CORRECTED_CALENDAR2009_SINGLE_RERUN_AND_CHRONOLOGICAL_PARITY_TRACE_BLOCKED`

Primary classification: `MP4B_INSTRUMENTED_MATLAB_RUN_BLOCKED`.

The Owner authorization was followed exactly as bounded:

> 同意授权一次 instrumented MATLAB corrected-2009 stationary rerun，仅增加逐轮 observability，禁止改方程、参数和算法，rerun=0。

The single MATLAB launcher process was started once at `2026-08-31T11:17:28.0340151Z` and ended at `2026-08-31T11:17:36.9548792Z` (exit `1`). It failed at the copied-wrapper source-binding guard, before `load_GDPdata` and before `mpHANK_equilibrium_2000`; therefore no top-level stationary, HJB, KFE, household, firm, or controller model call occurred. The task has no repair/retry lane, so no second MATLAB process or model call was made.

Exact emitted failure:

```text
MP4B:CopyBinding
required helper did not resolve from source_copy
```

The guard compared `fileparts(which(helper))` and the supplied `source_copy` with raw `strcmpi`. The command supplied a forward-slash path. This establishes a representation-sensitive source-copy binding failure; it does not identify which helper presentation differed, because obtaining that value would require another MATLAB execution, which this task forbids.

## Live continuity and authority

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Branch: `codex/ch5-adjustment-boundary-redesign`
- Live task authority / `HEAD` / `origin/main`: `69444469b67897d46e3450e126cb2ec5e3cb7ffa`
- Required direct parent: `f48ca0faf3fb626dbd65318773892d578c89c2d6` (verified as the sole parent)
- Fresh-fetch completed before work; pre-science and post-failure worktrees were clean, and ahead/behind was `0/0`.

All controlling authorities named by the task were read: `AGENTS.md`, the current rule index, GitHub capability/authority routing, local-file safety, and MATLAB diagnostic gates.

## Immutable identities and protected roots

The following repository SHA-256 identities all matched before the attempted launch: economics `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`; policy `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`; export `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`; MP2 `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`; MP3 `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`; stationary runtime `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0`; source map `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028`; source-postloop adapter `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06`; driver `9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E`; comparator contract `E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A`; field map `A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB`; helper `0FD6889E10E502F32C10B3373702445333B452B25A11A63A3899184A67853EF3` (Git blob `cbe7ce4e4855c139cc7bb3b20b56d124c4add266`).

`C:\MatlabProgram` was verified as Junction -> `D:\MatlabProgram`. The logical protected root `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK` and physical root `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK` both existed. Every protected source SHA matched both before and after the failed pre-model attempt:

| file | SHA-256 |
|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` |

D: had `75,422,593,024` free bytes. The source tree was `32,123,129` bytes; five times that size was `160,615,645` bytes, so the required `max(10 GiB, 5x tree)` gate passed.

## Corrected-calendar binding and preserved baseline

The canonical input `D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json` matched `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`: calendar year 2009, analysis/data-MAT index 1, data row 10 (Excel row 11), industry 4, regression vintage 10, and fixed-2020 `IND_Zt` initialization anchor.

The immutable preserved MATLAB root was reverified: output `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`; profile `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`; terminal `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`; presolver manifest `DF9380BB057ECF24E519BBF03D5A643036CC92B4FFAC18DB411B75783E5AABB9`.

The copied wrapper was constructed from the accepted direct route: copied working directory, `load_GDPdata(...,0.096,...)`, `data_MAT{1}`, and `mpHANK_equilibrium_2000(..., selected, 4, 10)`. Its required runtime binding manifest was not created because the guard stopped before data loading. Consequently, the binding was statically proven from source and preserved evidence, but not dynamically consumed.

## Copy, observability, and static audit

Fresh no-overwrite root: `D:\ProjectTemp\ch5-mp4b-instrumented-matlab-calendar2009-20260831-001`. It did not exist before creation. The copy preserved relative paths and the required filled workbook/cache. All 32 copied `.m` files matched the protected source before instrumentation.

Only the allowed copied objects changed: `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m`, and new `MP4B_OBS.m`; the bounded wrapper remained outside the repository. The observer prefix was absent from the protected tree before patching. Its patch only copies already-computed scalar/vector values to an in-memory global trace and performs one terminal serialization path. It adds no scientific-state assignment, equation/parameter/grid/tolerance/branch/multiplier/damping/update-order change, model call, retry, or per-event disk write.

`checkcode` was run on the observer, the three copied sources, and the wrapper. It returned exit `0`; its emitted diagnostics were existing/style/performance warnings, not syntax errors. The copy-diff allowlist and repository `git diff --check` both passed before launch.

Local diagnostic artifact identities:

| artifact | SHA-256 |
|---|---|
| `source_copy_manifest.json` | `1F40F2E207BEE74DCE49B5887CB581B39CA9CCA7C6EF7C8E18E13A685673FB59` |
| `instrumentation_manifest.json` | `2E61A340D3908BE473FB72AAFC4D0076420974B202136E71FDE07FDA1A97684A` |
| `instrumentation_manifest_revision_001.json` | `903EEFE050D65F9736820E3C0FFAC4E6496A0BFDF94726B14012158A0B38B5D9` |
| `instrumentation_patch.diff` | `8320F93726ADE831DE4B530551E66A153B7795E3AA7C36315C758D1F2025FDFA` |
| `instrumented_run_manifest.json` | `FF3417CA9D664807A424ED7D9A4EEAC279F2DCE506D301BD2EA1CF5052E0E50E` |
| `pre_science_gate.json` | `59E56A2C34C6BDE0FB06394322B964709A4477A4C4BC54E5304AA31CEAD16701` |
| `instrumented_terminal_status.json` | `AA88E352DF60D8366D40510544DC957B0E1B66DE4405880D0EAA5777B734C9A3` |

No invocation binding manifest, final-state MAT, trace MAT, trace summary, baseline-admissibility result, or chronological comparison exists, because the model call did not occur.

## Scientific ledger and unavailable analyses

| category | count |
|---|---:|
| MATLAB launcher process (pre-model failure) | 1 |
| instrumented corrected-2009 MATLAB stationary top-level | 0 |
| MATLAB reruns / other MATLAB model calls / HJB / KFE / household | 0 / 0 / 0 / 0 |
| Python stationary / household / HJB / KFE / MP2 / MP3 | 0 |
| qualified comparator, Zhejiang or Shanxi replay | 0 |
| other year/batch, shocks/AR1/transition/dynamics/IRF, R5/Results | 0 |

No baseline-admissibility comparison is available, so the trace is not admissible and no MATLAB/Python chronology, first numerical/categorical/controller divergence, extra low-return event, extra Zt-reset event, wage-boundary chronology, or same-input fault attribution may be claimed. The accepted prior facts remain unchanged but were not reinterpreted.

## Forbidden-operation audit and closeout

The original logical/physical MATLAB tree was never patched, saved to, or run as a mutated source. No protected Python/scientific module, comparator, test, contract, calibration, canonical data, rule, MP2, MP3, or production/export file changed. All copied sources and diagnostics remain external under `D:\ProjectTemp` and are excluded from Git.

Repository change scope is exactly this report. `git diff --check`, explicit-path staging, one execution commit, one non-force push, and GitHub blob read-back are completed in the Git closeout accompanying this report; no later scientific task was started.

Recommended next gate: publish a new, zero-science, copy-binding-path normalization/remediation task that may inspect this failed guard and must explicitly decide whether any future one-shot MATLAB authorization is warranted.
