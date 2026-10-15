# V010 原MATLAB主线SOURCE_ONLY方案的独立限定接受（2026-10-15）

状态：`ACCEPT_SOURCE_ONLY_PROPOSAL__NOT_IMPLEMENTATION_OR_SCIENTIFIC_ACCEPTANCE`。

Codex报告 `V010_MATLAB_MAINLINE_BASELINE_AND_MINIMAL_REPAIR_PROPOSAL` 后，Astra在新会话独立读取固定发布任务 `0320916bd2447d1846099cc90e52bd92c920ebb1`（blob `d4aacdafe5f4d0248745f8754088afd83fc1c6d2`）、推荐基线 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`（tree `4a118642da526d6bf2dfb65a1130f4d59d371374`）、`one_turn.py`、`stationary_runtime.py`、`steady_state.py`、`firm.py`、`wage.py`、`migration_labor.py`、`capital_allocation.py`、`capital_network.py`、corrected聚合器及接受的HJB/KFE关键入口，并对Owner原MATLAB .m和博士论文5.2.7/5.3作有限核对。

独立支持：旧Python确实保留顺序one-turn/manual outer外壳，但默认仍调用遗漏home-capital的旧分配器、错误`Lt_prev`覆盖、原工资税混轴/可能双扣及旧HJB单一value退出和污染行KFE；K1 same-S 和corrected完整HJB双门、source-free KFE、单调性halving存在于分离已接受模块，尚未成为可直接通用的完整HA主线。原MATLAB`GovInv`更新与C1为不同映射，Owner已在随后明确选择原0.9/1.1方案。原冲击入口传入`1`，沿历史MATLAB实际选择lagged-NKPC分支。

Codex报告的本机39份对象、7治理文件、读量、6.2min、source_ledger及零科学调用/原8 dirty保护**属于CODEX_REPORTED_WITH_LOCAL_RECEIPTS**，并无Astra对Windows日志/dirty字节独立证明。GovInv/TAX及新科学决定见`prefreeze_scientific_review_20261015.md`。

接受仅为`AUXILIARY_RESEARCH_NOT_MAINLINE`与MATLAB-first源接续和最小修错方案的科学规划资格；不自动使推荐code基线科学合格、不验收31省稳态/IRF，不把旧V009私人资本零支持当原有界方法无稳态的证据。此报告用于冻结同一V010实施合同，不再增SOURCE_ONLY微版。
