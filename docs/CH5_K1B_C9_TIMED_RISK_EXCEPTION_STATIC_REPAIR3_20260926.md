# C9 计时风险例外静态 Repair3

状态：`BUILDER_REPAIR3_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。依据 Repair2 独立审查 `REJECT__PREIMPORT_IDENTITY_AND_DIRECT_DELEGATE_ENTRY__ZERO_SCIENCE_REPAIR_ONLY`，仅修复身份检查、对象绑定和直接科学入口。Results eligibility 为 `FALSE`。

## 入口与身份

- 唯一工作树 `D:\ProjectTemp\c5k1bturn56`；入口 HEAD `f5ecd918107122dc6d2a018f53f4b8ecbd8f7f1a`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。`TASK_CURRENT.md` 与归档 Repair3 任务逐字节相同且均已提交；入口跟踪文件干净，仅四份受保护输出根未跟踪。
- wrapper 在执行任何 delegate 模块代码前，分别检查合同和 delegate 工作树文件的 Git 状态及按 Git 属性过滤后的 HEAD blob 身份，再检查 active 合同绑定的 delegate 原始 SHA-256。读取并编译的 delegate 字节再次与已核验原始 SHA-256 比较，执行的就是这份字节。匹配的未提交合同与 delegate 组合也会在导入前拒绝。inactive 静态前检仍可读取，明确报告旧 delegate 哈希待重绑。
- delegate 在导入 wrapper 进行 active 权限复核前，也先核验 wrapper 的已提交 blob 身份。

## 计时路径与直接入口

- `run_timed_action()` 只加载一个经核验的 delegate 对象。重新核验 gate、`MeasuredGuard`、科学调用、部分或完整封存及收据均使用该对象；原模块级 `_instrumented_action()` 已移为此调用内的闭包，不再提供独立科学入口。
- delegate 的 `_execute_after_gate()` 在输出根创建前要求当前 `run_after_valid_gate()` 调用登记的同一 runtime，以及来自已提交 wrapper 的 `MeasuredGuard`。`run_after_valid_gate()` 先核对回调代码的 wrapper 路径与入口身份，并在退出时撤销 runtime 登记。仅填写可读的合同哈希和执行 ID 不能进入科学路径；直接 delegate CLI 仍返回 `BLOCKED__C9_WRAPPER_REQUIRED`。
- Repair1 的逐省实际计数、部分文件封存与读回、首错、`CALL_LEDGER_UNRESOLVED` 和零重试语义保留。科学实现、预算、网格、容差及冻结输入未改。

## 零科学验证

- 两个聚焦惰性测试文件：`22 passed`。包含导入前脏文件拒绝、同一 delegate 对象贯穿 gate/action/guard/seal、模拟 active 下仅靠可读 runtime 字段的直接入口拒绝、计时 guard 的惰性连通、逐省计数与首错封存。模拟 active 测试在 preflight 后、科学前停下，未创建输出根。
- 提交后默认 wrapper CLI：退出码 `0`，`BLOCKED__INACTIVE_CONTRACT__DELEGATE_REBIND_REQUIRED`，科学/C9/C10 计数均为 `0`。wrapper `--execute --execution-id INERT_TEST`：退出码 `1`，`BLOCKED__INACTIVE_CONTRACT`。delegate 相同直接执行 CLI：退出码 `1`，`BLOCKED__C9_WRAPPER_REQUIRED`。
- 四份受保护清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。C9 timed-risk 和 outer 输出根均不存在。
- inactive 合同 SHA-256 `DED122DDE12E86D579B80C1FC4E268D3953A6A79009E713F3A05FE1FA272B91A`，仍为 `active=false`、`attempts=0`、`execution_id=null`、`resource_wall_seconds=null`，旧 delegate 哈希未重绑。

本次模型、科学、C9、C10、重试调用字面账本均为 `0`。active 真实执行与不可捕获的进程强制终止未验证；正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`。下一门仅为 GPT Work 独立 ACCEPT/REJECT，不由 Builder 自验收或启动 C9/C10。
