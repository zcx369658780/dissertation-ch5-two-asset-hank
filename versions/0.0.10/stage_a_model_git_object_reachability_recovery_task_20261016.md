# V010 Stage A：冻结模型 Git 对象可达性与独立签出单点修复（正式任务）

**任务ID：V010_STAGE_A_FROZEN_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY**

**授权来源**：Owner于2026-10-16确认执行前轮Astra独立验收建议，仅开展一次全新隔离 Stage A Git 对象可达性修复；执行条件由Astra在本任务限域冻结。不得把旧工程任务的未用Python额度继续使用。

**本任务目标**：修复前一 ENGINEERING_ONLY Windows preflight 使用治理分支 single-branch clone、致模型代码树缺失而 checkout exit128 的**准备阶段范围错误**。在正确的、独立的模型分支克隆中取得并实际校验冻结Commit/Tree/唯一Parent、九份源码 Git Blob与签出磁盘字节、独立 Git common-dir；以有限脱敏证据供Astra复审。**不运行Windows runner，不进行Python、AST、pytest、HA、HJB、KFE、selector、root、GE、IRF或真实数据科学计算。**

**状态资格**：只能报告 A_STAGE_OBJECT_REACHABILITY_VERIFIED 或 A_STAGE_OBJECT_REACHABILITY_FAIL_CLOSED。无论结果如何，ENGINEERING_RUNTIME_NOT_RUN、HA_SCIENCE_NOT_RUN、FULL_RUNNER_IO_CLOSURE=BLOCKED、Results FALSE；Codex不得自行给后续工程preflight或科学计算放行。

## 1. 固定证据和准确来源

- 唯一仓库：zcx369658780/dissertation-ch5-two-asset-hank，动态治理分支 migration/astra-workflow-20261012。
- 当前被Astra独立验收的前序失败：review commit 416cff6c00d2b865c3e9dda4088242d2b80969ce，tree 1d5bc390774d68ea619f6ad263c99d0090486b37；Astra原审议版本位于 versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md，blob 7ba0991b76bc2d5304f78c7e7ddb5d0c8f746b96。旧任务 ENGINEERING_PREFLIGHT_FAIL_CLOSED / STOP，不重试、不改原回执。
- **这次必须取得的远端模型分支**：refs/heads/codex/ch5-v010-matlab-first-20261015。Astra通过GitHub真实查询确认分支HEAD = 94de4501dec051b969bee9d852eba2d4591f30ef。
- **模型冻结身份**：commit 94de4501dec051b969bee9d852eba2d4591f30ef，tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5，sole parent a1db8c114dec0ab69d69a5576e153a7f868cba0e。
- V010冻结科学计划：commit bf091da33d59293f147d52c11580327d3ac2a85d / plan blob 85138d8859d53295262fe13bf5bc277bca95ed3f；原合成fixture blob 40915658d93403cfc21b33a6b864b332b7857749；单点manifest blob c23d331bed34e5ca478324cdc05034609ecb91b7。所有对象只作身份参考，本次不读运行数据、不执行，不追改。
- 前静态runner候选 review commit c207e866cf70d9d5ae6fb245f43cabfdeac1d32b 的 nine-source identity 在下方列明。它们是对冻结模型 Git 源码的预期，**不是先前Windows本机源码已验证的证明**。

以下九份路径均相对于冻结模型仓库根，全部位于 src/ch5_two_asset_hank/；期望 Git Blob（40位SHA1）必须逐一精确一致：

| 相对路径（省略公共前缀） | 期望Blob |
|---|---|
| multi_province/mainline_household_runtime.py | 3d2d7d92aea0036f36d88ef15c05cbb3b40eba90 |
| corrected_diagnostic/selector.py | 51517dde0c829060b6e0c0d594ec60e7e6143883 |
| corrected_diagnostic/generator.py | f86234340c6e09c7129225da1677614669754177 |
| corrected_diagnostic/option_a_step.py | e0fcbf01af9b1778d245d960fe85c592f55c032c |
| corrected_diagnostic/nonlinear_continuation.py | a473f86eef22ad893673dba2a80ec8029de8afd1 |
| corrected_diagnostic/contracts.py | 41186454de5ba1f55d3ba273f7ce57457ded11ca |
| multi_province/corrected_household_adapter.py | f79e089f06d0d74867284dc88c94c594215dc02e |
| corrected_diagnostic/v1_q1_topology.py | a238c999d3a6e18e8672efa1aae00498e747d403 |
| corrected_diagnostic/q1_kfe_validation.py | 45f4b95024c4441809dba3fe27044f25b3339f0f |

## 2. 全新隔离环境与硬权限

唯一新的 Stage A 本地scratch前缀：D:\ProjectTemp\ch5_v010_stage_a_git_reachability_20261016_01。若目标已存在或无法排他新建，必须STOP并报告，不能覆盖、删旧目录或自动换名以绕开证据。确切本机私有路径不进入公开文件。

