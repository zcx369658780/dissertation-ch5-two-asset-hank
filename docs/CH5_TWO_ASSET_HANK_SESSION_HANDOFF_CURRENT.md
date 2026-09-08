# Chapter 5 当前交接
更新：2026-09-08。唯一仓库：zcx369658780/dissertation-ch5-two-asset-hank。
Owner最终科学authority；ChatGPT Reviewer/路线协调者/GitHub任务发布者；Codex bounded Builder。持续授权保留，普通对话不自动启动本地模型，不修改provider，不混入deep-learning-hank或Zotero。

## 恢复与当前执行状态
先fresh读live main、AGENTS、规则索引、当前状态及exact task。最新接受candidate：9d76747f48858a3e9289de8f284fffbc49aaedce；本次任务发布前main为062cd3b715e9aed85e7c068063d6a099b2e30186，不假定检查点永远最新。
状态：OWNER_APPROVED_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_ACTIVE。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY.md。
Owner已明确批准紧接前次建议的独立单户.07实验，无需再次确认。任务已发布但本交接未收到执行报告；不要宣称已运行。
原参数prefix task已完成并接受，不重复725次前缀、年度触界表或历史HJB比较。验收：docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_ACCEPTANCE.md；报告同前缀_REPORT.md；摘要reports/2018_observable_prefix_replay_20260908/。

## 本次批准的具体事项与预算
独立Python安徽call725输入副本仅改rah .09→float('0.07')；对应HouseholdInputs.r_a从此字段绑定，其余输入/网格/a_bar/原算法/HJB100步规则不变。完整状态diff只允许rah，保持生产ramax和carried firm ra不变。按原生算法一次生成.07的V0/l0；.09保存数组仅作基线比较，不作warm start。
从前缀capture/call_0725原始对象读取输入，不从聊天近似数重建，不使用后来的MATLAB共同初始化MAT。复用保存的.09 HJB100 false/KFE非有限基线，新.09调用0。
一份task整合输入绑定、实现、相关合成测试、一次有限求解和报告。新科学上限：一个Python进程/worker，一次初始化（最多800原劳动根）、一次HJB（最多100次更新/直接求解）、自然到达时一次原KFE及聚合。原adapter在HJB正常false后仍进入KFE；异常停止，不加fallback。科学开始后不重启；只有有证据的零科学进入启动失败可按task至多重试一次。科学15分钟/全任务90分钟。MATLAB、其他利率点、基线重跑、firm/GE/年度/动态/IRF/Results全部0。
优先显式导入已认证的只读LF source_runtime；预先核验raw/LF身份，不因CRLF再次盲目启动，不改bootstrap expected hash或全局配置。只有相关源未变才可复用，不必重哈希历史13800引用。
该实验包含原初始化随rah变化的求解链敏感性，不是固定初值纯效应，也不是生产替换或.07安全定理。D1–D3未采纳/未实施。不同价格输出不能按同输入parity要求相等；HJB、KFE返回、分布与生成算子有效性分开报告。

## 最新已接受事实
725入口×11连续字段的新旧误差全0，历史HJB停止量和44控制器标量比较通过；仅已比较对象匹配，不证明全部旧内部数组同一性。
24份完整31省共同旧状态，725实际家户入口，713firm返回、23全国controller记录。call725原生初始化HJB100步false、统计量.3038218386543494，原adapter继续KFE并复现non-finite异常，raw线性返回已保存但无有效KFE/aggregate；无call726。
安徽turn22 raw ra0=.21979491622969854，turn23=.21906938941252802；turn23 wt0=2.5772708754207905，截断ra=.09/wjt=1.3。rk=.244069389412528，delta=.025，PIt截零、divrate0；mt=.9943859584740543。高raw不是家户直接接到21.9%的收益率。
turn23贵州决定maxKNgap=.04124871080231385，门打开；安徽Zt下调，GovInv*1.1真实发生。raw从turn5约.53423降至turn23约.21907仍在clip上方，存储ra不变不代表未调整。第23轮全国24省ra触上界；工资19上界/5下界/7内部，不是安徽孤立现象。
安徽外省权重0，turn23组合使用turn22 ra，之后才新firm及适应，call725的rah=.09沿此时序形成。全部同阶段价格/mt/税/劳动对象/资本身份4278项报告通过。原household Lt_prev与firm Lt_supply、firm-used与post-adaptation Zt/GovInv必须分开。

## 前缀实际预算与验收局限
前缀Builder一次Python科学进程；另一次CRLF bootstrap失败科学进入0，同HEAD隔离LF工作树后消耗其唯一launch retry，科学后重启0。科学2874.297秒。
HJB/KFE各725、HJB直接求解19961、KFE直接求解725/成功724；native labor roots580000（其中brentq同数，为嵌套），残差评估4837970；one-turn23/firm713/controller23。MATLAB/独立诊断求解/其他年度/动态/IRF/Results0。上述为历史预算，非本任务新预算。
Reviewer此前为L3提交/代码/报告与L4发布日志审阅，没有独立运行15测试/模型、直接读Windows全部capture或重新核验13800引用。manifest_02 SHA256：4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146，Builder回执13800引用/13696capture文件/8321索引条目。旧capture-time hash gap及历史环境不完整保持原限定，早期工程失败保留。本次发布未新增科学调用。

## 尚未接受范围
精确共同MAT初始化MATLAB143/Python500、终点18负元/15泄漏、P32巨大transfer/cost和sigma丢失未解决；不与原生100步失败混为同一实验。首轮53/53、固定线性及边界提案等历史接受仅保留原范围。
旧runtime-cache15/15年与Owner-A13/14年PASS分开，2018修正覆盖仍未接受。原价格审计PARTIAL_EVIDENCE保留，已排除audit-001错误派生。Results eligibility=FALSE，不把顺序比较静态叫真正IRF。

## 本地与文件保护
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原D:\ResearchCode\dissertation-ch5-two-asset-hank及70未跟踪文件保留。保护MATLAB根D:\MatlabProgram\2023年12月2日 多省份神经网络HANK只读。
前缀证据根D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001，包括source_runtime LF工作树、manifest及失败/成功启动回执，均保留。
本次新分支codex/ch5-call725-rah-0p07-native-init-20260908，新证据D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-001（占用则fresh suffix）。不得reset/clean/stash/force-push或覆盖旧证据。Builder完成后非force推送，Reviewer验收，不自行合并main或追加实验。输入/源身份详见task与当前状态。
