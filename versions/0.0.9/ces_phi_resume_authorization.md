# V0.0.9 CES方案B缺项修复：Astra独立签发剩余额度单次续跑许可

日期：2026-10-15（Asia/Shanghai）
**Authorization:** `ASTRA_APPROVED_EXECUTION__V009_CES_PHI_B__REMAINING_BUDGET_SINGLE_CONTINUATION`
**状态：`V009_CES_PHI_SCHEME_B_FROZEN_AND_SEPARATELY_AUTHORIZED__REMAINING_BUDGET_FULL_HANK_STATIONARY_RESUME__NO_RESULT_YET`。** 本单不是原冻结计划新版本、不是科研预算重新开放/重置、不是许可24×24/31省正式HANK/动态IRF/真实C8。

## 1. 固定来源与授权区间

- V009原正式freeze `f7caeb54b13ec977d1b503b124067ae522ca2433`，原plan blob `cb76a840fdd9d1756728189bf29518679831aba6`；原第一次授权 `5b4427ccc956b0189f4e0097d70862f0a29e743b` / `versions/0.0.9/authorization.md` blob `770a1fc304c3a602595e9d3d9d5ec21c2bdf1ee5`。
- Owner明确采纳保留GDP相对劳动偏好机制，唯一`phi`参数增补于`versions/0.0.9/ces_phi_supplement.md`，本轮**实际独立GitHub远端回读**commit `c4fe97b4bc3510c42683579ff1aa7edd1df27807`，tree `7a0301e7a5a77b827a28c51066d6c84e16c086d2`，supplement blob `1c9839fe639197176d0d8b1c981b4c13025dcd5a`；相对原治理HEAD恰修改6份来源/索引/科研文档，旧`plan.md` SHA始终不变。现单独签发的**本次许可**仅应用这份数值填补，不改变其它E1–E3参数、科学方程或原硬门。
- 科学代码baseline唯一`d41d229b681e09b913c21deff7a057085b9bc419`，PRE-PHI阻断候选`18256cd70b827e133e52d7609746c8afadb63ac1`永久保留供比对，不自接受、不重写Git历史。新候选需**唯一Git parent仍是baseline**、新的安全独立candidate分支；在原13个白名单源/测试/证据中精确修改`phi=None`、相应预注册、test/oracle和更新真实科学回执；原模型树/main/index/common-dir均不动。未经批准不得新增14th路径、checkout/reset/clean/stash/force push。

## 2. 补充参数与本次唯一权限

只给新 `SYNTHETIC_PILOT`：`pgdp_ref=(1.0,)`、`phi=((1.0,),)`（1省）；`pgdp_ref=(1.0,2.0)`、`phi=((1.0,1.1),(0.9,1.0))`（2省）。`phi[j][i]=1+.3*(pgdp_ref[i]-pgdp_ref[j])/(pgdp_ref[i]+pgdp_ref[j])`，目的行、来源列；无需填任何其它未冻结“便利参数”，`eta=1,nu=5,sigma=0,alpha/rho/delta/chi/S`等原数不改。
- 首次科学driver之前必须输出/固定人工配置的canonical hash，使用确切`phi`与`pgdp_ref`做前置静态算术oracle（双省`phi[1][0]=0.9`、`phi[0][1]=1.1`、单省1、CES dual/primal一致），拒绝方向反置和用内生`Y/N`更新权重，生产宏观求解不得包含旧MATLAB实际`Yt/Lt`反号。
- 此许可恢复**同一V009内尚未消费的Gate B单省完整人工HJB/KFE→宏观稳态**及其通过条件下的Gate C两省尝试；不是新科学实验支线。若单省HJB/KFE不能按原B/D、GESVD、边界和资源检查达到冻结标准，记录首次硬失败并`STOP`，**禁止再次重新选φ/GDP参考、网格/参数/方法或调松数值门槛**。

## 3. 继承真实剩余预算，不得归零

Codex原最终回执报告：pytest已经`4/8`，剩余≤4进程；完整科学driver`0/4`、完整macro root`0/4`、完整household HJB/KFE`0/176`。 toy/oracle已经发起selector约8、SCC约6、restricted gesvd约3、Q^Tp约3，必须按现有ledger真实类别记录，不得当成“0次科学计算”抹除。已经耗时约12.4分钟、产生约14.6MiB新存储，采样内存峰值71.8MiB仍属本版本累计账；新候选所需Git/view/回执/报告等新存储仍计入原≤256MiB及各子上限，旧候选不因不继续而删除/不计。
总科学硬顶保持：时间从本版实际第一操作至今累计≤8h、pytest≤8进程/各≤600秒、science driver≤4进程各≤2h；宏观1省≤2 root attempts各≤24残差eval、2省≤2各≤32、全部root≤4；household HJB/KFE≤176（每家庭≤100隐式HJB更新/≤101 policy Q/≤1 restricted terminal gesvd），sel/scalar≤400,000每家户与合计≤70,400,000，RAM采样达到512MiB阻止新科学进入、存储≤256MiB子项按原计划冻结；若原LOCAL_ONLY账与此报告数不同，以**保守实际较高消耗**为准。命令失败下游停，额度耗尽/不可靠时fail closed。
- 仅原`20×20×2` (b,a,z) 800状态；最终树复核也要占同一预算，缺final runtime证据只能标OBSERVATION；优先通过一次新科学运行与准确出清回执，而非把剩4次pytest都重复花在常规旧测试。
- 本轮许可能够修补旧候选经静态核已知的`phi`唯一缺口与同白名单聚焦oracle；若运行暴露新经济方程/目标冲突或需扩大原科学预算，不能用此许可自动修复新科学合同，保留未通过残差并报告Owner/Astra。

## 4. 零权限保持

原2017/2018/C8受保护真实原件stat/read/hash/parse、B3/A16/G0/敌对实验、C9/outer/旧生产HJB/KFE/历史数据、24×24与31省**完整HANK**、正式动态IRF与论文Results仍为0。旧`Results FALSE`、`model_activation=False`及A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、CALL_LEDGER_UNRESOLVED/C9 PAUSED不变。不得把当前Owner人工pGDP比1:2作为真实经济校准或扩展至2018现实GDP。

## 5. 集中交付

在原13白名单内交新单父候选commit/tree与精确GitHub changed-path比较、数值原始初值、完整HJB B/D、同Q KFE质量/唯一闭类、两资产内生聚合、各宏观出清及资源残差、原先toy和新科学进程/solver budget累计统计、被拒绝的参数变动或其它缺项、原dirty/index保护（外部LOCAL_ONLY如不能网页访问则声明为Codex回执）、正常non-force新分支push+readback。独立Astra验收之前不自称HANK稳态成功，也不开始V010。

**停止：`WAIT_ASTRA_V009_SYNTHETIC_HANK_NUMERICAL_ACCEPTANCE / STOP`。**
