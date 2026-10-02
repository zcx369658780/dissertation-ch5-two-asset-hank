# Builder engineering report — inactive public data-only entry

2026-09-30 Asia/Shanghai；第4条完成唯一测试，本次第5条仅补交报告与最终交付收据，交付后 completed5。结论：BUILDER_CANDIDATE_PENDING_INDEPENDENT_WORK_REVIEW。不是 Work ACCEPT，也不是实际数据运行许可。

Work报告 App read_thread 的第4条状态因 Selected model at capacity 为 failed，但 sole_process_result.json 与原始 stderr 已保存65PASS/exit0。这个 capacity 事件没有取消已发生的测试，也不重置预算。所有原执行/后验记录 active_turn=4 保留为历史；本次仅文档与行政交付，不新增test/Python/import/AST/model/science/真实数据执行，不再修改候选源代码。

唯一工作树 D:\ProjectTemp\c5k1bturn56。测试任务原始 SHA256：85E91A9BC2AA7154C2DF849D9DE076FD2958EE179C50BEE768400A620CFDFE29，精确快照保存在 tested_task_current.md。恢复附录沿用原工程唯一进程预算；暂停前测试启动0，恢复后仅启动1次，未新增预算。

## 三份候选与实现

| Action | Path | 最终 tested SHA256 |
|---|---|---|
| MODIFY | src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py | 0AA27B67030115DEC06F9F7A5F78F0113380ABC857D3F08189982EB90E3D8AFE |
| CREATE | validators/multi_province/annual_observed_labor_diagnostic/data_only.py | 6D72243D07550E51C793F1E540CBE1177BC6CB99CDC0238F10D32C341CB9788D |
| CREATE | tests/test_ch5_observed_annual_data_only_entry.py | B3132B5EB9690B6B5B1664FF0ED5D5DFAC1A04368B3FA3EBA502259C44B0AA21 |

这是 uncommitted/untracked 工作树候选的字节身份清单，不假称 Git 已提交 diff。无 stage/commit/push/其他 Git mutation。

context 新增 prepare_observed_data_only_context(raw_sources, *, data_only, progress)：显式 data_only=True，只接受原生 list[str] 进度，先记录认证 attempted；调用原 authenticator 认证全部七项固定原始 bytes 后才进行合法 helper code preload，再记录年度转换 attempted 并调用原 sealed kernel 恰好一次。原 helper 构造公式不重复计算；返回原 sealed inactive AnnualContext。失败保留前面进度；认证失败抑制转换；同 progress 不得重新尝试。该 Boolean 明确选择数据入口，不能替代真实 pins、seal、任务门或科学授权。

CLI 固定七个 relative locators/pins，无 root/data/pin/metadata/output override。显式 flag、唯一工作树、当前 actual-task 身份及独立 Work review/receipt/三候选绑定都在 raw bytes 读取之前。当前工程 task 不满足 actual status，未来独立 receipt/binding 尚未提供，因此 fail closed。CLI 自己逐项读取七对象一次；原内核 _helper 的额外路径 hash 复核保持，不能据此宣称整个内核只发生七次文件读取。

gate 保留已核验 context/adapter 的源码 bytes，ModuleType + compile/exec 执行同一 bytes，不依赖 SourceFileLoader 路径重读或未绑定 pyc。helper likewise 执行认证后的原固定源码 bytes，预载原 _annual_accepted_wedge_helper cache 名；不替换 authenticator、pins、seal、kernel 或 callback。原 _helper 保留的路径 hash 检查只复核身份，执行代码来自合法预载缓存。sys.dont_write_bytecode=True 在其他 imports 前，唯一测试命令也使用 -B。

serializer 验证原 context/carrier seal、mapping 和同一 master，输出 metadata、roundtrip .17g CSV、context manifest 与 ledger 到单一 JSON。numerical hash 明确为 uppercase SHA256/little-endian float64/C-order/no-shape-tag，和 K1B F-order field hash 分开。manifest 的 shape/count/finite/diagonal/min/max 摘要只读同一已生成 master，无公式重建、新科学 tolerance 或 Results 判定。synthetic carrier 保留 synthetic 标记，不伪称 observed 成功。实际 CLI 只允许 observed。

