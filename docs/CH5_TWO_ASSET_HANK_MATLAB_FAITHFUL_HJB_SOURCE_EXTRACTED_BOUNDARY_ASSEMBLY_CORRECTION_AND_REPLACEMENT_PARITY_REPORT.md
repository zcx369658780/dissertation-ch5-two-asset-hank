# MATLAB-faithful HJB source-extracted boundary assembly correction and replacement parity report

## Terminal classification

`MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_BLOCKED`

The corrected MATLAB and rebuilt Python HJB objects both converged and persisted. The single frozen comparator call then failed while serializing its result because a NumPy `int64` worst-index value is not JSON serializable. No comparison artifact was persisted. The comparator was not repaired or rerun.

## Authority and identity

- Live start/final `origin/main`: `1285abfac4548743f8b7f15a7e59923118c32120`.
- Designated `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.
- Designated `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`.
- Designated `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`.
- Designated `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.
- Old MATLAB object `3457F51AC0F910EA40FC35A832518B9068456E22DEA4E4783F487976432DDC0A` remains `DISQUALIFIED_SOURCE_EXTRACTION_OBJECT_RETAINED_FOR_DIAGNOSTIC_PROVENANCE`; it was not overwritten, deleted, or rerun.

## Exact source boundary audit and corrected evaluator

The designated source forms `X`, `Y=-(X+Z)`, and `Z` before `spdiags` placement. At lower liquid boundary the outward `X` entry is truncated while `Y` remains; at upper liquid boundary the outward `Z` entry is truncated while `Y` remains; interior rows place both entries and close. `AAH` uses the analogous placement, while its source boundary overrides normally zero the outward component. Therefore the accepted iteration authority is:

- `MATLAB_FAITHFUL_HJB_ITERATION_OPERATOR_FOLLOWS_EXACT_SPDlAGS_BOUNDARY_TRUNCATION`;
- `MATLAB_FAITHFUL_HJB_ITERATION_BB_MAY_HAVE_SIGNED_OFFDIAGONALS_AND_NONZERO_BOUNDARY_ROW_SUMS`.

The corrected external evaluator fixes `total=rb+rf` before testing whether either coupling is in bounds. It retains diagonal `-(rb+rf)` after an outward coupling is truncated. No other formula, fixture, ordering, solver setting, output field, or post-convergence construction changed.

- Old evaluator: `E81AB34611E3C31DAF2400ED6A34B58F91C4FA0E0FBCCEE843828F5A6588DCBA`.
- Corrected evaluator: `F6D33348329D242AC3C7D867D455DDD0B87184C00A5AD66332A1B62F359599FE`.
- Exact old/new diff: `1F69AFBD092A5A9A6FA84B31EB05FFB3885C64A89AD24E9D1E5F54CC030E61EA`.
- Source audit: `8F355CC9AE3F0860A4E88B25E4057C69D94FFB67011921CDA5387E82BCB6B14C`.
- MATLAB engineering preflight: `BOUNDARY_ASSEMBLY_PREFLIGHT_PASS`; artifact `5BEF1BCC766907AEC7FCB48CA87E9A22461658A0B13BC6578BCBE84CB5BC4D4A`.
- Parameter/grid manifest: `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A`.
- Ordering adapter: `52EB994358F07767AD8859D737C3D7A89BC7FB04DC063754027CA80386F2926D`.
- Initialization: `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`.
- Comparator: `4471CCC837A66245DCB8D2CA1D45F1BD79CBEE5EAE80874B14933E06C75F9A92`.
- Tolerances: `915B3539828F42099182A9145E64B4A353D0D049AF1674549C1031C923CEF72D`.

## Replacement MATLAB HJB

