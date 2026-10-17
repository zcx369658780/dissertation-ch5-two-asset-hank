# 第五章版本登记（2026-10-17 V010来源恢复与timestamp局部修复已审）

**VERSION=V010/V0.0.10；V011 NOT_STARTED；ACTIVE_TASK=NONE**。
**LAST_TASK=V010_SOURCE_SCRIPT_PROVENANCE_RECOVERY_AND_CONDITIONAL_TIMESTAMP_FIX__DELIVERED__STOPPED**。
**LATEST_REVIEW=DOCUMENTARY_LIMITED_ACCEPT__CURRENT_PS7_6_6_TYPE_COERCION_CODEX_REPORTED__24_OF_25_EXPECTED_MATCH__1_SPEC_UNRESOLVED**。
**REVIEW=[正式主审](../versions/0.0.10/source_script_provenance_conditional_timestamp_local_only_primary_review_20261017.md)；REVIEW_BLOB=d6a53e96e359ac2c3d437ed9025cd5f58b129492**。
**HISTORICAL_EXECUTED_BYTES=UNVERIFIED；HISTORICAL_PS_VERSION=UNKNOWN**。
**NEXT_GATE=WAIT_OWNER_FRESH_V010_TIMESTAMP_SPEC_BOUNDARY_AND_EVIDENCE_EXCHANGE_AUTHORITY / STOP**。
**NEW_RUNTIME_AUTHORITY=NONE__PS0__GIT/SSH/PUSH0__PYTHON0__VERIFIED_LOADER0__RUNNER0__SCIENTIFIC_HA0**。
**LEGACY_SEAL_CHAIN=UNVERIFIABLE；ORIGINAL_SANITIZATION_DENIAL_CAUSE=UNKNOWN；HISTORICAL_LEDGER_DEVIATION=UNRESOLVED**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；HA_SCIENCE_NOT_RUN；model_activation=False；Results FALSE**。

[上一冻结任务](../versions/0.0.10/source_script_provenance_recovery_conditional_timestamp_fix_task_20261017.md)发行Commit`fafffe0582a213ceec25312f97f47ade6f1aa508`/Blob`22aea7c18716c36ffb1f3154d35d751d9f524bf1`已STOP。Codex Gate R从以前执行调用和匹配失败receipt恢复现存脚本定位、**当前**整个脚本SHA256及字段/schema anchor；但历史没有源码文件哈希，**不得推断历史运行时与当下同字节**。Gate T报告当前PowerShell 7.6.6把原始JSON String、满足旧Z末尾和日期规则的timestamp解析成System.DateTime/Utc，旧脚本解析后仍string的断言发生类型误拒；历史解释器版本未知。Gate F报告25个新合成中24个预期匹配、高精度形态1个`SPEC_UNRESOLVED`不计PASS；一次原字段修正版只读复核据报接受、源hash未变。Astra只独立核验任务的Git身份，没有本机源码/原raw/25项逐案文件，不把局部结果升为`ASTRA_INDEPENDENT_WINDOWS_ENGINEERING_PASS`。

Codex自报PS2/2、旧三根depth0盘点一次各条目4/4/9、旧6文件14次累计读取95,510B、新7文件47,844B、Git/SSH/fetch/push/Python/runner/HA科学0；墙钟/写前reserve等尚未独立读账。本轮first/final据报同run_id与单向hash链，Owner最终receipt SHA256 `B37FA71992497C299D2E218029D08AD1F863A83A6F6C60C852342C82EB0430B0`，未给Astra原字节重算。全部本任务及之前STOP未用预算关闭不结转。老20例first raw/run_id永缺UNVERIFIABLE，新17例链仍LOCAL_ONLY，旧Sanitizer拒绝UNKNOWN且旧材料DENIED，历史ledger复制raw argv/源码偏差UNRESOLVED。

M1源模型纠错和Python代码候选、合成工程进展为局部成果，但真实Windows runner/完整I/O未闭、corrected HA单点仍UNTESTED；M2多省稳态及GovInv/Zt冻结后GDP≤1%独立校准未过，M3原冲击递推缺合格基点，M4无Results资格，V011 NOT_STARTED。冻结科学plan commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f及模型commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5不改。原MATLAB corrected HA→多省顺序→GovInv收益边界×0.9/1.1/Zt→GDP目标≤1%独立验证→lagged-NKPC递推、目的地税一次、same-S/前一完整轮raw ra0、phi_max=.3、人口人均/省财政总量/三劳动账不改。Owner既有C盘独立SSD备份+GitHub、SSHKey443、可信工作站风险决定不变；原8dirty/index/staged/untracked/ignored、外Git common-dir、旧失败原证、C盘备份及real C8/2017/2018/B3禁止触改。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；V011 NOT_STARTED**。
