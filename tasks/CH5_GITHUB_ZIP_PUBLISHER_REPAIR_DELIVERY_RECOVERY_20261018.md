# CH5 GitHub自动ZIP发布器修复与本轮旧证据远端补交：单张零科学工程长任务

**TASK_ID：CH5_GITHUB_ZIP_PUBLISHER_REPAIR_DELIVERY_RECOVERY_20261018**
**发起：Owner 2026-10-18再次强调禁止常态人工ZIP上传，已明确授权改验收交付工作流。**
**性质：ENGINEERING_DELIVERY_ONLY，既往科学 FAIL_CLOSED/旧预算不变；任务发行commit/blob由签发后的治理索引冻结。**
**最后STOP：WAIT_ASTRA_GITHUB_ZIP_PUBLISHER_RECOVERY_REVIEW / STOP。**

## 一、唯一输入与只读原件

原失败科学任务是TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_ROUND_LONG_TASK，发行commit 2c855f616efbca05c29d4069a44e3c6651070b44，科学结论为E2_SHARED_LEDGER_IO_FAIL_CLOSED，A1/A2/A3只有0/2/2轮、HA12次（9完成、1失败、2中断），无科学重试许可。

从Owner本机已经封存的已知原TEMP scratch D:\ProjectTemp\ch5_temp_pricebridge_2x2_100_20261018_01 仅只读指定 PRIVATE_FINAL.zip 和三个已经制作的 delivery 证据文件。不遍历未知旧目录、不修改原文件、不重新封存历史raw。固定PRIVATE_FINAL.zip：1,214,713B、SHA256 F3E8984FE4D2EF4BE65692C27FA7594D96B870D372A8C45D029899F7891841D8。唯一要自动上传的三份原字节为：
- delivery/result.md：4,542B，SHA256 70B047D4FD3C14182BFE00EA183C55F1917343CC777562108345C470E387500B；
- delivery/manifest.json：13,864B，SHA256 24A193F6557FE2EC7FF12872D5097274E6EF0E609D47E5B3B3D05ED38AEC0E9B；
- delivery/evidence_sanitized.zip：196,296B，SHA256 9F3F2CDA8360577DE83BFE02D01B6F57814BEE4E03B1C883F3A6A79698DC08E2，内29件。只发布这三份已脱敏文件；绝不发布含本机敏感路径的私人RAW原证ZIP。

若原精确来源读取或hash不符，必须E2 STOP；不能凭同名重造数据。发布前仍应对三文件、ZIP成员及内嵌压缩包作安全扫描，public Git历史不可删除。

## 二、只改新publisher，先跑无网络本地Git闭环

在项目外新独立scratch D:\ProjectTemp\ch5_reviewzip_delivery_repair_20261018_01 按V1.3 BOOTSTRAP0/1/2认证路径和保护根。禁止写原D盘8dirty/index/common-dir、旧TEMP scratch、C盘备份及任何原HA/科研代码。

只读分析旧 Publish-Review.ps1 和 PUBLICATION_COMMAND_003.json：此前Git argv[0]被错误拼为一个参数，其中同时包含bare路径与 -c core.quotePath=false；SSH预检真实已认证成功，fetch并没有真正访问远端。本任务仅可在新scratch创建修正版publisher及工程测试。优先使用 git -C <新的独立bare仓目录> -c core.quotePath=false <命令>，精确单token argv数组形式，预先无网络 rev-parse --is-bare-repository。以本地fake bare远端＋小型二进制ZIP真实跑一次 hash-object→tree→commit→非强制push→原字节回读→清理树，原错误argv须通过负例拦截。此阶段没有GitHub网络/模型科学求解。

## 三、仅发布远端独立临时树

**唯一新review分支：** review/ch5-temp-pricebridge-factorial100-deliveryrecovery-20261018（须先读回不存在）。
**唯一远端路径：** _review_tmp/ch5/temp-v010-pricebridge-2x2-100-delivery-20261018/。
**仅三件白名单：** result.md、manifest.json、evidence_sanitized.zip；其原字节就是Section1三个文件。review Commit唯一parent为本**工程任务正式发行Commit**，changed paths仅此三件。不checkout、stash、clean、reset、merge原项目工作树，不在任何本地worktree/index创建_review_tmp。
通过Owner已有SSH Key、ssh.github.com:443，新的独立无共享对象bare仓准备全量父树/blob身份；不要求PAT、新秘钥或改global/system配置；普通non-force推送。发布前校验准确父、Commit、3 Blob、ZIP SHA256和成员manifest；成功后remote ref、tree和blob readback并汇报。

**冻结工程预算：**墙钟≤3小时，非科学子进程≤24，本地无网络修补/完整预检≤6组，SSH预检≤2次，git fetch CLI≤3次，non-force push CLI≤2次，最多一次真正成功发布。失败/异常计数不可重置，普通参数打包E1在余额内修复并保留首错；凭据/源身份/风险/E2/E3则STOP，不强推。工程成果/新scratch artifacts≤64MiB，bare Git≤512MiB。**HA/HJB/KFE/policy selector/outer/GE/IRF科学调用严格0**，原计费12不变，旧科学预算全部CLOSED。

## 四、交付与清理

成功只返回 GITHUB_TEMP_MD_AND_BINARY_ZIP_DELIVERY_VERIFIED、精确remote review HEAD/tree、3件Git blob及独立SHA256、可点开的result和ZIP路径；顾问先永久验收、然后由Astra独立清理远端review当前tree的这三件。Codex不得提前删除；旧Git历史并不消失。失败返回完整SOURCE/NET/IO/E1/E2真实分类、当前预算和STOP，不能把本地错误默默转为需要Owner再次手动上传ZIP。

**正式主线:** ACTIVE_TASK=NONE；model_activation=False、Results FALSE、V011 NOT_STARTED，HA原黑箱及TEMP价格桥科学合同不改。
