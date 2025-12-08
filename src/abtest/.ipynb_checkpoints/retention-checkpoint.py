# src/abtest/retention.py

import numpy as np
from .config import retention_points

def build_retention_function(points_dict: dict):
    """
    Returns retention(age):
    - age in days since install (0 = install day)
    - Linear interpolation between known days
    - After the last known day, continues with exponential decay
      using the decay rate implied by the last two points.
    """
    days = np.array(sorted(points_dict.keys()))
    values = np.array([points_dict[d] for d in days])

    def retention(age_day: float) -> float:
        if age_day <= days[-1]:
            return float(np.interp(age_day, days, values))

        x1, x2 = days[-2], days[-1]
        y1, y2 = values[-2], values[-1]

        if y1 <= 0 or y2 <= 0:
            return 0.0

        daily_decay = (y2 / y1) ** (1 / (x2 - x1))
        extra_days = age_day - x2
        return float(y2 * (daily_decay ** extra_days))

    return retention

# ready-to-use retention functions
ret_A = build_retention_function(retention_points["A"])
ret_B = build_retention_function(retention_points["B"])


# new source retention
def new_ret_A(age: float) -> float:
    if age < 0:
        return 0.0
    if age == 0:
        return 1.0
    return 0.58 * np.exp(-0.12 * (age - 1))

def new_ret_B(age: float) -> float:
    if age < 0:
        return 0.0
    if age == 0:
        return 1.0
    return 0.52 * np.exp(-0.10 * (age - 1))