- Calls: exactly `1`.
- Output: `52CE922D7960AB77D87A226747B0B79A29AFAD0C6B9759C7A81AD937CB7E73BF`.
- Shape: `5 b x 5 a x 2 z = 50` states.
- Converged: `true`; iterations: `12`; statistic: `9.076792650830612e-10`.
- Persisted all authorized value/policy arrays and iteration/post-convergence `BB`, `AAH`, `Bswitch`, and full `A`.
- Iteration `BB`: `96` stored entries; maximum absolute row sum `0.00781423959671379`; minimum stored off-diagonal `-1.0888106657646826`.
- Iteration `AAH`: `110` stored entries; maximum absolute row sum `5.551115123125783e-17`; minimum stored off-diagonal `0.03695436144155011`.
- Iteration full `A`: `217` stored entries; maximum absolute row sum `0.00781423959671379`; minimum stored off-diagonal `-1.0888106657646826`.
- Post `BB/AAH/A` stored entries: `89/80/179`; maximum absolute row sums `1.0939644363092649/0/1.093964436309265`; minimum stored off-diagonals `0.04455113958836332/0.0003533148048050286/0.0003533148048050286`.

## Python faithful rebuild and replacement execution

The rebuild added a distinct source-placement operator and HJB driver and minimally exposed the raw iteration liquid coefficients from the faithful local-policy block. It accepts signed iteration components, fixes the diagonal to the negative sum before boundary truncation, uses MATLAB/Fortran ordering, and keeps post-convergence net-drift construction separate. Corrected/reference `policies.py`, `hjb.py`, and `generator.py` were untouched.

- `matlab_faithful_operator.py`: `0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC`.
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`.
- `matlab_faithful_hjb.py`: `924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE`.
- Runner: `CE3C320DC6D7014A692FE0B71165854236FECD0D23C0A8026C1BCD152D5FF2AC`.
- Static compilation: PASS.
- Synthetic upper/lower/interior signed and non-reclosing placement: `PYTHON_BOUNDARY_ASSEMBLY_PREFLIGHT_PASS`.
- Calls: exactly `1`.
- Output: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.
- Converged: `true`; iterations: `12`; statistic: `9.07700581365134e-10`; value shape `(5,5,2)`.

No converged Python HJB was run during engineering preflight. The initial import-only preflight attempt failed before any HJB because the shell lacked `PYTHONPATH=src`; after setting the repository's configured source path, the permitted engineering preflight passed. This did not consume or duplicate the scientific Python call.

## Comparator blocker and mismatch status

- Comparator calls: exactly `1`.
- Native failure: `TypeError: Object of type int64 is not JSON serializable` at the final `json.dumps(result, ...)` persistence statement.
- `comparison.json`: not generated.
- Comparator output hash and complete parity summary: unavailable because persistence failed.
- Complete scientifically established mismatch list: empty. No persisted comparator result exists from which a PASS or MATERIAL_MISMATCH can be established.
- A read-only pre-comparator diagnostic observed different stored-entry counts for some component matrices, but this was not promoted to a mismatch because the unchanged comparator did not persist its pattern/value decision.
- No comparator repair, retry, tolerance change, source adjustment, or scientific rerun occurred.

## Exact call ledger and failures

- Historical disqualified MATLAB call: retained separately; not rerun.
- Corrected replacement MATLAB HJB: `1/1`.
- Replacement Python faithful HJB: `1/1`.
- Comparator: `1/1`.
- Final ledger SHA-256: `156398C89EB72F60C331CA01EBC3F09246E11114205BA34EFC728A4D252E1CBE`.
- Source/environment failure list: comparator JSON serialization failure only.
- KFE, stationary distribution, steady state, D1-D3, tail, transition, IRF, dynamics, calibration, and Results: not run.

## Changed paths and repository state

- `src/ch5_two_asset_hank/matlab_faithful_operator.py` (new).
- `src/ch5_two_asset_hank/matlab_faithful_hjb.py` (new).
- `src/ch5_two_asset_hank/matlab_faithful_policy.py` (modified, faithful-only raw iteration fields).
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_REPORT.md` (new).

Final worktree is intentionally uncommitted with only the four task paths above changed. Acceptance level is BLOCKED before comparator persistence. No next scientific gate is recommended and the contaminated-row KFE gate is not authorized. Any comparator serialization correction or replacement comparator execution requires a new exact live GitHub task.
