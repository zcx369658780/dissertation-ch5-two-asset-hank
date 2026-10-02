# 创建/信息查询候选就绪判断 v2
2026-10-01 / TASK34 / ADVISORY_ONLY。原TASK33未完成；不得将本修正当原任务完成。

|接口/既有键|新增局部事实|仍缺|
|---|---|---|
|anchor_directory/锚定前提|CreateFile可打开目录；目录handle需要BACKUP_SEMANTICS，特权与无特权条件有别|父链稳定、每层对象身份、hold/transfer/lifetime、全攻击者适用性|
|claim_root/root_claim|CREATE_NEW只限新文件；CreateFile不能创建目录|根认领及具体根授权、并发/原子性、失败部分状态|
|mkdir_each_parent/each_recursive_mkdir_parent|文档指向CreateDirectory/CreateDirectoryEx，未读取|逐层创建/父链绑定、P0…Pn窗口、部分创建责任|
|create_exclusive_json_npz_leaf/exclusive_json_npz_create|CREATE_NEW既存冲突和writable-location前提；shareaccess有限约束|指定叶绑定、全父链排他、JSON/NPZ内容/持久性/失败清理|
|unlink_specified_leaf/specified_leaf_unlink|deleteaccess含rename；delete-on-close等所有handle关闭；reparse时link/target语义有条件|父/叶对应、最终检查至变更窗口、普通删除完成/部分状态|

GetFileInformationByHandleEx列FileIdInfo/FILE_ID_INFO并不建立稳定身份；infoquery不是原有第五变更操作。两条候选都尚不足以推荐任何可运行保护机制或非拒绝实现；推荐保留拒绝骨架，仅继续精确文献证明缺口。没有采用API、安装SDK或调用方式设计。SDK/API版本仍UNKNOWN；build/NTFS元数据不能替代契约和保护证明。
下一窄必要文献最多2项，均literalhref/未获取：
1 I源official_getfileinformationbyhandleex_batch4_20261001.html L946，SHA2843FD68F767D1197F1654CDAE745D7C196381ECF8BC0D76038DA56E04F5E50F，href /en-us/windows/desktop/api/winbase/ns-winbase-file_id_info；词法绝对locator https://learn.microsoft.com/en-us/windows/desktop/api/winbase/ns-winbase-file_id_info。用于核字段及identity适用范围/限制，未保证填补稳定身份。
2 C源official_createfilea_batch4_20261001.html L1636，SHAF7AB6ADE08B0B40CECA1F61D15764CA28A5734E2FD11DA5FFC634AD7C3FC9880，href /en-us/windows/desktop/api/fileapi/nf-fileapi-createdirectorya；词法绝对locator https://learn.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-createdirectorya。用于核创建单级目录条件/失败责任，不能预设原子全父链或递归保证。
二者状态DERIVED_LOCATOR_NOT_FETCHED，仅文献定位；词法绝对化依据各源captured Learn.microsoft.com URI，不是返回URL或已取内容。未跟链接。不建议重复取得已读资料回填旧来源缺口。
全部ObjectiveA主体/token/same-token/admin/DACL/ownership/rename/delete/reparse/cross-volume，以及loader/cache/constructor/callback/transitive/stdout/stderr/capture威胁保留。16UNRESOLVED/windowUNACCEPTED/六根具体授权缺失/C9PAUSED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE不变。历史C8科学保留，当前条件链0。
query2/rem0；HTTP批3/2/1/2各rem0；旧actualdata/fixture/archiveadmin/V1/V2各1/rem0；无重置。本轮所有查询/HTTP/研究运行/native/import/AST/compile/test/实验/模型/科学/consumer/真实数据/保护根0。