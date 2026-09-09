# Chapter 5 当前交接
更新：2026-09-10。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner为最终科学authority；ChatGPT为L3 Reviewer/科学路线authority/GitHub exact-task issuer/acceptance-gate reviewer；Codex为bounded Builder，默认`gpt-5.6-sol / medium`。GitHub live main是唯一repository-state authority；聊天不替代task authority。

## 新会话恢复顺序
1. fresh-fetch live `origin/main`，不要复用交接SHA当作最新值；
2. 读取 `AGENTS.md`；
3. 读取 `project_rules/PROJECT_RULE_INDEX_CURRENT.md`；
4. 读取 `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`；
5. 读取当前 active exact task；
6. 再读取相关 predecessor acceptance/report。

## 当前 live 状态
交接准备时 active task：`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。
状态标记：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_LEAKAGE_ATTRIBUTION_ACTIVE`。
最新接受科学候选：`9864129dd2e97bae97238ab9cc588aea48682d29`。
Results eligibility=FALSE。

## 2018 canonical 输入
本地私有 canonical workbook：`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`；SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。GitHub不保存私有xlsx本体。
安徽2018 final-use：GDP `34010.9`亿元；POP `6076`万人；PIM `K2018=1357314108.2013683`万元；alpha=`.772866243094144`；PLM vintage19/window2009–2018；same-year Zt约`.0006934644495858679`。时间合同仍为rolling-10y/same-year-Zt；PIM `K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`。

## corrected-2018 已接受轨迹
- turn1：安徽 household `rah=.09`；firm raw `ra0=-.02496997113112164`，used `ra=.02`；raw wage `2.5721358283733027`，used `1.3`。
- turn2：安徽 `rah=.0829892058879816`；raw `ra0=-.024968505109415375`；used `ra=.02`；`nk_gap=.34756612158493083`。
- turn3：直接corrected-rate传播已观测。安徽 `rah=.0184420457528848`，由 turn2 entering firm-`ra` vector生成；source vector 31/31均`.02`，不是残留`.09`。安徽 A/B/A+B从turn2 `7.2930/4.6852/11.9783`跳到turn3 `.01329/1.8787/1.89196`。
- five-turn：完整5 turns / 155 updates，0 scientific retries；turn4首次 adaptation gate开启，turn4/5均执行31省Zt adjustment与`LOW_RA_DECREASE_0P9` GovInv action。

## five-turn 已接受 blocker
Reviewer接受：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_SOURCE_FREE_STATIONARITY_AND_UPPER_B_LEAKAGE_BLOCK_PREFIX_INTERPRETATION`。
turn4/5全31省 returned densities均`DIAGNOSTIC_ONLY`。近机器精度negative mass不是主因；实质问题是source-free stationarity residual与upper-b boundary leakage。每轮全国620个positive upper-b leak cells，max leak rate约2.2393；其余三face outward leak为0。因而five-turn C/L/A/B不能作为accepted economic moments。

## 当前正在执行的任务
`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`
这是zero-science-call post-processing attribution。只读取已保存operator/density/drift；scientific processes/trajectory/household/HJB/KFE/solves/firm/controller/MATLAB/GE/annual/IRF/Results全部必须为0。
中心问题：是否确认与已接受 call725 `rah=.07` 相同的 finite-box upper-b leakage + row-replacement/pinning implicit-source algebra；并量化turn4/5全国pin-row residual、escape flow、mass-balance identity及implicit-source equivalence。

## 当前禁止
禁止turn6+、new KFE solve、steady state、GE、annual、IRF、Results；禁止production boundary/grid/source/pinning repair；禁止为了补artifact重跑科学模型。D1–D3仍是deferred redesign proposals。

## 下次验收后的路线
下次会话先验收当前 attribution 候选：
- 若 `FIVE_TURN_KFE_ATTRIBUTION_PASS__SAME_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`：接受机制证据后，下一步需要Owner科学决策是否进入 boundary/finite-box closure redesign；不得直接续跑turn或steady state。
- 若 PARTIAL/DISTINCT：先定位additional residual source。
- 若 BLOCKED：只接受evidence gap，不为补证据自动科学重跑。

用户已要求：下次当前任务验收后，立即生成完整会话交接prompt；以后每次正式发布exact task时，同一回复自动附Codex启动prompt。