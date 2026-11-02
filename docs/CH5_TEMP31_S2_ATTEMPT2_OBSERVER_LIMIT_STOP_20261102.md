# TEMP31 S2新增第2次尝试：HJB观察器计数上限停止 · 2026-11-02

STATUS=CLOSED_STOP_NO_RETRY__SECOND_OWNER_APPROVED_ATTEMPT_CONSUMED
OWNER_EXACT_STATEMENT=我授权，请继续
OWNER_APPROVED_QUESTION=是否授权修复后新增1次相同输入诊断，仍限120秒、2GiB，失败即停？
OWNER_DECISION=CH5_TEMP31_S2_OWNER_DECISION_20261102_02.json
OWNER_DECISION_SHA256=bfb8a75a4ed1a303079373d57ea81189b4c745844bf1ac6016dc243167973944
PROPOSAL=CH5_TEMP31_S2_AFTER_LABEL_REPAIR_PROPOSAL_20261102.json
PROPOSAL_SHA256=ae54a9b02f0e0d559a08ab474ac72269cb8aa9b4d2d739cfa433a4c38314f07b
CODE_CANDIDATE=c8a323dec6662221b377240921408e7905f2e1a9
CODE_TREE=73ef8ce15768918eb26b426ba816d8989da504d7
MODEL_CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
INTENT=temp31_s2_first_origin_a_after_label_fix_20261102

## 实际结果

新授权单进程已执行，墙钟35.313秒，峰值提交内存1,377,615,872字节；exit73，WORKER_STOP_RECORDED。父进程挂起绑定Job后恢复，子进程真实成员/限额及返回绑定交叉核对通过，进程退出/资源清理确认。未触发120秒或2GiB限制；没有再次启动或自动后继。

| 阶段/计数 | 本次证据 |
|---|---|
| 固定准备 | 原20×20×2网格及输入身份记录已保存；未改节点/价格/参数/容差 |
| 初始化 | 进入1、profile return事件1，并保存LOCAL_ONLY初始化返回；不读取NPZ评估数值 |
| 劳动根/Python Brent/native Brent | 各准入800；劳动根和Python Brent各800个profile return事件；native只计c_call，不把0个Python return解释为失败 |
| HJB | 进入1、profile return事件0；没有HJB返回/收敛元数据 |
| HJB线性求解 | 准入29、profile return事件29；不等同29轮完整迭代或科学通过 |
| policy格调用 | 准入23,810、profile return事件23,809；中途停止，事件不是独立成功认证 |
| 停止辅助函数 | HJB阶段尝试1,000,001、准入1,000,000，超过原固定观察器限额后拒绝 |
| KFE/汇总 | 观察器准入均0，未进入；无密度/汇总/原算子驻定诊断 |
| 模型结论 | 初始化路径已实际完成；HJB未返回，收敛/不收敛均UNKNOWN，不能评价KFE或正式HA |

原第1次因DUPLICATE_BINDING在CallObserver构造处停止；修复后本次已进入prepare/initializer/HJB，旧标签冲突未阻止这些阶段。不是新的数值收敛、科学接受或Results。

## 停止位置与证据限度

实测reason=ENTRY_LIMIT_EXCEEDED:hjb:dep_b3e4d9e82c5b8b0c3c19_72。通过现存观察器CLAIM的代码SHA与原源compile元数据对照，精确匹配src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py第55行validate_effective_wage_record.<locals>.<genexpr>.<genexpr>，代码SHA256=312d6040e81194553baf7bf1ee284e2591eebe8653fbbd8866ef0e21f021d7b1。这是工资记录验证中重建sigma的嵌套生成器；静态调用点确认policy与多个经济辅助函数会重复require_netwage_inputs，不能仅从总计数推断唯一动态调用栈或完整迭代次数。

原worker对获准辅助代码每阶段固定限额1,000,000，实际在1,000,001次调用前拒绝；没有提高、忽略、合并或绕过该限制。该上限属于本次固定代码pins中的执行约束。观察器主动抛出ObservedStop后CPython清除profile钩子，TERMINAL同时记录hook_lost=true、incomplete_phases=true；停止和异常均保存，不将其说成运行成功或独立的先发钩子丢失。

定位仅重新compile指定来源/包装器并比较代码元数据，未执行科学模块或创建新worker，未读原始NPZ数值。保存的初始数组不自动构成数值误差或性质认证。本轮不修改科学源码、观察器、初始化器、公式、输入、参数、网格、价格、容差或保护，不为尝试耗额追加测试/运行。

## 预登记、预算与保护

Owner本会话明确批准的是新的第2次累计尝试；先记录不可变决定_02、提案/最终代码/来源/fixture/环境pins和独立预登记账本，再调用既定启动器。593条代码路径逐件Git Blob一致、11源catalog、固定fixture、计划及环境摘要均匹配；未重新盘点公开资产或导入科学包作预检。

登记阶段一次工程格式误报保留：旧历史porcelain摘要使用-z空字符分隔，初版登记器误用换行分隔。尚未写决定/账本或建科研意图即拒绝；只读按旧格式重核后，HEAD/index/432条状态及原摘要均精确一致。保留初版脚本与误报记录后采用正确表示，并禁用Git optional locks。不是保护基线重绑定、科学尝试或科学重试。

本次新增1/1已用、重试0；S2跨两份Owner决定累计2/2已用，原第1次决定/意图/失败账本保持。初始化旧预算3/10已用、余7保留；工资进入1/1与捕获补录1/1仍关闭，不借用或重置。CURRENT已关闭CLOSED_STOP_NO_RETRY，owner_approved=true仅为历史事实，固定启动门拒绝。原待批准提案字节不变，批准事实由不可变决定_02记录，不能再拿历史提案或本批准续跑。

历史工作树HEAD、index SHA256与porcelain -z摘要在运行前后均保持原固定基线，432条既存改动未动。两处活动树本轮只改治理文档；模型代码c8a323d保持本地，无main合并、分支删除/清理、原件移动删除、LOCAL_ONLY上传或全局配置修改。

## 后续边界

已按失败即停完成本次许可，没有第3次提案/意图/进程。本轮未放宽计数或改工资校验；任何后续方案应先定点审查验证频率与观察器计数的关系，不能自行提高上限继续。新HA/HJB/KFE尝试仍需Owner新的具体决定，不能更名续用本额度。

严格KFE驻定未通过，严格接受阈值null；FORMAL_SOURCE_FREEZE/consumer_ready/formal_ha_accepted/科学接受/Results/model_activation/REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、OWNER_BASELINE_REBIND未授权及16项义务保持。Python为唯一主动主线，MATLAB仅历史参考；无31省/GE/IRF/校准/真实数据运行。工程证据整理不是独立科学审查。

运行目录、网格/初始化NPZ、原始日志、调用账本和哈希清单均LOCAL_ONLY，公开仅本脱敏说明及授权/短状态。同步提交/远端字节回读以本地交付回执记录，不把未完成回读报为已交付。
