# TEMP31 R4: isolated worksite-tax patch and synthetic contracts

COMPLETED=New isolated TEMP31 module, explicit synthetic validator and tests; fixed-source recheck; expected legacy counterexample followed by 12 passing candidate cases.
BLOCKED=Real initialization/HouseholdInputs/HJB consumer verification, empirical net-wage provenance, labor units and formal fiscal adoption.
NOT_COMPLETED=Production wiring, real HA/HJB/KFE/GE/IRF, empirical data certification, scientific acceptance, integration or model activation.
NEXT_ACTION=GPT independent A/B/C review of the delivered fixed candidate; Owner decides any subsequent scientific or integration authority.

The new source-like and normalized functions index tax by destination j, retain consumption/wage powers, use destination rows/origin columns, and multiply origin population only once. The net-wage adapter returns the same immutable wage-data tuple for proposed initialization and HJB consumers; additional HA tax and migration wedge are both zero. It does not construct shared HouseholdInputs or run either consumer. The fiscal diagnostic only compares assumed tau*L and tau*w*L and always marks SCIENTIFIC_PENDING.

Only three new code files are introduced. All ten existing authenticated source files, including both historical migration functions, one_turn, firm/fiscal and production entrypoints, retain exact source bytes. No change to V010, ORACLE_SHA, a household algorithm or an empirical asset is included.

Test budget 2/2: invocation 1 intentionally failed one destination-tax assertion against the unchanged historical origin-tax path (exit 1, 1 failure, 0 errors); invocation 2 passed all 12 candidate/legacy-contract cases (exit 0). No production package or household solver was imported/called. This is bounded engineering evidence, not a scientific model PASS.

Delivery is two-stage: payload then receipt seal. Exact payload/seal identities and successful remote file readbacks are recorded in DELIVERY_FINAL_RECEIPT.json and the final external readback receipt. This report intentionally does not embed its own future commit ID. Do not infer delivery success if either receipt is absent or pending.

One R4 bounded governance-HEAD observation used two same-channel SSH transport attempts: the first closed before returning a HEAD; the single disclosed technical retry returned the exact required HEAD. No further technical retry, supplemental-source fetch, new repository, credential/protocol change or cleanup was used. R3 branch and original STOP evidence remain intact; P3 remains BLOCKED.

TERMINAL_ACTION=STOP_AFTER_FIXED_CANDIDATE_REMOTE_READBACK__GPT_INDEPENDENT_REVIEW_PENDING
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE
