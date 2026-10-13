# V0.0.4 Owner D1/D2 正式采纳记录：北京历史元数据对象与完整保护威胁范围

**Owner 决定日期：2026-10-13（Asia/Shanghai）**  
**分类：`OWNER_ADOPTED__D1_D2_ONLY__D3_D4_PENDING__PROTECTION_BLOCKED__NO_READ`**  
**版本：`0.0.4` 版前阶段，**未冻结正式实施计划，未签发独立实施许可。

## 1. 原审议与权威边界

本文件登记 Owner 在 Astra [V0.0.4 版前审议](review.md)后明确确认的两项取舍。此前版前计划 `versions/0.0.4/plan.md` 固定草案 SHA `f5abef37cf7aa5b22c0b918782cc9a28daf60e5a`、blob `cda85bf01687b6e0fce9fffcfc57b5038f6358af`，此前审议文件固定在 GitHub 提交 `30eb35d613d5357ea9685f145a1892fce484f4c4`；其当时“D1–D4 全待决”准确反映**当时状态**。本条只追加新 Owner 决定，**不倒写冻结文档或旧审议**。

**D1 — `OWNER_ADOPTED__PROPOSED_OBJECT_ONLY`：** 将*历史 run004 初始北京*的下述三份元数据正式选定为 V0.0.4 **未来拟核验对象**。限定用途是将来一次经过新许可的*历史成员内容/manifest 一致性*验证。Owner 当前不是在决定它们可读、完整、真实生产可用、北京的 terminal checkpoint 是哪一号，也不是选择完整31省或后续 turns；历史科学接受作为待独立比对的锚，不能替代当前实际 bytes/权限核验。

**D2 — `OWNER_ADOPTED__FULL_A16_WINDOW_THREAT_SCOPE_UNCHANGED`：** 原 Objective A16/window 的完整保护威胁边界继续有效，**无缩减和无豁免**。须将同用户及获 ACL 授权的普通非管理员进程、父目录 `DELETE_CHILD`、祖先路径/目录重命名或替换、junction/reparse/symlink、读句柄从建立至关闭全生命周期及相关 TOCTOU 风险纳入可行性评估。不得把 `resolve → stat → open`、文件哈希一致或 Python-only 普通路径检查视为已完成这种保护证明。客观能否在当前 Windows 执行身份/权限模型下证明，**目前仍 UNKNOWN/PROTECTION_BLOCKED**，不能事先宣称 PASS。

## 2. 已选历史三文件（路径仍为历史源码推导，当前不允许探测）

根目录仅作未来精确定位讨论：
`R=D:\ProjectTemp\c5k1bturn56\reports\ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004`

| 拟核验成员 | 拟议单次上限 | 本次权限 |
|---|---|---|
| `R\sealed_manifest.json` | 1 文件尝试、2MiB | `NO_READ/NO_STAT/NO_PROBE` |
| `R\household\p00_北京\province_terminal_receipt.json` | 1 文件尝试、64KiB | `NO_READ/NO_STAT/NO_PROBE` |
| `R\household\p00_北京\native_initialization_receipt.json` | 1 文件尝试、64KiB | `NO_READ/NO_STAT/NO_PROBE` |

**未来提案数值**：3次尝试、2.125MiB（2,228,224 bytes）、重试0，**并非已冻结额度、也不是本版任何执行许可**。前置祖先/ACL/reparse/句柄等保护查询的对象和额度亦尚未批准，当前均为0。历史 manifest `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6` 及4353成员/61650777字节属原历史证据，不允许扫描全体或借旧 verifier 访问资产。

## 3. 未授予的 D3/D4 和后续步骤

**D3 `OWNER_DECISION_REQUIRED`：** 尚未批准执行 principal/SID/token、Windows 工具/句柄/访问控制实现、对原受保护路径的 `stat/exists/ACL/reparse/open/read/hash/parse`、保护窗口建立、祖先扫描，亦未批准上述三次尝试及其有效期。下一步只允许**对既有公开科学/Windows API 资料进行无真实目标接触的有界静态技术设计**，确认是否存在满足 D2 完整威胁的实现/证明路径；Codex 仅提交方案，不编写执行器、不运行保护试验。安全设计的可行性如无法证明，保持 `PROTECTION_BLOCKED/NO_READ`，不通过换工具/用户、管理员运行、改 ACL 或缩小威胁范围绕过。

**D4 `OWNER_DECISION_REQUIRED`：** 尚未批准原字节生命周期、LOCAL_ONLY 日志的精确保存/销毁期限、访问人、对外脱敏字段。可建议原文件字节仅在受控内存快照处理、原始机器/ACL/文件详情不出本地，但**建议不等于已批准具体处理策略**。

Codex 任何版前技术方案须将 D1/D2 视为已采纳、不得反复请求；只列 D3/D4 的必要技术选择和缺口。若保护无法证明，可以提交严格 `BLOCKED` 结论，不为版本连续性造一个假的可执行读计划。后续是否冻结 V0.0.4、是否发出 `ASTRA_APPROVED_EXECUTION` 或是否尝试微型 protected read 均需额外明确 Owner 决定。

## 4. 状态、代码基线与科学停点

**现行：`OWNER_D1_D2_ADOPTED__D3_D4_PENDING__PROTECTION_BLOCKED__NO_READ__V0.0.4_NOT_FROZEN`**。

V0.0.3 accepted document candidate `cf74384f151427f0b7071ac0461cede6ad6cdf11`、tree `372c693ca3dccea716ae8caef382f513e5a2316e` 仅是未来 V0.0.4 代码/文档候选**建议基线**；`NEXT_BASELINE_ADOPTION=UNDECIDED`，不修改 main、原 worktree/HEAD/index/dirty、不创建或推送实现候选。

V0.0.1–V0.0.3 均保持各自受限 `CLOSED/ACCEPT_WITH_OBSERVATIONS`；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED`、`model_activation=False`、`Results FALSE` 和旧 CLOSED 预算不变。人口/人均方向保持、户均封存，不 `N=P/3`；劳动力经济单位、外部年份/价格/日历以及 policy/Q/p/g 联合真实来源继续 `UNKNOWN`。V0.0.5 `NOT_STARTED`。
