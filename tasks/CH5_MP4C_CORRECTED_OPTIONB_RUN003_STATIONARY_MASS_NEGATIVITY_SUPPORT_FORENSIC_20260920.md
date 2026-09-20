# Task — run003 stationary-mass negativity support forensic

Date: 2026-09-20

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID: `CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_20260920`

Status: `COMPLETED_PASS_ACCEPTED`

## Authority

Owner is final scientific authority; ChatGPT is L3 Reviewer; Codex is bounded Builder. GitHub live main is repository-state authority.

Do not enter, read, search, use or modify the separate repository `zcx369658780/deep-learning-hank`.

Read the CURRENT index/status/handoff, the run003 acceptance, run003 report, sealed manifest, topology receipt, SVD receipt, stationary-mass receipt and checkpoint-12 receipt.

No new scientific execution or KFE method change is authorized.

## Objective

Using only persisted run003 artifacts, localize and quantify the stationary-mass nonnegativity violation relative to the accepted unique 400-state closed communicating class and the 400 transient states.

Do not change p, recompute a nullspace, rerun topology, or change an acceptance threshold.

## Exact input authority

Evidence root:
`reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run003/`

Require sealed manifest SHA-256:
`18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`.

Bind:
- `household/p00_北京/terminal_kfe/topology_receipt.json`
- `household/p00_北京/terminal_kfe/svd_rank_nullity_receipt.json`
- `household/p00_北京/terminal_kfe/stationarity_normalization_nonnegativity_receipt.json`
- `household/p00_北京/terminal_kfe/stationary_mass_arrays.npz`
- `household/p00_北京/checkpoint_012/checkpoint_manifest.json`.

Require stationary-mass artifact SHA-256:
`15C6D7B24375A20CADB8C871527C75B7447EE9397FCAA44C72FCFC26D064E436`.

Require field identities:
- p `F29C4A816652520ABB678301976BA8D3B62773652546B6434BB05674A88DF1CC`
- g `99BAC1D6842B04EF71D7914D31DCA04BE8E4C8E9BECC995A1307DD096859B46D`
- residual `A180AD4C72DE3D7951EEDE186BC93E95683D57B43CBE48CE08F968EF662CCD4D`.

Require topology closed-class count 1, closed members exactly F-order flat indices 200..399 and 600..799, transient count 400.

## Zero-science boundary

Allowed: reads, hashes, JSON/NPZ loading, deterministic masks/indexing, scalar/vector descriptive reductions, F-order coordinate mapping, serialization, manifest/readback.

Must remain zero:
- source-native initialization
- selector/root calls
- D2/Q assembly
- HJB/direct solve
- SCC/connected-components/topology recomputation
- SVD/eigen/nullspace solve
- sign orientation or normalization
- `Q.T@p`
- KFE rerun
- clipping/projection/truncation/renormalization
- aggregates/K1A/C1/firm/outer/MATLAB/GE/Results.

Use the already persisted residual and singular values only; do not recompute them.

## Required decomposition

Build the closed-state mask only from persisted `closed_members`.

For all states, closed states, and transient states separately, persist:
- state count
- zero/positive/negative counts
- count below frozen floor `-tau_nonnegative`
- minimum and maximum p
- minimum flat index/indices
- signed `math.fsum(p)`
- positive mass sum
- total negative mass
- L1 mass
- maximum absolute entry.

Also persist:
- global minimum flat index and support class
- every index with `p < -tau_nonnegative`
- breach counts in closed vs transient states
- maximum breach magnitude in each class
- transient signed mass and L1 mass
- closed-class signed mass
- `abs(global_min_p)/tau_nonnegative`
- total-negative-mass / frozen total-negative-mass bound.

Do not modify p.

## Coordinate localization

Use accepted F-order shape `(20,20,2)`, b fastest, b grid `linspace(-2,5,20)`, a grid `linspace(0,10,20)`, z grid `[0.8,1.3]`.

For the global minimum and every floor-breach entry, persist:
- flat index
- `(b_index,a_index,z_index)`
- physical b,a,z
- p
- closed/transient class.

A complete machine-readable breach table is required; the prose report may show only the top 20 by magnitude.

## Persisted residual decomposition

Using only the persisted residual vector, report for closed and transient states:
- infinity norm
- L1 norm
- signed sum
- max-absolute-residual index.

Do not multiply Q by p again.

## Classification

Choose exactly one:

A. `RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED`
only if every `p < -tau_nonnegative` entry is transient.

B. `RUN003_CLOSED_CLASS_ENTRYWISE_NEGATIVITY_BREACH_CONFIRMED__KFE_METHOD_DECISION_REQUIRED`
if any closed-class entry breaches the floor.

C. `RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_INCONSISTENT__NO_METHOD_DECISION`
for provenance/content inconsistency.

No classification accepts KFE or changes its method.

## Deliverables

Allowed implementation:
`validators/multi_province/run003_stationary_mass_support_forensic/run.py`

Allowed test:
`tests/test_mp4c_run003_stationary_mass_support_forensic.py`

Write:
`docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_REPORT.md`

Evidence root:
`reports/ch5_mp4c_corrected_optionb_run003_stationary_mass_negativity_support_forensic_20260920_run001/`

Persist authority binding, closed/transient mask receipt, group statistics, complete breach table, residual support decomposition, zero-science ledger, terminal classification, sealed manifest and independent readback.

Terminal marker:
`PASS__RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_COMPLETE__NO_KFE_METHOD_CHANGE`

followed by classification A/B/C.

## Git

Use an isolated task branch, explicit staging, ordinary non-force push, remote SHA/tree readback and clean worktree. Do not modify CURRENT files, merge main, or publish a successor.


## Reviewer closure — 2026-09-20

Forensic candidate `633e93d3ab114df95ac5d127170ced7da67a2cb1` is accepted.

Terminal:
`PASS__RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_COMPLETE__NO_KFE_METHOD_CHANGE`

Classification:
`RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED`

All 14 floor breaches are transient. Closed-class breach count is 0; all 400 closed-class entries are positive.

Acceptance:
`docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`

Next bounded diagnostic:
`tasks/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_20260920.md`
