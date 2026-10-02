# 官方句柄生命周期文档补充

2026-10-01 · Work TASK28 / Builder dialogue2 · CANDIDATE_DOCUMENTARY_TEXT_ONLY，待 Work 独立审查。

仅使用 hash-first 核验的本地文本；不渲染 HTML、不执行脚本或示例、不跟随引用、不联网。行号为原 HTML 的 1-based 行号；引文去标签、解码实体并折叠排版空白。解释与原文分列。

## 来源与文档元数据

| ID / 文件 | Requested URL = captured responseRequestURI | SHA256 |
|---|---|---|
| S / official_setfileinformationbyhandle_20261001.html | https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle | C4F3F396563F5D4ECDA8BB7611402BC6D32F6515250CAD1A6119F4313FED4885 |
| C / official_ntclose_20261001.html | https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntclose | D7252729FB90988F08694FA4D320C8DCBE8466BE479440F6D4C7C00FD34FF84E |

两个本地文件均在本补充同目录。Batch2 回执记录 retrieved_utc=2026-10-01T08:35:04.6166111Z、两页 HTTP200/text/html、response URI evidence=CAPTURED_RESPONSE_REQUEST_URI，consumed2/rem0/retry0；本轮未重新获取。Batch1 的 consumed3/rem0、returnedURL NOT_CAPTURED/fullprovenance NOT_PASS 保留，不被 batch2 修复。

- S：ms.date=2018-12-05T00:00:00Z（L73）；最低 client 为 Windows Vista [desktop apps | UWP apps]（L1049–1050），server 为 Windows Server 2008 [desktop apps | UWP apps]（L1053–1054）。
- C：ms.date=2018-12-05T00:00:00Z（L73）；最低 client 为 Windows 2000 Professional [desktop apps only]（L863–864），server 为 Windows 2000 Server [desktop apps only]（L867–868），Target Platform: Windows（L871–872）。

上述是页面元数据，不是实际 host/build/filesystem/SDK/API 版本或适用性证明；目标组合均 UNKNOWN，平台支持 NOT_ESTABLISHED。

## 精确条款与限定解释

**S01 · L853–856 · 返回值原文**
> Returns nonzero if successful or zero otherwise.
> To get extended error information, call GetLastError.

解释：仅记录返回约定；GetLastError 文献未读，未形成调用步骤或任何失败撤销、部分对象责任证明。

**S02 · L858–862 · 范围原文**
> Certain file information classes behave slightly differently on different operating system releases. These classes are supported by the underlying drivers, and any information they return is subject to change between operating system releases.
> The following table shows the valid file information classes and their corresponding data structure types for use with this function.

页面表格（L868–920）的类／结构为 FileBasicInfo/FILE_BASIC_INFO、FileRenameInfo/FILE_RENAME_INFO、FileDispositionInfo/FILE_DISPOSITION_INFO、FileAllocationInfo/FILE_ALLOCATION_INFO、FileEndOfFileInfo/FILE_END_OF_FILE_INFO、FileIoPriorityHintInfo/FILE_IO_PRIORITY_HINT_INFO。这只是本页表格的文本范围，不选定接口，也不将跨 release 语义视为恒定保证。

**S03 · L924–929 · access 前提原文（至第二句结束）**
> You must specify appropriate access flags when creating the file handle for use with SetFileInformationByHandle. For example, if the application is using FILE_DISPOSITION_INFO with the DeleteFile member set to TRUE, the file would need DELETE access requested in the call to the CreateFile function.

解释：只支持文中 DELETE access 必要条件；未读 CreateFile 或权限文献，不证明指定叶身份、授权、所有权、并发替换隔离或删除完成。

**S04 · L932–938 · transaction 原文（前三句）**
> If there is a transaction bound to the handle, then the changes made will be transacted for the information classes FileBasicInfo, FileRenameInfo, FileAllocationInfo, FileEndOfFileInfo, and FileDispositionInfo. If FileDispositionInfo is specified, only the delete operation is transacted if a DeleteFile operation was requested. In this case, if the transaction is not committed before the handle is closed, the deletion will not occur.

解释：保留 transaction-bound 前提和未提交则不删除的限制；未读 TxF/DeleteFile 引用，不据此推断普通路径操作、整体父链或四操作检查至变更的原子性。

**C01 · L806 · Deprecated 原文（完整段落）**
> Deprecated. Closes the specified handle. NtClose is superseded by CloseHandle.

解释：NtClose 为 deprecated，页面明确指出 replacement；不得将其当作获推荐的当前 API。CloseHandle contract=NOT_READ，未跟引用、未采用／替换 API、未改代码。

**C02 · L813–816、L825–829 · 参数及返回原文**
> The handle being closed.
> The various NTSTATUS values are defined in NTSTATUS.H, which is distributed with the Windows DDK.
> STATUS_SUCCESS
> The handle was closed.

解释：页面仅列这一成功状态描述；未读头文件、不补猜其他返回码或失败后的对象状态。

**C03 · L834–850 · 对象范围原文**
> The NtClose function closes handles to the following objects.

页面逐项为 Access token, Communications device, Console input, Console screen buffer, Event, File, File mapping, Job, Mailslot, Mutex, Named pipe, Process, Semaphore, Socket, Thread。仅记录对象列表；不推导对象持有、转移、关闭时机、失效、父链寿命或 user/kernel 上下文保证。本页未明确说明这些上下文条件，保持 NOT_ESTABLISHED，不搬入 driver/kernel 契约。

**C04 · L852 · 文献限制原文**
> Because there is no import library for this function, you must use GetProcAddress.

解释：仅忠实记录页面文字，不执行或建议加载／调用。Requirements 同页列 Library: ntdll.lib（L879–880）；此表项与 L852 的叙述并列保留，不自行消解或据此建立实现方案。

## 窄映射与保留缺口

S01/S03/S04 仅补充 specified_leaf_unlink 的局部返回、access 与事务限制；C01–C04 仅补充关闭句柄的文献范围和弃用限制。二者均未建立指定叶与名字绑定、稳定身份、全父链、并发替换、所有权、原子性、清理、持久化或完成／失败／部分删除责任。

anchor_directory 仍缺父链与句柄存续证明；root_claim、each_recursive_mkdir_parent、exclusive_json_npz_create、specified_leaf_unlink 四个操作各自的身份、检查至变更窗口、完成／失败／部分对象责任均 NOT_ESTABLISHED。局部条款不得拼成全链保护。

完整 Objective A 保留：principal/token、same-token、特权/admin writer、DACL/ownership、rename/delete、reparse、cross-volume，及 loader/cache/constructor/callback/transitive dependency、stdout/stderr、行政 capture 威胁；未覆盖能力不假定不存在。四机制 × 四操作的16项全部 UNRESOLVED，window UNACCEPTED，六根定位授权缺口保留，拒绝状态 STOP__UNRESOLVED。

本轮仅两份新文档，不读代码、数据、真实根或其他树。全部 runtime/import/AST/compile/test/probe/HTMLexecution/DLL/native/experiment/model/science/consumer/actualdata/protectedroot 调用0；新HTTP0。旧 actualdata/fixture/archiveadmin/V1/V2 各 consumed1/rem0，不重置。C9PAUSED、A3仅已完成准备例外、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE 保留；历史C8科学证据保留，当前条件链调用0。

交付后 STOP 等待 Work 独立文档审查；不自验收、不创建后继、不授权实验或新预算。
