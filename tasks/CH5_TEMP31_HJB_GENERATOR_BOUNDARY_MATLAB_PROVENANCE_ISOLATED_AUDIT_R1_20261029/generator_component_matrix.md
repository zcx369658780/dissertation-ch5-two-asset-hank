# Actual pure-fixture component matrices, row by row

Every matrix in this document is SYNTHETIC, not an archived historical HJB matrix. Each fixture calls the unmodified fixed pure builder exactly once. Reference entries are independently assembled by dense scalar index arithmetic and checked against all three real sparse components. Actual eight-rate input vectors, row losses, component nonzero entries and raw/public records are preserved in command_N_fixture_results.json. Zero-based rows/columns below; MATLAB uses+1.

For any row with coordinates(i,j,nz), let L_b=1_(i=0)*b_back+1_(i=I-1)*b_forward, and L_a=1_(j=0)*a_back+1_(j=J-1)*a_forward. Then BB*1=-L_b, AAH*1=-L_a, Bswitch*1=sum(Q[nz,:]), G*1=-L_b-L_a+sum(Q[nz,:]). The diagonal always subtracts the full signed rates. An outward positive rate is a negative row-mass loss; an outward negative rate creates positive row mass. Inward negative rates remain stored and may violate offdiagonal nonnegativity without violating row conservation.

A conservative finite-state CTMC generator needs offdiagonal>=0 and row sum0. A nonnegative-offdiagonal matrix with nonpositive row sums can instead be a killed-process subgenerator if that boundary interpretation is intended; this audit does not authorize or establish killing/absorbing semantics for the household assets. Positive row sums and negative offdiagonals require separate scrutiny. Small nonzero row sums alone are not proof of violating the original MATLAB tolerance.

## F1_VALID_INWARD_RATES — synthetic only

max_abs_row_sum=5.551115123125783e-17; min_offdiag=0.0; original_homecrit_pass=True.

| row(i,j,z) | BB nonzero col:value | AAH | Bswitch | G | G row sum | dropped rates |
|---|---|---|---|---|---:|---|
| 0(0, 0, 0) | 0:-0.2, 1:0.2 | 0:-0.05, 2:0.05 | 0:-0.333333333, 4:0.333333333 | 0:-0.583333333, 1:0.2, 2:0.05, 4:0.333333333 | 5.5511151231257827e-17 | none |
| 1(1, 0, 0) | 0:0.3, 1:-0.3 | 1:-0.05, 3:0.05 | 1:-0.333333333, 5:0.333333333 | 0:0.3, 1:-0.683333333, 3:0.05, 5:0.333333333 | -5.5511151231257827e-17 | none |
| 2(0, 1, 0) | 2:-0.2, 3:0.2 | 0:0.07, 2:-0.07 | 2:-0.333333333, 6:0.333333333 | 0:0.07, 2:-0.603333333, 3:0.2, 6:0.333333333 | 5.5511151231257827e-17 | none |
| 3(1, 1, 0) | 2:0.3, 3:-0.3 | 1:0.07, 3:-0.07 | 3:-0.333333333, 7:0.333333333 | 1:0.07, 2:0.3, 3:-0.703333333, 7:0.333333333 | -5.5511151231257827e-17 | none |
| 4(0, 0, 1) | 4:-0.2, 5:0.2 | 4:-0.05, 6:0.05 | 0:0.333333333, 4:-0.333333333 | 0:0.333333333, 4:-0.583333333, 5:0.2, 6:0.05 | 5.5511151231257827e-17 | none |
| 5(1, 0, 1) | 4:0.3, 5:-0.3 | 5:-0.05, 7:0.05 | 1:0.333333333, 5:-0.333333333 | 1:0.333333333, 4:0.3, 5:-0.683333333, 7:0.05 | -5.5511151231257827e-17 | none |
| 6(0, 1, 1) | 6:-0.2, 7:0.2 | 4:0.07, 6:-0.07 | 2:0.333333333, 6:-0.333333333 | 2:0.333333333, 4:0.07, 6:-0.603333333, 7:0.2 | 5.5511151231257827e-17 | none |
| 7(1, 1, 1) | 6:0.3, 7:-0.3 | 5:0.07, 7:-0.07 | 3:0.333333333, 7:-0.333333333 | 3:0.333333333, 5:0.07, 6:0.3, 7:-0.703333333 | -5.5511151231257827e-17 | none |

