# Chapter 5 当前规则入口
更新：2026-09-15；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_RECEIPT_REPAIR_AND_REEXECUTION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_PRECISION_ESCALATION_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_FREEZE_CURRENT.md`
9. active exact task：`tasks/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC.md`

当前状态：`J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC.md`。
最新 accepted finer-precision candidate：`e3db1ada75619a7db0139cef0da4aaabbb351690`。
Results eligibility=`FALSE`。

Accepted representative diagnostic state：`rb=.02,ra=.0675,w=15.5,a=[0,100],b=[-2,20],h=1,I=20`。HJB/KFE equations、FOC、selector、boundary、derivative floor、solver、tolerance、maxit=100、wage/return mappings、guards 与经济参数冻结。

Accepted finer-precision evidence：J320 HJB/KFE valid；J640 HJB 在 maxit=100 后未收敛但无 illegal/hard/nonfinite failure；KFE 未运行；J1280 未启动。该结果只支持 numerical nonconvergence，不支持 domain/scale pathology，也不支持 stabilized J。

当前 exact task 仅允许 identical-input J640 HJB diagnostic replay exactly once，fresh initialization、maxit100、tolerance unchanged，只增加 task-owned observation。目标是区分 slow/near-monotone convergence、policy/selector chatter、value oscillation、derivative-floor amplification、low-period cycle 或 unresolved mechanism。

禁止增加 maxit、damping/relaxation、修改 tolerance/HJB/KFE science、运行 KFE/J1280/J>1280、liquid-I ladder、domain change、recalibration、global model 或 Results。

Owner 已授权 ChatGPT Reviewer 对类似局部数值调试直接做 bounded、预注册决策并发布 exact task；结构方程、accepted equations/guards、主要经济校准、因果解释、Results eligibility 的变更仍由 Owner 决定。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
