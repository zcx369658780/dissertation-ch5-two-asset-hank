# Chapter 5 corrected Option-B run003 stationary-mass nonnegativity failure acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__BEIJING_HJB_TOPOLOGY_AND_RANK_PASS__STATIONARY_MASS_MINIMUM_NONNEGATIVITY_FAIL__ZERO_SCIENCE_SUPPORT_FORENSIC_AUTHORIZED`

## Accepted candidate

- live-main baseline: `829cc10785b88b02700204243e49f694ec8cf54a`
- Builder candidate: `e352acaa6003bf0ccec8e5ad56688a626ccf2146`
- candidate tree reported/read back by Builder: `df57dc548cbab3118a484059e176abb4c65e91e3`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly the baseline
- independently verified changed paths: 150
  - scientific-driver paths: 2
  - focused test: 1
  - report: 1
  - run003 evidence: 146
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main` as accepted run003 failed evidence.

## Engineering-repair acceptance

The run002 topology-persistence and exception-ledger defects are closed.

Accepted zero-science evidence establishes:

- `analyze_exact_positive_topology(Q)` and its SCC algorithm were not modified;
- topology persistence uses an explicit JSON-safe projection of the already-computed result;
- CSR adjacency is represented by deterministic shape/nnz/data/indices/indptr identities;
- labels are represented by a deterministic little-endian int64 SHA-256;
- persistence performs no second SCC;
- province-local terminal-KFE scientific-call counters are accumulated through the exception path with no duplicate success accumulation;
- focused tests: `18 passed`;
- synthetic topology projection uses 0 SCC / 0 SVD calls;
- code freeze and authority checks passed.

These repairs are accepted.

## Beijing HJB acceptance

Run003 exactly reproduces the already accepted Beijing HJB fixed point:

- checkpoint: `12`
- `B=1.292732587643286e-11`
- `D=1.2743897048750341e-08`
- policy maps / D2: `13/13`
- direct updates / post-update evaluations: `12/12`
- maximum direct-solve normwise backward error:
  `3.0832786979441453e-16`
- final V SHA-256:
  `48396D52F13045B4F3370CA892C9989813BBEA8F0D45A577DD8C6D6EDE5ADA93`
- final Q artifact SHA-256:
  `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

Beijing HJB convergence remains accepted.

## Beijing topology acceptance

The exact-positive graph audit is now durably persisted and accepted:

- exactly one SCC decomposition;
- exact-positive edges: `2316`;
- component count: `11`;
- component sizes: one `400`-state component plus ten `40`-state components;
- exactly one closed communicating class;
- closed-class size: `400`;
- closed membership:
  F-order flat indices `200..399` and `600..799`;
- transient states: `400`;
- every recorded transient condensation component reaches the unique closed class;
- labels SHA-256:
  `4D6A9A47469E183A1C56719C5D39B827F3B7796E885883070F4C3940F7A3C2D9`.

This topology is accepted for the exact Beijing Q12 object.

## Dense SVD rank/nullity acceptance

Exactly one full dense `scipy.linalg.svd(..., lapack_driver="gesvd")` was executed.

Accepted result:

- numerical rank / nullity: `799 / 1`;
- second-smallest singular value:
  `2.2838705156609336e-06`;
- smallest singular value:
  `3.0494145606360786e-16`;
- frozen rank threshold:
  `3.735954297981181e-12`;
- structural closed-class count equals numerical nullity: `1 = 1`.

Rank/nullity gate: PASS.

## Stationary-mass failure

Exactly one smallest right singular vector, one global sign orientation, one total-mass normalization, and one `Q.T@p` were used.

The first scientific failure is:

`北京 / checkpoint 12 / terminal_kfe / stationary_mass / minimum_mass_within_allowance`.

Accepted persisted facts:

- stationarity residual infinity norm:
  `1.3682631416767066e-16`;
- stationarity bound:
  `6.197427304868947e-13`;
- normwise backward ratio:
  `4.235572839943202e-17`;
- `math.fsum(p)=1.0`;
- `omega*math.fsum(g)=1.0`;
- minimum mass:
  `-2.217909641958515e-12`;
- frozen per-entry arithmetic allowance:
  `-1.9184653865526386e-13`;
- negative-entry count: `278`;
- total negative mass:
  `1.0087680036243705e-11`;
- frozen total-negative-mass bound:
  `1.5347723092421108e-10`.

All stationary/source-free/normalization/total-negative-mass checks pass except the per-entry minimum-mass check.

Under the frozen KFE contract this is a real scientific FAIL. It must not be relabeled as PASS, clipped, absolutized, renormalized, tolerance-relaxed, or repaired by a second solver call.

The current evidence does not yet prove where the violating negative entries lie relative to the unique closed class. Therefore no new KFE solver method or nonnegativity rule is adopted here.

## Scientific ledger

Accepted run003 consumption:

- initialization: 1
- labor roots: 800/800
- policy maps / D2: 13/13
- selector evaluations: 10,400
- scalar / interior-Z / interior-a / joint roots: 4,148 / 760 / 17 / 1
- HJB updates / evaluations: 12/12
- SCC / dense GESVD / normalized candidate / `Q.T@p`: 1/1/1/1
- aggregates / integration / firms: 0
- retries / solver substitutions: 0/0
- turn 2 / K1B / K2 / MATLAB / GE / Results: 0.

Run001 and run002 historical consumption remains separately preserved.

## Evidence

Run003 root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run003/`

Sealed manifest:

`18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`

with 144 entries and 1,996,742 bytes. Independent readback passed with zero bad paths. Pre/post code freeze matched exactly.

## Route consequence

No fresh HJB/KFE execution is authorized from this acceptance.

The next bounded task is zero-science only: use the already persisted run003 topology and stationary-mass artifacts to localize and quantify the negative mass relative to the unique closed communicating class versus the 400 transient states.

That forensic may characterize the mechanism but must not change the frozen KFE method, project/clip/renormalize the mass, run another SCC/SVD/nullspace solve, or declare KFE PASS.

Any later decision to change KFE solver semantics, support restriction, or nonnegativity acceptance law remains a substantive scientific decision.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
