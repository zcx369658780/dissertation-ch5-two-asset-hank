# TEMP-V010 Matlab-faithful HA Blackbox：100轮非收敛独立审查

**日期：2026-10-18；终态：`TEMP_V010_100_ROUND_OWNER_STOP_NONCONVERGENCE__EVIDENCE_LIMITED_ACCEPT__NO_FORMAL_STEADY_STATE`。**
**作用域：临时探索实验；不是正式V010冻结合同改变、不是论文Results、不是2009年31省parity否决。**

## 1. 权威和原始来源

- 隔离实验分支 `experiment/ch5-temp-matlab-ha-blackbox-100plus-20261017`；冻结实验发行Commit `503b418f790d61049f3df9016a783dcecc793237`、任务Blob `0f7917d3f8b89e99c6cd1c9430bf364a02cc30b3`。历史已验证2009年31省MATLAB/Python稳态的源码Commit `216283cf4f1303afa60f1915e143a0b7303a9ffb`，独立黑箱 `exports/matlab_faithful_two_asset_ha.py` 的Git Blob `9e7dc9556a2b76811e78f89999abecc045886106`、SHA256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`。
- 固定V010匿名双省输入Git Blob `40915658d93403cfc21b33a6b864b332b7857749`，上传ZIP内`reference/fixture_RAW.json` SHA256 `BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252`。冻结V010原模型Commit `94de4501dec051b969bee9d852eba2d4591f30ef`只作为外层输入及经济方程静态身份，不授原修正selector新代码资格。
- 本次Owner直接在ChatGPT私人会话上传 `TEMP_V010_MATLAB_HA_BLACKBOX_100PLUS_EVIDENCE.zip`，6,352,227B，实际独立SHA256 `4CD602CC3589F404E176937B96D21E265EB036374BCA95D708E5DC246A394156`；及同名RESULT.md，6,007B，SHA256 `FB026DED8E8AE682EE96EA7BB2BB33D73FBF99ECE2C17A7A070B186D6A6930B3`。这两份私人原始交付文件不公开上GitHub。
- ZIP完整性CRC PASS，**总910个成员=909个manifest索引的原件/派生项 +1个`FINAL_EVIDENCE_MANIFEST.json`**；manifest SHA256 `29C7DE2C5982EEE5FDF7F431D6B32E357117D15EFA77D127B721F5D9471C5FD6`。实际逐项读取909/909，长度/SHA256匹配，索引无失踪、重名或额外未登记项。
- ZIP内昨晚 `prior_evidence/OWNER_PAUSE_EVIDENCE.zip` 原字节2,806,221B、SHA256 `D5562BB4E500FD8A38E08F0F24645A39794A8C0A89CCA3DD9A1FDE13952AF0FD`，单独解压CRC PASS，805件；第1至94次HA各具有真实终态V/密度，原HA95只含部分初始原证且未标成功。今天补入第96至201次HA的106组终态。
- 直接重算两阶段合计**200组已完成HA**的终态`V_terminal.f64leF.bin`和`density_terminal.f64leF.bin`文件长度及SHA256，200/200配对与`FULL_ARRAY_READBACK.json`逐项一致、V/density全有限。按20×20×2及原 `db=7/19`、`da=10/19`加权重算密度质量，最大偏离1约`5.6e-16`（不同求和顺序略有数值差异）；最小原始密度`-1.4410430559239803e-14`、最大负质量约`1.26e-14`，**保留浮点负值，不宣称严格非负KFE经新方法认证**。
- 冻结blackbox源在本次ZIP中整个文件SHA256精确为上述B92F...，而不是改动了内部selector/HJB。原包及本轮资产的实际Windows只读/OS原生安全保护仍为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不将外部ZIP哈希冒充主机物理IO审计。

## 2. 100轮与两省稳态事实

- 实际解析`run/trajectory.jsonl`恰100行，`GLOBAL_TRAJECTORY.csv`恰100轮×2匿名省=200条，两个文件的回合/次序可复核；本轮不是2009历史31省184轮重跑。
- 终态 `OWNER_100_ROUND_LIMIT_NONCONVERGED`；注意**第100轮是Owner新的主动终止点，并非原承诺“500轮自然停止”、也非在一进程中不中断完成**：原science进程在第47轮后Owner中断，HA95虽已计费却未完成；第二科学进程从完整47轮状态恢复至第100轮，累计预算没重置。原第一科学进程时点中断并保留原始轨迹前缀。
- 第100轮 `max KN gap=0.1075218256230952`、`max Y跨轮gap=0.012719310966908814`、`HA converged=0/2`，两个`ra_used`均上界`0.09`，工资均触边。**两省在全部100轮ra/wage边界均100/100次**。每省原HJB收敛标记仅10/100轮为True，只有第31轮两省同时标True；即使那一轮也未满足非边界要求。整个100轮只有26轮 `max KN gap<0.1`，但这不等于原 `reg_threshold=1e-9` 收敛。
- 关键诊断节点 `(round,max KN gap,max Y gap,HA qualified count)`：1:(1.005766,1.044022,0)，10:(0.443248,0.396521,0)，25:(0.067587,0.071070,0)，50:(0.069515,0.007370,1)，75:(0.155539,0.141592,0)，100:(0.107522,0.012719,0)。路径有非单调反弹，不能单凭100轮上界推测500轮必然不收敛，或从最后25轮线性斜率推证稳定吸引子。
- 资本回报边界频率1.0、工资边界频率1.0，`GovInv`、`Zt`亦在更新，说明需要优先审查**合成输入/尺度/外层收益边界反馈**，而不仅把问题归结为5轮不够长或Bellman硬约束。本次只是机制排序建议，不主张已定位具体归因。
- 据原件，私人资产守恒残差最大约`4.55e-13`，财政代数桥复算残差0，国家诊断最多约`9.09e-13`；这些不是宣称劳动市场、政府预算或全部宏观GE出清。Bellman B已在轨迹中作为诊断记录，**没有作为外加HA求解硬门**。

## 3. 资源与进程证据边界

- `science/events.jsonl` **1004条事件序号1..1004连续**，除不可比缺失字段按0处理以外，HA/HJB/KFE/driver/roots/selector工作计数逐条非递减。前47轮`resume_inputs/events_prefix.jsonl`与今日同一事件流逐字节前缀一致；轨迹前缀亦相同。终态计数`HA charged=201`、`HA completed=200`、`HA owner interrupted=1`、`HJB enters=201`、`KFE enters=200`、`HJB updates observed=19476`、`initializer roots=160800`、`local policy cell operations=15580800`、`scientific driver=2`。
- 原`LEDGER.json`列6个进程：科学PID 9960/5352两个，工程Python四个；终态资源wall 36027.2626195s（约10小时，原12小时上限内）。科学进程计费与Owner的续算许可，除上传本地收据和当前Owner报告支持外，未由顾问直接获取Windows会话/OS独立时钟取证。
- `ACCOUNTING_E1_RECONCILIATION.json`承认原PowerShell通用计数`scienceDriver=1`错误并保留原`LEDGER_BEFORE_POSTRUN_ACCOUNTING_REPAIR.json`字节；原子进程列表/正式科学账证明实际启动两个science，不得把修正后的总数写成原回执自己就正确。未见第三次science或额度复活的本地记录。
- 本轮`ENGINEERING_PYTHON=4/12`，Git/SSH/fetch/push=0，`RESULTS=False`，`FORMAL_V010_ACTIVATION=False`。模型/执行本机未改写保护目录的说法仍属本地回执级。

**科学终审：本次两省synthetic长轮次实验有效完成至Owner新100轮停点，但原稳态资格未通过；不推定旧Matlab-faithful HA错误，也不能推定当年31省2009 parity失效。** 旧正式V010仍`ACTIVE_TASK=NONE`、`Results FALSE`、`V011 NOT_STARTED`，全部本次未用计算预算关闭。若Owner后续决定实验其它窗口/改入口，必须另获新阶段授权，不因本报告自行恢复500轮额度。

## 4. GitHub MD/ZIP临时交付制度及当前原包处理

Owner 2026-10-18已要求今后允许**可审阅报告MD和ZIP证据包一同上传临时GitHub review树**，验收后清理。此权限作为独立长期工作流制度，见 [Owner新协议](CH5_OWNER_REVIEW_MD_ZIP_TEMP_EXCHANGE_POLICY_20261018.md)；它**仅**准许经过逐成员脱敏、压缩包内包递归检查、可控大小及严格白名单的**审阅专用派生ZIP**，不能把原始本地证据ZIP不经检查直接提交；因为Git清理最新tree不抹历史commit/caches。
本次上传的私人ZIP存在Windows原始绝对路径及内嵌昨晚的暂停RAW ZIP，**不适合未经脱敏公开提交**；既然Owner已在ChatGPT上传了可核原件，本次不再向GitHub临时分支复制它。保留其在当前会话的原字节身份与本份永久主审的hash足以完成本次交换。后续Codex依明确未来任务自动生成`result.md`+`manifest.json`+`evidence_sanitized.zip`候选；Astra永久归档并readback后才删除当前review分支白名单temp文件，历史保留。
