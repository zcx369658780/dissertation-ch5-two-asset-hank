# Archived iteration and post operators

All indices are zero based. Grid is (b,a,z)=(20,20,2), Fortran state index=b_index+20*a_index+400*z_index; db=7/19, da=10/19. No scientific source or production entry changed.

DIRECT_ARCHIVE_OBSERVATION: four original CSR triples authenticated in original storage order; all 800x800, exact recorded hashes match. No source operator assembly.

| operator | stored nnz | max abs entry | max abs row sum | negative offdiag count | min offdiag |
|---|---|---|---|---|---|
| E03_iteration_G | 4031 | 17.6090646997271 | 0.00268084107604544 | 11 | -2.83801921035518 |
| E03_post_G | 3139 | 16.2540395284356 | 2.84019071084188 | 0 | 0 |
| E04_iteration_G | 3720 | 19.6674023814438 | 0.00268105538355606 | 23 | -3.86251208163602 |
| E04_post_G | 3125 | 18.4264398248055 | 3.86467005685863 | 0 | 0 |

PURE_ARCHIVE_ALGEBRA differences:

| difference | nonzero differences | max abs change | min row sum | max row sum |
|---|---|---|---|---|
| E03_post_minus_iteration | 2899 | 7.04097362702133 | -2.83801921035518 | 2.77555756156289e-15 |
| E04_post_minus_iteration | 2134 | 7.72502416327204 | -3.86251208163602 | 0.0026810553835559 |
| E04_post_minus_E03_post | 2655 | 9.22465316646517 | -3.86467005685863 | 1.41596989768209 |

Negative entries in a difference matrix are signed changes, not proof of a negative transition rate in either original matrix. KFE used the post matrix, not the iteration matrix. Iteration row-sum maxima about0.002681 are below historical homecrit0.01; no violation of that MATLAB threshold is asserted. Post row-sum nonconservation remains a distinct observed issue.

Top three changed entries for each comparison and source-row boundary/z summaries are in evidence/operator_metrics.json. BB/AAH components were not archived: component decomposition NOT_AVAILABLE. Exact source formula attribution, full MATLAB spdiags parity and causal explanation require future authorized work.
