# C9 inactive 合同 delegate 身份重绑

状态：`BUILDER_INACTIVE_REBIND_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。本次仅落实 GPT Work 对 Repair3 的 `ACCEPT__ZERO_SCIENCE_STATIC_ENTRY_REPAIR_ONLY` 后允许的 inactive 身份重绑；Results eligibility 为 `FALSE`。

## 精确变更

- 唯一工作树 `D:\ProjectTemp\c5k1bturn56`；入口 HEAD `1216720fff2de9d26601823a418bf6c6bae0d7b9`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。当前任务与归档任务逐字节一致且已提交，入口跟踪文件干净，仅四份受保护输出根未跟踪。
- 直接读取已接受 Repair3 delegate 的工作树字节，SHA-256 为 `A4B4985DAE8C15E5F21125A0A82FCE39D1B08D975929250186D941D691C4E7BB`；其 Git blob 与已接受候选 `fb37a8f62d6ca71c7fbf7f3516e9de21473c7ed3` 的对应 blob 一致。inactive 合同仅将 `delegate_sha256` 从 `54D8E39684CD659B4208D120551A47D03FE28E59EB23C2C5DCFD8766A6FFADF3` 改为此原始字节哈希。合同修改前后 JSON 逐键比较，唯一改变键为 `delegate_sha256`。
- `active=false`、`attempts=0`、`retries=0`、`execution_id=null`、`resource_wall_seconds=null`、`wrapper_sha256=null`、`independent_review_sha256=null` 保持；全部预算上限、冻结输入身份及其他合同字段不变。只将对应惰性测试的前检预期从待重绑改为哈希匹配的 inactive 状态；生产代码未改。

## 静态读回

- 提交合同与测试后，默认 wrapper CLI 退出码 `0`，状态 `BLOCKED__INACTIVE_CONTRACT`；`delegate_hash=true`、全部 wrapper 静态检查为真、全部 delegated C8 身份及预算检查为真，`scientific_calls=c9_attempts=c10_attempts=0`。
- wrapper `--execute --execution-id INERT_TEST` 退出码 `1`，终态 `BLOCKED__INACTIVE_CONTRACT`；delegate 直接执行 CLI 退出码 `1`，终态 `BLOCKED__C9_WRAPPER_REQUIRED`。两份聚焦惰性测试共 `22 passed`。
- 四份受保护输出清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。C9 timed-risk 与 outer 输出根均不存在。

本次模型、科学、C9、C10 与重试调用字面账本均为 `0`。正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`。此重绑不激活合同，不绑定 wrapper/review 为 active 身份，也不决定资源墙或授权一次性执行；下一门仅为 GPT Work 独立 ACCEPT/REJECT。
