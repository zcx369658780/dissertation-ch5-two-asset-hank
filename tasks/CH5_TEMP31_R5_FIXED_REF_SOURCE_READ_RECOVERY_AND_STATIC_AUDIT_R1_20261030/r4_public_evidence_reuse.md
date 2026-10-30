# R4 public evidence reuse, without NPZ access

Sources: fixed R4 seal5e1933e4c166fa40b95c82bed377538d843c7576 row-loss/operator reports; fixed independent review1033b4a0531613093ce13789e3916fd228ae9b5b, Blob2b079567bd03ade8ef9f2c37944be7bd9fdfc20a. Both reports were fetched and raw-byte verified again in this recovery task.

| point | post max abs row sum | nonconserving source rows | original post transpose residual inf | destination pin equation | main source loss indices |
|---|---|---|---|---|---|
| E03 | 2.840190710841881 | 20 | .32169695841610524 | 295 | 699 / 679 / 659, b upper,z1 |
| E04 | 3.864670056858631 | 29 | 2.9445205842114848 | 295 | 299 / 279 / 259, b upper,z0 |

Source row295 sums are near0: about5.55e-17 and4.44e-16. Other799 destination equations have residual maxima about1.249e-16 and7.497e-16. Source loss g_i*sum_jG_ij is indexed by the departing state; (G.T@g)_j is a destination-equation residual. They are linked by summing all states, not by identifying index295 as the origin of all loss.

The observed b-upper localization is consistent with retaining the outward diagonal and omitting the outward edge. This is a conditional static mechanism, not a fresh reconstruction of historical row rates or proof of original MATLAB runtime behavior. Other possible contributions include a-boundary outward drift, Q row-sum convention, different policy/drift formulas and strip padding/alignment. R4 did not archive component BB/AAH matrices or full policy labels.

Iteration row-sum maxima .0026808411/.0026810554 are below the original .01 homecrit; post maxima are different. Iteration negative offdiagonals11/23 and post negative offdiagonals0/0 remain separate risks. No claim that the observed iteration rows violated original homecrit. No NPZ or raw800 arrays opened in this task.

R4 review A independently verifies28/28 public GitHub files; B distinguishes public20-bin checks from executor-local archive witness; C leaves strict stationarity, causal mechanism and full parity uncertified. This recovery does not reclassify that evidence as local MATLAB execution.
