# Entry-round wage provenance and timing

SOURCE_COMMIT=92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27
SOURCE_ROOT_TREE=adb98b1ad14920902b62ad16bc8ed8e2df4605dc

LOCAL_BYTES_VERIFIED means exact local source bytes authenticated against fixed Git objects/previous raw-byte receipts. SOURCE_STATIC_OBSERVATION means only the frozen task's GPT-supplied Blob/line facts were available; no local content verification or execution is claimed.

## Entry routes

| Route | Actual entry/caller and source | Evidence class | First entering wage |
|---|---|---|---|
| annual_empirical | accepted_source_scalars lines 46-71: wjt=0.6, composite_wage=20.0, wage_tax=0.05, transfer_income=0.1, rb=0.02. load_entry_state lines 139-159 copies scalars into state w/wjt/tau/Tt/rb | LOCAL_BYTES_VERIFIED, Blob d2e74cb8b491489053dcde525cd4d83cb4bd0b3a | INITIAL_DEFAULT_UNPROVEN; no wage.py call in that state construction |
| annual production, Owner-A | production lines 149-152 passes empirical.accepted_source_scalars to owner_a.entry_states; Owner-A lines 215-222 use accepted composite_wage | Caller LOCAL_BYTES_VERIFIED, Blob 7473e04418744d745000afb21d84588273cc5bca. Owner-A body SOURCE_STATIC_OBSERVATION, Blob f89927c7a6234cf1c5106318b2b4249183b90cce | Contract-static default w=20; full Owner-A transformations/units not locally verified |
| annual production, runtime_cache | production lines 153-157 obtains the same accepted scalars and calls runtime_cache.entry_states; runtime_cache lines 98-108 use the default scalar | Caller LOCAL_BYTES_VERIFIED. Callee SOURCE_STATIC_OBSERVATION, Blob a02e86af75f272dcbf7c57b1f7d9f68e30afc4bd | Contract-static default w=20; source/cache/canonical bytes not authenticated here |

No route's default scalar is certified gross or net, or certified as wage.py output. The initial effective coefficient would be 20*(1-0.05)=19 before z where the contract-static HA formula applies. This calculation alone cannot classify a double tax in the first round: if 20 is gross, a tax may be appropriate; if already net, it is an additional wedge. The actual first-round semantic fact remains UNKNOWN.

## Exact local outer-loop order

1. stationary_runtime.py 50-52 sets entering=states and calls household_solver(entering, iteration).
2. Production solve_batch 170 computes phi from entering Yt/Lt, then 173-174 calls historical initialization and HA with entering state w/tau. Empirical solve_batch 237-245 does the same wage/tax handoff.
3. Only after household results does stationary_runtime 53-56 run one_turn and _post_turn_states.
4. one_turn.py 201-210 uses old destination wjt and historical origin-tax labor allocation. That historical path is unchanged and is not the correct TEMP31 destination-tax candidate.
5. one_turn 219-238 evaluates firms, then calls wage.py with new firm.wjt, old province tau, current turn phi and sigma. firm.py 126-133 clips firm wages before this composite calculation.
6. wage.py 55-75 applies destination tau_j and sigma_ji. steady_state.py 162 writes the resulting household_composite_wage to state['w']; firm.as_source_dict has no household-w field, so the subsequent update does not overwrite it. _adapt 197-232 changes Zt/GovInv, not w. The next loop enters with this prior-turn calculated composite.

Thus iteration>=2 entering w has code-structural CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA provenance from the prior completed turn. This is a static code timing conclusion, not proof of an observed run, converged household solution or actual source inputs. The current turn's phi is recomputed before HA while entering w reflects the prior turn's phi/wjt; a future witness must preserve the producing snapshot, not silently substitute current matrices.

Iteration 1 enters HA before any one_turn composite update. Its end-of-turn wage cannot retroactively certify its entering default. A new year/run can reset the default; iteration number alone is never evidence of net provenance.

## Owner bootstrap decisions remain open

Initial wjt=0.6 is below the stated wjtmin=0.8 used in entry state and firm clipping. Moving that clip before the first HA call, using initial phi versus a productivity-updated phi, or recomputing a preparatory wage from real source inputs changes the bootstrap contract. R1 performs none of those changes. The real wage/phi/sigma/tau provenance and labor/wage units need decisions and evidence before the preparatory-net option can be adopted. Three primary Excel originals remain unopened and unauthenticated.
