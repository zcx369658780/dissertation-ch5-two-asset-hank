"""Single national tax and explicit synthetic mobility-cost ownership."""
from math import isfinite

UNITS = ("MU_10WAN_YUAN", "NU_100_PERSONS", "MODEL_TIME")

def net_prices(wages, tax, costs, cost_owner=None, *, units=UNITS):
    if tuple(units) != UNITS:
        raise ValueError("incompatible economic units")
    n = len(wages)
    if not n or not isfinite(tax) or not 0 <= tax < 1:
        raise ValueError("one national proportional wage tax required")
    if len(costs) != n or any(len(row) != n for row in costs):
        raise ValueError("destination rows / origin columns required")
    if any(not isfinite(w) or w <= 0 for w in wages):
        raise ValueError("positive gross wages required")
    if any(not isfinite(c) or c < 0 or tax+c >= 1 for row in costs for c in row):
        raise ValueError("invalid mobility wedge")
    if any(c for row in costs for c in row) and cost_owner not in (
        "resource", "intermediary", "government_fee"
    ):
        raise ValueError("nonzero cost needs one explicit SYNTHETIC_SCENARIO")
    return [[wages[j]*(1-tax-costs[j][i]) for i in range(n)] for j in range(n)]

def check_income(gross, net, tax, mobility, tolerance=2e-12):
    values = (gross, net, tax, mobility)
    if any(not isfinite(v) for v in values):
        raise ValueError("nonfinite cash flow")
    if abs(gross-net-tax-mobility) > tolerance*max(1, abs(gross)):
        raise ValueError("income identity violated, including double taxation")
    return True

def rescale_labor_weight(weight, money_scale, gamma):
    if min(weight, money_scale) <= 0:
        raise ValueError("positive scaling required")
    return weight*money_scale**(1-gamma)
