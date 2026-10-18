# V1.9分类器：四份附件的有限独立验收

日期：2026-10-19。任务：CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018。
run_id：06ed068da2d948649f463889051ea157。
固定合同commit：fa923c6048d958eba772b8145f79cf1fa857ee42；Blob：4e726b000065c282c3a21df415ae69f27a840413。

## 裁决

FOUR_FILE_INTEGRITY=PASS
METADATA_CONSISTENCY=PASS
LOCAL_TEST_VERDICT=PASS_SYNTHETIC_CLASSIFIER_LOCAL（保留Codex报告等级）
IMPLEMENTATION_INDEPENDENT_REVIEW=PENDING_REQUIRED_ARTIFACTS
GITHUB_DELIVERY=NOT_COMPLETED_FOR_THIS_RUN
TEMP_CLEANUP=NOT_APPLICABLE_NO_CANDIDATE_REPORTED

这不是新的工程FAIL，也不是分类器实现已通过独立验收。四份实际附件的完整性及记录一致性已核验；不能用源码哈希索引替代源码、语料和逐项测试输出。未重新运行Windows测试，未访问旧491成员ZIP。

## 实際字节核验

以下均由Astra读取本轮四份附件原始字节独立计算。上传文件名的序号后缀仅作附件消歧，不改变内容。

| 逻辑文件名 | 字节 | SHA256 |
|---|---:|---|
| result.md | 5157 | eea5846cb80d395101b23b681c99b5de56d9089039f69216bdad15702c993a9d |
| manifest.json | 9810 | 980cda58c798e1731fd4fd7ae41325d8302b73452cd5e00fb0f2457a86b7873e |
| SOURCE_TEST_SHA_INDEX.json | 1970 | 80920ffa46f262776ea82312f5935186c532ec5ac754661ad64a19f58ffa766e |
| FINAL_RECEIPT.json | 6419 | 2c2a7d37069e1aa9fb0d077bd17ebd0963f1ab43a2e35d7a707ee4d41171cb76 |

回执内report/manifest/sourceTestIndex三个引用哈希均匹配实物；回执自身匹配Owner给出的6419字节及SHA256。JSON无重复键。manifest成员路径无重复或大小写碰撞，登记路径均为安全相对形式；这只是索引路径检查，不是所列文件内容的公开安全审查。

共25项本地字节与元数据一致性检查通过，包括sourceIndex/finalCompiled跨文件一致、任务/run一致、合同登记一致、统计分母和账本尾哈希引用一致。它们不是91个样本或1754条断言的复跑。

## 记录对账

manifest登记33个载荷；加manifest自身及独立FINAL_RECEIPT，声明总数为35。登记载荷长度之和303141，加9810和6419，等于319370字节。该式核实了报告内声明的加总，不是对Windows磁盘上35份文件的独立清点。

本次附件仅包含33个载荷中的result.md与SOURCE_TEST_SHA_INDEX.json，另有包外manifest和回执，共4份实际文件；其余31份登记载荷未作为本轮附件提供。不能声称已逐文件核验全部33份载荷。

七类混淆表每行TP+FP+FN+TN均为91；所有报告FP/FN为0。TP合计113与91个样本并不矛盾，因为统计单位是逐样本多标签类别出现情况，不是逐span准确率。91/91、1754/1754、56负例、15预设UNKNOWN在报告/manifest/回执间一致，但未经逐样本输出独立重算。15个UNKNOWN记为预期阻断，不是泄露证明，也不表示真实ZIP安全。

回执报告4批、790.5369083秒、Python/后代/工作线程/执行期网络/科学0；另列12次治理只读GET。不能把执行期网络0写成全流程网络0。保护20项和Git证明3项、资源账本及错误保留均有摘要登记，缺少对应原件，本轮不认证Windows执行事实。

FINAL_RECEIPT写明controllerExit=PENDING_EXTERNAL_TOOL_COMPLETION；后续退出仅有用户转述，外部工具完成原件未提供。因此本轮未独立认证控制器退出。

## 尚缺的实现验收原件

优先需要：src/PathClassifier_reliable.cs、tests/SyntheticSuite_reliable.cs、fixtures/synthetic_cases.json、attempt_02/RESULTS.json、docs/CLASSIFIER_BOUNDARY.md。要核实编译来源、保护、首次错误和资源终态，还需COMPILE_INDEX、TEST_SUMMARY、FIRST/FINAL_PROTECTION、resource记录、保留错误及控制器退出回执。源码/测试/语料身份已在现有索引登记，应交付原件或明确脱敏派生件，不手工重写为新样本，也不因补交而重跑测试。

目前未读取这些实现文件，不能断言System.Uri/System.Text.Json的调用方式、offset映射实现或测试gold独立性正确；上述实现描述仍来自result.md。

## 固定权限

旧V1.9合同明确LOCAL_ONLY/NO_NETWORK，不能追溯将未上传判为Codex违约。Owner新指令要求此后所有需验收的新任务冻结自动GitHub交付及验收后强制清理，见CH5_MANDATORY_REVIEW_DELIVERY_AND_CLEANUP_20261019.md。

不新签执行任务、不恢复旧预算、不运行旧ZIP扫描或科学。后续补证只需交付既有必要材料；是否执行须有明确新授权。model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。
