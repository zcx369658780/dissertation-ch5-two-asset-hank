# C9 output mutation A1：用户态 `NtCreateFile` 官方合同核查（零科学）

状态：Builder 文档候选，待 GPT Work 独立 ACCEPT/REJECT。签发 HEAD 为 `265f3c6c074e5924699f0effe1e0a4969a8ea1a3`；冻结 `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。Owner 的 A 目标保留并发及恶意路径替换防护。本报告不提出可执行设计或隔离实验。

## 唯一新增官方资源

| URL、状态与日期 | 官方短原文 | 能证明；不能证明 |
| --- | --- | --- |
| [Microsoft Learn：`NtCreateFile` 用户态页面](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile)，HTTP GET 200；HTTP `Date: Sun, 27 Sep 2026 01:46:12 GMT`；页面 `Last-Modified: Wed, 05 Aug 2026 07:36:44 GMT` | “This function is the user-mode equivalent to the ZwCreateFile function documented in the Windows Driver Kit (WDK).” 语法为 `__kernel_entry NTSTATUS NtCreateFile(...)`；Requirements 列 `winternl.h`、`ntdll.lib`、`ntdll.dll`；Remarks 允许用 `LoadLibrary`/`GetProcAddress` 动态链接。`RootDirectory` 非 NULL 时，`ObjectName` 相对该目录句柄。 | 这是明确的用户态调用、参数及相对目录名合同，补足旧 WDK 页面不能独自证明的接口层。它不证明初始目录句柄可信、全部后续变更均锚定该句柄、目标解释器已有绑定，或完整 containment。 |

同一 URL 的 Parameters 与 Remarks 给出以下局部合同（引文去掉排版标记，未改文字）：

| 项目 | 官方短原文 | 证明范围与缺口 |
| --- | --- | --- |
| `RootDirectory` | “If this value is non-NULL, the ObjectName member specifies a file name relative to this directory.” | 证明相对名解析；不证明根句柄起点可信或全链防替换。 |
| `FILE_CREATE` | “If the file already exists, fail the request and do not create or open the given file. If it does not, create the given file.” | 证明叶的独占创建 disposition；不证明父目录 containment。 |
| `FILE_DIRECTORY_FILE` | “With this flag, the CreateDisposition parameter must be set to FILE_CREATE, FILE_OPEN, or FILE_OPEN_IF.” | 证明可配合的 disposition；不证明逐层递归创建安全。 |
| 先前打开句柄与分享 | “For a shared file to be successfully opened, the requested DesiredAccess parameter to the file must be compatible with both the DesiredAccess and ShareAccess specifications of all preceding opens that have not yet been released with NtClose.” | 证明局部 access/share 相容条件；不证明敌对 rename/delete 下的身份生命周期及全链 containment。 |
| `ObjectAttributes.Attributes` | “This value can be zero or OBJ_CASE_INSENSITIVE, which indicates that name-lookup code should ignore the case of the ObjectName member rather than performing an exact-match search.” | 此用户态页面没有给出 `OBJ_DONT_REPARSE` 用法；旧 Native 结构页面的标志说明不可无条件移植。 |
| 用户态链接 | Requirements 列 `Header | winternl.h`、`Library | ntdll.lib`、`DLL | ntdll.dll`；Remarks：“You can also use the LoadLibrary and GetProcAddress functions to dynamically link to NtDll.dll.” | 证明所列接口入口及链接方式；不证明项目已有受支持绑定或四操作安全链。 |

Microsoft 用户态 `NtCreateFile` 页面关于 `FILE_OPEN_REPARSE_POINT` 的原文是：“Open a file with a reparse point and bypass normal reparse point processing for the file.” 这只说明打开目标文件时的局部处理（“for the file”）；不能推出所有祖先组件均被拒绝，也不能闭合四操作 containment 合同。

页面在文件位置语境写道：“Calls to NtSetInformationFile with the FileInformationClass parameter set to FilePositionInformation must specify an offset that is an integral of the sector size.” 它没有给出指定叶删除的用户态链接或 disposition 合同。本轮未猜测 URL。与已接受的 13 个去 fragment 唯一资源逐项比较，新增资源仅上述 **1 个**，HTTP 200 为 1、404 为 0；旧 13 个的 11×200、2×404 保留原状态，不重复计入新资源。该页面的 HTTP HEAD 存在性先前仅为线索，本轮 GET 正文才用于以上有限事实。

## 四项现有变更的合同结论

| 操作 | 此页新增的局部合同 | 尚未由官方用户态材料闭合的必要环节 | 判定 |
| --- | --- | --- | --- |
| 初始 output root claim | 可相对先前取得的目录句柄使用 `RootDirectory`，目录创建 disposition 有说明。 | 如何可信、无竞态地取得父/root 句柄；每个祖先与最终组件的 no-reparse 范围；完整 access/share、并发 rename/delete 时句柄身份与生命周期、失败清理及跨卷界限。 | `UNRESOLVED__FAIL_CLOSED` |
| 逐层 recursive `mkdir` | 单次相对目录创建有用户态接口说明。 | 每层以上一层已验证句柄为根的完整链；缺父/已存在分支，祖先及最终 junction/reparse，父目录同时替换、部分创建和错误清理。路径式 `CreateDirectoryW` 不补足该链。 | `UNRESOLVED__FAIL_CLOSED` |
| 独占 JSON/NPZ 创建 | `FILE_CREATE` 提供已存在即失败的叶创建方式。 | 在已验证父句柄下相对创建并拒绝全部不安全重解析；所需 access/share、并发替换、写入失败/关闭/部分文件清理。叶独占不证明父 containment。 | `UNRESOLVED__FAIL_CLOSED` |
| 指定叶 `unlink` | 此页只说明创建/打开；文件位置语境中的 `NtSetInformationFile` 提及不构成删除合同。 | 安全相对取得指定叶句柄，用户态 delete disposition、`DELETE` access/share、reparse 与并发 rename/delete、关闭/失败结果及跨卷边界。路径式 `DeleteFileW` 和已取得句柄后的 WDK/Win32 删除原语不能证明安全寻址。 | `UNRESOLVED__FAIL_CLOSED` |

Python `dir_fd` 在已核对的精确解释器对相关操作不受支持；Win32 路径 API、WDK `ZwCreateFile`/`ZwSetInformationFile` 与本页用户态 `NtCreateFile` 属于不同接口层。官方材料仍未组成目标 Windows build、精确 Python 解释器及现有 runner 上可审查的四操作用户态 containment 合同。**A1 总判定：`UNRESOLVED__FAIL_CLOSED`。** 不提出绑定、实现或可执行隔离实验。

本轮未进行主机/API/`ctypes` 探测、临时目录或 ACL 变更、代码/测试/live 编辑、测试、preflight、`--execute`、wrapper、模型或科学入口；无新 `reports/` 根。历史两次被禁止的 `--execute` 探测仍为违规，全部历史 REJECT 和有限 ACCEPT 不改判。旧、新 C9 尝试均已消耗，实际调用账本均为 `CALL_LEDGER_UNRESOLVED`；C10、重试、部分续跑与 Results 关闭，Results eligibility `FALSE`。下一门仅为 GPT Work 对本候选独立 ACCEPT/REJECT。
