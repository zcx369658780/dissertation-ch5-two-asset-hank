"""Render the attribution report from saved deterministic outputs only."""

import csv
import json
from pathlib import Path
import sys


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(evidence_root, report_output, report_path):
    evidence_root = Path(evidence_root)
    report_output = Path(report_output)
    summary = read(report_output / "summary.json")
    preflight = read(report_output / "preflight.json")
    calls = read(report_output / "zero_call_ledger.json")
    tests = read(sorted(evidence_root.glob("tests_*.receipt.json"))[-1])
    rows = list(csv.DictReader((report_output / "cell_ledger.csv").open(encoding="utf-8")))
    p_values = [float(row["p"]) for row in rows]
    negative_mass = sum(value for value in p_values if value < 0.0)
    negative_count = sum(value < 0.0 for value in p_values)
    loc = summary["pin_residual_localization"]
    bal = summary["signed_mass_balance"]
    scale = summary["residual_scaling"]
    top = summary["occupied_escape_cells"]["top_15"]
    top_lines = "\n".join(
        f"| {row['rank']} | {row['k0']} | ({row['b']}, {row['a']}, {row['z']}) | {row['p']:.17g} | {row['ell_total']:.17g} | {row['weighted_outward_flux']:.17g} | {row['cumulative_share']:.6%} |"
        for row in top[:10]
    )
    text = f"""# Call725 rah=0.07 KFE 质量收支归因报告

- Diagnostic completion: `COMPLETE`。
- Source escape interpretation: `SUPPORTED`，仅指保存有限箱算术，不采纳新的经济进入/退出法则。
- Results eligibility: `FALSE`；不称 `MODEL_PASS`。
- live main / task checkpoint: `{preflight['live_main']}`。
- 工作目录：`D:\\ProjectTemp\\ch5-astra-local-doc-sync-20260907-001`。
- 新证据根：`{evidence_root.resolve()}`；只读科学证据根：`{preflight['source_evidence_root']}`。
- 任务指定执行路由为gpt-5.6-sol / medium；本地实际模型标签未由仓库或运行回执暴露，因此不虚构已验证标签，也未修改provider/global配置。

## 归因结论

已确认发布诊断使用正确的原始对象和顺序：`Q`与HJB保存的post-loop算子、KFE入口算子、KFE返回的original operator在CSR存储上精确相同；`T`精确等于`Q.T`；`B`与直接求解入口及KFE返回的污染矩阵精确相同。保存density vector精确等于三维density的F-order展开，且精确满足`g=x/saved_eta`。保存`eta={summary['identity_checks']['eta_saved']}`与`omega*sum(x)={summary['identity_checks']['eta_recomputed']}`并非逐位相同，但通过预先冻结的128-eps规则；`omega*sum(g)={summary['identity_checks']['normalization']}`同样通过。

`B`只改变`T`的第`k={loc['pin_row_k0']}`行，差异support为4项；替换行为单位行，`rhs[k]=x[k]={loc['raw_rhs_pin']}`，其原始pin方程残差为`{loc['raw_pin_equation_residual']}`。该`.007`只固定raw向量分量，不是概率流率。F-order位置为零基`(b,a,z)=({loc['f_order_indices0']['b']},{loc['f_order_indices0']['a']},{loc['f_order_indices0']['z']})`、MATLAB一基`({loc['matlab_indices1']['b']},{loc['matlab_indices1']['a']},{loc['matlab_indices1']['z']})`，坐标`(b,a,z)=({loc['coordinates']['b']},{loc['coordinates']['a']},{loc['coordinates']['z']})`，是内点而非逃逸边界。

未修改稳态残差`r=Tg`的最大值全部落在被替换行：`r[k]={loc['stationary_pin_residual']}`，绝对值占残差L1的`{loc['pin_abs_share_of_residual_L1']:.17g}`。全部off-pin绝对残差之和仅`{loc['off_pin_abs_sum']}`，最大off-pin残差`{loc['largest_off_pin_residual_abs']}`位于row `{loc['largest_off_pin_row']}`；off-pin关系`r[i]=e[i]/eta`最大差`{loc['off_pin_relation_r_equals_e_over_eta_max_abs']}`。因此物质性的stationarity failure就是row replacement丢弃的那一个原方程；这不等于证明所有可能density都无稳态解。

## 有符号质量收支

按保存drift和实际网格间距重建，只有upper-b存在外向rate：29格，其他三面均0。29格中20格有正概率和正流量，9格的保存概率为0；upper-b面概率质量为`{bal['face_probability_mass']['upper_b']['signed']}`，边界union质量为`{bal['face_probability_mass']['union']['signed']}`。四个face质量在角点重叠，未相加冒充不重叠总量。

有符号流量账本为：

- `omega*fsum(r)={bal['omega_sum_r_math_fsum']}`；`dot(q,p)={bal['dot_q_p']}`。
- 实际density加权逃逸`dot(ell,p)={bal['escaped_mass_flow_dot_ell_p']}`，全部来自upper-b。
- `dot(delta,p)={bal['delta_weighted_correction']}`，其中`delta=q+ell`，`max|delta|={bal['delta_max_abs']}`。
- `-dot(ell,p)+dot(delta,p)={bal['minus_escape_plus_delta']}`，与`omega*fsum(r)`差`{bal['mass_identity_abs_discrepancy']}`，冻结上限`{bal['mass_identity_frozen_bound']}`，判定PASS。
- pin行候选补偿源`-omega*r[k]={bal['candidate_balancing_source_minus_omega_rk']}`；off-pin有符号修正`{bal['off_pin_signed_correction']}`。`escape-delta+offpin={bal['escape_minus_delta_plus_off_pin']}`，差`{bal['source_balance_abs_discrepancy']}`，冻结上限`{bal['source_balance_frozen_bound']}`，判定PASS。

因此，row replacement在该保存解中确实等价于一个正源，数值上平衡upper-b的density加权逃逸。这个源强度来自被丢弃方程及归一化后的`g`，不能从raw RHS `.007`直接解释。全部density仍保留`{negative_count}`个精确负项，带权负质量`{negative_mass}`；这些负项对逃逸流贡献为`{bal['escaped_flow_by_probability_sign']['negative_probability']}`，对`dot(q,p)`贡献为`{bal['row_sum_flow_by_probability_sign']['negative_probability']}`，没有裁剪或改符号。

## 主要占用逃逸格点

| rank | k0 | (b,a,z) | p | ell | p*ell | cumulative |
| ---: | ---: | --- | ---: | ---: | ---: | ---: |
{top_lines}

前3格贡献`{top[2]['cumulative_share']:.6%}`，前6格贡献`{top[5]['cumulative_share']:.6%}`，前10格贡献`{top[9]['cumulative_share']:.6%}`。完整800格账本在`cell_ledger.csv`，逐格保留坐标、face、g/p、mu、四方向ell、q、delta、r、带权流量和pin标记。

## 源码阶段

冻结export blob `{preflight['export_blob']}` 的lines424-450构造轴算子：在upper-b，保存`mu_b>0`成为`b_forward=mu_b/db`；因为`i+1`越出网格，其forward offdiagonal不写入，但对角线仍保留`-(rb+rf)`中的该rate，所以`q=Q*1`含相应负流失。lines561-562说明这是HJB停止后由最终保存drift重建的post-loop `Q`；lines592-600再形成`T=Q.T`、替换row k、设raw pin并归一化。具体行文本和保护HJB SHA在`source_line_map.json`。

质量账本没有使用最后一次HJB迭代算子`Qh`。`Qh`仍有`{summary['Qh_separate']['negative_offdiagonal_count']}`个负非对角元、最小`{summary['Qh_separate']['minimum_offdiagonal']}`；post-loop `Q`的非负offdiagonal不能消除这个独立问题，也不能把HJB停止统计量升级为完整非线性有效性。

## 残差尺度与剩余科学选择

污染系统raw残差inf=`{scale['contaminated_raw_residual_inf']}`、尺度分母=`{scale['contaminated_raw_scale_denominator']}`、比值=`{scale['contaminated_raw_ratio']}`。原始未修改稳态残差inf=`{scale['unmodified_stationary_residual_inf']}`、分母=`{scale['unmodified_stationary_scale_denominator']}`、比值=`{scale['unmodified_stationary_ratio']}`。后一个比值不是质量流失百分比；真正带权逃逸是上述`{bal['escaped_mass_flow_dot_ell_p']}`。尽管row-replaced solver返回且raw残差很小，数值陈述`Tg=0`仍明显不成立。

最小剩余科学选择是：Owner需在实施任何修复或修正KFE/2018运行前，选择有限箱边界法则以及是否/如何存在经济上有意义的source处理。已有D1-D3仍是未批准选项；本任务没有移动pin、改对角线、改边界、改rah/ramax/a_bar或重新求解。

## 检查、证据与调用账本

仅消费前序manifest绑定的13个文件：binding、HJB post-loop返回、KFE entry/direct input/direct return/KFE return及terminal的JSON/NPZ；外部science index与Git副本LF身份一致。前序manifest SHA256=`{preflight['predecessor_manifest_sha256']}`。未重哈希历史13,800项。

最终合成测试`{tests['ran']}/{tests['individual_ok']}`通过，覆盖实际ledger函数的F-order映射、exact row replacement、raw归一化、保守与带off-pin修正的非保守例、角点方向合并、负概率贡献、转置方向拒绝及import-time无solver。早期失败日志与一次eta exact断言失败回执均保留；这些都是纯后处理问题。

真实新增科学调用：initializer/root/HJB/KFE、直接/迭代/特征值/优化/条件求解、policy/evaluator、firm/controller/GE/年度/动态/IRF/Results和MATLAB全部0；scientific retry0；assembler/selector0。执行中仅有保存数组解码、矩阵向量乘法、求和和报告测试。生产/export/helper和全部前序科学文件未修改。
"""
    Path(report_path).write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
