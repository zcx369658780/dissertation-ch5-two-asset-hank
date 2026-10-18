# TASK_CURRENT — TEMP V010 Native Single-Child Resource Gate V3

唯一当前任务：TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018
状态：ISSUED_NOT_STARTED
范围：ENGINEERING_ONLY / NO_SCIENCE / NO_HA
发行提交：09e073ee69b34fc22dd5448a6a39156a0cd11775
固定合同：experiments/TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018/ENGINEERING_CONTRACT.md

固定合同链接：
https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/migration/astra-workflow-20261012/experiments/TEMP_V010_RESOURCE_GATE_NATIVE_SINGLE_CHILD_V3_20261018/ENGINEERING_CONTRACT.md

前置事实：上一次DOC_ONLY报告被接受为程序合规的STOP，不代表本地镜像同步成功。未写本地文件，不得擅自改用其他路径重试。上一资源门禁任务仍为FAIL_CLOSED_UNRESERVED_REAL_DESCENDANT；28/28合成测试不能抵消真实Windows Job预留2、累计3的E2。

本任务只检查和修复资源门禁的有界单子进程控制及计数。先核验保护路径和独立scratch；无法核验则只读报告并STOP。合成与真实OS测试分开报告。真实测试仅允许一个直接子进程，不允许测试子进程再派生后代；创建时挂起，分配Job并核验身份后才恢复运行。ActiveProcessLimit=1只限制并发活动进程，不代表限制生命周期累计创建数。任何未知身份、计数不一致、意外后代或STOP异常立即E2 STOP。

预算：工程全部后代≤192；Python启动≤48；同时活动Python≤8；跨进程活动线程≤64；工程时间≤3小时；最多8批。所有上限必须在创建前执行。

禁止HA/HJB/KFE/selector/root solver，禁止科学运行，禁止Git fetch/push、网络发布和旧review清理。旧预算不结转。

ACTIVE_RESEARCH_TASK=NONE
SCIENCE_CALLS=0
model_activation=False
REAL_GE=False
Results=FALSE
V011=NOT_STARTED
FULL_RUNNER_IO_CLOSURE=BLOCKED
最终停点：WAIT_ASTRA_NATIVE_SINGLE_CHILD_RESOURCE_GATE_REVIEW
