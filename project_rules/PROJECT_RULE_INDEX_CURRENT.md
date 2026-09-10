# Chapter 5 当前规则入口
更新：2026-09-10；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. 若存在active task，再读取该exact task及直接相关acceptance/report。

当前状态：`FIRM_PRICE_NORMALIZATION_FORENSIC_ACCEPTED__WAGE_UNIT_MISMATCH_AND_RETURN_LEVEL_EFFECTS_SEPARATED__BOUNDED_TRAJECTORY_DIAGNOSTIC_AUTHORIZED`。
当前 active Builder task：`tasks/CH5_MP4C_CORRECTED_2018_SOURCE_FAITHFUL_100_TURN_BOUNDARY_TRAJECTORY_DIAGNOSTIC.md`。
最新接受候选：`770cb06b49a8ede720fdec4bbf6450c1552a4902`。
Reviewer acceptance：`docs/CH5_MP4C_FIRM_PRICE_NORMALIZATION_AND_HOUSEHOLD_MACRO_BRIDGE_FORENSIC_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

最新firm-price forensic已接受：在当前统一宏观单位和corrected 2018 Track-A对象下，firm wage边界命中主要是未闭合的firm/household wage numeraire问题；`w_raw=.92*(1-alpha)*Y/L`，legacy `[.8,1.3]`不能直接当作当前MU/NU下的经济工资区间。firm return边界命中主要来自真实`Y/K`水平相对历史数值 safeguard 偏高；初始化下`ra_raw=.7240464015119004*(Y/K)-.025`，对Y、K共同货币缩放不变，因此不能靠共同货币单位重标度消除。household `a/b`绝对货币归一化和`At_grid -> At*N`中的`beta_a`仍未识别；不得用收敛结果反推。

Owner已进一步明确历史MATLAB求稳态原则：迭代途中大量边界命中本身不是失败，只要边界命中数随循环下降并最终退出边界、满足稳态要求即可。历史`ra`范围主要是HJB/数值安全区，最终稳态仍要求无`ra`边界命中。基于这一科学裁决，下一门只允许一个source-faithful corrected-2018 bounded trajectory，最多100个outer turns，逐轮记录ra/wjt边界命中数量、省份身份、KN/Y/GDP gaps、GovInv/Zt action与household/KFE有效性；不得看到轨迹后调参或运行第二个参数cell。

该trajectory baseline冻结为：correct 2018 GDP/POP、raw-NBS GFCF Track-A PIM、`delta_pim=.096`、`alpha=.7380939146868483`、`MU=10万元`、`NU=100 persons`、source-faithful `beta_a=1`仅作diagnostic、source-lagged rah、`lambda_w=lambda_rah=1`、无新增hysteresis/GovInv damping、原price bounds不变、无KFE/HJB repair。即使outer path改善，Results仍不可用，KFE/HJB独立科学门继续有效。

此前raw-NBS重估、mixed-year数据审计、steady-state redesign spec、initialization probe和five-turn KFE attribution均继续作为有效历史证据。

GitHub live main是repository-state authority；聊天不能替代exact task。任何新的科学执行必须先发布exact task。以后每次发布exact task，同一回复自动附Codex启动prompt。