# TASK_CURRENT：V010 corrected HA历史价格单点新科学授权

日期：2026-10-15（Asia/Shanghai）。
**ACTIVE_TASK=V010_CORRECTED_HA_SINGLE_PRICE_POINT_ONE_ATTEMPT**。
**PERMISSION=OWNER_EXPLICIT_SINGLE_ATTEMPT_SYNTHETIC_HA_SCIENCE_AUTHORIZED__NO_MACRO_OR_REAL_DATA**。

唯一任务：[corrected_ha_price_probe_task_20261015.md](versions/0.0.10/corrected_ha_price_probe_task_20261015.md)，由本发布提交固定。对应科学freeze `corrected_ha_price_probe_freeze_20261015.md` @ commit `81181490495f827aa0e15e6a6efb186e8addee67` / tree `846fd3f354d8f9d5d4978e15ad9ff78b71d2e451` / blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`；独立输入manifest `corrected_ha_price_probe_v1.json` @同一提交 / blob `c23d331bed34e5ca478324cdc05034609ecb91b7`。唯一代码候选 `94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`。

仅1次corrected HA，`rah=.0675,w_eff=15.5,rb=.02`及其全部冻结Tt/rb_gap/网格/参数；最多1科学进程，0 pytest，0宏观/IRF，严格原HJB/KFE及root/selector总门；不修源、不重跑已存失败点。任务从未用到1个科学尝试开始计算，任何科学调用后不得重新初始化用以第二次。最终`V010_SINGLE_POINT_CORRECTED_HA_PRICE_PROBE_RESULT` / `WAIT_ASTRA_V010_SINGLE_POINT_PRICE_PROBE_REVIEW / STOP`。

旧V010计划、原两省fixture、原8 dirty/common-dir与已消费科学账不动。旧C8/B3/2017/2018真实数据0；A16/window/C9/CALL_LEDGER保护不变；Results FALSE，V011 NOT_STARTED。
