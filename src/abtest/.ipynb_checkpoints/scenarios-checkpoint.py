# src/abtest/scenarios.py

import pandas as pd
from .dau import dau_on_calendar_day, dau_with_two_sources
from .retention import ret_A, ret_B
from .monetization import daily_revenue, daily_revenue_with_sale

def simulate_baseline(variant: str, max_day: int) -> pd.DataFrame:
    ret = ret_A if variant == "A" else ret_B
    rows = []
    for t in range(max_day + 1):
        dau = dau_on_calendar_day(t, ret)
        rev = daily_revenue(dau, variant)
        rows.append((t, dau, rev))
    return pd.DataFrame(rows, columns=["day", "dau", "rev"])


def simulate_sale(variant: str, max_day: int) -> pd.DataFrame:
    ret = ret_A if variant == "A" else ret_B
    rows = []
    for t in range(max_day + 1):
        dau = dau_on_calendar_day(t, ret)
        rev = daily_revenue_with_sale(t, dau, variant)
        rows.append((t, dau, rev))
    return pd.DataFrame(rows, columns=["day", "dau", "rev"])


def simulate_new_source(variant: str, max_day: int) -> pd.DataFrame:
    rows = []
    for t in range(max_day + 1):
        dau = dau_with_two_sources(t, variant)
        rev = daily_revenue(dau, variant)
        rows.append((t, dau, rev))
    return pd.DataFrame(rows, columns=["day", "dau", "rev"])
