# Public evidence privacy boundary

Only the one allowed validator and this task's public evidence are included. Scientific source caches, binary NPZ archives, original logs, authority transport/readback caches and local delivery helper/state files are excluded. Public source/archive identities use repository-relative paths and hashes, not private absolute paths. No credentials, personal empirical records, original private MATLAB files or private keys are included.

For each point, redaction_record.json records raw/public bytes and SHA256 and exact runtime/workspace-prefix substitutions. Raw stdout/stderr remain LOCAL_ONLY. Public derivatives preserve all numerical values and exceptions; no failed solve was replaced by a successful record. Zero retry failures occurred.

Manifest creation scans exact included bytes for Windows absolute paths, UNC prefixes, private-key headers and the local username. JSON parses and Python ASTs are syntax-checked without importing/executing scientific code. Public executable scripts use relative/derived paths. LOCAL_ONLY filenames may be mentioned as provenance but those files are not payload. Final seal adds only DELIVERY_FINAL_RECEIPT.json, avoiding a self-reference cycle; final external readback stays local.