本任务明确允许**在新隔离目录内**使用固定Git可执行程序、Windows PowerShell读取/哈希小型Git源码和写入新报告，建立**至多一个模型候选Git clone**，并仅在该新clone内执行配置与sparse checkout。用于GitHub脱敏review发布的额外最小Git元数据工作区可独立准备，但不得共享任何受保护Git objects/common-dir；两个工作区的新增Git对象和签出文件**合计≤2GiB**。不得使用原工作树、旧失败clone或它们的共享Git object store。严禁Git worktree、clone --shared、--reference、alternates以及对原保护repo的fetch/reset/checkout/clean/stash。

严禁访问或写入原受保护 D:\ProjectTemp\c5k1bturn56，包括其8 dirty tracked、index、staged、untracked/ignored和外部common-dir；禁止触及旧失败证据根、旧V009数组、C8/2017/2018/B3、真实经济数据以及相邻项目。本轮无须读取旧本机private runner或raw log；仅可参照已在GitHub脱敏的任务/审议/源Blob。

**全部Python/py/Jupyter/import/py_compile/pytest/scipy/模型执行、新工程runner/Windows argv harness与科学进程许可=0**。PowerShell不能间接启动 Python/模型；本轮只做Git对象和磁盘静态字节可达性校验。不修改九份Python源的任何字节，不修改任何原项目科学代码/经济参数/网格/阈值、runner设计、冻结manifest或审议原件。

## 3. 一次集中Stage A实施顺序

**A0：新进程之前的Git身份核验。**
- 使用真实固定URL和只读 git ls-remote --heads 精确查询 refs/heads/codex/ch5-v010-matlab-first-20261015；必须返回冻结 commit 94de4501dec051b969bee9d852eba2d4591f30ef。远端ref若变化/缺失/身份不一，STOP，不改用main或治理分支。
- 固定可执行Git二进制路径/哈希，独立scratch绝对路径，保证无链接/reparse到旧工作树；控制Git环境，拒绝GIT_OBJECT_DIRECTORY/GIT_ALTERNATE_OBJECT_DIRECTORIES等外部对象路径污染；不运行Git hooks、外部smudge filter或未知自定义脚本。无法保证可信、可界定时STOP。
- 在外部PowerShell持久账中先记目标远端ref/预期commit、新clone路径类别、资源和执行起点；日志明确UTF-8、LF及字节上限。记录所有显式Git命令、退出码和时间；依赖命令失败立即STOP，不能仅依据stdout判成功。

**A1：正确分支的新模型clone。**
- 只允许一次 clone，必须采用来自**模型分支** codex/ch5-v010-matlab-first-20261015 的 --no-checkout --single-branch --branch 取对象；可加 --no-tags、可信模板及关闭hooks等保护选项。**绝对禁止再以 migration/astra-workflow-20261012 作为此模型clone的唯一获取分支**。
- 本次Stage A模型网络顶层命令至多两项：一次上方ls-remote以及一次正确分支clone；**模型clone失败或对象仍缺失时不进行第二次clone、补fetch或另一个分支的大范围取物**。本轮不批准浅克隆、--filter导致的promisor/lazy-fetch、自动子模块递归、Git-LFS smudge联网或从旧clone复制objects。Git clone来源准确GitHub仓库；不能引入新remote。

**A2：Git对象及独立性门（先于checkout）。**
- 在新clone内核对HEAD/远端模型ref、固定commit对象类型commit、root tree=205eab47c4e4f9c6292c2ead9947d94d1a7579a5、唯一parent=a1db8c114dec0ab69d69a5576e153a7f868cba0e；确认git cat-file能读取tree和必要blob，不只是git show一个文本字符串。
- 核对 --show-toplevel、--git-common-dir、--git-dir、object-dir全部归属于唯一新clone；没有objects/info/alternates、无共享common-dir、无浅/partial/promisor状态、无环境Git目录指向旧保护树。路径比较只针对**新的**安全目录及已知禁止路径字符串，不去读取或stat原旧树来制造“保护证明”。
- 任何身份不匹配立即STOP，不能通过修改分支/重建tree/添加对象或改变期望SHA救PASS。

**A3：签出并核实际磁盘字节（仅新clone）。**
- 仅在A2 PASS后，本地设置core.autocrlf=false；在新clone内用受控sparse checkout限制到src/ch5_two_asset_hank所需源码范围，并checkout --detach固定commit。必须核实际退出码0和新HEAD精确等于冻结commit。
- 对九份列出的源码逐一取得固定commit的 git ls-tree / blob id，并由PowerShell/Get-FileHash和**无 -w 的只读 git hash-object --no-filters**读取新clone磁盘实际原字节，逐项比较Git Blob准确一致，记录实际SHA256及字节数。不得借Git tree的blob ID代替磁盘验证；不得对CRLF自动修正或放宽匹配来救PASS。不得导入九份模块（__file__/loader真实性属于未来独立工程runner门）。
- 如有未跟踪副本、源文件未按精确路径签出、reparse/软链接、不可信过滤器、Git Blob/磁盘不一致、对象丢失或外部common-dir，fail-closed。仍保留原失败现场，不进行自动修复/retry。