## F2_SYNTHETIC_SMALL_UPPER_B_LEAK — synthetic only

max_abs_row_sum=0.00045691399330394233; min_offdiag=0.0; original_homecrit_pass=True.

| row(i,j,z) | BB nonzero col:value | AAH | Bswitch | G | G row sum | dropped rates |
|---|---|---|---|---|---:|---|
| 0(0, 0, 0) | zero | zero | 0:-0.333333333, 4:0.333333333 | 0:-0.333333333, 4:0.333333333 | 0 | none |
| 1(1, 0, 0) | 1:-0.000456913993 | zero | 1:-0.333333333, 5:0.333333333 | 1:-0.333790247, 5:0.333333333 | -0.00045691399330394233 | BB forward 0.00045691399330394233 |
| 2(0, 1, 0) | zero | zero | 2:-0.333333333, 6:0.333333333 | 2:-0.333333333, 6:0.333333333 | 0 | none |
| 3(1, 1, 0) | zero | zero | 3:-0.333333333, 7:0.333333333 | 3:-0.333333333, 7:0.333333333 | 0 | none |
| 4(0, 0, 1) | zero | zero | 0:0.333333333, 4:-0.333333333 | 0:0.333333333, 4:-0.333333333 | 0 | none |
| 5(1, 0, 1) | zero | zero | 1:0.333333333, 5:-0.333333333 | 1:0.333333333, 5:-0.333333333 | 0 | none |
| 6(0, 1, 1) | zero | zero | 2:0.333333333, 6:-0.333333333 | 2:0.333333333, 6:-0.333333333 | 0 | none |
| 7(1, 1, 1) | zero | zero | 3:0.333333333, 7:-0.333333333 | 3:0.333333333, 7:-0.333333333 | 0 | none |

## F3_SYNTHETIC_UPPER_A_NEGATIVE_RATE — synthetic only

max_abs_row_sum=0.0; min_offdiag=-0.081; original_homecrit_pass=True.

| row(i,j,z) | BB nonzero col:value | AAH | Bswitch | G | G row sum | dropped rates |
|---|---|---|---|---|---:|---|
| 0(0, 0, 0) | zero | zero | 0:-0.333333333, 4:0.333333333 | 0:-0.333333333, 4:0.333333333 | 0 | none |
| 1(1, 0, 0) | zero | zero | 1:-0.333333333, 5:0.333333333 | 1:-0.333333333, 5:0.333333333 | 0 | none |
| 2(0, 1, 0) | zero | 0:-0.081, 2:0.081 | 2:-0.333333333, 6:0.333333333 | 0:-0.081, 2:-0.252333333, 6:0.333333333 | 0 | none |
| 3(1, 1, 0) | zero | 1:-0.081, 3:0.081 | 3:-0.333333333, 7:0.333333333 | 1:-0.081, 3:-0.252333333, 7:0.333333333 | 0 | none |
| 4(0, 0, 1) | zero | zero | 0:0.333333333, 4:-0.333333333 | 0:0.333333333, 4:-0.333333333 | 0 | none |
| 5(1, 0, 1) | zero | zero | 1:0.333333333, 5:-0.333333333 | 1:0.333333333, 5:-0.333333333 | 0 | none |
| 6(0, 1, 1) | zero | 4:-0.081, 6:0.081 | 2:0.333333333, 6:-0.333333333 | 2:0.333333333, 4:-0.081, 6:-0.252333333 | 0 | none |
| 7(1, 1, 1) | zero | 5:-0.081, 7:0.081 | 3:0.333333333, 7:-0.333333333 | 3:0.333333333, 5:-0.081, 7:-0.252333333 | 0 | none |

