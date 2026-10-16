# 第五章脱敏审阅材料 GitHub 临时交换与清理协议（Owner 2026-10-16 授权）

**状态：OWNER_APPROVED_OPERATIONAL_REVIEW_EXCHANGE_POLICY**。
**Owner指令：**“以后请你记得让codex把脱敏文件传到github仓库的临时目录中，你验收后就可以删除，这样能节省很多时间。” 本协议作为后续新任务默认交付附加条款，**不追改任何已冻结任务、科学合同、历史review候选或既有本地证据**；仅在每次未来冻结任务明确引用/允许时生效。服务于V1.2 Owner→Astra→Codex工作流的证据传输效率，不是科学或Python运行授权。

## 1. Codex默认交付：新独立review分支 + 临时目录

- 每轮由Astra在**新**冻结任务指定唯一temp分支，例如`review/ch5-temp-<task-slug>-YYYYMMDD`，且指定`_review_tmp/ch5/<task-id>/`作为仅存放本轮**脱敏**审阅文件的临时GitHub目录；分支名、白名单文件、大小、唯一commit parent、允许的发布次数与网络预算必须在该任务中固定。Codex先检查分支不存在，再通过已经授权的GitHub连接/SSH443路径发布一次普通nonforce review提交，不改main、治理branch、模型原branch、其他任务历史。
- 默认上传`result.md`与`manifest.json`；必要时第三个非可执行静态源码/案例文本，**必须由冻结任务显式列白名单**。所有文件必须UTF-8 LF、明确任务/模型固定SHA、相应raw SHA256和最终资源账的证据等级。不得上传原始log、敏感数据、实际绝对用户路径、Git credentials、SSH私钥、token、包含真实科研数据的blob或大体积本机回执。预览/脱敏检查为强制前置。
- 若用Git本地准备review commit，需先验证任务发行commit的parent tree和拟写index所引用的**所有必要Git对象已完整存在**，不能再使用不完整`--filter=blob:none`浅部分基线加`write-tree`而假设一定能成功。可在每轮新冻结权限内采用受控的GitHub Git Objects API/Codex授权connector直接按固定parent写blob/tree/commit/ref，避免不必要的大型clone；不能擅自补fetch、无额度重试、改global/system Git config或force覆盖旧分支。
- 失败则`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED / STOP`并封存，不为尽快交付而越过原权限。允许Owner把两份脱敏原件直接放入当前ChatGPT会话供Astra验收作为保底路径，但**常态不再要求Owner手动搬运报告**。

## 2. Astra验收、固定结果和临时副本清理

- Astra从**精确GitHub候选commit/ref**实际读取完整脱敏文件，独立核路径、唯一parent、tree、Git Blob、UTF-8原字节SHA256、case/source静态证据及证据等级；本地Windows进程/保护未由Astra实际取证时仍明确`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。**禁止仅看Codex执行摘要就颁发科学PASS**。
- 审查完成，先在治理分支永久归档`versions/<version>/<task>_primary_review.md`或等价正式限域验收报告，更新`CURRENT/TASK_CURRENT/DOC_INDEX/版本登记/知识入口`；记录固定候选SHA、脱敏文件Hash、真实PASS/PARTIAL/FAIL和后继STOP。**先保存永久必要证据，后清临时文件**。
- Owner已明确许可Astra在保存且远端回读永久验收后，**只删除明确`_review_tmp/ch5/<task-id>/`下的临时审阅副本**，通过GitHub有权限的`delete_file`/按固定ref的普通清理commit、验证文件在临时review分支最新HEAD下消失，记录cleanup SHA/状态。不得删除冻结任务、正式验收、科学decision、历史失败原件或其他review文件；清理失败标`TEMP_CLEANUP_PENDING`并通知Owner，不能force改写或自动扩大权限。
- **Git删除不是秘密的彻底擦除**：临时文件曾经提交到Git历史，即便在分支HEAD删除，它们仍可能经旧commit SHA或缓存访问；这也是必须**上传前完成真正脱敏**的原因。若未来需要完全删除仓库历史中的敏感数据，应另获Owner批准使用专门的安全清理流程，不以普通`delete_file`冒充永久清除。当前GitHub连接器明确支持文件删除，不承诺自动删除整个Git分支。
- 此协议仅是以后新任务的默认**证据交换约定**；当次冻结任务若更严格（如禁止push/限1次/只能LOCAL_ONLY），以更严格约束为准。通过review不能自动授予下一进程、源clone或HA权限。GitHub临时交换不等于本地QMD/Basic Memory同步。

## 3. 默认未来新任务提示

每张后续需外部独立验收的任务均须写明：

`SANITIZED_REVIEW_DELIVERY=GITHUB_TEMP_REVIEW_DIRECTORY_FIRST`；
`TEMP_PATH=_review_tmp/ch5/<task-id>/`；
`ASTRA_AFTER_REVIEW=ARCHIVE_PERMANENT_VERDICT_THEN_DELETE_ONLY_TEMP_FILES_WITH_READBACK`；
`DO_NOT_ERASE_GIT_HISTORY_OR_FROZEN_AUTHORITY`。

不使用以往“需要Owner每次手工上传本地脱敏MD/JSON”作为默认交接路线；仅保留GitHub发布失败时的安全保底。