**A4：静态结论与工程停点。**
- 仅当A0–A3全部PASS且资源/保护门均合格时报告 A_STAGE_OBJECT_REACHABILITY_VERIFIED；同时明确只是**source/object PRECONDITION**，不是Windows Git子进程audit/Job/timeout、runner完整I/O或任何HA科学PASS。否则 A_STAGE_OBJECT_REACHABILITY_FAIL_CLOSED，附准确最早失败命令、exit code、原始回执哈希和未验证项。
- 本任务完成后STOP；不得复用旧工程Python0/4启动后续Stage B–E。若未来需要工程Windows preflight，新预算和输入绑定须Owner再批准。

## 4. 本轮独立资源与失败扣账

- 总墙钟≤2小时；仅一次模型clone。模型远端顶层网络≤2（单个ls-remote + 单个正确branch clone）；**Stage A失败后没有追加fetch/retry许可**。额外GitHub安全脱敏交付可单独进行受界Git对象取用，但不得在此名义下再补取模型数据。
- Stage A本地显式Git身份/签出/源码核验命令建议≤32条（包含模型网络2条）；脚本辅助应通过PowerShell及Git原生命令，不启动Python或其他模型工具。Git内部spawn数量如未被单独instrument，必须标UNKNOWN，不凭外层条数谎称全局次数。
- 新scratch非Git工件（runner外壳不允许、本任务PowerShell脚本/最小日志/manifest/报告/外部账本/failed artifacts）累计≤16MiB；任一单文件公开前报告≤1MiB，正常日志应更小；写入前检查额度，错误raw bytes不得展开写入巨型异常文本，终态保留受界输出空间。**唯一模型clone加可选最小发布Git元数据工作区新增合计≤2GiB**，包括全部Git objects/index/checkout内容，不允许靠删除旧失败输出降账。
- 所有本次模型科学调用0、新Python进程0、工程runner0。原V010实施pytest4/6、driver1/4、HA1/26、selector1626、roots1642和先前两次单点preflight每次Python1/1 HA0及第一笔43519638B超旧32MiB 9965206B，全部不重置。本轮独立预算不回填、抵销或追加旧限额。
- 保护/时间/字节硬门、Git对象身份或可达性任何失败，STOP并封存，不能以更改scope、Git reset/clean或放宽科学合同取得表面PASS。

## 5. 唯一脱敏GitHub交付权限（本任务专属）

完成或失败后，交付唯一总报告 **V010_STAGE_A_MODEL_GIT_OBJECT_REACHABILITY_RECOVERY_RESULT**。须同时列远端ref和实际clone HEAD、commit/tree/parent、九份源码预期和实际Git Blob/磁盘SHA256/字节、独立 common-dir 和 alternates/shallow/promisor情况、真实Git命令return codes、大小时间与保护证据等级、未观测项。D盘私有回执保留LOCAL_ONLY，仅提交安全hash/匿名化的路径类别而非原始机器路径、原始argv或完整stderr。

**只允许创建并单次普通non-force发布全新review分支** review/v010-stage-a-model-ref-reachability-20261016，唯一parent必须是**本任务发行commit**（在签发后登记于动态TASK_CURRENT）；发布前确认同名分支不存在，不可force覆盖。仅允许2个GitHub公开文件：
1. versions/0.0.10/review_stage_a_model_ref_reachability_result_20261016.md（≤24KiB，完整安全摘要）；
2. versions/0.0.10/review_stage_a_model_ref_reachability_manifest_20261016.json（≤64KiB，九源结果、资源账/失败码、hash/UNKNOWN）。
GitHub发布所需task基线Git对象可在本轮全新隔离工作区**额外定向只读取得**，但只能为准备单父安全文档提交使用；必须另外记取物网络/对象字节、禁止额外模型ref补取，不得写main/治理分支/旧review或冻结模型。若发布准备会越预算/泄露私人信息，保持 LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED，不进行第二次push或强推。
- 发布后必须readback远端ref、commit、tree、sole parent、确切新增两文件blob/UTF-8 bytes；不能以本地提交存在自称远端已发布。
- GitHub不直接证明Windows本机dirty保护、日志完整、实际进程次数或最终输出字节；未公开本机receipt证据一律CODEX_REPORTED_WITH_LOCAL_RECEIPTS，不升级网页独立实测。

**最终停点：WAIT_ASTRA_V010_STAGE_A_GIT_OBJECT_REACHABILITY_REVIEW / STOP。**

原科学保护永久有效：A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、C8 A–D REQUEST_ONLY、原8dirty/index/common-dir、V011 NOT_STARTED。GitHub同步不等于本机QMD/Basic Memory同步。