## F4_COMPOSITE_SIGNED_BOUNDARY_COUNTEREXAMPLE — synthetic only

max_abs_row_sum=0.004000000000000059; min_offdiag=-0.081; original_homecrit_pass=True.

| row(i,j,z) | BB nonzero col:value | AAH | Bswitch | G | G row sum | dropped rates |
|---|---|---|---|---|---:|---|
| 0(0, 0, 0) | 0:-0.2, 1:0.2 | 0:-0.05, 2:0.05 | 0:-0.333333333, 4:0.333333333 | 0:-0.583333333, 1:0.2, 2:0.05, 4:0.333333333 | 5.5511151231257827e-17 | none |
| 1(1, 0, 0) | 0:0.3, 1:-0.300456914 | 1:-0.05, 3:0.05 | 1:-0.333333333, 5:0.333333333 | 0:0.3, 1:-0.683790247, 3:0.05, 5:0.333333333 | -0.00045691399330399785 | BB forward 0.00045691399330394233 |
| 2(0, 1, 0) | 2:-0.2, 3:0.2 | 0:-0.081, 2:0.081 | 2:-0.333333333, 6:0.333333333 | 0:-0.081, 2:-0.452333333, 3:0.2, 6:0.333333333 | 0 | none |
| 3(1, 1, 0) | 2:0.3, 3:-0.3 | 1:-0.081, 3:0.079 | 3:-0.333333333, 7:0.333333333 | 1:-0.081, 2:0.3, 3:-0.554333333, 7:0.333333333 | -0.0020000000000000573 | AAH forward 0.002 |
| 4(0, 0, 1) | 4:-0.196, 5:0.2 | 4:-0.05, 6:0.05 | 0:0.333333333, 4:-0.333333333 | 0:0.333333333, 4:-0.579333333, 5:0.2, 6:0.05 | 0.0040000000000000591 | BB backward -0.004 |
| 5(1, 0, 1) | 4:0.3, 5:-0.3 | 5:-0.05, 7:0.05 | 1:0.333333333, 5:-0.333333333 | 1:0.333333333, 4:0.3, 5:-0.683333333, 7:0.05 | -5.5511151231257827e-17 | none |
| 6(0, 1, 1) | 6:-0.2, 7:0.2 | 4:-0.081, 6:0.081 | 2:0.333333333, 6:-0.333333333 | 2:0.333333333, 4:-0.081, 6:-0.452333333, 7:0.2 | 0 | none |
| 7(1, 1, 1) | 6:0.3, 7:-0.3 | 5:-0.081, 7:0.081 | 3:0.333333333, 7:-0.333333333 | 3:0.333333333, 5:-0.081, 6:0.3, 7:-0.552333333 | -5.5511151231257827e-17 | none |

F1: inward nonnegative rates conserve mass. F2: a positive b-forward rate at row1, coordinate(1,0,0), has its grid-invalid neighbor dropped even though the global column2 exists; its diagonal still loses epsilon. F3: upper-a rows2/3/6/7 retain-.081 at columns0/1/4/5 with+.081 in the AAH diagonal, preserving row sum but violating offdiagonal positivity. This synthetic number is not proof that historical Arm B's-.081 was produced by that formula. F4 combines independent signed-rate mechanisms: row1 negative leakage, row3 additional outward-a loss, row4 positive row mass from a dropped negative backward-b rate, and retained negative upper-a rates.

Some deliberately injected boundary vectors may not be reachable under every condition of the actual household selector; these are builder counterexamples, not new household simulations or historical truth. In the frozen Q, Bswitch alone has offdiagonal0 or1/3 and zero row sums, so it cannot by itself create a negative offdiagonal. Exact historical BB-versus-AAH cell attribution still needs archived actual rates or matrices, which are absent. All tests are pure matrix assembly; no policy, root or HJB function was called.
