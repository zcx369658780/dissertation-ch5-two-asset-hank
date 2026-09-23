# Current Builder Task

Task ID: `CH5_FULL_OUTER_NINE_COMPONENT_1E6_STATIC_DIAGNOSTIC_20260923`

Status: `ACTIVE__ZERO_SCIENCE_SEALED_CHECKPOINT_DIAGNOSTIC_ONLY`

## Authority and objective

The Owner agreed to the previously recommended **`10^-6 = 1e-6` diagnostic precision** for the proposed complete outer state. The Owner mentioned `10^-12` class precision as a future aspiration, not a current stopping law. Build a static, reproducible nine-component readout from already sealed C4, C5, and C6 checkpoints. This task does not adopt a mathematical convergence law, prove a fixed point, authorize turn7 household, or set a model-call budget.

## Startup and exact inputs

- Work only in `D:\ProjectTemp\c5k1bturn56`. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the accepted full-state design/unit evidence and their independent reviews, then directly named sealed inputs. Never access `deep-learning-hank`.
- Verify a clean Work dispatch HEAD whose parent is `072a0655ae4f9720b89bd5e747f94c62b0e1dda2`, and `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. Record identities before writing. GitHub is not a gate.
- C4 = completed turn4 plus entering turn5 candidate/plan in `reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001/`; C5 = completed turn5 plus entering turn6 candidate/plan; C6 = completed turn6 plus entering turn7 candidate/plan in `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/`. Bind exact manifest, JSON, NPZ, province order, source provenance and SHA-256. C6 is not completed turn7.
- MATLAB reference, read-only exact files: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\multi_prov_HANK_12sts.m` (SHA-256 `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97`), `HANK_mp_1eq.m` in the same directory (SHA-256 `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF`), and `HANK_2ASSETS_HJB.m` there (SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`). Do not enumerate unrelated MATLAB files.

## Exact allowed writes

1. `docs/CH5_FULL_OUTER_NINE_COMPONENT_1E6_STATIC_DIAGNOSTIC_20260923.md`
2. `EVIDENCE/ch5_full_outer_nine_component_1e6_static_diagnostic_20260923/diagnostic_receipt.json`

Do not modify any other path. After checks, explicitly stage only these two outputs and make one local candidate commit. No push, PR, or scientific successor.

## Required static calculation

For each same-stage transition C4→C5 and C5→C6, align all 31 provinces and `S[destination,origin]` exactly. Use the nine proposed carrier components: `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0,rah,S`. Compute each component's maximum difference, location of maximum, finite/shape status, and `1e-6` diagnostic comparison. Save full precision in JSON; the Markdown may display rounded values only when clearly labeled.

Diagnostic formulas authorized **for observation only**:

- `Yt,Lt,wjt,w`: `max_i abs(new_i/old_i - 1)`, dimensionless; all old denominators must be finite and nonzero. This keeps the MATLAB `Yt/Yt_1-1` form for Yt but at the Owner's diagnostic `1e-6` level.
- `Kt_prev`: `max_i abs(new_i-old_i)/Kt0_i`, where `Kt0_i` is the identical positive frozen MU value in both sealed checkpoints. If it differs or is nonpositive, stop rather than substitute a scale.
- `rk,raw_ra0,rah`: `max_i abs(new_i-old_i)` in decimal one-model-period return units.
- `S`: `max_(destination,origin) abs(new-old)` in dimensionless share units, retaining zeros and column orientation.
- Use strict `<1e-6` for every comparison, matching the cited MATLAB strict comparator while changing the object/threshold explicitly. Report each component independently and the conjunction `ALL_NINE_BELOW_DIAGNOSTIC_LEVEL` or `NOT_ALL_NINE_BELOW_DIAGNOSTIC_LEVEL`. These are historical readout labels only, not convergence or stop statuses.

Report `wjt` boundary-hit counts and `Kt_prev==Kt0` counts at each checkpoint as context; neither can substitute for all-nine comparison. Include `raw ra0_n`→`S_(n+1),rah_(n+1)` one-turn timing and check the stored JSON/NPZ bit identities where available. If a component or checkpoint is unavailable, label it `UNAVAILABLE` and do not fabricate a value.

Explain precisely that original MATLAB `num.reg_threshold=1e-9` is used for K/L target and `Yt/Yt_1-1`, plus 31 converged households and zero clipped-`ra` boundary hits. Its HJB `num.crit=1e-7` is inner. The current nine-component `1e-6` readout is a new diagnostic comparison; do not inherit MATLAB's full acceptance predicate. State that C6's sealed 31/31 clipped-`ra` upper-bound hits prevent claiming the original MATLAB outer predicate passed.

## Evidence and stop rules

- Receipt: task ID, dispatch/start/precommit HEAD and `src` tree, exact input paths and SHA-256 (including the three MATLAB files), per-checkpoint identity, nine full-precision metrics per transition, formula/threshold/strictness, each observed comparison, missing/conflict list, two output paths and document SHA-256, exact changed-path inventory, first failure, and literal all-zero scientific/model call ledger. Do not self-hash the receipt; report its hash after commit.
- Static reading, parsing sealed JSON/NPZ, and arithmetic on those sealed numbers are allowed. Do not import or execute any model module, validator, MATLAB script, solver, household, integration, firm, or K1B network evaluation. No synthetic model point, rerun, tuning, or turn7 household.
- Stop on input identity/hash mismatch, accepted-law/source conflict, wrong stage/orientation, zero denominator, frozen `Kt0` mismatch, or need for science to answer the task. Preserve first failure within allowed outputs if feasible. A component merely above `1e-6` is an observed diagnostic result, not a task failure.
- Before delivery verify exactly two allowed outputs changed, frozen `src` tree, zero call ledger, `git diff --check`, output readback, and clean worktree after explicit-path commit.

## Terminal and next gate

Success: `STATIC_NINE_COMPONENT_DIAGNOSTIC_CANDIDATE_READY__ZERO_SCIENCE__WORK_REVIEW_PENDING`. Return candidate commit and hashes to Work for independent ACCEPT/REJECT. Results eligibility remains `FALSE`.
