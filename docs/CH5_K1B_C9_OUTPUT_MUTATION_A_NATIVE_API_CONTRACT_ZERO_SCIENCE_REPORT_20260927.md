# C9 安全目标 A：Windows 官方/API 合同核查（零科学）

状态：只读官方文档候选，待 GPT Work 独立 ACCEPT/REJECT；不授权隔离实验、实现或运行。签发 baseline/parent `9ba9cd330790250902bb0eae061148ce31faa819`；`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。Owner A 保留并发/恶意路径替换 containment 目标；精确解释器的独立 ACCEPT 仅证明 Python 标准库能力快照，其 `os.mkdir`/`os.open`/`os.unlink` 等不在 `supports_dir_fd`。本轮不调用主机或 native API。

## 官方页面台账

所有以下请求均于 **2026-09-27（Asia/Shanghai）** 只读访问。按**去掉 URL fragment 后的文档资源**计，共核对 **13 个唯一官方资源：11 个 HTTP 200、2 个 HTTP 404**；Python `os.html` 的 `supports_dir_fd`、`mkdir`、`open`、`unlink` 四个锚点均归为同一资源。相对已接受设计/能力报告的既引资源，新增直接相关资源共 **6 个**（4 个有效 WDK/Native 页面与 2 个 404 误用 URL），未超过 8 页上限。每条引文仅支持“证明”栏所述内容；不能把 API 存在推成完整 containment。

| 官方 URL（状态） | 短原文 | 证明；不证明 |
| --- | --- | --- |
| [Python 3.11 `os.supports_dir_fd`](https://docs.python.org/3.11/library/os.html#os.supports_dir_fd)（200） | “Different platforms provide different features”；不支持时传非 `None` `dir_fd` “will throw an exception” | `dir_fd` 是条件性接口；不证明目标构建支持。精确解释器独立收据中的 false 向量才是本机证据，也不证明 native 路线不存在。 |
| [Python 3.11 `os.mkdir`](https://docs.python.org/3.11/library/os.html#os.mkdir)、[`os.open`](https://docs.python.org/3.11/library/os.html#os.open)、[`os.unlink`](https://docs.python.org/3.11/library/os.html#os.unlink)（同一 `os.html` 页面，200） | “If a parent directory in the path does not exist, FileNotFoundError is raised”；签名含 `dir_fd=None` | 文档列相对 FD 参数及普通缺父行为；签名不证明 Windows 实现可用或防重解析。 |
| [Win32 `CreateFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)（200） | “You must set this flag to obtain a handle to a directory”；`CREATE_NEW` “Creates a new file, only if it does not already exist”；`FILE_SHARE_DELETE` “Enables subsequent open operations ... to request delete access” | 目录句柄、独占叶创建与 share 选项有公开合同；其路径输入、最终 `FILE_FLAG_OPEN_REPARSE_POINT` 或 share 选择不证明所有祖先无 junction/替换，也不提供以已验证目录句柄为相对根的完整创建链。 |
| [Win32 `CreateDirectoryW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectoryw)（200） | `BOOL CreateDirectoryW([in] LPCWSTR lpPathName, ...)`；“The path of the directory to be created” | 是路径式单层目录创建；页面未给父目录 HANDLE/`RootDirectory` 参数，不能单独覆盖每层递归 mkdir 的 anchored 合同。 |
| [Win32 `DeleteFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-deletefilew)（200） | `BOOL DeleteFileW([in] LPCWSTR lpFileName)`；“marks a file for deletion on close” | 公开路径删除及延迟删除语义；不证明以已验证父句柄为锚的安全 `unlink`。 |
| [Win32 `SetFileInformationByHandle`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle)（200） | 首参 `HANDLE hFile`，“handle to the file for which to change information” | 对已取得的目标句柄可设置删除相关信息；不证明如何无竞态、无重解析地取得**正确目标**句柄或与 `Path.unlink` 语义等价。 |
| [Win32 `GetFileInformationByHandleEx`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex)（200） | `BOOL GetFileInformationByHandleEx([in] HANDLE hFile, [in] FILE_INFO_BY_HANDLE_CLASS FileInformationClass, ...)`；`FileIdInfo (0x12)` | 可查询已打开句柄的身份信息类；不绑定之后的字符串路径 mutation。 |
| [Win32 `FILE_ID_INFO`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info)（200） | “To determine whether two open handles represent the same file, combine the identifier and the volume serial number ... and compare them.” | 可比较两个已打开句柄；不证明 FileId 永不复用、句柄存续期间完整 rename/delete 安全或跨卷 containment。 |
| [Native `OBJECT_ATTRIBUTES`](https://learn.microsoft.com/en-us/windows/win32/api/ntdef/ns-ntdef-_object_attributes)（200，新增） | `RootDirectory` 非 NULL 时名称相对该目录；`OBJ_DONT_REPARSE`：“no reparse points will be followed when parsing the name ... If any reparses are encountered ... STATUS_REPARSE_POINT_ENCOUNTERED” | 对该名称解析有相对根和拒绝 reparse 标志；不证明初始根句柄可信、所有后续操作均采用同一锚或目标用户态调用链已受支持。 |
| [WDK `ZwCreateFile`](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatefile)（200，新增） | “pathname relative to the directory file represented by the handle in the RootDirectory member”；`FILE_CREATE` 在已存在时出错，`FILE_DIRECTORY_FILE` 标识目录 | 存在相对创建与目录/独占 disposition 原语；不证明递归各层、祖先/末端 junction、共享与清理的完整组合合同，亦非现有 Python 路径调用。 |
| [WDK `Using Nt and Zw versions`](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/using-nt-and-zw-versions-of-the-native-system-services-routines)（200，新增） | “User-mode applications can access these routines by using system calls”；用户态调用 Nt/Zw 参数按用户源处理 | 说明用户态可经 system call 访问；此 WDK 页面不等于给本项目一个稳定、完整、可维护的用户态 ABI/绑定与所有安全语义。 |
| [WDK `ZwSetInformationFile`](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetinformationfile)（200，新增） | “Request to delete the file when it is closed or cancel a previously requested deletion.”；“The caller must have opened the file with the DELETE flag set in the DesiredAccess parameter.” | 说明**正确目标句柄已经取得后**的删除原语；不证明安全相对打开叶、祖先拒绝 reparse 或等价于当前 `Path.unlink`。 |
| [误用的 `fileapi/GetFileInformationByHandleEx`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandleex) 与 [误用的 `wdm/NtCreateFile`](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatefile)（各 404，新增） | `UNAVAILABLE` | 两个精确 URL 不可取证；已使用上列可访问的 `winbase` 与 `ZwCreateFile` 页面分别陈述其有限合同，不从 404 推断 API 不存在。 |

`CreateFileW` 的 `FILE_FLAG_OPEN_REPARSE_POINT` 原文为 “Normal reparse point processing will not occur; CreateFile will attempt to open the reparse point”。它不能被扩写成对每个**祖先**路径组件的保证。Win32 公共路径 API、WDK/Native NT 的 `RootDirectory`/`OBJ_DONT_REPARSE` 和 Python `dir_fd` 分属不同接口层；把各页面的局部句子拼接，仍不是受支持的端到端用户态合同。

## 四项必需变更的合同判定

| 操作与当前窗口 | 候选 API 所需但尚未闭合的条件 | 判定 |
| --- | --- | --- |
| 初始 output root claim：delegate 198–207 行在父检查后路径式 `mkdir`、再 `lstat` | 可信父句柄如何无竞态取得；相对建根时拒绝祖先及最终 reparse；创建 disposition、所需 access/share、失败时保留或清理根、跨卷禁止/处理；FileId/句柄生命周期与并发 rename/delete | `UNRESOLVED__FAIL_CLOSED`。`RootDirectory`/`OBJ_DONT_REPARSE` 是相关原语，不是完整 root-claim 证明。 |
| `mkdir(parents=True)`：293–332、352–358 行的最终检查后仍由原始 `Path.mkdir` 递归按路径解析 | **每层**从上一个已验证句柄相对创建，正确区分缺父/已存在、拒绝 junction/symlink，面对根或父目录同时替换时不外逸；每层错误与部分创建清理 | `UNRESOLVED__FAIL_CLOSED`。`CreateDirectoryW` 是路径式；单次 `ZwCreateFile` 文档不自动闭合整条递归链。 |
| 独占 JSON/NPZ：146–180 行 `output_target` 检查后以 `open("x")`/`open("xb")` 创建 | 已验证父句柄下的相对 `FILE_CREATE`/`CREATE_NEW`、所需权限/share、祖先/末端 no-reparse、写入失败/句柄关闭/部分叶清理；不能以叶独占替代父 containment | `UNRESOLVED__FAIL_CLOSED`。现有 `open` 路径仍可在检查后重解析。 |
| `unlink`：281–291、359–361 行检查后原始路径删除 | 相对父锚安全取得**指定叶**句柄；DELETE access/disposition、reparse/junction、open-handle share/rename/delete 交互、最后关闭与失败结果、跨卷边界；防删替换根下叶 | `UNRESOLVED__FAIL_CLOSED`。句柄删除原语不解决安全取得句柄与全链整合。 |

官方材料未建立这四项在**目标 Windows build、精确 Python 解释器与现有 runner**上的一个完整、受支持、可审查用户态相对变更合同。尤其尚未证明持有父/root handle 时并发 rename/delete 的 share mask 效果、FileId 重用/生命周期、祖先 versus 最终组件重解析、错误与句柄清理及跨卷上界。因此本阶段**不提出已可执行的隔离实验规格**：连同安全的精确可丢弃根和 first-failure 预算，须等 Work 取得缺失官方合同并另签任务后再定。未选择较弱威胁模型 B，也未用 `ctypes` 可调用性补空白。

本轮主机探测、ctypes/native API 调用、代码/测试、临时目录变更、preflight、`--execute`、wrapper、模型和科学调用均为 `0`；无新 `reports/` 根。原先两次被禁止的 `--execute` 探测仍是历史违规；历史 REJECT 与有限 ACCEPT 保持各自原范围。旧、新 C9 尝试均已消耗，两份实际调用账本仍为 `CALL_LEDGER_UNRESOLVED`；C10、重试、部分续跑及 Results 关闭，Results eligibility `FALSE`。六个受保护输出根与七项 manifest/readback 原始 SHA-256 已只读核对，映射见收据。

下一门仅为 GPT Work 对本设计候选独立 ACCEPT/REJECT。无论裁决如何，本 Codex 会话到达 30 轮后不得接下一写入任务，由 Work 按 `AGENTS.md` 安排交接；本任务不创建继任任务或交接文件。本报告及收据的原始哈希、candidate/tree 在提交后交接，避免自引用。
