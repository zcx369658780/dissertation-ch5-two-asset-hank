# Six authenticated wage consumers and corrected bindings

All original Blobs belong to fixed SOURCE_COMMIT5f55365d2aff6bd1517a567e2bcaf17452960a7e and are now LOCAL_BYTES_VERIFIED, with original bytes/SHA-256 in source_identity.json. Historical files remain unchanged.

| Point | Historical fixed source/lines | Original coefficient | New isolated source/lines |
|---|---|---|---|
| Initial labor/value | anchor b1710ae3c5d8d7baf96e85c932d777fa5f3b908c, 171-184 | (1-float(state['tau']))*float(state['w'])*z; same wage feeds the root and c/value | multi_province/temp31_ha_taxfree_bootstrap.py 202-217: inputs.wages[0]*z; unchanged root/helper and remaining body |
| HJB boundary resources | matlab_faithful_hjb e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50, 89-94 | (1-inputs.tau)*inputs.wages[0]*z*labor0 + Tt + effective_rb*b | temp31_netwage_hjb.py 93: net wage directly, same labor, transfer and borrowing-rate terms |
| Local policy labor/consumption | matlab_faithful_policy 2021db630f3057026ffc37d375a43aaddbccec48, 119-155 | wages[0]*(1-tau-migration_costs[0])*z; same coefficient in liquid resources and zero-drift consumption | temp31_netwage_policy.py 137-158: net wage*z; local no-tax input type retains effective rb, weights and provenance; calls corrected labor/drift functions |
| labor_from_vb | economics 810e0875febc873ae85bef7e88edd4de349b00b2, 80-85 | wages*(1-tau-migration_costs)*z | temp31_netwage_economics.py 81-87: wages*z; V_b, weights, phi power unchanged |
| asset_drifts | same economics Blob, 99-115 | sum(wages*(1-tau-migration_costs)*z*labor) | corrected economics 101-118: sum(wages*z*labor); mu_b, mu_a and adjustment cost unchanged |
| asset_drifts_matlab_faithful | same economics Blob, 118-137 | same labor-income tax/wedge | corrected economics 121-141: direct net income; liquid budget and MATLAB illiquid-return taper unchanged |

New Temp31NetWageInputs itself has no independent wage tax or additional migration deduction. A type guard rejects legacy HouseholdInputs at each corrected entrypoint. Local policy passes the same record/origin/expected context/order when rebuilding rates, preventing silent source loss at that boundary. The HJB imports the corrected policy; policy imports the corrected economics. The original matlab_faithful_operator import is byte/AST-equivalent and its implementation is not modified or fetched.

SOURCE_LEVEL_TAU_REMOVAL_BOUNDED covers these six declared sites, the no-tax input interface, source-derived dependency bindings and AST/scalar checks. It does not certify full runtime imports, grid behavior, KFE coupling, convergence or production. SOURCE_LEVEL_TAU_REMOVAL_COMPLETE=FALSE. Actual initializer/root, policy and HJB calls=0; operator/runtime closure beyond the specified sources is NOT_VERIFIED.

These are alternative consumers of a common wage, not evidence that multiple taxes were fiscally collected in a real run. .05 is only the first numerical reference. Real destination tau_j and sigma remain in producing evidence and are not zeroed globally.
