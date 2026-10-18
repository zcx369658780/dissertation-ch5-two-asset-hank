# 第五章工作流 V1.8：来源证据身份与预期值溯源

日期：2026-10-18。V1.8仅补充V1.7交付流程中来源文件身份核验与预期值溯源；V1.4资源门禁真实性、V1.5不可变任务身份、V1.6保护路径边界和V1.7交付闭环继续有效。

## 1. 最新失败事实

交付任务 `TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018` 的本轮run_id为 `6568ae4f4d134f3b9459e47d983f2acc`，在发布前以 `SOURCE_FINAL_RECEIPT_IDENTITY` 停止。Codex额外引入了一个从对话文本手工抄录、长度为65字符的错误预期SHA256；该值并非冻结交付合同规定的身份。不能据此认定来源回执被修改。ZIP和manifest身份按本轮报告匹配；ZIP逐成员审查、fake-bare预检、SSH、fetch、push、远端回读均NOT_RUN。原任务不续跑、不改写，所有原始失败信息保留。

用户提供的正确原始回执身份为：
- `FINAL_RECEIPT.json`
- 长度：9339字节
- SHA256：`14ca468c0c9b4339cea7a8bc91578fc899b88a4be7a9c96d4d7d552945d599f5`

该值用于新交付任务的来源校验；不得再从聊天文本重新手抄/变换。合同中固定的来源清单是唯一预期值来源。

## 2. 来源哈希门禁规则

1. 禁止新增冻结合同之外的“额外预期哈希”并将其升级为强制门禁。
2. 每个预期哈希必须来自固定合同、原始manifest、冻结source index，或Owner明确提供且在新合同中原样固定的来源身份；报告中标明source-of-expected-value。
3. 对源文件执行：先以固定路径/run_id打开实际原件并读取原始字节，再计算字节长度、SHA256；最后与固定预期值比较。禁止先复制哈希到脚本/Prompt再把它当成权威来源。
4. 若原件无法读取，报告 `SOURCE_BYTES_UNAVAILABLE`；若没有可信预期值，报告 `EXPECTED_IDENTITY_UNSPECIFIED`。这两者均为STOP，但不等于源文件损坏。
5. 若实际值与可信冻结预期值不匹配，报告 `SOURCE_IDENTITY_MISMATCH`；若预期值自身的来源/格式错误或校验逻辑使用了非合同值，报告 `VALIDATOR_EXPECTATION_DEFECT`。不得将后者写成源文件已修改。
6. SHA256必须恰为64个十六进制字符；长度、路径、文件名、run_id、来源清单与计算程序均需独立核对。任何复制/转录校验须由程序读取冻结来源字段，而不是人工二次输入。
7. 校验程序必须输出expected value、expected source、actual value、actual length和decision。若校验值来自用户本轮明确提供的原件身份，合同应记录该授权文本并将其固定为独立元数据。
8. 已发生的失败任务只作为历史保留；不得把本规则当作旧任务的追溯重试授权。若需要重试交付，必须发行新的delivery-only任务、固定新run_id并关闭旧任务。

## 3. 交付闭环继续适用

需要Astra独立验收的任务必须在签发时固定远端review branch、parent、唯一临时路径、白名单、大小、fake-bare预检、发布/回读/清理预算。ZIP需逐成员及嵌套归档检查；不得未经脱敏发布RAW。Astra必须取得ZIP真实字节并独立重算SHA256/长度。永久归档及回读完成后，才清理指定review分支当前tree的白名单临时文件。

本规则不授权任何科学、runner、测试重跑或已关闭预算恢复。正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results=FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。
