# TEMP31 历史 Python 基线恢复与隔离修订候选｜任务记录｜2026-10-24

TASK_ID=CH5_TEMP31_HISTORICAL_BASELINE_RECOVERY_AND_PATCH_CANDIDATE_20261024_R1
MODE=OFFLINE_LOCAL_GIT_READ_ONLY__HISTORICAL_BASELINE_RECOVERY__ISOLATED_PATCH_CANDIDATE__NO_HA_RUN

## 冻结任务单与输入

完整冻结任务单文件名：CH5_TEMP31_HISTORICAL_BASELINE_RECOVERY_AND_PATCH_CANDIDATE_OFFLINE_TASK_R1_20261024.md
任务单 SHA256：9dab451c251ab2a5c07290e10e42d5bfed9335f228b878f8cd9bd2f34d8e2aaf
Owner 决策 MD SHA256：81f87d661ed21f760ee41d3839591eee6c4a4448f7b0e7eb69547dc854f6e750
离线输入包：CH5_TEMP31_HISTORICAL_BASELINE_R1_OWNER_INPUTS_20261024.zip
输入包 SHA256：b3422b5820b0faaa29d0c084348a722b728e84b2a3fb45f8d4add21ddcbd2322

## Codex 交付

run_id：156211a0597e49c4a40f37e5c9489812
actual_terminal：PASS_BOUNDED_HISTORICAL_BASELINE_IDENTIFIED__PATCH_CANDIDATE_READY__GPT_REVIEW_PENDING
交付 ZIP：CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_R1_OFFLINE_REVIEW_20261024.zip
大小：131442字节
SHA256：36143632a1497d3f7e470bafbc3155ac5d1937b104f02169e939ec7bf0e7959c

候选基线 commit：ba98537fd5ae004f0aa37d319865da1f1739e503
候选基线 tree：f432f0acb5d94e0f60cd976b74a236be883e0db3
Codex报告逐件核验390个原始 Git 文件；历史 HA 导出 SHA b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3 与入口 guard 匹配且 guard 未改。此身份结论等待 GPT/Astra 独立复核。

## 候选变更与测试摘要

- wage.py：综合工资一般公式幂次修正。
- firm.py：工资税收入候选改为税前工资率×企业劳动×tau，需独立核验单位。
- mp4b_python_empirical.py：目的地劳动厌恶偏好方向修正。
- 新增未接生产的隔离劳动/净工资桥与 GDP 目标残差帮助函数。
- c3.tex 公式修订草稿；c5.tex 原方向报告为正确，不机械反号。
- 合成2/3/31省；2,132项数值对照、5项预期拒绝；最大绝对差约1.82e-12、相对差约8.33e-16；便携算术重放1,046项。
- 历史184轮/5,704调用案例未重跑；正式 HA/HJB/KFE/outer/GE/IRF、生产 one_turn/firm 和真实31省校准均未运行。

## 当前裁决状态

Codex 已交付隔离候选，GPT/Astra 独立审阅尚未开始。不得把 Codex 自报 PASS 升格为科学接受、Owner 经济制度采纳或正式来源冻结。下一会话第一步应独立验收已上传 ZIP，审阅来源身份、候选 diff、w/tau 用途清单、数学/合成测试、TeX 草稿与 E3。无自动后续任务。

保护状态：FORMAL_V010=UNCHANGED；V011=NOT_STARTED；Results=FALSE；model_activation=False；REAL_GE=False；ACTIVE_TASK=NONE。