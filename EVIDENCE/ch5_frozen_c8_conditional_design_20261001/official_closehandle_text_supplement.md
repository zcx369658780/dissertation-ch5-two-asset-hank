# CloseHandle 官方文档补充

2026-10-01 · TASK29 / Builder dialogue3 · CANDIDATE_DOCUMENTARY_TEXT_ONLY；待 Work 独立审查。

来源 H：同目录 `official_closehandle_20261001.html`；SHA256 `B12348AC1EC853B469CE5626A4EFF89825A3E3723C71071105DFE1F3F817F8BF`。Requested URL 与回执捕获的 responseRequestURI 均为 https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle 。回执记录 HTTP200/text/html，retrieved_utc=2026-10-01T08:39:02.1360159Z，batch3 consumed1/rem0/retry0；本轮无联网。Batch1/2 消耗及 batch1 returnedURL NOT_CAPTURED/fullprovenance NOT_PASS 均未修复或重置。

ms.date=2018-12-05T00:00:00Z（H L73）；Minimum supported client: Windows 2000 Professional [desktop apps | UWP apps]（L877–878）；server: Windows 2000 Server [desktop apps | UWP apps]（L881–882）。这些只是页面元数据；目标 Windows/build/architecture/filesystem/SDK/API 版本及适用性仍 UNKNOWN，平台支持 NOT_ESTABLISHED。

以下行号为原 HTML 1-based 行号，引文去标签、解码实体、折叠空白；不渲染或执行，不跟引用。解释不是调用建议。

**H01 · L814–816 · 成功／失败原文**
> If the function succeeds, the return value is nonzero.
> If the function fails, the return value is zero. To get extended error information, call GetLastError.

解释：仅为返回约定；GetLastError 文献未读，未建立失败撤销或对象清理责任。

**H02 · L817–819 · debugger／invalid／pseudo-handle 原文**
> If the application is running under a debugger, the function will throw an exception if it receives either a handle value that is not valid or a pseudo-handle value. This can happen if you close a handle twice, or if you call CloseHandle on a handle returned by the FindFirstFile function instead of calling the FindClose function.

解释：保留 debugger 前提和两项页面例子；不执行验证，不跟 FindFirstFile/FindClose 引用。

**H03 · L844 · 待处理操作与计数原文（前三句）**
> The documentation for the functions that create these objects indicates that CloseHandle should be used when you are finished with the object, and what happens to pending operations on the object after the handle is closed. In general, CloseHandle invalidates the specified object handle, decrements the object's handle count, and performs object retention checks. After the last handle to an object is closed, the object is removed from the system.

解释：原文计数是 object's handle count，不改称统一 reference count。待处理 I/O 的具体后果委托给对象创建函数文档，本轮未读这些引用，不能补出通用完成／取消规则或拥有权、父链寿命证明。

**H04 · L845 · invalid-handle 限制原文（完整段落）**
> Generally, an application should call CloseHandle once for each handle it opens. It is usually not necessary to call CloseHandle if a function that uses a handle fails with ERROR_INVALID_HANDLE, because this error usually indicates that the handle is already invalidated. However, some functions use ERROR_INVALID_HANDLE to indicate that the object itself is no longer valid. For example, a function that attempts to use a handle to a file on a network might fail with ERROR_INVALID_HANDLE if the network connection is severed, because the file object is no longer available. In this case, the application should close the handle.

解释：保留 usually 和例外；页面的网络例子仅为引文，不授权网络查询或关闭操作。

**H05 · L846 · transaction 原文（前两句）**
> If a handle is transacted, all handles bound to a transaction should be closed before the transaction is committed. If a transacted handle was opened by calling CreateFileTransacted with the FILE_FLAG_DELETE_ON_CLOSE flag, the file is not deleted until the application closes the handle and calls CommitTransaction.

解释：保留 transacted 和所列 flag 条件；未读相关 API/transaction 文献，不推导普通删除、四操作原子性、失败／部分删除或持久化保证。

**H06 · L847–848 · 对象移除限制原文（L847 前两句、L848 首句）**
> Closing a thread handle does not terminate the associated thread or remove the thread object. Closing a process handle does not terminate the associated process or remove the process object.
> Closing a handle to a file mapping can succeed even when there are file views that are still open.

解释：这些对象限制防止把 H03 泛化为所有资源均已释放；不形成终止线程／进程或清理方案。

**H07 · L849–850 · 排除对象原文（各首句及 L850 末句）**
> Do not use the CloseHandle function to close a socket.
> Do not use the CloseHandle function to close a handle to an open registry key.
> CloseHandle does not close the handle to the registry key, but does not return an error to indicate this failure.

解释：页面分别指向 closesocket/RegCloseKey，引用未读、未跟随；不选择替代 API。

TASK28 已接受文档明确 NtClose Deprecated/superseded by CloseHandle；本次独立任务允许读取 CloseHandle 文本，因而 TASK28 的 NOT_READ 为历史限定。此次读取不采用任何 API、不替换／修改研究代码。

上述窄关闭条款不建立 ownership、父／根／叶稳定身份、全父链、并发替换、检查至变更原子性或整体保护。anchor_directory 前提及 root_claim、each_recursive_mkdir_parent、exclusive_json_npz_create、specified_leaf_unlink 四操作仍需独立证据。

完整 Objective A 保留 principal/token、same-token、特权/admin writer、DACL/ownership、rename/delete、reparse、cross-volume 和 loader/cache/constructor/callback/transitive dependency、stdout/stderr、行政 capture 威胁。16项 UNRESOLVED、window UNACCEPTED、六根授权缺口、STOP__UNRESOLVED 不变。

本轮 metadataquery/CIM/DriveInfo/hostversion/runtime/import/AST/compile/test/probe/HTMLexecution/native/DLL/experiment/model/science/consumer/actualdata/protectedroot0，新HTTP0；旧 actualdata/fixture/archiveadmin/V1/V2 各 consumed1/rem0。C9PAUSED、A3仅已完成准备例外、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE 保留；历史C8科学保留，当前条件链调用0。STOP 等待 Work 独立审查，不自验收、不创建后继或签发执行许可。
