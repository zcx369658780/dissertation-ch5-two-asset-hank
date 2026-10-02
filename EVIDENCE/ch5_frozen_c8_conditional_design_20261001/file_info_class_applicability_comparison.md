# 文件信息类与结构适用性对照

2026-10-01 · TASK37 / Builder dialogue7 · DOCUMENTARY_CANDIDATE_ONLY，待 Work 独立审查。

## 来源身份与获取元数据

|ID／文件|SHA256|URL事实|
|---|---|---|
|S／official_file_id_info_batch5_20261001.html|495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE|HTML canonical L19：https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info 。本任务允许输入未含 batch5 获取回执，requestedURI/capturedURI **NOT_ESTABLISHED_IN_THIS_READSET**，不把canonical当成返回URL。|
|E／official_file_info_by_handle_class_batch6_20261001.html|CD329BDC284956E2BDDDF22288A7046C212A6B21BED6F99DFAD6B066EAD9D6AE|获准 batch6 回执 FF56E2562A69AA5E5E8744F3FBA9C56BC1F39D30F9E7BF7BB7722226B58DEE7A：requested https://learn.microsoft.com/en-us/windows/desktop/api/minwinbase/ne-minwinbase-file_info_by_handle_class ；captured responseURI https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ne-minwinbase-file_info_by_handle_class 。|

E 回执记录 HTTP200/text/html、retrieved_utc 2026-10-01T10:44:26.6816359Z、一次获取consumed1/rem0。本轮未重新获取、未跟引用。

## 原文与限定解释

行号为原 HTML 1-based；去标签、解码实体、折叠排版空白，不渲染或执行。

**S01 · S L831–832 · Requirements 原文**
> Minimum supported client
> None supported

**S02 · S L835–836、L839–840 · 原文**
> Minimum supported server
> Windows Server 2012 [desktop apps only]
> Header
> winbase.h (include Windows.h)

S ms.date=2018-12-05T00:00:00Z（L73）。这里只忠实记录结构页最低支持栏，不自行将 None supported 改为 Windows 客户端版本。

**E01 · E L899 · FileIdInfo 项原文（完整单元格）**
> FileIdInfo
> File information should be retrieved. Use for any handles. Use only when calling GetFileInformationByHandleEx. See FILE_ID_INFO.
> Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP: This value is not supported before Windows 8 and Windows Server 2012

**E02 · E L934–935、L938–939、L942–943 · Requirements 原文**
> Minimum supported client
> Windows Vista [desktop apps | UWP apps]
> Minimum supported server
> Windows Server 2008 [desktop apps | UWP apps]
> Header
> minwinbase.h (include Windows.h)

E ms.date=2018-12-05T00:00:00Z（L73）。枚举整体最低版本与 FileIdInfo 成员自己的限制分别记录，不将 Vista 枚举可用性当成该成员可用性。

## 未解决的客户端适用性差异

结构 S 的 client None supported 与枚举 E 中 FileIdInfo 的版本限制并列保留，分类 **UNRESOLVED_DOCUMENTARY_APPLICABILITY_DISCREPANCY**。E 的“此前不支持”不能被改写为在指定 Windows 11 上已支持，也不能据此静默修复 S、证明 ABI、API实际可用性或 installed SDK。Header 列表与 ms.date 是文档元数据，SDK/API版本及安装状态仍 UNKNOWN。信息类名称本身不证明身份字段或稳定对象绑定。

Owner 已指定本机 Windows11专业版/10.0.26200/build26200/64位+D:NTFS为未执行研究拟定平台；这一指定不调和文献差异或授权探测。Owner 六根定位确认（FC345EFF1E5E9575B7ECD7554490FBB1FD30B222A97D19D0D03EE3F83DEEFAEC）仅使定位缺项 CLOSED_OWNER_DECLARED，机器身份／ACL／ownership／保护验证仍 NOT_ESTABLISHED，root_access_authorized=false。

不采用 API、不测试／probe、不外推父链、并发替换、窗口原子性或保护 PASS。完整 Objective A及16 UNRESOLVED、window UNACCEPTED继续保留；六根的文字定位与物理身份事实分开。C9PAUSED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE不变，TASK29/33失败保留，历史C8科学保留、当前条件链0。

本轮reports路径访问/exists/hash/body0、系统query/HTTP/研究runtime/import/AST/compile/test/native/DLL/isolation/experiment/model/science/consumer/realdata0。所有旧耗尽预算不重置；STOP Work独立审查，不向Owner发问、不自验收或签发后继。

