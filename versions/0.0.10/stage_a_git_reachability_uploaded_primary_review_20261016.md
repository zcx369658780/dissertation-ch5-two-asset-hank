# V010 Stage A：上传脱敏原件的Astra独立审查与限域结论

日期：2026-10-16（北京时间）。
**审议分类**：`STAGE_A_DOCUMENTARY_LIMITED_ACCEPT__FROZEN_SOURCE_REMOTE_SHA256_9_OF_9_INDEPENDENTLY_REPRODUCED__LOCAL_WINDOWS_PROVENANCE_REPORTED_ONLY`。
**交付状态**：`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`；`GITHUB_REVIEW_NOT_DELIVERED`。
**范围界限**：接受冻结源码和Git对象的**可复核文档证据**，不得称为Astra亲自执行Windows clone、磁盘hash或common-dir独立性检验；不得据此升级成完整Windows runner I/O PASS或任何科学数值结论。
**当前执行许可**：`ACTIVE_TASK=NONE`，`NO_NEW_GIT_OR_PYTHON_OR_HA_AUTHORITY`。
**下一Owner决定**：`WAIT_OWNER_FRESH_V010_WINDOWS_ENGINEERING_ONLY_PREFLIGHT_AUTHORITY / STOP`；任何Stage B-E工程Python与HA须分离授权。

## 一、精确权威与上传文件（本审议直接读取）

