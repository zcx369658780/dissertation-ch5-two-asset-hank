# V0.0.2 source crosswalk — SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING only

Fixed code baseline: `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`, tree
`39e7a91ca473ba770bd65518607c3f78f4b9fe24`. All source locations below refer to
this exact commit, not the dirty local worktree or the documentation branch.
Freeze: `4b11c46823e7cdabc12de8b8036cc5efc2380c52`, plan blob
`43171bc6b841695845e7576d7feaa3135b88c588`; independent authorization:
`3ed139aee7563a7033fa02fb933c3b49f24bd6b1`.

## Evidence labels and route identity

- `SOURCE_ONLY`: read code defines a field or actually calls another function;
  this is not an observed real runtime or authentication of its output.
- `HISTORICAL_ACCEPTED`: an existing acceptance document describes its own fixed
  fixture/checkpoint and evidence. No historical solver/data task was reopened.
- `SYNTHETIC_ENGINEERING`: fictional in-memory records and deterministic reductions.
- `LOCAL_ONLY`: original process logs and private protection inventories.
- `UNKNOWN/BLOCKED`: real producer identity, permission, complete unit/year/price
  and calendar bindings, scientific convergence and production qualification.

The MATLAB-faithful result and accepted corrected checkpoint route are different
objects. `exports/matlab_faithful_two_asset_ha.py:652–669` uses a contaminated-row
KFE solve and density normalization. This is not the corrected unique-closed-class
KFE law. Its `solve_household_steady_state:698–705` actually invokes HJB and KFE;
it was NOT called. Its scalar aggregates cannot recover policy arrays or certify
corrected checkpoint identity. No automatic conversion of this result is provided.

## Exact source identities

| Baseline path | Git blob |
|---|---|
| exports/matlab_faithful_two_asset_ha.py | e144c645d3f4dc842c2faa6b93b2ba0e24275dcf |
| src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py | f79e089f06d0d74867284dc88c94c594215dc02e |
| src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py | 042189063fa5d24480ed4193e133425599b32c8b |
| scripts/ch5_mp4c_2018_corrected_household_aggregate_binding.py | 9a49b5841871d8276dc90d73fa6df60fb4d26e8c |
| src/ch5_two_asset_hank/multi_province/household_adapter.py | d4f62c869e781f078053fb3507e51b22151e3f10 |
| src/ch5_two_asset_hank/multi_province/one_turn.py | 621c8e2dfaf5f55eda39c9b9bffb22cd52ee451f |
| src/ch5_two_asset_hank/multi_province/synthetic_household_bridge.py | 41c0283bacef8a658be64f1cb69467f6d4a07197 |

The paths can be inspected at
`https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/<path>`.

## Producer to input crosswalk

In this table `export` means `exports/matlab_faithful_two_asset_ha.py`, `integration`
means the corrected diagnostic integration above, and `binding` means the old
aggregate-binding script. `adapter` is `corrected_household_adapter.py`.
All policy/mass/return arrays for the synthetic profile have shape `(20,20,2)`,
semantic axes `(b,a,z)`, b fastest in F-order; grids are `(20,)`, `(20,)`, `(2,)`.

| Required field | Existing source symbol and location | Joint input/source requirement; present qualification |
|---|---|---|
| consumption | export `MatlabFaithfulHJBResult.consumption`:561; integration `arrays['c']`:801; binding `selected['c']`:130 | Policy must belong to same province/stage/checkpoint/grid as mass and returns. SOURCE_ONLY; actual receipts not read. |
| labor | export `hjb.labor`:562; integration `arrays['l']`:801; binding `selected['l']`:131 | State-level ell, later z-weighted; persons/hours/per-household/employment mapping UNKNOWN. |
| b_grid/a_grid/z_grid | export external `MatlabFaithfulHJBGrid`, not fields of the top-level result; integration `grid.b/a/z`:802; binding cell coordinates:133–135 | Grid identity and F cell map must match policy and mass. Synthetic grid is frozen b[-2,5], a[0,10], z[.8,1.3]. No real coordinate seal verified. |
| effective_r_a | export `hjb.effective_illiquid_return`:565; integration effective taper:793–797,803; binding `cell['effective_r_a']`:132, law check:140–144 | State-dependent USED return distinct from uniform source return. Real producer/return-stage linkage UNKNOWN. Boundary validates role, shape, digest; does not establish economic origin. |
| source_r_a | integration `float(state['rah'])`:794,806; old binding fixed .09:153,247 | Scalar UNIFORM source return. Not a direct scalar-aggregate output; old .09 cannot be generalized to later provinces/turns. Raw-ra0/S/lagged law unchanged, not computed here. |
| probability_mass | integration terminal `mass['p']`:791, reshape F:804; binding p from protected stationary artifact:231–244 | Same-Q/checkpoint/province support and real provenance needed. Export KFE has no equivalent corrected p field. Cannot silently derive/renormalize p as real corrected output. |
| density | export `kfe.density`:641; integration `mass['g']`:792,805; binding g:231–245 | p–g–omega must agree. Matching bytes/names do not certify accepted KFE law or real asset source. |
| omega | export `kfe.cell_weight=db*da`:644,669; integration imported `OMEGA`:53,805; binding `OMEGA`:246 | Synthetic requires 70/361, no dz/endpoint weight or second normalization. Real density/grid weight binding remains unverified. |
| flat_indices_b_a_z | binding cell index and F-flat index comparison:122–125; V0.0.1 record:81–86 | Integer `(800,3)` mapping checked against known F mapping. A correctly labelled but jointly rewritten same-shape transpose is not authenticated. |
| province/source/stage/checkpoint/grid | integration province runner/state/context; binding fixed checkpoint/manifest/P11 identity checks:77–87,137–144,164–191 | Baseline does not expose one complete authenticated producer envelope. New labels are SIM/SYNTH declarations and per-field matching only. UNKNOWN for real sources. |

