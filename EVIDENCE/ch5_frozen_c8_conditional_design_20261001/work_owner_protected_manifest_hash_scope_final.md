# 七固定文件 SHA256 被动读回提案（Work 定稿）

2026-10-01 · TASK37 / Builder dialogue7。
状态：**REVIEWABLE_OWNER_PROPOSAL_ONLY_NOT_AUTHORIZED**。先供 Work 独立审查；Builder 不向 Owner 发问。本轮受保护路径 reads/exists/enumeration/hash/body/ACL/identity/native/run 均0。

Owner 原话“我确认，请继续”仅确认原六根的文字定位（owner_six_root_textual_designation_20261001.json，SHA256 FC345EFF1E5E9575B7ECD7554490FBB1FD30B222A97D19D0D03EE3F83DEEFAEC）。定位缺项 CLOSED_OWNER_DECLARED；机器身份及保护仍 NOT_ESTABLISHED。文字确认明确不授予访问，未来七文件哈希需要新的精确 Owner 例外与 Work bounded task；普通继续不构成批准。

指定 JSON 的 proposal_sha256=399D3A8B666179460A93816409071310F87DC65EFA9E310CF1185F8B4138A807 指向先前六根文字定位提案，不指向本文，也不是本次七文件哈希读取批准。此次是新的未授权提案。

## 精确七文件与历史 expected SHA

唯一来源：EVIDENCE/ch5_k1b_c9_output_mutation_a2_security_boundary_specification_20260927/specification_receipt.json，SHA256 BA7B10BC463227025215F2DFCBAA75373D1AB84169D3D609DD050128F82998A7，L68–74。每项通过纯字符串 parent 对应 Owner 声明 R1–R6；不是系统路径解析、存在检查或目录身份绑定。历史 expected 只作未来比较基准，历史7/7不作本轮结果。

|序号/根/来源行|完整绝对文件字符串|历史 expected SHA256|
|---|---|---|
|1/R1/L68|D:\ProjectTemp\c5k1bturn56\reports\ch5_turn6_same_frozen_input_repeat_20260923_run001\execution_artifact_manifest.json|7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61|
|2/R2/L69|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn7_outer_r2_20260925_run001\execution_artifact_manifest.json|413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91|
|3/R3/L70|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn8_outer_r2_20260925_run001\execution_artifact_manifest.json|5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301|
|4/R4/L71|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn8_same_frozen_timing_measurement_run001\science_artifact_manifest.json|5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D|
|5/R5/L72|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_timed_risk_exception_run001\partial_artifact_manifest.json|80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3|
|6/R6/L73|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_post_failure_new_attempt_001\partial_artifact_manifest.json|3B10AB56BC2CE3D8FF9B4FB6442E012CB39686AF389624D17566CC8D68F57D20|
|7/R6/L74|D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_post_failure_new_attempt_001\partial_artifact_readback.json|8191C24E8A472EE702C71A72DB4F4CCC9A0733D432226DFDB6EF0B4045792BAC|

## 若未来单独批准的唯一事实层级

仅 **SHA256BYTE_READBACK_ONLY**：读取上述文件字节以计算 SHA256，并逐项与历史 expected 比较。哈希计算需要读取文件字节；不得解析、显示或另行保存文件正文，不跟随 manifest/readback 内的引用，不做目录枚举、extra exists check、ACL/ownership/对象 identity 检查或写入；不得扩大路径。哈希相等不证明目录对象身份、anti-reparse、snapshot atomicity、并发抗替换、全链保护或任何科学结论。

未来单独新增 bounded 行政预算7，max7 attempts，按表顺序每个精确文件最多一次、retry0；locator、hash命令或 mismatch 任一首失败立即 STOP，不做后续项、不回退、不替代。失败的尝试也消耗额度，所有剩余额度退休不可转授；错误只记录最小 category/code，不输出完整 dump/正文。提案不重置旧 archiveadmin/fixture/actualdata/V1/V2 各1/rem0、行政query2/rem0或HTTP批次1–6的3/2/1/2/2/1 rem0。

下列七个表达式**仅为本提案文本**，不执行、不写脚本，也不在本轮检查参数路径：

```text
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_turn6_same_frozen_input_repeat_20260923_run001\execution_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn7_outer_r2_20260925_run001\execution_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn8_outer_r2_20260925_run001\execution_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn8_same_frozen_timing_measurement_run001\science_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_timed_risk_exception_run001\partial_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_post_failure_new_attempt_001\partial_artifact_manifest.json' -Algorithm SHA256
Get-FileHash -LiteralPath 'D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn9_post_failure_new_attempt_001\partial_artifact_readback.json' -Algorithm SHA256
```

未来若另获批准，只可在既有 EVIDENCE/ch5_frozen_c8_conditional_design_20261001 目录直接新增两输出：

- D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\protected_manifest_sha256_readback_20261001.json
- D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_frozen_c8_conditional_design_20261001\protected_manifest_sha256_read_receipt_20261001.json

本轮不创建它们或目录。未来任务须确认输出不存在，不覆盖证据；记录 attempts/status/actualSHA/expected/match/最小错误及未查后续项，不能把未启动项记为匹配。任何失败保留最小终态证据并停，由 Work 处理，不授权自动修复或重跑。

没有科学/model/真实数据/test/native/experiment/系统query/API采用或根写权限。完整 Objective A及16 UNRESOLVED、window UNACCEPTED不变；六根定位已OwnerDeclared与物理身份/保护未验证分别记录。C9PAUSED、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE；TASK29/33失败原件保留，历史C8科学保留、当前条件链0。当前七路径均未访问、未Test-Path、未hash或正文读取，新增查询/HTTP/研究调用0。

交付 STOP 等待 Work 文档审查；不自验收、不签发后继或推断 Owner 已批准七次字节读取。

## Work 字节读取语义澄清
本定稿仅校准读取语义，原 Builder 候选 SHA BAF28F886C1013C7E7FAD3D28FE35C54B2DE0621579EF8BBC93B2A7C1C8EC0C3 不修改。未来若批准，每个Get-FileHash是对固定文件字节的实际读取，必须记录为受保护文件字节读取attempt，不能声称保护根访问仍0或所有底层文件操作0；仅不解析/显示/另存正文、不进行独立目录查询或根变更。本轮未执行，受保护文件字节读取0。