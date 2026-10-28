# 保护快照与基线

|测量点|status SHA-256|非空NUL记录|性质|
|---|---|---|---|
|历史旧|c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3|5971（既有记录）|本轮未重读旧流|
|既有恢复观察|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（既有记录）|未采纳为新可信基线|
|本次BEFORE|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|新测观察|
|本次AFTER|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|新测观察|

BEFORE UTC=2026-10-28T03:36:30.726384+00:00；北京时间=2026-10-28T11:36:30.726384+08:00。AFTER UTC=2026-10-28T03:42:39.425562+00:00；北京时间=2026-10-28T11:42:39.425562+08:00。

HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e；branch=codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922；index SHA=28058a7e2d9ab773c5813205c75999e6c221533aeae0b9bb094b9a83451bf7cc；refs SHA=600912e7f3dabd0661d2314f533bb432d95cf4bd35b622ab5b16d6149e3c6729，count=243。两次各11件保护资产bytes/SHA匹配既有执行者保护上下文；具体匿名身份见source_inventory。该预期不等于新基线授权。

采集模式：`git --no-optional-locks -C SCIENCE_TREE status --porcelain=v1 -z --untracked-files=all; refs raw for-each-ref --format=%(refname) %(objectname); raw index SHA256`。不公布原始状态流或其他未跟踪记录。两次保护快照预算已耗用，AFTER之后不再访问科研树；发布期只验证独立证据分支。P3正式批准，保护基线仍BLOCKED。
