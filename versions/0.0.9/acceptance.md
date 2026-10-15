# V0.0.9 最终独立验收：φ方案B已实现；首次人工完整HANK稳态未取得

日期：2026-10-15（Asia/Shanghai）

**Terminal:** `CLOSED__LIMITED_ACCEPT__V009_PHI_B_CODE_AND_REPORTED_SCIENCE_STOP_ONLY__NO_SYNTHETIC_HANK_STEADY_STATE__WITH_OBSERVATIONS`.

本版接受的范围只包括固定φ方案B的源代码实现、人工独立数学oracle的可核设计、HJB/KFE与宏观求解接口的可审实现，以及**耗尽单省硬额度后正确停止和明确披露科学失败**。**不接受任何完整单省/双省两资产HANK稳态、真实31省GE或动态IRF。** 持久回执的Windows实际数值属于 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，而不是Astra已经独立复跑科学模型。

## 1. GitHub身份、执行和冻结边界

- Owner已单独采纳φ相对人均GDP方案B：[CES φ补充冻结](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/c4fe97b4bc3510c42683579ff1aa7edd1df27807/versions/0.0.9/ces_phi_supplement.md) `c4fe97b4bc3510c42683579ff1aa7edd1df27807`，blob `1c9839fe639197176d0d8b1c981b4c13025dcd5a`；[独立剩余额度授权](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/5e32c112fed5dd096540061da3c918b0d924520b/versions/0.0.9/ces_phi_resume_authorization.md) `5e32c112fed5dd096540061da3c918b0d924520b`，blob `76616b2bef739a2119c510475f786d4134a7f5e6`。原V009冻结plan blob `cb76a840fdd9d1756728189bf29518679831aba6`未变。
- 候选 [`e25f8e22490dddf57568e14aec2819d52603a78f`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/e25f8e22490dddf57568e14aec2819d52603a78f)，独立从GitHub Git对象查得 tree `4b161428470e4bc8070ed4ec4010a0ea08f9695a`，唯一parent `d41d229b681e09b913c21deff7a057085b9bc419`。候选分支 `codex/ch5-v009-phi-b-resume-20261015` 正确指向候选，相对基线**仅13份新增白名单文件**，1 ahead/0 behind，未合并main。之前 PRE-PHI 候选 `18256cd70b827e133e52d7609746c8afadb63ac1` 是兄弟候选，未重写、未force。
- 与PRE-PHI候选逐一核Git blob：`household.py`、`stationary_kfe.py`、`accounts.py`、三个旧toy测试等代码字节未变；`contracts.py`增补φ与账本I/O修复、`stationary.py`增补预注册源身份，`test_v009_stationary_acceptance.py`新增φ和账本保护oracle。不能据这些静态身份声称最终Windows pytest由Astra运行。
- GitHub无独立CI status checks；候选三份 `versions/0.0.9/`文档与JSON均明确 `PRE_SEAL`，新科学结果存候选外 [本地最终回执](D:/ProjectTemp/ch5_v009_hank_20261015_01/receipts/FINAL_DELIVERY_PHI_B.json)（仅由Codex给出，不能把D盘链接当GitHub可见的证据），报告SHA256 `E75E4C1B4434AB8D3850114B0F6329C46B54C08DA21E8D9E90EF9860C6FF3D79`，本轮Astra无法独立开读或复算这些最终实际科学数组。
- 用户报告：最终封存视图 `15 passed`、pytest累计7/8，源候选的精确测试文本已由Astra读取，表现为φ行列/固定外生GDP、CES对偶、3态toy KFE、拒绝门和固定S再配置R的真实数学oracle。这**不等于真实800-state家庭/宏观稳态PASS**。

## 2. 条件家庭解与经济失败分账

Codex终交回报：五个完整宏观价格点评估各自运行内生家庭HJB及最终Q唯一闭类KFE；HJB同check-point最大Bellman`3.373e-11`、value change`3.372e-8`，满足原B≤1e−8/D≤1e−7；KFE报告五个均只有一个34-state闭类、restricted GESVD rank33/nullity1、最大stationary `1.388e-16`、上边界质量0。这些**是Codex本地计算声明**；GitHub的PRE_SEAL机器摘要只覆盖了首次I/O中断过程，不包含最终五个价格点的全部新数值，不能伪称独立浏览器已看完整原证。
- 五个合格家庭的私有基金权益均值 `A=0`。在人工网格`a>=0`、KFE`p>=0`、概率质量1成立的条件下，`E[a]=0`意味着KFE正支持必位于`a=0`面。原人工非退化`A>0`和私人资本市场共同出清硬门失败；这不证明**所有可能价格下**私人资产供给为0或HANK均衡不存在。
- 用户给出的初始宏观价格点残差（源数值未作Astra科学重算）：工资FOC 0.56867045、资本FOC −0.78852838、债券市场0.00834925、财政−0.00977005、资源−0.42351713，显著非零，因此既不是完整均衡，也不能用“家庭HJB/KFE局部PASS”提升GE结论。

