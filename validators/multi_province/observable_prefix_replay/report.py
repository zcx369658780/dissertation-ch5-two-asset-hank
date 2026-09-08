"""Render a bounded observation report from completed durable postprocessing."""
import csv
from pathlib import Path
import sys
from analyze import read,REPO

def rows(p):
    with p.open(encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def mdtable(data,keys):
    if not data:return '未到达；没有可报告的观测。\n'
    lines=['|'+'|'.join(keys)+'|','|'+'|'.join('---' for _ in keys)+'|']
    for r in data:lines.append('|'+'|'.join(str(r.get(k,'')).replace('|',' / ') for k in keys)+'|')
    return '\n'.join(lines)+'\n'
def main(root):
    out=REPO/'reports/2018_observable_prefix_replay_20260908';s=read(out/'summary.json');t=s['terminal'];assert t is not None
    c=t['counts'];p=s['prefix'];error=t['error'];firms=rows(out/'firm_prices_and_operands.csv');controllers=rows(out/'controller_timeline.csv');actions=rows(out/'actual_adaptive_actions.csv');panel=rows(out/'province_coverage.csv');h=rows(out/'hjb_return_comparison.csv');a=rows(out/'accepted_timeline_comparison.csv')
    if p['first_mismatch']:reproduction='PREFIX_DIVERGED'
    elif t['terminal']=='PREFIX_LIMIT':reproduction='LIMIT_REACHED_WITHOUT_ORIGINAL_FAILURE'
    elif error and error['message']=='faithful contaminated-row solve is non-finite' and t['current']['call']==725:reproduction='MATCHED_PREFIX_AND_FAILURE_REPRODUCED'
    elif t['terminal']=='PRELAUNCH_BLOCKED':reproduction='PRELAUNCH_BLOCKED'
    else:reproduction='EARLIER_EXCEPTION' if error else 'LIMIT_REACHED_WITHOUT_ORIGINAL_FAILURE'
    complete='OBSERVABLE_PREFIX_CAPTURE_COMPLETE' if c['outer_entry']==24 and c['firm']==713 and c['HJB_returns']==725 else 'PARTIAL_EVIDENCE'
    assert reproduction=='MATCHED_PREFIX_AND_FAILURE_REPRODUCED' and c['HJB']==725 and c['KFE_returns']==724
    assert all(x['absolute']==0 for x in p['maxima'].values())
    test=read(sorted(root.glob('tests_*.receipt.json'))[-1]);scope='新路径证据；不得填补旧 PID67056 的分叉后内部状态' if p['first_mismatch'] else '旧入口标量的匹配前缀；历史没有保存的完整数组身份仍未获证明'
    text=f'''# 2018 原参数可观测前缀回放报告

- Completion: `{complete}`。
- Reproduction: `{reproduction}`；Results eligibility=`FALSE`。
- Authority/base main: `09de5178d6a51bf6b36fbd4a309d161a8ef99d44`；exact task `tasks/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY.md`，启动时 live main 指定本任务有效。
- Builder worktree: `D:\\ProjectTemp\\ch5-astra-local-doc-sync-20260907-001`。
- Branch: `codex/ch5-2018-observable-prefix-replay-20260908`；不合并 main、不启动后继实验。
- Evidence root: `{root}`。

## 关键结论

原异常在第24轮安徽call725复现，HJB100步返回 false、统计量0.3038218386543494，原 adapter 随后进入KFE并遇到原 non-finite异常；HJB及原始KFE线性返回均已保存。新旧725个入口的11个连续字段完全相同（不只是容差内），未发现首差。

第23轮贵州决定全国max nk_gap=0.04124871080231385，门确实打开。安徽真实动作是Zt从0.7163967429125945调至0.6650485431957093、GovInv从115261012.11434016乘1.1至126787113.32577418。控制器已执行，并非遗失调整。

该轮firm使用调整前Zt/GovInv，返回ra0=0.21906938941252802、wt0=2.5772708754207905，截断到ra=.09、wjt=1.3。rk=0.244069389412528、delta=.025、截零后PIt=0，故此时ra0由rk减折旧决定，divrate=0；mt=0.9943859584740543。Kt中私人供给份额约0.0008794002451333387，其余为GovInv。当前household Lt_prev=0.6661844894752886，而目的省lt_supply=3210665.858026796；这些是不同源字段，未做单位修正。

安徽r_i=0，call725的rah=.09来自turn23资本配置消费的turn22 ra=.09；turn23 firm仍截断为.09。反馈调整发生在firm之后，不能即时改写已经生成的该家户价格。以上是阶段与代数归因，不是失败的因果利率结论。

## 复现与终点

保存 {p['available_entries']} 个家户入口；逐项比较 11 个连续字段以及 outer/province/order/call 分类，连续规则严格为 `abs(x-y)<=128*eps64*max(1,abs(x),abs(y))`。匹配前缀 {p['matched_prefix']} 个入口。首个差异：`{p['first_mismatch']}`。逐字段最大绝对误差/eps 归一误差见 `prefix_comparison.json`，所有标量行见 `entry_comparison.csv`。

终止：`{t['terminal']}`；当前位置 `{t['current']}`；阶段 `{t['phase']}`；最后完整保存阶段 `{t['last_durable_stage']}`。异常：`{error['type']+': '+error['message'] if error else '无'}`。完整 traceback 保存在 receipts/terminal.json。科学耗时 {t['scientific_seconds']:.3f} 秒。

HJB 历史返回可比较 {len(h)} 项，状态/步数不匹配 {sum(x['status_match']!='True' for x in h)} 项，128-eps 统计量不匹配 {sum(x['statistic_match_128eps']!='True' for x in h)} 项。旧审计可比控制器标量 {len(a)} 项，不匹配 {sum(x['match_128eps']!='True' for x in a)} 项。以上只证明已比较字段；{scope}。保留原审计 PARTIAL_EVIDENCE，不重复年度表提取，错误 audit-001 完全排除。

## 已观测的价格与调整

本轮家户入口保存 actual rah/w；firm 原返回保存 ra0/wt0/ra/wjt/mt/rk/PIt/Corptax，未把重建值冒充返回值。`firm_prices_and_operands.csv` 保留所有 consumed 参数，包括当前 household `l_ss` 原值被放入 `Lt_prev`（没有乘 N）、目的省 lt_supply、Kt_prev、Zt_1、pit/pit_1、carried rk、税率与上下界。包含大小写不同的 it/It 字段，读取表时须用大小写敏感解析器，如 Python csv。

安徽关键生成阶段：

{mdtable([x for x in firms if x['province']=='安徽' and int(x['step']) in (1,4,5,12,22,23)],['step','ra0','ra','wt0','wjt','mt','input_Zt','input_GovInv','input_Lt_prev','lt_supply','private_share','state_share'])}
安徽实际动作：

{mdtable([x for x in actions if x['province']=='安徽' and int(x['step']) in (4,5,12,22,23)],['step','zt_before','zt_after','govinv_action','govinv_before','govinv_after'])}
全国控制器（真实 diagnostics 返回；门开闭由 captured max 和 steady_state 按原 `<0.1` 规则标注）：

{mdtable(controllers,['step','max_nk','max_nk_provinces','max_yt','household_converged','ra_upper','ra_lower','converged','gate_derived_from_captured'])}
每轮 31 省 nk_gap、yt_gap、tKN 和全部 max ties 在 `controller_all_provinces.csv`，可逐步追查贵州及其他决定省份；实际逐省动作在 `actual_adaptive_actions.csv`。第四轮安徽由低产出触发 Zt 向上重置，GovInv 乘 0.9，这是捕获的真实动作，不是假定初值过高。

价格归因使用同一 firm 调用的 operands，单纯标量运算核验 `ra0=rk-delta+PIt*(1-corptau)/Kt`、`rk=mt*alpha/(Kt/Yt)`、mt 原分解和 clipping 后税收。`algebra_checks.csv` 共 {s['algebra_checks']} 项，超出冻结规则 {len(s['algebra_failures'])} 项。重建仅为对捕获对象的身份核对，没有调用 evaluate_firm 或任意求解器。截断 branch 是根据实际 raw/returned/bounds 的派生归因；未声称捕获了函数内部逐行 branch trace。

`rah_lag_transmission.csv` 单列旧 ra 消费时点、rah 生成时点及下一轮共同状态。安徽 inter_prv_ratio=0，故传递式等于 consumed old ra：turn23 生成下一入口 rah 时消费 turn22 ra；turn23 新 firm ra 不会反向进入同轮已经完成的家户。GovInv/Zt 在 firm 后调整，必须与 firm-used 状态区分。任何未到达 turn22–24 的链条均保留为空，不用旧报告数字补成此次观测。

## 全省覆盖与边界口径

共24份完整31省共同入口状态、725个实际家户入口、713个firm返回及23份全国控制器记录。第24轮仅前12省进入家户；其余19省的共同旧状态已提前保存，但没有第24轮家户返回，且不存在第24轮firm阶段。call725的KFE返回对象和家户aggregate缺失，原始nonfinite线性返回仍在；没有call726。

全部31省都曾出现raw ra0高于上界。第23轮仍有24省ra触上界；天津、内蒙古、吉林、黑龙江、西藏、青海、宁夏已在内部。该轮wjt为19省上界、5省下界、7省内部。这些省际差别与动作时序保留在全省表，不将安徽推广为所有省份。


{mdtable(panel,['province','common_entries','household_entries','firm_returns','ra0_min','ra0_max','ra_exact_lower_count','ra_exact_upper_count','wt0_min','wt0_max','wjt_exact_lower_count','wjt_exact_upper_count'])}
完整表还给出 raw excursions、exact/128-eps near flags、上下界距离、mt 范围和实际 rah/w 范围。初始化独立列：全部 initial ra/rah=.09、wjt=.6、w=20；初始 wjt=.6 低于 firm 后续 .8 下界，这不是已执行 firm clipping 的返回。rah 与 firm 范围的比较仅为描述；w 为 composite household wage，不适用 wjt 的原生截断边界。没有引入 .07 阈值。

## 原算法、预算与工程经过

原年度 worker、online runtime、post-loop adapter、export 和其前置 source_map 依赖绑定不变；原输入 SHA256=`F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`。每户使用原生初始化，不用后期 MATLAB 共同初值 MAT，不更改 a_bar、参数、边界、算法、Delta1000、crit1e-7、100步 HJB 或 solver。source 默认 outer ceiling500；原 worker 实际传250，本任务只加外部24入口/23完整轮/call725停止上限，均未修改原上限。

首次启动 PID34908 在 import bootstrap 因 CRLF raw SHA 不符退出，尚未创建 capture/worker_outputs，初始化及全部科学进入=0。随后 `git -c core.autocrlf=false worktree add --detach` 在 evidence/source_runtime 建立同一 HEAD 的 LF 运行工作树，保留原工作树及全局配置。raw export SHA 与原 bootstrap 要求一致，全部 bound LF 身份通过；只导入 bootstrap 的探测返回 scientific_model_calls=0。消耗唯一外部启动重试，科学 PID28120，一个 worker，四个线程环境变量均1。科学进入后没有重启。

运行环境 Python3.11.9/NumPy2.4.6/SciPy1.17.1，Windows 和 BLAS 配置完整保存。旧启动 receipt 的 Python3.11.9 和四个单线程设置匹配；所读旧 receipts 未记录完整 NumPy/SciPy/BLAS 版本，不能断言全部历史环境二进制相同。没有切换或安装 solver。

真实计数（含失败进入）：

{mdtable([{'counter':k,'count':v} for k,v in c.items()],['counter','count'])}
一次 Python 科学进程，外部零进入失败启动一次；两次 launch 不等于两次科学运行。root residual/bracketing/brentq evaluations 分开计数；直接求解分 HJB/KFE。完整 per-call 账本见 `call_ledger.json`。MATLAB、独立诊断/条件估计求解、其他年份、R/PLM、shock/IRF/Results 均0。本任务包含新的 HJB/KFE/one-turn 运行，绝不填报全部0。

## 检查与证据

运行前13项合成测试通过。后处理增加边界128-eps与首差/完整比较测试，最新真实日志解析 `{test['ran']}` 项、逐行 ok `{test['individual_ok']}` 项、passed=`{test['passed']}`；日志 LF SHA256=`{test['lf_sha256']}`。测试只使用合成对象/AST 提取加假函数，未调用模型。曾有日志 GBK 解码失败和合成 NPZ 句柄清理失败；已修复并保留实际失败日志/成功日志，不计为科学调用。一次 PowerShell Import-Csv 因 it/It 大小写列冲突失败，改用 Python 大小写敏感解析，未修改数据或重跑科学。

`capture_index.jsonl` 给出每个阶段 JSON/NPZ 地址及原始字节 SHA；数组/稀疏 support 原样保存外部，Git 只保存小表和 receipts。有限 manifest 覆盖输入、绑定源码、全部 indexed captures、worker输出和允许交付物；排除 manifest 自身及 readback 避免循环；manifest_readback.json 记录独立逐文件重读结果。Git 文本的 LF 身份与 Windows 原始字节身份分列，不用历史 CURRENT 哈希对照新文档误报。

生产文件无修改；原主 checkout、70 个未跟踪文件及历史分支未清理或覆盖。实际新增文件仅在任务四个允许路径下。提交后非 force 推送专用分支并核验远端 SHA，发布身份由提交及最终交接提供。

## 结论边界与未决问题

这是原参数观测复现，价格关联不构成降 rah 的因果实验，不证明高价格导致 KFE/HJB 失败。即使复现原异常，也不构成稳定性修复、generator 有效性或年度接受。精确共同初值 MATLAB143/Python500 的独立历史结果、边界 generator 与 P32 内点/sigma 问题保持原判；D1–D3 未采纳且未实施。缺失的阶段不能用推测、舍入日志或分叉后新路径冒充旧内部事实。后续科学决策与任务发布留给 Owner/Reviewer。
'''
    (REPO/'docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_REPORT.md').write_text(text,encoding='utf-8',newline='\n')
    print(reproduction,complete)

if __name__=='__main__':main(Path(sys.argv[1]))
