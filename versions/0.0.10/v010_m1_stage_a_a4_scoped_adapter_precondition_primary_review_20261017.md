# V010 M1 Stage A → A4：SCOPED ADAPTER 工程前置独立主审

**日期：**2026-10-17（北京时间）；**签署对象：**原冻结任务 `V010_M1_EVIDENCE_AND_CONDITIONAL_SYNTHETIC_MAINLINE_LONG_TASK`，发行Commit `54454066859692a0f481cfa44de8df8dc298ce03`、任务Git Blob `5d87753b4a3ac972f37f1ac59722b464efd11bd9`。**这是任务内A4检查点，不是新任务、额外预算或科学Results验收。**

**正式A4裁决：`M1_SCOPED_ADAPTER_ENGINEERING_PRECONDITION_FOR_V010_SYNTHETIC_SCIENCE=PASS`。**

**严格作用域：**本PASS仅采纳上一M1在已披露残余风险下的 `SCOPED_ADAPTER_ONLY` 工程前提，允许 **同一TASK_ID** 从Stage A PAUSE进入冻结Stage B的 **B0非求解工程确认**。Stage B必须依旧按既定B0→B1→B2→B3→B4→B5先后顺序执行；**在B0的两项关键准备和最终候选接线/资源账有效闭合前，HA/HJB/KFE/selector/scalar-root实际调用仍须为0**。本裁决并不接受native无适配导入或完整Windows Runner I/O闭环。

## 一、独立取得的原始输入及身份

- Owner上传的 `CH5_V010_M1_EVIDENCE_ORIGINALS_20261017.zip`：65,737B；容器独立SHA256 `8961AD01642992CF397BBD2DB165D62AB5AD4B44A9990DDEC1D4000C96C819CA`。CRC成功、10个平铺成员、无重复，其中九份M1既有文件204,154B以及一份独立派生 `package_manifest.json`。
- 另单独收到 `V010_M1_STAGE_A_EVIDENCE_AND_READINESS_HANDOFF.md`：3,089B，独立SHA256 `294CDE6AC35DD92F4FA9ED7FE05E2AD619528FBAECBB51AAC3912AF6E0B71899`。
- 九件均实际从上传ZIP读取并逐件计算长度/SHA256，与旧GitHub固定补充审议和本次pack manifest 9/9一致。**文件原字节可验≠历史所有Windows底层日志完整存在。**
- 在实际读取文件之间对 run_id、FIRST→FINAL哈希、manifest/evidence/ledger/index、原工程任务Blob、模型Commit/Tree、source/module/runner child结构、Stage A交接及B0前置作58项限域静态一致性断言，58/58匹配；这些断言不构成新的Windows重跑或22项数学focused测试。
- 固定科学plan `bf091da33d59293f147d52c11580327d3ac2a85d`/Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型 `94de4501dec051b969bee9d852eba2d4591f30ef`/Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；唯一匿名双省fixture Blob `40915658d93403cfc21b33a6b864b332b7857749`。远端Git对象身份保持不变。没有真实C8或31省数据验收。

