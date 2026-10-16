# 第五章 CURRENT：Windows argv静态交付已报告，runner I/O仍BLOCKED

日期：2026-10-16（Asia/Shanghai）。
**状态：V010_WINDOWS_GIT_GUARD_STATIC_DELIVERY_LIMITED_ACCEPTED__FULL_RUNNER_IO_BLOCKED__WAIT_PRIMARY_DRAFT_FOR_INDEPENDENT_REVIEW。**

原任务`V010_WINDOWS_GIT_ARGV_PREFLIGHT_STATIC_FORENSIC_AND_GUARD_REPAIR`已由Codex交付并STOP；[最新Astra限定审议](versions/0.0.10/windows_git_argv_guard_static_review_20261016.md)已登记。Codex报告已有`V010_WINDOWS_ARGV_GUARD_STATIC_REPAIR_RESULT.md`与未执行`windows_git_guard_draft.py`、24项静态allow/deny用例、3文件33576B，且本轮Python/HA/HJB/KFE/selector/root/pytest均0，保护的旧对象hash不变。因报告仍位于Windows D盘且未作为附件上传，以上仅`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，Astra未独立审原代码或24例。

**核心证据更正**：原运行回执并未存实际Windows被审计argv，撤销旧“已经确认收到Windows字符串”的表述；只能说Codex报告在源码发现命令形态兼容/子命令权限约束缺陷。guard草案`STATIC_READY`是Codex自己的静态候选状态，不是runtime资格；完整runner I/O保护仍`BLOCKED`。

两次正式单点preflight各Python进程1/1已耗、HA均0；首次GBK预检日志43519638B/旧32MiB，超9965206B；第二次Windows守门拒绝、artifact117446B/96MiB未超额。冻结单点`rah=.0675,w_eff=15.5,rb=.02`仍**UNTESTED**，原source candidate `94de4501dec051b969bee9d852eba2d4591f30ef`工程限域接受和旧V010计划/manifest不追改。

**ACTIVE_CODEX_TASK=NONE**，本轮不再签发新Python或HA科学运行。最短下一门是读取用户上传的上述MD/py及24静态例，先由Astra独立检查guard和I/O缺口，再制定只含工程预检的有限任务/许可；之后才可能另行请求Owner科学HA许可。旧V010消耗账、原8dirty/index/common-dir/真实C8/B3、A16 FAIL_CLOSED、C9 PAUSED、window UNACCEPTED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE保持，V011 NOT_STARTED。
