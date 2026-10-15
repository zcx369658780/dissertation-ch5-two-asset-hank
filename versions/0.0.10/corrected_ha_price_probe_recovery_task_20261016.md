# V0.0.10 ACTIVE：UTF-8/日志守门修复后仅1次corrected HA科学恢复

**唯一任务ID**：`V010_CORRECTED_HA_UTF8_LOG_GUARD_ONE_SHOT_RECOVERY`。
**当前授权**：Owner于2026-10-16明确批准一次性执行器修复、**新增1个Python进程并最多1次单省synthetic HA**，且同意适度提高储存上限。Astra已正式冻结新的限域恢复合同。此任务属于**原V010内同一数值点**；不修改原V010、原probe、历史超额/停止记录，不启动V011。

## 0. 先核固定身份，错一项即STOP

仓库`zcx369658780/dissertation-ch5-two-asset-hank`，治理分支`migration/astra-workflow-20261012`（仅导航/本task签发）。
1. 新恢复冻结合同 `versions/0.0.10/corrected_ha_price_probe_recovery_freeze_20261016.md` @ 固定commit `9aca1018c77d19e9489f2baf59c02bc654923999`、tree `4a04fd536b1cd4dd82b07dbdc23b5d73d1c8f6cc`、blob `95843d1ec838f52b056a8ca768d3f4cc55022b6f`。**此冻结文件是完整权限和硬资源的authority**，本任务不能修改它。
2. 原单点科学合同：`versions/0.0.10/corrected_ha_price_probe_freeze_20261015.md` @ commit `81181490495f827aa0e15e6a6efb186e8addee67`、blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`。原完整input `versions/0.0.10/corrected_ha_price_probe_v1.json` @同commit/blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。输入必须从**此原blob完整读取**，不能更换`ra`、网格、税含义、借款利差或V0。
3. 唯一允许的Python科研源：commit `94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，以及恢复冻结合同列出的9个必需source Git blob。
4. 原V010 plan @ `bf091da33d59293f147d52c11580327d3ac2a85d` / blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原两省synthetic fixture blob `40915658d93403cfc21b33a6b864b332b7857749` 均严格不变；此前[预检失败独立审议](corrected_ha_price_probe_preflight_review_20261016.md) blob `d87d29173e8c22a38df3e8bdb636a8b80c50ccda`也不追改。

此前失败`V010_CORRECTED_HA_SINGLE_PRICE_POINT_ONE_ATTEMPT`于1/1 Python进程里发生GBK解码及43,519,638 B日志，对旧32MiB硬上限超9,965,206 B；该进程1/1已用、实际HA=0。将它与本轮新账**永久并列记录**，不能描述为重算前一次成功、超额豁免或原额度回滚。

## 1. 唯一任务执行内容：先修私有runner，再做一个单点尝试

### A. Python启动前的非科学静态门
只在全新`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_recovery_20261016_01`目录（不存在先报冲突；无覆盖）准备一个短私有runner；只能修改这个**runner/IO证据wrapper**，不得改Git跟踪科研源、corrected数学组件、原输出目录、任何先前固定manifest或经济参数。

**静态审阅无需启动Python**：检查每个文本`open`、`Path.read_text`、`.decode()`是否显式`encoding='utf-8'`或strict UTF-8；原始文件哈希通过`read_bytes`而非`repr(bytes)`；错误处理不能记录错误`args/object`原始字节、全量traceback、原始数组、source正文。遇到`UnicodeDecodeError`仅保留`type,encoding,start,end,reason`与输入`bytes,sha256`；其它错误仅类型、预设短原因码/≤4096字符已净化消息，非原始bytes。禁止直接`print(bytes)`、无限stderr/stdout。

**写前限额审查**：确保runner输出、model `seal_json`回执及stdout/stderr都受预先核定的UTF-8**字节数**守门；可仅在runner内插入**receipt-only、行为等价的I/O包装**，不改数学模块的Git源码或任何selector/HJB/KFE方程。须记录原输出writer和包装器SHA；JSON先编码、核不存在/容量/路径，再排他创建并一次写入，绝不写后清理超额。后续写入超过总额前需`STOP_BEFORE_ARTIFACT_CAP`，余量不足保留终态预留；若无法保证所有写入处受控，**不允许启动唯一Python进程**。

将shell输出也纳入guard；只记录简要回执，不直接导出原始`repr(raw_bytes)`/大数组。预启动仅PowerShell/Git文本及哈希检查，**不运行任何`python`/`py`/Jupyter/pytest/MATLAB/selector**。如果runner静态内容或安全隔离不合格，Codex可在**首次Python启动之前**对新runner进行必要普通修订并重新静态检查，但不得更改输入/模型源码或扩大时间/存储上限。