| M1已交付成员 | 字节 | 独立SHA256 | 身份 |
|---|---:|---|---|
| `FIRST_RECEIPT.json` | 1097 | `4F1511731A3A01C4F69136F5B9F7C81E0F492F21202107D8EDF9108131B87F32` | RAW_EXACT_AS_DELIVERED |
| `ENGINEERING_FINAL_RAW.json` | 6879 | `80F224002E4A5B41ABF3D7E14CB522F3E948329658DE1AB40E17A485B99D24CF` | RAW_EXACT_AS_DELIVERED |
| `manifest.json` | 1290 | `C2A6D9C1C6E96445B5DBA0BB0D9729A482F3D8684F6F2287DED18D460F4550BB` | SANITIZED_DERIVATIVE |
| `result.md` | 3238 | `72A2236FAAA7A2DF33D85FAF042CBDE52C17704D8714AAB4E50D5A63ACB054BB` | SANITIZED_DERIVATIVE |
| `engineering_evidence.json` | 43997 | `4128FAF7755876A2AD7B2C44FCE5E4646DE681E939E9A35B8845D62BA112AB3A` | SANITIZED_DERIVATIVE |
| `runner_candidate.txt` | 64668 | `5FA1DC0272BEC4DAF7CD35B73141C8CCEBCF91249843FABF83DB60763F2E6391` | SANITIZED_DERIVATIVE |
| `PUBLICATION_RECEIPT.json` | 1178 | `644F376B591CD2011447D42771EE3BAA0861712B7FE8400C906491E7066D1E32` | RAW_EXACT_AS_DELIVERED |
| `TERMINAL_ARTIFACT_INDEX.json` | 61929 | `505B58F273B3D5351692D50CF2D22463D42BC21FDC60155B74A9B441F34BBD73` | RAW_EXACT_AS_DELIVERED |
| `LEDGER.json` | 19878 | `901179BF0C41941EF69C175AC18842D711A28E2AF96CBCEB6AB619C2E905E8BF` | RAW_EXACT_AS_DELIVERED |

原M1 run_id：`98dd956bb1d54154a1d449b244f83a50`。本轮 Stage A 打包run_id：`47288dc296c2481f9bbabd763e7b4fc5`。二者**不是**同一运行，不可混淆。

## 二、证据分级与已知残余

1. `UPLOADED_RAW_BYTES_SHA_VERIFIED`：上述九份**按此前原始交付身份**的字节真实被本会话取得并核对；其中5份 `RAW_EXACT_AS_DELIVERED`、4份原本已脱敏 `SANITIZED_DERIVATIVE`，后者不是其Windows底层RAW原件。
2. `GITHUB_REMOTE_VERIFIED`：冻结plan/模型tree/fixture身份与现时治理分支经远端校对。上传ZIP本身不发布到GitHub，只在本审议记录SHA。
3. `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`：Stage A本机最终focused为22/22（第一次AST预期19/20后保留失败再修正）；工程Python4/16；Stage A wall 816.473秒；raw source 1,124,689B/16MiB；旧M1工程23/24及20 runner-Git child、5 Git child/Job/reader/reap、N13超时等Windows发生事实。Stage A `FOCUSED_ORACLES_ATTEMPT_3.json` 等11份文件只有文件名/哈希，未上传原字节，**22/22不能改写为Astra独立重跑PASS**。
4. `UNKNOWN/UNVERIFIABLE`：原20个runner-Git children逐项原始事件、精确曾执行runner源码的raw字节（现为派生 `runner_candidate.txt`）、早期Git prelaunch snapshots、旧PowerShell host wrapper PID、原dummy overflow read probe、原B/S/L first/run_id历史缺口、真实native OS隔离。此前 `process_result_19/final.json` 的N13 `streams_complete=true`错误与应为FALSE的派生修正保留，不能声称原件本身被更正或独立确认超时时点。
5. scoped适配器仅为当前Windows host的 `platform.win32_ver` metadata替代；原canonical native导入仍 `GIT_NO_CAPABILITY` 阻断，网络/Popen无限制放行不许可。保留 `FULL_RUNNER_IO_CLOSURE=BLOCKED` 与 `TRUSTED_WORKSTATION_NOT_NATIVE_OS_SANDBOX`，Owner既有风险备份选择不变。

**为什么可限域签A4：**冻结A4明确要求的**九份上一M1已交付文件本身**已真正取得、身份逐件复核，并可将原阶段所报告的adapter/runner/ledger与明确UNKNOWN分别定位。此PASS只是**已知范围的工程前提/阶段准入**，绝不据其宣布底层Windows日志全部独立验证或科学数值合格；Owner批准的剩余可信工作站风险仅适用于冻结的匿名synthetic运行，B0工程闭合仍先于任何求解。

## 三、B0两项已知工程缺口：必须在任何B1求解前关闭

