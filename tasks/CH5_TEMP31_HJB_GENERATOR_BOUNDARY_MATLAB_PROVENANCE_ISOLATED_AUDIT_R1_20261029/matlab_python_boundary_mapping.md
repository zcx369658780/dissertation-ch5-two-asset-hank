# Bounded MATLAB excerpt / authenticated Python mapping

MATLAB authority is solely the frozen publication contract and its GPT-extracted line evidence. Codex did not read the ZIP or original .m bytes. matlab_excerpt_provenance.json preserves the claimed original file/ZIP byte identities with that attribution. MATLAB_RAW_LOCAL_VERIFICATION=NOT_AVAILABLE; source comparison is GPT_EXCERPT_PROVENANCE_ONLY. No matching frozen MATLAB filenames were found in the fixed isolated Git source tree metadata; this is not a search of protected local directories and not a global absence claim.

Python paths below are all src/ch5_two_asset_hank/. Line numbers were read from the fixed raw blobs, not inferred from older versions.

| Original excerpt | Python fixed location | Relation and limit |
|---|---|---|
| HANK_2ASSETS_HJB.m155-157 X/Y/Z | temp31_netwage_policy.py263-270; temp31_netwage_hjb.py108 | X=iteration_b_backward_rate=-(IcB*scB+IdhB*sdhB)/db; Z=iteration_b_forward_rate=(IcF*scF+IdhF*sdhF)/db; Y=-X-Z. Predicate reachability/full MATLAB selector equivalence not certified. |
| .m185-189 BB/spdiags offsets+/-1 | matlab_faithful_operator.py19-45,55; HJB108,110 | BB uses spatial b-axis neighbors r+/-1, diagonal -(X+Z). Python checks actual i-boundary, so an index inside global8x8 can still be dropped as a grid wrap. Original complete spdiags padding/vector alignment is not included in the frozen excerpt; exact whole-matrix equivalence is NOT established. |
| .m190-198 MhB/MhF | temp31_netwage_policy.py227-232 | Interior mh_b=min(shadow_transfer_b,0); mh_f=max(shadow_transfer_f,0)+effective_return*a. Upper a explicitly overrides mh_b=shadow_transfer_b+effective_return*a_max and mh_f=0. This is a semantic match to the quoted upper-bound formula, not a complete raw-source comparison. |
| .m190-198 chih/yyh/zetah | policy261-262; operator43,56 | chih=-MhB/da maps to backward-a rate; zetah=MhF/da to forward-a; yyh=(MhB-MhF)/da equals negative sum of these rates. A positive upper-bound MhB produces a negative retained inward rate. |
| .m226-233 AAH and offsets+/-I | operator36,39-43,56 | AAH moves by2 in this I=2 fixture; diagonal remains negative rate sum. Original full reshapes/shifts and boundary padding still require raw MATLAB. |
| .m226-233 A=BB+AAH+Bswitch | operator55-59 | Actual Python full=bb+aah+bswitch, Bswitch=kron(Q,I_(I*J)). Under the frozen two-state Q, switches are z-state transitions, not province migration. Full original Bswitch construction is not present in the excerpt. |
| .m233-239 A2max and homecrit; multi_prov_HANK_12sts.m18 | HJB110-113 and HJBNumerics36-40 | MATLAB quote checks max(abs(sum(A,2)))>.01 before inversion. Python source has no corresponding homecrit field/check in this HJB route. This is a confirmed bounded excerpt-level difference; the historical4.56914e-4 would nevertheless remain below that original threshold. |
| .m185-189 BB2max | pure BB component diagnostic | max(sum(BB,2)) is signed; it can be0 even when another row is negative. It differs from max(abs(sum(A,2))). Do not confuse either with offdiagonal positivity. |
| .m240-244 implicit step | HJB111-114 | (1/Delta+rho)I-G and u+V_old/Delta, F-order flatten/reshape, real SciPy sparse solve. No such solver is called by this audit. |
| HANK_mp_1turn.m15/46/50 | future methodology only | Household first, firm update, composite wages next is coarse excerpt timing; no empirical first-round wage semantics or complete production map is inferred. |

Fortran zero-based row r=i+j*I+nz*I*J corresponds to MATLAB one-based r+1. BB b-neighbors are r+/-1, AAH a-neighbors r+/-I, and with I=J=2 the switching neighbor is r+/-4. These offsets are distinct for the8-state fixtures; row sums and component labels must not be confused with the destination-row/origin-column labor matrix convention.

The corrected TEMP31 net wage and previously authorized tax removal are intentionally retained. This mapping does not restore an old tax wedge or claim the whole corrected household code is an untouched MATLAB clone. Source-faithful rate algebra and mathematical generator defects can coexist. Any future choice between archival replication and a scientifically corrected boundary scheme requires a new Owner decision; no fix is made here.
