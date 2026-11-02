# TEMP31 捕获元数据补录实施与一次工程取证 · 2026-11-02

STATUS=APPEND_ONLY_SUPPLEMENT_WRITTEN__TYPED_ATTACHMENT_PENDING__NO_SCIENTIFIC_RELEASE
AUTHORIZATION_PARENT=5a4f5070304d71d02d8114fef49847a6a530d376
LOCAL_CODE_CANDIDATE=b9af5ba423f66876481dd56324406b30f2ca471b
LOCAL_CODE_PARENT=c7824e59902adbffa336c99a7bcc1c8686e04669
LOCAL_CODE_TREE=044881ae2471e0e432bf89f6b96ab9706a0f371b
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

先完成并固定[补录合同](CH5_TEMP31_METADATA_SUPPLEMENT_CONTRACT_20261102.md)及JSON，随后在Owner同类工程调试委托内实现、夹具检查并登记一次具体工程读取许可。读取两份已固定合成捕获文件的字节，数字保持不透明token，不调用旧工资函数、初始化或求解器。冻结合同不回写执行状态，执行许可/claim/回执与新旁证分别保存。

## 实际补录结果

| 元数据 | 取得结果 | 身份绑定 |
|---|---:|---|
| 完整实际参数的canonical byte_count | 206 | 规范字节SHA与旧entry及lineage的7ea0130e...完全一致 |
| 实际返回形状 | (2,) | 由旧values数组结构直接计数，再与类型元数据/来源地数量交叉核对 |
| 规范返回byte_count | 39 | SHA与旧return及lineage的2900a554...一致，也匹配旧39字节记录 |

实际只启动1个工程提取worker，退出0、未超时、父进程墙钟0.438秒，entry/return各读1次，无重试。新工程读取额度1/1已耗并关闭，原工资单次源函数额度仍关闭、初始化3/10已用余7保持。工程读取不是新的科学worker或生产者观测。

新旁证SUPPLEMENTARY_CAPTURE_METADATA.json排他新建，包含原捕获文件pins、原lineage/清单、代码身份、方法、规范SHA/字节数、shape及源span哈希/偏移。原捕获文件、原参数/返回值、旧清单与旧元数据未改。旁证/许可/脚本/日志全部LOCAL_ONLY，公开只同步聚合元数据和代码身份。

科学数字未转换为Python int/float或科学数组，未求值或舍入；没有重算工资、调用原初始化/root/HA/HJB/KFE/GE/IRF/policy/MATLAB、访问真实数据或读取R12资产。仅在字节与结构层面补齐旧记录缺失的描述。

## 提取器与检查

新增标准库模块temp31_capture_metadata.py及一份测试。词法器只保留标量token字节、对象键序和容器结构；规范化只排序对象键并移除结构空白，原数字拼写保留。返回报告只包含元数据与身份，不返回规范参数/返回字节或数值。没有文件I/O、科学导入、callback或源程序执行入口；实际读取由单独有限执行器负责。

新模块缺失时setup错误1、tests_run0；首轮179项检查有1项夹具预期错误：过大的CapturePin在构造时先被拒绝，已分开验证pin拒绝和原文档大小拒绝。自审补充字符串token边界失败用例，复现后修复含结束引号的长度计数。最终19项新+163项既有限定检查=182/182通过，错误/失败/跳过0。

文件执行器另外6项纯夹具检查通过：单次读取、坏哈希消耗读取后停止、未知角色/越界路径、排他claim/输出、大小错误读前停止，以及从根到叶的重解析祖先检查。祖先顺序问题先通过元数据注入用例复现，再修复；没有创建真实重解析路径或通过新的平台保护认证。共182项限定回归+6项文件保护夹具，实际捕获读取前完成。

在排他持久claim之后才打开两份捕获文件，文件哈希/大小及读前后状态通过，受父进程30秒超时门控制。worker阻断网络/子进程与科学包导入，并监视原科学函数进入；已载入科学模块、科学调用均0。路径前后核对不等于原子OS隔离，WASM保护STOP不变。工程自审不替代独立科学评议。

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_capture_metadata.py | 39d7aa0ed80a4b8b3ac221de3fde9f9b6f4f32e3 | 10290 / 797cac4df5436b13a2a8a356460a9bc863a99172522c2ffb644735d818e2c6eb |
| tests/test_temp31_capture_metadata.py | 6b976175438c6ed1f76ef94a698edb699a28a81f | 8719 / dd5914d8bb2bc6bf557ce3a419e75295ecb24da05ae1f22635e3482d65653adb |

原575代码路径及最初565路径Blob全部保持，新加两文件后577个选定代码路径。代码仅本地，旧科学源码、参数/输入/价格/容差和HA网格未改，不提供不存在的远端源码链接。

## 当前边界与下一步

两项缺失元数据已取得独立旁证；旧保存桥的None字段尚未通过新分支接入，旧行为保持。下一工程仅实现严格身份绑定的旁证接入与拒绝检查，无旁证/错旁证保持原拒绝路径；不重跑科学函数。

即使旁证接入，仍为历史固定合成调用的保存证据，不等于真实生产输入/来源/现场资格或科学接受。所有consumer_ready、real_execution_enabled、scientific_acceptance、formal_ha_accepted、FORMAL_SOURCE_FREEZE、Results、model_activation、REAL_GE保持FALSE，严格KFE未通过。

旧dirty树/HEAD/index、历史原件/缓存/证据、V010、WASM/R12 STOP、R13未授权、保护重绑定未授权、16义务和旧耗额保持；无分支删除/main合并/原件移动/全局配置修改。
