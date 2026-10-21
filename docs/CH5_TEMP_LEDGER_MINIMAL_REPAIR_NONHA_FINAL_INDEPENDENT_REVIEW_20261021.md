# 第五章 TEMP V010 — 真实 Budget 最小修复无 HA 隔离回归独立终审
日期：2026-10-21
TASK_ID=CH5_TEMP_V010_LEDGER_MINIMAL_REPAIR_NONHA_REGRESSION_20261021
RUN_ID=2e291bedc84d41199fa8d187898eb6a2
ASTRA_MAIN_REVIEW=PASS
PASS_SCOPE=BOUNDED_ISOLATED_DERIVED_BUDGET_PATCH_AND_NONHA_PAIRED_REGRESSION_EVIDENCE
PATCH_STATE=PATCH_PREPARED_NOT_DEPLOYED
PRODUCTION_RUNTIME=UNVERIFIED
GLOBAL_SUPERVISOR_READER=UNVERIFIED
FORMAL_RESULTS=FALSE

## 1. 固定Git候选与原字节独立核验
- 原冻结任务issue_commit=`c0b169472cba9066398b3b97385fcadff65c59a5`、发行HEAD=`6de4d7be1e0202141a57be7c26cbb85378bf581b`；远端独立review分支`review/ch5-temp-ledger-minimal-repair-nonha-20261021`指向candidate `6cbac91ccaab323a938e94a7bc0720238c91dd36`，tree `89c4652ad47c5e869a92b24d26d23aac53a5d59d`，唯一parent `f34cbd06e613481bf185d839a7e319e30cfc192f`。compare ahead1/behind0，**仅新增**`_review_tmp/ch5/temp-ledger-minimal-repair-nonha-20261021/`三白名单文件result.md、manifest.json、evidence_sanitized.zip。
- Git blob身份分别：result `95bed4ba98233140a40a20450684f8eaea36dd24`，manifest `9c1faae8f44cd7724ff2706ffe9ce350432c5de7`，ZIP `3dd5e6c28ed55f02ec332f0c2fc8c743c9877e56`。Owner提供本候选脱敏ZIP原字节；Astra使用Python标准库核原ZIP **47700 bytes**、SHA256 `76ed04b3864b694bc2475666c970862d9514559775a8db31b40b0c39d28a074f`，计算Git原生Blob SHA1也精确为`3dd5e6c28ed55f02ec332f0c2fc8c743c9877e56`，与固定远端对象一致。
- ZIP **29/29成员**实际展开总199020 bytes，经`zipfile`解压`testzip`、每件`zlib.crc32`、`hashlib.sha256`及字节长度复算通过；远端manifest登记成员身份的按名称、字节、SHA256、CRC32规范化列表与本地完整复算一致。无明显路径穿越、大小写重复、加密、符号链接、嵌套档案。
- GitHub已提供result、manifest原始文本；本轮Owner只另上传ZIP，不宣称三件都经Owner上传。Codex自动上传远端三件早已完成；Astra工具无法把Github Base64无损传给本地标准库的既往`REVIEW_PENDING_IO`已由同Blob原件解锁，不等于Codex漏发。

