# Three real consumer points versus the proposed data probe

All references use SOURCE_COMMIT 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27. The seven missing auxiliary objects were not fetched or imported. Only their task-supplied fixed Blob/line facts are used below. Missing exact equations are not filled in from memory or a generic HANK model.

| Real point | Fixed source / lines | Known wage coefficient and data | Local evidence limit |
|---|---|---|---|
| _source_initial_arrays: initial labor/value | mp4b_python_empirical.py Blob b1710ae3c5d8d7baf96e85c932d777fa5f3b908c, 171-184 | Contract static wage=(1-state['tau'])*state['w']*z. Production 173 calls this helper before the solve. State contains Tt, rb, rah and other prices | SOURCE_STATIC_OBSERVATION only. Exact baseline-labor formula, initial consumption/value formula, utility constants, transfer and asset-return placement in this body are UNKNOWN_FROM_LOCAL_BYTES |
| HJB boundary resources | matlab_faithful_hjb.py Blob e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50, 89-103; contracts.py Blob c746b616bec38531a7d96da81a54e2899d8aba53, 79-104 | Task-static wage term=(1-inputs.tau)*w*z*labor. Locally verified production 174 supplies state w, state tau, sigma=[0], labor-type weight=[1], rah and rb through HouseholdInputs; Tt and rb_gap are additional solve arguments | Deep body SOURCE_STATIC_OBSERVATION. Full boundary-resource equation, transfer integration and effective illiquid-return treatment are not locally authenticated or executed |
| Local policy labor/net wage/consumption | matlab_faithful_policy.py Blob 2021db630f3057026ffc37d375a43aaddbccec48, 119-155 | Task-static effective wage=w*(1-tau-sigma)*z; labor choice and consumption consume that coefficient | SOURCE_STATIC_OBSERVATION. Exact labor FOC, clipping/caps, saving/drift and full consumption expression remain UNKNOWN_FROM_LOCAL_BYTES; no policy function was called |

Production/empirical callsites are LOCAL_BYTES_VERIFIED: production.py 173-174 and empirical.py 237-245. z originates from the household grid; production's grid construction at 162 contains (0.8,1.3), but no grid or household object was instantiated by this task. Passing Tt/rb/rb_gap is locally visible; their detailed use inside missing bodies cannot be inferred merely from argument names.

## Conditional repeated-wedge conclusion

If w is the wage.py net composite from a previous completed turn, applying nonzero state tau again gives (1-tau_i)*W_net*z (and times labor where appropriate), rather than W_net*z. The destination tax tau_j is already inside W_net; an origin-indexed HA scalar is not a substitute for destination taxation. Current visible production sigma-for-HA is zero, so a second nonzero migration deduction is a defensive injection case, not an observed current sigma deduction.

These three consumer points are alternative/related calculations inside one household problem. Their formulas do not prove three separate fiscal collections, or repeated sequential multiplication by three taxes. No real tax payment or fiscal revenue was observed.

## What the isolated executable contract proves

The new source record requires complete synthetic producing inputs, fixed source/formula IDs, province order, run context, previous completed iteration and an independent net-wage recomputation. Only then does it call the unchanged R4 pure-data adapter. Both future initialization/HJB wage views receive one W_net and extra tau_HA=sigma_HA=0; original destination taxes/wedges remain separately retained.

For caller-supplied positive z and nonnegative labor ell, all three proposed wage-income probes equal W_net*z*ell. The illustrative accounting expression is:

R_proposed = W_net*z*ell + T_assumed + rb_assumed*b_assumed + other_asset_resources_assumed.
C_illustrative = R_proposed - saving_flow_assumed.

These are explicitly pure accounting identities. They do not reconstruct the missing initial-value, actual HJB boundary or policy-consumption equations, and do not solve for labor, saving, consumption policy or value. The exact real-consumer equivalence step is BLOCKED/NOT_EXECUTED pending source and separate HA authority.
