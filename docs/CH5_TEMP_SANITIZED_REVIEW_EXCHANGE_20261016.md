# 第五章脱敏审阅材料 GitHub 临时交换与清理协议（Owner 2026-10-16 授权）

## 2026-10-16 Owner 最新 GitHub SSH Key连接要求（仅改变Codex发布链）

Owner明确指定**Codex连接GitHub使用既有SSH Key**（已知可走`ssh.github.com:443`），不为临时审阅要求PAT、API Key或新令牌，禁止写global/system Git config或把SSH私钥/agent信息纳入公开文档。若此前本协议某段建议“GitHub Git Objects API作为Codex默认首选”，**优先于该建议的Owner新规定是：Codex在原项目工作树之外、独占且不共享.git objects的`git --bare`发布对象库中，经SSH key/443准备全部task parent-tree/blob对象并执行唯一普通nonforce push**。禁止重复以不完整`--depth=1 --filter=blob:none`基线制造`write-tree`缺promisor blob；不额外clone/fetch未授权模型代码。Astra仍可通过其已安装GitHub连接器审核、永久归档、按Owner已许可的**远端临时路径**删除review文件与回读；连接器本身不代表Codex改成PAT。

**长期本地目录禁令不变且从严**：`_review_tmp/ch5/<task-id>/`只能在**远端review分支提交tree中存在**，Codex禁止在原科研/模型/治理项目worktree、index/staged、已有受保护仓库或C盘备份目录创建/checkout/git add该目录，也不靠修改.gitignore隐藏。bare Git对象库存于项目外新scratch，无checkout；本地只允许平铺脱敏MD/JSON供转换成远端树对象，不在本地创建`_review_tmp`目录。Astra先审阅并永久归档，远端readback成功后**仅清理远端temp branch当前tree中的白名单临时文件**、回读cleanup；原历史commit保留，不能靠删除实现秘密消除。每张新任务需固定分支/path/parent/大小/发布次数/失败STOP。

**生效当前任务实例**：`V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT`，已发行Commit`01129efd5220683d415bd1486f23f6ecd068cb53`、task Blob`1e6757fd235fd96d8b08130ca3fefb3b602c413c`；本条不追改旧Git候选或授权新科学过程。


## Owner补充强制规则：临时审阅目录不得进入任何本地项目工作树或Git索引（2026-10-16）

**长期Owner决定（优先于下方一般临时交付例示）**：`_review_tmp/ch5/<task-id>/` 是**GitHub远端独立review分支的临时文件路径**，并非本地模型、科研项目、治理工作树下可创建的文件夹。Codex**不得**在原项目repository root、任何既有项目worktree、受保护D盘旧树或其staged index内创建/复制/暂存/提交`_review_tmp`；不得把review临时目录加入本地`git add`、git status待提交项、checkout或主分支/科学模型tree；也不修改全局Git配置、本地protected worktree的`.gitignore`/`.git/info/exclude`来掩盖临时文件。不要使用`git worktree add`、共享工作树、hardlink/alternates/--reference/--shared。**同名路径仅允许存在于远端临时review commit的树中**；这不是把文件加入本地项目工作区。

**推荐优先路径**：通过有权限的GitHub Git Data Objects API/连接器，直接对**完整、固定的任务发行commit**创建脱敏Git Blob、附加到远端candidate tree、单parent commit和独立临时review ref，全程不落地仓库工作树或Git索引。工具不可用时，替代为在项目工作树**之外**新建独占、非共享`git --bare`发布对象库，保持`core.bare=true`、无checkout/working-tree、不共享原`.git`或对象；在发布前证明parent/tree/所有必要blob齐全、write-tree不会因`--filter=blob:none`造成lazy-fetch依赖缺失。不能在旧/受保护的本地Git index里临时stage。模型源码、runner原件和历史失败本地树均不能为审阅发布而改写。

**验收/删除范围**：Astra先从远端临时ref+commit精确读MD/JSON并归档永久review、动态治理和必要证据哈希，经GitHub远端readback确认后，才可在**该临时review分支**用允许的删除动作删`_review_tmp/ch5/<task-id>/`里的明确白名单文件并核对临时目录从分支最新tree消失。绝不在Owner本机原工程工作树里执行`git clean`、`rm -rf`、checkout、reset或`git add`；不能清理正式`versions/`验收、冻结任务、旧失败或model branch。连接器不支持安全删整个branch时，维持清理后的review ref与清理Commit，不用force/rewrite历史。文件旧commit历史仍可能可访问，所以上传前脱敏不可省。

**交接/记忆锚点**：此段写入项目长期GitHub知识入口、V1.2工作流与后续固定任务；ChatGPT产品个人Memory摘要不保证由工具即时同步或可强制写入。未来顾问必须先读`docs/DOC_INDEX_CURRENT.md`、本协议及知识入口，按Owner当前决定执行；不以仅凭对话的“已记忆”替代可回读的仓库权威。


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
