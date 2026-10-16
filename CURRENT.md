# 第五章 CURRENT：V010 Windows工程预检阶段A失败，已独立验收并停止

更新：2026-10-16（Asia/Shanghai）。
**STATUS=ENGINEERING_PREFLIGHT_FAIL_CLOSED__INDEPENDENT_REVIEW_COMPLETED__NO_ACTIVE_EXECUTION_TASK**。
**ACTIVE_TASK=NONE**。
**NEXT_GATE=WAIT_OWNER_FRESH_A_STAGE_GIT_OBJECT_REACHABILITY_AUTHORITY / STOP**。

前一任务`V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT`已由Codex完成失败封存，不得按原发行任务自动重试、补fetch或延用未消耗的工程Python许可。[本会话Astra独立审议](versions/0.0.10/runner_io_engineering_preflight_fail_closed_primary_review_20261016.md)，Git blob `7ba0991b76bc2d5304f78c7e7ddb5d0c8f746b96`。Codex脱敏review candidate [`416cff6c00d2b865c3e9dda4088242d2b80969ce`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/416cff6c00d2b865c3e9dda4088242d2b80969ce)，tree `1d5bc390774d68ea619f6ad263c99d0090486b37`，sole parent为前一task发行commit `343c22132deb23ba6d913d70e132b43a00b95f1d`，仅增加3项允许Git文件。

**失败定位**：隔离clone错误限定`--single-branch --branch migration/astra-workflow-20261012`，没有取得模型候选分支；本机`checkout --detach 94de4501dec051b969bee9d852eba2d4591f30ef`报告exit128、unable to read tree。Astra已从远端实际核验：`refs/heads/codex/ch5-v010-matlab-first-20261015`指向该固定commit、其tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`存在且可读取。可支持`A_STAGE_GIT_REF_SCOPE_FAILURE`工程解释，不是模型科学失效。D盘实际Git对象数据库未由网页独立读取。

**工程/科学**：本任务Python0/4、HA0、真实runner0/2、准备Git显式命令5次/最后exit128与原树保护未访问等属于Codex私有回执级别；69个用例的`NOT_EVALUATED`已经GitHub静态独立核对。Stage B–E没有执行；`FULL_RUNNER_IO_CLOSURE=BLOCKED`；单点corrected HA从未真正运行，`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`。最终工程artifact 14,983,882B/16MiB、clone 497,029,770B/2GiB是Owner转述的本地回执值，网页未独立计算文件实际字节；原进程余量不自动跨任务转移。

原V010计划commit`bf091da33d59293f147d52c11580327d3ac2a85d`/blob`85138d8859d53295262fe13bf5bc277bca95ed3f`；模型candidate `94de4501dec051b969bee9d852eba2d4591f30ef`、single-point input manifest blob`c23d331bed34e5ca478324cdc05034609ecb91b7`不改。原模型科学主线、GovInv收益边界×0.9/1.1、目的地工资税一次、家庭/firm劳动和财政分账、same-S、lagged raw-ra0、原lagged-NKPC递推保持。旧V010实施账pytest4/6、science driver1/4、HA1/26、selector1626、roots1642和前两次单点预检各Python1/1 HA0、第一次存储超额永久保留。

**安全及项目资格不变**：A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、原8dirty/index/staged/外Git common-dir/untracked/ignored、V011 NOT_STARTED。GitHub不代表本机QMD/Basic Memory同步。后继若需Git补取或新工程preflight，必须Owner另行明确授权并重新冻结范围和新资源，不得未经决定运行。
