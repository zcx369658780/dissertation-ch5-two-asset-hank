# Chapter 5 当前规则入口
更新：2026-09-08；治理修订仍为CH5_ASTRA_WORKFLOW_2026_09_07。

## 适用与优先级
适用仓库：zcx369658780/dissertation-ch5-two-asset-hank。这些文件同时供Codex+Zotero+Obsidian科研的Chapter5项目源使用，不自动修改其他仓库。
平台/系统限制始终生效。仓库按当前AGENTS、此索引、有效task及相关科学契约执行。
新规则替代强制逐小gate、每次retry另发单、草稿一律不可修订等旧流程，不追溯增加历史task权限或预算。旧R5/R1A和过期CURRENT附件不能覆盖当前两资产路线，实质科学冲突交Reviewer/Owner处理。

## 最小读取
每次任务读取AGENTS、此索引、exact task和当前状态，随后按需读相关规则及证据。已读且身份未变者可复用，不强制全历史审计。

## 规则清单
以下路径均相对project_rules/：
| 文件 | 何时读取 |
| --- | --- |
| PROJECT_RULE_OVERVIEW_CURRENT.md | 项目定位/角色 |
| PROJECT_RULE_CODEX_GITHUB_WORKFLOW_CURRENT.md | 任务执行 |
| PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md | 本地写入/运行 |
| PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md | GitHub操作 |
| PROJECT_RULE_ACCEPTANCE_LEVELS_CURRENT.md | 验收 |
| PROJECT_RULE_PROMPT_AND_HANDOFF_FORMAT_CURRENT.md | prompt/交接 |
| PROJECT_RULE_MEMORY_AND_PROGRESS_SUMMARY_CURRENT.md | 状态更新 |
| PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md | MATLAB工作 |
| PROJECT_RULE_PYTHON_MODEL_REBUILD_DIAGNOSTIC_GATES_CURRENT.md | Python工作 |
| PROJECT_RULE_DISSERTATION_CH5_ROUTE_CURRENT.md | 科学路线/比较口径 |
| PROJECT_RULE_RESEARCH_EVIDENCE_AND_CITATION_CURRENT.md | 文献及正式论文claim |

当前状态：docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md。
路线正文：docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md。
当前交接：docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md。
当前active Builder任务：tasks/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT.md。
状态：OWNER_DIRECTED_PRICE_BOUNDARY_AUDIT_ACTIVE__ORIGINAL_ALGORITHM_RETAINED。

Owner于2026-09-08要求保留原算法及a_bar，先检查各省rah/wjt是否越界或触界，并诊断原自适应机制。新任务仅授权保存证据读取、标量诊断、检查及报告，新增模型/求解预算为0；缺轨迹不得自行重跑。
此前tasks/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC.md已完成并验收，candidate15f51be9733b5043e738d3e522b97554e95902b9。其D1-D3修复target没有被Owner采纳，暂缓，不实施。过去“等待采纳后才能有successor”的未来路线由本次Owner指令取代；原诊断证据不改写。
普通对话发布不等于已启动本地Builder。完整轨迹parity、算子有效性、修正2018及Results均未由本任务接受。
