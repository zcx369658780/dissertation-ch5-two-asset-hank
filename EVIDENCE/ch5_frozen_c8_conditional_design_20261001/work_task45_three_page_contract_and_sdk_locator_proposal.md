# 三页文献契约与一次被动 SDK 登记定位提案
2026-10-01 · TASK45 · Work 文档候选，等待两名独立只读助手复核。提案尚未授权或执行。

现有 batch4 API 正文已重新核对 SHA256 2843FD68F767D1197F1654CDAE745D7C196381ECF8BC0D76038DA56E04F5E50F。它就是 TASK43 拟获取的同一 requestURI；捕获返回URI为 /windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex。TASK43 文献GET提案不再推进，无新增HTTP；批次原获取次数和预算保持原样。

## 本轮文献事实
行号为现有 HTML 1-based，仅惰性文本。
- API页 L944–946：FileIdInfo (0x12) 对应 FILE_ID_INFO。该表是文档参数/结构映射，不是本机ABI或SDK证明。
- API页 L1024–1025：Minimum supported client / Windows Vista [desktop apps | UWP apps]。
- API页 L1028–1029：Minimum supported server / Windows Server 2008 [desktop apps | UWP apps]。
- API页 L1036–1037：Header / winbase.h (include Windows.h)。
- API页 L1040–1041：Library / Kernel32.lib; FileExtd.lib on Windows Server 2003 and Windows XP。
- API页 L1044–1045：DLL / Kernel32.dll。

另两已核页面的窄原文保留：结构页 S（SHA495740A144FFB540A4B8008A56CB6BCAA9DE70682F68A85FE2CA6716B3D550BE）L831–832写 Minimum supported client / None supported；信息类页 E（SHACD329BDC284956E2BDDDF22288A7046C212A6B21BED6F99DFAD6B066EAD9D6AE）L899写 FileIdInfo 在 Windows8/Server2012之前不支持。API整体最低版本、成员版本限制与结构页支持栏是不同层级。现有API页增加了文档映射证据，但不静默调和客户端差异，不证明指定build26200可用性。差异仍UNRESOLVED_DOCUMENTARY_APPLICABILITY_DISCREPANCY；SDK/API机器证据UNKNOWN，目录身份和保护NOT_ESTABLISHED。

## 供 Owner 决策的具体窄提案
拟允许主 Work 新增一次**被动 SDK 登记定位值读取**，仅询问下列注册表键的 KitsRoot10 值：

```text
Get-ItemPropertyValue -LiteralPath 'Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Kits\Installed Roots' -Name KitsRoot10
```

此键字符串是拟议行政定位符，未在本轮独立建立其存在性或官方契约；查询可能直接失败。若 Owner 批准，Work另签精确任务，新独立行政预算max1attempt/retry0。仅主Work调用，不先检查键、枚举注册表、查看其他值、环境/架构、尝试其他registryview/备用路径。键缺失/命令失败或非预期类型立即STOP，失败计耗；不重试、不替代，未用额度退休。所有旧被动查询consumed2/rem0不复活。

上述限制是请求字段及输出的范围，不证明 registry provider 内部全部读取行为。实际底层访问总量未验证；一次获准命令 attempt 不等同于已经证明只发生一次底层注册表读取。本提案不增设 provider 行为探测权限。

只读该登记字符串，**不跟随返回路径**，不检查或读取SDK目录、header、安装版本、库、DLL，不调用API/native/编译/测试/探测或研究运行。它只可能填补“SDK登记定位值是否有明确本机来源”这一窄行政事实；值存在不证明真实安装、文件可读性、ABI、版本支持、客户端差异调和或保护成立。默认注册表视图的事实仅限执行进程所见，不宣称其他视图一致。

未来仅新增一个回执：D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\official_sdk_registered_root_locator_readback_20261001.json。尚未检查/创建它。批准后的任务须先确认此输出不存在，失败仅保存最小类别/状态；成功保存精确返回字符串、值类型、attempt1、实际退出状态与事实限制，不输出完整注册表或错误dump。输出行政证据不读取外部SDK文件，不扩展项目边界。

这是新的精确Owner决定，不能由“继续”、旧平台指定、七文件哈希批准、未执行代码准备批准或文档验收代替。执行之前仍NOT_AUTHORIZED；主Work与助手本轮均无注册表/SDK/OS查询。

## 保留状态
TASK40两行政失败、TASK41OS267均保留；两个任务不整体ACCEPT，原缺失回执不补造。TASK42只接受证明义务/权限边界并排除虚假完成声明。C9PAUSED/fullObjectiveA/16UNRESOLVED/windowUNACCEPTED/CALL_LEDGER_UNRESOLVED/priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；历史C8科学保留、新条件科学0。query2rem0、HTTP3/2/1/2/2/1rem0、protectedbyte7rem0及actualdata/fixture/archiveadmin/V1/V2各1rem0不变。没有新HTTP、平台查询、受保护字节读取、native、运行、测试、模型或科学调用；不选择保护机制。
