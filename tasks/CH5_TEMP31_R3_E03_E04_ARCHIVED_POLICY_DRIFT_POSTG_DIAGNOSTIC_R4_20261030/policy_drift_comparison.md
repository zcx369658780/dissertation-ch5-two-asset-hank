# Saved fields, drifts and last-iteration rates

All indices are zero based. Grid is (b,a,z)=(20,20,2), Fortran state index=b_index+20*a_index+400*z_index; db=7/19, da=10/19. No scientific source or production entry changed.

DIRECT_ARCHIVE_OBSERVATION for original fields; PURE_ARCHIVE_ALGEBRA for differences. All contrasts below are E04 minus E03.

| field | min diff | max diff | signed mean | mean absolute | max absolute | median |
|---|---|---|---|---|---|---|
| value | 0.0232584922062093 | 0.0546145291050939 | 0.0372527399612753 | 0.0372527399612753 | 0.0546145291050939 | 0.0375562119341269 |
| consumption | -3.57588412345375 | 0.105072086554692 | -0.625313853721364 | 0.634298329578951 | 3.57588412345375 | -0.33164155476446 |
| labor | -0.000738980623475882 | 0.0870270341376055 | 0.0152049727418893 | 0.0152750658231062 | 0.0870270341376055 | 0.00803295618990985 |
| utility | -0.0411755857448199 | 0.000717190895908965 | -0.00660696173249981 | 0.00666701851353577 | 0.0411755857448199 | -0.00316107963275469 |
| mu_a | -1.06870229244562 | 0.643176694758302 | 0.100100189929542 | 0.244237996368948 | 1.06870229244562 | 0.167505638426063 |
| mu_b | -0.521673120198663 | 5.6419434870149 | 0.919533588577736 | 0.952758225432351 | 5.6419434870149 | 0.492153504115419 |
| b_backward | -10.0230849680211 | 1.41597010292676 | -1.13066216968696 | 1.36666841159747 | 10.0230849680211 | 0 |
| b_forward | -0.92070947273459 | 7.34911875299496 | 1.36521471359547 | 1.65654740735995 | 7.34911875299496 | 1.44271779874883 |
| a_backward | -1.22203572004077 | 2.03053435564667 | -0.122426813263406 | 0.396288645498277 | 2.03053435564667 | -0.129401596566654 |
| a_forward | 0 | 0.636561254699468 | 0.0677635476027241 | 0.0677635476027241 | 0.636561254699468 | 0 |

Drift signs use tolerance1e-12; -1/0/+1 denote negative/near-zero/positive.

| drift | negative to positive | positive to negative | zero to nonzero | nonzero to zero |
|---|---|---|---|---|
| mu_a | 168 | 57 | 0 | 0 |
| mu_b | 106 | 11 | 0 | 5 |

High-b last four grid positions, upper-b boundary, and first two a positions are explicit overlapping masks; lower/interior/upper partitions and z partitions are separate. Full group means, quantiles and sign tables are in evidence/policy_drift_metrics.json.

| field | group | mean signed difference | max absolute difference |
|---|---|---|---|
| mu_a | b_upper | -0.0762406399449537 | 1.06870229244562 |
| mu_a | high_b_last4 | -0.0767932135752946 | 1.06870229244562 |
| mu_a | a_lower | 0 | 0 |
| mu_a | a_lower_near_first2 | 0.0272077757153269 | 0.0897518639706645 |
| mu_b | b_upper | 1.38829868439641 | 3.69351055803716 |
| mu_b | high_b_last4 | 2.00066028070931 | 5.6419434870149 |
| mu_b | a_lower | 0.392299699432282 | 2.58463344525731 |
| mu_b | a_lower_near_first2 | 0.384599122851243 | 2.65031038981973 |
| consumption | b_upper | -0.936551197591094 | 2.20538587133357 |
| consumption | high_b_last4 | -1.34052604857284 | 3.57588412345375 |
| consumption | a_lower | -0.179350154019235 | 1.84539783814589 |
| consumption | a_lower_near_first2 | -0.19718644522908 | 1.8513739336219 |
| labor | b_upper | 0.0218151285281977 | 0.0486780395655756 |
| labor | high_b_last4 | 0.0325991780164333 | 0.0870270341376055 |
| labor | a_lower | 0.00483168397431054 | 0.0416993375558204 |
| labor | a_lower_near_first2 | 0.00521183908311526 | 0.0418174543298815 |

POLICY_LABELS_NOT_ARCHIVED: transfer, adjustment_cost, liquid_label, transfer_label and complete iteration snapshots absent. Saved backward/forward rates belong to last recorded HJB iteration; do not represent a freshly selected post policy. Co-location with changed density supports only a descriptive association, not proof of an optimal-choice switch causing the distribution jump.
