# 第五章 CURRENT · V010 M1 V1.3 工程闭环长任务

更新：2026-10-17。Owner明确要求停止单报错微任务，采用一次完整M1长任务实施。最新ACTIVE以此处为准，所有较旧任务均已STOP。
**WORKFLOW=V1.3__CONSOLIDATED_LONG_TASK_ACTIVE**。
**RESEARCH_VERSION=V010/V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_M1_V13_CONSOLIDATED_ENGINEERING_EXIT**。
**FIXED_ISSUE_COMMIT=6f4df14b62fb7f5406b3df97707848aab21edf71；TASK_BLOB=762ad617365a82bc1fee2b0cc986b3e816edc883**。
**TASK=[本轮唯一冻结M1工程长任务](versions/0.0.10/m1_v13_consolidated_engineering_exit_task_20261017.md)**。
**STOP=WAIT_ASTRA_V010_M1_CONSOLIDATED_ENGINEERING_REVIEW / STOP**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False；Results FALSE**。

**CLASS=ENGINEERING_ONLY_LONG_TASK__SINGLE_CONCENTRATED_M1_DELIVERY**。
**SCIENTIFIC_PLAN_BLOB=85138d8859d53295262fe13bf5bc277bca95ed3f**。
**FROZEN_MODEL_COMMIT=94de4501dec051b969bee9d852eba2d4591f30ef；MODEL_TREE=205eab47c4e4f9c6292c2ead9947d94d1a7579a5**。
**NEW_ENGINEERING_WALL_MAX8H__PYTHON_PROCESSES_MAX24__NON_GIT_ARTIFACTS_MAX128MIB**。
**RAW_FROZEN_GIT_SOURCE_STREAM_MAX16MIB__DIAGNOSTIC_LOGS_MAX1MIB_PER_CHILD__SEPARATELY_METERED**。
**NEW_SCIENTIFIC_HA/HJB/KFE/SELECTOR/ROOT/GE/IRF/REAL_C8_0__NO_MODEL_SOLVE**。
**OPTIONAL_REVIEW_REF=review/ch5-temp-v010-m1-consolidated-20261017**。

本次范围一次涵盖**固定70份raw源码身份/三非空init、Git raw字节通道与日志计量分离、单写者原子ledger、Windows平台元数据/NumPy导入工程兼容、真实canonical import、九模块source、五Git child的Windows runner/Job/PIPE/reader/reap与必要负例、最终真实first/final和可选脱敏远端审阅**。Codex对任务内普通工程E1问题可自主修复和复测，无通用PowerShell命令微额度或focused回归轮次上限，实际执行仍在8h/24 Python/128MiB等总额与保护边界内；必须使真实M1结果而非工具修复本身成为交付重点。

对上一[Git源码管道硬超限主审](versions/0.0.10/m1_v13_platform_syscmd_ver_local_only_output_cap_fail_closed_review_20261017.md)的`FAIL_CLOSED/LOCAL_ONLY`不追改：旧管道1,106,482B高于旧262,144B限额844,338B且未及时STOP，台账并发覆盖与文件冲突保留；旧NumPy→platform._syscmd_ver→未经授权Popen来源已有本地报告，adapter未具可信全部语义/原生canonical未通过。新任务只针对工程import**实际消费的版本元数据字段**允许有来源、受控、有证据的最窄适配，必须标`SCOPED_ADAPTER_ONLY`，不得修改冻模型/stdlib或开放任意Popen/网络，不等同科学PASS。此前N13 4.039s本机正向仅在Job/reader语义变更时需本轮重测。此前所有STOP预算不得结转，旧first/raw与未知历史源证据不可追补。

原论文主线原MATLAB corrected两资产HA/HJB/KFE→多省手动有界顺序→GovInv收益界乘0.9/1.1和Zt→冻结GDP每省误差≤1%独立验证→原lagged-NKPC递推，目的地工资税一次、same-S/上一完整轮raw ra0、家庭人均/省财政总量与三劳动账、phi_max=.3、20×20×2原数值标准照旧。Owner corrected HA单点UNTESTED；M1实质工程closed与M2稳态/M3响应/M4成果均尚需真实证据。原D盘8dirty/index/staged/untracked/ignored、外Git common-dir、独立C SSD既有备份、全部旧失败scratch与real C8/2017/2018/B3/V009资产保护不变。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、real C8 A–D REQUEST_ONLY仍冻结。
