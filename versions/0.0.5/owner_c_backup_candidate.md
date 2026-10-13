# V0.0.5 Owner C 盘备份区域提议及安全边界

日期：2026-10-13（Asia/Shanghai）

**`OWNER_PROPOSED_C_BACKUP_AREA__TRUSTED_ROOT_NOT_ESTABLISHED__NO_FIXTURE_AUTHORIZATION`**

Owner 说明本机有 C、D 两个盘符，偏好采用路线 A，并明确允许考虑在 C 盘建立一个**备份区域**。这一新决定优先于此前“尚未指定候选位置”的旧状态，但**不是**声明 C 盘属于已经独立认证的专用可弃用卷，也不是对卷身份/ACL/祖先保护、攻击 fixture 或北京真实受保护资产的访问批准。

## 一、保留 Owner 原意

- C：Owner 指定的**备份区域候选位置**。备份区是要保全的非可弃用资产，不得变成实验攻击、删除、rename/reparse/ACL 修改或压力测试对象。
- D：原第五章模型仍在既有 `D:\ProjectTemp\c5k1bturn56`，保护不减。两个盘符究竟位于两个物理盘、两个分区或不同文件系统/卷，**尚未核验**；即便独立分区，C 盘如果容纳 Windows 或个人内容也不能将整块盘当作可弃用攻击卷。
- 路线 A 的旧成功前提：*实际有 Owner/平台可信供应凭据的、专用且可弃用的独立卷/环境*。仅“C/D 两个盘符”以及新建 C 目录**不能自证**独立、可信或全威胁窗口安全。
- 因此当前精确状态为 `C_BACKUP_LOCATION_NOMINATED__A_CANDIDATE_NEEDS_STORAGE_TOPOLOGY_AND_ANCHOR_REVIEW`；不把 Owner 的“可以建立备份区”扩大为“已授权实验、格式化 C 卷或访问真实数据”。

## 二、建议两条互不混用的用途

1. **备份区**：仅用于未来授权的有限备份，禁止自动复制模型的大量 dirty/untracked/ignored 或 LOCAL_ONLY 保护资产，禁止复用为可弃用实验根。备份的具体路径、复制对象、单次写入、目录冲突/重解析检查和容量约束在实施前单独冻结。
2. **人工 fixture 区**：必须是独立于备份区和所有不可弃用祖先攻击对象的**单独可弃用命名空间**。即便以后位于 C 的某个子目录，也需核实可信首次根、祖先不可替换范围和对完整 D2 威胁的覆盖；**不能把 C:\ 或备份区视作允许攻击的可变祖先**。
3. 若 C 只是非可弃用的系统/数据盘，无法作为既有*整卷可弃用*方案 A，则需要另行考虑方案 B 的独立可信实验卷/VM 等资源供应，且不得自行创建 VHD/VM、改磁盘/ACL/全局环境。

## 三、现阶段 Codex 唯一可提交的最小下一步方案

仅依据 Owner 新提供的事实和已有公开权威，准备一个**C 盘备份区及可信根核验最小前置方案**，重点回答：
- C 与 D 的卷/物理磁盘关系需要哪些**指定的非递归、只读操作系统存储拓扑查询**才能判断；该查询需先有独立冻结许可，不能以本文件直接启动；
- 是否能由 Owner 自主提供 Windows“磁盘管理”截图（避免 GUID/SID/路径等隐私外传）或平台可信供应记录；
- C 备份区若只用于保全资料，如何做到独立于后续恶意实验、不会被自建 fixture 攻击或清理；拟议目录名称不得冒称已经实际存在/安全；
- 如果没有专用可弃用独立卷，哪个最小 B 路线需要 Owner 新选择；
- 只报一次集中方案，避免重复生成 V0.0.3/V0.0.4 已有通用合同。

**不因本决定直接对 C/D 执行 stat、Get-Volume/Get-Partition/Get-Disk、ACL/reparse/祖先探测、创建目录/卷、复制数据、运行攻击或提交代码候选。** Owner 的 C 备份区创建意向已确认，真正首次写入范围与必要的限定预检需先由 Astra 按 V1.2 冻结计划并单独签发执行许可。

## 四、固定防升级

V0.0.5 仍 `DRAFT__OWNER_C_BACKUP_NOMINATED__TRUSTED_FIXTURE_ROOT_UNPROVEN__NO_IMPLEMENTATION_AUTHORIZED`；`NEXT_BASELINE_ADOPTION=UNDECIDED`，不切 main/模型旧 HEAD/index/dirty。

V0.0.4 保持 `CLOSED__BLOCKED__G0_FIXTURE_ISOLATION_UNPROVEN__NO_EXPERIMENT__WITH_OBSERVATIONS`，旧实验许可不延续。D1历史北京拟核验对象、D2完整 A16/window 保留；D3-real/D4-real 均未授权，真实 run004 stat/open/read/hash/ACL/probe = 0许可。A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、C9 `PAUSED`、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧数据/科学预算全部不变。V0.0.6 NOT_STARTED。
