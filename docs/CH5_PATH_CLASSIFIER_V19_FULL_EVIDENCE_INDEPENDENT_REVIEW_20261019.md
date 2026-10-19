# V1.9分类器完整证据独立验收与远端临时清理回执

日期：2026-10-19
任务：CH5_CLASSIFIER_V19_EXISTING_EVIDENCE_GITHUB_DELIVERY_20261019
交付run_id：1a3849c860944d119d3eb08497449139
来源run_id：06ed068da2d948649f463889051ea157

## 1. 最终裁决

`PASS_BOUNDED_SYNTHETIC_CLASSIFIER_EVIDENCE_WITH_OBSERVATIONS`

接受范围仅限V1.9分类器在固定91个合成样本上的既有实现与测试证据、以及本次远端交付包完整性。没有执行、编译或重跑分类器。此裁决不表示生产文本穷尽覆盖、不表示旧491成员ZIP安全，也不授权恢复任何科学任务。

## 2. 固定远端身份

- Review branch：`review/ch5-classifier-v19-evidence-20261019`
- Delivery commit：`41922a7370f8388ef1a5d0063327da65f3066e52`
- Tree：`5a386bc1066d23c4c138c3340fc517c472603825`
- 唯一 parent：`69652a0791e813ffaa0dd629feafcf9b5bd4db79`
- 远端临时目录：`_review_tmp/ch5/classifier-v19-evidence-20261019/`
- 远端白名单：`result.md`、`manifest.json`、`evidence_sanitized.zip`

实际读取远端Git ref、commit、目录及三份文件。Commit的唯一parent与固定parent一致，diff只新增三份白名单文件。

## 3. Astra独立字节核验

| 文件 | 实际字节 | 独立SHA256 | Git Blob |
|---|---:|---|---|
| result.md | 3671 | `26274718469a8cd490d8066691d5ca5ca67127cd3010b7b3452ef8955ce763a1` | `0a8333420ac812221af03702bb707bbf61983a0e` |
| manifest.json | 28835 | `184e0586764e428e5ed5993e92b0250c48aed15b3d8373246cbad9739014f91c` | `cd89b7b6b72e283dc6943c53d3b55cb30f535876` |
| evidence_sanitized.zip | 108004 | `083834e6f78b83e163579a096fa80b702b2519d0c8900029b0e3f8298a88b74d` | `194418641ec3b94db51e5c8387dfd3604aabf391` |

ZIP通过Base64原字节回读并由Astra独立解码；ZIP字节数与SHA256均匹配发布回执和manifest。独立解析ZIP central directory：44/44成员，声明解压总量383547字节；中央目录边界与EOCD精确闭合；44/44成员解压长度与CRC均通过；重复路径0、大小写碰撞0、绝对/盘符/UNC/路径穿越名称0、链接0、嵌套归档0。Manifest登记44成员，路径、长度、计数对齐。成员SHA256列在冻结manifest中；本次独立复算了ZIP整体SHA256，但未独立重算每个解压成员的SHA256，因此成员级SHA256独立复算记为LIMITATION，而非宣称完成。

## 4. 内容和实现审阅

- ZIP包含35份来源副本和9份delivery audit材料，共44成员。
- 来源映射为29份RAW_EXACT、6份SANITIZED_DERIVATIVE；6份仅针对私人路径/机器元数据进行脱敏。分类器最终源码、最终测试源码、合成fixture和逐样本结果标记RAW_EXACT。
- 内容审计记录覆盖JSON键/值、源码字面量、原始与解码JSON语义、URI authority/userinfo/query及有界Base64检查；审计报告为PASS，未发现需阻断发布的内容。
- 静态阅读分类器源码与边界说明：只接收内存字节，不执行被审查文本，不访问文件系统或网络；严格UTF-8、System.Text.Json、System.Uri与结构化Windows/UNC token分类；分类与安全判定分离；JSON原始转义与解码语义分开输出；偏移采用半开区间并记录UTF-16字符/UTF-8字节映射。
- 原始测试报告记录91/91样本、1754/1754断言、0失败；多标签逐样本统计而非span级生产精度。Astra未重跑测试，仅审查源码、fixture、逐样本结果和原始报告的一致性。
- 本任务没有读取旧491成员ZIP；其完整安全性仍为UNKNOWN。
- 历史源控制器退出原始外部完成字节缺失、初始工具祖先进程内核身份未知，保留UNKNOWN；没有伪造补证。

## 5. 资源与科学边界

Delivery回执记录耗时956.377秒、计费进程131/256、Python启动2/48、E1批次3/6、fake-bare 1/3、SSH预检1/2、fetch 2/3、push成功1/1、只读GET13/64。科学/模型/runner/分类器重跑/旧491成员ZIP读取均为0。执行器回执声明controller在封存时仍等待外部工具完成；随交付报告提供的外部工具完成事件为exit_code=0。该历史证据仍标记为Codex报告，不视为Astra独立内核认证。

## 6. 必须执行的清理

Astra已将本裁决永久归档到治理分支并回读后，必须删除review branch当前tree内精确三条白名单文件：
- `_review_tmp/ch5/classifier-v19-evidence-20261019/result.md`
- `_review_tmp/ch5/classifier-v19-evidence-20261019/manifest.json`
- `_review_tmp/ch5/classifier-v19-evidence-20261019/evidence_sanitized.zip`

清理必须是单个普通non-force commit，唯一parent为清理前review HEAD；不得触及其他路径或重写历史。随后回读分支HEAD与三个路径缺失。Git历史中的旧commit仍保留这些字节，删除当前tree不等于历史抹除。

## 7. 正式科学状态

`model_activation=False`
`REAL_GE=False`
`Results=FALSE`
`V011=NOT_STARTED`
`FULL_RUNNER_IO_CLOSURE=BLOCKED`

最终分类器裁决：`PASS_BOUNDED_SYNTHETIC_CLASSIFIER_EVIDENCE_WITH_OBSERVATIONS`
原491成员ZIP：`UNKNOWN_NOT_SCANNED`
清理在执行并回读前：`TEMP_CLEANUP_PENDING`
