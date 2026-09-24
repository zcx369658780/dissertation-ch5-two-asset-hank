# Independent Work review: fourth turn6 repeat-runner repair

Date: 2026-09-24 (Asia/Shanghai)

Verdict: `REJECT__TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR4__ROOT_MUTATION_AND_LEDGER_GAPS__ZERO_SCIENCE`

## Candidate and verified progress

Reviewed local candidate `ea19d0ad8131f46e3275a0d7ecc28cd596cfbf18`, parent `81e0c1052bf47454c747aa1bf93b43e259626e3c`. Only the four task-allowed paths changed; worktree clean; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; planned output root absent; diff check passes. Focused zero-science tests pass 27/27 and default static preflight passes. No replay, HJB/KFE, integration, firm or turn7 household ran.

The candidate exclusively creates root-bound JSON/NPZ targets and checks output-root identity on those writes. Previous comparison, structural/digest, `int64`, integration guard and ledger regression tests remain passing. The receipt's 34 source/reference identity entries read back consistently. This establishes useful preparation progress only.

## Blocking findings

1. The new writer guard does not cover filesystem mutations in reused source code. `base._solve_province()` creates `province_root` with `mkdir(parents=True, exist_ok=False)` in `src/.../optionb_turn2_household_integration.py:652`. If the claimed output root is removed before this point, that child mkdir can recreate it; the scientific call may then start before the first bound JSON/NPZ write detects lost ownership. Other source checkpoint/terminal mkdir and compact-checkpoint unlink operations also bypass the guard. The preparation task requires root loss/replacement to fail closed without touching a foreign root. Add a bounded pre-entry and mutation-path guard or state a precise, testable weaker ownership contract before execution; do not modify production `src` or call the model in this repair.
2. When `owns_output_root()` fails, `run_after_valid_gate()` raises `BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED` with only `original_terminal` (`run.py:737-743`). It omits available `guard.attempted`, source ledger and resolution status. An inert post-entry stub reproduces this. Since no receipt can safely be written into a lost/foreign root, the raised failure detail itself must preserve the earliest terminal and all available attempted-call evidence.
3. `owns_output_root()` uses `Path.stat()`, which follows symlinks (`run.py:137-142`). Moving the claimed directory and replacing its path with a symlink to the original can preserve `(st_dev, st_ino)` while redirecting writes through a replacement path. Reject symlink/reparse-point roots before identity comparison where the host supports the check; add a capability-gated stub test. If the platform cannot guarantee this, document the exact residual limit and fail closed.

The existing 27 tests do not cover these paths. No new scientific law or Owner decision is needed for a bounded zero-science repair. Do not issue the one-shot execution task yet. Results eligibility remains `FALSE`.

## Handoff gate

This review closes the current repair4 task. Under the Owner's handoff rule, this conversation issues no new Builder task sheet. The next GPT Work conversation must verify local HEAD/worktree/review, then create a scoped zero-science repair task before waking the designated Codex session. The only designated session is “整理第五章 K1B 收敛设计证据”, thread `01a0cce5-241d-7ab3-b87c-e0a41628572e`; do not use “审查第五章HANK候选”.
