# TEMP31 工作地工资税独立路线状态 · 2026-10-25

```text
ACTIVE_TASK=NONE
CURRENT_ROUTE=TEMP31_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_AND_DESTINATION_INDEX
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=False
REAL_GE=False
FULL_RUNNER_IO_CLOSURE=BLOCKED
SCIENTIFIC_MODEL_CALLS=0
HA_HJB_KFE_GE_IRF=0
NEXT_TASK_AUTOSTART=FALSE
```

TEMP31 是独立临时研究/实现验证路线，与旧主线、正式生产来源隔离。历史候选基线 commit 为 `ba98537fd5ae004f0aa37d319865da1f1739e503`，tree 声明为 `f432f0acb5d94e0f60cd976b74a236be883e0db3`。Owner 已决定工资税按实际工作地/目的地省份归属；含目的地税的综合工资不得在 HA 适配层重复扣同一税率，劳动拆分按目的地 `tau_j` 索引。

状态来源：Owner 于 2026-10-25 明确授权的 `CH5_TEMP31_CURRENT_ROUTE_GITHUB_MILESTONE_BACKUP_TASK_20261025.md`，SHA-256 `57557ab46e10ef348d89c7cfc0f0c4ecf252bb1244dbafbd9c9aadabb3fb70b7`。Astra 裁决按该任务单接收并归档；本次 DOC_ONLY 备份不重新验收 R1/R2/R3 原包、独立报告或测试，不把 Codex 自检替代 Astra 接受。

## 三轮里程碑与分层裁决

### R1 历史 Python 基线候选

- run_id：`156211a0597e49c4a40f37e5c9489812`
- ZIP：`CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_R1_OFFLINE_REVIEW_20261024.zip`
- 原件身份：131442 bytes；SHA-256 `36143632a1497d3f7e470bafbc3155ac5d1937b104f02169e939ec7bf0e7959c`
- 本任务单转述的 Astra 独立裁决：`PASS_BOUNDED`
- 范围与限制：Astra 对工资幂局部推导、目的地偏好方向及工资税财政项作有界独立审阅；E3 与生产接口仍阻塞，正式来源未冻结。

### R2 工作地工资税单次应用

- run_id：`38615efcc645480183d8071526c5dd46`
- ZIP：`CH5_TEMP31_E3_WORKPLACE_WAGE_TAX_SINGLE_APPLICATION_R1_OFFLINE_REVIEW_20261025.zip`
- 原件身份：94755 bytes；SHA-256 `01a402aef2b625a068c48c9fe895a52a745ee39ee878a8a209477e8463180e82`
- 本任务单转述的 Astra 独立裁决：`CHANGES_REQUIRED_BOUNDED_SCOPE_GAP`
- 范围与限制：Astra 认为 HA adapter/初始化重复扣税修复局部有效，但劳动拆分仍使用来源地税率；该历史退修裁决永久保留。

### R3 目的地税率索引

- run_id：`1ae1549d867a43239d75a619c3d39208`
- ZIP：`CH5_TEMP31_E3_WORKPLACE_TAX_DESTINATION_INDEX_MINIMAL_PATCH_R1_OFFLINE_REVIEW_20261025.zip`
- 原件身份：41367 bytes；SHA-256 `64bf19f235692cfd338356bfb08ec653cb9d3ac18875974985fd9c08204a3ef6`
- 本任务单转述的 Astra 独立裁决：`PASS_BOUNDED_DESTINATION_TAX_INDEX_PATCH__FORMAL_INTEGRATION_BLOCKED`
- 范围与限制：Astra 有界审阅通过目的地索引修复；核心函数和限定范围直接调用者采用 tax_by_destination[destination]，10 项 GREEN、6 个预期 RED 失败；历史整轮 fixture 及正式集成仍待认证。

## 当前进度的适用范围

“进度超过旧主线”仅指 TEMP31 的隔离工程验证进度已经超过旧主线原先停留阶段。它不表示完整财政、真实模型调用闭包、正式科学结果、生产就绪或正式来源冻结已通过。旧主线的历史记录、STOP、PENDING、科研合同及关闭预算全部保留，不追溯改写。R3 解决的是 R2 已定位的目的地税率索引缺口，不能把 R2 的历史 CHANGES_REQUIRED 改写为完整通过。

已完成的是候选基线恢复、工资税单次应用隔离修订、目的地税率索引隔离修订及相应有界审阅记录。R2 单次扣税和 R3 目的地索引均处于隔离候选层；本文件不将两次交付拼成正式运行闭包。

仍未闭合：历史整轮 fixture 的新口径认证、正式集成与生产 HA 接线、真实生产调用闭包、最终价格/末次 batch 规则、完整财政、工资/劳动/效率/模型期及 HU/期间单位、指标选择、sigma 的经济收受方和 Owner 正式来源接受。

## 停止门与下一阶段

下一阶段方向为“历史整轮 fixture 更新与受界集成验证”，尚未签发独立离线任务单、尚未启动。必须先完成本次远端提交与五文件回读，经 Owner/GPT 复核身份，再由 GPT 顾问签发新任务。不得因本次备份成功自动执行、冻结正式来源或恢复旧预算。历史 2009 年 184/5704、31/31 收敛属于旧合同下的历史案例，不能自动视为新税率口径通过。

本次只允许五份治理文档的正常 GitHub 新增/更新，不修改科研源码、测试、数据、旧候选、历史 commit、Issue/PR/Review 或保护区；不创建分支、不清理历史对象。交付本地脱敏回执后立即 STOP。

## 导航

- [当前状态](../CURRENT.md)
- [当前任务](../TASK_CURRENT.md)
- [项目记忆](CH5_PROJECT_MEMORY_CURRENT.md)
- [文档索引](DOC_INDEX_CURRENT.md)
