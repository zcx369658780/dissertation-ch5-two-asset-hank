# TASK_CURRENT · TEMP V010资源门禁与累计账本修复

**唯一当前任务：TEMP_V010_RESOURCE_GATE_REPAIR_20261018**
**ACTIVE_TASK=TEMP_V010_RESOURCE_GATE_REPAIR_20261018；TASK_SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA**
**STATUS=ISSUED_NOT_STARTED**
**ISSUE_COMMIT=2ba4a716ebde395a7f659729513e725e0d8d1f07**
**TASK_BLOB=e817ce5737ba8c2a189122e4d0bb08cd4f85ef7c**
**TASK_PATH=experiments/TEMP_V010_RESOURCE_GATE_REPAIR_20261018/ENGINEERING_CONTRACT.md**

[固定任务合同](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/migration/astra-workflow-20261012/experiments/TEMP_V010_RESOURCE_GATE_REPAIR_20261018/ENGINEERING_CONTRACT.md)

## 任务边界

只处理已失败TEMP任务的资源硬门与累计账本核对。不得重启科学driver、续跑A1、启动A2/A3、运行任何HA/HJB/KFE/selector/root solver或更改正式模型。当前任务SCIENCE调用预算=0。

## 新资源上限（只对本任务生效）

| 域 | 上限 |
|---|---:|
| ENGINEERING全部真实子进程/后代 | 192 |
| Python/focused pytest启动总数 | 48 |
| 同时活动Python进程 | 8 |
| 跨全部Python进程活动工作线程 | 64 |
| 主动工程墙钟 | 3小时 |
| 工程修复/验证批次 | 8 |
| 新增非Git字节 | 512 MiB |

上限必须在创建/启动前强制执行。进程与线程分开计数；资源账本不得静默倒退。写前身份与STOP规则不放宽。

## 重点验收

1. 对账manifest打包前ENGINEERING=37与最终receipt ENGINEERING=35的差异；没有原始证据就保留UNKNOWN，不猜测。
2. 合成测试证明Python第49次启动、并发第9个Python进程、总第65个活动线程、工程第193个后代均在创建前拒绝。
3. 注入账本/checkpoint故障或STOP后，dummy后续调用数必须为0。
4. 全过程HA/HJB/KFE/selector/root solver调用数严格为0。
5. 保留初始失败和原TEMP证据；不发布/清理旧review候选，不运行Git fetch/push。

**PREVIOUS_TEMP=FAIL_CLOSED_SHARED_RESOURCE_PRECONDITION；OLD_BUDGETS=CLOSED_NO_CARRY_FORWARD**
**FORMAL_V010_UNCHANGED；model_activation=False；REAL_GE=False；Results FALSE；V011 NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**FINAL_STOP=WAIT_ASTRA_RESOURCE_GATE_REPAIR_REVIEW / NO_SCIENCE**
