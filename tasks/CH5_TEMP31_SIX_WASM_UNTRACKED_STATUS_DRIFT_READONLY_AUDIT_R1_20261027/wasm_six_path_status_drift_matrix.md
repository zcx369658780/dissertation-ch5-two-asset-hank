# 六路径状态矩阵

原始记录类别均为`??`，只公开别名和记录SHA；精确路径与完整记录仅在Owner私有ledger中。

|别名|原记录事件|当前状态流成员|文件存在/大小/时间/SHA|reparse证据|
|---|---|---|---|---|
|WASM_OLD_01|PATH_RECORD_REMOVED|NO，仅证明记录不在当前流|NOT_CHECKED / NOT_MEASURED|祖先守卫命中；组件UNKNOWN|
|WASM_OLD_02|PATH_RECORD_REMOVED|NO，仅证明记录不在当前流|NOT_CHECKED / NOT_MEASURED|安全STOP后未逐件检查|
|WASM_OLD_03|PATH_RECORD_REMOVED|NO，仅证明记录不在当前流|NOT_CHECKED / NOT_MEASURED|安全STOP后未逐件检查|
|WASM_NEW_01|PATH_RECORD_ADDED|YES，??|NOT_CHECKED / NOT_MEASURED|安全STOP后未逐件检查|
|WASM_NEW_02|PATH_RECORD_ADDED|YES，??|NOT_CHECKED / NOT_MEASURED|安全STOP后未逐件检查|
|WASM_NEW_03|PATH_RECORD_ADDED|YES，??|NOT_CHECKED / NOT_MEASURED|安全STOP后未逐件检查|

旧三件当前是否仍存在未知；不把状态记录移出等同文件删除。新三件虽在当前未跟踪状态流中，仍没有获准完成普通文件身份或内容测量。当前流成员核验不同于直接文件访问。完整历史状态变化仍是既有执行者记录，内容对比和重命名配对均不可完成。