## 2. 源码修复/配对回归实际审阅
- 已阅读ZIP实际`harness/build_candidate.py`、`repair_support.py`、`nonha_regression_source.py`、`original_boundary.py`、`prior_fixture_support.py`；五个Python文件通过独立静态AST语法解析。builder从已验原Budget的AST派生私有候选，只涉及`guard`、`event`、`checkpoint`、`begin_ha`、`finish`；`safe_ast_patch_manifest.json`把constructor/profile/close和Budget外AST登记为未变。派生私有candidate 13136字节、SHA256 `51005056766f99b9f6c4bf4fe0fb8d42d6547ace8eebba9ab5bba30465ff8a3c`属于Codex私有环境验证**而非Astra直接重算其全源码**；公布的最小patch包含必要修订片段及旧方法AST摘要，未发布整个原私有源码。
- 八份最终配对T1–T6与J1/J2的原始**公开结果JSON全部逐项读取**，均report `same_fixture=true`、`real_science_calls=0`；旧T1/T6与补丁两侧均qualified，旧T2/T3/T4/T5/J1/J2未qualified而补丁侧qualified。输出是Codex隔离Windows上实际运行的记录，**Astra未在Windows重复运行也未独立重取1.2MB私人原始archive**，因此PASS限定为交付证据、代码结构和可审核配对观察，而不是生产Windows OS审计。
- **R1/T2/J2**：旧方法append seq2后WinError5使checkpoint仍seq1与current.next残留，新派生候选验证staged原件身份证据和events prefix后恢复到seq2且无重复append；合法commit的重复checkpoint不改inode，三次恢复均返回无错并保持仅两个持久事件。
- **R2/R3/T4**：修复侧第一次PermissionError对象在secondary finish时继续为同一对象；`classify(exc,'checkpoint')`对普通WinError5标typed shared hard，对无关fixture E1标非hard。`run`原E2_字符串判断**尚未生产接线/未执行full run**，不能据此宣布真实硬故障广播已修复。
- **R4/T5**：受限公开`RepairProtocol`用本地同协议单写者/STOP发布者锁、`admit_and_enter`惰性回调包围持久准入；测试`STOP_ACK`发生在成功commit和惰性entry返回之后，ACK之后新准入为0。原基线相同竞态可出现ACK后返回。此仅**LOCAL_FENCE_ONLY**；生产supervisor/reader及不遵守本地围栏的进程写STOP无全局线性化证明。
- **J1**：event_seq、bool_seq/bool_counter、previousHash、损坏current、partial/unknown/staged JSON、partial event等共**10个负例**，修复侧均rejected、before/after原账本数据文件摘要一致，满足FAIL_CLOSED的已测部分。**T3**：新候选在两种Windows读者共享模式下仍可能遇WinError5，关闭受控读句柄后可按安全stage条件恢复；不能认定历史唯一句柄根因或原生os.replace已不再拒绝。**T6**：新旧helper exit23及reap、charged1/entered0/completed0/failed0/unresolved1一致，原constructor一次性existing-directory拒绝语义保留；wrapper replay不等于原生产resume能力。
- 公布`minimal_patch.diff.txt`仅是受限的安全摘录而非完整原私有diff；私有完整补丁SHA在锁定清单，正式部署/原始全部AST diff需要在后续安全授权集成门重新读取。不能把本轮代码结构PASS升级成整个真实生产运行链PASS。

## 3. 隐私/资源与证据边界
- Astra对全部29公共成员扫描常见密钥/令牌、邮箱、真实Windows/UNC私有绝对路径，并对patch与敏感报告做人工语义聚焦；未见清晰泄露。公开`privacy_review.json`枚举28件（未自列），Astra另直接检查该隐私清单本身。未发布原私人1.2MB ZIP、旧私有日志、完整旧源及完整私有diff。
- 完整最终JSON回执（此前用户粘贴）已独立校验长度10336 bytes和SHA256 `ea191978675bc00e43ca3ce520e4787c0565de89796f72c9012c50a6f5d9ec06`；其余GitHub发布与资源统计来自Codex回执自报。工程Python27/32、工程E1=2/4、4个自有helper已reap，HA/HJB/KFE/GE/IRF自报全0、OS kernel descendants仍UNKNOWN，不能转写为Astra独立内核检查。
- 明确NOT_COMPLETED：原私人Budget原字节与13136字节修复候选全源码由Astra重新SHA/AST验证；真实生产driver接线和global跨进程supervisor/reader；断电恢复与诊断写入失败注入；历史native WinError5唯一根因；真实A1/A2/A3价格桥或HA数值实验。生产包尚未部署。
- 任务正确交付隔离候选和完整八组证据，并保留上述边界，故`PASS__BOUNDED_ISOLATED_REPAIR_REGRESSION_EVIDENCE`不等于`PRODUCTION_READY`。**下一项新任务仅在Owner重新授权后可做实际ledger安全集成和外部协同测试，不允许自动复跑A1–A3。**

## 4. 分层裁决与清理规则
artifact_integrity=PASS__ZIP_RAW_GIT_BLOB_AND_29_OF_29_MEMBER_HASH
implementation_review=PASS__BOUNDED_PUBLIC_SOURCE_AND_PAIRED_TEST_EVIDENCE
privacy_review=PASS__ALL_29_PUBLIC_MEMBER_BYTES
delivery=PASS__CODEX_AUTOMATIC_EXACT_THREE_IN_GITHUB
production_runtime=UNVERIFIED
original_private_full_patch_independent_AST=NOT_COMPLETED
cleanup=ARCHIVE_READBACK_REQUIRED_THEN_EXACT_NONFORCE_3_PATH_DELETE
other_pending_reviews=4e05976bbc8068b971ba5915133e9a6c3b73193d;1579e7f1d7a1975c322dd6ae9af1776e88e83e7c
fetch_seconds=UNKNOWN
integrity_seconds=UNKNOWN
semantic_seconds=UNKNOWN
archive_cleanup_seconds=UNKNOWN

先永久归档终审及CURRENT/TASK_CURRENT/索引/项目记忆并远端readback，确认本review HEAD仍固定后以普通nonforce精确删除本次review当前tree的三文件，逐条compare和404回读，并另归档清理回执。不得触碰旧两个PENDING review，所有科学预算0、V010/Results FALSE/V011 NOT_STARTED维持。
