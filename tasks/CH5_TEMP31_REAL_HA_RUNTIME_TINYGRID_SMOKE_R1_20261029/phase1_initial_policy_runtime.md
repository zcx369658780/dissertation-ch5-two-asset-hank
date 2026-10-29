# Phase1: import-initial-policy

IMPORT_RUNTIME_PASS
INITIALIZER_POLICY_CELL_PASS
Exit0; elapsed 4.031s; 30s external hard timeout; no timeout or exception. Job process-commit cap1073741824 bytes, observed peak 56229888 bytes. Exactly one scientific child; no retry.

The immutable first-round record is NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL, entering_iteration1, context TEMP31_TINY_HA_SMOKE_SYNTHETIC_20261029, province_order(A,B), numerical20*(1-.05)=19. Both actual tax_by_destination values remain .05; sigma is the zero2x2 matrix. Temp31NetWageInputs uses origin_index0, wages[19], labor_weights[1], r_a=.09/r_b=.02 and has no extra household tau or migration_costs field.

Real initialization: shape(2,2,2), 8 actual source root calls and 8 real SciPy brentq calls, finite value/labor. Observed root wage coefficients are19*.8 and19*1.3, not an extra tax wedge.
Real direct policy cell: a=0,b=-2,z=.8, lower-a/lower-b flags true and both upper flags false; all four local derivatives1. baseline_labor comes from the actual initialized array[0,0,0]. da10/db7, Tt.1, borrowing gap.07. It returned a finite Temp31NetWageLocalPolicy: {"consumption": 1.0, "labor": 1.7233310683892176, "transfer": 0.0, "adjustment_cost": 0.0, "effective_illiquid_return": 0.09, "mu_a": 0.0, "mu_b": 25.114632239516112, "utility": -5.365772039919352}. No second cell was tried; HJB calls0 in phase1.

Claims, unmodified command hashes, raw-output hashes, public stdout/stderr, exact prefix redaction records and receipts are under evidence/phase_1_*; raw private originals stay LOCAL_ONLY.
