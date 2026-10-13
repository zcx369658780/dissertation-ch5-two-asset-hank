# V0.0.2 · Astra 独立实施授权

日期：2026-10-13（Asia/Shanghai）

## 裁决与固定权威

**`ASTRA_APPROVED_EXECUTION__CH5_V0.0.2__SYNTHETIC_SOURCE_CONTRACT_ONLY`**

根据 Owner 已批准的 V1.1 分工与 V0.0.2 版前协商，Astra 已集中审核 Codex `V0.0.2_EXECUTION_PROPOSAL_DRAFT`、当前 GitHub 源码与科学保护边界。准许 Codex 在**以下固定冻结计划**范围内自主实施、正常合成 focused 测试与普通工程修复，并一次集中交付候选。未经授权的真实科学、来源认证及数据权限依旧封闭。

- **唯一冻结计划 commit：** `4b11c46823e7cdabc12de8b8036cc5efc2380c52`。
- **冻结计划 path/blob：** `versions/0.0.2/plan.md` / `43171bc6b841695845e7576d7feaa3135b88c588`。
- **获批 V0.0.2 源码基线：** `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`。
- **代码基线采纳：** `NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`；不代表 main merge 或本地原工作树 HEAD 改变。
- **候选分支名：** `codex/ch5-v0.0.2-household-source-contract`，须从上述固定源点独立构造，不覆盖已有分支。
- 此授权文件不修改、补充或追改正式冻结验收标准；冻结后原计划只读。

## 已获批的五个 Git 交付路径

只允许从源代码基线**新增**：
1. `src/ch5_two_asset_hank/multi_province/household_source_contract.py`
2. `tests/test_v002_household_source_contract.py`
3. `versions/0.0.2/source_crosswalk.md`
4. `versions/0.0.2/execution.md`
5. `versions/0.0.2/acceptance_summary.json`

仅允许另在本版本有界 `LOCAL_ONLY` 临时根生成 Git 操作性 index/object、完整精确候选树的 `candidate_view`、合成 fixture、私有回执与必要 supervisor 工具。不得因 Git admin 存储路径变化破坏原索引/其他项目远端引用。不得改动本版禁改路径、旧模型源码/数值算法/科学合同/已接受 V0.0.1 源文件、默认生产路由或用户既存 dirty/untracked/ignored。

## 实施与测试许可（仅合成）

- 实施墙钟最多 `3h`、focused pytest 子进程累计最多 `12` 个且各不超过 `120s`、目标单进程 RSS `1GiB`；失败亦计入。
- 新建存储总额最多 `168.25MiB`，其中 Git 操作性数据 `128MiB`、准确候选视图/合成 fixture `32MiB`、私有原回执 `8MiB`、公开脱敏三报告合计 `256KiB`；每类无重复计数，不自行把其它新内容排除。实施前先检查临时 index 和导出闭包的预估大小。
- 真实 HJB/KFE、旧 C8/C9/C10、真实31省消费者/受保护源数组与 NPZ/JSON、旧科学/保护许可、GE/IRF/Results/生产部署和新全局配置变更**全部 0 次**。
- 仅允许明确 `SYNTHETIC/NOT_REAL_SOURCE` 在新 typed boundary 的检查后，经**原有真实** corrected aggregate/frozen/V0.0.1 batch 处理。真实/历史/不明来源无论是否带 SHA、布尔认证、模拟 seal 都不得获得计算准入。
- 普通范围内可自主修复测试、记录失败后重新 focused 测试，不用逐次询问 Astra。但科学/数据/隐私/权限/禁改原文件冲突或预算硬门触发时，应保存现场停止，向 Owner/Astra 报告，不绕过冻结条件。
- 验证精确 candidate Git tree 的导出模块来源，必要时使用 child-scoped 环境而非自动依赖 `python -I` 与 `PYTHONPATH` 同时生效。不得从原 dirty model tree 偷导入来声称 candidate 通过。
- 合成 seal 和 digest 只支持内存一致性检查；无法证明真实 producer。未来真实 source 所需的联合身份认证和读取审批继续 `BLOCKED/UNKNOWN`。

## Git 与终态

Codex 可在不改原 checkout HEAD/index/branch 的前提下，以单父代码基线、独立临时 index 构造仅五个新增路径的候选，执行精确候选视图 focused 验证，生成脱敏 source crosswalk、execution、acceptance_summary。准许**一次正常 non-force push** 到所列候选分支并对远端 commit/tree 回读；目标分支已存在或出现非快进冲突须停。不合并 `main` 或文档分支、不清理其它成果、不上传私有原回执/真实数据/凭据。

Codex 交付 code/tree、实际命令与结果、资源/异常/保护账、原始回执哈希和可独立检查的脱敏摘要后，停在 `WAIT_ASTRA_FINAL_ACCEPTANCE`。Astra 按固定冻结计划做**最终独立验收和偏差复盘**，不持续监督或自动发起 V0.0.3。

**状态：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。**
