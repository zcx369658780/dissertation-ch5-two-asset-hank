# 2018回溯数据适配器：独立工程候选

Owner已于2026-09-30确认2018年回溯诊断，使用本次采集的修订后2017 GDP/年末人口，只更新劳动系数来源，不全量重新校准。本轮仅完成新独立数据适配器候选，不接入模型、不运行模型、实际矩阵为0。

写范围：本证据目录（adapter.py、test_adapter.py、收据、报告、review、旧任务副本），TASK_CURRENT/CURRENT。现有src/tests、数据表、原面板、原始XLS、Owner AGENTS及受保护报告不修改。父HEAD75cee92b1ad9e5cb6fc069bca892213838ffdddc；HEAD:src00682b2e1a7ba23665f6e16f6acf48ad35874883。

适配器只用标准库；接受确切audit JSON路径及期望SHA256，显式target_year=2018和31项省份(index, source_name)顺序。按源名连接、省份标识保留原面板1—31的对应，不凭网页行号赋标识。校验完整31省×2015—2018唯一键、positive finite数值和严格年份；读取31项2017原始单位GDP/人口，不生成q或phi。冻结输出记录、顺序、来源SHA256及采集时间。保留retrospective_revised、year_end_resident、current_price_supported_exact_binding_pending、release_date=None、price_verified=False、model_activation=False，拒绝将其直接视为可激活 observed binding。不得导入helper/model。

验证预算：一个初始纯虚构fixture测试调用，最多一个仅为明确修复的追加调用；一次真实data_audit只读适配器readback。禁止helper重测、模型包导入、wrapper/preflight、HJB/KFE、GE、校准、实际phi、science及Git提交。必须独立只读工程审查；原数据/修订artifact/protected字节读前读后保持。C9暂停、Objective A保留、两次预算已消耗、实际账本CALL_LEDGER_UNRESOLVED、Results eligibility FALSE。
