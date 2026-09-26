# C9 计时风险例外静态 Repair2

状态：`BUILDER_REPAIR2_CANDIDATE__AWAITING_INDEPENDENT_GPT_WORK_ACCEPT_REJECT`。本轮只处理 Repair1 独立审查的 `REJECT__CALLER_SUPPLIED_DELEGATE_BYPASSES_BOUND_IDENTITY__ZERO_SCIENCE_REPAIR_ONLY`；Results eligibility 为 `FALSE`。

## 修复与边界

- 唯一工作树为 `D:\ProjectTemp\c5k1bturn56`，入口 HEAD `9598b6fc4d478d6ee16b08b0ab2761fdaf8b9be8`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。入口任务、归档任务与受保护根的核验已通过。
- `run_timed_action()` 不再接受位置参数形式的 delegate；`_instrumented_action()` 不再接受 delegate 参数。两个可直接调用的生产入口分别从固定 `DELEGATE` 路径严格加载合同哈希绑定的模块，重新执行 `future_gate()`，并只使用该加载对象执行、计账或封存。`execute_once()` 的下游调用也不传入 delegate。
- 测试通过内存替换加载函数和 action，验证伪造 delegate 在模拟有效 gate 下仍不能作为参数进入两个入口；验证检查 gate 时拿到的对象正是加载返回的对象。保留 Repair1 的逐省计数协调、部分产物封存、首错和 `CALL_LEDGER_UNRESOLVED` 语义。
- inactive 合同未修改：`active=false`、`attempts=0`、`execution_id=null`、`resource_wall_seconds=null`。其 `delegate_sha256=54D8E39684CD659B4208D120551A47D03FE28E59EB23C2C5DCFD8766A6FFADF3` 仍是旧值；当前只读 delegate SHA-256 为 `D88616CFBA2F07398A6375A1C055D9B7A3ACADD74987DD0C72677F1369E4F70A`，后续需另行审查重绑。

## 零科学验证

- 聚焦惰性测试：`PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn9_timed_risk_exception_preflight.py`，`11 passed`。无模型、科学、C9、C10 或重试调用。
- 默认 CLI 退出码 `0`，状态 `BLOCKED__INACTIVE_CONTRACT__DELEGATE_REBIND_REQUIRED`，科学/C9/C10 计数均为零。`--execute --execution-id INERT_TEST` 退出码 `1`，终态 `BLOCKED__INACTIVE_CONTRACT`；未触及 delegate 或科学入口。
- 四份受保护清单 SHA-256 依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`。C9 timed-risk 和 outer 输出根均不存在。
- Wrapper SHA-256 `9820235C3BA17C13E9DA713A4E0DE80A51351FB9F86A791BDBA9D85C0A71628C`；测试 SHA-256 `3E0C473BB4CE68D054AB2DAE9664A1A7415CCB00742F9F98C4F9F13193977AD9`。机器收据记录最终路径与状态。

本候选等待 GPT Work 独立 ACCEPT/REJECT；不得据此激活合同、选择资源墙、运行 C9 或启动 C10。正常时长门仍为 `BLOCKED__DURATION_BOUND_UNAVAILABLE`。
