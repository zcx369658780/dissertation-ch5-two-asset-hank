# V010 CP2_F25 机制取证／条件式修复任务：独立终态主审

**日期：2026-10-17（北京时间）；裁决：`V010_CP2F25__NO_MATH_PRESERVING_REPAIR_PROVEN__INDEPENDENT_LIMITED_ACCEPT__STOP`。**
**任务终态：`DELIVERED__STOPPED`；新任务未签发；上轮所有未使用预算关闭。**
**本报告性质：**独立读取 Owner 通过 ChatGPT 私人上传的源字节、验证现有冻结 GitHub 规则、重算独立标量代数及交叉检查执行证据。**本审议未在用户 Windows 上重新运行模型/原生进程，不替代物理OS审计或全局存在性证明。**

## 1. 冻结 Authority 与实际取得的材料

- 唯一任务：`V010_CP2F25_SELECTOR_MECHANISM_AND_CONDITIONAL_REPAIR_LONG_TASK`，原不可变发行 commit `98b3154e84db62d4d319836db0a39e3278017c33`，任务 Blob `dfc29c2df0187875aee8d81b0ad6a23662e76a02`。私人ZIP中的 `task_RAW.md` 精确15,164字节，经 Git blob-header/原字节重算 `dfc29c2df0187875aee8d81b0ad6a23662e76a02`，匹配冻结发行正文。任务期间治理固定HEAD `5723d0f34fa8541b8094892542bce5857ddda273`。旧 M1 任务已 `SCIENCE_FAIL_CLOSED`、旧预算不续用。
- 冻结V010科学plan Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型 commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；匿名fixture Blob `40915658d93403cfc21b33a6b864b332b7857749` 不变。
- 用户实际上传 `CH5_V010_CP2F25_MECHANISM_EVIDENCE_20261017_FINAL.zip`，**2,632,180 B**，独立SHA256 `A1459D9452F1AD7A755479AACE65B5FCA61E08130C73D098491599AB971E9141`；另实际上传结果报告 `V010_CP2F25_MECHANISM_REPAIR_LONG_RESULT.md`，**5,418 B**，SHA256 `F0CCF6A1EB2C27BC8FEB92391918750D56BA277EEC539816E412058722C76E61`（与ZIP同名原字节一致）；另外上传外部回执 `DELIVERY_RECEIPT(1).json`，**1,633 B**，SHA256 `064EBDF09FC5467692D9A6E9D3D1FB1AD0898C10ADB3D948D24D27399F2B0D15`。
- ZIP有522个有效文件成员（无重名、CRC通过），其中最终manifest `PRIVATE_PACKAGE_FINAL_MANIFEST.json` **121,321 B**，SHA256 `CA6A300BB938CDC0315D1C2A0DA6A711496914403351D35BF244DA68153DE2C0`；该清单对**其余521份**逐项标注路径、长度、SHA256。本审议实际迭代521/521：路径集合完全一致、原字节长度与SHA256全部匹配。原内部 `PRIVATE_PACKAGE_MANIFEST.json`只覆盖514份历史打包节点，不代替最终521件清单；此前不完整1,346,609B ZIP以`INCOMPLETE_PRESERVED_NOT_VALID_DELIVERY`另存，没有误报终态。
- 首封 `FIRST_RECEIPT.json` 867 B、SHA256 `21059BDB8D2D8C18A29D9776A9C60D3B159DEE58E2CEB12F80E01263FC47680E`；`FINAL_RECEIPT_RAW.json` SHA256 `30D96ECBBBD366562D2AB7D41C722C56F74410CD6DB1FF7820C38DD0BA93B6D2`；后继 `FINAL_RECEIPT_V2.json` SHA256 `1218B356FF3188C24BB41B9C3A47315F57D370398EEADDE82BD3952B91D7D9FC`。保留原始E1封存修复事件，不伪造更早初始raw或重写历史报告。

## 2. 数学合同与代码身份：原Owner筛选门确实存在

本审议从上传包内直接重算三个Owner权威合同的Git blob，并从**固定模型commit GitHub**独立回读匹配：

