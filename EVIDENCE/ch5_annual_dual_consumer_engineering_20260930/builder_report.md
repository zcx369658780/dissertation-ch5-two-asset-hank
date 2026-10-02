# Annual dual-consumer engineering: Builder candidate

2026-09-30。仅工作树 D:\ProjectTemp\c5k1bturn56；HEAD 75cee92b1ad9e5cb6fc069bca892213838ffdddc。任务 raw SHA256 1B6998A66BF206A969D29A81DF76899B9DC0DDA6F5119A110152570C6AAD3A2C。入口确认新源/test三路径均不存在；prechange中除Work本次更新的CURRENT/TASK外33项身份全部匹配。Owner原AGENTS修改、全部既有dirty/untracked文件保留。备份依据既有backup_receipt；未读取其Zotero目录目标。项目归属依据既有Owner UI，不宣称API提供projectId。

## Candidate

仅新增 annual_observed_labor_context.py、独立annual_observed_labor_diagnostic/integration.py、直接加载的test_ch5_annual_observed_labor_context.py，以及本任务证据。未stage/commit/push。

新标准库context使用原封不动、raw-hash认证的accepted helper。显式年度制备仅一次调用build_annual_labor_wedge；同年消费者沿调用链复用同一context与同一tuple-of-tuples。没有年度全局cache，也不从states重构系数。标准Python模块导入缓存只复用helper代码类，不缓存年度或数据。每个context的不可变seal绑定原wedge身份、年份、轴、来源、价格口径、provenance与inactive状态；公开构造、dataclasses.replace、伪对象及可变系数在spies前拒绝。

新integrate_turn保留旧K1B入口十个positional参数，新增必填年度/provenance/DI参数；绕过旧_one_turn_inputs，不使用Yt/Lt。逐行state必须带province_index/source_province_name且匹配年度轴。劳动重建与firm_stage之后的复合工资共享exact phi对象；MigrationLaborInputs/composite kwargs与实际旧接缝静态对齐。其他参数、distance、shares等透传，不改变旧代码或方程。firm_stage只是opaque synthetic spy边界，**没有实现资本/C1/firm流程，也没有接入完整outer runtime或历史runner**；tuple向真实科学array的适配未激活。

生产raw-byte认证入口固定manifest/attribution/audit/GDP/population/adapter/helper七项accepted pins，无caller override；全部认证先于JSON解析/数值转换。代码将记录从authenticated audit绑定到canonical31province index/name、2017观测，保留两源capture/hash与方法归属。此任务没有调用其真实成功路径、读取真实audit/display/panel，也没有生成实际矩阵。prepare_observed_context在认证后仍显式ProductionBlocked；**真实observed年度数值carrier尚未制备**。生产消费者阻断，model_activation=False。

## Exact new test budget

同一命令：python -B tests/test_ch5_annual_observed_labor_context.py。初次14项中13PASS、1ERROR、exit1，原因是静态源读取使用Windows默认GBK；原始输出保留。Repair1修正UTF8并落实具体review元数据/不可变provenance问题：15PASS/exit0。Work随后发现公开replace可同时更换wedge/phi，Repair2增加每个制备seal及改系数/空provenance反例：16PASS/exit0。1初次+2修复额度全部消耗；没有pytest、旧测试重跑或进一步执行。

虚构3省不对称fixture测试方向、diag1、上下界、同年改变states复用、两消费者同对象、不可变mutation、年份/轴/来源/价格/hash/伪对象/replace/错序states先于spies拒绝，以及actual旧签名/keys静态对齐。测试不调用真实劳动、工资、firm或model。

三位独立具体只读helper分别完成接缝映射、raw-pin/provenance检查和独立风险审查；实现与review分开，全部测试由主Builder执行。advisory记录另存；其意见不替代Work ACCEPT/REJECT。

科学/模型/校准、实际observed矩阵、真实adapter/audit/panel读回、wrapper/preflight/--execute、主机/API/隔离探测、下载、新reports根均0。旧预算没有重置，两个C9实际账本仍CALL_LEDGER_UNRESOLVED而非0。C9PAUSED、ObjectiveA RETAINED、Results eligibilityFALSE。

停在未提交Builder candidate，等待GPT Work独立ACCEPT/REJECT；不自行接受或签发科学继任。
