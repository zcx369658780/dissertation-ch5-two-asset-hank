# CH5 MP4C 2018 KFE D1-D3 corrected HJB one-step design/input binding blocked acceptance

Date: 2026-09-16

Reviewer verdict:

`PASS__DESIGN_BINDING_REPORT_ACCEPTED__OWNER_SEED_DECISION_REQUIRED__NO_SCIENTIFIC_RUNTIME_AUTHORIZED`

Accepted Builder candidate: `202c71f757266eee38da7c52d56658680439d010`.

The zero-science report correctly freezes the non-seed contract for the smallest corrected-target HJB experiment and correctly fails closed on the unresolved initialization choice. Repository authority uniquely supports the call-725 `(20,20,2)` F-order grid, frozen household scalars, raw one-sided derivative construction, corrected D1/D3 selector contract, corrected D2 generator, and one implicit linear HJB step. It does not uniquely select a starting value function among the source-native call-725 initialization, the historical post-step143 terminal state, and the one-step MATLAB-faithful replay output.

None of those objects is a corrected-target fixed point. Therefore choosing among them is a substantive Owner scientific/provenance decision and cannot be delegated to Builder or Reviewer merely on numerical convenience, historical fixed-point proximity, expected selector success, or runtime considerations.

Reviewer scientific recommendation, not Owner adoption: prefer the source-native call-725 `hjb100_initialization.mat:v0` as the first corrected-diagnostic seed if the Owner wants the least path-dependent initialization. Its scientific rationale is that it is an already accepted numerical initialization with MATLAB/Python identity and is not itself the endogenous output of the source-faithful boundary/operator whose derivative state was shown to be incompatible with the corrected D1-D3 contract at Cells 4/8/10. This recommendation does not claim that the source-native seed is closer to the corrected fixed point or more likely to pass.

If the Owner instead prioritizes a continuation experiment from the historical source-faithful trajectory, the post-step143 state is also an admissible provenance choice, but that choice explicitly carries source-faithful path dependence into the corrected one-step experiment. The one-step replay output should be chosen only if the Owner specifically wants that distinct historical replay object; its numerical closeness to the terminal state is not itself scientific authority.

No corrected policy map, scalar root, HJB solve, KFE solve, MATLAB call, outer/firm/wage-return recalculation, GE, annual, shock, IRF or Results call is authorized by this acceptance.

Results eligibility=`FALSE`.
