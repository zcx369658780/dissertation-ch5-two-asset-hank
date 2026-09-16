# CH5 MP4C 2018 KFE D1-D3 corrected HJB Option A seed — Owner adoption acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Owner decision

The Owner explicitly adopts **Option A** as the numerical seed for the first corrected-target HJB one-step diagnostic experiment:

- source object: `hjb100_initialization.mat:v0`
- source file SHA-256: `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- field SHA-256 over native little-endian float64 `(b,a,z)` F-order bytes: `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`
- shape: `(20,20,2)`
- field range: `[-2.6471989790143082,-1.710759724165037]`

Scientific rationale: Option A is an already accepted source-native numerical initialization with MATLAB/Python identity and is not itself an endogenous output of the historical source-faithful boundary/operator trajectory whose derivative states were shown to be incompatible with the corrected D1-D3 target at Cells 4/8/10. This is a provenance/path-dependence decision, not a claim that Option A is closer to the corrected fixed point, more likely to converge, or more likely to pass the selector.

## Frozen common contract

The accepted common contract from `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md` remains unchanged:

- call-725 grid `(b,a,z)=(20,20,2)`, 800 cells, F-order;
- `b=[-2,5]`, `a=[0,10]`, `z=[0.8,1.3]`;
- frozen scalar binding including `rho=.05`, `gamma=2`, `phi=5`, `chi0=.1`, `chi1=2`, `a_bar=1e-6`, `Delta=1000`, fixed wage/returns/tax/transfer;
- raw one-sided finite differences from the Owner-selected seed, with only the inward derivative scientifically valid at an asset boundary;
- unused boundary carrier fields may duplicate the valid inward raw derivative only as a finite representation marker and may never become an additional derivative candidate;
- corrected D1/D3 selector contract and strict D2 consumed-total-drift conservative generator;
- one implicit direct step only: `M=(rho+1/Delta)I-Q0`, `rhs=vec_F(u0)+vec_F(V0)/Delta`, `vec_F(V1)=solve(M,rhs)`.

## Authorization boundary

This Owner decision resolves only the seed ambiguity. Reviewer may now publish one bounded successor task for:

- one complete corrected policy map on the 800-cell call-725 grid;
- at most 800 real selector evaluations;
- at most 264 scalar root invocations;
- exactly zero retries for adverse numerics/scientific outcomes;
- one D2 generator assembly only after all 800 cells produce durable `SELECTED_ADMISSIBLE` receipts;
- at most one sparse direct HJB solve;
- zero second policy map, zero nonlinear continuation, zero KFE, MATLAB, outer/firm/wage-return recalculation, GE, annual, shock, IRF or Results calls.

Any first failed selector cell stops the map and forbids D2 assembly/direct solve. A successful one-step diagnostic does not establish nonlinear HJB convergence, KFE validity, production replacement, or Results eligibility.

Results eligibility=`FALSE`.
