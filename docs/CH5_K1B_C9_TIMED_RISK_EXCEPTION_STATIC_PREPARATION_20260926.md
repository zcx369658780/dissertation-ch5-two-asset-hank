# C9 单轮计时风险例外：零科学静态准备

状态：`BUILDER_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。本次只准备 C9 delegate、计时 wrapper、**inactive** 合同和静态测试；C9/C10 科学尝试均为 `0`，没有创建预定输出根。正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`，`E_upper=null`，Results eligibility `FALSE`。

## 入口与固定身份

- 工作树 `D:\ProjectTemp\c5k1bturn56`；签发 HEAD `f4369ff3eb5bf5c8aef02c0bcce89401d3086c26`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。归档任务和 `TASK_CURRENT.md` 同为 SHA-256 `758185576BF4126413B8682D490247E329C2F10F6AF0F1001D4B372FA299A149`，均已提交；入口时跟踪文件干净。
- 受保护 C6-prime/C7/C8/C8-timing 清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。四根保持未跟踪且未暂存。
- C8 entering-C9 manifest/readback SHA-256：`40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65` / `E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`；JSON/NPZ：`FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB` / `E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`。
- 只读 C8 delegate SHA-256 `10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831`；只读 C8 timing wrapper SHA-256 `8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A`。Owner C9 路线选择 SHA-256 `EF452E26A642AA98FE2C6AD4EB3263D475AD31405236470DFB2F7CA4D247D050`；额度采纳 SHA-256 `4C2B540DF5906825253D79EA6A0603A91BDA09F4E2DC72967C9DC87858F33C40`；C8→C9 独立审查 SHA-256 `108FCB04A7521A3B3602B128BA524B39FA9070B97047AD002AB6EC6358DB233F`。

## 本候选的七条路径

1. `validators/multi_province/k1b_turn9_outer_r2/run.py`：C8 封存束的完整读回、C9 逐省/集成、C8→C9 九项严格 `<1e-6`、预备 C10 束；直接执行入口拒绝。
2. `validators/multi_province/k1b_turn9_timed_risk_exception/run.py`：未来任务、独立审查、Owner、合同和输出身份门；单调计时的协作资源墙；先记尝试的 journal、完整科学清单及读回；封存后单独写 `SAFE_PAUSE_AFTER_SEALED_C9`，不启动 C10。
3. `tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json`：39 类逐轮、5 类逐省、C9+C10 累计上限与冻结身份；`active=false`、`execution_id=null`、`attempts=0`、`resource_wall_seconds=null`、零重试。
4. `tests/test_mp4c_k1b_turn9_outer_r2_preflight.py`：inert 输入、额度、比较和失败账本检查。
5. `tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`：inert CLI、身份、时钟、资源墙、别名尝试、封存后暂停检查。
6. 本报告。
7. `EVIDENCE/ch5_k1b_c9_timed_risk_exception_static_preparation_20260926/preparation_receipt.json`：机器收据。

科学类别 guard 按采用表锁定 39 类，逐省 5 类；`frozen_k1b_quantity_allocations` 与 `k1b_feedback_calls` 记同一事件。新 C8-start 窗口从零开始，不沿用已耗尽的旧 C6→C8 或 C8 timing 额度。逐省和集成进入前 journal 保留预算预留与显式尝试；来源内部计数在返回或异常时协调。若中断使内部尝试数无法确定，保留 `CALL_LEDGER_UNRESOLVED` 和原始错误，不自动重试或续跑。资源墙使用单调时钟拒绝下一次入口，已进入的调用只在安全点退出；墙钟另行记录，不当作可信时长上界。预定根的既存路径、坏链接和重解析点均拒绝。

## 静态验证

- `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn9_outer_r2_preflight.py tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`：最终 `11 passed`。过程中测试夹具曾缺少模拟账本/合同字段，修正后复测通过；没有科学入口。
- 默认 wrapper CLI 返回 `BLOCKED__INACTIVE_CONTRACT` 的静态检查结果；`--execute --execution-id TEST_ONLY` 退出码 `1`、原始终态 `BLOCKED__INACTIVE_CONTRACT`。两者均未创建 C9 根。
- 后续提交仅暂存上述七路径；具体提交、树、blob 和 `git diff --check` 结果以终端交接及机器收据为准。

## 尚待外部门

本报告只证明静态候选与 inert 测试，不证明真实 C9 运行路径、计时精度上界、经济收敛或 Results。GPT Work 必须独立 `ACCEPT/REJECT`；之后 Owner 才能选定有限 C9 资源墙、采纳新的 active 合同并另行授权最多一次 C9 执行。C10 仍需自身正常门和新任务；午夜例外不会自动扩展到 C10。

过程偏离：本轮在读取 Chapter 5 `TASK_CURRENT.md` 前，曾只读查看 `D:\Zotero-Analytical-Workflow` 的 startup brief/index 和用户级 memory registry。这超出了本任务限定的文件读取范围；没有修改这些位置，也未访问 `deep-learning-hank`。后续实现、测试、证据和提交均在唯一 Chapter 5 工作树内。请独立 GPT Work 审查时一并考虑这一偏离。
