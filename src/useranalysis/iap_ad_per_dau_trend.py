import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_iap_ad_per_dau_trend(
    save_path="../outputs/figurestask2/iap_ad_per_dau_trend.png"
):
    """
    Creates a line chart showing IAP per DAU and Ad revenue per DAU trends
    from 2024-02-15 to 2024-03-15.

    Returns:
        df (pd.DataFrame): Dataframe containing the values used for the plot.
    """

    df = pd.DataFrame({
        "event_date": [
            "2024-02-15","2024-02-16","2024-02-17","2024-02-18","2024-02-19",
            "2024-02-20","2024-02-21","2024-02-22","2024-02-23","2024-02-24",
            "2024-02-25","2024-02-26","2024-02-27","2024-02-28","2024-02-29",
            "2024-03-01","2024-03-02","2024-03-03","2024-03-04","2024-03-05",
            "2024-03-06","2024-03-07","2024-03-08","2024-03-09","2024-03-10",
            "2024-03-11","2024-03-12","2024-03-13","2024-03-14","2024-03-15"
        ],
        "iap_per_dau": [
            0.012147,0.024635,0.028880,0.036939,0.056786,
            0.057357,0.077679,0.072520,0.073441,0.068315,
            0.067731,0.054518,0.061274,0.063934,0.066887,
            0.057015,0.063135,0.066616,0.073476,0.079943,
            0.082632,0.067939,0.072310,0.074784,0.085787,
            0.059864,0.062790,0.074864,0.068276,0.084250
        ],
        "ad_per_dau": [
            0.019579,0.020513,0.022629,0.023089,0.023910,
            0.024197,0.024717,0.024047,0.021722,0.022079,
            0.023455,0.024720,0.027013,0.026392,0.025340,
            0.023975,0.024892,0.024385,0.024775,0.024355,
            0.023394,0.022429,0.021239,0.022444,0.024148,
            0.024941,0.023293,0.023238,0.023016,0.021795
        ]
    })

    df["event_date"] = pd.to_datetime(df["event_date"])

    plt.figure(figsize=(14, 6))

    plt.plot(
        df["event_date"],
        df["iap_per_dau"],
        marker="o",
        linewidth=2,
        color="tab:green",
        label="IAP per DAU"
    )

    plt.plot(
        df["event_date"],
        df["ad_per_dau"],
        marker="o",
        linewidth=2,
        color="tab:purple",
        label="Ad Revenue per DAU"
    )

    plt.title("IAP per DAU & Ad Revenue per DAU Trend (Daily)", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Revenue per DAU ($)", fontsize=12)
    plt.grid(alpha=0.3)
    plt.legend()

    out_dir = os.path.dirname(save_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()
