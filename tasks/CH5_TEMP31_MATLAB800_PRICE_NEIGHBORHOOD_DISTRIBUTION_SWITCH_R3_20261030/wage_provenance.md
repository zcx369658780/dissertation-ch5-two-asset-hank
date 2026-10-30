# Source wages and cold initialization

E08 alone uses numerical_bootstrap19 -> netwage_inputs, NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL. The other11 points use actual SyntheticNetWageCalculation -> calculated_round_record -> later_net_wage_record -> netwage_inputs, A/B, phi_ji1, sigma0, tau_j.05, phi_l5, alphal1, firm_wage=wt/(.95*2^(5/6)). All12 actual source wages were checked before the first HA initializer/HJB/KFE. Error<=1e-12, source context/order preserved, no second tax or migration wedge. The iteration1/2 tags are counterfactual provenance labels, never real firm updates or empirical wages.

Each point has exactly one fresh original initializer and its own V0/l0,800 root cells and measured brentq calls. Initialization/consumption metadata and F hashes are recorded; no warm start. The effective_return-squared term and original labor-root algorithm remain unchanged; scientific interpretation is unresolved. No actual MATLAB runtime was used.
