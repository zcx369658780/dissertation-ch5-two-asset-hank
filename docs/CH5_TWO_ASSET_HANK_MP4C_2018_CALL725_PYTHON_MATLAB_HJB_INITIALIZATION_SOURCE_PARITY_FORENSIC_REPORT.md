# MP4C 2018 call-725 Python/MATLAB HJB 初始化源级取证报告

日期：2026-09-04
任务：`CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_PYTHON_MATLAB_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC`

## 结论

`INITIALIZATION_FORMULAS_SOURCE_IDENTICAL__CROSS_LANGUAGE_DIVERGENCE_LIES_DOWNSTREAM__FURTHER_HJB_FORENSIC_REQUIRED`

Python 年度经验 helper 的 HJB 初始值/劳动构造，与受保护 MATLAB `HANK_2ASSETS_HJB.m` 的对应源表达式逐项一致；未建立 Python 初始化源码错配，也未建立 MATLAB 提取 evaluator 初始化错配。此前 call-725 的跨语言 HJB/aggregate 差异不能归因于本任务审计的初始化公式，后续只能在新的 Owner/L3 live task 下进行下游 HJB forensic。

同时，严格的持久化数组结论为：

`CROSS_LANGUAGE_INITIAL_ARRAY_DIRECT_COMPARISON_UNAVAILABLE__NO_REGENERATION`

Python call-725 证据只保存了 `(20,20,2)`、finite 标记和 V0/labor digest，未保存原始数组；MATLAB replay 保存了 `hjb100_initialization.mat` 与 `hjb500_initialization.mat`。因此没有重建任何初始化，也没有声称原始 Python/MATLAB 数组直接相等。

## Live 连续性与源身份

- `HEAD = origin/main = 469ca3e110235fa086413e513ff54872330278cc`，直接父提交为任务要求的 `3716ddd0ca0c39ce45ecfab96f4b0119046ce5dd`；执行开始时 ahead/behind `0/0`、tracked worktree clean。
- Python Git blob 与任务绑定一致：`mp4b_python_empirical.py` `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`；`matlab_faithful_two_asset_ha.py` `9e7dc9556a2b76811e78f89999abecc045886106`；adapter `0033baee136c0328e80ffb8b794a88d4405c976c`。
- 受保护 MATLAB 文件 SHA-256 全部匹配任务约束：`HANK_2ASSETS_HJB.m` `049136B7...F56C3EAE`、`HANK3_FOC.m` `772B7B7B...F8463D`、`HANK3_cost.m` `3504A74B...F9A3C`、`lab_solve2.m` `74FD6AE8...C5662C20`。

## 公式矩阵的源级结论

| 对象 | MATLAB | Python | 分类 |
| --- | --- | --- | --- |
| tapered return rate | HJB 第 81 行 `raah=rah.*(1-0.1*(ahmax./ah).^(-9))` | `r_a*(1-0.1*(a/a_max)^9)` | `SOURCE_IDENTICAL` |
| illiquid term in labor `temp` | 第 82–90 行：`Rah` 复制 `raah`，故 `Rah.*raah` | `effective*effective` | `SOURCE_IDENTICAL` |
| liquid rate/income | 第 79–80 行 `Rb` 的 `b<0` spread 与 `Rb.*bbb` | `rb` 同一分段与 `rb*b` | `SOURCE_IDENTICAL` |
| transfer 与 `temp` | `Rah.*raah+Rb.*bbb+Tt` | `effective*effective+rb*b+Tt` | `SOURCE_IDENTICAL` |
| wage argument | `lab_solve2` 分别接收 `(1-tau),w,z` | 预合成为 `wage=(1-tau)*w*z` | `REPRESENTATION_ONLY` |
| labor root | `lab_solve2` 第 11 行 residual | `_source_labor_root` 的同一 residual | `SOURCE_IDENTICAL` |
| initial resource | 第 111 行 `c0` | `c=wage*l+rb*b+Tt` | `SOURCE_IDENTICAL` |
| initial value | 第 112 行 `v02` | 冻结 `ga=2, alphal=1, frisch=.2` 下的 `(c^(1-gamma)/(1-gamma)-l^6/6)/rho` | `SOURCE_IDENTICAL` |
| shape/order | `(I,J,Nz)` / `i,j,nz` | `(b,a,z)` / `[i,j,k]` | `REPRESENTATION_ONLY` |

`effective` 的角色已从 faithful return 与 drift 源码交叉核定为**收益率**而非已经乘资产的 income flow：同一对象随后以 `mu_a=r_a_effective*a+transfer` 进入 drift。因此 `effective*effective` 不是本次能支持的漏乘资产或单位错误主张；它是 MATLAB `Rah.*raah` 的直接源级对应。

## Call-725 可达性与既有证据范围

静态调用链为：

`run_python_once -> solve_batch -> _source_initial_arrays -> solve_matlab_source_postloop_household -> solve_matlab_faithful_hjb`

故 call-725 确实使用该 constructor；这只建立其可达性，不替代缺失的跨语言原始-array 直接比较。

两个既有接受结论与本任务并不冲突：

- 50-state HJB parity 使用预冻结且共享的 `initialization.mat`（`5 x 5 x 2`）；它证明条件化的 HJB/fixed-point parity，不独立覆盖 800-state annual `_source_initial_arrays(...)`。
- Beijing same-input preflight 将重新计算的 Python constructor 输出与既有 `contract.python_mapping` 比较，未调用受保护 MATLAB 初始化；它不是 MATLAB 初始化公式的独立验证。

复用的 Python call-725 和 MATLAB call-725 audit manifest 分别重新哈希为任务要求的 `B15FE27...C7A0CF` 与 `87500F...02457B`。

## 运行边界与证据

科学调用账本全部为零：MATLAB HJB、Python HJB、MATLAB KFE、Python KFE、protected household、GE/stationary/annual、R/PLM、shock/IRF/Results 均为 `0`。本次仅进行了 source inspection、静态表达式比较、Git/文件 hash 与已持久化证据可用性检查。

外部 no-overwrite evidence root：

`D:\ProjectTemp\ch5-mp4c-2018-call725-hjb-initialization-source-parity-forensic-20260904-001`

其中包含 source maps、formula matrix、semantic/reachability/scope audits、数组可用性结论、zero-science ledger、stdout/stderr、audit manifest 和 readback。`audit_manifest.json` SHA-256：

`B3B0BE432A2CCED37812F21243CC6B032F7CEA1528EA5BAC10F23271E159A42B`

readback 已通过 JSON/CSV 解析与全部清单条目 hash 校验。

## 授权边界

未修改 production/protected/test/validator source，未给出 production correction candidate，未运行模型，也未重新运行 2018、GE、shock、IRF 或 Results。

唯一后续门：新的 live GitHub task 与 Owner/L3 明确授权，才可决定是否开展任何下游 HJB forensic、production redesign 或科学 rerun。

终局：

`MP4C_2018_CALL725_HJB_INITIALIZATION_SOURCE_PARITY_FORENSIC_COMPLETE__UPSTREAM_PARITY_BREAK_CLASSIFIED__NO_MODEL_RERUN_NO_PRODUCTION_CHANGE`
