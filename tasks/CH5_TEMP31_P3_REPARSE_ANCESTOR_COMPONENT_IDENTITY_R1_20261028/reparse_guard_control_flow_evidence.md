# 持久化先于安全判断的控制流证据

每条祖先记录含递增sequence、匿名alias、根相对depth、原始attributes、reparse布尔、目录类型、UTC与北京时间。

实际顺序：预算预占 → `component.lstat()` → 构造记录 → 新建任务scratch私有JSON → flush → fsync → 回读完整原始字节并核对JSON → 保存并验证确认记录 → 判断reparse → 若命中保存STOP事件并break。下一组件仅在当前非reparse且为目录时才允许检查。WASM文件名末端不包含在祖先链中。无resolve、realpath、readlink、目录列举或stat-follow诊断调用。

公开ledger每条含实际私有记录SHA、字节数、保存验证时刻、保存确认SHA和顺序证明。私有记录本体含完整路径，不上传；公开记录只保留匿名属性。成熟SHA-256和原字节相等核验用于保存确认；操作系统fsync成功是执行者观察，不冒充独立设备崩溃恢复验证。

初始helper根记录已持久化，但附加单调时钟严格不等断言在相同读数下中断。根记录回读证明成功保存，缓存接续从下一未检查组件开始；没有重复lstat或重读源账本。原辅助异常与修正说明均保留。根组件的顺序通过原代码串行调用及保存确认证明，不依赖严格递增时钟；后续三条也以同一串行规则判断。

命中ANCESTOR_03，第四条；保存确认先于reparse安全分支，STOP事件记录后break。后代调用0，目标跟随0，WASM访问0。完整执行者helpers的raw SHA及必要真实短摘录见source_inventory/source_excerpts；独立执行时见证UNKNOWN。
