"""CES index duality and exact finite-state distribution integration."""
from math import fsum, isfinite

def dual_wages(v, phi, eta):
    n = len(v)
    if not n or not isfinite(eta) or eta <= 0 or len(phi) != n:
        raise ValueError("invalid CES dimensions or curvature")
    if any(len(row) != n for row in v+phi):
        raise ValueError("square destination-origin matrix required")
    if any(not isfinite(x) or x <= 0 for matrix in (v, phi) for row in matrix for x in row):
        raise ValueError("positive finite CES inputs required")
    power = 1+1/eta
    return [fsum(phi[j][i]**(-1/eta)*v[j][i]**power for j in range(n))**(1/power)
            for i in range(n)]

def bilateral_controls(ell, origin, v, phi, eta, wages=None):
    if not isfinite(ell) or ell < 0:
        raise ValueError("invalid labor index")
    W = dual_wages(v, phi, eta) if wages is None else wages
    return [ell*phi[j][origin]**(-1/eta)*(v[j][origin]/W[origin])**(1/eta)
            for j in range(len(v))]

def integrate_distribution(population, distributions, labor_indices, v, phi, eta):
    n = len(population)
    if len(distributions) != n or len(labor_indices) != n:
        raise ValueError("origin axis mismatch")
    W = dual_wages(v, phi, eta)
    flows = [[0.0]*n for _ in range(n)]
    for i in range(n):
        states = distributions[i]
        if not isfinite(population[i]) or population[i] <= 0:
            raise ValueError("positive population required")
        if len(states) != len(labor_indices[i]) or abs(fsum(s["p"] for s in states)-1) > 1e-12:
            raise ValueError("normalized finite-state distribution required")
        for s, ell in zip(states, labor_indices[i]):
            if s["p"] < 0 or s["z"] <= 0 or not all(isfinite(s[k]) for k in ("p","z")):
                raise ValueError("invalid distribution")
            h = bilateral_controls(ell, i, v, phi, eta, W)
            for j in range(n):
                flows[j][i] += population[i]*s["p"]*s["z"]*h[j]
    return flows, [fsum(row) for row in flows]

def comparable_labor_reference(previous, current, *, previous_role, current_role,
                               previous_unit, current_unit, previous_axis, current_axis,
                               previous_time, current_time):
    if (previous_role != "destination_total" or current_role != previous_role or
        previous_unit != current_unit or previous_axis != current_axis or
        previous_time != "economic_t_minus_1" or current_time != "economic_t"):
        raise ValueError("labor reference is not economically comparable")
    if current <= 0 or not all(isfinite(x) for x in (previous,current)):
        raise ValueError("invalid labor")
    return (previous-current)/current
