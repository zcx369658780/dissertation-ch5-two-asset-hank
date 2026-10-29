# R2 single HJB call binding repair

TASK_ID=CH5_TEMP31_HA_TAXFREE_HJB_POLICY_CALL_BINDING_REPAIR_R2_20261029
COMPLETED=single source call identifier repair and bounded static regression.
LOCAL_TERMINAL=LOCAL_SINGLE_CALL_REPAIR_VERIFIED__REMOTE_DELIVERY_PENDING
Delivery verification is sealed separately in DELIVERY_FINAL_RECEIPT.json and the external final readback receipt.

At line 105, the unbound select_matlab_faithful_local_policy call is replaced by select_temp31_netwage_local_policy, imported on line 14 and defined in the corrected policy module on line 57. Every other HJB source byte is unchanged. The full native diff and before/after identity proof are archived.

Test command 1: expected red, exit 1, one actual assertion at the unbound line105 call. Test command 2: exit 0, 8/8 static checks; injected old call is rejected. Tests consumed 2/2; actual initializer/root/policy/HA/HJB/KFE/GE/IRF calls 0. No imports of scientific modules occurred.

NOT_COMPLETED=real module runtime linkage, HJB grid, solver convergence, economic/scientific validation, production wiring, fiscal adjudication and empirical wage authentication. No broader implementation claim is made.
BLOCKED=P3 and FULL_RUNNER_IO_CLOSURE remain blocked. Bootstrap19 is only the approved numerical guess; real tau_j and sigma semantics and all six prior wage expressions are unchanged.
V010=UNCHANGED; V011=NOT_STARTED; Results=FALSE; FORMAL_SOURCE_FREEZE=FALSE; model_activation=FALSE; REAL_GE=FALSE.
NEXT_ACTION=STOP after exact remote readback; await GPT independent A/B/C review. No automatic PR, Issue, merge, cleanup or successor.
