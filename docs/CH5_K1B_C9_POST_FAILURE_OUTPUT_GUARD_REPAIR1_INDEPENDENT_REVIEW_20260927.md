# C9 output-guard Repair1: independent GPT Work review

Verdict: `ACCEPT__BOUNDED_ZERO_SCIENCE_MKDIR_GUARD_AND_CHECK_WINDOW_EVIDENCE_ONLY`.
Date: 2026-09-27 (Asia/Shanghai).

## Identity and review result

Candidate `42ed80037d62ef7934fa1a8eeeecab5bd9695172`; parent `d52d96003090a1b0cd54d560dc206171e7f6e0de`; tree `27dac011c914e48a4cd08543e4048f646ff8862a`; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Exactly three allowed paths changed: inert test raw SHA-256 `F31F86D9975171441AF4CB7ADD5E6B072163DB27051D9EE5BD9F320087DBE161`, report `F444E93C0D4CBBCF09305BF3BC581F3A5D6A8D9A9CFD80CD9E517F23CC44304A`, receipt `C38C089B1674F5305F201A173C5BEE0E5C50AF38DF7931B167BB90FF299C01DA`. Delegate and frozen `src` were not edited. Tracked/index are clean; six protected untracked roots and seven named manifest/readback hashes match the prior binding.

The added inert test replaces the owned output root after the first successful `owns_output_root` check inside `guard_output_mkdir` and before its final check. The final check blocks before original `Path.mkdir` mutates the replacement root, and records bounded `root_not_owned` detail. The one authorized focused test invocation returned `1 passed`. The prior candidate's `7 passed, 1 skipped, 62 deselected` remains historical; the real-directory-symlink case was skipped on this host, with simulated reparse passing. No preflight, `--execute`, wrapper, model or scientific entry was used in Repair1 or this review.

The candidate report correctly limits the result to check-time root replacement. The final ownership check and the subsequent path-based `Path.mkdir` are **not atomic**; a replacement after that final check remains a TOCTOU risk. Non-`mkdir` guard failures do not acquire the new bounded diagnostics. Neither limitation is silently accepted for whole-runner activation. The earlier `5e40792d` REJECT and every older REJECT, including the two prohibited `--execute` probes, remain historical verdicts; Repair1 supplies the missing bounded evidence without retroactive reclassification.

The report does not embed its own final commit/tree or its own/receipt final raw hash because that would create a self-reference. These identities were supplied in the candidate handoff and independently recomputed above. This is not an evidence defect for this limited review.

## Authority boundary

This ACCEPT covers only the static `mkdir` missing-suffix repair and the tested ownership-check window. It is not a whole-runner safety approval, contract rebind, execution approval, or evidence of completed C9. The old and new C9 attempts remain consumed; both actual ledgers are `CALL_LEDGER_UNRESOLVED`. C10, retry, partial resume, model science and Results remain closed; Results eligibility is `FALSE`. A separate zero-science design review must decide how to handle the post-final-check mutation window before any runner-recognized safety approval. Future science needs a new explicit Owner decision and independently reviewed R/C/O/T chain.
