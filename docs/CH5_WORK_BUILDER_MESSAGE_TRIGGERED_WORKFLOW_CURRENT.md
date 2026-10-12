# 当前工作流入口已迁移
2026-10-12 Owner批准的新方式见 CH5_ASTRA_WORKFLOW_CURRENT.md；本文件以下全部Work消息触发、路由、通知预算与逐阶段验收规则仅历史，不再生效，不恢复自动派单。
科学/数据/不可逆保护及旧试验结论范围保持，历史通知不是接受。

---
# 第五章 Work—Builder 消息触发工作流（现行修订）
生效：2026-10-07（Asia/Shanghai）。Owner明确授权保存四目标试运行验证后的改进，发送当前Codex并再测试连续四单。以下修订为当前有效规则，优先于后附2026-10-06历史原文；历史正文完整保留，不追认旧STOP或恢复闭预算。

## 当前权威与路由
- Work负责人及独立验收：01a111b6-410f-7fe1-8492-40b00e660b49/local。
- 唯一Builder：01a1138a-7ada-7192-aa04-4d652e762d9f/local。旧Work/旧Builder退役，不通知、不唤醒。
- 实际树D:\ProjectTemp\c5k1bturn56；Zotero仅UI归属，不授权其仓库、Project sources、deep-learning-hank或跨树索引。
- ref codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922、HEAD a1db8c114dec0ab69d69a5576e153a7f868cba0e、七tracked dirty/index0是2026-10-06实核快照，不冒称当前。Git读取是否开放由每单另签；全部dirty/untracked/index原位保留。
- automation work最近实核PAUSED，保存5分钟周期不生效。本修订不查询/修改target、不恢复、不建替代定时。消息是正常触发路径，不用heartbeat/循环查询兜底。
- Owner已在Builder聊天直接授予本项目长期完成/实质停点报告授权，准确当前对象与每单次数仍须签明；不逐单重复请批，不扩大其他通信或科学/保护权限。

## 消息闭环与执行合同
Work签完整长任务单发给唯一Builder后结束本轮。Builder在目标、路径、预算内连续执行；先落盘报告、准备receipt和PREPARED意图，再一次消息通知当前Work，保存真实工具结果并结束。Work被实际通知拉起，独立验收后按目标依赖和当前授权续签。
每单明确ID/版本/关联码、目标标准、输入与次数/缓存、输出与文件归属、总时间和无进展阈值、修正/首失败门、验证、Git/科学/保护、准确通知对象/次数/重试、Work验收预算及最终停止点。
Builder与Work各自独占报告/receipt/notification及review/control，不并行修改同批文件。四目标试验第四目标终裁后必须总结停止，修正不增加目标数，按交付版本计通知，不自行派第五单。

## 已验证的改进
1. 普通写前输出工具、文字、格式错误可在准确合同内有限纠正，默认值由每单签明（本试验最多2次），记录失败步骤、原因、改动和消耗。输入hash/strictUTF8/缓存缺失、范围/身份/保护、未知目标冲突、部分写入或写盘状态不明、预算耗尽仍首失败STOP，不覆盖/删除残留。不得把普通纠错扩为追加输入、消息重发、预算重开。已落盘需新版本由Work准确签发，不修改旧失败事实。
2. 使用原生PowerShell/.NET严格UTF8与DateTimeOffset.UtcNow或Unix毫秒，起止同一UTC类型，等待/工具/通知收尾计入墙钟。不假定工具环境有btoa/Buffer等未声明全局；负耗时为账本错误，保留原值并在许可的新记录说明，不偷偷改旧receipt。
3. 后续聊天返回内容不设8KiB门；文件cap、次数、范围、总预算仍有效。紧凑状态查询与必要正文读取分开。先取准确最新turn状态，不固定读取超长AGENTS/CURRENT/TASK历史；需要正文必须有单独白名单和次数。
4. 同聊天沿用一次已核身份缓存；是否重核由准确任务单决定。继任不能冒用旧聊天缓存，必须核实自身ID和当前路由。
5. 验收执行STOP/CLOSED与交付接受状态REVIEW_PENDING分别记录，后者不授继续读取或重跑。依赖缺失交付的后继等ACCEPT；已授权独立目标由Work判断继续，不把普通文档STOP自动扩大成全项目STOP，也不换名复活关闭目标。

