# Builder engineering report

日期：2026-09-30（Asia/Shanghai）。状态：BUILDER_CANDIDATE_PENDING_INDEPENDENT_WORK_REVIEW。

## 权限与交付

唯一工作树：D:\ProjectTemp\c5k1bturn56。任务：ISSUED__INACTIVE_ANNUAL_K1B_MIDDLE_STAGE_ENGINEERING__ZERO_SCIENCE。
TASK_CURRENT.md raw SHA-256：3CB8B6279F09286CACFCBCA0BEBB052123DC21B86A0BF5006BC08BF8084E5815。
已保存收据中的 HEAD：75cee92b1ad9e5cb6fc069bca892213838ffdddc；HEAD:src：00682b2e1a7ba23665f6e16f6acf48ad35874883。

实现与唯一测试属于第29条。第30条仅新增本报告及 builder_helper_advisories.md；未修改源码、测试或原始证据，未重新核查源码或运行测试。原后验收据的 active_turn=29 为历史记录，保持不变；本次交付后 completed30，由 Work 自动交接 Builder，不停止 Work，不自行新写任务。

## 候选行为与限制

middle_stage.py 提供 standalone NumPy/stdlib、显式 fixture dependencies 的 inactive bridge，无真实默认科学 callee。PreparedMiddleStage 绑定原 context、prepared array、mapping 和 ledger 身份，预先校验字段、轴、形状、有限数和正值条件。资本按冻结 shares 计算，保存守恒与 home-retained 核验；C1 与逐省 firm 仅调用显式 fixture callbacks，输出窄 immutable 结果。

integration.py 显式接入 prepared_middle_stage，要求 prepared array，并在 labor 前完成预校验。顺序为 labor → frozen capital → C1 → firms → wage；保留旧 API。两个消费边界传递同一个 immutable-bytes-backed master。

frozen shares 哈希使用 np.asarray(values,dtype='<f8').tobytes(order='F') 后 SHA-256 大写；形状另校验，与年度 C-order master backing 分开。pre-spy 与 run 入口各复核一次，不作单次 hash hook 声明。

唯一测试前，C1 原位篡改漏洞已修复：回调前固定 target/private tuple 权威，回调后核对 shape/value；残差、后续 firm 供给及最终结果使用原权威。两个拒绝测试覆盖 target/private 原位篡改，失败保留 C1 attempted1、阻止 firm/wage。正值、精确 float overrides、duck context 拒绝及 C1 exactly-one 核验也已在唯一测试前修正。labor counter timing 建议已撤回：历史行为在 nested factory/reconstruct 前增量，factory 失败仍消费 attempt，保留原语义。

仅 invented fixtures。2/3省 fixture 不证明 canonical31 原 C1/firm API 的运行兼容性、数值有效性或完整 outer 集成。原科学 consumers 未导入或调用。model_activation=False；Results eligibility=False。

## 已保存验证事实

来源：builder_execution_ledger.json、builder_postchange_receipt.json；本条仅读回既有记录。
唯一测试：43 PASS、exit0，同一进程包含旧30回归（含旧16）及13新测试。sole process=1；allowed=1；remaining=0；repairs=0；retries=0；测试后源码修改=0。既有年度/helper预算已消耗，不重置。

后验固定身份55/55匹配（58基线扣除 integration 授权编辑和两个 Owner 状态文件）。三候选最终哈希均与测试前绑定哈希一致：

| 候选路径 | raw SHA-256 |
|---|---|
| validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py | 82665113213CBC93286468A87069C8E014B64A12415A2B947FFA7EFDF3579F81 |
| validators/multi_province/annual_observed_labor_diagnostic/integration.py | BB594FA2A34340B330638459D1CF58524D405DEA2FB059194D43C3C79E48345A |
| tests/test_ch5_annual_k1b_middle_stage.py | 568CD9C4EFD119CEAF4A12F39DCEFDBE7B87C500096171A261932C6973EB4D8A |

本条未重算源码哈希；以上为已保存后验收据事实。保留 prechange_identities.json、backup_receipt.json、prior_task_current.md、执行账本、测试原始 stdout/stderr 与后验收据，不覆盖。

## 保持的边界与下一门

真实科学、模型、校准、生产调用、真实数值读回、真实 observed 矩阵、真实认证成功及转换均零/NOT_EXECUTED；科学输出根、下载探测、Git mutation 与发布均零。第30条没有 Python/import/AST/测试/科学/Git 操作，也没有访问其他仓库。已有 dirty/untracked 状态保留。

历史 leaf 读取 scope NONCOMPLIANT 保留，不改写；超范围读取的算法内容未用于实现。C9 PAUSED；Objective A RETAINED；两次旧 attempts CONSUMED；历史 CALL_LEDGER_UNRESOLVED；current_price_methodologically_attributed，price_verified=False，release UNKNOWN；Results FALSE。不重问 Owner，不创建科学继任。

助手 FINAL_STATIC_READY 仅为 advisory，非 ACCEPT。交付后停待 Work 独立 ACCEPT/REJECT；主代理不自接受。