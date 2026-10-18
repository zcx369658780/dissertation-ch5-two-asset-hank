# CH5 自动GitHub证据交换 V2 — Owner 2026-10-18明确要求

**强制默认：今后Codex自动向GitHub独立临时review分支发送MD＋证据ZIP，不再把手动上传ChatGPT当常规验收步骤。** 此要求由Owner在当前会话再次明确，优先于此前文件里“可以发ZIP，但一次发布失误即手动上传”的低效执行习惯。旧2026-10-16/18协议中的脱敏、远端专有白名单、先验收归档再清理、Git历史不消失与模型保护仍生效。

## 1. 真正执行的默认交付

每个新冻结版本长任务须在签发时直接指定：
- 唯一独立远端review分支与固定parent commit，只在远端tree写入 _review_tmp/ch5/<task-id>/。
- 默认白名单三件：result.md、manifest.json、evidence_sanitized.zip（当存在待审原始证据，ZIP就是默认交付件，不是例外或口头可选）。
- SHA256、长度、ZIP完整成员表、RAW_EXACT和SANITIZED_DERIVATIVE的身份和哈希；ZIP默认压缩上限32MiB/解压总≤256MiB/≤3000成员。本人上传ZIP是极端兜底，不是任务交接常态。
- 在科学启动前进行一次**不运行HA的发布器端到端本地预检**，用假bare Git远端和小型二进制ZIP验证：精确argv token、git hash-object/mktree/commit、普通推送、远端读取原始ZIP字节及清理树。无网络测试不消耗真实GitHub远端预算。

## 2. 科学运行与交付预算分账

**SCIENCE_BUDGET和DELIVERY_BUDGET独立**。科学PASS、科学FAIL_CLOSED、Owner停止都立即关闭科学HA/HJB/KFE/GE调用额度，但已在任务中预授权的只读封存、脱敏和发布动作，在安全条件成立时仍可用自己的工程预算完成。绝不把“科学STOP”当成“不能再上传已存在的证据ZIP”。

今后任务默认预留有用的工程恢复范围：本地无网络发布器修复≤6次，SSH凭据预检≤2次、git fetch CLI尝试≤3次、普通non-force push CLI尝试≤2次、最多**一次成功发布**。首次参数/路径引用/本地脚本语法E1应按计数在同一交付阶段修复、保留first错误，**不得只因PowerShell argv小错误就再次要求Owner手传ZIP**。真正认证/权限失败、Git父对象身份不符、越白名单、敏感数据未能脱敏、保护根风险是E2/E3，STOP而不强推。旧STOP预算和科学任务权限不能追溯解封；如旧交付预算已关闭、Owner仍要自动传输，则另签零科学的纯交付工程任务。

## 3. 本次失败的确定性工程修复

本轮GitHub SSH预检确已成功认证；发布器把两个原本独立的Git参数拼成一个argv元素，即把 --git-dir=<独立bare路径> 和 -c core.quotePath=false 当成了同一个实参，git fetch因此在**本地**报exit128，未访问GitHub远端。

**必修条件：** 发布器改为 git -C <独立bare目录> rev-parse --is-bare-repository 的本地身份检查，调用子命令时使用明确的每token独立字符串数组/参数展开，不以空格拼接整段命令；对旧错误argv提供确定性负例。检查通过才准真实SSH连接/一次被授权的临时分支发布。不能改git global/system配置、要求PAT或把私人SSH凭据记录到GitHub。

## 4. 真实ZIP字节、公开范围及清理

GitHub仓库是public，临时Git提交也会保留历史。Codex应自动将完整RAW原证留本地，把**逐成员、递归内嵌压缩包核验并脱敏**的派生证据ZIP上传；严格排除真实绝对Windows路径、用户身份、SSH私钥/token/argv/env、非授权真实科研数据与不明二进制，不能原样上传私人RAW ZIP。manifest同时列出原RAW SHA256和派生ZIP SHA256；不能以脱敏件冒充raw已验真。

Astra须从GitHub固定ref/commit/tree核对三件。ZIP二进制必须真的得到字节并核SHA256/manifest，GitHub连接器不能直接读二进制时须使用合法只读GitHub原文件下载路径或用户已连接的浏览/Work能力；不能拿纯URL当已审ZIP。若确实无法获得字节，报告BINARY_NOT_INDEPENDENTLY_READABLE而非假称PASS。

**先**将正式结论永久归档到治理分支并readback，**后**仅对那个独立review分支的当次三件做普通nonforce清理commit并readback。不能修改/删除main、模型树、历史科学失败或清理Git历史。SSH/fetch/push执行在原项目worktree和index之外的独占bare Git库，_review_tmp永不出现在本地受保护源码树或index。

## 5. 新的唯一工程补救

本次价格桥2×2任务科学已STOP，A1/A2/A3完成0/2/2轮，HA12次计费；交付三件其实已制作并在Owner私人ZIP中被独立验证，失败仅是E1发布器argv误拼。本政策支持另签**一次**单独的零科学发布器修复和现成脱敏三文件远端交付任务（见 tasks/CH5_GITHUB_ZIP_PUBLISHER_REPAIR_DELIVERY_RECOVERY_20261018.md）；不准续跑原科学实验、改HA、延长100轮、把已关闭的任务预算重开。

正式V010 ACTIVE_TASK=NONE；黑箱源码、数学合同、Results FALSE、V011 NOT_STARTED不变。
