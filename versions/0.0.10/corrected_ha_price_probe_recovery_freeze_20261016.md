# V0.0.10 单点corrected HA：一次性UTF-8预检/日志保护恢复科学许可冻结合同

日期：2026-10-16（Asia/Shanghai）。
**冻结分类**：`CH5_V010_SINGLE_POINT_RECOVERY_EXECUTION_FREEZE_V1`。
**Owner明确批准**：为2026-10-15单点probe的GBK预检失败和日志失控，前瞻性新增**至多1个Python进程及至多1次条件HA尝试**；可适度提高新存储预算。本合同将新运行artifact上限从32MiB调整为**96MiB=100,663,296B**，单独clone上限从1GiB调整为**2GiB=2,147,483,648B**。这仅适用于全新隔离恢复任务，不追溯豁免、重置或擦除原任务已记录的`43,519,638B`及`9,965,206B`超额。不可由后续动态分支偷偷替换本固定合同。

## 0. 前提和始终不变的科学对象

- 旧单点任务（已STOP）固定发布commit `21c736d4163a12978486c3b8256f4db8b9bd6c76`、tree `a66a8c07e21c8ce9bdbeff1a5f801e7d376256e3`、blob `270f61b6d5e21a6afa7de1bf05aa3dabade4175d`。其旧许可为science Python process **1/1已耗**、HA **0**、32MiB storage **已突破**。永不把旧进程/超限改为0或“可复用”。原runner_result.json报告SHA-256 `E7CE0C4EE35D8858A96710FF58FCA3E1EDC1493E8CEF1D5D952F3BC301C780CB`（仅Codex本机回执，Astra未直接核原字节）。原超额目录及原始证据**保留只读、不可覆写、移动、清理、公开原raw bytes**。
- 2026-10-16原失败审议：`versions/0.0.10/corrected_ha_price_probe_preflight_review_20261016.md`，Git blob `d87d29173e8c22a38df3e8bdb636a8b80c50ccda`。它是故障/超额历史，不因后来恢复成功而覆盖。
- **科研模型代码**唯一本：`94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。此为有限接受工程候选，非已通过科学HA或GE。
- **单点原科研freeze不追改**：`versions/0.0.10/corrected_ha_price_probe_freeze_20261015.md` @ commit `81181490495f827aa0e15e6a6efb186e8addee67`, tree `846fd3f354d8f9d5d4978e15ad9ff78b71d2e451`, blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`；**完整科学输入不追改**：同固定commit中的`versions/0.0.10/corrected_ha_price_probe_v1.json`，blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。
- 固定单省科学输入只从manifest的`ha_inputs`原字段读取：`rah=0.0675`、`w_eff=15.5`（已净工资，不能再扣税）、`rb=0.02`、`transfer=0.1`、`rb_gap=0.07`及同原`parameters/grid_spec`（b∈[-2,5]、a∈[0,10]、20×20×2、F-order b-fast、z=[0.8,1.3]、Delta=1000）。V0仍由既有源码从当前冻结价格确定性新建，不可warm start、缓存替代或改变任何固定数值。
- 原V010长期实施合同 `versions/0.0.10/plan.md` @ commit `bf091da33d59293f147d52c11580327d3ac2a85d`、blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，原两省fixture blob `40915658d93403cfc21b33a6b864b332b7857749` 不变。新单省点绝非31省或两省GE。

## 1. 一次性新增许可、不可跨用预算

本恢复是**前瞻性新增且独立账册**：`RECOVERY_PROCESS_NEW=1`、`RECOVERY_HA_NEW≤1`；一个Python进程既承担完整预检，又（仅全部预检通过后）调用**一次**`HAInputs`与`solve_conditioned_household`。在Python进程首次启动时就扣掉`1/1`，即使UTF-8/哈希/路径等仍失败也不得重启；只有真正调用HA入口前才计`HA_attempt`，失败亦计数。

- Python进程≤1；pytest进程=0，额外Python/`python -c`/`py -m`/Jupyter=0，MATLAB/宏观外层/IRF/真实C8/B3/旧失败数据调用=0。
- 在1次HA内部：value updates≤100；policy/Q maps≤101；selector cell evaluations≤80,800；scalar-root（含V0初猜800状态）≤400,000；direct sparse value solves≤100；**source-free terminal KFE≤1且仅严格同checkpoint B≤1e−8、D≤1e−7与Q全部合法时允许**；global monotonicity halving k=0..52；direct normwise backward error≤1e−12；原selector分支较紧门保持。
- 总墙钟≤2小时（从首个本任务准备性写入或科学预检开始计，包括静态检查、唯一Python进程和报告），达限立即STOP，不能重新开时钟或第二进程。
- **新独立输出artifact硬上限96MiB=100,663,296B**，覆盖新runner、临时/最终JSON、stdout/stderr、log、Python缓存、回执和候选私有报告在新恢复根下产生的全部增量。为失败终态预留2MiB，科学过程中其余写入不得耗尽预留；个别模型回执JSON≤16MiB，单个runner摘要JSON≤4MiB，stdout和stderr合计≤4MiB，独立异常摘要≤4KiB，均须**编码成UTF-8后计算字节、写入前守门**。写入前预估总文件大小，超出即`STOP_BEFORE_ARTIFACT_CAP`，禁止写完后删除/换名挪账。若某个不可控第三方写入源不受守门覆盖，预检须STOP，不能假装全局配额可保证。
- **只有必要新增的独立不共享Git common-dir clone预算≤2GiB=2,147,483,648B**（与96MiB运行产物独立计数，clone自身建立的脚本/日志不能不计）。优先现有`D:\ProjectTemp\ch5_v010_mainline_impl_20261015_01`隔离clone**只读**作为固定源码；它若非精确candidate commit/tree/逐文件hash即STOP或在新恢复路径安全clone，绝不借原受保护历史工作树。新clone不允许下载/复制整个旧`reports/`/C8数组。
- RSS采样目标512MiB（非硬否决的资源观察；可得则报峰值，缺失标UNKNOWN，真实资源失控即停止），时间/字节/调用数全部按原始单调累计核算。旧输出43,519,638B不并入新任务96MiB硬额，但必须并列显示且仍标`OLD_BREACH_UNRESOLVED_AS_HISTORICAL_FACT`，不得因此声称旧错误消失。