## 通知、去重与有界收尾
去重键为[stage_id, delivery_version]二元组；correlation辅助核对，不替代键。同版本完成/STOP共一次通知、retry0，修正新版本须新授权。重复通知只识别已有终局，不再次裁决、派单或复用预算。
notification_sent、work_received、work_review_started、work_decided分开记录。Builder后三项UNCONFIRMED，Work按实际事件独立补记；发送工具确认不直接证明接收或ACCEPT。通知失败保存实际结果与送达UNKNOWN，不重发、不换目标、不定时兜底。
消息到达时账本可能仍PREPARED或同turn仍inProgress。Work只有在本单预签新验收预算内，可对该同turn有界完成等待一次（上限50秒）和追加notification读取一次；先核剩余预算，不循环、不换turn、不重派/重发。仍未稳定则保留UNKNOWN/REVIEW_PENDING并结束本次验收，余预算关闭。
未来签单在不追加观测的前提下记录实际接收采样UTC、review开始/终裁UTC、wait调用起止及elapsed、明确计时精度；等待上限不能当实际耗时，准备receipt不能当最终完成账本。

## 观察证据与停止边界
首轮四目标最终4/4静态文档接受；原S1 STOP与Owner新授权repair-1分开，5个交付版本各通知1、retry0。四个已接受版本的消息均实际触发Work独立验收和必要续签。S4实际普通收尾工具故障纠正1/2，追加输入0、消息重发0。证据总览：docs/CH5_MESSAGE_PILOT4_WORK_FINAL_SUMMARY_20261007.md。
这是有限试运行，不证明数小时/数日长期可靠率。失败送达歧义、重复事件持久去重等实际异常仍未测试；纸面案例不能称runtime PASS。
所有旧STOP/CLOSED和耗尽预算保持。五False、ResultsFALSE、C9PAUSED、完整Objective A16UNRESOLVED、windowUNACCEPTED、CALL_LEDGER_UNRESOLVED及MISSING_HISTORICAL_EVIDENCE不变。来源认证、原live身份、科学/consumer/guard/保护变化、发布、外传、重要删除均未由本工作流开放。
四目标试运行完成后关闭全部执行/修正/验收/通知余预算，无自动科学后继。实质下一门仍为Owner提供准确历史线索后另签有限核验，不扫描/摘要/合成复活定位链。

---
# 以下为2026-10-06完整历史原文
旧路由、单次通知授权及旧测试号仅历史；冲突处由上述现行修订覆盖。

# 第五章 Work—Builder 消息触发工作流（现行）

生效：2026-10-06（Asia/Shanghai）。Owner明确要求：Work发布长任务单并直接唤起Codex；Codex完成后发布报告并唤起Work。Owner随后授权固化文档并测试一次闭环。
本文件是现行路由、触发和通知规则。此前文档中的旧会话、5分钟heartbeat或定时监督规则仅作历史记录；冲突处以本文件和Owner最新要求为准。

## 唯一路由与定时状态

- Work负责人及独立验收人：01a10e8a-c26c-7ed0-9af0-cc4442c2ecf0/local。
- 唯一Codex Builder：01a10af3-93d6-75b2-a7dc-d0627d5c8ebd/local。
- 唯一实际树：D:\ProjectTemp\c5k1bturn56。
- ref：codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922。
- HEAD基线：a1db8c114dec0ab69d69a5576e153a7f868cba0e；每阶段是否刷新及读取预算由任务单明确。
- automation work已PAUSED。保存的周期不生效；不得以heartbeat、轮询、定时器、睡眠循环或新automation作为日常接续/失败兜底。
- 复用两个现有会话；不创建、更换、迁移会话，不向旧Work/旧Builder/Dot发单或报告。Zotero项目仅UI归属。

## 唯一正常闭环

1. Work签发完整阶段长任务单，通过send_message_to_thread发给唯一Builder；任务单同时明确Owner授权的完成/实质停点回报、准确Work路由及本阶段通知预算。Work随后结束本轮，等待Builder消息。
2. Builder在已签目标、路径、总预算和自主范围内连续执行。普通实现问题自主诊断修复；明确首失败即停、一次性、禁重试条款优先。Work不逐步骤问询，也不并行修改Builder同批文件。
3. 完成或实质停点后，Builder先保存可核验报告和预算账本，再通过send_message_to_thread向唯一Work发一次带阶段、版本、证据路径和结果摘要的通知，触发Work继续。通知成功后结束本轮，等待验收；不得自己签后继。
4. Work被完成消息触发后，独立核验交付与原始证据，给出准确ACCEPT/REJECT/STOP及预算结案。必要时集中签发一批实质修复；只有当前已开放范围内确有下一目标，才签下一份长任务单。Owner暂停或缺真实/科学/保护证据时停止依赖动作。

