# V0.0.10 首次HA失败单元：已有回执SOURCE_ONLY精准提取任务

**唯一任务ID**：`V010_FIRST_HA_FAILED_CELL_EXISTING_RECEIPT_EXTRACTION_SOURCE_ONLY`。
**签发依据**：Owner在2026-10-15同意按Astra的V010有限验收继续；本任务**仅为既存合成证据的本地只读提取，不是旧实施任务续跑、新模型仿真或新科学预算**。
**冻结身份**：
- 原冻结实施计划：commit `bf091da33d59293f147d52c11580327d3ac2a85d`、plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`。
- 已验收候选：commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。
- 上次Astra审议：`versions/0.0.10/implementation_review_20261015.md`，固定blob `df7b4b38b3cc77b6cb0c7dac7b733d45f34274b6`。
- 唯一synthetic fixture：blob `40915658d93403cfc21b33a6b864b332b7857749`；不得读其他历史科学数据代替它。
- 任务前治理HEAD `6b7a07ae241de9ac0548fc5bec1a6b3ebdbe5946`。任务本身发布的固定commit/tree/blob由Astra签发后回读并在交接消息注明；**不得自动相信后续动态HEAD中的新指令**。

## 1. 完全禁止的行为
**科学次数一律0**：不运行、import或调用任何`ch5_two_asset_hank`模块、selector、scalar-root、HJB、KFE、SciPy求解、model driver、pytest、MATLAB、宏观迭代、IRF、Newton、V008/V009辅助实验。不重播scientific run，不生成新的政策/Q/V0数值，不重新计算任何经济体。不得修改fixture、参数、网格、现有代码、已有失败回执或冻结合同，不能借新输出目录重置旧账。
不使用Git checkout/fetch/merge/stash/reset/clean/commit/push，不修改原`D:\ProjectTemp\c5k1bturn56`及其8 dirty/index/外部common-dir/untracked/ignored，不访问真实C8/2017/2018/B3、V009失败数组及其它项目。
**允许**使用本地文件读取工具或标准库的纯JSON解析、字符串统计、SHA-256和文件元信息；这些不得间接import模型模块或执行其函数。局部代码查看只可读本候选中下述精确源码的已存在副本，用于字段解释，不作运行。

## 2. 只读定位与阅读界限
本轮本地获准工作根：
`D:\ProjectTemp\ch5_v010_mainline_impl_20261015_01`。

先只读该根的`DELIVERY_RECEIPT.json`；必须对照用户回报的SHA-256：
`322D707CF666D5CEDF1E4B907F7FE75A5423734867BA717D28CCB6DD73A792C9`。
若不匹配就`STOP_RECEIPT_IDENTITY_MISMATCH`。

优先从该回执、前一轮科学输出目录的显式记录确定**首个**科学run的精确output路径。允许精确读取同次run现存的：
1. `first_failed_cell.json`（checkpoint=2、F-order flat index=25）；
2. `attempt_summary.json`；
3. `V0_before_HJB.json`；
4. `input.json`；
5. `ledger.json`；
6. 必要时同一run前两个`update_000.json`、`update_001.json`；
7. `DELIVERY_RECEIPT.json`中的本次源哈希与最终候选信息。
8. 如有必要，仅只读候选`src/ch5_two_asset_hank/multi_province/mainline_household_runtime.py`、`src/ch5_two_asset_hank/corrected_diagnostic/selector.py`与同轮科学输入收据明确列出的源文件哈希。

**查找保护**：不遍历完整repository/reports/.git或扫描其它D盘目录，不打开任何`.mat/.npz`或真实C8/B3文件；从`DELIVERY_RECEIPT`定位失败run目录。若没有明确路径，仅可对已知run输出根进行至多两层、至多20个**目录名**的定位；仍找不到就`STOP_OUTPUT_PATH_UNKNOWN`，不可用全盘recursive glob补救。

总计只读对象≤12份、累计读取≤8MiB、墙钟≤30分钟。仅在独立新目录`D:\ProjectTemp\ch5_v010_failcell_extract_20261015_01`写至多2份脱敏MD/JSON摘要，总写入≤256KiB；保持所有原始回执原字节和时间不变，任何创建目录失败不借原模型树写入替代。若原始内容包含不可公开信息，仅报告可核哈希、统计和脱敏相对路径，不复制原始证据全文。

## 3. 必交取证数据：只转写真实字段
A. **原始身份**：每个实际读取JSON的相对路径、bytes、SHA-256、解析成功与否；`DELIVERY_RECEIPT`确切身份；源科学attempt中`input.json`列出的Python/NumPy/SciPy版本、fixture Git blob、V0 SHA和实际加载的数学/适配器源码哈希；单列最终候选源码哈希是否**逐项一致**，无法核对就`UNKNOWN`而非猜测。

B. **失败细胞**：原记录的checkpoint、flat、(b-index,a-index,z-index)、实际`b/a/z`、`v_b_backward/v_b_forward/v_a_backward/v_a_forward`等导数（依据真实字段命名）、工资和税后工资、`r_b/r_a`、转移及其上下界；缺失字段直接标`NOT_IN_RECEIPT`。按F-order固定20×20×2推算的理论坐标仅作旁证，不可覆盖原cell数值。

C. **所有候选拒绝原因**：从`result.candidates`读取candidate总数、admissible数、每类`reasons`或原名字段出现的精确频次；按active-set、`positive/zero_kink/negative`转移 regime、资产导数branch分组，枚举`INTERIOR_A_SWITCHING`、`INTERIOR_Z`及joint switching是否存在、root尝试和拒绝判据；最多5个具代表性的rejected candidate的ID、原始reason、关键residual/容差数值。**不要把NO_ADMISSIBLE_POLICY重新概括为NO_UNIQUE_ADMISSIBLE_POLICY**。对于真实JSON中没有的字段，一律写`UNKNOWN/NOT_IN_RECEIPT`，不自己求解生成。

D. **当时账**：与现有`attempt_summary`/`ledger`对齐checkpoint0/1的B/D、checkpoint2的停止、直接更新=2、KFE=0；核科学单轮已耗1/26 HA、1/4 driver、1626 selector cells、1642 roots（V0=800）是否被本地原证支持。先前Codex报告focused pytest已耗4/6，既不重跑也不补新测试。

E. **有约束的分类建议**：将可能问题分为`ADAPTER_INPUT_OR_MAPPING`、`FROZEN_V0_OR_PARAMETERS`、`ACCEPTED_SELECTOR_DOMAIN`、`FLOAT_PRECISION_OR_NUMERIC`或`INSUFFICIENT_EVIDENCE`；只有被现有字段直接支持才判主因。给出后续修复必须检视的**精确函数/行段及最小证据需求**；不是新科研算法设计、不自动改变已采纳门禁/固定输入，不自行授权再次HA。

## 4. 停止条件与交付
任一原路径/receipt身份缺失、读取超限、保护风险或无结构可用，保留失败分类并STOP，绝不补跑计算。完成只读后提交**唯一**`V010_FIRST_HA_FAILED_CELL_SOURCE_ONLY_EVIDENCE`报告；既有回执的原SHA和可用证据优先于结论。最终状态：
`WAIT_ASTRA_V010_FIRST_HA_FAILURE_REASON_REVIEW / STOP`。

**全项目安全状态继续**：A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE；真实C8 A–D REQUEST_ONLY；旧8 dirty保护；V011 NOT_STARTED。本任务不改变原冻结plan、历史Git提交、剩余/已耗科学预算。