## 2. 必须先完成的执行器预检/日志保护

**允许改变的仅是新隔离目录里的临时runner/IO evidence wrapper**，不编辑、patch源文件内容、不提交模型代码、不修改`corrected_diagnostic/`、宏观源码、参数、grid、科学selector、solver、KFE数学或任何既有回执。新恢复输出唯一目录：
`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_recovery_20261016_01`。
原失败目录：
`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_20261015_01`
**绝对不可写/移动/覆盖**。

**预启动静态检查（不得启动Python）**：
1. 通过PowerShell/文本工具在独立新路径检查runner所有`read_text`、`open`文本模式、`read_bytes().decode`，逐个明确`encoding="utf-8"`，或UTF-8严格decode；拒绝系统默认GBK。文件原始hash从`read_bytes`独立计算，不通过`str(bytes)`。
2. runner异常处理不能`repr(raw_bytes)`、`str(raw_bytes)`、对bytes展开、打印大型数组/原始JSON或无限traceback。针对`UnicodeDecodeError`只记录类型、encoding/start/end/reason、输入文件的bytes/hash；其它错误类型+短、经脱敏限制的摘要，**绝不将异常`.object`、`.args`和source bytes写入日志**。
3. 预定义**写前**容量guard和每日志截断：科学源码的`seal_json(path,payload)`可以在runner中建立**仅IO层、行为等价**的受界包装（在内存中替换receipt-writer引用需审计/记录原source SHA、wrapper SHA）；不得改变`HAInputs/construct_v0/select_constrained_policy/Q/solver/terminal_kfe`等任何数学逻辑与参数。guard应先确定UTF-8 JSON实际大小、检查文件不存在、验证总余额与单文件上限，再原子写入；失败不得产生部分超限文件。模型其他写入函数同样需要被隔离或明确 fail-close，不能依靠运行后扫描代替写前控制。
4. 禁止runner import旧`validators/multi_province/v010_mainline_validation.py`作为运行入口；它会执行两省外层/额外试验。只从固定候选Python package导入单省HA入口。Python以`-B -X utf8`或等价环境启动，且`PYTHONDONTWRITEBYTECODE=1`, `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`，预防加载源目录产生pycache；**但即便启用UTF8模式，所有自己的文本读取也必须显式指定encoding**。
5. 在唯一Python进程的模型调用前，验证冻结合同/input blob/代码commit/tree/九个source Git blob与实际Python`__file__`全部匹配，绑定完整输入JSON和V0派生身份、记录Python/NumPy/SciPy版本及module provenance。导入本身不应执行求解；如预检失败必须报告0 HA、process1/1并STOP。

**运行顺序**：先做非Python纯文本审查与容量guard验证（不运行模型也不另外起Python进程）→唯一Python进程与九模块/manifest/runtime载入核验→预先封存本次input身份与call ledger→原`solve_conditioned_household`调用最多1次→保存严格HJB/KFE真实原证→单次脱敏摘要和STOP；不重试、不改数救PASS。

## 3. 独立验收与不可变保护

只许一次真实science进程。结果分类区分：
`ENV_PREFLIGHT_FAILED_WITH_PROCESS_EXHAUSTED`、`SCIENCE_STOP_FAIL_CLOSED`、`STRICT_CORRECTED_CONDITIONAL_HA_PASS`（只表示该单省净工资价格点和固定网格的corrected HA有效）以及`STORAGE_GUARD_STOP_BEFORE_WRITE`；结果不能跨化为REAL_GE/IRF或Results。

报告名：`V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT`，必须含原失败进程1/1及43,519,638B上限突破、旧未用HA0、旧V010 4/6 pytest、1/4 science、1/26 HA、1626 selector/1642 roots的**独立历史账**；新恢复进程0/1或1/1、实际HA0/1或1/1、各root/selector/update/KFE使用情况、新artifact/clone原始bytes、时间/资源、source sha/input sha、每个门控结果，及保护和未观察事项。若科学失败，保留首个cell真实拒绝原因及合法回执，不能靠近历史价格区就宣称通过。最终：`WAIT_ASTRA_V010_CORRECTED_HA_RECOVERY_REVIEW / STOP`。

原`D:\ProjectTemp\c5k1bturn56`及8项dirty、staged/index、external common-dir、untracked/ignored，原15文件candidate、旧科学数据/C8/2017/2018/B3/V009失败数组及其它项目均不可改写、清理或借用。**旧冻结文档/旧失败审议永不追改**。不进行`git checkout/reset/stash/clean/push/merge`于任何既有受保护仓；只许新隔离clone若必要。V011 NOT_STARTED、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY，全局安全门一项不变。

**此freeze尚未自动行使新的科学预算；只有后续单独签发的`recovery_task_20261016.md`准确引用本freeze固定commit/tree/blob并更新`TASK_CURRENT.md`，Codex才可执行。**
