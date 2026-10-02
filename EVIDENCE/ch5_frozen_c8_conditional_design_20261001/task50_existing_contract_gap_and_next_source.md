# 既有官方文本契约缺口与下一来源

2026-10-01 · TASK50 / Builder dialogue13 · DOCUMENTARY_ADVICE_ONLY，待 Work 独立审查。TASK49仍STOP；本任务是新的限定纯文本接续，不重开、修复或重试旧任务。

## 来源与身份层级

六输入限 TASK_CURRENT、work_task49_review_receipt.json、TASK47证明映射、TASK48失败审查、TASK45三页契约报告及 batch4 GetFileInformationByHandleEx HTML。沿用 TASK49 的四项**历史匹配声明**，本轮输入 hash0，未独立fresh核验：

|输入|继承历史 SHA256|
|---|---|
|official_getfileinformationbyhandleex_batch4_20261001.html|2843FD68F767D1197F1654CDAE745D7C196381ECF8BC0D76038DA56E04F5E50F|
|task47_unexecuted_interface_proof_map.md|590E3CDF3A0503E6889BBF111BE813663A7007314E0B13CE778621DD7BF8BB2E|
|work_task48_task47_report_failure_review_receipt.json|65092714C6E4304B370A0C658DC6B0A9BF1896E0831CBB79EA9228E18BF58BF7|
|work_task45_three_page_contract_and_sdk_locator_proposal.md|53122FA7E6049DB107DC053449ED5A8FD15D3BBC4A6FCED1B96D407FCABA931B|

HTML canonical（L19）为 https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex ，ms.date（L73）为2018-12-05T00:00:00Z；canonical不是抓取request/responseURI。本轮无获取回执白名单，返回URI仅有TASK45文档记述，未独立复核获取事实。

## 精确官方文本及局部支持

行号为该允许 HTML 1-based；引文去标签、解码实体并折叠空白，不渲染或执行。

**Q1 · L833–834 · hFile**
> A handle to the file that contains the information to be retrieved.
> This handle should not be a pipe handle.

**Q2 · L836–837、L840–842 · 类型／输出**
> A FILE_INFO_BY_HANDLE_CLASS enumeration value that specifies the type of information to be retrieved.
> A pointer to the buffer that receives the requested file information. The structure that is returned corresponds to the class that is specified by FileInformationClass. For a table of valid structure types, see the Remarks section.

**Q3 · L846–849 · 返回值**
> If the function succeeds, the return value is nonzero and file information data is contained in the buffer pointed to by the lpFileInformation parameter.
> If the function fails, the return value is zero. To get extended error information, call GetLastError.

**Q4 · L855–857 · OS／driver 限定**
> Certain file information classes behave slightly differently on different operating system releases. These classes are supported by the underlying drivers, and any information they return is subject to change between operating system releases.

**Q5 · L944–946 · 表格映射**
> FileIdInfo (0x12)
> FILE_ID_INFO

API页 Requirements L1024–1025记最低client Windows Vista [desktop apps | UWP apps]；L1028–1029最低server Windows Server 2008 [desktop apps | UWP apps]；L1036–1037 Header为winbase.h (include Windows.h)。这些是页面元数据，不证明机器API/ABI、SDK安装或build26200效果。

本页的参数／结构映射和成功缓冲区规则只说明信息查询文本。没有据此建立 parent/root/leaf 稳定身份、授权、拥有权／寿命、变更完成／失败／部分状态或 hostile replacement窗口；定向阅读与词项检查限本页，不能声称其他文献或整个SDK没有相关契约。TASK45分别记录API整体client、成员限制及结构页client栏；层级不同、客户端差异仍UNRESOLVED，SDK/API机器证据UNKNOWN。此处不新读另两页、不调和差异、不采用机制。

## 五接口的文本支持与证明缺口

接口定义来自已获有限建议分类的TASK47报告，非本轮代码读取或验证。其直接拒绝占位不等于运行时fail-closed。

