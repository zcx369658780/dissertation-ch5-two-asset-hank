"""Pure saved-scalar diagnostics. No production imports, initialization or solves."""
import math
import sys

EPS = sys.float_info.epsilon
BOUNDS = {'ra': (.02, .09), 'wjt': (.8, 1.3)}


def close(x, y):
    return math.isfinite(x) and math.isfinite(y) and abs(x-y) <= 128*EPS*max(1., abs(x), abs(y))


def classify(value, low, high, provenance='CAPTURED', phase='post_firm'):
    if value is None:
        return {'status': 'MISSING', 'finite': False}
    x = float(value)
    if not math.isfinite(x):
        return {'status': 'NONFINITE', 'finite': False}
    if provenance == 'ROUNDED_LOG':
        return {'status': 'ROUNDED_UNCERTAIN', 'finite': True}
    return {'status': 'INITIALIZATION' if phase == 'initialization' else 'OBSERVED',
            'finite': True, 'lower_distance': x-low, 'upper_distance': high-x,
            'strict_below': x < low, 'strict_above': x > high,
            'exact_lower': x == low, 'exact_upper': x == high,
            'near_lower': close(x, low), 'near_upper': close(x, high),
            'outside_by_roundoff': (x < low and close(x, low)) or (x > high and close(x, high)),
            'near_inside': low < x < high and (close(x, low) or close(x, high))}


def controller(max_gap, steady_state, exited, complete=True):
    if not complete:
        return 'INTERRUPTED_BEFORE_CONTROLLER'
    if exited:
        return 'CONVERGENCE_EXIT_FIRST'
    if max_gap is None or not math.isfinite(max_gap):
        return 'UNKNOWN_GATE'
    return 'ENABLED' if max_gap < .1 and steady_state == 1 else 'CLOSED'


def gov_multiplier(ra, low=.02, high=.09):
    if ra < low + .02:
        return .9
    if ra > high - .02:
        return 1.1
    return 1.


def portfolio(old_ra, ratios):
    n = len(ratios)
    total = sum(ratios[i]*old_ra[i] for i in range(n))
    return [(1-ratios[i])*old_ra[i]+ratios[i]*(total-ratios[i]*old_ra[i])/(n-1) for i in range(n)]


def weight_sums(ratios):
    return [1-r+sum(r*q/(len(ratios)-1) for j,q in enumerate(ratios) if j!=i) for i,r in enumerate(ratios)]


def raw_prices(y, k, labor, mt, alpha, z_used=None, rk=None, pit=.02, theta=100., delta=.025, tax=.25):
    """Price expressions only, supplied saved/derived operands; never evaluate a firm turn."""
    rent = mt*alpha/(k/y) if rk is None else rk
    profit = max((1-mt)*y-theta/2*pit**2*y, 0.)
    wage = mt*(1-alpha)*z_used*(k/labor)**alpha if z_used is not None else mt*(1-alpha)*y/labor
    ra0 = rent-delta+profit*(1-tax)/k
    return {'ra0': ra0, 'wt0': wage, 'rk': rent, 'divrate': profit*(1-tax)/k,
            'profit': profit, 'ra': min(.09, max(.02, ra0)), 'wjt': min(1.3, max(.8, wage))}


def spell(records):
    """Missing steps break spells. Input is (step, exact_contact) for one phase/regime."""
    first = last = prev = None
    longest = run = contacts = 0
    for step, hit in sorted(records):
        if hit:
            contacts += 1
            first = step if first is None else first
            last = step
            run = run+1 if prev is not None and step == prev+1 else 1
            longest = max(longest, run)
            prev = step
        else:
            run = 0; prev = None
    return dict(observed=len(records), contacts=contacts, first=first, last=last,
                longest_confirmed=longest, frequency=contacts/len(records) if records else None)
