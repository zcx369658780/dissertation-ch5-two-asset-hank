# Chapter 5 当前交接 — wage-conditional `(ra,w)` health-region / provincial mapping audit candidate

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

Baseline：`44df9bb331770a930d8ff465c23d59d6fe5cb65a`。

Branch：`codex/ch5-mp4c-k1-ra-w-health-region-mapping-audit-20260913`。

Worktree：`D:\ProjectTemp\ch5-mp4c-k1-ra-w-health-region-provincial-mapping-audit-20260913-001`。

状态：`WAGE_IDENTITY_ALIGNED__ALL_ACCEPTED_PROVINCIAL_POINTS_OUTSIDE_STANDALONE_WAGE_COVERAGE__TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。

Exact Builder task 已完成，active Builder task=`NONE`；未发布 successor task。Results eligibility=`FALSE`。

报告：`docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_REPORT.md`。

Compact evidence：`docs/evidence/ch5_mp4c_k1_ra_w_health_region_provincial_mapping/`。

Wage semantic gate：`WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`。Standalone `w` 和省级 HJB consumed composite `results.w` 均进入 `HouseholdInputs.wages[0]`；guarded `wjt` 是不同的上游 firm object，经 `wage_caculate` / `composite_household_wages` 聚合后才成为 household wage。Source 未定义 `results.w` 到 HJB input 的额外 unit conversion/normalization。

Observed map：accepted 27 点；interior=4、ambiguous=7、lower=7、upper=8、KFE pathological=1。`(.06,.8)` 保留 severe signed KFE pathology，绝非 healthy/admissible point。

Provincial projection：accepted 62/62 exact input rows；turn1 `20/31` converged，turn2 `2/31` converged；两轮各 31/31 都是 `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`，因为省级 consumed composite wage=`12.8426–18.5197`，standalone 只观察 `.8/1.05/1.3`。20/20 turn1-converged→turn2-failed 省份的 consumed `ra` 上升且 wage 下降，但只能作 descriptive association，不能判为跨越 observed unhealthy frontier。

Guard：turn2 return upper guard `18/31`；29 个 failures 中 upper=16、unsaturated=13，两项 converged 也均 upper。Wage guard 也不唯一分离 outcome。Accepted compact evidence未提供每行 raw `wt0`，未猜测或重构。

Scientific runtime：HJB=0、KFE=0、outer=0、MATLAB=0、firm=0、K1B/K2=0、GE/downstream/shock/IRF/Results=0。

唯一当前 gate：ChatGPT Reviewer 对 candidate 独立 ACCEPT/REJECT。

唯一建议但未授权、未执行、未发布的下一 Owner gate：`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。

不要 merge main。
