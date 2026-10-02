# 独立回溯数据适配器交付

日期：2026-09-30。Owner已采纳2018回溯诊断/2017修订观测、仅劳动系数数据来源更新，不全量重校准。

## 本轮完成

在本独立证据目录创建`adapter.py`，不修改任何现有src/tests或求解器。标准库适配器读取确切audit JSON与期望SHA256，验证完整31省×4年数据覆盖、唯一键、正有限数值和显式年份；按31项(index,source_name)准确重排，返回冻结的31项2017 GDP/年末人口记录及来源元数据。没有计算q或phi。

`readback.py`核对原面板中的2017省份标识映射与候选常量完全一致，再读取本次已审查audit快照。北京输出GDP31325.9亿元、人口2194万人。31省均进入2017观察年/2018目标年的独立数据对象。保留来源显示值/DOM哈希及采集时间，版本为retrospective_revised，价格绑定未决，price_verified=False、model_activation=False、release_date=None。

## 执行证据

- 虚构fixture测试仅一次：bundled Python `-B test_adapter.py`，10项PASS，exit0。覆盖选年、单位原值、轴重排、不可变对象、hash错配、重复/缺失记录、错年/bool、错index/name、非法数值及缺失/激活来源元数据。
- 真实数据readback仅一次：bundled Python `-B readback.py`，31省、轴一致、输入hash保护PASS、exit0。完整结果与候选hash在`readback_receipt.json`。
- 原数据、修订artifact和七项受保护manifest/readback、原integration、Owner AGENTS核对前后字节一致。
- 当前模型/科学调用、校准、helper重测、实际q/phi矩阵和现有源集成均为0。原C9账本仍为CALL_LEDGER_UNRESOLVED，不能将其改记为0。
- 不stage/commit/push，不访问禁止仓库；原有文件与Owner改动保留。

## 实际限制

这是独立未接入的数据候选，不是模型adapter已生产激活。`InactiveSnapshot`不转换为helper的`GDPRecord/ProvenanceBinding`，未调用helper。调用方提供的期望audit哈希必须来自已采纳来源合同；任意自算哈希只能证明自身字节一致，不能证明来源权威。当前真实调用使用独立已审查artifact_receipt绑定的hash。

适配器携带显示值文件哈希，不自行访问或重新抓取网页；本次快照与页面DOM的一致性由前轮独立数据审查提供。实际metadata价格绑定和目标年消费者接入仍需后续精确任务，不能以fixture PASS解除该限制。

独立工程结论见`independent_review.md`；该结论不等于科学有效性或收敛结论。C9暂停、Objective A保留、两次尝试已消耗、Results eligibility FALSE。
