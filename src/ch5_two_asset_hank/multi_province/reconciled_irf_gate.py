"""Dynamic HANK evidence gate; conditional static paths cannot supply evidence."""
REQUIRED = (
    "dynamic_household_HJB_terminal_value",
    "forward_KFE_distribution_conservation",
    "asset_public_capital_debt_transitions",
    "forward_looking_firm_pricing_inflation",
    "monetary_fiscal_intertemporal_closure",
    "each_period_market_clearing",
    "accepted_initial_terminal_HANK_steady_states",
    "shock_time_scale_terminal_error",
)
def irf_gate(evidence=None):
    evidence={} if evidence is None else evidence
    # Require accepted scientific evidence references, not boolean placeholder PASS.
    missing=[key for key in REQUIRED if not isinstance(evidence.get(key),dict)
             or evidence[key].get("independent_acceptance")!="ACCEPTED"
             or not evidence[key].get("reference")]
    return dict(status="IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE" if missing else "READY_FOR_SEPARATE_IRF_AUTHORIZATION",
                missing=missing,dynamic_execution_authorized=False,Results=False)
