# 拟定平台文献 locator 附录

2026-10-01 · TASK32。仅3个优先候选；从本轮获准 HTML 的 literal href 提取，未跟随链接或联网。relative href 仅依源 known requestedURL 的 origin 作词法绝对化；全部状态 **DERIVED_LOCATOR_NOT_FETCHED**，绝对化结果不是返回 URL 或已核实目标页。

| 优先级／具体缺口 | 源文件与原 HTML 1-based 行号 | 原始 href | 词法绝对 locator |
|---|---|---|---|
| 1 · 创建入口及对象创建函数的句柄／pending-operation 条件 | official_closehandle_20261001.html L903 | /en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea | https://learn.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea |
| 2 · 文件信息查询语义；是否具有身份相关字段／保证尚未知 | official_setfileinformationbyhandle_20261001.html L827 | /en-us/windows/desktop/api/winbase/nf-winbase-getfileinformationbyhandleex | https://learn.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-getfileinformationbyhandleex |
| 3 · disposition 信息类对应结构的使用条件／限制 | official_setfileinformationbyhandle_20261001.html L892 | /en-us/windows/desktop/api/winbase/ns-winbase-file_disposition_info | https://learn.microsoft.com/en-us/windows/desktop/api/winbase/ns-winbase-file_disposition_info |

来源 pins：CloseHandle SHA256 B12348AC1EC853B469CE5626A4EFF89825A3E3723C71071105DFE1F3F817F8BF；SetFileInformationByHandle SHA256 C4F3F396563F5D4ECDA8BB7611402BC6D32F6515250CAD1A6119F4313FED4885。known requestedURL 分别为 https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle 与 https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle 。NtCreateFile 源亦仅限本轮许可文本检查，未扩大来源。

第3项结构已有 batch1 的有限摘录；这里仅记录本轮源页里的精确引用位置，不批准重新获取，不修复其旧 returnedURL 缺口。第2项是查询入口定位，不证明已经定位到稳定身份契约；具体 identity 保证仍 NOT_ESTABLISHED。上述候选的内容／适用范围未由本轮抓取核验，不能承诺其会补齐缺口或证明 Objective A。

无新HTTP、系统查询、代码／示例执行或实际根操作。无运行计划、目标路径或保护操作方案；没有 SDK/API 选择、NTFS 保证或全父链推导。全部16项/window/六根授权缺口、消耗预算与保护边界保留。下一步仅待 Work 文档审查；本附录不授权获取、重试或后继任务。
