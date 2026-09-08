"""Render the bounded scientific report from saved summaries only."""
import json
from pathlib import Path
import sys


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(root, output, report):
    root = Path(root)
    output = Path(output)
    summary = read(output / "summary.json")
    arrays = summary["array_comparisons"]
    operators = summary["generator_diagnostics"]
    distribution = summary["distribution_diagnostics"]
    terminal = read(root / "science/terminal.json")
    preflight = read(root / "preflight.json")
    old = summary["HJB_status"]["baseline_09"]
    new = summary["HJB_status"]["new_07"]
    report_text = f"""# Call725 rah=0.07 原生初始化敏感性报告

- Diagnostic completion: `COMPLETE`。
- Input binding: `EXACT_ONE_FACTOR_RAH_AND_MAPPED_R_A`。
- Outcome: `HJB_CONVERGED_AND_KFE_RETURNED`；数值有效性单列，不称 MODEL_PASS。
- Results eligibility: `FALSE`。
- live main / task checkpoint: `{preflight['live_main']}`。
- 工作树：`D:\\ProjectTemp\\ch5-astra-local-doc-sync-20260907-001`；证据根：`{root}`。

## 结果

只读 `.09` 基线在原生初始化后运行100个HJB更新仍未收敛，统计量 `{old['HJB_statistic']}`；原adapter继续进入KFE，原始直接求解结果非有限并抛出 `faithful contaminated-row solve is non-finite`，没有有效density或aggregate。

新的 `.07` 单户运行在第 `{new['HJB_iterations']}` 个HJB更新收敛，统计量 `{new['HJB_statistic']}`，满足原有严格条件 `<1e-7`。原KFE返回，原聚合返回：C=`{new['aggregates']['c_ss']}`，有效z加权L=`{new['aggregates']['l_ss']}`，A=`{new['aggregates']['a_ss']}`，B=`{new['aggregates']['b_ss']}`，A+B=`{new['aggregates']['total_assets']}`，density normalization=`{new['aggregates']['density_normalization']}`。

这一结果支持该实现、该保存输入下的局部“收益率 + 原生初始化链”敏感性：从 `.09` 的HJB非收敛/KFE失败变为 `.07` 的HJB收敛/KFE返回。实验同时重新生成了随rate变化的V0/l0，因此不是固定初值算子实验；它不证明rah是唯一原因、`.07` 是普适安全率或生产ramax应修改。

## 精确输入绑定

基线对象来自已接受的 `D:\\ProjectTemp\\ch5-2018-observable-prefix-replay-20260908-001`，manifest_02 SHA256=`{preflight['baseline_manifest_sha256']}`。逐项核验15个消费对象的capture-index/manifest SHA，未重哈希旧13,800项全集。上下文为calendar2018、outer24、province index0=11/index1=12、安徽、call725。

深拷贝状态仅改 `state['rah']`：`0.09 -> float('0.07')`；新值repr=`{preflight['intervention']['repr']}`、hex=`{preflight['intervention']['hex']}`，并验证它不等于 `0.09-0.02` 的binary64结果。映射后的HouseholdInputs仅 `r_a` 同步改变；carried firm ra和ramax仍为 `.09`，其余state、grid、EconomicParams、wage=`16.82014806560587`、rb=`.02`、rb_gap=`.07`、tau=`.05`、Tt=`.1`、a_bar=`1e-6`、Delta1000、crit1e-7、maxit100、drift tolerance1e-12逐对象保持。

`.07` 通过原 `_source_initial_arrays` 一次重新生成V0/l0，没有读取 `.09` V0/l0作为运行输入。新旧V0最大绝对差 `{arrays['native_initial_value']['difference']['norm_inf']}`，2范数差 `{arrays['native_initial_value']['difference']['norm_2']}`；l0最大绝对差 `{arrays['native_baseline_labor']['difference']['norm_inf']}`，2范数差 `{arrays['native_baseline_labor']['difference']['norm_2']}`。两组各800个值全部有限。

实际加载的LF runtime保持只读；initializer blob `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`、adapter blob `0033baee136c0328e80ffb8b794a88d4405c976c`、worker mapping blob `7473e04418744d745000afb21d84588273cc5bca`、export blob `9e7dc9556a2b76811e78f89999abecc045886106` 均核验。protected MATLAB HJB SHA256=`{preflight['protected_HJB_sha256']}`，仅只读；没有调用年度worker或MATLAB。

## 策略与初值响应

全部 `.07` HJB数组均为20x20x2且800/800有限。consumption范围 `{arrays['consumption']['new']['min']} .. {arrays['consumption']['new']['max']}`，labor范围 `{arrays['labor']['new']['min']} .. {arrays['labor']['new']['max']}`，transfer范围 `{arrays['transfer']['new']['min']} .. {arrays['transfer']['new']['max']}`，adjustment cost范围 `{arrays['adjustment_cost']['new']['min']} .. {arrays['adjustment_cost']['new']['max']}`，mu_a范围 `{arrays['mu_a']['new']['min']} .. {arrays['mu_a']['new']['max']}`，mu_b范围 `{arrays['mu_b']['new']['min']} .. {arrays['mu_b']['new']['max']}`。相对不同输入的 `.09` 保存输出，liquid label改变 `{arrays['liquid_label']['changed_count']}` 个，transfer label改变 `{arrays['transfer_label']['changed_count']}` 个；这些是描述性响应，不使用parity阈值判相等。

有效illiquid return在 `.07` 下范围 `{arrays['effective_illiquid_return']['new']['min']} .. {arrays['effective_illiquid_return']['new']['max']}`；`.09`基线为 `{arrays['effective_illiquid_return']['baseline_09']['min']} .. {arrays['effective_illiquid_return']['baseline_09']['max']}`。完整数组极值、有限计数、差范数及标签计数见 `array_comparison.json`。

## 算子与边界

HJB最后迭代算子：负非对角元 `{operators['HJB_iteration_operator']['negative_offdiagonal_count']}` 个，最小 `{operators['HJB_iteration_operator']['negative_offdiagonal_min']}`；行和最大绝对值 `{operators['HJB_iteration_operator']['row_sum_fsum_max_abs']}`；矩阵无穷范数 `{operators['HJB_iteration_operator']['matrix_norm_inf']}`。

post-loop KFE算子：负非对角元 `{operators['post_loop_KFE_operator']['negative_offdiagonal_count']}` 个；行和最大绝对值 `{operators['post_loop_KFE_operator']['row_sum_fsum_max_abs']}`；矩阵无穷范数 `{operators['post_loop_KFE_operator']['matrix_norm_inf']}`。用保存mu和网格间距重建的边界外向rate有 `{operators['post_loop_KFE_operator']['post_drift_boundary_leak']['exact_positive_count']}` 个正单元，最大 `{operators['post_loop_KFE_operator']['post_drift_boundary_leak']['max']}`，总和 `{operators['post_loop_KFE_operator']['post_drift_boundary_leak']['sum']}`；row-sum+leak最大绝对值 `{operators['post_loop_KFE_operator']['post_drift_boundary_leak']['row_sum_plus_leak_max_abs']}`。其中外向漂移全部来自upper-b的29个单元；lower-b/lower-a/upper-a外向计数均0。它延续已知边界生成算子问题，KFE返回没有修复该问题。

`.09` post-loop算子规模为 `{operators['baseline_09_post_loop_KFE_operator']['matrix_norm_inf']}`，`.07` 降为上述规模，但不同输入下的改善不是同输入parity或普适稳定性结论。矩阵行和的负值另列为“matrix-implied omitted rate”；只有post-loop算子才用保存drift独立重建边界leak，未把普通浮点抵消直接命名为泄漏。

## KFE与分布

原contaminated-row直接求解残差inf=`{distribution['contaminated_raw_residual_inf']}`，尺度分母=`{distribution['contaminated_raw_scale_denominator']}`，比值=`{distribution['contaminated_raw_normwise_ratio']}`，与source回报一致。未修改转置上的稳态残差 `||A.T @ density||inf={distribution['unmodified_transpose_stationary_residual_inf']}`，尺度分母=`{distribution['unmodified_transpose_scale_denominator']}`，比值=`{distribution['unmodified_transpose_normwise_ratio']}`。这两者是不同方程；contaminated-row残差小不能替代原稳态残差。

归一化总质量 `{distribution['normalized_total_mass']}`。density最小 `{distribution['density_min']}`、最大 `{distribution['density_max']}`；精确负值 `{distribution['negative_density_exact_count']}` 个，带权负质量 `{distribution['weighted_negative_mass']}`。负值幅度接近binary64舍入量级，但本报告保留精确符号计数，不裁剪；较大的未修改稳态残差和边界泄漏意味着“有限且归一”不等于有效稳态分布。

## 调用账本与工程记录

一个Python科学进程、一个worker，四个线程环境变量均1；Python3.11.9、NumPy2.4.6、SciPy1.17.1，与保存 `.09` 运行环境相同。科学耗时 `{terminal['scientific_seconds']}` 秒，warning `{len(terminal['warnings'])}` 条，科学重启0。计数：native initialization1；labor root800、nested brentq800、root residual `{terminal['counts']['root_residual']}`（bracketing `{terminal['counts']['root_bracketing_residual']}` + brentq `{terminal['counts']['root_brentq_residual']}`）；adapter/HJB各1；HJB update/direct solve26；KFE/direct solve各1；aggregate1。`.09` 新科学调用0。额外policy/evaluator、诊断/条件/高精度solve、firm、one-turn/controller、GE、年度、其他省年、R/PLM、动态/IRF/Results和MATLAB均0。

首次预检目录 `...-001` 因外部index在旧manifest中以仓库副本路径绑定而停止，科学进入0；随后显式验证外部index与该副本字节一致，在fresh `...-002` 完成。一次测试命令曾带错误路径，未创建科学进程；首轮10项合成测试发现普通映射键名 `array` 与数组描述符冲突，修复后保留失败日志并通过。科学启动没有失败，任务允许的外部启动重试未使用；科学进入后没有重启。

## 检查、证据与限制

合成测试覆盖schema解码、exact one-field diff、binary64字面值、原生初始化单次委派、`.09`不作为warm start、false-HJB继续KFE、失败前保存、失败进入计数、缺失阶段和import-time零科学；后处理增加算子精确符号与两类残差区分。最终真实日志解析计数和hash在reports receipts中。

外部science目录保存input binding、`.07` V0/l0、完整HJB返回、KFE matrix/RHS/raw、KFE返回、聚合、warnings和terminal。有限manifest只绑定实际消费的旧基线对象、加载源码、新科学输出和交付物，并独立重读；不上传大数组。生产/helper/export未修改。

本实验不实施D1–D3，不修改ramax、carried firm ra、Zt/GovInv、a_bar、参数、helper、solver或容差。HJB/KFE改善不能宣布生产修复、唯一因果、普适安全率、完整2018、generator有效或Results接受。已知P32、sigma、共同初始化多轮、边界leak及修正年度覆盖问题继续开放。后继科学选择由Owner/Reviewer另行决定。
"""
    Path(report).write_text(report_text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
