# Chapter 5 两资产 HANK 当前状态
更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_TRANSFER_RAW_CANDIDATE_CENSUS_ACCEPTED__OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE_REQUIRED`。

最新 accepted raw-census candidate：`e6c71240e945c988958a16c67886b056376a2da4`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`。
Owner transfer-control safeguard policy freeze：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`。
当前 active Builder task：NONE。
Results eligibility=`FALSE`。

## 已接受：exact raw transfer-candidate census
在 frozen annual G1/G2 science 下，observation-only census完成 G1/G2 各5 turns，310 HJB、310 KFE、27,196 HJB iterations，零 scientific/runtime retry。Instrumentation ON/OFF scientific parity通过；transfer safeguard未实现。

Exact census包含 `87,027,200` 个 raw branch-cell candidates，全部 finite。旧 instrumented evidence 的 `108,784` 个 raw arrays与 `652,704/652,704` 个 min/median/p95/p99/max/hash 字段全部 exact reconcile。

Pooled raw `abs(d)`：median=`2.75556`，p99=`2,888.04`，p99.9=`58,175.12`，p99.99=`1,015,033.53`；极值约 `-2.785e9` 至 `+1.715e12`。尾部在 `1e2–1e8` diagnostic grid 上连续存在。唯一巨大 adjacent top-gap 只隔离两个 positive outliers，不具备 branch/path/turn2 robustness，因此 data 不识别唯一 operational cutoff。

Accepted exact raw exceedance shares：`|d|>1e3`=`2.145776%`，`>1e4`=`0.398441%`，`>1e5`=`0.064336%`，`>1e6`=`0.010142%`。这些仍是 diagnostic sensitivity evidence，不是 frozen safeguard stages。

## Safeguard semantics
当前首选 future semantic contract 仍为：

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`

即保留 raw FOC receipt；未来若 raw branch 被判 inadmissible，则该 branch 不参与 selector competition，同时保留既有 zero-transfer option 与其他 admissible branches。Candidate clipping 仍不推荐。当前未冻结任何 numeric `d` interval，也未授权 runtime。

## 当前 Owner gate
唯一下一门为：`OWNER_NUMERIC_TRANSFER_SAFEGUARD_FREEZE`。

Owner 需选择第一套 temporary transfer-control admissibility interval/ladder，以及 symmetric/asymmetric 形式。现有 census 支持多个 continuation options，但不会从数据唯一推出一个 cutoff。

`chi0=.1`、`chi1=2 years`、derivative floor、transfer FOC、selector/boundary law、G1/G2 return guards、`wjt [.8,1.3]`、annual calibration、grid、tolerance、solver、K1/C1、source-faithful labor全部保持不变。

不得 longer G2、G3/G4、wage relaxation、K1B/K2、GE/IRF/Results。KFE仍为`DIAGNOSTIC_ONLY`；finite-box upper-b leakage与MATLAB-style pinning独立未解决。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。
