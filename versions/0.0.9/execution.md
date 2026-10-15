# V009 execution — PRE_SEAL

Fixed authority: plan commit `f7caeb54b13ec977d1b503b124067ae522ca2433`, tree `7c51c01cb81b5ca1dfe2124de4de1e3a154e71cf`, plan blob `cb76a840fdd9d1756728189bf29518679831aba6`. Separate authorization commit `5b4427ccc956b0189f4e0097d70862f0a29e743b`, authorization blob `770a1fc304c3a602595e9d3d9d5ec21c2bdf1ee5`.
Sole parent: `d41d229b681e09b913c21deff7a057085b9bc419`, tree `88833acf90613380afa30ab8d6ee7e0297e98664`. Remote governance HEAD read back at authorization commit. Main untouched.

## Actual scope and status

Implemented the six new modules and four focused test files inside the frozen thirteen-path whitelist. The new household driver computes policies at every state, consumed-drift Q, implicit HJB updates, same-checkpoint B/D, deterministic positivity-preserving halving and final-policy restricted-support KFE. The macro driver nests fresh household solves in every residual evaluation, with wage/capital FOC, national bonds, signed fiscal T and independent resource/funding checks.

**No full household or macro solve was launched.** The frozen CES equation contains `phi[j,i]`, but neither plan section 3 nor the Owner-adoption/authorization supplies numerical phi. Zero migration fees do not determine a CES disutility weight. A temporary draft default was removed BEFORE runtime configuration registration or any full scientific call; actual registered cases use null and reject missing phi before macro/household reservation. The exact omitted coefficient has been requested from Astra via Owner. This is an input-contract blocker, not observed HJB nonconvergence, an economic impossibility result, or completed science.

## Runtime isolation

A new standalone Git directory borrows fixed read-only baseline objects through audited alternates; original refs/index/objects were not written. Only five audited old pure mathematical files are exported for runtime: corrected contracts, boundary, cost, generator, selector. No production package initializer, historical runner, old HJB/KFE or data loader is imported. New modules are loaded as the explicit `v009` namespace, old pure modules as `_v009_pure`; the ordinary production package import is intentionally not the launch route.

An import-only subprocess recorded exact new-module origins and preregistered artificial parameter cases and source hashes. Frozen phi remains null. Toy oracles have their own explicitly constructed inputs and do not masquerade as the full calibrated model.

## Actual attempts before sealing

- pytest red_001: exit 2, four expected missing-new-module collection errors; 2.236 s.
- pytest oracles_002: exit 0, 11 passed; 3.424 s.
- import-only import_001: exit 0; 0.744 s. No solver called.
- pytest oracles_003: exit 0, 13 passed; 1.266 s.
- Full scientific drivers 0/4; macro attempts 0/4; household HJB/KFE attempts 0/176; HJB direct updates 0; full household policy/Q maps 0; terminal household GESVD 0.
- Toy oracle calls: selector 5, scalar roots 0, SCC 4, restricted GESVD 2, full toy Q-transpose validations 2. Expected bad-shadow/multiple-class refusals are test cases.
- Highest sampled working set 75,264,000 B; no scientific memory measurement because no full solver ran.
- Failed attempts were retained. No tolerance, initial macro price, registered numeric parameter or grid was changed in response to numerical outcomes.

Cumulative counters are persisted BEFORE counted calls. Process argv, stdout/stderr, exit/time and sampled working set remain LOCAL_ONLY. A final focused check of the sealed Git tree is reserved inside the same process/toy budgets; this PRE_SEAL text does not predict its result. Final commit/tree, actual final check and publication readback belong in a detached delivery receipt.

## Protection and remaining work

Original eight tracked dirty files and original index have a before hash receipt. HEAD/branch/dirty categories are unchanged at intake. Post comparison and final candidate identities will be reported outside the sealed tree. Untracked/ignored were not scanned; protected C8 files, B3, A16/G0, old C9 and production consumers were not accessed. No QMD/Basic Memory write.

Candidate publication is at most one ordinary non-force push, with remote SHA/tree/path readback. No merge main and no self-ACCEPT. The incomplete frozen phi contract prevents one-province science, hence two-province science remains closed. Dynamic IRF, 31 provinces and 24x24 remain forbidden.

Terminal: `WAIT_ASTRA_V009_SYNTHETIC_HANK_NUMERICAL_ACCEPTANCE / STOP`.
