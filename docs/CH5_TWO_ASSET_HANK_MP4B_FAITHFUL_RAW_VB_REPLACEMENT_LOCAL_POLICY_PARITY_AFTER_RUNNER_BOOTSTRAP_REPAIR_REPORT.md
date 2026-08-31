# MP4B faithful raw-Vb replacement local-policy parity after runner bootstrap repair

## Terminal verdict

`MP4B_FAITHFUL_RAW_VB_REPLACEMENT_LOCAL_POLICY_PARITY_PASS`

Established:

- `MP4B_FAITHFUL_RAW_VB_MODULAR_CANDIDATE_PATCH_FROZEN`
- `MP4B_FAITHFUL_RAW_VB_TRANSFER_HELPER_ROUTE_ISOLATION_PASS`
- `MATLAB_FAITHFUL_RAW_VB_TRANSFER_HELPER_10CASE_SOURCE_PARITY_PASS`
- `MP4B_ACCEPTED_ORACLE_RAW_VB_SOURCE_ORDER_REPAIR_STATIC_REVIEW_PASS`
- `MP4B_RAW_VB_LOCAL_POLICY_RUNNER_REPOSITORY_SRC_BOOTSTRAP_STATIC_REVIEW_PASS`
- `MP4B_RAW_VB_LOCAL_POLICY_RUNNER_DIRECT_INVOCATION_SMOKE_PASS`
- `MATLAB_FAITHFUL_NEGATIVE_RAW_VB_LOCAL_POLICY_PARITY_ACCEPTED`
- `MP4B_FAITHFUL_RAW_VB_REPLACEMENT_LOCAL_POLICY_PARITY_AFTER_RUNNER_BOOTSTRAP_REPAIR_PASS`

This accepts only the frozen modular candidate patch at the local-policy layer. Production/export bytes were rolled back before closeout.

## Live continuity and preserved authority

