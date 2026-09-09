# Chapter 5 MP4C 2018 revised GDP + canonical workbook — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `7e363b2d228623d3b315f8c140cad6332a57104b`.

## Verdict

Reviewer marker: `REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACCEPTED__2018_DATA_LAYER_CLOSED__SCIENCE_RUN_NEXT`.

Accept `REVISED_2018_GDP_CLOSED__CANONICAL_WORKBOOK_BUILT`.

## Accepted findings

1. 安徽省统计局《安徽省统计局关于修订2018年全省生产总值数据的公告》在第四次全国经济普查和地区生产总值统一核算制度基础上公布安徽2018年现价GDP修订值为 `34010.9` 亿元。
2. 保护工作簿 `34010.91` 亿元与官方公布值在官方一位小数精度下匹配；不能把官方来源提升为两位小数精确身份。canonical final-use GDP采用官方公布的 `34010.9`，同时保留原源值 `34010.91` 和精度边界。
3. 2018安徽最终静态输入接受为：GDP `34010.9`亿元 / `34010900.0` transformed；POP `6076`万人 / `607600.0`；PIM CAP `1357314108.2013683` / `1357314108201.3684`；industry-4 alpha `0.772866243094144`；same-year `IND_Zt=0.0006934644495858679`（显示精度）。
4. `CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx` 已在外部私有证据目录生成，SHA-256 `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。仓库未提交该私有工作簿，只提交manifest/readback/receipt等窄证据。
5. Builder报告的workbook验证：12/12 required sheets；744/744 PIM记录与保护workbook binary64一致；2022–2023六个非正资本记录保留并使相应Zt无效/留空；无公式、宏或外部链接；8/8静态/合成测试通过。
6. 本轮所有MATLAB、household/HJB/KFE、root/linear solve、firm、GE/annual、IRF/Results科学调用均为0。

## Acceptance boundary

Reviewer通过GitHub核对了候选diff、GDP receipt、报告、manifest/readback边界；私有canonical xlsx本体不在GitHub，因此Reviewer没有独立打开该本地二进制文件。对workbook内部结构的接受依据是Builder的hash-bound manifest/readback、测试与渲染审阅记录。该限制不影响GDP身份闭合和2018静态输入身份接受。

## State after acceptance

2018数据层主要blocker关闭：
- GDP closed at official published precision;
- population closed at revised official-yearbook history;
- capital/PIM method and 2018 CAP closed as model-derived calibration object;
- temporal contract / rolling-10y PLM / same-year Zt closed.

2022–2023六个非正资本记录仍为独立未来年份数据质量问题，不影响下一次2018受控验证。

Results eligibility remains `FALSE`.

## Next route

进入真正2018 corrected input 的小规模科学验证。第一步仅做一个受控单年2018 source-faithful one-turn/prefix验证，不直接运行完整31省稳态到收敛，也不调GovInv/alpha、grid、rate、solver或tolerance。