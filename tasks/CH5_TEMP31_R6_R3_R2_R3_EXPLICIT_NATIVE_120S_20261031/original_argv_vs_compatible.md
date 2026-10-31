# Frozen compatible argv semantics

Reference: fixed R6-R3-R1 source Blob2aa98c299cfa5b3a4f4866a0bb599ec29cd6fa3b; new actual argv is retained LOCAL_ONLY and projected in pre_execution_source_job_gates.json.

| Token role | R6-R3-R1 frozen source | This actual run | Delta |
|---|---|---|---|
| executable | fixed authenticated MATLAB executable | same SHA2564d251e680b8409d76d0524a1eb716de3c9e747386d3101e10f6ce1405ad1a59d | no executable identity change |
| desktop | -nodesktop | -nodesktop | none |
| splash | -nosplash | -nosplash | none |
| thread | -singleCompThread | -singleCompThread | none |
| logfile flag | -logfile | -logfile | none |
| logfile value | previous task-local log | new task-local isolated log | required fresh path |
| batch flag | -batch | -batch | none |
| batch payload | run(previous isolated probe) | run(this fixed isolated probe) | new task/probe/run token |
| -nojvm | already absent in compatible reference | absent | remains excluded for Windows R2022b |

Thread-limit keys remain1, MATLABPATH remains empty, Python environment sanitization matches the frozen reference, and MATLAB_PREFDIR is the new child-only directory. Parent/system/user environments are unchanged. No license/account/permission option was added. Native window is120 seconds rather than30; current process exited abnormally before30. New directory, new run token and explicit validated entry are declared isolation differences. No single-variable historical causal inference is made.
