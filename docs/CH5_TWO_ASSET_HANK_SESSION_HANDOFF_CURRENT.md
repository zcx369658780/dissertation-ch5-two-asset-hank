# Chapter 5 当前交接
更新：2026-09-07。仓库：zcx369658780/dissertation-ch5-two-asset-hank。

Owner为最终科学authority；ChatGPT为Reviewer、路线协调者、任务发布者；本地Codex为有界Builder。Owner已授权Reviewer验收后将范围内提交纳入main，并在无实质科学选择时自动发布下一完整有界任务，无需常规重复确认。
当前从工作模式接入普通对话；Reviewer只做GitHub审阅/文档发布，不因此启动本地模型。“Astra工作方式”不意味着provider或本地配置已修改。

## 恢复live authority
Fresh读取main，再读AGENTS、规则索引、当前状态、路线及exact task。最新接受证据锚点b2d7a814039a585b696d8cc5079b8b9865017501，不是假定永不变化的main。
不要混入deep-learning-hank；旧R5/R1A只作历史。项目源附件可能旧于GitHub，不能覆盖live文档。

## 已完成且不得重跑
治理迁移及本地同步已处理。首轮25e5db9已接受53/53；轨迹dedd0f8已接受诊断但不是完整parity。
策略/算子b2d7a81已L3接受：M24/P24/M143_FINAL各38/38，P32为36/38，首差V1、随后统计量。P32 M/RHS容差内一致但不逐位一致，不能只归因于solver或认定公式错误。
算子峰值已追到未截断transfer导数分母及平方cost。两端存在负非对角元和边界泄漏；终点也仍有18负元/15泄漏位置。小残差和stop通过不解决算子有效性。
MATLAB143步收敛，Python500步未收敛；Python尾100步持续切换。四状态每端4次调用/更新/求解、重试0，下游0。
Reviewer本轮读了提交/相关代码/JSON，未重读Windows数组、未独立运行8项测试、未运行模型；外部核验和测试通过按Builder证据记录。完整验收见docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_ACCEPTANCE.md。

## 当前任务
唯一active：tasks/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.md。
预定分支：codex/ch5-call725-frozen-linear-system-20260907。
已发布，尚未收到完成报告。目标为两套P32保存线性系统的交叉求解、二进制幂行缩放诊断和残差归因；正常8次直接求解，每端4次，符合条件重试至多每端1次。HJB/长轨迹/下游0。精确条件以task为准，不把行缩放探针当作生产修复。
收到新提交后按风险验收；无实质Owner决策则纳入main、更新CURRENT并续发任务，Codex启动prompt使用单一代码框。不要把旧dedd0f8或b2d7a81重复消息误认为新任务结果。

## 本地工作与路线
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001。原D:\ResearchCode\dissertation-ch5-two-asset-hank及70未跟踪文件保留；不reset/clean/stash/强制覆盖。
旧轨迹与四状态证据目录见当前状态。新task用fresh无覆盖证据根，禁止从聊天近似值重建输入。
Codex UI可仍在D:\Zotero-Analytical-Workflow，但所有repo命令显式使用Chapter5目录；切cwd不保证清空预加载指令，遵守实际平台/全局规则，不改Zotero配置。
年度口径分开：旧runtime-cache15/15历史接受；修正Owner-A13/14返回PASS、2018失败，完整覆盖未接受。
后续为线性数值归因与legacy算子问题定位→有依据修复/稳定化→恢复修正2018及年度→冻结真正动态规格→动态集成/稳健性/Results。不把顺序比较静态称为真正IRF，不编造论文完成百分比。
