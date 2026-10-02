# 官方平台文档文本摘录

2026-10-01 · TASK27 / Builder dialogue30 · CANDIDATE_DOCUMENTARY_TEXT_ONLY。

这里只摘录已 pin 的本地 HTML，不渲染、不执行、不跟随引用、不重新联网。下列 URL 均为 **requested URL**，不是已验证的返回 URL。三次先前行政 HTTP 请求已 consumed3/rem0，回执记录 HTTP200、text/html；returned_url 均为 null，**returnedURL NOT_CAPTURED / PARTIAL_DOCUMENT_ACQUISITION / full provenance NOT_PASS**。先前 retrieval first_failure=null 仅表示未记录请求／正文获取失败，不消除来源元数据缺口。

## 来源及文档元数据

| 来源ID／本地文件 | Requested URL | 本地 SHA256 |
|---|---|---|
| N / official_ntcreatefile_20261001.html | https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile | 46F7E2CCAE640E46BCFA3C995C862C802B35C5D641438C689B4365FE701D8440 |
| O / official_object_attributes_20261001.html | https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes | D8E88BF91D04CA999B96E43AE8A2093D6F13E5F8CBEF142ADBE675EE0081210C |
| F / official_file_disposition_info_20261001.html | https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_disposition_info | 131D760BC4EC90F48B0AFA1B04E03AEB5BEA70AA0AB185E12BB31EF7F8B57027 |

三份文件位于本文件同一已授权证据目录。行号为原 HTML 的 1-based 行号；引文去掉 HTML 标签，解码文本实体，折叠排版空白，不复制代码语法或示例。

- N：ms.date=2018-12-05T00:00:00Z（L73）；最低 client/server 元数据为空（L83、85），Requirements 仅列 Target Platform: Windows（L1460–1461），最低 OS **NOT_STATED**。
- O：ms.date=2023-08-09T00:00:00Z（L73）；最低 client/server 元数据为空（L83、85），最低 OS **NOT_STATED**。
- F：ms.date=2018-12-05T00:00:00Z（L73）；Minimum supported client: Windows Vista [desktop apps only]（L824–825）；server: Windows Server 2008 [desktop apps only]（L828–829），亦见 L83、85。

这些是文档元数据；不是精确 API 版本确认、实际 host/build/SDK 检查或平台采用。目标平台、build、安装 SDK、适用 API 版本均 **UNKNOWN**；平台支持 **NOT_ESTABLISHED**。

## 精确引文与限定解释

**N01 · N L805 · 原文**
> This function is the user-mode equivalent to the ZwCreateFile function documented in the Windows Driver Kit (WDK).

解释：仅保留页面的 user-mode 定位；未读取 ZwCreateFile 文档，不能将未读取的 driver/kernel 契约自动搬入当前任务。

**N02 · N L1041 · RootDirectory 原文**
> If this value is NULL, the ObjectName member must be a fully qualified file specification that includes the full path to the target file. If this value is non-NULL, the ObjectName member specifies a file name relative to this directory.

解释：支持相对命名的窄文本事实，不证明完整父链、抗替换身份、句柄寿命或受保护根授权。

**N03 · N L1149、1153 · FILE_CREATE 原文**
> If the file already exists, fail the request and do not create or open the given file. If it does not, create the given file.

解释：仅支持既存文件冲突时的这一描述；不证明 JSON/NPZ 写入、持久化、整体排他链或部分文件清理。

**N04 · N L1202、1206 · FILE_DIRECTORY_FILE 原文（前两句）**
> The file being created or opened is a directory file. With this flag, the CreateDisposition parameter must be set to FILE_CREATE, FILE_OPEN, or FILE_OPEN_IF.

解释：仅支持目录类型与所述 disposition 约束，不证明递归各父层关系或认领权限。

**N05 · N L1122、1126 · FILE_SHARE_DELETE 原文**
> The file can be opened for delete access by other threads' calls to NtCreateFile.

解释：仅支持这个共享标志的文本含义，不推导所有删除、重命名或特权攻击者的隔离保证。

**N06 · N L1381 · 原文（首句）**
> For a shared file to be successfully opened, the requested DesiredAccess parameter to the file must be compatible with both the DesiredAccess and ShareAccess specifications of all preceding opens that have not yet been released with NtClose.

解释：仅记录前序未释放 open 的共享兼容描述；未读取 NtClose 契约，不证明所有权转移、关闭时机、父链寿命或 all-attacker 保护。

**N07 · N L1429 · reparse 原文（前两句）**
> If the CreateOptions parameter specifies the FILE_OPEN_REPARSE_POINT flag and NtCreateFile opens a file with a reparse point, normal reparse processing does not occur and NtCreateFile attempts to directly open the reparse point file. If the FILE_OPEN_REPARSE_POINT flag is not specified, normal reparse point processing occurs for the file.

解释：仅描述页面给定的文件打开行为；不外推每一级父链、跨卷、并发替换或完整 reparse containment。

**N08a · N L1261 · FILE_SYNCHRONOUS_IO_ALERT 原文（首两句及末句）**
> All operations on the file are performed synchronously. Any wait on behalf of the caller is subject to premature termination from alerts.
> If this flag is set, the DesiredAccess SYNCHRONIZE flag also must be set.

