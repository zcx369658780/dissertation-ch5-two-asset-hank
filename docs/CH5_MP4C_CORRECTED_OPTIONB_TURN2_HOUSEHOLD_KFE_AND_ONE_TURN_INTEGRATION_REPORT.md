# Chapter 5 corrected Option-B turn-2 household/KFE and one-turn integration report

Date: 2026-09-20

## Terminal verdict

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The bounded turn-2 execution stopped at the first scientific failure. Beijing
(`province_index=0`) reached checkpoint 2, where F-order flat index 579 returned
`NO_ADMISSIBLE_POLICY`. No later cell, province, terminal KFE, aggregate, K1A,
C1, firm evaluation, turn-3 payoff construction, or turn-3 household call ran.

## Repository and authority binding

- actual fresh-fetched live-main baseline:
  `a6fbf9d66d4d3603759e87f845e71bc4597c0e1c`
- code-freeze commit before science:
  `04a2ad2d819e7b0baeb887a6b2f6732b9bd0cc02`
- entering-state Git blob:
  `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- accepted entering raw payoff:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- canonical integration predecessor manifest:
  `79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`
- accepted 31-province household predecessor manifest:
  `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`

Both predecessor manifests passed full deterministic readback before science.
The entering receipt had status `PASS`, exactly 31 rows in the accepted province
order, the required classification on every row, and the accepted raw-payoff
identity. The persisted state objects were used directly.

## Reached household checkpoints

### Beijing checkpoint 0

- source-native initialization: PASS; 800/800 labor roots returned
- initial V SHA-256:
  `4A1762649C18499A7530D0D2633DA5ADCB8DD18F5E6EBE21A042CD785D569283`
- initial labor SHA-256:
  `6EEB0A2108F10D69DD4754E1D188A95006B6FF894E6A475196D935BC4D14FA8F`
- `B=0.35948978452765235`; `D=N.A.`; update required
- policy identity:
  `3A9488598DEB9266C121F57057B40D76F08828DE7F2F161B1948C7717EE798AB`
- policy branches: negative 760; zero-kink 40
- selected liquid-Z switches: 40; interior-a 0; joint 0
- Q nnz: 3,080; `max_abs(Q@1)=2.942091015256665e-15`
- minimum offdiagonal: `0.03876660674682193`; D2 PASS
- Q artifact SHA-256:
  `7A408529F8523F8671BEB4D6F4AB8C44877BAE09873A38034A8367630FADC96B`
- direct update 0→1 backward error:
  `2.1754586146795478e-16` (PASS, threshold `1e-12`)

### Beijing checkpoint 1

- `B=0.019968227378343403`
- `D=0.5603661628256393`
- primary convergence: FAIL
- exact cycle: none
- approximate period-2/3: none
- policy identity:
  `D08C0FE03A0F7DBF59A15D20A0C33FE431A31C77544D2C2CBFD27E5C69B6D45F`
- policy branches: negative 658; positive 127; zero-kink 15
- selected liquid-Z switches: 41; interior-a 0; joint 0
- Q nnz: 3,119; `max_abs(Q@1)=3.552713678800501e-15`
- minimum offdiagonal: `1.2171482354261075e-05`; D2 PASS
- Q artifact SHA-256:
  `D6752BB073925F68DA3DD88192FB91ACEB6EDECA2915239797C9AE22D10B8B00`
- direct update 1→2 backward error:
  `1.4650295837509506e-16` (PASS, threshold `1e-12`)

### Beijing checkpoint 2 first failure

- failure cell: flat F-order index 579
- index `(b_index,a_index,z_index)=(19,8,1)`
- physical state: `b=5`, `a=4.2105263157894735`, `z=1.3`
- selector outcome: `NO_ADMISSIBLE_POLICY`
- selector cell id: `v002_f0579_b019_a008_z001`
- the upper-b zero-kink candidate failed with
  `ROOT_FAILURE_NO_UNIQUE_BRACKET`; all six regimes were inadmissible
- no checkpoint-2 D2/Q assembly occurred
- stop was immediate; no scientific retry or rescue change occurred

## Exact scientific ledger

The exception-path finalizer initially omitted the partial checkpoint-2 selector
consumption. Exact totals were deterministically recovered from the already
persisted durable failure-cell cumulative budget. This post-processing made zero
scientific calls and is recorded in `scientific_ledger_reconciliation.json`.

- source-native initializations: 1
- scalar labor roots attempted/returned: 800/800
- policy-map attempts: 3 (2 complete, 1 partial failed map)
- selector evaluations: 2,180
- scalar selector roots: 1,154
- liquid-Z roots: 422
- interior-a/joint roots: 0/0
- D2/Q assemblies: 2
- direct HJB updates: 2
- completed post-update checkpoint evaluations: 1
- SCC / restricted GESVD / full-space GESVD: 0 / 0 / 0
- normalized KFE candidates / `Q.T@p`: 0 / 0
- aggregates / household batch: 0 / 0
- labor / K1A / C1 / firms: 0 / 0 / 0 / 0
- wage / monetary / fiscal: 0 / 0 / 0
- canonical turn-3 payoff constructions: 0
- scientific retries and solver substitutions: 0 / 0
- damping, relaxation, adaptive Delta, clipping, artificial diffusion,
  continuation, and payoff transformations: all 0
- turn-3 household calls / third outer turns: 0 / 0
- K1B / K2 / MATLAB / GE-annual-shock-IRF-welfare-Results: all 0

## Evidence and checks

Evidence root:

`reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001/`

- sealed manifest SHA-256:
  `50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`
- entries: 612
- bytes: 9,677,554
- independent readback: PASS; bad paths 0
- pre/post scientific code freeze: exact match
- focused tests: 6 passed
- related regression tests: 26 passed
- `py_compile`: PASS
- `git diff --check`: PASS

The first launcher attempt failed before importing the task module because the
`src` import path was absent. It made zero scientific calls. The subsequent
launch entered the scientific driver exactly once; scientific retries remained
zero.

## Scope closure

Turn 2 did not complete. No province passed terminal KFE in this task, and the
integration stage was not reached. Turn 3 was not run. CURRENT files were not
modified, no successor was published, and main was not merged.
