# P3：首次reparse祖先组件已定位，保护基线继续BLOCKED

终态：`STOP__P3_FIRST_REPARSE_COMPONENT_IDENTIFIED__TARGET_NOT_FOLLOWED__BASELINE_BLOCKED`。在WASM_OLD_01的已知祖先链中，自核准SCIENCE_TREE根开始共完成4/16次非跟随lstat；首次reparse命中 `ANCESTOR_03`，第4次、相对根深度3，原始attributes=1040（0x410，目录0x10与reparse 0x400）。命中时刻 UTC=2026-10-28T00:35:38.500154+00:00、北京时间=2026-10-28T08:35:38.500154+08:00。全部4条记录均先写入私有scratch、flush/fsync并原字节回读确认，随后才判断是否安全停止。命中后下级检查0、目标跟随0、WASM文件本体访问0。

## 治理门与状态同步差异

固定发文 `0cec18b4a2cc68920dcc32912ed2f40097151bef` 中完整任务及Owner正式P3批准记录均存在；候选固定parent `0a278dfe1c355e6f8d07254960acb8ba52e3b5d4` 独立记录。现行2026-10-25权威规则第13行规定逐张冻结任务由Owner交本地Codex，在核验工作区后仅按任务范围执行；第28行声明其为最高工作流权威；第32行允许逐张有界只读核查。本轮Owner批准记录第3行明确批准P3及本张祖先诊断。当前Owner消息再次明确转交本任务。

CURRENT.md与TASK_CURRENT.md在此固定提交中最后仍为上一轮ACTIVE_TASK=NONE、P3待Owner批准。本轮没有宣称它们已同步，也未重试GPT受阻的治理大文件写入或绕过安全检查。AGENTS第87行是TASK_CURRENT的“only default execution entry”，第91行禁止由已完成状态启动科学执行；本次有更新、准确的Owner冻结任务与批准，且科学执行预算0。所读最高规则没有把累计ACTIVE_TASK同步写成此类只读任务的强制前置门。因此治理判断为 `ALLOW_BOUNDED_READ_ONLY_WITH_DISCLOSED_CUMULATIVE_STATE_SYNC_GAP`；保留同步缺口，不把它变为科学激活、基线重绑定或后续权限。该解释交GPT独立审阅。

## 保护核验

本次before/after status均 `734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b`、5971个非空NUL记录；HEAD、branch、index、243条refs和11件保护资产前后相同，匹配既有保护身份。旧 `c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3` 状态与观察状态 `734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b` 分开。Owner已正式选择P3，任何当前status均未采纳为新可信基线。保护快照严格2/2，第二次在诊断安全STOP后、证据发布前；其后不再读取科学树。

## 执行者辅助计时断言的记录与缓存接续

第一次helper在根组件记录及其保存确认均已fsync且原字节回读成功后，对两个单调时钟值强制严格小于，因读数相同触发`PERSISTENCE_ORDER_CONFLICT_STOP`。原辅助STOP记录保留。时钟分辨率=0.015625秒；成功保存的原始根属性16、reparse=false及保存确认已从缓存核对。该附加断言不能证明持久保存失败或保护冲突。

随后只从已经持久化的根检查点继续下一未读组件，不重读私有原件、不重复根lstat、不删除任何原记录。使用实际串行控制流“保存返回→回读确认→安全分支”证明顺序，允许有限分辨率时钟数值相同。后续3次lstat同样逐条先保存确认；实际总数仍为4。没有绕过任务关于持久保存失败、权限、reparse或预算的硬停点。此辅助断言修正与真实第4组件reparse安全STOP分别登记，不自称全程无工具问题。

## 输入、来源与限制

只读取获准私有账本1/1次，仅使用WASM_OLD_01的精确旧路径。词法根绑定、无父跳转、原记录编码在私有记录中核对；其他5条路径未使用，optional delta读取0/1。源账本的实际bytes/SHA记录为执行者本地观察，未假称获得此前独立固定的私有原件SHA。实际组件名和全部映射只在Owner私有lookup内。

本轮关闭“哪个匿名祖先先触发reparse及计数缺失”的元数据缺口；未读取reparse tag或目标、WASM存在性/内容、依赖manifest、旧状态原始流，不证明依赖更新、合法重命名、WASM安全、原件变动原因或TEMP31科学来源。上述仍UNKNOWN/BLOCKED。

实际预算：private ledger1/1、optional delta0/1、ancestor lstat4/16、保护快照2/2且每次11件资产。用于核实唯一输入原件为普通文件的对象lstat另记1次，不是WASM文件或祖先链探索。科研、模型、测试、no-HA、预检、WASM内容/执行、目标跟随、目录列举、D盘调查、安装重建、数据或源码写入、清理移动删除均0。

通过普通授权SSH分批发布和固定提交逐项回读后STOP。P3正式批准保持BLOCKED；未来原路线/TEMP31各一活动目录目标无当前清理权限。等待GPT独立验收，不自动Issue/PR/合并或后继。