正常阶段不使用wait_threads/read_thread的定时轮询。完成消息到达后，为核原始进程/通知结果，Work可在新签有限验收范围内读取最新Builder turn一次；这属于验收，不是触发替代。
定时器不会主动恢复。若Owner日后明确要求额外定时机制，须独立说明用途和授权，不能从“继续工作流”推定重启heartbeat。

## 长任务单必填合同

每阶段写明阶段ID+版本、目标、可观察标准、准确权威上下文、读写路径及文件归属、约束、自主范围、少数决定停点、总时间/资源预算、无进展阈值、证据位置、Git权限、必要验证与修复规则、通知对象/次数/重试，以及Work验收范围。
授权过的普通可回滚工程事项由Work判断，不逐步骤重复请Owner批准；科学事实、来源认证、原live身份、重要保护/权限目标、发布外传删除等不能由备份或一般工程授权替代。

## 通知、接收、验收与去重

- 去重键为stage_id + delivery_version。Builder只发该版本一次完成/停点通知；Work同版本只裁决一次。重复消息只识别既有终局，不重派、重跑或恢复预算。
- 分开记录notification_sent、work_received、work_review_started、work_decided。Builder只记录其通知动作；后面三项由Work依据实际接收和审查记录，不能提前宣称ACCEPT。
- Builder发消息前将报告落盘，记录通知意图；发送后保存实际成功/失败及目标。若新预算允许通知记录更新，任务单必须列明次数。
- 通知失败：保存固定失败事实，停止，不无限重试、不换目标、不建会话、不启用定时兜底。未获准确次数授权不能发消息。Owner已明确授权本次闭环测试中的一次Builder→Work完成通知。
- 通知成功只是工具确认已发送，不能直接证明Work已接收/验收；单轮实测也不证明长期可靠率。
- 消息到达时Builder可能还在保存通知结果；Work应依据该次结果或有限最新turn核验稳定交付，不为读取未完成文件无限轮询。

完成消息到达后的通知账本收尾：若第一次读取仍为PREPARED，先记录该真实快照。Work可新签一个仅验收的补充范围：对同一已发送通知的Builder turn有界等待完成一次（上限50秒）并追加读取通知账本一次；不得循环、重派、重发或启用定时器。该等待发生在消息已触发Work之后，不承担唤醒责任。若仍未收尾，保留REVIEW_PENDING/UNKNOWN，结束本轮，不能自称完整验收。2026-10-06首轮实测已观察此竞态，追加核验后确认通知SENT_TOOL_CONFIRMED及Builder完成。


## 保留边界与当前实质工作状态

全部dirty/untracked/index原位保留；禁reset/stash/clean、清node_modules、未经准确授权的Git写。禁止Zotero仓、Project sources写、deep-learning-hank、跨树索引、旧STOP/耗尽预算重置；不派新助手或新执行会话。
五False及Results FALSE、C9 PAUSED、Objective A 16UNRESOLVED、window UNACCEPTED、CALL_LEDGER_UNRESOLVED保持。流程消息测试不授模型/consumer、真实科学解析、科学定义、保护变化或发布。
当前C8已接受31份未认证checkpoint元信息观察；历史writer版本、实际阶段和准确历史证据仍缺失。该实质链保持MISSING_HISTORICAL_EVIDENCE，不以流程测试解除。

## 本次闭环测试与验收停点

测试ID：STAGE_CH5_MESSAGE_TRIGGERED_LOOP_TEST_20261006；版本delivery-1；关联码CH5_MSG_LOOP_20261006_V1。
任务单另存docs/CH5_MESSAGE_LOOP_TEST_PROMPT_20261006.md。测试只读取本工作流及任务单、写最小回执和通知账本、发一次完成消息；源码/科学产物/Git/模型/测试运行0，不制造新的科学报告。
Work发单后结束本轮，不主动轮询Builder。Builder完成消息实际触发Work新一轮，且Work独立记录接收/审查/裁决，方可称本轮消息闭环PASS。测试报告或发送成功本身不是PASS。
本测试完成后停止，不签科学/实质后继，定时automation保持PAUSED。若回报消息未触发Work，不静默启用定时器；保留结果，由Owner或明确人工接续核验。
