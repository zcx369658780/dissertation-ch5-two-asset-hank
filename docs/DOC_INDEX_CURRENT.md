# CH5动态总目录 · V1.9完整证据验收与清理状态

## 当前状态
- [CURRENT.md](../CURRENT.md)：V1.9完整证据已验收归档，远端临时清理进行中。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：无活动执行/科学任务；清理仅处理本次白名单三件。
- [V1.9完整证据独立验收与清理回执](CH5_PATH_CLASSIFIER_V19_FULL_EVIDENCE_INDEPENDENT_REVIEW_20261019.md)。

## 已验收
远端交付 commit `41922a7370f8388ef1a5d0063327da65f3066e52`，唯一 parent `69652a0791e813ffaa0dd629feafcf9b5bd4db79`。Astra独立复算 result.md、manifest.json和ZIP原字节的长度/SHA256；ZIP为44成员、总解压383547字节，所有成员CRC/大小通过，无重复、大小写冲突、不安全路径、链接或嵌套归档。单成员SHA256未全部独立复算，限制已在验收回执披露。源码/测试/fixture/逐样本结果已静态审阅，未重跑分类器。

旧491成员ZIP完整安全性仍UNKNOWN；正式V010不变；model_activation=False；REAL_GE=False；Results FALSE；V011 NOT_STARTED；FULL_RUNNER_IO_CLOSURE BLOCKED。

## 清理
Astra须在永久归档并回读后，仅删除 `_review_tmp/ch5/classifier-v19-evidence-20261019/` 下三份白名单文件，并回读确认缺失。清理完成前不得标记CLOSED。

---

# CH5动态总目录 · 2026-10-19现成证据补交

本页只保留一个当前状态；旧完整索引在固定commit 326935e286d00be70306dfeee66b598e73f93725的同一路径保留，不从历史ACTIVE/NEXT推导权限。

## 当前授权

- [CURRENT.md](../CURRENT.md)：唯一ACTIVE为V1.9现成证据DELIVERY_ONLY任务，尚未执行。
- [TASK_CURRENT.md](../TASK_CURRENT.md)：固定身份、上传/清理责任与独立预算。
- [固定补交合同](../tasks/CH5_CLASSIFIER_V19_EXISTING_EVIDENCE_GITHUB_DELIVERY_20261019/CONTRACT.md)：只读取35份现成文件，不重跑、不读旧ZIP；Codex自动上传，Astra归档后强制删除。
- [来源身份JSON](../tasks/CH5_CLASSIFIER_V19_EXISTING_EVIDENCE_GITHUB_DELIVERY_20261019/SOURCE_EXPECTATIONS.json)及[发行身份清单](../tasks/CH5_CLASSIFIER_V19_EXISTING_EVIDENCE_GITHUB_DELIVERY_20261019/ISSUE_MANIFEST.json)。

## 规则与已有证据

- [当前工作流入口](CH5_ASTRA_WORKFLOW_CURRENT.md)：继续继承V1.3—V1.9限域规则，不另增泛化工作流版本。
- [强制上传与验收后清理](CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md)：执行/交付权限分域，必须交原始内容的安全副本、回读及清理。
- [四份附件有限独立验收](CH5_PATH_CLASSIFIER_V19_FOUR_FILE_INDEPENDENT_REVIEW_20261019.md)：字节与元数据PASS，实现审查PENDING_REQUIRED_ARTIFACTS。
- [旧冻结合成任务](../tasks/CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018.md)：本地执行已结束，旧4/4批次不重开。

原491成员ZIP安全性仍UNKNOWN；本次不访问它。正式V010不变；model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。
