# Executed code and fallback audit

Entry=validators/multi_province/temp31_r6_r3_r2_r2_explicit_task_route_canary_isolated.py
Executed bytes=9769; SHA256=c0dbee9b672c90c96a00618146d7b2f7862e4a79cf7444896a61975f54eeb073. Pre/post identities are equal. The script was not edited or re-run after its sole invocation.

Before execution the main agent parsed and compiled its AST without importing it. Imports are argparse/hashlib/json/pathlib/sys/time/datetime only. CLI requires exactly one dry-run/verify-route mode, all explicit identity and zero-authority fields, rejects unknown options and abbreviation, and supplies no default task. validate_identity checks required fields, exact values, exact types, extra keys and allowed mode before any receipt file access. Current governance commit/path/Blob/bytes and target commit/path/Blob/bytes are fixed. Source receipt request arguments and complete body bytes are rechecked independently by the actual child.

Code path: parse explicit arguments -> exact positive identity validation -> safe task-local ancestry checks -> install in-process audit hook -> read exactly two current task connector receipts -> rehash body identity -> three in-memory negative validator calls -> JSON stdout -> exit0. There is no target dispatcher, dynamic application import, default-index read, task glob, launcher, model, MATLAB, process or network invocation in this entry. No execute/arm/run-target branch exists. The only R40 string is an inert input to the pure negative validator.

Observed after library imports: two exact authorized receipt opens, zero file writes, zero denied actions, and unchanged open count across each negative case. In-process audit instrumentation is not independent OS tracing, and does not measure interpreter startup imports. The real interpreter used isolated/no-site/no-bytecode flags. The complete source plus actual stdout and parent receipt support only this explicit invocation. They do not certify arbitrary host processes or old launcher precedence.

Static AST import and forbidden-call checks are in LOCAL_ONLY; runtime source and outputs are public. Implementation review here is main-agent static plus actual bounded CLI evidence, awaiting independent GPT A/B/C.