`CorrectedHouseholdAggregateInputs:38–91` requires all ten numerical fields,
checks increasing finite axes, finite shaped arrays, finite scalar returns and
positive omega, and p≈omega*g using its existing floating-point bound. It does
not by itself authenticate a source or guarantee nonnegative/unit mass. This
version reuses `SyntheticHouseholdRecord:53–91` for those synthetic mass, grid
and index checks; it does not modify the adapter.

## Reduction and downstream consumer crosswalk

| Output/consumer | Actual baseline code | Qualification and restriction |
|---|---|---|
| Ct | adapter:174, sum(C*p); export scalar c_ss:694 | Real deterministic formula tested on synthetic inputs. Units/year/price UNKNOWN. |
| Lt | adapter:175, sum(z*ell*p); export scalar l_ss:694 | z-weighted household labor. No N=P/3 or household-average conversion; real economic unit UNKNOWN. |
| At/Bt/total_assets | adapter:176–189; export a_ss/b_ss:695 | Per-model asset aggregation, total At+Bt. Real denominator/price interpretation not certified. |
| AtTax | adapter:190–198, At*source_r_a−sum(a*effective_r_a*p) | Illiquid return-flow gap; export scalar aggregates:672–678 contain no AtTax. No annualization or alternative payoff introduced. |
| FrozenHouseholdOutputs | adapter `frozen_output`:114–127; household_adapter:229–250 | Existing output object receives five aggregates and explicit flag/statistic. Synthetic False/0 is not HJB B AND D convergence. |
| Existing scalar output map | household_adapter:69–77 | AtTax points to post-solve reconstruction; strings are static mappings, not a complete executable authenticated producer bridge. |
| PreFrozenHouseholdOutputBatch | synthetic bridge:110–125 actually aggregate→frozen→batch | Real functions invoked in V0.0.2 tests. Diagnostics remain SYNTHETIC_ENGINEERING; no source qualification upgrade. |
| Callback | synthetic bridge:129 onward constructs a one-use supplier; stationary_runtime callback signature:19, consumer:52–55 | SOURCE_ONLY in this version. No callback/controller/outer turn called. |
| Firm labor boundaries | one_turn:223 household Lt→Lt_prev; 227 migration.lt_supply→current firm Lt | Distinct identities retained. No one-turn/firm calls in this version; normalized route remains inactive. |

Historical corrected aggregate/adapter acceptance is recorded in
`docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`.
It concerns its own fixed checkpoint, mass and formula fixture, not today's source
authentication. Its single-statistic frozen flag is representational and does
not replace the accepted corrected B AND D law. The K1 payoff/period contract and
later scientific-index timing decisions remain unchanged. Old NOT_ACCEPTED/CLOSED
binding tasks and C8/C9/C10 budgets were not reopened.

## New opt-in boundary and limits

`HouseholdSourceIdentity` binds fictional province, source, positive simulated
iteration, simulated checkpoint and grid. `HouseholdSourceMetadata` snapshots
the tuple of frozen field references. `admit_synthetic_household_record` requires
an independent requested identity, the exact eleven payload fields, matching
per-field identity/role/digest, complete simulated seal, `(b,a,z)/F` and the
unchanged numeric/record checks. It snapshots numerical inputs before comparing
digests and returns an unchanged V0.0.1 record, converged=False/statistic=0.
`assess_source_contract` gives a reason, never an authorization token; conversion
always revalidates. No loader, real branch or REAL_AUTHENTICATED switch exists.

Digests cover field name/role/shape/canonical little-endian bytes, F traversal,
and manifest declarations. They are NOT signatures, trust anchors, real seals,
runtime permissions or economic validation. A self-consistent transpose or a
jointly altered payload and manifest can pass consistency; an asymmetric oracle
demonstrates changed Ct (5.6→4.7) without pretending to detect all source fraud.
Physical ndarray C/F storage is not semantic axis identity. Checkpoint/grid
labels remain self-declarations, even when every reference agrees.

The existing record/batch do not carry a full real checkpoint certificate. The
original typed metadata and local intake receipt must accompany any future
review; this version does not alter the downstream API to claim such a certificate.

## Future source-loader questions — proposals only, no authorization

1. Owner must select the precise corrected producer route and fixed accepted
   checkpoint/turn/province set; the MATLAB-faithful route is not interchangeable.
2. Define joint policy/mass/Q/grid/return-stage asset identity, manifest authority,
   validation order and safe lifetime/copying. Synthetic SHA cannot certify this.
3. A future protected read request must name exact authorized roots/files, hashes,
   categories, byte/call limits and redaction/output rules before reading policy
   cell receipts, stationary arrays or checkpoint manifests. No such read is
   requested or performed here; old denied/closed archive permissions remain closed.
4. Resolve labor units, population denominator, data year/price and calendar/market
   interpretation only with separate science/data decisions. Internal model-time
   return meaning remains distinct from unresolved external mapping.
5. Preserve C9 PAUSED, CALL_LEDGER_UNRESOLVED, A16 FAIL_CLOSED, model_activation=False,
   Results FALSE, population/per-capita direction and no N=P/3. Source-only,
   historical and synthetic evidence do not establish real production or Results.
