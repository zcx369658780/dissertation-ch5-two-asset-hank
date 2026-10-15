# V0.0.10 唯一执行任务：1次corrected HA历史价格单点对照

**任务ID**：`V010_CORRECTED_HA_SINGLE_PRICE_POINT_ONE_ATTEMPT`。
**任务权限**：`OWNER_EXPLICIT_SINGLE_ATTEMPT_SYNTHETIC_HA_SCIENCE_AUTHORIZED`。
**角色**：Codex仅执行该1个科学尝试并交精确证据；Astra独立验收，Owner保留方向决策。旧SOURCE_ONLY失败提取与价格域调查已完成，不重做。任务一旦执行或STOP，不自动开新的science任务。

## 0. 正式冻结与候选身份：启动硬门

GitHub仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理发布分支`migration/astra-workflow-20261012`。
- **本次新增单点对照科学合同**：`versions/0.0.10/corrected_ha_price_probe_freeze_20261015.md`，固定 commit `81181490495f827aa0e15e6a6efb186e8addee67`，tree `846fd3f354d8f9d5d4978e15ad9ff78b71d2e451`，Git blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`。
- **本次完整输入manifest**：`versions/0.0.10/corrected_ha_price_probe_v1.json`，**同固定commit**、Git blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。运行时从此manifest按原字节读取`ha_inputs`，不从动态CURRENT、历史报告或临场命令行拼参数。
- **唯一Python固定源**：候选commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。这仅是工程限域接受而非HA/GE资格，绝不切到旧MATLAB-faithful solver或V008/V009。
- **历史V010冻结未改**：`versions/0.0.10/plan.md` @`bf091da33d59293f147d52c11580327d3ac2a85d`，blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原两省fixture blob `40915658d93403cfc21b33a6b864b332b7857749`。新manifest明确是**平行的单省诊断输入**，绝非覆盖或更新此两省fixture。
- 必须在首个science调用前核对以上全部Git身份、`ha_inputs`字段/源blob清单、模型源码的实际加载路径及依赖版本；任何不符立即STOP，不启动任何科学操作。

## 1. 唯一允许的科学操作

执行`ch5_two_asset_hank.multi_province.mainline_household_runtime.HAInputs`与`solve_conditioned_household(inputs, new_receipt_directory, ledger)` **且仅调用后者一次**；`ledger`应以专用新任务0调用开始，科学尝试在调用前先扣1/1，根及selector累计从首次V0开始精确计数。源包来自指定固定候选，不能替换`selector/generator/derivative/relaxation/KFE`算法。

本次HA输入完全取自冻结manifest：
- `rah=.0675`, `w_eff=15.5`（已经包含工资税的**有效**综合工资，不再扣一次）, `rb=.02`, `transfer=.1`, `rb_gap=.07`。
- 其余`parameters`全字段及`grid_spec`全字段取manifest原字节，`b∈[-2,5]`, `a∈[0,10]`, 20×20×2、F-order b-fast, `Delta=1000`。
- `V0`由现有`construct_v0`当次在所有800状态按冻结公式重新生成，不能读取原V010失败`V0`作为warm start、不能改网格/经济参数/容差/预算救PASS。

只观察本单省`CONDITIONAL_HA`：是否通过严格D1-D3/F0364合法策略、Q作用/边界、同checkpoint `B≤1e-8`且`D≤1e-7`、求解后向误差≤1e-12、单调性最多52次halving、唯一闭类source-free KFE及五字段聚合。任何关卡失败立即保留异常，绝不推进行政上未批准的第二点/另一期/双省外层/IRF。source-free KFE只允许在HJB门通过后执行一次；原MATLAB污染行KFE不允许作为替代。

注意历史`(.0675,15.5,.02)`是MATLAB-faithful原工资`w`数字坐标；这次为净工资`w_eff`数值相同但税/求解器含义不同，不能叫严格相同经济体复现。旧首次失败`(.055,1.7085897434929322,.02)`只作为已保存观察，不能反事实归因`rah`与`w`各自贡献。

## 2. 独立执行位置和真正硬预算

- 本轮全局新增科学次数：**仅1/1省级HA、1/1 science进程**；无需pytest（0进程）、无需本项目任何macro iteration、KFE/HJB之外模型运行、冲击/IRF/MATLAB；不启动V011。
- 代码`solve_conditioned_household`当前硬限制：HJB更新≤100、policy/Q maps≤101、selector cells≤80800、scalar-root总≤400000（含V0约800初值root）、稀疏value solve≤100、terminal source-free KFE≤1。原子选择器内部更低硬门仍适用，不能事后开大。
- 全部操作累计墙钟≤7200秒；新隔离输出+runner+日志+缓存≤32MiB；RSS目标≤512MiB（无法测`UNKNOWN`），新独立安全clone确需创建时新增Git对象/文件≤1GiB。达到硬限制就STOP，不能另起进程重新尝试。
- 唯一允许输出新路径`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_20261015_01`；每个run文件用互异新名字，禁止覆盖源回执。可以在该路径创建仅为组装冻结manifest、记录证据、执行唯一Python调用的简短私有runner，**不得修改任何已提交Python模型/数学/fixture/治理合同**；runner须记录原始文本SHA-256和精确source path。
- 旧`D:\ProjectTemp\c5k1bturn56`及8 tracked dirty、index、external common-dir、untracked/ignored、旧16文档镜像完全禁止写入/清理/checkout；原实施独立clone与D盘失败回执也禁止写入。可从原实施**独立clone只读加载**固定候选源，但必须满足`git rev-parse HEAD`、tree、逐项source blob、Python`__file__`对照；否则在独立新目录安全clone固定commit，不能附挂原dirty仓common-dir。禁止代码或证据push、改main/治理branch、访问其它仓库。
- 不读或计算现实C8/2017/2018/B3、旧V009失败数组、历史受保护科学mat与人工Newton路径。不得安装依赖或替换SciPy版本为了得到PASS；环境缺依赖可STOP并报告。已消费**旧V010**报告科学账`4/6 pytest、1/4 science driver、1/26 HA、1626 selector cells、1642 roots`作为历史**并行列账**，不得被本新一尝试清零、更名或充作续用余额。

## 3. 执行次序、产物与分类

A. **纯静态硬门预检**：确认仓库Git身份、冻结input blob、9份数学源blob、runner未改数学方程、软件版本和input `HAInputs`字段，唯一候选导入源路径；预先承诺一次run的输出路径，无任何HJB/KFE/selector/root活动。如预检失败，STOP且`new_science_attempts=0`。
B. **恰好一个受界尝试**：在新输出目录记录`start_utc`、本任务调用账，在调用前扣1；运行`HAInputs(...)`+一次`solve_conditioned_household`，允许其内部V0、≤100更新/101映射、条件满足才一次KFE。若失败保留`first_failed_cell`（若生成）、`attempt_summary`及合法的原生回执，返回非0科学失败分类；不试第二点、不补热启动、不修改方程。
C. **一次集中结果**：生成`V010_SINGLE_POINT_CORRECTED_HA_PRICE_PROBE_RESULT`，说明准确freeze/manifest/code blobs、Python/scipy/numpy与导入模块路径、V0 SHA/FOC/单调性、每checkpoint B/D及最后policy/Q/KFE质量（如到达）、第一个fail原因和最小候选reject频次（如失败）、roots/selector/updates/KFE、时间/内存/产物大小、所有STOP/UNKNOWN，及与原旧MATLAB-faithful实验**不等价**的范围。原始回执保持LOCAL_ONLY、只有极简脱敏摘要可公开；Codex不能自行对数值科学结果给Astra最终ACCEPT。
D. 只准出现一条本任务science run记录。可在不再调用科学模型的情况下纯只读汇总现有JSON日志、计算hash；任何进一步调用必须Owner/Astra另行前瞻性签发。运行后无论成功失败状态均`WAIT_ASTRA_V010_SINGLE_POINT_PRICE_PROBE_REVIEW / STOP`。

**全过程不改变A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、V011 NOT_STARTED。**
