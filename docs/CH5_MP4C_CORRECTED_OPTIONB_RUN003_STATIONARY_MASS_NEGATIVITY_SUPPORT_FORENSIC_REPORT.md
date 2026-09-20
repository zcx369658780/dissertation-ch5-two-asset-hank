# Chapter 5 run003 stationary-mass negativity support forensic

## Terminal result

`PASS__RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_COMPLETE__NO_KFE_METHOD_CHANGE`

`RUN003_NEGATIVITY_BREACHES_TRANSIENT_ONLY__CLOSED_CLASS_MASS_PASSES_ENTRYWISE_FLOOR__KFE_METHOD_DECISION_REQUIRED`

The forensic is deterministic post-processing of the accepted run003 artifacts. The existing KFE result remains FAIL and no KFE method or tolerance was changed.

## Authority binding

- Actual live-main baseline: `03a6c3d17b9741cf60fb0d3f4bd2b981ac5e2fef`.
- Accepted run003 manifest: `18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`.
- Accepted stationary-mass artifact: `15C6D7B24375A20CADB8C871527C75B7447EE9397FCAA44C72FCFC26D064E436`.
- Accepted p / g / residual identities: `F29C4A816652520ABB678301976BA8D3B62773652546B6434BB05674A88DF1CC` / `99BAC1D6842B04EF71D7914D31DCA04BE8E4C8E9BECC995A1307DD096859B46D` / `A180AD4C72DE3D7951EEDE186BC93E95683D57B43CBE48CE08F968EF662CCD4D`.

## Closed and transient mass statistics

| support | states | zero | positive | negative | breaches | min p | max p | signed mass | positive mass | negative mass | L1 mass | max abs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all | 800 | 0 | 522 | 278 | 14 | -2.2179096419585152e-12 | 0.15047341337432121 | 1 | 1.0000000000100877 | 1.0087680036243705e-11 | 1.0000000000201754 | 0.15047341337432121 |
| closed | 400 | 0 | 400 | 0 | 0 | 3.4169927219422868e-07 | 0.15047341337432121 | 1.0000000000100855 | 1.0000000000100855 | 0 | 1.0000000000100855 | 0.15047341337432121 |
| transient | 400 | 0 | 122 | 278 | 14 | -2.2179096419585152e-12 | 2.8605821799510003e-16 | -1.0085295212390263e-11 | 2.3848238534402572e-15 | 1.0087680036243705e-11 | 1.0090064860097144e-11 | 2.2179096419585152e-12 |

## Global minimum and breaches

Global minimum is flat index `419` at `(b_index,a_index,z_index)=(19,0,1)`, physical state `(b,a,z)=(5,0,1.3)`, p=`-2.2179096419585152e-12`, support=`transient`.

Closed/transient breach counts: `0` / `14`. `abs(global_min)/tau=11.560853052157272`; total-negative-mass/bound=`0.065727534797817164`.

Top 20 floor breaches by magnitude:

| flat | (b,a,z) index | physical (b,a,z) | p | support |
|---:|---|---|---:|---|
| 419 | (19,0,1) | (5,0,1.3) | -2.2179096419585152e-12 | transient |
| 0 | (0,0,0) | (-2,0,0.80000000000000004) | -1.4985646575093866e-12 | transient |
| 1 | (1,0,0) | (-1.631578947368421,0,0.80000000000000004) | -3.4146003745344344e-13 | transient |
| 418 | (18,0,1) | (4.6315789473684204,0,1.3) | -3.1357508869517396e-13 | transient |
| 2 | (2,0,0) | (-1.263157894736842,0,0.80000000000000004) | -2.9433735616481112e-13 | transient |
| 3 | (3,0,0) | (-0.89473684210526327,0,0.80000000000000004) | -2.7574777621719651e-13 | transient |
| 4 | (4,0,0) | (-0.52631578947368429,0,0.80000000000000004) | -2.6575608965748665e-13 | transient |
| 5 | (5,0,0) | (-0.15789473684210531,0,0.80000000000000004) | -2.5913767014864898e-13 | transient |
| 417 | (17,0,1) | (4.2631578947368416,0,1.3) | -2.5165730995351825e-13 | transient |
| 6 | (6,0,0) | (0.21052631578947345,0,0.80000000000000004) | -2.3597184618380508e-13 | transient |
| 416 | (16,0,1) | (3.8947368421052628,0,1.3) | -2.2279717743627408e-13 | transient |
| 7 | (7,0,0) | (0.57894736842105265,0,0.80000000000000004) | -2.1120352015136875e-13 | transient |
| 415 | (15,0,1) | (3.5263157894736841,0,1.3) | -2.0442448318772523e-13 | transient |
| 8 | (8,0,0) | (0.94736842105263142,0,0.80000000000000004) | -1.9392333783594802e-13 | transient |

The complete breach table is persisted as JSON and CSV in the evidence root.

## Persisted residual decomposition

| support | inf norm | L1 norm | signed sum | max-abs flat index |
|---|---:|---:|---:|---:|
| closed | 1.3682631416767066e-16 | 1.4464432662687418e-14 | 2.5986039085519955e-16 | 629 |
| transient | 1.2082642359055641e-16 | 1.1548046149573596e-14 | -2.071203799373681e-16 | 114 |

The residual was loaded from the persisted artifact. No `Q.T@p` multiplication was performed.

## Scientific boundary

All prohibited scientific-call counters are zero. No vector entry was clipped, projected, truncated, absolutized, oriented, normalized, or otherwise changed. Results eligibility remains `FALSE`.