**B0-1（全量输出重复身份）**：冻结 `validators/multi_province/v010_mainline_validation.py` 目前将同输入HA的`asdict(first)==asdict(second)`与`V0`摘要比较作为重复检验；现有 `mainline_household_runtime.py` 的qualified摘要含policy哈希和KFE统计，但没有独立封存并比较**最终完整值函数V**与**KFE概率质量数组**的原字节哈希。必须在plan允许的15代码路径范围内，绑定两次同输入的完整V/p及其F-order/float64/归一化口径，先做source-only/stub确认，不得改HJB/KFE公式或接受阈值。
 
**B0-2（跨driver累计预算）**：固定validation driver在每个新output建立新ledger，不能凭单进程本地计数证明同TASK_ID跨最多4次driver科学进程的HA≤26、selector≤2,100,800、root≤10,400,000及其他冻结上限。必须先建立当前任务持久的**单写者累计科学调用账**、失败先扣和进程重启读回/抗重置检查，再允许运行B1。不得将Stage A 4/16资源重新归零或混充Stage B，禁止启动未经认证的standalone driver。

B0还应完成原先冻结的最终候选tree、fixture逐字节、真实源码/adapter来源以及非求解focused oracle身份确认。**如果B0任一关键工程门不合格、试图修改数值阈值/经济法则、破坏账本或触原保护目录，立即依原冻结任务FAIL_CLOSED/STOP；不得因本PASS跨过B0直接算HA。** 本次不发新任务、不改冻结task/plan/fixture/model，不授额外Python/pytest/driver/HA次数。

## 四、任务生命周期、科学等级、保护

- Stage A：`DELIVERED__A4_SCOPED_EVIDENCE_ACCEPTED`，不把22/22本机测试提升独立完整数学PASS。
- Stage B：`RELEASED_CONDITIONAL__B0_PRE_SOLVER_ENGINEERING_FIRST`；未来若B0真实合格，才可在既有冻结预算、真实fixture和严格双门下开展B1两次同输入HA。任何后续B2-B4只可逐门限额推进，失败诚实STOP。
- 未来最高26次HA（2＋10＋2＋12）、4 science drivers、6 focused pytest仅在这份已签A4的原同TASK_ID下受冻约束；**本次实际新增科学调用0，科学有效性、模型激活与Results都仍FALSE**。
- `SOURCE_ENGINEERING`：SCOPED_A4_PRECONDITION_PASS_WITH_RESIDUALS；`SYNTHETIC_HA_HJB_KFE`、`SYNTHETIC_STEADY_STATE`、`FREEZE_GDP_TARGET`、`DYNAMIC_RECURSION`均NOT_RUN；`REAL_GE=FALSE`；`Results FALSE`；`V011 NOT_STARTED`。
- 不接触历史 `D:\ProjectTemp\c5k1bturn56` 8 dirty/index/外common-dir、已有C盘独立SSD备份、旧失败回执、真实C8/2017/2018/B3/V009；旧A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED保留。

## 五、GitHub审阅交换与清理

本次Owner的私人ZIP和MD由ChatGPT会话接受，没有临时Github review tree新增；M1上一轮SSH预检exit128、push0，精确review ref不存在，**没有本任务远端临时文件可以清理**。10月16日Import Guard先归档再清理的旧review HEAD已是cleanup `823c86d2ac210d65d10568c42fa793b0de72dc41`，两份temp文件在该HEAD均404。未来Codex按当次已冻结许可优先将可公开脱敏MD/JSON放独立远端review分支，Astra先归档回读再清白名单文件；大型/含raw秘密材料继续Owner私下上传。上述不意味着有自动后台清理服务。

**唯一后继动作：**Codex收到本治理A4裁决后，在同一TASK_ID及同一累计账内恢复**B0**，先关闭两项工程硬缺口与最终树的非求解校验，再循原plan的B1-B5资格顺序自主推进；Owner仅在既定重要/科学STOP点集中交付。**正式A4签署值：`M1_SCOPED_ADAPTER_ENGINEERING_PRECONDITION_FOR_V010_SYNTHETIC_SCIENCE=PASS`。**
