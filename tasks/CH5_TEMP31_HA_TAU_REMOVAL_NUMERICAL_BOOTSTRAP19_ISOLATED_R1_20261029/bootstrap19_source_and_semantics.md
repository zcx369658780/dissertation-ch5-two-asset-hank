# Owner-authorized numerical starting wage, not empirical wage adoption

SOURCE_COMMIT=5f55365d2aff6bd1517a567e2bcaf17452960a7e
SOURCE_ROOT_TREE=84424adb69027d4bb3b82f6481f5b961f051033c

Annual empirical source Blob d2e74cb8b491489053dcde525cd4d83cb4bd0b3a lines 61-65 gives wjt=0.6, composite_wage=20, wage_tax=.05. The newly authenticated anchor Blob b1710ae3c5d8d7baf96e85c932d777fa5f3b908c line 179 uses (1-state['tau'])*state['w']*z. Owner approved the exact numerical wage guess 20*(1-.05)=19 to preserve that first effective wage coefficient, without treating 20 or 19 as an empirical wage.

The new first-round record retains w_initial=20, tau_legacy_reference=.05, effective wages=19 and NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL. It requires entering iteration 1, fixed current source identity, explicit context/order and real mechanism tax/wedge arrays. Changed initial numbers, changed semantics, missing/incorrect context/order or a changed consumer wage are rejected. No state['w'] or state['tau'] is modified. The .05 reference is not the actual destination-tax vector; the synthetic test keeps real mechanism taxes (.2,.6) unchanged while the numerical guess remains19.

Later wages must come through unchanged R5 calculated-round evidence: complete destination wages/phi/tau_j/sigma, independent formula recomputation, previous producing iteration, run context and province order. R5's frozen formula witness still names its original R4 source pin 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27. The current consumer source pin is 5f55365d2aff6bd1517a567e2bcaf17452960a7e; wage.py Blob48001b2e4ca64d81dda6174255f6ccf130e07004 is unchanged at both. No R5 pin is silently rewritten. The record preserves this producer/consumer identity distinction.

Bootstrap and later calculated net semantics cannot be interchanged. The source-like/normalized labor and real tau_j mechanisms remain separate; no global zeroing of tax occurs. The new wage-only consumer type contains rates, wages, weights, record, origin and expected context/order, but no tau or migration_costs parameter. It validates a single positive wage/labor category against the record. Zero or negative effective wage is rejected consistently with the historical one-category effective-wage domain.

Initialization is a source-derived local function, not a fake algebra-only household implementation. Its unchanged source labor root and value formula are included, with only the wage coefficient replaced by the explicit net input and a new input-type guard. Neither function is executed. The original temp=effective*effective+rb*b+Tt and l**6/6 terms are preserved rather than silently repaired.

Owner's numerical starting choice does not certify primary Excel files, initial enterprise wage/clip/phi calibration, real later wage provenance, convergence, fiscal tax base or z/N units. Those remain separate scientific gates.
