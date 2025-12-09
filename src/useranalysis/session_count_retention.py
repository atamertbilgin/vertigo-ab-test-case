import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_session_count_retention(
    save_path="../outputs/figurestask2/session_count_retention_line_with_table.png"
):

    df = pd.DataFrame({
        "session_segment": ["1 session", "2 sessions", "3-4 sessions", "4+ sessions"],
        "d1":  [0.26221, 0.44399, 0.59969, 0.72371],
        "d3":  [0.09398, 0.17280, 0.25334, 0.34928],
        "d7":  [0.04118, 0.07843, 0.11735, 0.16827],
        "d14": [0.01670, 0.03215, 0.05187, 0.07995],
        "d21": [0.00724, 0.01444, 0.02319, 0.03478],
    })

    df_melt = df.melt(id_vars="session_segment", var_name="day", value_name="retention")
    day_order = ["d1", "d3", "d7", "d14", "d21"]
    df_melt["day"] = pd.Categorical(df_melt["day"], categories=day_order, ordered=True)

    fig, ax = plt.subplots(figsize=(12, 8))

    for segment in df["session_segment"]:
        segment_df = df_melt[df_melt["session_segment"] == segment]
        ax.plot(
            segment_df["day"],
            segment_df["retention"],
            marker="o",
            linewidth=2,
            label=segment,
        )

    ax.set_title("Retention Curves by D0 Session Count Segment", fontsize=16)
    ax.set_xlabel("Retention Day", fontsize=12)
    ax.set_ylabel("Retention Rate", fontsize=12)
    ax.grid(alpha=0.3)
    ax.legend(title="Session Segment")

    df_display = df.copy()
    for col in ["d1", "d3", "d7", "d14", "d21"]:
        df_display[col] = (df_display[col] * 100).map("{:.2f}%".format)

    table = plt.table(
        cellText=df_display.values,
        colLabels=df_display.columns,
        cellLoc="center",
        loc="bottom",
        bbox=[0.0, -0.45, 1.0, 0.35],
    )

    plt.subplots_adjust(left=0.1, bottom=0.35)

    out_dir = os.path.dirname(save_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    plt.savefig(save_path, dpi=150, bbox_inches="tight")

    return df_display
