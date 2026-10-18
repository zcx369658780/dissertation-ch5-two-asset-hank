# TEMP-V010 2×2价格桥任务 — E2共享账本I/O失败独立终态审议

**终态：FAIL_CLOSED_E2_SHARED_LEDGER_IO__EVIDENCE_LIMITED_ACCEPT__NO_FACTORIAL_SCIENTIFIC_RESULT。**
**审议依据：Owner在ChatGPT本轮真实上传原始ZIP、MD、交付回执；独立审阅者没有重新在Windows运行任何科学solver。**

## 1. 独立原证完整性与源码身份

私人ZIP TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_PRIVATE_FINAL.zip：1,214,713B，SHA256 F3E8984FE4D2EF4BE65692C27FA7594D96B870D372A8C45D029899F7891841D8；内部278件（277个被FINAL_PRIVATE_MANIFEST索引，另一个是manifest自身）；**277/277文件长度及SHA256 PASS，CRC无错误**。外部结果报告6,049B，SHA256 564FF051EA4FA197B9A4CB59AC4FA9932A2EC36CF72A1DBD9E45535202CE69AE；外部交付回执3,453B，SHA256 DDEFBE5CB2D6A4C63B3A34E30C0A1E0BE271421C5CB3D9E8C5DE4A8A14BF01C8。ZIP内同名报告与外部MD SHA一致。

冻结任务Commit 2c855f616efbca05c29d4069a44e3c6651070b44，task Blob 4e81556bff068b9bedc6c7c608faf24ee1e439fe。77份源码索引逐件实际重算SHA256、长度和Git blob SHA1**77/77相符**；黑箱HA原SHA B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3；旧postloop adapter SHA 8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06；唯一synthetic fixture SHA BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252。源身份与原证真实，Windows protected-root只读事实仍限于Codex本机receipt。

## 2. 共享账本故障和实际计费

A1科学events.jsonl有11条、A2和A3各25条；**61/61序号和previousEventSHA256链连贯**。A1原子checkpoint current.json仅到seq9，第10条是KFE进入前扣账，第11条是A1第二HA错误；append head和current head不相同，属于真实账本断裂，不能伪装账本完好。A2/A3各seq25当前检查点与事件head一致。

最早故障为A1第一轮第二省，原记录WinError5：os.replace(current.next,current.json)被拒绝访问。残留current.next后再次写checkpoint出现FileExistsError。可能与PowerShell并发读取current.json不共享删除有关，但**尚未独立复现归因**。主控错误延迟识别“局部→共享”硬门：A1 02:39:27Z结束；02:41:54Z才发出全停，A2/A3在两轮后第3轮首省已扣HA费，随即回收。原始延迟、first失败与final纠正都原样保留，不追溯篡改。

A1/A2/A3完成外层0/2/2轮；HA各计费2/5/5，总计12，完整返回1/4/4共9、A1失败1、A2/A3第3轮中断2。**9/9完成HA原始V与density二进制均6400B/件，与各自observation SHA256一致且数值有限**；剩余3次不能伪作完成。每个science driver各1，累计3/3；工程Python最终8/24，pytest0；P0本机先19/19后26/26，未覆盖真实Windows共享读/atomic replace冲突。A0只读历史基准，不重跑。缺少共同完整四ARM轮次，因此**绝不能得出价格桥优劣、交互效应或100轮收敛结论**。余量全部关闭，不重复HA。

## 3. 三份脱敏审阅材料已具备，问题在发布器

上传私有ZIP内已存在真实：
- delivery/result.md 4,542B、SHA256 70B047D4FD3C14182BFE00EA183C55F1917343CC777562108345C470E387500B
- delivery/manifest.json 13,864B、SHA256 24A193F6557FE2EC7FF12872D5097274E6EF0E609D47E5B3B3D05ED38AEC0E9B
- delivery/evidence_sanitized.zip 196,296B、SHA256 9F3F2CDA8360577DE83BFE02D01B6F57814BEE4E03B1C883F3A6A79698DC08E2。内含29件，CRC PASS。

GitHub SSH预检认证成功。唯一Git fetch被PowerShell把 --git-dir=... 和 -c core.quotePath=false 拼成同一个argv，Git在本地报exit128，**没有产生本次fetch的远程传输**；push0，review/ch5-temp-pricebridge-factorial100-20261018经GitHub连接器返回404。本轮无可清理旧temp。正式被封存的科学任务不能为发布器重开HA/旧fetch预算，但可依Owner新决定**签发独立零科学交付修复任务**来完成自动GitHub ZIP交付，而不是再问Owner手动搬运。

## 4. 终态

实验科学FAIL_CLOSED，数学/经济结论NOT_ESTABLISHED，源原字节未改；本轮文档审查为证据限域接受，非科学PASS；工程硬门存在识别延迟与并发I/O风险，未来若继续数值实验必须先修科学journal可靠性。正式V010 ACTIVE_TASK=NONE；model_activation=False、REAL_GE=False、Results FALSE、V011 NOT_STARTED。所有旧TEMP/正式研究预算不结转，原8dirty/index/external common-dir及C盘独立SSD备份保护不变。
