# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`CORRECTED_2018_SINGLE_TURN_ACCEPTED__FULL_ORDERED_TURN_PASS__TURN2_PROPAGATION_ACTIVE`。
最新接受候选：`90ee5b29f3be070d9f8f28c9614e1b59fe798462`。报告：`docs/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_TWO_TURN_PROPAGATION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 2018数据层已闭合
- 安徽修订后2018现价GDP官方公布值=`34010.9`亿元；保护workbook=`34010.91`仅在官方0.1亿元精度下匹配。
- 安徽2018常住人口=`6076`万人，依据2023《中国人口和就业统计年鉴》按2020人口普查修订的历史序列。
- PIM资本冻结并闭合：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；安徽`K2018=1357314108.2013683`，V2 CAP=`1357314108201.3684`；资本是model-derived calibration object，2011投资统计定义断点继续作为限制。
- 时间合同：PLM rolling 10-year；2018 PLM vintage19/window2009–2018；same-year Zt。
- canonical workbook：`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`，私有本体不提交GitHub。

## 已接受 corrected-2018 turn 1
一次完整31省source-faithful ordered turn已通过。31/31 household/HJB/KFE/firm均返回；所有HJB在64次更新后收敛，KFE 31/31返回。科学重试0。

安徽turn 1：
- firm raw `ra0=-0.02496997113112164`；used `ra=0.02`，撞下限而非上限；
- raw wage=`2.5721358283733027`，used wage=`1.3`；
- household进入turn 1仍使用carried `rah=0.09`；
- HJB statistic=`3.5073277615538245e-11`，KFE返回；
- aggregates C=`11.400731651949162`、L=`0.647623598114104`、A=`7.274097868486394`、B=`4.6982774669466725`。

全国turn 1：firm rate lower/interior/upper=`31/0/0`；wage lower/upper=`5/22`；最大`nk_gap=204296.40029802968`在山东，因此adaptation gate未开启，Zt/GovInv调整0。

该PASS只证明corrected-2018第一轮完整可执行且当期firm return位于低收益侧；不能据此声称旧turn23/call725的后期高收益或不收敛已消失。尤其turn 1 household `rah=0.09`仍是进入/滞后状态，而当期firm `ra=0.02`不能改写同轮household。

## 当前 active task：turn 2 propagation
下一任务严格只执行一个fresh corrected-2018两轮轨迹，最多turn 1 + turn 2，禁止turn 3/steady-state/GE/annual/IRF。中心问题是观察turn 1的corrected firm rate如何通过native state transition进入turn 2 household `rah`及后续firm/HJB/KFE/controller。

必须记录turn 2实际`rah`来源，不得手工设为0.02；若fresh turn 1与已接受turn 1出现实质不一致则停止。任何科学失败保存并停止，不做科学重试，不调模型方程、GovInv、rates、grid、solver/tolerance或boundary law。

## 后续路线
turn 2 propagation验收 → 决定是否进入更长但仍受控的multi-turn prefix → 只有在轨迹证据充分后才考虑steady-state prefix。若corrected数据下仍出现后期高收益/不收敛，再审计GovInv外层适应速度和household/KFE数值有效性。

2022–2023六个非正资本/无效Zt记录继续作为独立未来年份数据质量问题。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
