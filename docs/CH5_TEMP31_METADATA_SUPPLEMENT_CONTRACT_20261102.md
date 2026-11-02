# TEMP31 只追加捕获元数据补录合同 · 2026-11-02

STATUS=FROZEN_ENGINEERING_EXTRACTION_SPEC__EXECUTION_RECORDED_SEPARATELY
AUTHORIZATION_PARENT=5a4f5070304d71d02d8114fef49847a6a530d376
INTENT_ID=CH5_TEMP31_FIXED_CAPTURE_METADATA_SUPPLEMENT_20261102_V1
MACHINE_CONTRACT=CH5_TEMP31_METADATA_SUPPLEMENT_CONTRACT_20261102.json

本合同补足[保存元数据桥](CH5_TEMP31_SAVED_METADATA_BRIDGE_IMPLEMENTATION_20261102.md)缺少的完整参数规范字节数和实际返回形状。Owner已委托Codex下达同类有限工程调试许可，见[委托规则](CH5_TEMP31_DELEGATED_DEBUG_AUTHORITY_CURRENT.md)。允许的是对两份既有固定合成捕获文件的字节/结构取证；不授予新科学运行、实际生产来源或科学接受权限。先固定规格、实现与夹具检查，再登记具体执行许可，执行状态独立保存，不回改冻结JSON。

## 精确输入与读许可

| 原观测根下相对路径 | bytes | SHA-256 |
|---|---:|---|
| attempt01/FUNCTION_ENTRY_OBSERVATION.json | 686 | a4748223ff08dba37f0c269e99b39ed67a0b0c3e6481bec0f781d8e48dd80124 |
| attempt01/FUNCTION_RETURN_OBSERVATION.json | 237 | c36f6fa3e6e965f23079e0490b2f6c9bc69083be334ebca222a1e7a3c148e8ad |

这些文件包含前次已授权固定合成调用的捕获值。受限读取只将数字当作不透明JSON token原文字节；不得把它们转换为科学数值或数组、计算工资或输入模型。原文件、原清单、原计数和旧旁证保持。R12、真实数据、其他原始数组/CSR/私有或购入资产不在此许可内。

输入由原观测清单SHA-256=c6b41cdad2124c86f98fdb608643179cafcd186fc4827b139e7469b70deb222f固定。支持材料仅限同清单中的lineage元数据和旧worker源码编码器静态核对；旧worker不导入或执行。当前AST确认canonical编码器sort_keys=True、紧凑分隔符、ensure_ascii=True、allow_nan=False；捕获writer同样ensure_ascii=True、indent=2。两者使用同一JSON编码规则，结构空白与键序可在不解释科学数字的前提下恢复规范字节。

具体许可由Codex在既有委托内下达：最多1个工程提取进程、墙钟30秒，两份捕获文件各读1次。科学worker/函数入口为0。1/30秒是Codex选择的保守工程限额，不冒称Owner本句逐字指定；不能使用或恢复旧工资1/1额度或初始化余额。

实际读取前需代码身份固定、纯夹具检查通过、输入/元数据pins重核，以及独占且flush/fsync的持久意图claim。既有claim或输出阻止再次读取；未知结果、哈希/路径/权限/格式异常即停止并保留证据，不重命名意图或自动重置限额。未满足前置条件不能打开捕获文件。具体进程许可、代码pin和执行回执另存LOCAL_ONLY。

## 非数值提取方法

1. 先按旧清单核文件大小和SHA-256，再扫描JSON语法。识别对象/数组/字符串/数字token，不构造科学参数对象或科学数组。
2. 定位entry的arguments对象，按解码后的对象键排序，保留标量值token原文，去除结构空白，以原编码规则构建临时规范字节。其SHA必须同时匹配entry声明及固定lineage的7ea0130eb362d12a951f967275d61fa34a963cba20e27080378cc4be986ffd28。匹配后，字节序列的len才是参数规范byte_count。
3. 从return的values数组结构直接计数，要求为非空扁平数字token向量。形状来自实际数组结构；计数后才与element_types和来源地数量交叉核对，不能先拿省份数填shape。
4. 规范返回字节SHA必须匹配return声明和lineage的2900a554e1c52b4ffc9cb27a820046750ae902e79458b52d7892fd1ae54f23b3，字节数必须与旧记录39一致。

科学数字不调用int/float/Decimal，不计算、舍入、规整指数或改写负零来匹配哈希；字符串值token也保留原文。编码差异或身份不符就失败，不做数值修补。临时规范字节只用于内存中的长度/哈希，不能写入旁证、stdout或日志。

文档大小上限1MiB，嵌套深度64，语法节点/键token上限16384，字符串token上限65536字节。拒绝重复解码键、非法JSON数字、NaN/Infinity、截断、未知捕获字段、非扁平返回和类型计数不符。祖先重解析/符号链接检查从根到叶进行；读前后状态和文件身份异常停止。这不是原子OS隔离证明，也不重新绑定WASM保护基线。

## 只追加输出与接入

新文件SUPPLEMENTARY_CAPTURE_METADATA.json绑定意图ID、原清单、输入文件pins、lineage、提取器代码pin/方法、规范SHA/字节数、实际shape和原文件span哈希/偏移。它只保存元数据，不保存科学token原文、规范参数/返回字节或数值数组。使用新文件排他写入，不修改捕获文件、旧清单或旧元数据。

没有旁证时，旧元数据桥保留两项None及BLOCKED行为。未来只在旁证与原身份/上下文严格匹配后填这两项元数据；即使数据齐全，仍为旧合成观测scope，不升级生产凭据、现场科学资格、来源/输入采纳或任何消费者接受标志。

配套JSON列出18类计划夹具场景：键序/空白/转义、原数字拼写、重复键、非法数字/非有限、截断、信封、参数/返回身份、实际shape、类型交叉核对、记录互换、资源限额、路径/读中变化、claim与只追加输出。计划矩阵不等于测试已执行，实际检查和本轮后续一次补录见[实施记录](CH5_TEMP31_METADATA_SUPPLEMENT_IMPLEMENTATION_20261102.md)。

科学公式/参数/网格/容差、HA/HJB/KFE/GE/IRF/policy/校准/MATLAB运行、严格驻定接受、Results和受保护操作仍按Owner边界保持。所有消费者/科学接受门固定FALSE；旧预算与历史证据不变。
