# V0.0.5 B2 Astra 验收：Windows Python 文件身份检查误报安全停点

日期：2026-10-14（Asia/Shanghai）

**终态：CLOSED__BLOCKED_PRE_COPY__IMPLEMENTATION_IDENTITY_API_MISMATCH__SAFE_STOP**

权威：B2 冻结 commit bd3cfd39c091abb7276d611dfaa0e2064864ecaf，plan blob 1887e8f52587d8c47ffaa1f6152076a4a570b098，文件 b2_link_descriptor_backup_plan.md。冻结标准、单次失败即停和零自动重试不追改，B2旧权限视为已消费。

**技术判断。** Codex 报告在首次打开普通源文件之前，将 Windows Python3.11 的 os.DirEntry.stat() 所得 st_ino/st_dev/st_nlink 零值与后续 os.stat() 结果直接比较，造成 SOURCE_CHANGED_BEFORE_OPEN。Python 3.11 官方明确 Windows 下 DirEntry.stat 的三个字段始终为零，应改用 os.stat 取得它们：https://docs.python.org/3.11/library/os.html#os.DirEntry.stat 。因此是实现语义错误的有力证据，**不是源文件真的发生改变的有效证据**。Astra尚未独立查阅本地执行器源码，不能声称所有其它身份保护条件正确；从 DirEntry.stat 得到的硬链接零值不是可采纳的无硬链接证据，仍 UNKNOWN。

**B2实况（全由 Codex 本地报告，非 Astra Windows 独立复测）：**
- 模型工作树76,625普通文件、5,877目录、1,150,549,423B；Git common-dir14,141普通文件、448目录、654,409,363B。总90,766普通文件、6,325目录、1,804,958,786 B；同B0汇总一致，不证明全树同一时间点。
- 唯一目录 reparse 描述在内存已取得，未跟随外部目标，描述未落盘。
- 单进程约3.297秒、exit1、零重试、工作集峰值95,105,024B；普通源正文实际打开和读取0，读取额度在失败前预扣1。没有C快照、复制文件/字节、源目标哈希、隔离Git恢复、C卷实时准入或目标冲突检查。
- 文件系统写入、Git refs/index/HEAD写入、攻击和科学计算报告均为0；本轮未额外散列原工作树，不能独立证明源未变化。

**裁决。** 接受 B2 遵守冻结停点，备份验收 NOT_ACHIEVED，旧版本目录清理不得启动。Owner倾向优先完成 V0.0.5，允许下达有界纠错长任务；新 B3 独立冻结并配置新一次保全额度，不改B2、不重跑B2、不把B2预扣额度称为未消费。

完整 A16/window、可信可弃用敌对根G0、真实科学D3-real/D4-real、C9、Results仍维持旧状态；V0.0.6 NOT_STARTED。