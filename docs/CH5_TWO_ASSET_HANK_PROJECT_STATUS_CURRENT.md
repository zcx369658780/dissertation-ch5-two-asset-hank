# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`CORRECTED_2018_TWO_TURN_ACCEPTED__TURN2_PROPAGATION_PASS__TURN3_DIRECT_RATE_TRANSMISSION_ACTIVE`。
最新接受候选：`406d4132836e08d30b42b41e09f8237e6aac66a9`。报告：`docs/CH5_MP4C_2018_CORRECTED_INPUT_TWO_TURN_PROPAGATION_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 2018数据层
2018 canonical 数据层继续冻结并已闭合。canonical workbook：`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。安徽final-use：GDP 34010.9亿元，POP 6076万人，PIM K2018=1357314108.2013683万元，PLM vintage19/window2009–2018，alpha=.772866243094144，same-year Zt≈.0006934644495858679。

## 已接受 corrected-2018 两轮传播
Fresh turn1精确复现已接受单轮证据，mismatch=0；随后turn2完整31省执行，62/62 household/HJB/KFE/firm均返回，科学重试0。

安徽：
- household rah：`.09 -> .0829892058879816`；
- turn2 rah由原生资本分配复合规则使用turn1 entering `ra`向量生成，Anhui source old ra仍为`.09`，没有人工override；
- turn1 firm used `ra=.02`成为turn2 entering firm `ra=.02`，但不直接成为turn2 household rah；按源码时序，它第一次能够通过下一次资本分配进入household composite return是在turn3；
- firm raw ra0：`-.02496997113112164 -> -.024968505109415375`，两轮均低于`.02`并clip到`.02`；
- raw wage：`2.5721358283733027 -> 2.1373365306922518`，两轮均clip到1.3；
- HJB iterations `64 -> 31`，HJB/KFE两轮均返回；
- nk_gap `98575.17052447716 -> .34756612158493083`，yt_gap `.5829310876093212 -> .04945416591467944`。

全国：firm rate lower/interior/upper两轮均`31/0/0`；wage `5/4/22 -> 5/8/18`；turn2 max nk_gap=`.45946738761290562`，仍高于现有`<.1` adaptation gate，所以两轮Zt/GovInv调整均0。

这些证据证明corrected-2018前两轮可执行且firm return没有落入旧高收益区；但只有两轮，不能据此声称稳态收敛或旧call725后期失败已经消失。

## 当前 active task：turn3 direct corrected-rate propagation
严格执行一个fresh三轮轨迹，fresh turn1/turn2必须先复现接受证据。turn3是首个能让corrected turn1 firm used `ra=.02`通过native capital-allocation timing进入household composite `rah`的高信息量门。

中心问题：turn3安徽rah实际值与source vector；corrected `.02`传播幅度；turn3 raw firm return区域；wage/HJB/KFE/gap/controller变化。禁止turn4、steady-state、GE、annual、MATLAB、IRF/Results、科学重试或参数/solver/boundary调整。

## 后续路线
turn3传播验收 → 再决定是否需要5–10 turn受控prefix或可进入bounded steady-state prefix。只有corrected轨迹再次出现高收益、异常反转或不收敛证据时，才重新进入GovInv外层适应速度/household-KFE数值诊断。

2022–2023六个非正资本/无效Zt继续作为独立未来年份数据质量问题。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
