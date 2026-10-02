# Owner 平台信息决策提案

2026-10-01 · TASK29 / Builder dialogue3。
状态：**PROPOSED_ONLY__NOT_ISSUED_NOT_AUTHORIZED**。本文不是执行任务、不是批准请求的实际发送；须先经 Work 独立审查，再由主 Work 向 Owner 提问。

已接受的官方文档摘录只建立局部文本事实。拟适用的目标 Windows 版本、build、architecture、filesystem、SDK/API 版本仍缺失，因而尚不能采用其平台适用性。当前主机不自动等于 Owner 的拟定目标；文档最低支持版本不证明当前环境或整体保护。

## 两个精确 Owner 选项

**选项1：手动提供拟定目标描述。** Owner 给出目标 Windows 版本/build/architecture 与文件系统格式；这些信息记为 `OwnerDeclared`，未作机器核验。SDK/API 版本单独声明、单独记录；未提供项继续 UNKNOWN，不补猜，不扫描 SDK。此选项不含查询或实验授权。

**选项2：另行明确批准两次被动本地元数据查询。** 仅在 Owner 明确批准及 Work 签发精确任务后，新增行政查询预算2，attempts max2、retry0、首失败立即 STOP。此时仅拟查询当前本地 OS 的四字段和 D: 文件系统格式；Owner 仍需说明该主机是否就是拟定目标。本轮预算0，不执行。

未来查询表达式原样列为提案文本，**不是本轮可执行指令或脚本文件**：

```text
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber, OSArchitecture
[IO.DriveInfo]::new('D').DriveFormat
```

第一项限本地，输出仅 Caption/Version/BuildNumber/OSArchitecture 四字段，不指定远程机器或会话；第二项限 D: 的 DriveFormat 字段。不枚举驱动器或路径，不读取文件正文、目录或受保护根；不查询 SDK inventory、credentials、用户名、序列号、网络、globalsettings、权限或其他字段。上述表达式仅存于本文文本，不创建执行文件、不发起调用或子进程。

若未来另获批准，精确新输出仅为本证据目录直接下的：

- `D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\passive_platform_metadata_readback.json`
- `D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\passive_platform_metadata_read_receipt.json`

当前不创建这些文件，也不创建目录。未来 Work 任务须先确认两文件不存在，再绑定字段白名单与输出身份；不得覆盖旧证据。两查询各尝试最多一次，失败也消耗相应预算；第一项失败则不做第二项，不回退、不重试、不替代。错误只保留最小错误码／状态，不能记录完整 CIM dump。未执行的额度不构成其他查询授权。

## 为什么需要新的精确 Owner 例外

既有精确提案 `inert_isolation_implementation_scope.md`，SHA256 `E947AA15BE4DE86C968092589E2A3A7A8F5D6227FD0DADC2C276F7EAC44EE1AE` 明文：

> No invocation/import/AST/compile/test/platform probe budget at implementation stage.

同文还说明 generic continuation 不解除 protected restriction。已完成的未执行准备例外不扩为平台探测；因此未来两项查询需要新的、单独的 Owner 明确批准，随后才由 Work 签发 bounded task。本文与普通“继续”均不是该批准。

## 查询也不能关闭的门

即使选项2另获批准并成功，查询结果也只属于被动元数据，不选择 SDK/API，不采用安全机制，不证明保护，不解决四机制 × 四操作的16项 UNRESOLVED、window UNACCEPTED 或六根具体授权缺口；不授权 native/import/test/isolation/science/model/consumer，也不重置旧预算。SDK/API 仍 UNKNOWN，除非 Owner 分别声明；单独版本查询不能形成 readiness PASS。

完整 Objective A 保留：principal/token、same-token、特权/admin writer、DACL/ownership、rename/delete、reparse、cross-volume，及 loader/cache/constructor/callback/transitive dependency、stdout/stderr、行政 capture 威胁。四操作 root_claim、each_recursive_mkdir_parent、exclusive_json_npz_create、specified_leaf_unlink 和 anchor_directory 前提仍需独立证据；拒绝状态 STOP__UNRESOLVED。

本轮 metadataquery/CIM/DriveInfo/hostversion/runtime/import/AST/compile/test/probe/native/DLL/experiment/model/science/consumer/actualdata/protectedroot 调用全部0，新 HTTP0。batch1=3/rem0、batch2=2/rem0、batch3=1/rem0；旧 actualdata/fixture/archiveadmin/V1/V2 各 consumed1/rem0，不重置。C9PAUSED、A3仅已完成准备例外、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE 保留；历史C8科学保留，当前条件链调用0。

没有实验计划、真实目标路径或受保护根操作方案。完成本文后 STOP，等待 Work 审查；Builder 不向 Owner 提问、不自验收、不签发后继任务。
