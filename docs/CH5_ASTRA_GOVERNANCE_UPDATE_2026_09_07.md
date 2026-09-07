# Chapter 5 治理更新记录
日期：2026-09-07。
Owner 已批准前轮审阅建议，授权直接更新 GitHub，并要求完整项目源 ZIP 和本地 Codex 同步 prompt。
修订标识：CH5_ASTRA_WORKFLOW_2026_09_07。

## 发布范围
更新根 AGENTS、当前规则入口/角色/工作流/验收/路径保护/MATLAB及Python诊断/路线/交接规则，更新当前状态及唯一多省份路线，发布本地文档同步任务。
项目源中的研究证据与引用规则保持原文纳入当前索引。
未修改已完成任务、历史科学报告、生产源码、测试、配置、保护 MATLAB 或任何运行输出。

## 主要改变
- 强制逐小 gate 改为完整工作单元及任务内部检查。
- 工程修复、普通检查重试和报告补全在已授权范围内连续完成。
- 科学调用预算预先明确、失败调用照实计数，历史预算不追溯重置。
- GitHub 同主题多文件原子发布并统一核验；无关 main 变化不自动阻塞。
- 正式输入/输出不可覆盖；允许开发脚本、草稿和 CURRENT 文档在 task 范围内更新。
- 只核验与结论相关证据，不把缓存清点当作科学验收。
- 纠正 R1A、旧 one-asset R5 和过期 MP1“下一步”状态。
- 冻结 post-boundary vb 为主比较、pre-boundary 为诊断的表示契约；不改变公式或容差。
- 本地任务仅同步仓库内文档及适用 instruction，不修改全局模型设置。

## 科学证据依据
先前独立审阅已读取 live main e98bfad214b0c85005fac2ce23b1e4585a20e634、四份原有 CURRENT repo 规则、AGENTS、近期 task/report、当前源码导数片段及完整仓库树。
最新 forensic 的提交只新增其报告。接受的是 repo/commit 级报告结论；Windows 原始 MAT/NPZ 并非本会话直接读取。
治理变更不宣称完整首轮、多轮或经验 stationary parity 已接受。Results eligibility 保持 FALSE。新科学调用为0。

## 历史材料
旧报告和任务保持原貌。新规则只在未来有效任务中使用，不追溯扩权。
旧 R5 与 R1A 项目源退出活动上下文，Git 历史保留。原论文 PDF 和文献不属于本次替换对象。

## 核验方式
发布前检查文档链接、当前口径、路径清单和科学源未变；发布后比较预期文件 blob 与 commit tree，核验 main 指向发布 commit。
最终 commit 由发布回执记录，避免文档自引用本身的 commit hash。
