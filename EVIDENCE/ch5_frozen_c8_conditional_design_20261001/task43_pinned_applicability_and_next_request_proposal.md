# 已 pin 适用性条款与下一文献请求提案

2026-10-01 · TASK43 / Builder dialogue10 · DOCUMENTARY_CANDIDATE_ONLY，等待 Work 独立验收。

## 窄官方文本

仅读取两个已 pin HTML 的文本，不渲染、执行或跟引用。引文为原 HTML 1-based 行号，去标签、解码实体、折叠空白。

|来源|SHA256|canonical（各 L19）|
|---|---|---|
|S：official_file_id_info_batch5_20261001.html|495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE|https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info|
|E：official_file_info_by_handle_class_batch6_20261001.html|CD329BDC284956E2BDDDF22288A7046C212A6B21BED6F99DFAD6B066EAD9D6AE|https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ne-minwinbase-file_info_by_handle_class|

两页 ms.date 均为2018-12-05T00:00:00Z（各 L73）。canonical 是页面元数据，不等于请求 URI 或捕获返回 URI。本轮两个获取回执未在白名单中，因此其 requested/capturedURI 直接核验为 NOT_ESTABLISHED_IN_THIS_READSET。既有对照文档对 E 获取信息的记述只能作为该文档的来源声明，不能说本轮独立核验了回执。

**S01 · S L831–832**
> Minimum supported client
> None supported

**S02 · S L835–836、L839–840**
> Minimum supported server
> Windows Server 2012 [desktop apps only]
> Header
> winbase.h (include Windows.h)

**E01 · E L899 · FileIdInfo 完整单元格文本**
> FileIdInfo
> File information should be retrieved. Use for any handles. Use only when calling GetFileInformationByHandleEx. See FILE_ID_INFO.
> Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP: This value is not supported before Windows 8 and Windows Server 2012

**E02 · E L934–935、L938–939、L942–943**
> Minimum supported client
> Windows Vista [desktop apps | UWP apps]
> Minimum supported server
> Windows Server 2008 [desktop apps | UWP apps]
> Header
> minwinbase.h (include Windows.h)

结构页 client None supported、枚举整体 minimum、FileIdInfo 成员独立版本限制分别保留，**applicability discrepancy UNRESOLVED / SDK_API UNKNOWN**。不将“此前不支持”改写为 Windows11 上已支持，不自行修正文献、推断 installedSDK/API/ABI 或稳定身份、parent-chain、原子性、保护。Header 和 ms.date 只是文档元数据。

## 一项具体未授权 Owner 文献 GET 提案

状态：**UNAUTHORIZED_OWNER_PROPOSAL__NOT_ISSUED_NOT_AUTHORIZED**。仅供 Work 独立审查，Builder 不向 Owner 发问。

观测 literal href：S L805，source SHA495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE：

```text
/en-us/windows/desktop/api/winbase/nf-winbase-getfileinformationbyhandleex
```

锚名称：GetFileInformationByHandleEx。E L899 亦含同一 href。以上是捕获文本中的引用；未跟随链接。仅通过 S canonical 的 origin `https://learn.microsoft.com` 与该 absolute-path 字符串拼接得到 proposed requestURI：

```text
https://learn.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-getfileinformationbyhandleex
```

分类 **DERIVED_REQUEST_LOCATOR_NOT_FETCHED_IN_TASK43**；观测 href、词法提出的请求 URI、未来实际 responseURI必须分开，不能预先称其为 canonical response 或已取得正文。

拟议的唯一事实问题：该 API 文档的 supported client 与 FileIdInfo/FILE_ID_INFO 调用契约究竟怎样表述。后续若 Owner 明确批准且 Work 签发 exact task，才新增独立文献 GET 预算1、最多一次请求、retry0、无其他请求或正文引用跟随；不是旧预算恢复。命令／状态／来源定位任一失败首失败 STOP，无 fallback／重试，失败尝试消耗预算、未用额度退休。

请求仅上述精确官方 URI；提案不允许 redirect-follow（maximum redirection0），若出现 redirect 则记录最小状态并 STOP，不补请求新 location。不承诺指定 URI 会返回200或规范路径，不猜 responseURI。若另行审查需要不同响应处理，须由精确任务另列，本文不授予。

未来只可在既有证据目录直接新增：

- D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\official_getfileinformationbyhandleex_batch7_20261001.html
- D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\official_getfileinformationbyhandleex_batch7_receipt_20261001.json

本轮不创建、检查这两个未来文件。未来获取需分别记录 requestURI/实际 captured responseURI或NOT_CAPTURED、status/media/acquisition time/body SHA、attempts/最小错误；失败不造正文或完整错误 dump。正文只保存惰性文本，不渲染／执行。获取文本可能为客户端契约问题提供来源，不能自行证明 runtime/ABI/SDK安装、实际平台支持、directory identity、并发保护或可行 containment；未解决差异需独立审查，不由 HTTP成功关闭。

## 当前权限与保留限制

没有 machine inventory/probe/API调用/实现/实验/runtime/model额度，也不选择机制。既有 TASK42 review SHA6A690119A1C648DE4E6C2A62FDFED216F6FCC09D52666C03E0FE648E5EAA6CF1仅接受 TASK40 证明义务与权限边界的文档建议，明确排除“本文与回执已新增”的虚假完成声明；TASK40/41不整体ACCEPT。TASK40提前读缺回执exit1、助手错误TASK_CURRENT locator numericexitNOT_CAPTURED、TASK41错误cwd OS267均保留，不重试或补造原输出。

本轮 reports/受保护根/其他仓库/actualdata/model/science/研究runtime/import/AST/compile/test/native/DLL/probe/experiment/consumer/systemquery/HTTP0。query2rem0、HTTP3/2/1/2/2/1rem0、protectedbyte7rem0、actualdata/fixture/archiveadmin/V1/V2各1rem0均不重置。C9PAUSED/fullObjectiveA/16UNRESOLVED/windowUNACCEPTED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；历史C8科学保留，新条件链0。

交付仅本文与TASK43回执；STOP Work 独立审查，不自验收、不签发后继或实施本 GET 提案。

