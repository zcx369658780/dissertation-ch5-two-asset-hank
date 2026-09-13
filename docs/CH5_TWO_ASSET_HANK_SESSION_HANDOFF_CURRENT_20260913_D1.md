# Chapter 5 当前交接 — 2026-09-13 D1 acceptance

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 角色与 authority
Owner = 最终 scientific authority。ChatGPT = L3 independent reviewer / scientific-route authority / GitHub exact-task issuer / acceptance-gate reviewer。Codex = bounded Builder/executor。GitHub live `main` 是唯一 repository-state authority；聊天摘要不能替代 live task/status authority。

## 新会话恢复顺序
1. fresh-fetch live `origin/main`，不要把本文件中的 SHA 当作永远最新；
2. 读 `AGENTS.md`；
3. 读 `project_rules/PROJECT_RULE_INDEX_CURRENT.md`；
4. 读 `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`；
5. 读本交接；
6. 读 D1 freeze、raw-census acceptance、D1 runtime acceptance/report；
7. 在 Owner/Reviewer 对下一 HA/HJB numerical contract 达成决定前，不发布 successor runtime task。

## 当前 accepted state
最新 accepted D1 candidate：`c7d29f5bc0751751f1547072eac79eff916a8240`。
Reviewer acceptance：`docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Results eligibility=`FALSE`。

## D1 frozen contract
D1 是 temporary numerical continuation safeguard，不是结构经济约束。对称区间 `[-1e5,+1e5]`，inclusive：`abs(d_raw)<=1e5` admissible；超界 raw branch 只在 raw FOC candidate 已生成并保存之后被排除出 selector competition。禁止 clipping / manufactured endpoint。existing zero-transfer option 和其他 admissible branches继续按 accepted selector law工作。D1 implementation 默认 OFF 时必须 exact parity。

## D1 bounded runtime accepted findings
比较 fresh G2 control 与 fresh G2+D1，两边 turn1 exact equal；turn2 common-entering-state gate PASS。D1 turns2-5 检查 `39,440,000` 个 active raw branches，拒绝 `15,330` (`0.0388692%`)；形成 `3,459` 个 iteration-cell winner changes，其中 `2,156` fallback 到 existing zero，`1,303` switch 到其他 admissible nonzero。最终 HJB iteration 的 `99,200` cells 中只有 `21` 个 final selected controls不同。

D1 强烈压低 far-tail stress：selected `|d|` max 约 `4.27e7 -> 9.99e4`，adjustment-cost max 约 `1.92e14 -> 3.79e9`，`mu_a/mu_b` extrema 同数量级收缩。但 HJB convergence 没改善：turns2-5 control `6/124`，D1 `5/124`；all-turn `26/155` vs `25/155`；D1多用87次 HJB iterations。Turn2 same-state convergence仍 `2/31` vs `2/31`。

因此 D1 证明 transfer-candidate explosive tail 是重要 numerical-stress amplifier，但**不是当前 HJB convergence failure 的充分/主导解释**。目前不支持 longer D1，也没有正面证据支持 D2/D3/OFF。

## Price guards
Return/wage safeguards仍大量 binding。G2 return turns2-5 upper/unsaturated省数为 `18/13`, `22/9`, `22/9`, `22/9`。Wage turns1-4为 lower/upper/unsaturated=`4/24/3`；turn5 control=`13/12/6`、D1=`14/12/5`。长期目标仍是 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`，最终科学结果也不得依赖 binding D1。

## Scientific contracts仍冻结
`MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`；`rho=.05/year`、`rb=.02/year`、borrowing gap `.07/year`、firm/HJB `delta=.10/year`、`Q_z=1/3/year`、`chi0=.1`、`chi1=2 years`。K1A fixed theta、`beta_distance=2`、`beta_return=0`、same-S quantity/payoff、source-faithful labor、C1 unchanged。不得自动改 derivative floor、transfer FOC、return/wage guards、boundary/KKT law、grid/tolerance/solver。

## Capital-network / KFE boundaries
K1 bilateral capital network 与 annual time-base 已 accepted；K1B `beta_return=.5`仍只 preregistered，未授权 runtime；K2未授权。KFE仍 `DIAGNOSTIC_ONLY`，finite-box upper-b leakage 与 MATLAB-style pinning 是独立 blocker。Standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

## 下一 scientific gate
`OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`。

D1 已把 transfer tail 切掉但 convergence 不改善，因此不要继续靠扩大/收紧 D 自动试错。下一会话先讨论剩余 HA/HJB blocker 的隔离顺序。可讨论的候选 family：
- return/price-interface calibration 与 guard dependence；
- wage-interface calibration / wage safeguard；
- value-derivative / derivative-safeguard 数值合同；
- HJB iteration / solution method diagnostic（不先调经济参数）；
- boundary/selector authority 仅在证据指向时再开。

Reviewer当前倾向：先做**无科学参数变化的 HJB convergence-mechanism review/design**，明确为什么 transfer far-tail被切掉后仍 `~95%` calls 不收敛；但这是新会话需要与 Owner 再确认的 substantive route，不在本交接中自动发布 exact task。

## Workflow硬规则
不得 force push/reset/clean/stash。不得为 PASS 调 solver/parameter/tolerance。正式发布 exact task 时同一 ChatGPT 回复必须附完整 Codex startup prompt。Results eligibility保持 `FALSE`，直到独立 Results gate。
