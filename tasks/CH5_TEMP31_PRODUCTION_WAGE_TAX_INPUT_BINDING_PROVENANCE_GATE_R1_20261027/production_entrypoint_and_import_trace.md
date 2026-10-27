# 实际入口、导入与callback来源门

结论：BLOCKED。只能确认两个受界入口及库间静态调用，未证明TEMP31真实生产入口/部署/运行绑定。发现来源守卫身份冲突后结束来源发现，只继续报告与授权交付。以下均未import或执行。

## 已识别入口

1. `validators/multi_province/mp4b_python_empirical.py`，ENTRY:1直接写明“Validation-only one-shot calendar-2009 Python stationary entry”。ENTRY:390–408的CLI可静态指向run_python_once，不能由此称为已认证生产driver。ENTRY:66–75导入固定名字的HA类、postloop函数、OneTurn batch与在线控制器；ENTRY:336–350定义局部solve_batch并在371–372传给OnlineStationaryInputs。这里只证明调用表达式，不证明运行时实际采用。

2. `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`，CORRECTED_ENTRY:1–5明确是opt-in task driver，且“不改变默认或生产运行路线”；1573–1584的CLI只提供该任务execute入口。不得将其命名为已认证默认生产入口。

## 新增的关键静态身份冲突

ENTRY:18将ORACLE_PATH定位到当前仓库`exports/matlab_faithful_two_asset_ha.py`；ENTRY:19要求SHA256 `b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3`。当前该原件实际SHA256为 `f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8`。

ENTRY:30–36先计算目标原件哈希、不同则raise；ENTRY:64在文件顶层调用该bootstrap，早于66–75的HA导入。**这对当前文件组合的静态身份门不匹配可证，但本轮没有实际import、bootstrap-check或运行，因此不是一次观察到的runtime失败。** 不修改ORACLE_SHA、不换导出文件、不标准化原件、不绕过守卫、不尝试历史替换包。

## 可确认的静态库链

ENTRY.main → run_python_once → OnlineStationaryInputs(household_solver=solve_batch) → RUNTIME.run_online_stationary在52调用该callback；callback表达式导向POSTLOOP.solve_matlab_source_postloop_household，POSTLOOP:30–40再将同一个inputs对象传HJB并做后置聚合。STATE_UPDATE:153–168将综合工资放入下一轮state.w。所有箭头仅为静态源引用，bootstrap身份冲突和真正生产入口缺口使其不能提升为实际生产闭包。

HA_ADAPTER:200–225只是StaticHouseholdCall字段映射，不能把函数签名/solver_symbol字符串当成已执行callback。RUNTIME:19、23–29的callback类型和35–55的消费表达式提供形状/有序state接口，但不是D2已部署的显式31省生产adapter证明。

## 冻结身份的界限

发文commit=eaf11cb5edfd311e7f942858a1c85424a6b5d672；候选分支基点=ef980d454726d3fadd12184b669517fea564d721；源commit=b69ae535a1518c68822733603f1e506620327375，tree=8dbd81c0938f603511c7de1c763ed29b6d2d4b83。发文提交parent与BASE一致，BASE的parent是源commit；各自角色分别记录。

本轮9份本地源字节与上轮审计记录一致，但均与源commit下同名文件的Git Blob不同（0/9）。这不是要求修复工作树或推断语义全不同；按任务合同只公开本地SHA、原行号和安全摘录，不把远端同名源码、旧审计源码或R2/R3候选当作当前已部署来源。

未在这9个精确文件和2个定向定位查询中建立一个ACTUAL_PRODUCTION绑定，不宣称全仓库/全盘没有其他生产driver。实际生产启动身份、批准版本/导入来源、对应canonical生成调用及输入原件仍SOURCE_UNAVAILABLE/UNKNOWN。Gate B因此不闭合，no-HA前置条件不满足。
