from __future__ import annotations


ALPHA_LOWER = 0.2
ALPHA_UPPER = 0.8
LAMBDA_CANDIDATES = (1.0, 0.5, 0.25)
HYSTERESIS_ENTER_CANDIDATES = (0.10, 0.05, 0.02)
MIN_CONSECUTIVE_CANDIDATES = (2, 3, 5)


def alpha_contract(alpha_raw: float) -> dict[str, float | bool | str]:
    if alpha_raw < ALPHA_LOWER:
        return {"alpha_raw": alpha_raw, "alpha_used": ALPHA_LOWER, "alpha_clip_flag": True,
                "alpha_clip_reason": "CLIPPED_TO_LOWER_OWNER_BOUND"}
    if alpha_raw > ALPHA_UPPER:
        return {"alpha_raw": alpha_raw, "alpha_used": ALPHA_UPPER, "alpha_clip_flag": True,
                "alpha_clip_reason": "CLIPPED_TO_UPPER_OWNER_BOUND"}
    return {"alpha_raw": alpha_raw, "alpha_used": alpha_raw, "alpha_clip_flag": False,
            "alpha_clip_reason": "NONE_INSIDE_RANGE"}


def damp(prior_used: float, composite_raw: float, lam: float) -> float:
    if not 0.0 < lam <= 1.0:
        raise ValueError("lambda must satisfy 0 < lambda <= 1")
    return (1.0 - lam) * prior_used + lam * composite_raw


def hysteresis_candidates() -> tuple[tuple[float, float, int], ...]:
    return tuple((enter, 2.0 * enter, consecutive)
                 for enter in HYSTERESIS_ENTER_CANDIDATES
                 for consecutive in MIN_CONSECUTIVE_CANDIDATES)