**N08b · N L1266、1270 · FILE_SYNCHRONOUS_IO_NONALERT 原文（首两句及末句）**
> All operations on the file are performed synchronously. Waits in the system to synchronize I/O queuing and completion are not subject to alerts.
> If this flag is set, the DesiredAccess SYNCHRONIZE flag also must be set.

解释（分别适用于 N08a/b）：所述同步／等待与 SYNCHRONIZE 前提不等于检查至变更原子性，不证明任何四操作链的完成、失败或部分状态责任。

**N09 · N L1374 · 原文**
> For a caller to synchronize an I/O completion by waiting on the returned FileHandle, the SYNCHRONIZE flag must be set.

解释：仅记录等待完成的所述必要标志，不构成调用步骤或当前运行许可。

**N10 · N L1364 · 原文（前两句）**
> NtCreateFile returns either STATUS_SUCCESS or an appropriate error status. If it returns an error status, the caller can find more information about the cause of the failure by checking the IoStatusBlock.

解释：窄返回状态文本，不证明任何失败后的对象撤销、句柄责任或部分状态，也不设计检查程序。

**O01 · O L811 · 原文（末句）**
> The RootDirectory handle can refer to a file system directory or an object directory in the object manager namespace.

解释：保留对象目录与文件系统目录区分；不能与 N02 拼接成已成立的完整父链保证。

**O02 · O L849–850 · OBJ_KERNEL_HANDLE 原文**
> The handle is created in system process context and can only be accessed from kernel mode.

解释：仅支持该 flag 的页面文字，不声称当前 user-mode 主体可获得这一保护。

**O03 · O L878 · driver-specific 原文**
> Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE flag for the Attributes member (by using the InitializeObjectAttributes macro). This restricts the use of a handle opened for that object to processes running only in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running.

解释：明确仅为原文所指 driver routines／kernel 上下文，不类推为 user-mode 契约；未读取所提宏或其他引用。

**F01 · F L802–803 · 原文**
> Indicates whether a file should be deleted. Used for any handles. Use only when calling SetFileInformationByHandle.

解释：只记录该结构页面明确的适用调用限制；未读取、采用或调用所提接口。

**F02 · F L811–813 · DeleteFile 原文**
> Indicates whether the file should be deleted. Set to TRUE to delete the file. This member has no effect if the handle was opened with FILE_FLAG_DELETE_ON_CLOSE.

解释：仅支持字段与这项 no-effect 限制，不证明指定叶解绑、删除完成、并发身份或失败／部分删除责任。

## 候选条款映射与未解决门

| 拒绝接口 | 原有操作键／地位 | 候选窄文本 | 仍缺失的整体证据 |
|---|---|---|---|
| anchor_directory | 目录锚定前提；不是第五类变更操作 | N02、O01；O02/O03 仅 kernel/driver 边界提示 | 稳定身份、全父链绑定、持有／转移／关闭／失效寿命及当前主体适用性 UNKNOWN。 |
| claim_root | root_claim | N02–N07、N08a/b–N10 | 根身份与权限、认领原子性、完成／失败／部分状态责任 NOT_ESTABLISHED。 |
| mkdir_each_parent | each_recursive_mkdir_parent | N02、N03、N04、N07–N10 | 每一父层 P0…Pn 的身份、父链与寿命、检查至变更窗口及部分创建责任 NOT_ESTABLISHED。 |
| create_exclusive_json_npz_leaf | exclusive_json_npz_create | N02、N03、N05–N10 | 指定叶与父链、全程排他性、JSON/NPZ 完成／失败／部分文件责任 NOT_ESTABLISHED。 |
| unlink_specified_leaf | specified_leaf_unlink | N05/N06、F01/F02 | 指定叶身份、名字与句柄绑定、检查至删除关系、完成／失败／部分删除责任 NOT_ESTABLISHED。 |

所有引文只支持局部候选文本事实，不建立四操作全链证据；路径／句柄复核均不被判为充分。完整 Objective A 保留：principal/token、same-token、特权／admin writer、DACL／ownership、rename/delete、reparse、cross-volume；loader/cache/constructor/callback/transitive dependency、stdout/stderr 与行政 capture 威胁均未获豁免，全部攻击者能力仍须独立证据。

acl_dacl / separate_principal / sandbox / appcontainer × 四个原有操作键的 **16 项全部 UNRESOLVED**；检查至变更窗口 **UNACCEPTED**；六个受保护根具体定位授权缺口保留。未读取实际根、原代码、旧 probe、carrier/module 或其他树；未重核 fixed72。整体平台／保护／运行准备支持仍 **UNKNOWN / NOT_ESTABLISHED**，拒绝接口仍 **STOP__UNRESOLVED**。

本轮只新增本文与同目录 official_platform_contract_text_extract_receipt.json。无实验程序、目标路径、合成目标、尝试建议或可运行代码。运行/import/AST/compile/HTMLexecution/probe/DLL/native/test/experiment/model/science/consumer/data/capture/protected-root 均0；HTTP 新请求0，旧3/rem0不重置。旧 actualdata/fixture/archiveadmin/V1/V2 各 consumed1/rem0。C9PAUSED、ObjectiveARETAINED、A3仅已完成的精确未执行准备例外、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；历史 C8 科学保留，当前条件链调用0。

交付后 **STOP 等待 Work 独立审查**。Builder 已到 dialogue30，不自验收、不创建后继、不再接写任务；生命周期接续由 Work 决定。