- Live task: `f982e6ce572078c41825d6be43bd267e1147ef3a`.
- Direct parent: `43c1ae62021caca31fb291a62df5a889e7d9aec5`.
- Entry worktree: clean.
- predecessor `economics.py` blob/SHA-256: `d6611d7cca702dcaaf1371c44e6179c7f88f5318` / `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`.
- predecessor faithful policy SHA-256: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`.
- unchanged standalone SHA-256: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

Preserved read-only MATLAB root: `D:\ProjectTemp\ch5-mp4b-raw-vb-local-policy-20260831-001`.

- manifest: `5AD56F4C99DF38F43C4F0CB6FB5221F80797EE9B9D6B51A2229B4EE0077007FE`;
- evaluator: `8AA8E0A5EBFCEF136813FF1A880DE8C96BE63D5B958BC947EEE6D8EEBADAC8EA`;
- MATLAB 12-row output: `3510767089553256B860B53D7BBD042C18E02600948DD711244B7F9E1DBE9F5C`.

No preserved artifact was modified or rerun.

## Frozen modular candidate patch

Path: `validators/multi_province/mp4b_faithful_raw_vb_modular_candidate.patch`.

- patch SHA-256: `0F044055DA9B4BFF22A2F8342EF189781AD3D536BFD2A67148C1182C1F9AB31D`;
- candidate economics Git object: `810e0875febc873ae85bef7e88edd4de349b00b2`;
- candidate economics exact blob-byte SHA-256: `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`;
- candidate policy Git object: `2021db630f3057026ffc37d375a43aaddbccec48`;
- candidate policy exact blob-byte SHA-256: `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`.

Deterministic replay used a fresh no-checkout clone at `D:\ProjectTemp\ch5-mp4b-raw-vb-patch-replay-20260831-001`, exact task authority, and the frozen patch. Both replayed paths normalized to the exact candidate Git objects above; extracting those blobs reproduced the recorded candidate SHA-256 values.

The patch introduces `transfer_candidate_matlab_faithful_raw_vb` with IEEE `np.divide`, `np.fmin/np.fmax`, exact threshold, and bare-`a` scaling. It removes only the faithful selector's pre-floor raw-`Vb` positivity rejection and retargets its four FOCs. Shared/corrected helpers and routes remain unchanged. Persisted ten-case parity passed for finite, negative/zero `pb`, `0/0 -> 0`, infinities and signed `-0`.

## Runner bootstrap and zero-call smoke

Runner: `validators/multi_province/mp4b_faithful_raw_vb_local_policy_python_runner.py`, SHA-256 `367A8C791F1C31C6ECB7F7DDE75133453E60CEF85757F3349EAEB6B2178BA855`.

It derives `REPO_ROOT` from `Path(__file__).resolve()`, binds exact `REPO_ROOT/src` before package import, and verifies every loaded `ch5_two_asset_hank` origin remains below that tree. It rejects wrong roots, outside origins and `chapter5_model`.

One direct-file smoke ran from `D:\ProjectTemp` into fresh root `D:\ProjectTemp\ch5-mp4b-raw-vb-runner-smoke-20260831-001`:

- smoke SHA-256: `5A49429938CA12E5E393BD4D9E7C3BADC19A39F49B6A6E5E6A98444E1FCBD1DF`;
- repo/src roots exact;
- economics and faithful-policy origins exact;
- candidate hashes exact;
- cases/policy calls/rows: `0/0/0`.

Comparator: `validators/multi_province/mp4b_compare_faithful_raw_vb_local_policy.py`, SHA-256 `BD4343EC5CBAA2F789A81D129F40CF4AEA575135C8789067752B4B1E90A85CB2`. Synthetic continuous and categorical perturbations both failed before scientific execution.

## Replacement Python batch and complete parity

Fresh root: `D:\ProjectTemp\ch5-mp4b-raw-vb-replacement-python-20260831-001`.

- Python output SHA-256: `677040AFFB12A5CE1402BF364039B055B0358A7B39F980F5ABD0F9F5FB2FBDB5`;
- comparison SHA-256: `A5D4D81B105549914002EA33259CFC321BBF122689256F21D942F171FC0DF6DD`;
- rows: `12/12`;
- categorical mismatches: `0`;
- all twelve common continuous fields: maximum absolute difference `0`;
- comparator result: PASS.

| case | liquid | transfer | liquid dir | illiquid dir | continuous parity |
|---|---|---|---|---|---|
| lower_a_lower_b_zero_transfer | B | 0 | B | 0 | exact |
| below_abar_positive_transfer | B | B | B | F | exact |
| at_abar_negative_transfer | 0 | F | F | B | exact |
| interior_positive_transfer | 0 | B | B | F | exact |
| interior_negative_transfer | 0 | F | F | B | exact |
| upper_a_negative_transfer | 0 | F | F | B | exact |
| lower_b_blocks_backward_transfer | B | 0 | B | F | exact |
| upper_b_forces_backward_transfer | F | B | B | F | exact |
| liquid_backward | B | B | B | F | exact |
| liquid_forward | F | 0 | F | F | exact |
| liquid_zero | 0 | 0 | 0 | F | exact |
| beijing_iteration5_5_18_1 | B | B | B | F | exact |

Beijing witness was accepted rather than rejected before selection. Both sides give consumption `16.55885094926209`, labor `0.004741141950860115`, transfer `33.3811741130419`, adjustment cost `120.95896695652173`, `mu_a=33.736827215333754`, `mu_b=-170.89756537639485`, backward liquid rate `405.8817177689378`, and forward illiquid rate `64.09997170913414`.

## Call ledger and rollback

| call | count |
|---|---:|
| ten-case MATLAB scalar rerun | 0 |
| junction smoke rerun | 0 |
| MATLAB local-policy rerun/calls | 0 |
| zero-case Python bootstrap smoke | 1 |
| smoke policy calls | 0 |
| replacement Python batch | 1 |
| replacement Python policy calls | 12 |
| comparator | 1 |
| Python/Matlab 50-state HJB | 0 |
| KFE/Beijing household/second province/stationary | 0 |
| MP2/MP3/annual/shocks/transition/dynamics/IRF/R5/Results | 0 |

Rollback hashes pass exactly:

- economics: `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`;
- faithful policy: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- standalone: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

Final production/export mutation: `0`.

Checks: candidate/runner/comparator `py_compile` PASS; helper static parity PASS; comparator negative preflight PASS; focused regression tests `18 passed`; `git diff --check` PASS. Forbidden-operation audit: PASS.

## Exactly one recommended next gate

Apply the frozen modular candidate patch byte-identically for one repaired modular Python 50-state faithful HJB revalidation against the preserved MATLAB HJB artifact under the unchanged propagation-aware contract; do not yet authorize standalone household or 2009 stationary execution.