|接口／原有键|当前允许官方页支持|尚缺的操作契约|
|---|---|---|
|anchor_directory／锚定前提，非第五类操作|Q1文件句柄输入、Q2/Q5类型映射可作为信息查询文献片段|目录锚定与完整父链；查得信息与后续对象绑定、句柄取得／持有／转移／关闭。|
|claim_root／root_claim|Q3只有信息查询成功／失败规则|根身份与父子关系、认领权限及完成／失败／部分认领；查询结果不证明变更对象。|
|mkdir_each_parent／each_recursive_mkdir_parent|同一局部查询片段，无本页递归创建契约|每层P0…Pn父／目标身份、寿命、权限及部分创建责任。|
|create_exclusive_json_npz_leaf／exclusive_json_npz_create|Q2/Q5仅映射返回结构，不是排他创建或内容写入|父／根／叶绑定、排他性、完成／持久性、失败／部分文件责任。|
|unlink_specified_leaf／specified_leaf_unlink|Q1/Q3信息查询句柄／返回规则，不是删除完成规则|指定叶绑定、授权、检查至删除关系及完成／失败／部分删除。|

每行还须覆盖并发hostile replacement窗口；参数名、API名称、信息类或可返回标识都不能直接替代全链证明。acl_dacl/separate_principal/sandbox/appcontainer × 上述四操作的**16格全部UNRESOLVED**；window UNACCEPTED。完整Objective A保留principal/token、same-token、特权/admin、DACL/ownership、rename/delete、reparse、cross-volume和路径替换；loader/cache/constructor/callback/transitive dependency、stdout/stderr、行政capture也不豁免。

## 唯一下一来源：结构契约的精确定位提案

本页L946实际literal href为：

```text
/en-us/windows/desktop/api/winbase/ns-winbase-file_id_info
```

锚名称FILE_ID_INFO；source为上述batch4 HTML、历史SHA2843FD68F767D1197F1654CDAE745D7C196381ECF8BC0D76038DA56E04F5E50F。以该页canonical的origin与absolute-path字符串词法拼接，定位URL为：

```text
https://learn.microsoft.com/en-us/windows/desktop/api/winbase/ns-winbase-file_id_info
```

仅观测href和词法定位，没有跟随或GET。精确待证问题：该返回结构的身份字段定义何种身份域及稳定范围，文献是否给出跨句柄、rename、卷变化或重启的保障与限制？本页已覆盖class/structure映射及查询返回；这些字段契约未由该映射建立。不能据本页缺口声称全局缺文献。

TASK45已记载batch5结构页存在；因此最小建议是Work另签精确本地文献白名单复用既有页核对上述问题，**不建议重复获取已有API页或结构页**。本提案不赋予本轮读取batch5的权限。若Work在单独事实核对后仍认为需要GET，任何候选GET都只是未签发文献提案，须独立具体授权；TASK50的HTTP预算0，不发请求、不刷新旧预算或自动授予max1。定位本身不证明身份／稳定性／保护，也不解除SDK或运行门。

## 保留状态与停止门

TASK48仅接受TASK47报告建议，排除错误document_sha256、first_failure=null、最终完成／封存声明；TASK47仍STOP，原件不改。TASK49模型容量失败STOP，四次输入hash已consumed4/rem0，输出hash0、unused2已退休，不检查旧输出或补造完成。TASK46 SDK ObjectNotFound与query1/rem0仍保留，不等于SDK不存在、不再查询。TASK40/41及其他旧失败不抹去。

oldquery2rem0、HTTP3/2/1/2/2/1rem0、protectedbyte7rem0、actualdata/fixture/archiveadmin/V1/V2各1rem0均不重置。C9PAUSED/fullObjectiveA/16UNRESOLVED/windowUNACCEPTED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；原C8科学保留、新条件链0。重大方向／科学／实验决定保留Owner门。

本轮输入hash、代码读取或执行、Git、reports/受保护根、HTTP/SDK/registry/systemquery/model/science/研究runtime/test/import/AST/compile/native/DLL/probe/experiment/consumer/data均0。仅写TASK50本文与回执；两个新输出各hash一次单独封存。STOP等待Work独立验收，不自验收、不另建会话或签发后继。
