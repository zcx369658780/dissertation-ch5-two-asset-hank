# Chapter 5 当前规则入口
更新：2026-09-09；治理修订仍为CH5_ASTRA_WORKFLOW_2026_09_07。

## 适用与优先级
唯一活动仓库zcx369658780/dissertation-ch5-two-asset-hank；这些规则不自动修改其他项目。平台/系统限制始终生效；仓库按当前AGENTS、此索引、有效task及相关科学契约执行。旧R5/R1A和过期CURRENT附件不能覆盖live状态。
完整任务取代逐小gate/任意失败另发单；不追溯扩大历史预算。实质科学选择由Owner裁决。

## 最小读取与规则清单
每次读取AGENTS、此索引、exact task和当前状态，其余按需。已读且身份未变者可复用，不强制全历史审计。
以下路径均相对project_rules/：
| 文件 | 使用场景 |
| --- | --- |
| PROJECT_RULE_OVERVIEW_CURRENT.md | 定位/角色 |
| PROJECT_RULE_CODEX_GITHUB_WORKFLOW_CURRENT.md | 任务执行 |
| PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md | 本地保护/证据 |
| PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md | GitHub读写 |
| PROJECT_RULE_ACCEPTANCE_LEVELS_CURRENT.md | 验收证据范围 |
| PROJECT_RULE_PROMPT_AND_HANDOFF_FORMAT_CURRENT.md | prompt/交接 |
| PROJECT_RULE_MEMORY_AND_PROGRESS_SUMMARY_CURRENT.md | 状态更新 |
| PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md | MATLAB诊断 |
| PROJECT_RULE_PYTHON_MODEL_REBUILD_DIAGNOSTIC_GATES_CURRENT.md | Python诊断 |
| PROJECT_RULE_DISSERTATION_CH5_ROUTE_CURRENT.md | 科学路线/比较口径 |
| PROJECT_RULE_RESEARCH_EVIDENCE_AND_CITATION_CURRENT.md | 引用/论文资格 |

## 当前入口
状态：docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md。
路线：docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md。
交接：docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION.md。
状态标记：RAH_0P07_SENSITIVITY_ACCEPTED__ZERO_SOLVE_KFE_MASS_BALANCE_ACTIVE。
Builder默认gpt-5.6-sol / medium；本任务无例外。Owner授权Reviewer在后续任务中指定有理由的模型例外，不授权自动修改provider/global配置。

最新接受e3176e9352b4f7e155c91891a4cabdd517e9e232：精确单因素.07原生初始化下HJB26步收敛、KFE/聚合返回；未修改稳态残差3.4540415243199343、upper-b外向29格、末次HJB算子21负非对角元仍阻塞有效稳态。接受的是敏感性实验与结果，不是MODEL_PASS或生产修复。
原.07任务、原参数725次前缀和价格审计均已完成，不重跑，不继承旧预算。新任务只使用现有.07数组定位被替换方程残差、计算密度加权边界流和质量收支；新增初始化/求解/HJB/KFE/模型调用全部0。发布不代表本地已启动。
保持原算法、a_bar和生产ramax；D1–D3未采纳/未实施。新任务不改矩阵、不移pin、不裁剪密度/速率、不扫利率、不恢复年度。所有进一步边界/校准/生产选择另行明确。Results eligibility=FALSE。
