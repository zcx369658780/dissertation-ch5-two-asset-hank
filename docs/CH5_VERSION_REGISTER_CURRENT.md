# 第五章版本登记（2026-10-16 Trusted Workstation Loader工程预检）

**CURRENT_VERSION=V010 / V0.0.10；V011 NOT_STARTED**。
**ACTIVE_TASK=V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT**。
**NEW_AUTHORITY=OWNER_TWO_BACKUP_SSH_TRUSTED_LOADER_ENGINEERING_ONLY**。
**SCIENTIFIC_NEW_PERMISSION=0；FULL_RUNNER_IO_CLOSURE=BLOCKED；Results FALSE**。

唯一冻结[VerifiedLoader工程任务](../versions/0.0.10/trusted_workstation_loader_engineering_preflight_task_20261016.md)，发行commit`01129efd5220683d415bd1486f23f6ecd068cb53`、tree`75ca195ecc41b8e6fbd7f43a090d22aa4f170dea`、Blob`1e6757fd235fd96d8b08130ca3fefb3b602c413c`。Owner风险决策[双备份＋SSH/Loader](CH5_OWNER_RISK_BACKUP_SSH_LOADER_DECISION_20261016.md)发行commit`e15b874b955883e754dee8b3e5543705ed0706a8`/Blob`7f1ee509d35343521e79e5df318aa164cd513261`：项目不保密，使用既有C盘物理独立SSD备份＋GitHub备份，不新建第三备份；Git连接用SSH key/443；可信工作站ENGINEERING_ONLY import隔离不强制Windows VM，不得据此认证native OS安全沙箱。Astra选双根身份+认证Loader，真实70源Blob装配、九源真实import唯一成功执行后认证，不做科学调用。

新工程Python进程≤6、真实runner≤2、每进程≤180s/总≤4h，新非Git产物≤32MiB、项目外独占bare Git审阅发布≤1.5GiB；所有旧科学pytest4/6、driver1/4、HA1/26、selector1626、roots1642与两次单点Python各1/1、第一次超额9965206B，以及前工程STOP剩余额度原样保留。模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，原V010科学plan`bf091da33d59293f147d52c11580327d3ac2a85d`/Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`不可变。原GovInv×0.9/1.1、目的地工资税一次、same-S/lagged raw ra0、原lagged-NKPC，corrected HA UNTESTED。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、real C8 REQUEST_ONLY、原8dirty/index/common-dir/历史失败、Results FALSE、V011 NOT_STARTED。
