"""Pure grid and accounting helpers; never imports scientific runtime."""
import math
import numpy as np


def expand_b(old_b, extra=19):
    old = np.asarray(old_b, dtype=np.float64)
    if old.shape != (20,):
        raise ValueError("expected captured 20-node liquid grid")
    db = old[1] - old[0]
    values = old.tolist()
    for _ in range(extra):
        values.append(np.float64(values[-1] + db))
    return np.asarray(values, dtype=np.float64), db


def pin_details(b, a, z):
    shape = (len(b), len(a), len(z))
    count = math.prod(shape)
    k = math.floor(.37 * count) - 1
    i, j, n = np.unravel_index(k, shape, order="F")
    return {"state_count": count, "k_zero_based": k, "i_b_zero_based": int(i),
            "j_a_zero_based": int(j), "i_z_zero_based": int(n),
            "b": float(b[i]), "a": float(a[j]), "z": float(z[n])}


def boundary_leak(mu_b, mu_a, db, da):
    shape = np.asarray(mu_b).shape
    leak = np.zeros(shape)
    faces = {
        "lower_b": np.maximum(-mu_b[0], 0.0) / db,
        "upper_b": np.maximum(mu_b[-1], 0.0) / db,
        "lower_a": np.maximum(-mu_a[:, 0], 0.0) / da,
        "upper_a": np.maximum(mu_a[:, -1], 0.0) / da,
    }
    leak[0] += faces["lower_b"]
    leak[-1] += faces["upper_b"]
    leak[:, 0] += faces["lower_a"]
    leak[:, -1] += faces["upper_a"]
    return faces, leak


def mass_regions(density, b, cell_weight):
    d = np.asarray(density)
    return {
        "total": float(d.sum() * cell_weight),
        "b_le_5": float(d[np.asarray(b) <= 5.0].sum() * cell_weight),
        "b_gt_5": float(d[np.asarray(b) > 5.0].sum() * cell_weight),
        "top_face": float(d[-1].sum() * cell_weight),
        "negative_count": int(np.sum(d < 0)),
        "negative_mass": float(np.minimum(d, 0).sum() * cell_weight),
    }
