# V010_STAGE_A_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY_RESULT

结论：A_STAGE_OBJECT_REACHABILITY_VERIFIED。仅报告 Git 对象与磁盘源码前置条件；等待 Astra 独立验收。

固定任务 commit 68530b3f121952b4382d08dc9ff964c7f6c7ab75，tree 70a7662ba654dff6acbe05e3a8b0444324b8f346，blob 3688674363aa8a0c45a7a322c9c2098baed62fae。已实际读取发行任务全文、当前 CURRENT/TASK_CURRENT 与前轮 FAIL_CLOSED 独立审议；各 blob 身份列在 manifest。前轮 STOP 与原回执不修改。

## Stage A 实际证据

指定远端 refs/heads/codex/ch5-v010-matlab-first-20261015 经一次 ls-remote 返回 94de4501dec051b969bee9d852eba2d4591f30ef。一次全新 no-checkout / single-branch / no-tags clone 明确取此模型分支；未浅克隆、partial clone、共享对象、使用旧 clone 或补 fetch。

在签出前核对 clone HEAD 与 origin 模型 ref 均为固定 commit；tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5；sole parent a1db8c114dec0ab69d69a5576e153a7f868cba0e。cat-file 实际读取 commit、root tree 和九个 blob 的对象字节，并按 Git 类型/长度前缀重算全部 11 个对象 SHA1，逐一匹配。不是只引用 show 文本。

show-toplevel、git-dir、common-dir、object-dir 均经绝对路径比较落在唯一新模型 clone；新路径链未见 reparse，alternates/shallow/promisor/partial 状态均无。子进程不继承外部 Git 环境，关闭 global/system 配置与系统 attributes，采用新空模板、空 hooks 目录；新 clone 配置未见外部 filter/include/object 路径。未读取或 stat 原保护树来制造保护证明。

A2 身份门通过后，设置 autocrlf=false，仅 sparse 签出九个精确源码路径并 detach 固定 commit，退出码 0；再次核 HEAD 正确。固定 commit 的 ls-tree 与磁盘只读 hash-object --no-filters 逐项相符；PowerShell 独立记录 SHA256 与字节数，未规范化换行、改字节或导入模块。未跟踪副本检查为空。

| 源码相对路径 | Git Blob（预期＝tree＝磁盘） | SHA256 | B |
|---|---|---|---|
| src/ch5_two_asset_hank/multi_province/mainline_household_runtime.py | 3d2d7d92aea0036f36d88ef15c05cbb3b40eba90 | 400F7D05BB63E235397F3BB66F0737B2A74E913665E206D1DE2586832C36480B | 16079 |
| src/ch5_two_asset_hank/corrected_diagnostic/selector.py | 51517dde0c829060b6e0c0d594ec60e7e6143883 | 25B93033FD886A159DBE74E219087250408A7239F370C8B64D3F58624418E1A4 | 62595 |
| src/ch5_two_asset_hank/corrected_diagnostic/generator.py | f86234340c6e09c7129225da1677614669754177 | EA3D168AAFA18E28889B59807A24065E9D4D34F01D222D58E8B1321CC7C89D1A | 5911 |
| src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py | e0fcbf01af9b1778d245d960fe85c592f55c032c | 62B5FFDB5C25500B5BD1A6E87C76D3FFBA0455B5AFD295343280EFACE42F13C4 | 41938 |
| src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py | a473f86eef22ad893673dba2a80ec8029de8afd1 | 189B3E6F010C346583CB2F52178DBB4AD67FAE1588A474DDA9CA477B28D5E399 | 70586 |
| src/ch5_two_asset_hank/corrected_diagnostic/contracts.py | 41186454de5ba1f55d3ba273f7ce57457ded11ca | 5E5DA41969571A463D89E589C6D9B4126A1F964E74DC5D15E12B278A0D73E89E | 2056 |
| src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py | f79e089f06d0d74867284dc88c94c594215dc02e | A6D1B5B46FC91C91E5F8C8C96F3D320677B10AA4D97665DBFD91C7B1471B7B76 | 7649 |
| src/ch5_two_asset_hank/corrected_diagnostic/v1_q1_topology.py | a238c999d3a6e18e8672efa1aae00498e747d403 | B40B1E03C8E67E8FF9D62C4D03D2B538D2725CE821BAD25CA2E6AA546390959E | 34326 |
| src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py | 45f4b95024c4441809dba3fe27044f25b3339f0f | 54680D232B1E383F880B13E5BBA1E079F3EB9953632FA94BA5478828BCF020DD | 29048 |

## 独立资源和回执

Stage A 模型网络顶层命令 2/2：一次精确 ref 查询、一次正确分支 clone。Stage A 显式 Git 共 14 条，全部 exit 0；逐条 exit/wall/stdout 与 stderr 哈希在 manifest，原始 argv 和本机路径仅留本机。Git 内部 spawn 数量 UNKNOWN，不以外层条数代替全部子进程数。

报告快照在 Stage A 与单独发布基线准备之后：Git 工作区合计 1008580801 B / 2 GiB，非 Git artifact 335526 B / 16 MiB，已用墙钟 364.413 s / 7200 s。这些是明确时点快照；发布后的最终对象/index、工件、累计写入保守扣账、最终墙钟和 Git 发布账在本机 DELIVERY_RECEIPT 中另行封存，不能将快照冒称最终总量。

发布基线额外取物仅为固定任务发行 commit，不补取模型 ref；采用新的独立 bare 元数据工作区，无共享对象。只允许本轮新 review 分支、两份文件、发行 commit 单父、一次普通 non-force push；发布后回读 ref/commit/tree/parent/两文件原字节。此文档不自行认证其未来发布步骤；最终结果以远端回读和本机封存为准。

全部新 Python/AST/import/pytest、工程 runner、HA/HJB/KFE/selector/roots/GE/IRF/MATLAB 与真实数据计算均 0。旧 Python 0/4 工程许可已经 STOP，未结转或续用。

## 限制、保护和停止

本地磁盘、命令次数、保护与资源记录归类 CODEX_REPORTED_WITH_LOCAL_RECEIPTS；GitHub 文档不能代替 Astra 对 Windows 本机过程的独立实测。模块 __file__/loader、Windows Popen audit、Job Object/timeout/reap、writer 故障路径与完整 runner I/O 均 NOT_RUN。未声明重建历史实际 argv。

原保护树、8 dirty/index/staged/common-dir/untracked/ignored、旧失败根未访问或修改；未改模型数学、经济参数、网格、阈值、runner 设计、manifest 或历史审议。原 driver1/4、HA1/26、pytest4/6、selector1626、roots1642、两笔单点 Python 各1/1 与旧存储超额全部保留。

ENGINEERING_RUNTIME_NOT_RUN、HA_SCIENCE_NOT_RUN、FULL_RUNNER_IO_CLOSURE=BLOCKED。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、C8 A-D REQUEST_ONLY、V011 NOT_STARTED 不变。Stage B–E 或科学 HA 须未来另行获得 Owner 授权，不能由本次 Stage A 结论自动启动。

最终停点：WAIT_ASTRA_V010_STAGE_A_GIT_OBJECT_REACHABILITY_REVIEW / STOP。