## 静态审查与唯一进程

至少三名分工助手：context_public 独占 context 追加实现；governance 只读文档/身份/预算提取；entry_static_review 独立只读审查。主 Builder 独占 runner/tests、唯一测试和证据。详情在 builder_helper_advisories.md。

暂停前静态 READY 被 Work 后到 findings 覆盖。恢复后在唯一测试之前关闭 verified-bytes/pyc 风险和 kernel 内部 completed UNKNOWN 两项；bytecode 禁写与 observation_year 顶层字段保留。最终摘要版本获得 fresh FINAL_STATIC_READY；Work 也独立报告同三 hashes 无具体未关闭静态点。两者都不是测试 PASS 或 ACCEPT。

唯一执行：C:\Users\zcxve\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -B tests/test_ch5_observed_annual_data_only_entry.py

65 PASS，exit0；同一进程包含 unchanged old43（内含旧30/16）和22新增检查。仅1次 launch；repairs/retries/reruns0，engineering remaining0。测试后源码修改0。原 stdout/stderr 按 native stream 原始 bytes 保存为 sole_test_stdout.txt / sole_test_stderr.txt；stderr footer 为 Ran 65 tests / OK。stdout 为空，hash E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855；stderr SHA256 43660B5AE44DDB2042C548D5BD278477AA614809A6EF90CE1E33B1CB820ACA6F。

新增检查覆盖 flag/root/task/receipt 错误在 raw 前拒绝、固定七 locators/pins/无 override、原 blocked 入口、错误 invented rawhash 抑制 parse/转换并保留attempt、genuine synthetic CSV/轴/units/provenance/shape/hash/同 master 摘要、retained bytes loader 不读路径、helper code preload 的固定身份与错误 bytes 拒绝、seal copy/replace 拒绝、once-only synthetic helper、无文件 writer/scientific dependencies、内部 attempted/completed UNKNOWN。没有 mock 真实七hash匹配、真实认证成功、observed token 或公共 observed 转换成功。

## 固定身份与交付

初始非状态69身份一致；恢复与测试后固定68/68一致（71基线精确排除 CURRENT/TASK/context 三项）。三候选 post hashes 等于唯一过程输入 hashes。context 原前22478 bytes SHA256 1E10D5FCF73D772F8C8C0AC8462FE3E522A0B16652837E896C874CE9EC7B709B，与 prechange 完全一致。HEAD 75cee92b1ad9e5cb6fc069bca892213838ffdddc、HEAD:src 00682b2e1a7ba23665f6e16f6acf48ad35874883 均不变；其余 source、adapter、helper、integration、中间桥接、旧tests、保护资料及 dirty/untracked 均保留。

已保存两报告（本报告及 builder_boundary_report.md）、helper advisory、builder_execution_ledger.json、builder_postchange_receipt.json、测试原始输出、sole_process_launch_record.json、sole_process_result.json、tested_task_current.md 及新的 resumed pretest receipts。另以 builder_turn5_delivery_receipt.json 记录第5条补交身份，不覆盖 active_turn4 历史收据。旧 pretest/backup/prechange/prior-task/pause 证据未覆盖。

Owner realdata max1 仍 launched0/remaining1，本条真实授权0；实际 raw 数值、认证成功、observed 转换、真实矩阵、science/model/calibration/production 均0。旧测试/科学预算保持消耗，不重置。C9 PAUSED、Objective A RETAINED、历史 CALL_LEDGER_UNRESOLVED、price_verified=False、release UNKNOWN、model_activation=False、Results FALSE，历史 leaf/admin NONCOMPLIANT 保留。

停待独立 Work ACCEPT/REJECT；通过作者测试不自行接受、不签发或执行后续实际数据任务。
