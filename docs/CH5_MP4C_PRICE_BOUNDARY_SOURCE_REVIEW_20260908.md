# MP4C 省份价格边界：Owner 原版压缩包静态复核

日期：2026-09-08。Reviewer：ChatGPT。仓库：zcx369658780/dissertation-ch5-two-asset-hank。
读取时 live main：da543d7960451da5b2ed9f67dae906269d45b273。

## 证据范围
本会话实际读取 Owner 上传的 多省份HANK_matlab原版程序.zip，SHA256：
CEB94CCF34D2D218722B81E5111A8F4C530571A9F886BD4AFE0610A00321F755。
归档含32个.m文件及一个数据估计结果_1000_100_0.mat，没有Multi_Province_12sts_<year>.mat年度稳态文件。32/32个.m逐文件SHA256均与项目源中的MP0来源审计表相同；校准MAT的SHA256也与已指定runtime cache相同：923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A。
这证明上传字节与已记录来源身份一致，不是本会话重读了Windows保护根或复验了历史年度结果。未执行归档内任何程序，也未据此计算新的省份状态。

实际阅读了入口、初始化、外层控制器、one-turn、厂商、工资聚合和HJB价格绑定的相关源段，并读取main的Python firm/capital_allocation/steady_state及年度诊断报告。未独立读取Windows年度MAT、2018轨迹或call-725大数组；后者由新Builder任务进行保存证据审计。

## 关键源身份
| 文件 | SHA256 | 重点源行 |
| --- | --- | --- |
| multi_prov_HANK_12sts.m | 3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97 | 49-55边界；85-94初始化；118-135缓存分支 |
| mpHANK_equilibrium_2000.m | 26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5 | 22-50数据初值/国资/跨省比例；72外层入口 |
| HANK_mp_1eq.m | ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF | 14-22触界统计；31-55收敛与自适应 |
| HANK_mp_1turn.m | D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF | 15旧状态家户；29-40资本/rah；45-52新厂商/工资 |
| HANK_firm.m | EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5 | 9-17投入；30-54原始价格；57-74截断 |
| wage_caculate.m | 0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63 | 7-11跨省综合工资 |
| HANK_2ASSETS_HJB.m | 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE | 26-31实际家户价格输入 |

## 1. 先区分三个阶段，不能把触界等同越界
入口的有效值为ramin=.02、ramax=.09、wjtmin=.8、wjtmax=1.3。被注释的.065等不生效。
厂商先算原始ra0与wt0，再分别写成有界ra与wjt，并把超额/不足部分计入Corptax调整。因而只检查存储ra/wjt是否严格超过边界可能漏掉所有被截断的原始异常；但恰好等于边界也不独自证明原值严格越界。
家户实际读取的是rah与w；它们不是ra与wjt的别名。rah由跨省投资公式生成，w由工资/迁移/偏好聚合生成。不能用wjtmax=1.3判定w=16.82014806560587越界；不能把厂商ra的clip直接假定为家户rah的硬约束。

## 2. .07确实出现在原自适应机制，但它约束的是ra触发条件
HANK_mp_1eq.m:47-55仅在maxKNratiogap<.1且steady_state==1时进入参数调整。其后：
- 产出偏离目标超过1%时更新Zt；
- ra<ramin+.02时，GovInv乘.9；
- ra>ramax-.02时，GovInv乘1.1。
在当前边界下后两个阈值约为.04和.07，且是严格不等式。高ra方向的源码行为是增加国有资本，不是减少。当前Python steady_state._adapt保留了这一方向和全局开关。
这是源码证据，不是对Owner“rah在.07附近稳定”的经验回忆做了数值验证。任何后续触界分析都应保存实际阈值表达式，不能把经验值改成新的停止或安全标准。

## 3. “为什么没有调回来”需要全局开关与时序证据
maxKNratiogap是全国最大值，不是高收益率省份自己的误差。别的省份未进入近收敛区间，可能使高收益率省份也无法进行国资/生产率调整。另一方面，家户/KFE异常若中断one-turn，则本轮后续厂商计算和自适应步骤不能完成。这两种机制都值得查，但目前没有读取失败外层轨迹，尚不能断言哪一种已经发生。
原代码已有ra/wjt的上、下界省份计数；逐省名称的打印行被注释。最终收敛条件要求ra上下界计数均为0，却不要求wjt上下界计数为0。因此原来的SOURCE_CONVERGED标志不独自排除工资触界。

## 4. 初始化、缓存和rah滞后不能混为错误
入口初值ra=rah=.09，wjt=.6，w=20。初始wjt低于厂商下界是源码本来设置的猜测，不能当作截断器失效；但应检查后续是否长期停留异常区域。
若年度st存在，入口直接读取缓存，其内实际参数/边界不能用入口默认设置覆盖。
one-turn先计算家户，再由保留下来的旧ra生成下一轮rah，之后才更新厂商ra。因此保存状态中的rah和同一状态的新ra不是同一生成时点。必须按这条滞后关系追溯安徽输入，不能从单个终点重新聚合就判定实现错误。

## 5. 上游假说与分解式
源码厂商使用Kt=Kt_supply+GovInv，Lt=Lt_supply，Yt=Zt*Kt^alpha*Lt^(1-alpha)，并计算：
wt0=mt*(1-alpha)*Zt*(Kt/Lt)^alpha；
rk=mt*alpha/(Kt/Yt)；
PIt=max((1-mt)*Yt-(theta/2)*pit^2*Yt,0)；
ra0=rk-delta+PIt*(1-corptau)/Kt。
因此Owner提出的Zt较高或资本相对不足，与源码价格表达式相容，但mt、利润截断、折旧、跨省权重和自适应时序也可能影响结果。应提取同阶段的Zt、Y/K、Kt、GovInv、Lt_supply、mt及divrate，而不是只看最终rah。
上传源码的Kt_supply表达式仅为源码规定的跨省项；本次不擅自补入本地留存资本项，也不重写rah的比例位置。可能的公式/数据问题先如实记录，与当前已指定输入口径分开讨论。

## 路线决定
Owner要求暂保留原算法及a_bar，先查各省rah/wjt触界。新任务：tasks/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT.md。
任务新增科学调用预算为0：只读保存状态，区分原始越界/截断触界/实际家户输入，检查自适应行为。之前D1-D3修复target未采纳、未实施，暂缓；已确认的边界/算子异常证据不撤销。任务发布并不表示已启动本地Codex，也不表示已完成各省数值清点。
