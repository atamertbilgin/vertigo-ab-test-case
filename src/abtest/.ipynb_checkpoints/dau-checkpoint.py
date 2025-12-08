# src/abtest/dau.py

from .config import INSTALLS_PER_DAY
from .retention import ret_A, ret_B, new_ret_A, new_ret_B

def dau_on_calendar_day(t: int, retention_func) -> float:
    """
    Single-source DAU:
    - t = 0 is the first install day.
    - Each day t, a new cohort of INSTALLS_PER_DAY installs.
    - On day t, each cohort c ∈ [0, t] has age = t - c.
    """
    total = 0.0
    for cohort_start in range(t + 1):
        age = t - cohort_start
        total += INSTALLS_PER_DAY * retention_func(age)
    return total


def dau_with_two_sources(day: int, variant: str) -> float:
    """
    Two sources starting from day 20:
    - Day 0–19: 20k installs/day from original source
    - Day >= 20: 12k original + 8k new source
    """
    ret_main = ret_A if variant == "A" else ret_B
    ret_new_fn = new_ret_A if variant == "A" else new_ret_B

    dau = 0.0

    # Original source
    for cohort_day in range(0, day + 1):
        installs_main = 20000 if cohort_day < 20 else 12000
        age = day - cohort_day
        dau += installs_main * ret_main(age)

    # New source (starts at day 20)
    for cohort_day in range(20, day + 1):
        installs_new = 8000
        age = day - cohort_day
        dau += installs_new * ret_new_fn(age)

    return dau
