import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_daily_session_duration_trend(
    save_path="../outputs/figurestask2/daily_session_duration_trend.png"
):
    """
    Generates a daily average session duration trend line chart (with optional active users overlay).
    Returns the dataframe used for plotting.
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
        "avg_session_duration_sec": [
            1141.89,1243.00,1335.19,1355.42,1316.82,
            1340.85,1357.05,1346.43,1336.54,1362.70,
            1428.91,1415.90,1421.96,1450.02,1436.98,
            1400.11,1384.96,1474.48,1472.30,1437.45,
            1474.70,1474.51,1426.16,1465.94,1511.00,
            1531.70,1513.83,1546.80,1536.45,1482.24
        ],
        "users_active": [
            32919,52000,71965,83608,75338,
            74914,75530,77982,81795,94000,
            95317,79909,79909,80235,82279,
            89251,102542,107577,88562,88106,
            88106,92000,101741,119313,123085,
            104837,113615,115227,115590,120532
        ]
    })

    df["event_date"] = pd.to_datetime(df["event_date"])

    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(
        df["event_date"], df["avg_session_duration_sec"],
        color="tab:blue", marker="o", linewidth=2
    )
    ax1.set_xlabel("Date", fontsize=12)
    ax1.set_ylabel("Avg Session Duration (seconds)", color="tab:blue", fontsize=12)
    ax1.tick_params(axis="y", labelcolor="tab:blue")


    out_dir = os.path.dirname(save_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()