## 3. 本次Astra独立源码发现：第六次评估是未接受Newton试探步

在 [`reconciled_hank/stationary.py`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/e25f8e22490dddf57568e14aec2819d52603a78f/src/ch5_two_asset_hank/reconciled_hank/stationary.py)，1省有`(log w,r,r_b,T)`四个宏观未知；第一次evaluate(x)是评估1，有限差分Jacobian循环依次四次`pert=evaluate(trial)`是评估2–5，接下来的首个`candidate=evaluate(x+delta)`是评估6（`power=0`完整Newton步），**尚未被line search接受**。
用户说明首次driver因持久账本I/O中断，第二次driver五个完整+第六个不可行，因此原候选顺序表明最终`NO_ADMISSIBLE_POLICY`出现在**初个完整Newton候选试探点**。源码现行`candidate=evaluate(trial)`异常直接传播，不把有明确定义的非可行trial视作拒绝并尝试较小阻尼；这是一种**未来可能需独立审议的可行域感知宏观line search**，不能在V009原冻结“无可行控制必须STOP”条款下未经新科学批准自行修改、重试或恢复耗尽的预算。
- 报告失败标签`h7_f179`，在`20×20×2` b-fast F-order中 flat179 = (b索引19，a索引8，z索引0)，即**流动资产上界b=2、非流动资产内部a=2.1052631579、低效率z=.8**。HJB到checkpoint3最近完整`B=69.0713841, D=36.6341509`远未收敛，KFE未启动。该单个候选动作拒绝既不认证大样本科学bug，也不证明已接受价格点的家户根本无可行政策。
- **单省`phi11=1`与中性方案完全相同**；GDP相对差`phi[1][0]=.9,\phi[0][1]=1.1`只存在于未运行的2省。故本次单省失败**不能被归因为Owner坚持的跨省φ方案B**，也不能用它作为放弃内生劳动偏好机制的理由。

## 4. 完整累计保护与资源等级

用户报告最终V009累计：
- 7/8 pytest，2/4 science drivers；macro总2/4且1省2/2**耗尽**；残差评估attempted7、completed5。
- Household7/176（完整5，失败/中断2）；HJB直接更新55；policy/Q映射62 attempted/60 completed；selector48,783、scalar-root21,222，合计70,005；完整家庭SCC/GESVD/Q^Tp各5；toy累计SCC12/GESVD6/Q^Tp6；约90.7分钟；新增存储29.7MiB，采样峰值72.9MiB。
- 前一次driver的`os.replace`私有账本共享权限错误已经保留原两份持久快照、选择较高count并在已冻结普通工程修复范围内变更账本持久化，消耗剩下的第二次单省macro attempt。不能把工程错误漏账、成功回复或中间树结果当科学结果。
- 原模型8个dirty跟踪文件/index前后SHA256一致、HEAD和branch未变、untracked/ignored未重扫、本机未触C8/B3由Codex `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`陈述；GitHub可以独立证候选只加13文件，无法认证D盘整盘保护或科学日志原始字节。
- **V009单省完整root2/2和该冻结任务均已终止，不应自动动用余下2省预算，因为Gate B未通过；本版未使用额度不是下版的免费科学执行权限**。原科学跑次冻结计划保留不改。

## 5. 独立最终裁决与下一步

**`CLOSED__LIMITED_ACCEPT__V009_PHI_B_CODE_AND_REPORTED_SCIENCE_STOP_ONLY__NO_SYNTHETIC_HANK_STEADY_STATE__WITH_OBSERVATIONS`**。φ方案B的精确编码与科学stop证据有限接受；`SYNTHETIC_TWO_ASSET_HANK_ONE_PROVINCE_STATIONARY_ACCEPTED=FALSE`、2省`NOT_RUN__GATE_B_FAILED`、`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`，旧真实31省HANK/政策反事实/Results为FALSE。
下一版本优先**不调用任何模型**、不提早改变φ/宏观人工参数：针对已保存V009私人合成回执/五组宏观解/价差/Jacobian/质量支持和拒绝候选，一次SOURCE_ONLY复核首次Newton未接受试探、私人a=0闭类机制与是否数值可行性域问题。调查期间不能临时重写V009冻结plan或重新开science root；任何新的科学求根方法、主动trial-rejection规则/经济假设或额度，须Owner另行决定、正式冻结和独立授权。
继续A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE，原真实C8 A–D REQUEST_ONLY，V0.0.11 NOT_STARTED。工作流V1.2和Owner连续立版委托未改变。
