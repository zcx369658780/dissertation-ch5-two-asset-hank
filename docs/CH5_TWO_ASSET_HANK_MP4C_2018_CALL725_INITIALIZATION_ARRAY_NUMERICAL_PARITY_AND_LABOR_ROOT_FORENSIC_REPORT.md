# MP4C 2018 call-725 初始化数组数值 parity 与劳动根取证

日期：2026-09-04

## 终局

`CALL725_INITIALIZATION_ARRAYS_NUMERICALLY_PARITY_ACCEPTED__DIVERGENCE_BEGINS_INSIDE_HJB_ITERATION_OR_LINEAR_SOLVE`

Python 与 MATLAB 真正进入 call-725 HJB 的初始 `V0` 和 baseline labor 均满足既有 machine rule。它们不是 canonical float64 C-byte bitwise 相同，但没有任何单元超过 `128*eps64*max(1,abs(Python),abs(MATLAB))`。因此此前 HJB100/HJB500 差异不再可归因于预-HJB initialization 数值差异；本结论不授权任何 HJB、KFE、production repair 或 rerun。

## 连续性、输入与 Phase A digest gate

- live start 为 `HEAD = origin/main = 3f8f27aa5cb4b102828a84198b121a2d14d58e4a`，直接父提交 `b9b768e9d6f964fa30f537e3fd43281a7878a4af`，ahead/behind `0/0`、tracked worktree clean。
- 三个绑定 Git blob 与原 call-725 evidence 一致：empirical helper `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`、faithful export `9e7dc9556a2b76811e78f89999abecc045886106`、adapter `0033baee136c0328e80ffb8b794a88d4405c976c`。受保护 HJB 与 `lab_solve2` SHA-256 亦分别匹配 `049136B7...F56C3EAE` 和 `74FD6AE8...C5662C20`。
- 原始 Python evidence 的 audit manifest、MATLAB evidence manifest、父 source-forensic manifest 均重新验证为任务要求的 `B15FE27...C7A0CF`、`87500F...02457B`、`B3B0BE...124790`。
- Phase A digest contract 由 audit-bound 原 `run_call725_diagnostic.py` 第 188–191 行无歧义恢复：`hashlib.sha256(array.astype(np.float64).tobytes()).hexdigest().upper()`，即 native float64、C-order byte serialization、SHA-256。捕获和本次 runtime 均为 Windows AMD64/little-endian、Python 3.11.9、NumPy 2.4.6、SciPy 1.17.1。

## 唯一 Python regeneration

对冻结的安徽 / index 11 / outer-24 / global-call-725 state，仅调用一次 `_source_initial_arrays(...)`。使用的输入为 `rah=.09`、`rb=.02`、`rb_gap=.07`、`tau=.05`、`w=16.82014806560587`、`Tt=.1`，及冻结 `20 x 20 x 2` `(b,a,z)` grid 和参数。

该一次 constructor 内完成 800 个正常 scalar labor-root solves，retries 为 0；没有调用 adapter、household、HJB 或 KFE。再生结果与原 Python commitments 精确一致：

| 对象 | 原始 SHA-256 digest | 再生 digest | 结果 |
| --- | --- | --- | --- |
| `V0` | `D07742C5...195285A` | `D07742C5...195285A` | exact PASS |
| baseline labor | `BA2731D9...48B541` | `BA2731D9...48B541` | exact PASS |

## MATLAB restart 与跨语言数组比较

持久化 `hjb100_initialization.mat` 和 `hjb500_initialization.mat` 的 `b`、`ah`、`z`、`l0`、`c0`、`v0` 均逐元素 exact equal、finite 且维度一致。两个 MAT container hash 不同只因各自 header creation timestamp；它们的初始化字段值没有差异。

| 对象 | canonical bitwise | max abs diff | max normalized diff | 超过 machine rule 单元 | 最坏 `(b,a,z)` |
| --- | ---: | ---: | ---: | ---: | --- |
| baseline labor | false | `3.1086244689504383e-15` | `0.109375` | 0 | `(0,1,0)` = `(-2,0.5263157894736842,0.8)` |
| `V0` | false | `8.881784197001252e-16` | `0.01368731378888698` | 0 | `(0,0,0)` = `(-2,0,0.8)` |

两侧 shape/order 对齐为 `(b,a,z)` / MATLAB `(I,J,Nz)`，所有元素 finite。仅在 canonical byte 级别存在极小浮点舍入差，均远低于固定规则，未事后扩张 tolerance。

## 劳动根与 V0 分解

由于 labor 不是 bitwise identical，已对两侧已持久化 labor 代入同一冻结 residual（不重新求根）。Python/MATLAB residual maximum absolute values分别为 `4.218847493575595e-15` 与 `2.220446049250313e-16`；两者均在既有 machine rule 内。因此该观察只表明两种实现给出了 machine-equivalent floating roots；它不足以把 proximal cause 断言为某一 root solver。

按冻结 `c0`/`v02` 公式、保留源中的浮点指数求值顺序，V0 observed-minus-labor-propagated 最大差为 `4.440892098500626e-16`，最大 normalized 值 `0.009133368848681786`，越界单元为 0。故 V0 的可见差异在相同 machine rule 下可由 labor propagation 完全解释。

## 调用账本与证据

- `_source_initial_arrays`：`1`；内部 scalar labor roots：`800`；constructor retries：`0`。
- MATLAB/Python HJB、MATLAB/Python KFE、protected household、GE/stationary/annual、R/PLM、shock/IRF/Results：全部 `0`。

no-overwrite evidence root：

`D:\ProjectTemp\ch5-mp4c-2018-call725-initialization-array-numerical-parity-20260904-001`

其中包含 regenerated `.npy` arrays、原 digest contract、MATLAB artifact/restart identity、逐单元 CSV、residual 与 V0 decomposition、ledger、audit/readback。初始 `audit_manifest.json` SHA-256 为：

`039F363E7C91494EAC3FB0AA66046853C7939E71F951A9CDB8BBA211AB124790`

为覆盖保留的 source-order V0 decomposition 修正，另建了不覆盖既有文件的最终 supplemental manifest：

`817845439CDC77E2C3873AA3D9675E16704E0AB48263F02CFBD653626245D07C`

该 manifest 覆盖 25 个当前证据条目；final readback 已逐项重哈希，并解析全部 JSON 和 3 份 CSV，SHA-256 为 `A1F50E1EBAE9DC6B91BB09EE3F7DF5AC5A979E4EF124981C893768CFCFAA8AA1`。早期使用整数指数替换的 V0 decomposition 仅保留作可审计历史，已由 source-order-preserving artifact 明确 supersede。

## 边界

未修改任何 production/test/validator/protected MATLAB source。只有新的 Owner/L3 live GitHub task 才能决定是否开展以共同初始化为前提的 first-iteration HJB forensic；本任务不自动启动该路线。

终局：

`MP4C_2018_CALL725_INITIALIZATION_ARRAY_NUMERICAL_PARITY_FORENSIC_COMPLETE__PRE_HJB_NUMERICAL_PARITY_CLASSIFIED__NO_HJB_NO_KFE_NO_PRODUCTION_CHANGE`
