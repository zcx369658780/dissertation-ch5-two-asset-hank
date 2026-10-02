# TASK53 文件身份字段与证据边界
状态：字段原文摘录完成，等待 Work 独立审查；不作自验收或保护 PASS。
## 来源与身份限制
- 唯一源文件：`official_file_id_info_batch5_20261001.html`，本报告行号均为其 1-based HTML 行号；仅作文字摘录。
- 标题 L13 `FILE_ID_INFO (winbase.h) - Win32 apps | Microsoft Learn` 与 canonical L19 `https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info` 继承自 TASK52 持久记录及失败回执，TASK53 未重读身份段。
- 历史 SHA256：`495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE`，仅任务书报告的历史身份，输入哈希 0；不是 TASK53 当前字节 pin 或网络获取来源证明。
- TASK52 的工具显示截断 STOP 保留；持久记录恢复不反转 STOP。本任务只完成先前未执行的字段摘录。
## 逐字引句与字段
下列引句保留已摘录文字措辞，省略 HTML 标记及链接标记；不执行或渲染 HTML。
> L804–807: Contains identification information for a file. This structure is returned from the GetFileInformationByHandleEx function when FileIdInfo is passed in the FileInformationClass parameter.

L808–813 语法（按源文件换行）：
```c
typedef struct _FILE_ID_INFO {
  ULONGLONG   VolumeSerialNumber;
  FILE_ID_128 FileId;
} FILE_ID_INFO, *PFILE_ID_INFO;
```
> L815–816, VolumeSerialNumber: The serial number of the volume that contains a file.

> L817–820, FileId: The 128-bit file identifier for the file. The file identifier and the volume serial number uniquely identify a file on a single computer. To determine whether two open handles represent the same file, combine the identifier and the volume serial number for each file and compare them.

| 字段 / 规则 | 原文明确支持 | 证据边界 |
|---|---|---|
| VolumeSerialNumber | 包含文件的卷之序列号；语法类型 ULONGLONG | 本段未说明卷变化或重启后的稳定性 |
| FileId | 128 位文件标识符；语法类型 FILE_ID_128 | 唯一性表述使用两个值的组合，不能仅据 FileId 声称跨卷或跨机器唯一 |
| 身份域 | 文件标识符 + 卷序列号，单台计算机上唯一识别文件 | 不构成跨机器、跨时间或永久不可复用保证 |
| 跨句柄识别 | 对两个打开句柄各取上述组合并比较，判断是否表示同一文件 | 不证明随后 mutation 仍作用于被比较的对象 |
## 源文事实、推论与沉默
源文事实：字段含义、单计算机身份域及两个打开句柄的组合比较规则，均如上引句。
有限推论：该规则可作为两个已打开句柄之对象身份比较的文档依据；完整取得字段、比较及操作实施没有在本任务执行或验证。
限定沉默：精确词检索未出现 Remarks 匹配；L821 进入 Requirements。以下仅指已摘录身份段没有提供保证，不声称所有文档或平台全局缺失。
| 待证义务 | 本摘录的边界 |
|---|---|
| rename / 路径替换 | 未说明名称变化、同路径对象替换期间身份稳定性或路径到对象绑定 |
| delete / recreate | 未说明删除重建后的标识符复用或旧对象与新对象区分期限 |
| 卷变化 / reboot | 未说明跨卷迁移、卷序列号变化或重启后的稳定性 |
| directory / parent-chain | 未证明目录、父链、root、leaf 之间关系或后续操作绑定 |
| principal / privilege / authority | 未给权限、same-token/admin 对手隔离或授权证明 |
| handle ownership / lifetime | 未给取得、借用、转移、关闭及存续约束 |
| completion / failure / partial state | 未定义任何 mutation 的完成、失败及部分状态结果 |
| hostile replacement / check-to-mutation | 身份比较不提供原子绑定、锁定或间隙保护保证 |
## 五接口与四种修改操作
| 接口 | 仍需独立建立的操作契约 |
|---|---|
| anchor_directory（前置） | 锚定目录身份、父链、句柄所有权及存续 |
| claim_root | root 与已检查对象绑定、claim 权限及完成/失败状态 |
| mkdir_each_parent | 逐层父链、创建目标绑定和部分创建状态 |
| create_exclusive_json_npz_leaf | leaf 对象绑定、独占创建及完成/失败/部分状态 |
| unlink_specified_leaf | 指定 leaf 身份约束、删除目标绑定及操作后状态 |
结论：本页实际补足字段含义、身份域与跨句柄比较原文；唯一身份比较不证明 check-to-mutation 保证，也不证明保护成立。四种操作的 16 项边界均保持 UNRESOLVED，fullObjectiveA 及 hostile replacement 威胁保留；目标 SDK/API/native 支持 UNKNOWN，适用性差异不在本任务调和。
## 保留状态与执行边界
TASK52STOP / TASK49STOP（四输入哈希4/rem0、输出2退休）/ TASK47STOP（无效seal及completion排除）/ TASK48仅建议保留，旧原件未改。
SDK1/rem0、oldquery2/rem0、HTTP各批3/2/1/2/2/1且rem0、protectedbyte7/rem0、actualdata/fixture/archiveadmin/V1/V2各1/rem0；无预算重置。
C9PAUSED / windowUNACCEPTED / CALL_LEDGER_UNRESOLVED / priceFalse / releaseUNKNOWN / baseyearNone / modelFalse / ResultsFALSE / originalC8 保留。
输入哈希、HTTP、SDK查询、native、模型/科学/研究运行、测试均为0；不发出后续提案或执行授权。方向、科学、实验决策仍由 Owner 决定。
