# CH5 Owner 2026-10-18：TEMP独立2×2价格桥100轮科学对照授权

**Owner直接决定：**“我同意下一轮在独立 TEMP 版本中研究这两种价格桥的对照，而正式 V010 继续保持冻结。其实100轮已经足够了，至少是否收敛已经可以判断出来了。请继续下达任务单。”

**新临时版正式任务：`TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_ROUND_LONG_TASK`。**
- 独立实验branch：`experiment/ch5-temp-price-bridge-factorial-100-20261018`
- 实验任务发行固定Commit：`2c855f616efbca05c29d4069a44e3c6651070b44`
- 实验任务不可变Git Blob：`4e81556bff068b9bedc6c7c608faf24ee1e439fe`
- 实验合同：[EXPERIMENT_CONTRACT.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/2c855f616efbca05c29d4069a44e3c6651070b44/experiments/TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_20261018/EXPERIMENT_CONTRACT.md)
- 以原TEMP已冻结任务Commit `503b418f790d61049f3df9016a783dcecc793237`为唯一源码/任务父，实际Git源继承历史2009已验收`216283cf4f1303afa60f1915e143a0b7303a9ffb`。
- 核心HA`exports/matlab_faithful_two_asset_ha.py`：原SHA256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`，**黑箱一字不可修改**；2009/postloop adapter、冻结V010模型、synthetic fixture亦只读。
- 原100轮A0为实际已验收RAW ra0+RAW wt0基准，**只读复用，不重复运行**；A1：used ra + raw wage；A2：raw ra + clipped wage；A3：used ra + clipped wage。新实验启动仅三ARM，各从原冻结fixture第一轮的相同参数起跑，100轮是**硬上限**，更早满足原source稳态条件可早停。不从旧A0第100轮热启动，不授权500轮、续跑或重复baseline。
- **算术干预范围**只改变进入HA之前的`rah_i=Σ_j S[j,i]return_j`与下一轮`w_eff`工资来源；`S`的lagged zscore继续使用原raw ra0且企业资本数量、govinv/Zt/财政/税楔/相同输入均不修改。特别必须绕开`prepare_mainline_household_states`无条件用raw重新覆盖`rah`的陷阱，在**实际进入HA前**独立核对数值/来源。目的地税只扣一次，家庭tau=0等价参数，经济混合规则只有TEMP探索资格。
- **新冻结预算**：三独立science drivers≤3，每ARM≤2省×100轮HA，任务总≤600 HA，工程Python≤24（focused pytest≤8），wall≤24小时、artifact≤512MiB，停止/异常真实扣费。所有旧TEMP/M1/F25 science额度已STOP，不结转；未完成ARM不换名重跑。结果只允许`SOURCE_CONVERGED_BY_100`、`NOT_CONVERGED_WITHIN_100`、真实early fail/resource stop；不得扩大“100轮内未收敛”为任何将来都无解。
- **交付**：Owner 2026-10-18批准的[MD+sanitized ZIP 临时交换协议](CH5_OWNER_REVIEW_MD_ZIP_TEMP_EXCHANGE_POLICY_20261018.md)，remote-only review ref `review/ch5-temp-pricebridge-factorial100-20261018`、目录`_review_tmp/ch5/temp-v010-pricebridge-2x2-100-20261018/`仅`result.md`、`manifest.json`、`evidence_sanitized.zip`，唯一review parent为上面发行Commit，1次普通non-force push；原RAW本地私有保存。Astra完成独立验收和治理主审回读后才能限域清理远端临时文件。Git删除不擦历史，上传前必须递归检查脱敏与内容。
- 所有正式V010权限仍`ACTIVE_TASK=NONE`，原冻结科学Plan/九月数值方法决定完全不改；`model_activation=False`、`REAL_GE=False`、`Results FALSE`、`V011 NOT_STARTED`；临时对照不代表已采纳新的价格体系或学位论文实证通过。原8dirty/index/external common-dir、原M1/F25/TEMP100证据、C盘独立SSD备份及2009/真实C8/2017/2018/B3/V009资产保护继续。

**交接优先级：** TEMP执行权在精确实验branch的发行合同，不得从历史TEMP根`CURRENT/TASK_CURRENT`或正式治理`ACTIVE_TASK=NONE`猜测已执行/停机许可。Codex只读合同后执行一张长任务，E1工程自修复，不每轮问Owner/Astra；到原source收敛或100轮/科学硬STOP后才集中交付。