# MATLAB-faithful two-asset HA standalone single-file export and transfer validation

## Terminal classification

`MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_AND_TRANSFER_VALIDATION_MATERIAL_MISMATCH`

The one authorized standalone scientific run reproduced every numerical HJB, operator, KFE, and aggregate object exactly, but the single comparator found that the two policy-label arrays were not representation-identical to the accepted NPZ. The standalone retained source-module labels as strings `B/F/0`; the accepted artifact stores the same categories as integers `-1/+1/0`. The task explicitly permitted canonicalization only for sparse stored `0.0/-0.0`, not label encoding. Therefore the export cannot be accepted or published under this task. No repair or rerun followed.

The three PASS freezes are not issued.

Preserved validation root: `D:\ProjectTemp\ch5-standalone-export-validation-20260830-001`.

## Authority and source identities

- Fresh-fetched live start/final pre-publication authority: `6469e5a87a00366c1b2af38f27efaa3014206936`.
- Direct parent: `115c7b00c777e64a2e00ab79a67f9982f93a9e04`.
- MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.
- `contracts.py`: `134A0C7666087776CC99FE07E8BE0520D2B132D435B3CEC03CFBE6D9DF910644`.
- `economics.py`: `66E3C56F177DB6DAFE7FE0A5FD6DA480D71A7ACC10B5209BC0E3F7360226DC55`.
- faithful policy: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`.
- faithful operator: `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`.
- faithful HJB: `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`.
- faithful KFE: `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`.

All four accepted faithful identities matched the controlling reports. No modular source was modified.

## Export source map and provenance audit

The candidate single file source-mapped only:

- `EconomicParams` and `HouseholdInputs` from contracts;
- faithful cost, bare-a FOC, taper, consumption/labor FOCs, utility, and tapered drifts from economics;
- exact local policy/upwind branches from faithful policy;
- exact source-axis sparse placement and operator composition from faithful operator;
- faithful implicit HJB and separate post-convergence operator from faithful HJB;
- contaminated-row KFE from faithful KFE;
- source-audited `C/L/A/B` stationary sums and a convenience HJB→KFE→aggregate wrapper.

The header recorded the designated MATLAB source/hash, repository, task commit, accepted parity markers, numerical-oracle status, NumPy/SciPy-only dependency, and explicit GE/dynamics exclusion. It included all required faithful authority markers.

Candidate identity before withdrawal:

- SHA-256: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`;
- size: `27,961` bytes;
- line count: `633`;
- validation runtime: Python `3.11.9`, NumPy `2.4.6`, SciPy `1.17.1`;
- public API included the four required solvers/helpers plus faithful primitives and auditable result dataclasses.

Because terminal is MATERIAL MISMATCH, the candidate and focused test were copied to the external validation root and removed from the repository. They are not transferable authority.

## Engineering validation before scientific execution

- `py_compile`: PASS.
- Import allowlist: standard library, NumPy, SciPy only; no package/repository/MATLAB/data dependency.
- Focused test file SHA-256: `3FB6BAA4FB757C4CA3732035CE8E6A72368315E27C96A98CA41573327FC91CF8`.
- Focused tests: `5 passed`.
- Covered dependency/public API boundary, isolated import, bare-a `a=0`, taper, boundary sparse placement, `M=50→17`, KFE normalization, aggregate weighting/order, and absence of GE/dynamics API.
- Clean-room copy/import from `D:\ProjectTemp\ch5-standalone-cleanroom-20260830-145748`: PASS; only the candidate file was copied and no `ch5_two_asset_hank` module loaded.

These engineering results do not override the scientific transfer mismatch; the requested PASS freezes remain unissued.

## One-shot scientific validation

| Call | Count |
|---|---:|
| MATLAB HJB/KFE/aggregate | 0/0/0 |
| modular Python scientific rerun | 0 |
| standalone end-to-end validation | 1 |
| standalone comparator | 1 |

Standalone validation artifact SHA-256:

`3DD8F459D7D37885888EC2164BF384510595A5C3960BE8B8B50274126EF51AA6`

Comparator artifact SHA-256:

`368B9928F8339733A34EAE41C4E51F0058140F007C050B033E5960B0C68538FE`

The standalone converged in exactly `12` iterations with convergence statistic `9.07700581365134e-10`.

| Aggregate | Standalone | Accepted Python | Exact result |
|---|---:|---:|---|
| `C_ss` | 1.1296890749136979 | 1.1296890749136979 | PASS |
| `L_ss` | 0.7341069339182127 | 0.7341069339182127 | PASS |
| `A_ss` | 0.44059476682729026 | 0.44059476682729026 | PASS |
| `B_ss` | 0.4601208223181049 | 0.4601208223181049 | PASS |
| total assets | 0.9007155891453952 | 0.9007155891453952 | PASS |

Exact PASS objects:

- grid/order and initial value;
- converged flag, iteration count, convergence statistic, value;
- consumption, labor, transfer, adjustment cost, effective return, `mu_a`, `mu_b`, utility;
- iteration `BB/AAH/Bswitch/A`;
- post-convergence `BB/AAH/A`;
- contaminated row/index/RHS, raw KFE solve, normalization factor, density;
- all five aggregates.

Material comparator failures:

| Object | Standalone dtype/categories | Accepted dtype/categories |
|---|---|---|
| `liquid_label` | Unicode `B/F/0` | `int64` `-1/+1/0` |
| `transfer_label` | Unicode `B/F/0` | `int64` `-1/+1/0` |

Read-only localization showed the exact bijections `('B',-1)`, `('F',1)`, and `('0',0)` for both arrays. This establishes an encoding-only mismatch, but it is outside the task's sole allowed sparse-zero representation exception. It was not canonicalized after output, and neither scientific execution nor comparator was rerun.

## MATLAB transitivity and limitations

The exact numerical objects remain transitively covered by the previously accepted MATLAB/Python household parity evidence. This task made zero MATLAB calls and did not create new MATLAB parity evidence. Since transfer acceptance failed on required label representation, no standalone MATLAB-faithful export acceptance is claimed.

GE provenance remains unresolved as `MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED` and is entirely outside this export attempt. No GE, D1-D3, transition, IRF, dynamics, neural-network, calibration, or Results action occurred.

## Repository closeout

Published changed path: only this report. The unaccepted candidate export and test were preserved externally and withdrawn from the repository before staging. Acceptance level: material transfer mismatch; no standalone file accepted or published.
