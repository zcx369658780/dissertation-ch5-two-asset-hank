# CH5 TEMP V010｜人口N×0.5短迭代价格边界与家企投入核对（半自动长任务）

TASK_ID=CH5_TEMP_V010_SEMIAUTO_N050_PRICE_BOUNDARY_10_20_20261022
REVISION=ISSUED_20261022_R1
OWNER_APPROVED=2026-10-22：首轮降低N、10轮或条件延长20轮、逐省价格边界与供需表、每轮验收后Owner讨论；不授权下一组参数
MODE=ONE_SYNTHETIC_TWO_PROVINCE_N050_ARM__MAX_20_OUTER_ROUNDS
BASELINE_GOVERNANCE=cc8616038c595c302915b736e2f356cef46bc695
REVIEW_BRANCH=review/ch5-temp-n050-price-boundary-10-20-20261022
REVIEW_FIXED_PARENT=cc8616038c595c302915b736e2f356cef46bc695
REVIEW_TEMP_PATH=_review_tmp/ch5/temp-n050-price-boundary-10-20-20261022/
FORMAL_V010_UNCHANGED=TRUE
RESULTS=FALSE

## 1. 科学问题、真实来源与实验冻结
唯一实验为已归档100轮 TEMP 黑箱使用的原V010合成双省 `SYN_A,SYN_B`。冻结fixture `versions/0.0.10/synthetic_fixture_v1.json` Git Blob `40915658d93403cfc21b33a6b864b332b7857749`（同份源见历史模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` 的`tests/fixtures/v010_mainline_synthetic_v1.json`）；已精确核此fixture的`population_N=[100,160]`。唯一外生试验变化：`N_trial=[50,80]` = 两省原始N各乘0.5。不改本轮其它外生初始字段，特别是`Zt`、`GovInv`、`alpha`、目标Y、税、价格边界、capital S / lagged raw排序、人口参考pgdp及HA参数；**不得依N重估/重写初始Zt**，因为本轮只隔离人口效应，但在报告中明确原MATLAB使用`Zt_new=Y*K^(-alpha)*N^(alpha-1)`，所以这是一项受控敏感性分析而非直接复现MATLAB现实校准。轮次中若原已冻结模型`GovInv/Zt`自适应更新合法发生，必须照旧执行和记录，禁止额外冻结或偷偷改规则。
固定MATLAB-faithful两资产黑箱Git源：commit `216283cf4f1303afa60f1915e143a0b7303a9ffb`，`exports/matlab_faithful_two_asset_ha.py` Blob `9e7dc9556a2b76811e78f89999abecc045886106`、SHA256 `b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3`。冻结多省经济逻辑参考commit `94de4501dec051b969bee9d852eba2d4591f30ef` 的现有`firm.py`、`one_turn.py`、`steady_state.py`、`wage.py`等；不跨接不同版本的无证代码形成新模型。历史100轮事实仅复用2026-10-18审查 `docs/CH5_TEMP_V010_BLACKBOX_100_ROUNDS_INDEPENDENT_REVIEW_20261018.md`，不能重跑基准100轮，若逐轮基准源不完整记NOT_COMPARABLE。原私人历史ZIP可保留其已确认SHA256作身份参照，但**本任务不读取原私人整个ZIP/受保护旧journal或遍历历史scratch**。
V010数学正式plan `versions/0.0.10/plan.md`不改，TEMP不升格正式稳态/真实GE/政策冲击Results；不把100轮非收敛认作永不收敛。

## 2. 启动和生产安全限制
在同一live治理发行HEAD核 `CURRENT.md`、`TASK_CURRENT.md`、`docs/DOC_INDEX_CURRENT.md` 唯一 ACTIVE 及本轮ISSUE_MANIFEST源Git Blob，再对四件冻结来源精确单文件/单Blob核身份；不查宽`tasks`目录或root recursive树。使用唯一新隔离scratch `D:\ProjectTemp\ch5_temp_n050_price10or20_20261022_01`；BOOTSTRAP0检查可信父`D:\ProjectTemp`、scratch原不存在、拒绝reparse/符号链接逃逸、受保护root/index与外Git common dir元数据，不在旧树写脚本/代码，再BOOTSTRAP1独占创建、BOOTSTRAP2首次写前复核。不能修改旧100轮轨迹、历史私有ZIP、旧正式V010代码、旧ledger、C盘备份、真实31省数据/参数。允在新scratch里构建最小任务专用只读源加载与实验驱动，前提是源身份/单一启动入口/子进程回收/真实预算计费/STOP机制可证明；已有派生Ledger修补`PREPARED_NOT_DEPLOYED`，不能直接当作原生产修复或给未知supervisor/reader签PASS。
**生产GLOBAL_STOP及实际supervisor/reader仍UNVERIFIED**。如无法在新隔离run建立可靠的本任务本地STOP、append/checkpoint和进程回收保证，则`STOP_RUNNER_SAFETY_UNVERIFIED`，HA预算实际使用0；禁止用切换账号、SSH、代理或更改原生产安全机制绕过。先用不含HA的轻量stub确定性测试确认“上限20、10轮决策、错误后不再新扣账、STOP后不得继续、保护身份”；工程资格PASS后才允许新真实科学调用。此资格只管新scratch合作执行者，不冒称生产GLOBAL_STOP已修复。

## 3. 唯一科学预算与10→20有界门
只有**一组N050 ARM**，从原始冻结双省状态开始、无中途再初始化。第1至10轮完整外层，若HA返回仍有有限终态但`converged=False`，按原TEMP历史处理，只真实记录，不为了续轮给它写PASS，也不额外新增Bellman正式硬门。真正非有限/异常、不可用KFE质量/状态、安全STOP/E2、预算/来源异常必须立刻STOP，并保存所有完整轮次。失败轮不可计完整，已启动HA计费不可撤销。每轮最多两省各一次HA；总外层≤20，每省≤20，总HA/HJB启动≤40，KFE进入≤40（HJB严谨状态允许时）、science driver≤1，不可任何额外HA预检/重跑/参数补试。原每HA的HJB update≤100、每HA标量root≤400000、总root≤16000000；每个调用的真实计数由运行器记录，超过硬STOP；不给旧science预算续命。
到第10轮，若不足10个完整轮因为硬失败/危险状态，立即结束。10轮全部完整时，比较每轮`max KN_gap`和`max Y_gap`：第8—10轮各自均值均≥第1—3轮对应均值的1.2倍（基准均值必须>0，数据全有限），**且**第6—10轮至少4轮两个省份均出现任一企业raw工资/回报超过真实clip区间，定为`EARLY_STOP_OBVIOUS_WORSENING_10`。如10轮已达到原冻结TEMP外层收敛条件也可以提前终止但不得把短期观察升级正式V010稳态；遇硬失败随时STOP。否则分类`TREND_NOT_OBVIOUS_AT_10`，只有剩余预算、安全/有效状态全部成立时，在**同一科学进程/同一累计ledger**继续11—20轮；不自动寻找第二组N、不重启失败ARM、不改阈值。早停规则只是节省预算的预定义描述门，不能用它证明经济学全局收敛或根因。

## 4. 不可省略的逐省逐轮价格表与区间趋势
必须交付**省×完整轮** CSV及 Markdown聚合，两省分别统计：
A. `ra0_raw, ra_used, ramin,ramax, wjt_raw_wt0, wjt_used,wjtmin,wjtmax,rk,divrate`，以及家户使用的`rah`、工资`wt/w/w_eff`按真实变量名/来源/单位/时点精确映射。企业raw越界定义`raw>upper`或`raw<lower`，used恰等边界**不能单独证明**触界；raw=边界另列`AT_BOUNDARY_EXACT`。对`rah`和家庭工资只在确证同量纲/同边界规则时记录实际bound事件，否则仅提供`REFERENCE_BAND_ABOVE/BELOW/INSIDE/NOT_COMPARABLE`，严禁称家庭字段实际clip。
B. 每省上界和下界事件次数、有效轮数分母、百分比、首次事件轮、每轮到上下界的原始距离、最早连续触界区间、由INSIDE转OUTSIDE的轮、是否一开始就触界、曾经回归INSIDE及再次触界（RECURRENT）；报告首轮、第5、第10、第15/20（存在时）及首次触界等关键点。分母未完成轮另报失败/缺失原因，绝不默认当0；按省分别给10轮阶段与全部已完成轮的统计，不能用全国平均掩盖差异。
C. 每省逐轮`KN_gap,Y_gap, HA.converged/HJB具体终态/KFE质量及资产/劳动有效性`，标实际是否触达GovInv/Zt原适应律及生效于哪一轮；所有异常、预算与停止事件真实编号。
趋势结论只能是`OBSERVED_EARLY_HIT`、`LATE_HIT`、`PERSISTENT`、`RECURRENT`、`NEVER_HIT`、`INDETERMINATE`，并给起止轮证据，不臆测定律。

## 5. 家企投入、量纲与来源对照表
第二份**省×完整轮** CSV及 Markdown summary逐一显示企业`Zt,alpha,mt,Kt,Kprivate, GovInv,Lt_firm,Yt,Kt/Lt`，家户`N,At_per_person, N*At, household labor supply raw(per_person)/N-scaled(total), rah, household wage`，`Lt_mat[j,i]`目的地×来源跨省桥以及`firm_Lt - destination_Lt_mat_sum`、`Kt-Kprivate-GovInv`残差和same-S资本守恒。原MATLAB`HANK_mp_1turn.m`里企业`Lt=Lt_supply`，家庭`At`为人均资产；`Lst`不是已核实的原MATLAB标准字段：必须通过真实执行源码+时点+单位证据归属`Lst/Lt_HA/Lt_supply`，无法归属记`UNMAPPED_HOUSEHOLD_LABOR_SUPPLY`，不伪造列/把企业Lt直接冒充家户劳动。期初/期末及同轮对齐保留。指标数值不全时逐格写NA+原因并停止涉及该缺字段的结论，**不能**为齐表修改经济公式。
在报告中注明理论方向（其他条件固定，K/L↑一般工资↑、资本边际回报↓，Z↑一般两者↑）只是条件比较；本轮N同时影响N*At与劳动，总K/L可双向变化，不以经验规律替代真正观测。要附原MATLAB POP×100,GDP/CAP×1000 与实际synthetic N=100/160的单位对照说明。

## 6. 限域资源/公开证据/回执
本任务单次独立预算：wall≤21600秒，验证/准备≤2400、工程≤3600、科学≤14220、交付≤1200、终封存预留180（总计21600，所有阶段硬上限）；工程Python starts≤12、直接进程≤50、E1≤2批仅格式/确定性非科学bug，成功公开发布≤1、Git Data API mutations≤8，独立science driver≤1，HA/HJB≤40、KFE≤40、总20轮。新scratch原始证据≤256MiB，Git review三个公开脱敏原件总≤2MiB且ZIP展开≤4MiB/≤32成员；所有新预算启动前先计账。若极端每轮时长触墙，保留真正完成的轮次并合法STOP，不强行补20。
Codex**自动**上传至独立GitHub Review分支 `review/ch5-temp-n050-price-boundary-10-20-20261022` 的临时目录 `_review_tmp/ch5/temp-n050-price-boundary-10-20-20261022/` **恰三件** `result.md`、`manifest.json`、`evidence_sanitized.zip`，review sole parent固定`cc8616038c595c302915b736e2f356cef46bc695`（不是issue/release commit），不force；必须有每个来源/派生列身份、CSV两套、Markdown每省表、逐轮真实字段映射/测试源码/10轮决策原件、价格阈值、完整本轮budget/status/first-error，脱敏后ZIP逐成员CRC/length/SHA；远端commit/tree/sole parent/三个Git Blob/原字节hash和ZIP独立readback，不能仅报告本地路径。可能的原私有状态、内部完整HA arrays与本地绝对路径不公开；不因脚本可读而泄露凭据。
Astra先独立审阅再永久归档remote readback，后普通非强制只删除本轮白名单三文件；任何`REVIEW_PENDING_IO`保留candidate。本轮之前B-only review `f8db0251fb98f2b157affc9bf7391895b86edba0` 与旧`4e05976bbc8068b971ba5915133e9a6c3b73193d`/`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c` **全部只读保留**；上一B-only限域审查仅本地PASS，GitHub归档/cleanup受平台安全检查拦截，不能偷偷篡改为已闭环。遇平台拒绝即STOP，不切换账号/SSH代理绕过。
最终原始JSON Base64、字节长度SHA256、run_id、actual_terminal、完成事件（外部进程退出后）按实际支持通道交付；科学失败和交付失败分账。完成后必须`WAIT_ASTRA_AND_OWNER_PARAMETER_DISCUSSION`，**绝不能自动发下一组N/生产率/价格边界参数任务**；直到Owner看过表、同意下一参数后才可发单。正式V010、旧100轮、真实31省、GE/IRF调用=0，`model_activation=False,REAL_GE=False,Results=FALSE,V011=NOT_STARTED`。