### B. 仅一个新的Python进程
全局新进程 `≤1/1`，调用前先持久记录并扣除（预检失败也消耗）。启动显式`python -B -X utf8`及`PYTHONDONTWRITEBYTECODE=1`, `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`；禁止pip/替换依赖/第二进程。程序内部全部自有文本读取仍显式UTF-8；在**该同一Python进程内、HA首次调用前**验证9个源码Git blob、candidate HEAD/tree、实际`__file__`、NumPy/SciPy/Python、原manifest字节Git blob及完整字段，一不匹配就process 1/1、HA0 STOP。

原manifest中唯一输入`rah=.0675,w_eff=15.5,rb=.02,transfer=.1,rb_gap=.07`，其余`parameters/grid_spec`完全原值`b=[-2,5],a=[0,10],shape=[20,20,2],F`。先哈希完整输入，再且仅在预检全部PASS后调用`HAInputs`与`solve_conditioned_household`一次；**实际V0由该唯一HA内部新算并在首次HJB前存哈希**，不提前调用V0生成器造成第二次科学计算。科学调用前记`new_HA_attempts=1/1`；调用失败也计入，不retry、不warm-start，不借历史已完成的HJB或KFE。

科学数学门沿用旧science freeze（B≤1e−8、D≤1e−7、source-free KFE唯一闭类及质量、原selector/KKT/边界/单调性/原较低budget）。单HA至多100 HJB value updates、101 policy/Q maps、80,800 selector cells、400,000 scalar-root（含V0）、100 sparse direct solves、≤1 terminal KFE；不准更换源码、数值方程、税定义或价格区间救PASS。

### C. 本轮加高的存储硬限额
- **新输出总≤96MiB = 100,663,296 B**，覆盖新runner、JSON、输出、缓存、trace/日志、stdout/stderr、临时文件、报表；提前留2MiB写最终STOP记录；单model JSON≤16MiB、单runner JSON≤4MiB、stdout+stderr总≤4MiB、异常摘要≤4096字节。写入前检查UTF-8实际bytes、全路径、当前总增量；遇上限主动拒绝，不能通过打印原始失败bytes形成又一大文件。
- 如果现有独立V010实现clone已验证固定SHA及blob且能只读使用，则不新增clone；否则只允许在本恢复根中全新不共享旧Git common-dir的clone，总clone≤2GiB=2,147,483,648 B。两个budget分账，不得以clone分类规避输出限额。
- 本轮准备+预检+唯一Python运行+报告墙钟总≤7200秒。RSS目标512MiB采样，未知标UNKNOWN。旧失败run中**43,519,638B及超额9,965,206B仍为历史事实、不可计入此次96MiB但必须交付引用**。
- 不得执行`validators/multi_province/v010_mainline_validation.py`，它有两省外层/多次HA调用；不做pytest、31省/2省外层、IRF或真实数据读取。仅单省条件HA价格点，不是同一历史经济体、真实GE或论文Results。

## 2. 保护与一次集中报告
禁止触碰`D:\ProjectTemp\c5k1bturn56`（8 dirty/index/external common-dir/untracked/ignored）与所有旧独立失败目录、原V010报表/初始fixture；旧日志只读，不复制/打印raw bytes至GitHub。禁止模型tracked源码更改、checkout/merge/push、GitHub证据发布、MATLAB、Newton、C8/2017/2018/B3/V009失败数组、其它项目。固定source clone只读（含禁止`__pycache__`写入）。

新故障若在启动前、Python预检时、HJB selector/根/KFE时、容量guard时发生，按阶段精确标`STOP`，**不得第二个Python进程或第二次HA**。保留原失败及新尝试调用账，不夸大科学结果。

最终只交`V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT`：报告(1)freeze/task/manifest/source SHA与实际源和版本；(2)原GBK/超额已保留，**旧Python1/1 HA0**和旧V010科学账并列；(3)本次**Python 0或1/1、HA 0或1/1**、roots/selector/HJB/KFE准确信息；(4)**本轮正确上限=96MiB**及clone的实际字节、日志守门检查、UTC/time/RSS与所有未确认；(5)是否达到严格corrected单点HA资格，绝不能宣称GE/Results；(6)保护证据等级`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`直到Astra可独立核。任何终态：`WAIT_ASTRA_V010_CORRECTED_HA_RECOVERY_REVIEW / STOP`。

旧A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY、V011 NOT_STARTED一律不变。
