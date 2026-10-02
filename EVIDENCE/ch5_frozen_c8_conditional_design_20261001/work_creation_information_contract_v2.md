# 创建与信息查询契约：Work v2 窄摘录
2026-10-01 / TASK34 / DOCUMENTARY_CANDIDATE_ONLY。TASK33原STOP及TASK29原STOP均保留，本新文档不追溯验收失败任务。未渲染或执行HTML、示例；仅文本读取。引文按原HTML 1-based行号，去标签/实体与排版空白。
来源C：official_createfilea_batch4_20261001.html，SHAF7AB6ADE08B0B40CECA1F61D15764CA28A5734E2FD11DA5FFC634AD7C3FC9880。requested https://learn.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea；captured https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea。
来源I：official_getfileinformationbyhandleex_batch4_20261001.html，SHA2843FD68F767D1197F1654CDAE745D7C196381ECF8BC0D76038DA56E04F5E50F。requested https://learn.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-getfileinformationbyhandleex；captured https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex。
来源回执SHA6DA29CF92B285D5D8BD715CD8BBA7B34C0FED37CD43FE555000967C9805CE943，独立batch4各HTTP200/text-html/attempt1、2耗尽，无重试。旧batch1返回URL缺口仍保留。
文献metadata：C L73 ms.date2022-08-16；L1995–2000最低clientXP/server2003 desktop；L2007–2012 fileapi.h(includeWindows.h)/Kernel32.lib。I L73 ms.date2018-12-05；L1024–1041最低clientVista/server2008 desktop/UWP；winbase.h(includeWindows.h)/Kernel32.lib，XP/server2003另列FileExtd.lib。这不是安装SDK/API精确版本或build26200适用性核验。

C01 / L865–866：
> You cannot request an access mode that conflicts with the sharing mode that is specified by the dwShareMode parameter in an open request that already has an open handle.
C L870–872另明确 attributes/extendedattributes访问不受该share flag影响；共享约束不外推为所有主体/权限保护。
C02 / L909–913（FILE_SHARE_DELETE）：
> Enables subsequent open operations on a file or device to request delete access.
> Delete access allows both delete and rename operations.
省略间句含未指定flag/既有deleteaccess时的限制，不能据选句宣称所有删除重命名都可用或都被拦截。
C03 / L995–998（CREATE_NEW）：
> Creates a new file, only if it does not already exist.
> If the specified file exists, the function fails and the last-error code is set to ERROR_FILE_EXISTS (80).
> If the specified file does not exist and is a valid path to a writable location, a new file is created.
仅叶创建条件，不证明全父链排他、JSON/NPZ持久化或部分失败清理。
C04 / L1632–1637：
> An application cannot create a directory by using CreateFile, therefore only the OPEN_EXISTING value is valid for dwCreationDisposition for this use case. To create a directory, the application must call CreateDirectory or CreateDirectoryEx.
C L1175–1180保留backup/restore特权可override securitychecks及目录handle需要BACKUP_SEMANTICS；L1638–1641无SE_BACKUP_NAME/SE_RESTORE_NAME时适当检查仍适用。不能把“打开目录”当递归创建或关闭特权威胁。
C05 / L1231–1236（OPEN_REPARSE_POINT）：
> Normal reparse point processing will not occur; CreateFile will attempt to open the reparse point. When a file is opened, a file handle is returned, whether or not the filter that controls the reparse point is operational.
> This flag cannot be used with the CREATE_ALWAYS flag.
> If the file is not a reparse point, then this flag is ignored.
L1517–1531另区分指定flag时symboliclink本身、未指定时target；不证明每级父链reparse containment。
C06 / L1190–1195（DELETE_ON_CLOSE）：
> The file is to be deleted immediately after all of its handles are closed, which includes the specified handle and any other open or duplicated handles.
既有handles须均FILE_SHARE_DELETE，否则callfail；后续opens未指定该sharemode则fail。不是单一handleclose立即完成的普遍保证。
C07 / L1410–1413成功为openhandle，失败INVALID_HANDLE_VALUE；L1423–1427：
> When an application is finished using the object handle returned by CreateFile, use the CloseHandle function to close the handle. This not only frees up system resources, but can have wider influence on things like sharing the file or device and committing data to disk. Specifics are noted within this topic as appropriate.
本窄摘录未确立所有pending操作的取消/完成责任。
C08 / L1983（alias前句）：
> The fileapi.h header defines CreateFile as an alias that automatically selects the ANSI or Unicode version of this function based on the definition of the UNICODE preprocessor constant.
同段警告编码中立alias与非中立代码混用会造成编译/运行错误。CreateFileA页不能自动作为CreateFileW精确合同或安装版本确认。

I01 / L833–842：handle为被查file的handle，不应为pipe；returnedstructure对应指定FileInformationClass。L846–849：
> If the function succeeds, the return value is nonzero and file information data is contained in the buffer pointed to by the lpFileInformation parameter.
> If the function fails, the return value is zero.
未读GetLastError契约，不构成调用程序。
I02 / L855–857：
> Certain file information classes behave slightly differently on different operating system releases. These classes are supported by the underlying drivers, and any information they return is subject to change between operating system releases.
I03 / L944–947表格：FileIdInfo(0x12)对应FILE_ID_INFO，仅映射事实；未读结构，不能凭类名推出字段、唯一性、身份持久性或防替换保证。
当前Owner指定目标Windows11/build26200/64位+D NTFS；SDK/API UNKNOWN，平台readiness/protection NOT_ESTABLISHED。全部16/window/sixroot缺口及ObjectiveA保留；本任务无系统查询/HTTP/native/运行/模型/科学。