上轮[Stage A唯一正式任务](stage_a_model_git_object_reachability_recovery_task_20261016.md)：发行commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`，tree `70a7662ba654dff6acbe05e3a8b0444324b8f346`，task blob `3688674363aa8a0c45a7a322c9c2098baed62fae`。Codex本地据称已交付`A_STAGE_OBJECT_REACHABILITY_VERIFIED`并STOP；前[仅凭口述接收审议](stage_a_git_reachability_local_only_intake_20261016.md) blob `00c79477243d2a3906a1f8004114adf07c01fa0e`，现由本轮上传原件扩充核查，而不追改历史审议。

本会话用户**实际上传**两份已脱敏原件，已在当前运行时读取原始字节并独立计算：
- `review_stage_a_model_ref_reachability_result_20261016.md`：6190字节；SHA256 `A1DFCAA8FAEA7A1A257D119A54F2AFBA4911FDC705B5B589B08239316F5C26F8`。
- `review_stage_a_model_ref_reachability_manifest_20261016.json`：15107字节；SHA256 `C6593C9C1B1B0DD8FB84A52D3D93C242F01311F359A0F574E43FE9357CE66ABC`。

两者UTF-8、无BOM/CRLF、末尾LF；JSON实际解析、九份源码路径/Blob/SHA256/大小、逐条Git命令摘要及预算时点字段检查完成。检查常见凭据、私钥和Windows用户目录路径模式未发现明显敏感项，**不保证对所有未列出秘密绝对完备**。这两份上传文件仅作为本会话直接审阅证据，不自动发布/补push为Codex旧review候选。

## 二、冻结Git远端复查与九份SHA256真正独立复算

当前远端精确模型分支 `refs/heads/codex/ch5-v010-matlab-first-20261015` 的HEAD仍是 `94de4501dec051b969bee9d852eba2d4591f30ef`，固定Commit Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，唯一Parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，经GitHub Connector原始Git对象独立检查。

Astra将GitHub从上述固定Commit真实读取的每份Python源码UTF-8内容重新编码成原始字节，并用经常规 SHA256 空串及abc向量检查的独立算法**重新计算SHA256与字节大小**；以下9/9与上传Manifest的三Blob列、SHA256及bytes四类字段逐项一致。对应身份不会随治理分支动态HEAD改变：

| 冻结src/ch5_two_asset_hank/相对路径 | SHA256（前16位） | 原始字节 |
|---|---|---:|
| multi_province/mainline_household_runtime.py | 400F7D05BB63E235 | 16079 |
| corrected_diagnostic/selector.py | 25B93033FD886A15 | 62595 |
| corrected_diagnostic/generator.py | EA3D168AAFA18E28 | 5911 |
| corrected_diagnostic/option_a_step.py | 62B5FFDB5C25500B | 41938 |
| corrected_diagnostic/nonlinear_continuation.py | 189B3E6F010C3465 | 70586 |
| corrected_diagnostic/contracts.py | 5E5DA41969571A46 | 2056 |
| multi_province/corrected_household_adapter.py | A6D1B5B46FC91C91 | 7649 |
| corrected_diagnostic/v1_q1_topology.py | B40B1E03C8E67E8 | 34326 |
| corrected_diagnostic/q1_kfe_validation.py | 54680D232B1E383F | 29048 |

九份合计270188字节。**独立核验结论**是：公开冻结源码与Codex在上传Manifest声明的`diskBlob`/`sha256`/`bytes`记录完全吻合，且不存在替换另一个已知Commit源来获得一致记录的表面问题；**不能**凭这种交叉核对推导Astra亲临Windows硬盘实际读过该clone的九文件。因此本文明确`REMOTE_HASHES_REPRODUCED`、`LOCAL_DISK_BYTES_ASSERTED_BY_CODEX_WITH_MATCHING_DIGESTS`两个不同层级。

## 三、Git/系统过程证据等级与资源账

JSON自洽性独立查明：
- 9份源路径唯一，Git`expectedBlob = treeBlob = diskBlob` 9/9，全部`match=true`；自报签出commit/tree/parent、`independentCommonDir=true`、`alternates=false`、`shallow=false`、`promisor=false`，`objectRawBytesAuthenticated=11`（commit+tree+9 blobs）均在报告及Manifest中对应，但本机会话并没有实际枚举Windows common-dir或证明加载路径。
- `commandReceiptsBeforePublication`恰有19个连续且唯一的ID，全部记载`exit=0`；其中前14个分类是`modelNetwork`2、`stageA`12，吻合“Stage A显式Git14条成功”，其余5项属发布准备而非模型Stage A。Git内部spawns明确`UNKNOWN`。上传仅含输出字节数和哈希摘要，不含未经脱敏raw stdout/stderr或准确本机argv，不能重演其执行。
- Stage A模型单次clone、网络2/2、本地九文件认证、原保护树未访问、Python/pytest/AST/import/runner/HA/HJB/KFE/GE/IRF/真实数据0，均为**Codex本地回执级声明**，不是Astra对Windows进程与保护目录的实时取证。
- Manifest`stageA.gitWorkspaceBytes=511561812`，后续发布准备时模型511561812B＋独立发布工作区497018989B＝`combinedGitBytes=1008580801`，加和精确；后者为**发布准备中途快照**。Manifest`resourceSnapshot`中的`nonGitArtifactBytes=320419`、`elapsedSeconds=364.3658056`及报告文档另有335526B/364.413s，均明确属于不同记录时点。其后Owner转述的**最终本地封存**Git 1023532480B/2GiB、工件376945B/16MiB未由上传Manifest或本地原回执独立重算，但无明显数值矛盾。
- 源上传文件没有最终私有`DELIVERY_RECEIPT.json`，Owner转述其SHA256 `56AD3D6F83782886D4E6E49FB0E37622B5E20EF8D94C2D94A739C62CF39B97D0`；未访问原字节，**不能宣称hash被Astra确认**。Manifest的19个命令收据不包含后来失败的push事务原始回执。

## 四、发布失败的独立裁定

GitHub Git-refs实际查询 `review/v010-stage-a-model-ref-reachability-20261016` 返回404；Codex称本地候选 `d84cc76b19cbb81e097f502348b5073633fbda6e` 原始Git commit查询也是404。对“push恰一次、退出码128、根因受控Git环境未提供认证”的陈述，现仍仅有Codex/Owner转述，**两份上传文件均没有完整最终push exit128原始命令回执**。故保持 `LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`、`GITHUB_REVIEW_NOT_DELIVERED`，不重试、不上传原始私人回执、也不拿本治理审查提交冒充候选已发布。

## 五、正式限域裁决与下一授权边界

**限域接受**：在“固定模型远端来源真实性、九份源码哈希/字节与本地自报记录完全一致、Stage A流程及预算记录内部可核”范围，认定`STAGE_A_DOCUMENTARY_LIMITED_ACCEPT`。Stage A目标已有足够证据进入**后续工程preflight的Owner授权决策**；下轮受权工程runner必须独立重验实际模型clone与可信OS/解释器/argv/common-dir边界，不能把本审议当作Windows OS级运行证明。

**仍然阻断**：`LOCAL_WINDOWS_RUNTIME_ATTESTATION=NOT_ESTABLISHED`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`、`Results FALSE`。先前Stage A任务已完成并STOP，任何Python工程流程、Git补推/再clone、真实HA都无自动许可。未来若要ENGINEERING_ONLY preflight，Owner必须另行批准新边界/预算；其后HA科学计算继续另行授权。

严格保留冻结V010 plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`、原fixture/单点manifest、之前两次单点Python各1/1和首次存储超额、实现pytest4/6-driver1/4-HA1/26-selector1626-roots1642。原8dirty/index/common-dir/untracked/ignored/历史失败证据、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、C8 A–D REQUEST_ONLY、V011 NOT_STARTED全部维持。不改任何V010经济方程、GovInv、税、same-S、原递推冲击或V1.2工作流。
