# Native output and command visibility

The two exact original stdout/stderr files were independently re-read: each0 bytes, SHA256e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Their paths and receipt selectors are bound in evidence/original_raw_log_identities.json.

Controller107-111 creates separate inheritable output files, assigns them to STARTUPINFO with STARTF_USESTDHANDLES, and line116 asks CreateProcessW to inherit handles. Original receipt API success plus verified source supports intended capture. No independent observation proves MATLAB used/flushed these handles. The source uses no parent pipe read; the wait is file-existence and exit-status polling. A blocked pipe-drain explanation is not supported.

The source argv is configured-executable + -nojvm -nodesktop -nosplash -singleCompThread -batch run(ISOLATED_RECIPE). No shell or -logfile argument is present. The private runtime path and environment values were not semantically read; their task-internal config bytes were hash-checked only. Old static binary/version identity is executor evidence, not a current runtime observation. Direct application argument passing does not prove the configured binary has no internal launcher behavior.

No licensed-server, account, user path or private environment value is published. No independent license/configuration/startup log is supplied in these records. LICENSE_CAUSE=UNKNOWN; empty output is not proof of no MATLAB activity.
