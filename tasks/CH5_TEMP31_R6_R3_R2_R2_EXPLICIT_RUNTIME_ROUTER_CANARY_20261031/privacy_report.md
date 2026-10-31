# Original mandatory privacy rule

Unmodified existing scanner source SHA256=95f5de1f1d926de8683ff721bd1bcdcf2f7c90bdc52c1f6be799cfd3cb624ad2.
Exact original STOP_PRIVATE_PAYLOAD assertion: 155 UTF8 bytes; SHA256=38f498e140dd2d583d0ab760d0294a29f30b4cd1e73e8ee045240daaa4ea34ee; Git Blob=e9f14643517273255bb41276f92ca1f17e6b762f; original source line=180. The assertion is extracted by AST, compiled unchanged, and executed on every exact file selected for publication, including manifest and final seal. No replacement regex, skip or rule relaxation is used. The full legacy module is not run because it includes unrelated preparation/replay operations.

Raw source calls and connector messages, complete index snapshot, actual CLI paths/cwd, raw execution receipts, raw stdout/stderr and delivery state stay LOCAL_ONLY. Public argv replaces the interpreter and script full paths with stable roles/relative source path; cwd becomes a role. The receipt records original byte counts/SHA256 and the exact field projection. Actual stdout contains no private path and is published byte-identically; raw and public identities both accompany it. Empty stderr is represented by its real0-byte identity, not an empty public report. Source bodies themselves are not copied into Git payloads.

JSON and Python AST parse checks complement, and do not replace, the original assertion. Per-phase exact scan results stay LOCAL_ONLY and in the seal's bounded delivery summary. Final seal identity is externally recorded LOCAL_ONLY without a third commit.
