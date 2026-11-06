# B3子进程环境与停止回报修复准备：未应用补丁，12项离线检查通过

DATE=2026-11-06
OWNER_CONTINUATION=请继续
STATUS=UNAPPLIED_REPAIR_PREPARATION_COMPLETE__12_OFFLINE_CHECKS_PASS
MODEL_ENGINEERING_CANDIDATE=0bc66c0eda5539f86dfb757bfbf60011b2eed945
MODEL_ENGINEERING_TREE=bb963051f9669b2af4ccfec68479453d6d6a3857
MODEL_PARENT=da0ba2e9be4cc453d571c44615a2e13d8945a711
GOVERNANCE_PARENT=eb4fc056513e4f9e6decbad2e7767064966ec799
PATCH_APPLIED=FALSE
NEW_EXECUTABLE_CONTRACT_CREATED=FALSE
NEW_REAL_WORKERS=0
NUMPY_SCIPY_IMPORTS=0
PROJECT_SCIENTIFIC_CALLS=0
NEW_GRANTS=0
SUBAGENTS=0

## 已完成的修复准备

本片仅新增一份未应用补丁、机器可读准备清单和离线测试，共三路径。旧监督器/worker/合同/测试四份原字节保持；旧四项真实检查仍为三项资源通过、环境一次停止、各1/1关闭且零重试。没有新runner、临时真实验证目录或新运行合同，也未以“请继续”重开旧额度。

补丁对两个已知工程问题作出具体修改，尚未安装到实际路径：

1. 父端构造新的Unicode子进程环境块时，保留三个线程项为1，另预置OPENBLAS_MAIN_FREE=1；处理Windows键名大小写冲突，保留调用方环境映射不变。子端启动证明新增该项的实际值核对，准备合同也要求该项明确存在。os.putenv/os.unsetenv、越界写、网络和任意子进程的原审计拒绝函数AST完全不变；不修改NumPy、Python、Desktop或全局配置。
2. 环境成功结果才检查definitions_loaded、真实导入标记、ver次数等成功专属字段；停止结果先验证共同身份、零科学进入与停止诊断，再将原错误传到父端回执。这样不会用KeyError:definitions_loaded遮蔽已保存的AUDIT_DENIED:os.putenv。完整成功证明仍须24定义、实际导入TRUE、公共包初始化FALSE及严格整数的ver次数0或1；未知状态、错误身份、非零科学体、非法诊断或状态/退出码不一致仍拒绝。

旧合同既缺新增环境项，也绑定旧源码SHA。离线检查分别确认这两层拒绝；补丁即使以后应用，也不能拿旧合同直接放行。未来实际绑定仍须单独准备，不能修改旧claim或消费旧关闭次数。

## 证据与12项离线检查

已保存的真实环境WORKER_RESULT没有definitions_loaded等成功字段。测试使用其原字节解码，并只构造标明为测试数据的父/Job证明：旧verify_child稳定复现缺字段KeyError，补丁候选验证同一停止结果后保留原RuntimeError:AUDIT_DENIED:os.putenv。mock生命周期进一步确认父端最终记录WORKER_STOP_NO_RETRY及原错误，清理结果仍被核对；不生成新的真实运行见证。

只读安装NumPy _core/__init__.py确认当前源码在OPENBLAS_MAIN_FREE缺失时调用os.putenv并登记后续清理。测试仅从这份已锁SHA源码提取env_added赋值和导入前for分支，交给假的os对象执行：缺项时重现拒绝，预置值时不调用putenv且清理名单为空。没有导入NumPy或执行其数组/二进制初始化。它确认所读代码分支的机制，不补写旧失败日志未保存的事件键值/调用栈，也不证明真实导入一定成功。

最终12项通过，覆盖补丁/完整基础字节pin、旧合同双层拒绝、子环境与父环境隔离、上述源码片段、原审计不变、新子证明、保存失败复现/回报、成功字段缺失及布尔冒充整数拒绝、完整合成成功与23定义拒绝、身份/诊断/状态反例及mock父端清理。所有结果限离线工程资格，合成成功记录不算环境或HA通过。

首轮11项中一项测试期待较晚的pin拒绝，实际先被新增合同字段拒绝；已把两层拒绝隔离测试，原日志保留。随后12项通过。预提交清单另发现缓存路径分隔符比较问题及补丁自身空白上下文的格式告警，均为新检查工具问题：归一清单路径，并将补丁保存为零上下文格式，完整基础SHA仍锁定；修正后12项复核及补丁只读适用性检查通过。未为了测试改动任何已封存源码或证据。

补丁只读检查使用git apply --check --unidiff-zero，未执行应用操作。两个拟修改文件分别锁基础和候选完整SHA；零上下文格式不能成为忽略源身份的理由。代码图谱未返回较新模块的目标函数，故按当前报告列明的精确路径直接读取；没有扩大索引或查询范围。主代理工程自审，不称独立科学审查。

## 本地候选与保留核对

| 新路径 | Git Blob | 字节 | SHA256 |
| --- | --- | ---: | --- |
| validators/multi_province/outer_no_model_repair_20261106/repair.patch | e07c2c958b3ef8af54385ef85e9b180d27a31924 | 3535 | d9c18866d634c07b88d82a9006d6d99068fd65f6034fad89910b2c9d0048064f |
| validators/multi_province/outer_no_model_repair_20261106/repair_plan.json | 09d37f79eb05d746f3b96640eccb69e09a3f0262 | 2228 | 2f4de21849777090456084f680d924d778662d822c51bf10172fd1bd008fb3e6 |
| tests/test_outer_no_model_repair.py | 041b7270605687dbc01d2714a73e602a8b6ca79d | 13063 | 9181f67fdbbc0ad3edc00f4901520e00f81157f9af239da8c0344b8428525c8f |

旧四份执行源码/合同/测试、四项检查20份回执、上片14份准备证据及六份缓存逐件长度/SHA一致；新增缓存0，原24份定义源码身份保持。完整安装路径/旧回执/测试日志及保存范围仅LOCAL_ONLY，代码/补丁/测试/清单仅本地模型分支。GitHub只同步脱敏治理文档，API写入0，不推模型代码、不合并main。

## 下一具体工程目标与硬门

下一步是准备未来版本的实际监督器/worker与独立合同绑定方案：保留旧版本和全部关闭记录，明确新文件身份/固定入口/输出目标/子环境证明及前瞻次数、资源、STOP。旧三项已通过的资源检查不因本次修复再跑；环境真实检查也不能沿旧合同、改名或改目录自动重试。本轮真实worker预算0，未登记或执行后继额度。

真实NumPy/SciPy及24定义导入、完整动态/native依赖、实际HA资源、科学调用预算、具体输入/冻结网格及可执行消费许可仍未建立。HA整体黑箱、原算法/网格/controls不变，不新增内部解释、误差阈值或科学接受标准；后继科学运行须适用Owner具体有限决定。

TEMP31 7/7、Moll 3/3、七入口1/1及工资/补录保持关闭，旧初始化余额仅原8格、不跨借；strict reference/thresholds为null。科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。A1、工资税、财政边界各乘H一次及a*r_a决定保持。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务不变；历史dirty树、原件/缓存/证据不移动或清理，无reset/stash/clean、强推、main合并或全局配置修改。

前置：[四项无模型检查封存](CH5_B3_NO_MODEL_RESOURCE_ENVIRONMENT_RESULT_20261106.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
