# 文件身份与目录创建：窄官方契约
2026-10-01 / TASK35 / DOCUMENTARY_CANDIDATE_ONLY；未执行/渲染HTML或示例，1-based行号、去标签与排版空白。
Identity source：official_file_id_info_batch5_20261001.html SHA495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE，requested https://learn.microsoft.com/en-us/windows/desktop/api/winbase/ns-winbase-file_id_info；captured https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info。
Directory source：official_createdirectorya_batch5_20261001.html SHA29532A4A958D990D1C1531FA4723EBAFF903A2575910698ACE9721928BF20521，requested https://learn.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-createdirectorya；captured https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectorya。
Acquisition receipt F6F56BAA8B0326F579C5BAAC27CB68BD7BD1008BF62E43B57967179DB48859BB：两HTTP200/text-html/各attempt1/consumed2/rem0/retry0，无旧预算重置。

I01 / Identity L804–807：FILE_ID_INFO在GetFileInformationByHandleEx指定FileIdInfo时返回。L816：
> The serial number of the volume that contains a file.
这是字段说明，没有本机卷序列号查询或记录。
I02 / L818–820：
> The 128-bit file identifier for the file. The file identifier and the volume serial number uniquely identify a file on a single computer. To determine whether two open handles represent the same file, combine the identifier and the volume serial number for each file and compare them.
仅同一计算机/两个openhandles条件；没有本页支持的跨主机、跨时刻永久不重用、父链稳定、rename/delete替换隔离或查询到变更原子性证明。
I03 / L831–840 metadata：Minimum supported client = **None supported**；server = Windows Server 2012 [desktop apps only]；header winbase.h(includeWindows.h)。不得改成clientWindows8/Windows11，不以操作系统“更新”或GetFileInformationByHandleEx表格列了FileIdInfo覆盖本结构页限制。当前Windows11 client目标的此项适用性仍NOT_ESTABLISHED，SDK/API版本UNKNOWN。本页没有给出一切生命周期/重用约束，未陈述项UNKNOWN。

D01 / Directory L824–825：
> Creates a new directory. If the underlying file system supports security on files and directories, the function applies a specified security descriptor to the new directory.
D02 / L846–853：lpSecurityDescriptor指定新目录descriptor；lpSecurityAttributes为NULL则defaultdescriptor，ACL从parent继承。
> The target file system must support security on files and directories for this parameter to have an effect.
本页提及GetVolumeInformation/FS_PERSISTENT_ACLS，但未跟文献或调用。不把D:NTFS读回当实际ACL/ownership/权限验证。
D03 / L855–857：成功nonzero，失败zero，extendederror指向GetLastError（未调用）。L867–871 ERROR_ALREADY_EXISTS：
> The specified directory already exists.
L877–882 ERROR_PATH_NOT_FOUND：
> One or more intermediate directories do not exist; this function will only create the final directory in the path.
只有末级创建；不能把它当递归/原子全父链创建或完整部分失败撤销。
D04 / L894–897：securitydescriptor查询可能heuristically determine/report inheritance，所指传播文献未读；不推断ACL一定保持目标保护。
D05 / L952：CreateDirectory alias按UNICODE选择ANSI/Unicode，同段警告中立与非中立混用的编译/运行错误。CreateDirectoryA页不自动证明CreateDirectoryW精确行为。
D06 / L964–981 metadata：clientXP/server2003 desktop/UWP；fileapi.h(includeWindows.h)/Kernel32.lib；仅文献requirements，不验证安装SDK或build26200精确语义。

本轮systemsquery/HTTP/native/runtime/import/AST/compile/test/实验/模型/科学/真实数据/consumer/保护根0。全部ObjectiveA/16/window/sixroot缺口保留，未选择API/机制或证明平台/保护PASS；历史失败原件不改写。