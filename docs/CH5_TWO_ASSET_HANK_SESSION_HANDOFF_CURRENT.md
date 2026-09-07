# Chapter 5 当前交接
更新：2026-09-07；迁移：GPT-5.6 Sol reviewer → 用户选择的 GPT-6 Astra 工作方式。

仓库：zcx369658780/dissertation-ch5-two-asset-hank。
角色：Owner 最终科学 authority；Reviewer 路线、任务与验收；Codex bounded Builder。
模型名称表示用户选择，不说明本地 provider/config 已被切换。

## 启动
读取 live main 的 AGENTS.md、规则索引、当前状态及指定任务。科学证据 checkpoint 为
`e98bfad214b0c85005fac2ce23b1e4585a20e634`，不能假定未来 main 仍是此值。

## 已完成交接裁决
最新 raw-vb forensic 在 repo/commit 范围 L3 接受；处理前/后保存时点不同解释 40/40 差异。
选择 post-boundary derivatives 为主比较对象，pre-boundary 为诊断对象。不需要再次询问 Owner 名称含义。
没有证据支持因此修复生产导数；首轮随后已在25e5db97a0239d956d572359db5835cec945962f完成并验收，53/53通过；多轮parity仍待建立。

## 新工作方式
一个 task 一个完整问题；任务内允许工程修复、相关验证、预算内执行和报告。复用未变化证据；只在具体科学风险或授权边界处暂停。
禁止预算重置、保护源改写、事后调容差和 Results 越界。
旧 forensic 的 Owner naming 建议被新路线规则明确取代；历史事实不改写。

## 当前任务与下一步
本地同步已 L3 接受，报告 commit：d2f3e6e7cc21fffe8807f577ec2262bb77afdc07。
工作目录：D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001。
可在原 Codex 会话明确切换命令工作目录来继续；仅切换 cwd 不保证清除会话预加载指令，仍需遵守实际平台/全局规则。Zotero 的限定项目历史指令不是本仓库科学 authority。
若 UI/权限必须另开项目，使用此既有目录，不创建新模型仓库；读取此交接及 live task 即可恢复必要状态，旧会话保留。

当前任务：tasks/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY.md。
多轮诊断提交dedd0f8e5fa894b83c8b20e522d66893e7b6b377已验收；最早第2步差异在共同状态复查38/38通过，后期仍待解释。MATLAB143步收敛，Python500步未收敛。每端2次调用，分别144/501次求解，retry0。
下一步复用已保存轨迹，分析策略/算子增长，四组指定共同状态单步对照；不再重复长轨迹。调用预算仅见新task。
Owner 授权：Reviewer 验收后无实质决策即可续发下一任务；减少重复审核，保留真实数值标准与保护源。
完整年度进度见当前状态：旧 runtime-cache 口径15/15已接受；修正 Owner-A 口径13/14年返回PASS，2018仍阻塞完整覆盖。不要把 raw-vb 伪差异解释当作完整模型通过。
