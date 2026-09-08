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
当前active Builder任务：tasks/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY.md。
状态：OWNER_APPROVED_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_ACTIVE。

Owner于2026-09-08明确批准：独立Python安徽call725副本仅改rah .09→float('0.07')，使用该价格下的原生初始化，其余输入/算法/a_bar/HJB100步规则不变；复用已保存.09失败基线，不重跑基线。此批准取代前次验收和CURRENT中“尚待Owner选择”的未来安排，不改写历史报告。
新task独立授权一次初始化（最多800个原劳动根）、一次HJB（最多100次更新/直接求解）及自然到达时一次原KFE。科学进入后不重启；具体零进入启动重试、15分钟科学/90分钟任务上限以task为准。普通对话发布不自动启动本地Builder，尚未收到本任务执行报告。
最新已验收9d76747f48858a3e9289de8f284fffbc49aaedce的原参数prefix及此前价格审计均已完成，不重复725调用/年度表、不继承旧预算。D1–D3未采纳、暂缓；不改生产ramax、GovInv/Zt规则、solver或容差，不增加其他利率点。单户诊断不等于生产替换、普适安全率、完整parity、生成算子有效性、修正2018或Results接受。
