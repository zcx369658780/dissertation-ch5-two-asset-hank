# 拟定平台 API 文献候选比较

2026-10-01 · TASK32 / Builder dialogue5 · **ADVISORY_ONLY__DOCUMENTARY_EVIDENCE_READINESS**；待 Work 独立验收，不采用机制或 API。

Owner 原话“我确认，请继续”，通过 owner_target_platform_designation_20261001.md（SHA256 B5467EF5BB4649BD8860F0E7E6109E8AB0157A4C56916D0E62E7DCDBBC17DEEA）指定本机 Windows 11 专业版 / Version10.0.26200 / Build26200 / 64位及 D: NTFS 为未执行隔离研究拟定平台。基础值来自已接受的被动读回 A7DAEBE493FE3327A09B527974ACEA574579D909F60F2EF096BF5BAE13A240F1。该指定属于 OwnerDeclared target designation；读回及旧文档中的原 UNKNOWN 状态不追溯改写。provider 内部读取范围未证明。

API 名称、页面 ms.date、最低 OS 元数据、实际 SDK/API 版本与安装状态是不同事实。Owner 指定平台不验证 SDK/API，不证明 Windows build26200 或 NTFS 上的具体契约适用性，SDK/API 仍 UNKNOWN。

## 候选的证据就绪程度

| 候选片段 | 已有局部文献事实 | 尚缺证据／分类 |
|---|---|---|
| NtCreateFile + OBJECT_ATTRIBUTES：native user-mode relative-name 候选 | 既有摘录 N01 明确 user-mode 定位；N02 非空 RootDirectory 时 ObjectName 相对该目录；N03 FILE_CREATE 冲突行为；N04 目录 flag/disposition；N07 reparse 打开行为；N10 返回状态。O01 区分文件系统目录与 object-manager 目录。 | **PARTIAL_DOCUMENTARY_FACTS_ONLY**。不导入未读 WDK/kernel 契约；没有全父链、稳定身份、并发替换隔离、拥有权、原子性或六根授权证明。batch1 returnedURL NOT_CAPTURED/fullprovenance NOT_PASS 保留。 |
| SetFileInformationByHandle + FILE_DISPOSITION_INFO：Win32 信息／删除片段 | 既有 F01/F02 仅给适用接口、DeleteFile 字段及 DELETE_ON_CLOSE no-effect；S03 DELETE access 前提例；S04 transaction-bound 删除及 commit/close 限制；S01 零／非零返回。 | **PARTIAL_DOCUMENTARY_FACTS_ONLY**。不能据此补出 Win32 创建链或 relative-root 保证；指定叶身份、失败／部分状态和普通删除原子性未建立。 |
| CloseHandle：Win32 关闭片段 | 本轮 raw pinned HTML 的窄条款见下。NtClose 已在接受的摘录中明确 Deprecated/superseded by CloseHandle，因此不作为首选候选。 | **LOCAL_CLOSURE_TEXT_ONLY**。读取 replacement 文献不采用／替换 API；关闭成功不证明全资源清理、寿命所有权、父链或全链保护。TASK29 草稿与 STOP 不修改、不追溯 ACCEPT。 |

建议仅按缺口继续准备文献候选，优先补创建契约、信息查询语义与结构适用范围；这是证据就绪度建议，不是执行顺序、API 选择或实现方案。现有片段不足以推荐可运行的保护机制。

## CloseHandle 本轮原始文本

来源：official_closehandle_20261001.html，SHA256 B12348AC1EC853B469CE5626A4EFF89825A3E3723C71071105DFE1F3F817F8BF；known requestedURL 为 https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle 。本轮未读 acquisition receipt，不新增 responseURI 捕获事实。ms.date=2018-12-05T00:00:00Z（L73）；最低 client Windows 2000 Professional [desktop apps | UWP apps]（L877–878），server Windows 2000 Server [desktop apps | UWP apps]（L881–882）。仅是文档元数据。

原 HTML 1-based 行号；引文去标签、解码实体、折叠空白。

**L814–816 · 返回原文**
> If the function succeeds, the return value is nonzero.
> If the function fails, the return value is zero. To get extended error information, call GetLastError.

**L817 · debugger 段首句**
> If the application is running under a debugger, the function will throw an exception if it receives either a handle value that is not valid or a pseudo-handle value.

**L844 · 前三句**
> The documentation for the functions that create these objects indicates that CloseHandle should be used when you are finished with the object, and what happens to pending operations on the object after the handle is closed. In general, CloseHandle invalidates the specified object handle, decrements the object's handle count, and performs object retention checks. After the last handle to an object is closed, the object is removed from the system.

解释：计数原词为 handle count，不改成统一 reference count；pending I/O 后果仍委托给对象创建函数文献，未跟引用，不推导通用取消／完成规则。L847 明文限制 thread/process handle close 不终止或移除对应对象；L848 file mapping close 可以成功而视图仍打开；L849–850 排除 socket/registry-key close。对象特殊限制与 L844 一并保留，不宣称所有资源已移除。

## 五接口与四操作缺口

| 接口／既有键 | 支持的窄片段 | 保留缺口 |
|---|---|---|
| anchor_directory／锚定前提，非第五类操作 | N02/O01；本轮 CloseHandle 关闭文字 | 全父链、抗替换身份、当前主体适用性、持有／转移／失效寿命。 |
| claim_root／root_claim | N02/N03/N04/N07/N10 | 根授权、并发身份、原子认领、完成／失败／部分状态。 |
| mkdir_each_parent／each_recursive_mkdir_parent | N02/N04/N10 | P0…Pn 每层绑定、递归语义、窗口及部分创建责任。 |
| create_exclusive_json_npz_leaf／exclusive_json_npz_create | N03 既存冲突；N05/N06 共享兼容文字 | 全链排他、JSON/NPZ 写入、持久性、失败／部分清理。 |
| unlink_specified_leaf／specified_leaf_unlink | F01/F02、S01/S03/S04；关闭局部限制 | 叶名与句柄绑定、并发替换、检查至删除原子性、完成／失败／部分删除。 |

完整 Objective A（principal/token、same-token、特权/admin writer、DACL/ownership、rename/delete、reparse、cross-volume，以及 loader/cache/constructor/callback/transitive dependency、stdout/stderr、行政 capture）不缩小。16项 UNRESOLVED、window UNACCEPTED、六根授权缺失、STOP__UNRESOLVED 保留。

本轮查询/CIM/DriveInfo/HTTP/研究runtime/import/AST/compile/test/native/DLL/experiment/model/science/consumer/realdata/protectedroot0。已用行政查询2/rem0、HTTP3+2+1/rem0；旧actualdata/fixture/archiveadmin/V1/V2各1/rem0不重置。C9PAUSED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；历史C8科学保留，当前条件链0。STOP Work 独立审查，不自验收、不问 Owner、不签发后继。