- 2026-09-16 `interior liquid-Z` Owner采用协议，Blob `cc11b11a1c288220ca0138584cd41256122eae6b`：同一冻结非流动资产分支/转移regime下，液态 backward candidate 必须严格`g_b>+bound`、forward candidate严格`g_b<-bound`且影子价格有限正，才有权调用合法Z根；不具strict crossing则不运行Z根。
- 2026-09-19 `interior-a zero-drift` Owner采用协议，Blob `b82dc896673466e79ab86258bc6e897eb3c8bf95`：单轴a切换的严格方向穿越、D3 KKT和已采用液态规则照旧。
- 2026-09-19 **joint simultaneous two-axis zero drift** Owner采用协议，Blob `17e0c4de4b1fdaa9a43f1b2211fb10d8f5173c75`：**a-backward与a-forward两端分别须先产生合法liquid-Z回执，然后两回执的a漂移再形成严格交叉**；`g_b=g_a=0`方程、D3比率、导数矩形交集与唯一root只是该触发之后的后续条件。该先决条件由本报告核对合同正文第1节，而非从Codex口头推测得到。
- 冻结 `src/ch5_two_asset_hank/corrected_diagnostic/selector.py` Git Blob `51517dde0c829060b6e0c0d594ec60e7e6143883`，在上传包及GitHub固定模型下逐字节一致（62,595 B、SHA256 `25B93033FD886A159DBE74E219087250408A7239F370C8B64D3F58624418E1A4` **注意该SHA以实际上传来源重新验出的值为准，详见随附证据索引**）。源代码`_interior_z_candidate`的两侧strict跨越筛查、`select_constrained_policy`中需要两侧`liquid_z_candidates`才能形成`joint_contexts`、`_joint_switching_candidate`对两份合法Z回执与a漂移穿越的审查，与上面采用文本是同一逻辑方向。**不是应当从当前任务白名单内直接删除的无害工程if。**
- 共7份Owner规则与历史测试的原字节Git Blob逐一匹配所声明的固定源；本次本地`candidate/` 76份文件与上一M1由Owner先前独立上传的ZIP中`final_view_v2/` **76/76精确相同**，且F25 `first_failed_cell.json`、`input.json`与上一包原字节相同。与更早冻结原模型76份对比为74一致、仅两份前M1已经验收的B0工程adapter/validator差异；**无新selector补丁**、无新增focused修复源码。本次没有Github模型Commit或完整HA新候选。

## 3. F25 单格原始数值与真正的阻断性质

旧M1 `reference/science_driver_01/HA_01_binding/first_failed_cell.json` 22,390 B，独立SHA256 `E01A5E5137424C238F8090903D21970910A2CC1562103FC2C78FB16E0487CEC3`，精确记录CP2、F-order zero-based flat=25，`b=-0.1578947368421053, a=0.5263157894736842, z=0.8`，原selector 12个candidate全inadmissible、`selected=null`、`admissible_comparison_count=0`。
 
**独立标量复算：** 本审议没有运行上传的原`f25_algebra_oracle.py`或原模型，而是从上述失效单元原始shadow、输入参数和12个candidate，使用另行编写的Python decimal运算，自主计算 `c,l,d,C,g_b,g_a,D3/KKT`及漂移方向条件。**12/12 rejection_reasons逐件顺序完全相等，逐值最大浮点差约`1.717376241217039e-16`**，没有不符记录。拒因次数（同一候选可有多因）：B导数方向8、A导数方向7、D3 KKT8、negative transfer符号3、positive transfer符号3。
 
**严格liquid-Z前置门的实际值**：在negative transfer、`a=backward`同一regime下，液态 backward-b 原始`g_b≈-0.00723960631082224`、forward-b`g_b≈-0.37202352655533`，对应浮点算术bound约`9.73e-14`与`1.07e-13`；**二者都严格负**。因此没有符合“backward液态正、forward液态负”的方向穿越，**backward-a没有合法liquid-Z回执**。同一negative regime的`a=forward`端点虽显示相反符号并出现单轴液态Z候选，但该候选因a轴方向不符被拒。没有同时满足两端合法Z回执的joint上下文；`joint switching root invocations=0`。
 
**同时，联合方程在更弱意义下有根**：由`g_a=0`求得固定`d_{ZZ}≈-0.02894736842104366`，D3比率`q_a/q_b≈0.7900000000000341`，正导数闭交集 `q_b∈[0.5125993570052673,0.5460198582796224]`。独立使用冻结 `g_b(q_b,d_{ZZ})`复算，两端约`-0.013473607513933913`与`+0.04612905863486928`；给定正参数的`g_b`随正`q_b`严格递增，所以在此区间由介值定理得唯一**代数**根。但**未授权计算该joint数值根**，且**代数根存在不能替代冻结“先双侧Z回执”触发**。这些条件分账使“原合同阻止joint fallback”和“没有任何数学意义的联合根”明确不同。

