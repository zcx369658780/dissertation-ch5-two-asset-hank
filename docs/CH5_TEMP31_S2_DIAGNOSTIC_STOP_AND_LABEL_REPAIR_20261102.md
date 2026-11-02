# TEMP31 S2单次诊断停止与观察标签修复 · 2026-11-02

STATUS=SINGLE_OWNER_APPROVED_ATTEMPT_CONSUMED__STOP_NO_RETRY__ENGINEERING_LABEL_REPAIR_VERIFIED
AUTHORIZATION_PARENT=7e0fc7bcaefd9a5a61dda727d23c2b73ad02e7ca
OWNER_EXACT_STATEMENT=请继续，我授权。
OWNER_DECISION=CH5_TEMP31_S2_OWNER_DECISION_20261102_01.json
OWNER_DECISION_SHA256=77572df42b18fa401ef1ea940822f1b1893184a7c55c373bcdd1f011f54afa20
EXECUTED_CODE=41eb30005c223eced9b25d744f5253c288256864
REPAIR_CODE=c8a323dec6662221b377240921408e7905f2e1a9
REPAIR_CODE_PARENT=0847fc480e3b46bc5627fbd1465c19a48bfc0ce6
REPAIR_CODE_TREE=73ef8ce15768918eb26b426ba816d8989da504d7
MODEL_CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

## 实际执行与停止

Owner明确批准既定S2提案后，先登记不可变决定、代码/来源/fixture/环境与累计账本，才启动唯一进程。代码和环境摘要、原11模块源码字节/Blob/SHA与目录摘要、固定输入摘要均匹配。历史工作树/index状态保持。单次意图temp31_s2_first_origin_a_20261102用1/1进程，重试0。

| 观测 | 实际值 |
|---|---|
| 墙钟 | 2.875秒，限额120秒含导入 |
| 峰值进程提交内存 | 1,344,159,744字节，限额2,147,483,648字节 |
| 资源保护 | 父进程恢复前Job绑定；子进程独立确认实际成员及限额；退出/句柄清理确认 |
| 返回 | exit73；WORKER_STOP_RECORDED；ObserverBlocked:DUPLICATE_BINDING |
| 停止位置 | 原11模块加载及绑定规则构造后，CallObserver构造时；尚未调用sequence/prepare |
| 已发生 | NumPy/SciPy实际导入；停止记录列465个依赖模块名；原11源模块隔离加载 |
| 未进入 | 网格生成、初始化、模型Brent、HJB、KFE、家户汇总各0 |
| 数值结果 | 无模型数组、无HJB/KFE或原算子诊断；尚不能判断数值兼容或收敛 |

零调用结论依据固定代码控制流和构造器异常位置，不冒称取得科学调用观察账本；calls目录/观察器CLAIM尚未创建。资源限制未触发，不把峰值或导入完成解释成模型性能/动态依赖完全认证。原停止记录不含堆栈或具体冲突标签，不能冒称捕获运行时第一对冲突函数。

## 静态定位与有限工程修复

只对原11源与两份指定SciPy包装代码compile、递归查看代码元数据，不执行科学源码，发现四对不同生成器代码共享filename/qualname/firstlineno：工作地劳动输入校验65行、合成工资校验79行、有效工资记录校验58行和SciPy is_sptriangular803行。旧标签只哈希这三个字段，确定会把同一阶段的不同代码对象命名成同一标签；该缺陷与实测DUPLICATE_BINDING一致。

修复只修改worker绑定标签：按实际code/global身份配发独立序号并保留原来源摘要前缀；同一身份仍复用标签。没有忽略或合并重复规则，没有放宽观察器拒绝门、阶段许可、计数、native身份、Owner门、资源约束或科学参数。科学源码/公式/网格/输入/容差均未改，原11源目录摘要保持。

新增两个不导入科学模块的夹具，分别覆盖同一行两个生成器、同一代码在不同globals下的绑定；先复现两个失败，再修复。修后相关9项检查一次通过，失败/错误/skip均0，观察器实际区分并记下两类不同身份调用；工程阶段科学导入0、新worker进程0。既有中性进程21不重跑，旧16项历史验证不冒称新版全套重新通过。本次为Local Codex工程自审，不是独立科学评议。

| 修复文件 | 字节 | Git Blob | SHA-256 |
|---|---:|---|---|
| tests/test_temp31_locked_worker.py | 8006 | 04854d4bbb1ac985cc98b563398ccb0c8fc5f202 | 84221c51a908c2b05dcdd3a403081374aaab274fb9571e9b3a83cf409d757195 |
| validators/multi_province/temp31_first_origin_worker.py | 24715 | ad5e1a347efb8a8bbb1a64cae368569d6d9eb84a | 56f6be029551f79657ce5d56c8a06447b9ec5caf0fda497510df9b51b409a874 |

代码范围仍593路径，仅修改worker与其测试，其余591路径及原565基线保持。修复源码已本地提交，不推模型代码或原始证据；实际失败进程绑定原41eb300版本，不事后替换为修复版。

## 授权闭合与下一具体决定

CURRENT状态CLOSED_STOP_NO_RETRY，原owner_approved=true仅保留历史批准事实，启动门因状态关闭而拒绝。原决定、原proposal、原执行根、失败日志和预登记/完成账本保持；本次1/1已用、重试0，旧初始化3/10余7、工资/补录1/1关闭均不动。

[修复后新一次提案](CH5_TEMP31_S2_AFTER_LABEL_REPAIR_PROPOSAL_20261102.json)已固定最终代码pins：科学输入、原800格、净19、价格、参数、容差、1进程120秒/2GiB和各调用上限与原请求完全相同。若Owner另行明确批准，将是新的第二次累计尝试；绝非当前许可剩余额度，也不重开或更名续用旧意图。当前未获新批准、未建新执行意图、未启动第二进程。失败/未知仍停止，零自动重试/后继。

严格接受标准仍null，消费者/formal_ha_accepted/科学接受/Results/model_activation/REAL_GE均FALSE；R12/R13/WASM/OWNER_BASELINE_REBIND及16义务保持。不清理分支、不合并main、不移动删除原件、不修改全局配置。普通工程已完成到可审阅的新提案，下一科学运行必须有新Owner决定。
