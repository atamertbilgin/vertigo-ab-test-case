# src/abtest/monetization.py

from .config import purchase_ratio, ecpm, impressions, ARPPU, SALE_START, SALE_END

def daily_revenue(dau: float, variant: str) -> float:
    """
    Baseline daily revenue = ads + IAP.
    """
    ad_rev = (dau * impressions[variant] / 1000.0) * ecpm[variant]
    iap_rev = dau * purchase_ratio[variant] * ARPPU
    return ad_rev + iap_rev


def daily_revenue_with_sale(day: int, dau: float, variant: str) -> float:
    """
    Daily revenue when a 10-day sale is active:
    - Adds +1% absolute to purchase rate between SALE_START and SALE_END.
    """
    base_pr = purchase_ratio[variant]
    boosted_pr = base_pr + 0.01

    if SALE_START <= day <= SALE_END:
        pr = boosted_pr
    else:
        pr = base_pr

    ad_rev = (dau * impressions[variant] / 1000.0) * ecpm[variant]
    iap_rev = dau * pr * ARPPU
    return ad_rev + iap_rev
