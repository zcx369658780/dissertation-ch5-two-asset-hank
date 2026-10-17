# V010 M1 原长任务终态独立审议：B0 工程限域接受，B1 CP2_F25 科学 FAIL_CLOSED

**2026-10-17（北京时间）｜正式 E2/E3 集中原证审议；不新发任务、不重置预算。**

**总裁决：`V010_M1_LONG_RESULT__B0_ENGINEERING_LIMITED_ACCEPT__B1_CP2_F25_SCIENCE_FAIL_CLOSED__TASK_STOPPED`。**

**证据边界：**这是对 Owner 在 ChatGPT 私有对话上传的 **实际 ZIP/MD/JSON 字节、机器日志、二进制调用 journal、源代码及 GitHub 冻结合同的独立静态取证/交叉核验**，**不是审稿人重新在 Windows 运行科学 solver 或独立鉴证OS沙箱**。可以独立接受这一失败事件的证据、位置、停止次序与账本的一致性；不能据此宣称 HJB/KFE/稳态、现实31省GE、IRF或博士第五章 Results 科学 PASS。

## 1. Authority、任务身份与本轮验收输入

- 唯一冻结任务：`V010_M1_EVIDENCE_AND_CONDITIONAL_SYNTHETIC_MAINLINE_LONG_TASK`，发行Commit `54454066859692a0f481cfa44de8df8dc298ce03`、固定Blob `5d87753b4a3ac972f37f1ac59722b464efd11bd9`。Stage A及2026-10-17 A4原限域签署 [独立主审](v010_m1_stage_a_a4_scoped_adapter_precondition_primary_review_20261017.md) Commit `7f706aa4915eacf7573b5e5e42cb02058e44552b`、Blob `859c1341bbf02a9c079d630f0398b3105d523019`；该A4当时**只授B0先行的条件科学门**，不保证B1数值资格。
- 原科学Plan Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；原冻结模型 Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`。匿名fixture `40915658d93403cfc21b33a6b864b332b7857749`；不触真实中国资料。前述权威 GitHub 身份在本次审议前读回。
- Owner实际上传 `CH5_V010_M1_LONG_RESULT_20261017.zip` **1,877,576B**，独立SHA256 `D76207C452496737D4A9DCA159A197826E9053A7298383AD003A6BEB30AD2E8B`；`V010_M1_EVIDENCE_SYNTHETIC_MAINLINE_LONG_RESULT.md` SHA256 `0CC9C7EA5B9FA36FEDFA46FD3B0D43726B58CA04159D466B1E4864010C11AF80`；独立上传 `DELIVERY_RECEIPT_V010_LONG.json` SHA256 `D627E7972EF9DB99AF100DE7E0A9FCE9EA377C14A1FD609640AA80AD0D3EC51F`（本回执包含 ZIP/MD/manifest 字节摘要）。MD与ZIP内同名成员**原字节一致**。
- ZIP 426个文件成员，含425件被索引内容＋ `LONG_RESULT_PACKAGE_MANIFEST.json`（88,329B，SHA256 `59769162F6C3E68EA8CD8539E6B10C0040D8D98E52981E9175BDCAE3705D9A18`）。ZIP CRC通过；425/425逐条原始字节长度/SHA256全部吻合manifest，无丢项、重复、越界路径。九旧M1原件原封随Stage A嵌套ZIP继续保留（65,737B，SHA256 `8961AD01642992CF397BBD2DB165D62AB5AD4B44A9990DDEC1D4000C96C819CA`），不重建历史缺失的Windows原始日志。
- 固定双省 `fixture_RAW.json` **2,948B**，SHA256 `BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252`；按Git `blob <bytes>\0<raw>` 独立复算的blob为 `40915658d93403cfc21b33a6b864b332b7857749`，与执行视图的fixture两份逐字节一致。

## 2. Stage A和B0工程证据：限域接受

1. Stage A曾报告非求解22/22；本次ZIP确实新增其focused首次失败、修订与最终尝试的原始JSON及执行脚本，可核对第三次 `22/22` 的**本机执行记录**。仍不冒称Astra重跑过Windows测试；保留第一次AST期望失败19/20及修复经过。
2. `B0_FINAL2_RESULT.json`（SHA256 `48317A33847D4B53F2EFCAD6B0333DC41567D9B199BC73AB71B550C26894B80A`）实际记录7项成功、0失败、0错误，且HA/HJB/KFE/selector/root=0。B0测试包括**人工数组**完整V/概率质量 little-endian float64 F-order身份、变更敏感性、工程单写者持久账重启与失败扣费、Z-root局部门、冻结fixture与原数学守门、非求解工资/劳动/财政stub。注意：人工V/p验证不等于取得两个真实HA终态数组；B1失败后，真实 `fullTerminalVPComparison=NOT_REACHED`。
3. ZIP `FROZEN_MODEL_INDEX.json` 索引中的76条冻源/测试/fixture/validator，实际包内 `frozen_model/` 逐字节76/76匹配自身索引；`final_view_v2/` 恰两条白名单相异：`src/ch5_two_asset_hank/multi_province/mainline_household_runtime.py`及`validators/multi_province/v010_mainline_validation.py`。两条差异属于终端V/p哈希与跨driver累计审计/运行接线；基于冻结的76文件本地隔离副本实际应用 `B0_TWO_PATH_PORTABLE.patch`，生成两文件与最终视图**字节完全相等**（patch SHA256 `B89161B09445B53E4541C070578D64FC6EB39AB341E9C1BEA20A9C7093E5C76B`）。HJB/V0/KFE核心函数静态AST、双门与Delta及原 `corrected_diagnostic/` 等源保留。**本地执行视图 commit `bb5eae2dfb84c9d73b6644f97148eb244b4cf4fa` / tree `6243e58b7acc36f868f057022267a6b78428ea92` 仅是 `LOCAL_EXECUTION_VIEW_ONLY`，并非完整或已推送的模型仓候选，不能据此解除Git/模型候选资格。**
4. `SCOPED_ADAPTER_ONLY`及本次 `SCIENCE_MODULES_01.json` 的44条实际 `EXECUTED` 记录与已上传模块原字节匹配；无原生无适配导入资格，不代表Windows OS-native sandbox独立PASS。旧 `FULL_RUNNER_IO_CLOSURE=BLOCKED` 不因本次受界工程运行变成全历史PASS。

**B0审议分类：`B0_NON_SOLVER_ENGINEERING_LIMITED_ACCEPT_WITH_UPLOADED_RECEIPTS`；不等于全科学资格。**

## 3. B1 第一真实HA失败位置与算法资格

- 第一 driver（已计费，child seq27）因Windows命令参数列表拆分导致解释器把目录当入口，exit=1，**脚本未启动、HA=0**；出错stderr字节已上传。修正后第二 driver（seq28）真实启动、Job/双PIPE读取及进程reap报告正常，exit=2，耗时8.0715964秒；资源较小，但不得凭exit=2断定底层全部安全。两次均入总 `scienceDrivers=2/4`。首次失败记录继续保留，不改造成成功或免预算。
- 第二 driver用冻结fixture的 `SYN_A`，`rb=.02,rah=.055,w_eff=1.7085897434929322,Tt=.1,rb_gap=.07`；没有替换为Owner额外给定的 `rah=.0675,w_eff=15.5` 单点。原输入SHA256 `C001B9506E8AD94CF9D1F47264301964E281191C4DDA22434E8AF37296D6AB45`。V0先封存SHA256 `4D4042BB927FC78BB631D59DB4D3EEDB0A0664547435706A9BE403422340D3B3`，FOC相对误差2.1871393585115584e-12、最小liquid b斜率0.06410621585514509。
- 已完成CP0/CP1两个策略映射及2次直接value更新：Bellman B=2.3410249912350563、0.2328433126744121；CP1 value D=3.290243356756511；后向相对误差2.658994752749849e-16、1.5159350570911279e-16；两个Q行和误差7.105427357601002e-15、3.552713678800501e-15，`alpha=1`无halving。**B和D当时均远未达到HJB双门，不能称HJB合格或KFE有资格。**
- 在CP2的F-order flat=25（零基），格点 `b=-0.1578947368421053,a=0.5263157894736842,z=.8`；`first_failed_cell.json`（22,390B、SHA256 `E01A5E5137424C238F8090903D21970910A2CC1562103FC2C78FB16E0487CEC3`）真实记录 `NO_ADMISSIBLE_POLICY`、12个枚举candidate的`admissible=false`、`selected=null`、`admissible_comparison_count=0`。原candidate拒因由本审议直接读取：B/A导数方向与实际漂移不一致、资产转换正负符号及KKT残差。若干残差远高于当前局部浮点容差，**不能因solver根求不出就不加分析地归为数值精度舍入**。
- CP2只处理26/800格点后停止；没有完整Q、Bellman B/D、HJB terminal资格、source-free KFE。第二个同输入HA和B2两省outer、B3冻结GovInv/Zt后GDP误差≤1%校验、B4三期原lagged-NKPC短动态全部`NOT_RUN`。运行stderr记录过3条selector乘法overflow RuntimeWarning，其与该格点最终不可接纳的因果关联**未验证**，不能凭warning定根因。

**科学裁决：`B1_FIRST_CONDITIONED_HA_FAIL_CLOSED__CP2_F25_NO_ADMISSIBLE_POLICY_EVIDENCE_ACCEPTED`。不宣布整个模型无解、不宣布某种selector修正已采纳，不准修改方程、边界、网格或阈值谋求PASS。**

## 4. 持久二进制科学账、进程与资源独立审议

- ZIP `science_ledger/events.bin` 长52,416B，独立SHA256 `C3DA9FCC247750981A5DAC88DF35D8B64FB7DFA4540D74B1191CA23481B7AF18`；16B×3276条。按上传候选源码的 `<IBBHI + CRC32` 事件格式，实际逐条验出**3276/3276序号连续且CRC32正确**；sha与 `science_ledger/current.json` 的序号/前缀哈希一致。事件类型计数：`HA_BEGIN=1`、`ROOT=1642`、`SELECTOR_CELL=1626`、`POLICY_MAP=3`、`HJB_VALUE_UPDATE=2`、`HA_FINISH_FAILURE=1`、`KFE=0`、`HA_SUCCESS=0`。前800次root属于V0，之后842次selector；policy maps处理格点800、800、26，吻合最早失败CP2_F25。仅一个ordinal=2的driver journal事件——第一driver未进入Python脚本，故其计数来自**单独上传的child seq27进程及supervisor receipt**；绝不伪称journal自身包含两次driver启动事件。
- 上传 `LEDGER.json` 含28个逐child回执，其 `process_logs/1..28.(stdout|stderr)` 共56份原记录 **56/56 SHA256一致**。55份 retained bytes=read bytes；seq9出现被截流进程**额外读取1B作为配额探测**（read=1,044,481B，retained=1,044,480B，stdoutSHA与保留文件一致）；该record的统一 `timedOut=true` 标记不可视为真实达到墙钟超时。与既往GBK输出超额事件分账，不追溯赦免任何历史失败。
- Stage A工程Python4/16、活动时间816.4729557秒；Stage B focused4/6、science drivers2/4、真实HA1/26；HJB2 updates、selector cells1626、roots1642、KFE0。Stage B报告用时991.4435925秒/8小时；样本peak RSS 80,859,136B，首个短driver RSS为UNKNOWN；报告的非Git产物、Git原流量各在本轮相应限额内。以上**累计资源账在所上传原证与summary之间静态一致**，Windows全物理文件访问/保护根没有由审稿人OS级独立复核。
- `SCIENCE_LEDGER=SCIENCE_FAIL_CLOSED`，剩余所有预算因任务STOP永久关闭。**不得再发第二个同输入HA、不能同task继续B2或把剩余额度转入新任务**。

## 5. 长期UNKNOWN、Owner权限及下一门

`UPLOADED_RAW_BYTES_SHA_VERIFIED`：本次425个文件的实际上传字节、旧九件及二进制journal可验证；`GITHUB_REMOTE_VERIFIED`：科学合同/冻结任务/A4签署身份、**本轮新代码尚未上传GitHub**；`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`：Windows受信任主机过程/Job/文件锁/防重解析/保护根无写入及测试执行事实；`INDEPENDENT_SCIENTIFIC_ACCEPTED=FALSE`：没有任何成功的HA/KFE/稳态/动态或现实论文结果。承认静态机器取证原件支持真实失败，但它不是独立Windows solver重跑。

历史 `FULL_RUNNER_IO_CLOSURE=BLOCKED`、native import未接受、early Git prelaunch缺失、原20个Git children逐事件底层完整原证缺失、N13历史错误原件和派生修正区别、旧B/S/L first/run_id缺失、早期PID/旧dummy overflow UNKNOWN均持续。C盘物理独立SSD备份、原D盘8 dirty/index/staged/untracked/ignored/外Git common-dir、历史失败原证以及真实C8/2017/2018/B3/V009资产不授权改动。保留A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 REQUEST_ONLY。

**正式终态：** `ACTIVE_TASK=NONE`；`V010_M1_EVIDENCE_AND_CONDITIONAL_SYNTHETIC_MAINLINE_LONG_TASK=DELIVERED__STOPPED__SCIENCE_FAIL_CLOSED`；`NEXT=WAIT_OWNER_DECISION / STOP`；`model_activation=False`、`REAL_GE=False`、`Results FALSE`、`V011 NOT_STARTED`。未来如Owner决定推进，应另行明确冻结**一张有边界的V010主要数值机制调查/修正长任务**，优先CP2_F25的导数方向/零漂移/转换KKT源法则静态对照、再决定是否需要新科学预算，不恢复逐异常微任务审批。**本审议本身不签发该任务，也不转移旧预算。**

## 6. GitHub发布与临时清理

本轮原始425件ZIP采用Owner私有上传，Codex GitHub push=0，无针对本轮新增的远端`_review_tmp`候选；故**不执行任何远端临时路径删除**。本次只发布本脱敏、数字与哈希级永久主审及动态状态，不发布原始私有文件或完整日志。此前 Import Guard temp清理已归档且不属于本轮；GitHub临时交换与验收后清理制度继续适用于未来当次任务明确允许的脱敏review发布，非后台自动监控。
