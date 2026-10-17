# V010 / V1.3：Codex 一次本地文档镜像同步（DOC_ONLY）

**唯一任务ID：CH5_V13_ONE_TIME_CODEX_LOCAL_DOCUMENT_SYNC**。
**批准：2026-10-17 Owner明确要求升级V1.3、更新GitHub/GPT项目知识与Codex同步一次。**
**性质：DOC_ONLY__ONE_TIME_LOCAL_MIRROR_SYNC。**
**冻结发行：**首次包含本任务文档的GitHub治理commit及此文件Git Blob由随后 CURRENT/TASK_CURRENT 精确登记。Codex从**该固定commit**读取原文和V1.3，不以变化中的HEAD或main代替。
**交付ID：CH5_V13_ONE_TIME_LOCAL_DOC_SYNC_RESULT**。
**STOP：WAIT_ASTRA_CH5_V13_LOCAL_DOC_SYNC_REVIEW / STOP**。

## A. 目标和权威

同步V1.3本地工程快速通道和知识入口，使本地Codex后续读到正确工作流。GitHub仓库 zcx369658780/dissertation-ch5-two-asset-hank 的治理分支 migration/astra-workflow-20261012；新V1.3正文 docs/CH5_ASTRA_WORKFLOW_V1_3_20261017.md；动态导航 docs/CH5_ASTRA_WORKFLOW_CURRENT.md、docs/DOC_INDEX_CURRENT.md、CURRENT.md、TASK_CURRENT.md、docs/knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md；GPT项目离线记忆覆盖层 docs/knowledge/CH5_GPT_PROJECT_SOURCE_OVERLAY_V13_20261017.md。

Codex按固定发行commit读本任务与V1.3全文、当前HEAD只读核状态；V1.3替换**未来任务工作方式**，不会修改已有V010冻结计划/模型、旧失败原件、真实C8或科学许可。优先根据固定哈希记录实际获取的文件字节身份，若来源不可达标UNKNOWN/STOP，不用聊天摘要补造源码。

## B. 唯一允许本地写入与首次写入前顺序

首选若旧Owner已经审核过的独立文档镜像有**准确可信位置和对应记录**，仅在该安全镜像按白名单更新；若无法安全认证，则用唯一新项目外目录 D:\ProjectTemp\ch5_workflow_v13_docs_mirror_20261017_01，不得在现存模型树/治理工作树自动“就近”创建。

无论选哪一种，必须在**第一次写操作之前**使用当前可执行的受信任PowerShell/Windows只读命令检查父目录、目标身份、重解析/UNC/ADS/别名和受保护目录不重叠，不得为了运行preflight先向目标写脚本/日志/manifest；如做不到，在终端报告匿名STOP，不在未认证位置写失败回执。preflight完成才可新建目标，随后再次只读确认目录身份，才写第一份文件。先写后验属于硬STOP，不能补造事前PASS。

仅同步以下文档字节及明示导航，最多7个只读GitHub正文来源文件（本任务、V1.3、workflow-current、index、CURRENT、TASK_CURRENT、knowledge overlay；长期知识正文可只同步路径与校验锚，不必复制全历史）： 
- CH5_ASTRA_WORKFLOW_V1_3_20261017.md
- CH5_ASTRA_WORKFLOW_CURRENT.md
- DOC_INDEX_CURRENT.md
- CURRENT.md
- TASK_CURRENT.md
- CH5_GPT_PROJECT_SOURCE_OVERLAY_V13_20261017.md
- 本任务自身的固定副本/引用信息

允许在**镜像内**增加一个仅含上述固定文档路径/来源身份的AGENTS.md导航段；禁止修改原D:\ProjectTemp\c5k1bturn56旧模型root/八dirty/staged/index/external common-dir或其原AGENTS.md，不触原C盘独立SSD备份、历史runner/数据或其它项目。不要向GitHub另行push，也不要把GPT项目Sources上传操作伪称Codex已经完成；那一步须Owner在ChatGPT项目界面手动上传本次更新包。

## C. 本任务小预算

工程文档同步墙钟≤45分钟；只读GitHub固定正文≤8份，总计≤300KiB；新镜像新增/修改文档≤8份，总计≤400KiB；最多2次小型PowerShell静态验证批次，时间/文件/读写/首次preflight PASS事件按真实情况记账。所有旧预算继续STOP不结转。

**模型Python/科学HJB/KFE/HA/GE/IRF/真实C8调用0；旧runner、VerifiedLoader、git checkout/fetch/commit/push/模型源码修改0。**如需要远端读取允许已连接GitHub只读访问或严格受信任网络读取，不引入PAT/新SSH凭据、不改全局Git配置。任务只改授权独立文档镜像，不修改本项目GitHub文档（已由Astra发布）。

## D. 一次集中交付

输出严格脱敏≤2KiB的`CH5_V13_ONE_TIME_LOCAL_DOC_SYNC_RESULT`：V1.3政策Git Blob、固定issuer Commit及task Blob；实际本地镜像的安全身份与来源锚点、同步了哪些文件与SHA256、首次preflight前没有写入的证据、文件数/时间/批次、保护资产未写的可证范围、未知和失败。不能以“复制成功”冒充ChatGPT个人Memory或项目Sources已自动更新。结束`WAIT_ASTRA_CH5_V13_LOCAL_DOC_SYNC_REVIEW / STOP`，不可自动签发下一工程证据交换或科学任务。