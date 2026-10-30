# Bounded static parity review

SOURCE_EXCERPT_ONLY throughout the MATLAB comparison; actual Python source bytes independently verified at fixed Ref.

SOURCE_STATIC_MATCH (bounded): last-iteration saved-policy timing; scalar post upwind rates conditional on equal drift; BB+AAH+Bswitch sum; F-order indexing; transpose/pin-row/normalization sequence. Python source r=i+I*j+I*J*z gives row-origin/column-destination links. It omits an out-of-grid offdiagonal but always retains center=-(back+forward).

For nonnegative post rates and h>0, an axis lower row loses max(-drift,0)/h and upper row loses max(drift,0)/h; an interior row sums to0. A corner adds both axis contributions. Positive outward drift at the upper boundary is sufficient for a negative contribution from that axis; it does not prove actual full-row loss at every historical state. Q row sum contributes separately. Signed iteration rates are a different case and may generate negative offdiagonals; do not apply the post nonnegative-rate classification to them.

SOURCE_STATIC_DIFFERENCE: original MATLAB114-239 excerpt includes an iteration A2max>homecrit BREAK. The fixed TEMP31 driver85-118 and export596-629 lack that internal row-sum branch; their stopping branch is value-change convergence. External R3 trace observations and warning reports are not equivalent to an internal early BREAK. No source repair authorized.

SOURCE_STATIC_DIFFERENCE in representation / SOURCE_PARITY_GAP in value: the MATLAB263 excerpt contains -Cmin, while the inspected historical export liquid budget160-166 has no explicit Cmin. The export caller passes C-Tt445-455. Without the original Cmin value or an equivalence witness, neither equality nor a nonzero numerical defect is established.

Approved wage-context distinction: corrected HJB93 uses net composite wage directly; historical export604 multiplies by(1-tau), and export local policy347/162 retains its historical tau/migration factors. These are separate frozen paths. Gross-to-net wage and migration identities must hold at the interface; this task does not globally zero tau or re-certify the wage provenance. The corrected selector definition was not among the four inspected files; its exact scalar mu formula remains a bounded gap, rather than borrowed silently from historical export.

Post timing: Python assembles policy from old=V_k, solves to V_(k+1), then stops or continues. Returned value is V_(k+1), while returned policy/mu arrays and post rates are the last V_k policy. No final policy reselection occurs. MATLAB262-264 excerpt also uses saved last C,l,dh/Idh, so this timing is compatible; it does not certify identical policies or their optimality residual.

Spdiags: a square-strip entry on diagonal d requires storage band_d[r+d]=A[r,r+d]. For b,+1 requires Z(r) at r+1 and -1 requires X(r) at r-1. For a replace1 by I. The excerpt descriptions updiag=Z(i-1) and lowdiag=X(i+1) are compatible with this local alignment. Full a/z-block seam zeroing and exact lengths/padding of [updiag;0]/[updiagh;0] are not supplied, so complete original sparse placement is SOURCE_PARITY_GAP, not a blanket STATIC_MATCH. The one stdlib toy checks only artificial required alignment and masks.

FULL_MATLAB_PYTHON_RUNTIME_PARITY=NOT_TESTED. STRICT_STATIONARY_CERTIFICATION=FALSE_INHERITED_R3_R4. OWNER_DECISION_REQUIRED for obtaining complete authorized source context, any MATLAB runtime comparison or scientific修复.
