import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_d0_playtime_retention(
    save_path="../outputs/figurestask2/d0_playtime_retention_line_with_table.png",
    show=True,
):

    df = pd.DataFrame({
        "play_segment": ["0-5 min", "5-10 min", "10-15 min", "15-30 min", "30+ min"],
        "d1":  [0.17235, 0.23467, 0.30512, 0.41190, 0.58223],
        "d3":  [0.05529, 0.08360, 0.11055, 0.14962, 0.24910],
        "d7":  [0.02388, 0.03589, 0.04614, 0.06349, 0.11984],
        "d14": [0.00919, 0.01409, 0.01852, 0.02540, 0.05298],
        "d21": [0.00407, 0.00595, 0.00767, 0.01109, 0.02393],
    })

    df_melt = df.melt(id_vars="play_segment", var_name="day", value_name="retention")
    day_order = ["d1", "d3", "d7", "d14", "d21"]
    df_melt["day"] = pd.Categorical(df_melt["day"], categories=day_order, ordered=True)

    fig, ax = plt.subplots(figsize=(12, 8))

    for segment in df["play_segment"]:
        segment_df = df_melt[df_melt["play_segment"] == segment]
        ax.plot(
            segment_df["day"],
            segment_df["retention"],
            marker="o",
            linewidth=2,
            label=segment,
        )

    ax.set_title("Retention Curves by D0 Playtime Segment", fontsize=16)
    ax.set_xlabel("Retention Day", fontsize=12)
    ax.set_ylabel("Retention Rate", fontsize=12)
    ax.grid(alpha=0.3)
    ax.legend(title="Playtime Segment")

    df_display = df.copy()
    for col in ["d1", "d3", "d7", "d14", "d21"]:
        df_display[col] = (df_display[col] * 100).map("{:.2f}%".format)

    plt.table(
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

    if show:
        plt.show()
    else:
        plt.close(fig)

    return df_display
