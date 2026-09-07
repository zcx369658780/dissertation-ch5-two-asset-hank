# Chapter 5 当前交接
更新：2026-09-08。唯一仓库：zcx369658780/dissertation-ch5-two-asset-hank。
Owner最终科学authority；ChatGPT为Reviewer/路线协调者/GitHub任务发布者；本地Codex为bounded Builder。持续授权允许证据验收后纳入main及无实质科学选择时发布精确后继任务。普通对话发布不自动启动本地计算，不修改provider。

## 启动和当前任务
Fresh读取live main，再读AGENTS、规则索引、状态和exact task。发布前main为da543d7960451da5b2ed9f67dae906269d45b273，不能假定它仍最新。不要混入deep-learning-hank或从旧R5/R1A附件重启。
活动任务：tasks/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT.md。
状态：OWNER_DIRECTED_PRICE_BOUNDARY_AUDIT_ACTIVE__ORIGINAL_ALGORITHM_RETAINED。
本交接发布时尚未收到其Builder报告，不得说已完成各省清点。

## Owner新方向
Owner明确要求保留原算法及a_bar，认为rah=.09可能过高，记得稳定收敛时rah通常约.07，要求先查各省rah/wjt越界/触界，然后继续诊断。此前D1-D3修复target未采纳、未实施，暂缓，不再等待其采纳才允许价格审计；已确认边界/算子异常不撤销。
当前任务仅允许保存状态读取、原始价格与截断价格区分、时序和控制器分析、相关测试及报告。新增HJB/KFE/线性或根求解/one-turn/GE/annual/R-PLM/shock/IRF/Results预算均0。没有关键快照就如实报告缺口，不能重跑2018、改rah=.07或修改生产实现。

## 本次源证据
Reviewer实际读Owner上传zip；SHA256 CEB94CCF34D2D218722B81E5111A8F4C530571A9F886BD4AFE0610A00321F755。32个.m与MP0库存哈希全同；一个校准MAT同旧runtime cache；无年度st。不能假定ChatGPT附件已挂载到Windows，Builder可直接用已有hash-matched保护源码。
源码静态复核：docs/CH5_MP4C_PRICE_BOUNDARY_SOURCE_REVIEW_20260908.md。
关键：原始ra0/wt0先算再clip为ra/wjt；rah/w为另一层家户输入；rah用旧ra在新firm计算前生成。全国maxKNratiogap<.1时才开启自适应，高ra>.07附近触发GovInv*1.1，低ra<.04附近触发*.9。源码终止检查ra触界而不检查wjt触界。初始化ra=rah=.09、wjt=.6单独标识。事实是否发生在失败路径需要保存轨迹，尚未确认。

## 保留的历史诊断与限制
最新接受边界规格15f51be9733b5043e738d3e522b97554e95902b9：14/14快照预算/捕获漂移一致但存在上界向外漂移；相关验收和报告均在docs。Reviewer以前做L3提交审阅/L4已发布日志检查，未重算Windows数组。D1-D3是未采纳提案，不是实现结果。
首轮53/53，多轮共同初始化MATLAB143步收敛、Python500未收敛；M143终点18负元/15泄漏。P32极端transfer/cost和sigma丢失尚未解决。固定线性2ff3eb2已接受局部归因，不反复换solver/调容差/跑轨迹追求机器级PASS。
旧runtime-cache15/15年、465省年历史接受；Owner-A修正13/14年PASS而2018失败，必须分组。Results eligibility=FALSE；价格审计不自动建立因果、修复、年度或动态接受。
完整身份、预算、证据根及局限见当前状态和原报告，不重开已完成任务。

## 本地保护与交付
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001。原D:\ResearchCode\dissertation-ch5-two-asset-hank及报告中的70未跟踪文件保留；不reset/clean/stash/覆盖。保护MATLAB物理根D:\MatlabProgram\2023年12月2日 多省份神经网络HANK只读。
UI可仍为D:\Zotero-Analytical-Workflow，repo命令明确使用Chapter5目录；仍遵守平台/全局限制，不改Zotero或全局配置。
Builder完成任务内完整问题后按allowed paths提交并非force推送专用分支，Reviewer再读证据。后续受控实验/校准/算法选择需新明确授权。
