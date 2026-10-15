# V010 单点corrected HA：首次预检失败及硬预算超限独立审议

更新：2026-10-16（Asia/Shanghai）。

**审议分类**：`ACCEPT_FAILURE_REPORT_ONLY__PREFLIGHT_BLOCKED_STOP__PROCESS_QUOTA_EXHAUSTED__ARTIFACT_CAP_BREACHED__NO_SCIENCE_RESULT`。
**任务状态**：`STOP_CLOSED_PENDING_OWNER_LIMITED_REAUTHORIZATION`。
**这不是HA不收敛、selector NO_ADMISSIBLE_POLICY或KFE失败**；科学阶段根本未进入。原V010工程候选的有限源码接受仍保留，不据此给经济稳态/Results资格。

## 1. GitHub独立核验的固定身份
- 唯一原任务`V010_CORRECTED_HA_SINGLE_PRICE_POINT_ONE_ATTEMPT`，签发commit `21c736d4163a12978486c3b8256f4db8b9bd6c76`、tree `a66a8c07e21c8ce9bdbeff1a5f801e7d376256e3`、task blob `270f61b6d5e21a6afa7de1bf05aa3dabade4175d`。
- 新单点科学freeze `81181490495f827aa0e15e6a6efb186e8addee67`、blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`；完整manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。
- 唯一源Python候选 `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；旧V010冻结plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f` 原样。
- 输入`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`以及固定20×20×2网格仅代表拟运行点；**尚无科学试验结果**。

## 2. Codex提交的本地执行事实与证据等级
以下均为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，而非Astra已直接读取Windows原件：
- 进程中`Path.read_text`等预检环节未显式UTF-8，系统GBK解码报错，**未完成九个源码与完整输入硬门**。不能把已经核对的少量Git对象自动扩展为运行时全链认证。
- 原本准许的Python science进程 **1/1已消耗**，但`HA/HJB/KFE/selector/scalar-root/pytest/macro/IRF=0`；此处`process_started=1`与`HA_invoked=0`两账必须永久分开。
- 因异常日志将原始bytes展开，新输出`43519638`字节，对合同`32MiB=33554432B`超出**`9965206`B**（上限之约`29.70%`）。这是已发生的**硬存储超限**，不因为后续停止、归档、删除或改变路径而消失。
- Codex报告立刻STOP、未重跑、未清理既有证据、未改冻结输入/候选源码/旧回执、原工作树无写、真实C8/B3访问0。**网页端没有独立证明这些本地保护或回执哈希**。
- 现有私有回执 `D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_20261015_01\runner_result.json`，用户提供SHA-256 `E7CE0C4EE35D8858A96710FF58FCA3E1EDC1493E8CEF1D5D952F3BC301C780CB`；尚未经Astra独立本机sha256复验，不能推断其体积或contents。
- 由于展开的原始bytes可能导致暴露内容，**不得把超额raw log直接推GitHub或复制进脱敏公开报告**；保留原本地只读证据，必要时仅取type/文件大小/hash/有限长度、无原始bytes的故障摘要。

## 3. 审议裁决
- **接受故障报告作为STOP的依据；拒绝执行合规PASS。** 单点科学结果为`UNTESTED__NO_HA_INVOCATION`，既不能认定价格点失败，也不能借旧MATLAB-faithful价格域给本corrected算法科学PASS。
- 之前HA首次synthetic失败、12个policy候选全拒绝的结论仍是独立的旧证据；它**不是**本次GBK预检故障的延续HJB结果。
- 原新单点任务的`science_process=1/1`及`storage_cap`硬超限已经终止了任务。虽然实际`HA=0`，这不表示在旧授权下还可免费再开一次Python；**没有新的science/pytest调用许可**。
- 2026-10-15的Owner单次授权只涵盖已消耗的那个独立进程，不得从对方曾经批准科研方向推断其同意新的进程或超额豁免。旧V010实施账另存：Codex报告4/6 pytest、1/4 science driver、1/26 HA、1626 selector cells、1642 roots。新单点任务的`HA=0`、`process=1`，二者不能冲销或混合。
- 科学freeze、manifest、code candidate、`CURRENT`历史版本、Owner GovInv 0.9/1.1与目的地工资税一次扣的已确定经济方程全部不改。V011不启动。

## 4. 如Owner将来批准精确补充许可，推荐的唯一修复方向（当前未授权）
同一V010下前瞻性**单独**签发一次受限环境/执行恢复，明示新增加`≤1`个Python进程和`≤1`次HA科学尝试，原`(.0675,15.5,.02)`全输入、数学方法、fixed code SHA不变；此补充**不是恢复或作废本轮process/存储违约**。

在执行前静态核查私有runner：所有文本读取显式`encoding='utf-8'`或先`read_bytes()`后安全decode，避免GBK系统默认；异常摘要只限异常类型与≤4096字符的截断描述，禁止将`repr(raw_bytes)`、大数组、原始文本导入日志；预估字节并逐写限制累计artifact≤32MiB，超限须阻止写入而非事后删除。唯一新Python调用仍先完成全部输入/九文件哈希/模块加载的preflight，再决定是否开始唯一HA；无法通过则fail-closed，不得第二次。新运行应在**新的**受控输出目录，原超额目录原样只读封存，不挪出原始账。新许可须给出精确费用/时间/停止路径/证据资格；不得用改fixture或放宽B/D/KFE/selector去救PASS。
**以上不是当前新任务**。本轮Owner尚未确认是否追加被超额损失的进程。不能越过Owner批准而执行。

## 5. 当前保护
`ACTIVE_CODEX_TASK=NONE`；`V010_PROBE_PREFLIGHT_BLOCKED__WAIT_OWNER_ADMIN_AND_SCIENCE_PROCESS_REAUTHORIZATION`。
A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY；旧8 dirty/index/common-dir/untracked/ignored与C8/B3不触。V011 NOT_STARTED。
