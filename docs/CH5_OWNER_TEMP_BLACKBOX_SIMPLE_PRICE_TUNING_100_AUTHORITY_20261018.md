# Owner新方向与冻结任务：TEMP HA黑箱＋简化观察门＋价格调参（2026-10-18）

Owner在本会话完成交接后明确：“可以，让我们继续TEMP的方向（HA黑箱+约束条件简单化 的调参）”。

此为新的TEMP方向授权。顾问据此将本轮具体科学/工程范围和新预算冻结在[唯一新长任务](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/6d07cdf1a565376927bd64997780ad77669d9390/experiments/TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018/EXPERIMENT_CONTRACT.md)；具体三臂、顺序、预算值为顾问本次实施设计，不冒称Owner逐项报出了数字。旧交接的WAIT_OWNER已完成其等待目的，不能再用其历史NONE阻止本次新合同；也不能把本次授权倒推到旧任务。

## 唯一任务身份及状态

- TASK_ID：TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018
- 发行分支：experiment/ch5-temp-blackbox-simple-price-100-20261018
- 发行Commit：6d07cdf1a565376927bd64997780ad77669d9390
- 发行Tree：628677d32b773d7fd8cb9a4e9f906979d17067b5
- 任务路径：experiments/TEMP_V010_HA_BLACKBOX_SIMPLE_PRICE_TUNING_100_20261018/EXPERIMENT_CONTRACT.md
- 任务Blob：04af299d04f1e37243d8af806fb4a4e10eed0feb
- 任务原字节SHA256：2e6fc6e118c3c4bd71d4380a0d6f070d5fe2839ed4dffbaf13ae123bf9da9dc3；长度25559B。
- 唯一父：2c855f616efbca05c29d4069a44e3c6651070b44。远端compare确认1 ahead/0 behind，仅新增这一份194行合同，源模型0变更。
- 状态：ISSUED_NOT_STARTED。本轮顾问未在Windows或本环境运行任何模型；P0通过后方可由本地Codex在同一冻结任务内进入科学，无中间微审批。
- 当前唯一ACTIVE_TASK/RESEARCH_ACTIVE_TASK为上述TEMP任务；TASK_SCOPE=TEMP_SYNTHETIC_ONLY；FORMAL_V010_ACTIVE_TASK=NONE。
- 没有另行交付补救任务；DELIVERY为本长任务内已预授权的独立预算域。
- 新review分支review/ch5-temp-blackbox-price-tuning-100-20261018在签发前404；尚无结果上传或工程PASS。

## 科学范围：两因素调参，不改HA内部

A0复用旧100轮；A1家庭used ra/raw wt0，A2 raw ra0/clipped wjt，A3 used ra/clipped wjt。单science driver固定A1→A2→A3，各自同一初始fixture起步、每组最多100轮/200次HA，全局最多600次新计费HA。tKN/Y_previous等全部外围状态也逐臂重置，只有资源账共享。

HA固定216283cf4f1303afa60f1915e143a0b7303a9ffb的exports/matlab_faithful_two_asset_ha.py，Blob9e7dc9556a2b76811e78f89999abecc045886106、SHA256 B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3。原adapter、网格、初始化、FOC、HJB/KFE、阈值与真实converged标记不改；CP2_F25不续修。

第1轮输入同A0，第2轮起选择两条价桥；S始终来自前一完整轮raw ra0且数量收益同S，真实pre-HA核验防止旧prepare覆盖rah。其他经济通道、税/人口/GovInv/Zt/边界/松弛率和初值不变。该调参是已有两个价格开关的有限比较，不扩展为未知参数优化。

TEMP原HA正常返回但converged=False可继续外层，Bellman/KKT/KFE尾数和工资触界只观察。旧TEMP已经如此，不把本次包装为新取消Bellman。源式收敛仍需两省原HA True、KN与Y gap均<1e-9且ra严格内点；数据有限合法只是允许观察，不代称收敛。正式V010 Bellman/HJB合同不受影响。

## 一张任务内的工程前置与交付

P0集中验证：单写append/checkpoint、不可变快照供外部监视、唯一临时名、真实故障进程内全STOP、短寿命子进程累计计费、同一publisher的无网络fake-bare二进制ZIP往返及价格stub。E1在白名单内有预算自主修复，P0通过后自动开始三臂；共同E2/E3立即科学STOP。串行化不被宣传为已证明旧Windows根因。

新工程进程含后代≤192，唯一HA driver≤1，交付进程含后代≤192，全局≤385；按用途域互斥记账。失败bootstrap至多3次尝试，成功进入HA的唯一driver归SCIENCE，其余无HA失败归ENGINEERING，不能重复计或再起第二个science。P0发布器预演与全部Git/SSH也扣DELIVERY预算。时间工程≤3h、科学≤18h、交付≤3h，总任务≤24h；科学到界真实部分交付，不保证三个100轮都完成。旧预算不继承。

Codex自动向新review固定目录提交result.md、manifest.json、evidence_sanitized.zip三件。唯一parent是本次发行Commit，manifest必须写本次ref/parent，不能复用旧元数据。所有RAW/派生分级，先验收永久归档再由Astra清远端临时三件。

发布前ZIP无法包含之后push/readback的最终计数：新合同已要求区分prepublication计数，并在最终回复提供≤8KiB最终资源回执原字节Base64/长度/SHA256，不增加第二次成功发布。Astra能复算文件字节不等于已独立认证Windows OS事实；原件未收到则保持CODEX_REPORTED。

## 历史与正式状态保持

[完整旧交接](CH5_SESSION_HANDOFF_20261018_AFTER_TEMP_HA_PRICE_BRIDGE_AND_GITHUB_ZIP_CLOSEOUT.md)及各独立终审保留：旧100轮未收敛；旧2×2共享账本E2、0/2/2轮、12HA；旧ZIP传输字节成立但至少26/24仍本机报告级、工程FAIL_CLOSED_RESOURCE_EXCEPTION；旧三件清理f72a2a7f24313e2272de083d2eedf4645aef1c61已完成。全部旧预算CLOSED_NO_CARRY_FORWARD，不重传、不复清、不回填失败。

正式研究版本V010/v0.0.10，FORMAL_V010_ACTIVE_TASK=NONE，V011 NOT_STARTED，model_activation=False、REAL_GE=False、Results FALSE，FULL_RUNNER_IO_CLOSURE=BLOCKED。新TEMP即使某臂收敛也只获得有限探索结果，正式方法采纳仍须Owner另行决定。

执行结束唯一停点：WAIT_ASTRA_TEMP_BLACKBOX_PRICE_TUNING_100_REVIEW。
