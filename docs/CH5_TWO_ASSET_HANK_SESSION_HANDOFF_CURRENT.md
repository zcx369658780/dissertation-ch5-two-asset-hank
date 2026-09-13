# Chapter 5 当前交接 — k-unit normalization / asset-domain design audit candidate

更新：2026-09-14。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

Baseline：`d7d6d4718d27abe33a8915fd2b07ac042a125783`（fresh-fetched `origin/main`）。

Branch：`codex/ch5-mp4c-k1-k-unit-asset-domain-design-audit-20260914`。

Worktree：`D:\ProjectTemp\ch5-mp4c-k1-k-unit-asset-domain-design-audit-20260914-001`。

状态：`MACRO_K_UNIT_REBASE_COHERENT__HOUSEHOLD_MONETARY_BRIDGE_UNPROVEN__BMAX_OWNER_SELECTION_REQUIRED`。

Exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_REPORT.md`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_k_unit_normalization_asset_domain_design/`，manifest seals 10 payload files。

Macro unit result：current aggregate monetary unit `MU=100k` rebase 到 total k 时 aggregate money `×100`；current `NU=100 persons` rebase 到 persons 时 quantity `×100`。因此 `GDP_multiplier 1000→100000`、`POP_multiplier 100→10000`，而 `Y/N`、`K/N`、`Z`、raw firm wage 与 rates 数值不变。

Household bridge：source 未证明 `w/C/Tt/a/b/At/Bt` 已经是 k/person(/period)。不得为对齐 GDP、`wjt=1.3` 与 composite wage 13–18 而人为乘 10/1000/10000。结论：`MONETARY_UNIT_BRIDGE_UNPROVEN`。

Domain result：`amax=100` 是 conditional individual illiquid state-grid upper bound，不是 `At=100`。`bmax` bounded candidates=`{20,50}`，Owner 必须选择；`bmin=-2` 仅 first diagnostic 暂留。I=J=20 时 `da=5.2631578947`；`db=1.1578947368` 或 `2.7368421053`。20×20 仅适合第一轮 domain diagnostic，production 前必须 precision sensitivity。

Scientific runtime：HJB/KFE/global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results 全部 0；scientific retries=0；parameter/grid/model-source changes=0；deterministic offline audit builds=1。

唯一下一 Owner gate：`OWNER_REVIEW_HOUSEHOLD_K_UNIT_BRIDGE_AND_BMAX_SELECTION`。在此之前由 ChatGPT Reviewer 独立 ACCEPT/REJECT candidate；不要 merge main，不要发布 successor task。
