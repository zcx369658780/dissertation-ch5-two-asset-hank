# 三阶段、四个测量点的保护矩阵

|阶段/测量点|status SHA-256|NUL记录数|证据性质|是否本轮采纳为可信基线|
|---|---|---|---|---|
|历史旧保护基线|c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3|5971（冻结任务/前次独立报告所记）|旧原始流未获准取得，不能本轮复算|NO；保留旧记录|
|历史恢复状态|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（既有记录）|既有执行者差异JSON，非新基线授权|NO|
|本次诊断BEFORE|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（实测）|原始NUL流本地测量，私有保存|NO|
|本次诊断AFTER|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（实测）|诊断安全STOP时第二次快照|NO|

BEFORE UTC=2026-10-27T23:13:56.654405+00:00；北京时间=2026-10-28T07:13:56.654405+08:00。AFTER UTC=2026-10-27T23:16:43.124521+00:00；北京时间=2026-10-28T07:16:43.124521+08:00。

两次HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e；branch=codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922；index SHA=28058a7e2d9ab773c5813205c75999e6c221533aeae0b9bb094b9a83451bf7cc；refs SHA=600912e7f3dabd0661d2314f533bb432d95cf4bd35b622ab5b16d6149e3c6729、count=243。11件资产两次原字节size/SHA一致，并匹配既有执行者保护上下文的预期身份；该预期不冒充本轮新授权基线。完整保护测量与公开资产别名见source_inventory.json。

捕获模式：`git --no-optional-locks -C SCIENCE_TREE status --porcelain=v1 -z --untracked-files=all`，原始字节SHA-256与非空NUL记录计数；refs用`for-each-ref --format=%(refname) %(objectname)`的原始字节；index是`rev-parse --git-path index`所指既有文件原字节。无写index/refs。

诊断期间未见新的保护摘要差异；不得据此否认历史旧/恢复差异。第二次快照以后不再访问科研树；最终GitHub回读只验证证据分支，不能冒充第三次科研树测量。