原F25 selector实际重放的回执 `F_F25_EXACT_REPLAY.json` 对上轮失败 `result` 全字段重放一致，仅selector全球ordinal由1626改成1；仍`NO_ADMISSIBLE_POLICY`，计1次单格selector、3次其中有合法调用权限的scalar roots、joint roots 0、warnings 0。这里的原生Windows运行过程由Codex回执支持，Astra的独立核对是源文件身份、JSON字段与十二候选的自主代数计算，**没有在Astra运行原Windows selector**。

**科学判定：`NO_MATH_PRESERVING_REPAIR_PROVEN__STOP` 的证据充分。** 这不代表selector在所有单元完全正确，也不证明整个HANK经济模型或联合PDE无解；仅证明在F25这个固定单元里**不能把删除现有joint strict触发门宣称为“保持原Owner科学合同不变的实现bug修复”**。根据原冻结任务“未证明等价修复则F阶段STOP”的门，应停止而不patch。R阶段、修复后的D阶段、新HA/KFE、外层稳态及短动态均NOT_RUN。

## 4. 新任务资源账、失败与GitHub远端

- 207份 `ledger_events/0001..0207.json` 逐件实际检查run_id `9778e181319c4532b239724a3b7a0a3a`、序号1..207连续、Python/roots/selector/HA/HJB/KFE/pytest/oldBytes/push计数**无递减**，终态与`LEDGER.json`一致。原`SELECTOR_DIAGNOSTIC_EVENTS.jsonl`四个先记后操作事件对应 selector=1、roots=3，HA/HJB/KFE=0。
- **Python槽已扣3/24，真实启动2**：首次PowerShell`New`方法名称碰撞在Job启动前发生，但保守计1槽；后两个真实Python各exit0。Focused pytest 0/8。Root=3/2048、single-cell selector=1/64，model policy-map、完整HA/HJB/KFE/GE/IRF均0。新wall含封存740.901秒/21600；old archive read=4,567,535B/64MiB，非Git和RSS自报在冻界内。未用额度随STOP全部关闭，不迁移。
- `LEDGER.json`登记11个子进程（2 Python、9 Git）；22份实际stdout/stderr原字节逐件核hash/bytes **22/22 PASS**。原启动、Job、PID reaped、物理权限/备份等仅为`CODEX_REPORTED_WITH_UPLOADED_LOCAL_RECEIPTS`，不宣称审稿人在Windows OS系统独立证真。受信任工作站仍不等于OS-native sandbox。
- SSH-over-443首次且唯一的远端预检失败exit128，实际stderr为`Could not read from remote repository`；未能证明具体是key、权限还是远端连接根因。未再次SSH、fetch0、push0、未生成review候选commit。GitHub连接器独立检查约定review分支`review/ch5-temp-v010-cp2f25-selector-mechanism-20261017`返回404；**本轮没有GitHub temp文件可清理**。仅本次独立主审及治理状态由Astra在治理分支永久保存，私人原证ZIP绝不外传到GitHub。
- `FIRST_RECEIPT`/本机bootstraps/新scratch旧保护无写，除前述原字节证据外尚非独立Windows系统调用取证；更早20 child/N13历史错误原件/时点及A16/window/C9/CALL_LEDGER、8 dirty/index/external common-dir与C盘独立SSD备份仍为原证等级、保留原保护，绝不重新赋予PASS。

## 5. 最终权限与下一Owner科学门

**ACTIVE_TASK=NONE**。
**LAST_TASK=`V010_CP2F25_SELECTOR_MECHANISM_AND_CONDITIONAL_REPAIR_LONG_TASK`，TERMINAL=`V010_CP2F25__NO_MATH_PRESERVING_REPAIR_PROVEN__INDEPENDENT_LIMITED_ACCEPT__STOP`**。
**NEXT=WAIT_OWNER_V010_JOINT_TRIGGER_SCIENTIFIC_DECISION / STOP**，不自动签下一任务。
**BUDGET_CLOSED_NO_CARRY**；数学规则、V010模型源码、MATLAB、固定fixture均不改变，`SCIENTIFIC_DECISIONS.md`无新采纳故不改。
**FULL_RUNNER_IO_CLOSURE=BLOCKED，model_activation=False，REAL_GE=False，Results FALSE，V011 NOT_STARTED**。

下一步若Owner意欲解决当前F25的HJB策略可行性瓶颈，科学上必须**单独重新审议已经采纳的joint strict-crossing触发法则本身**：它是否只是保证数值upwind选择的充分条件、是否过度限制联合候选、与原连续时间HJB Hamiltonian/viscosity solution定义的一致性如何。若修改采纳法则，这是**E3新科学规则决策**，不得称E1工程bug或在此次STOP任务里悄然放宽；未来新的HA预算更须Owner重新授权。现阶段仅建议，不发行任务，也不虚构已证明的新法则。
