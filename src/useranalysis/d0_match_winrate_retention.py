import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_match_winrate_retention(
    save_dir="../outputs/figurestask2/match_winrate_retention/"
):

    df = pd.DataFrame({
        "match_segment": [
            "1 match","1 match",
            "2-3 matches","2-3 matches","2-3 matches","2-3 matches",
            "4-7 matches","4-7 matches","4-7 matches","4-7 matches",
            "8-15 matches","8-15 matches","8-15 matches","8-15 matches",
            "16-30 matches","16-30 matches","16-30 matches","16-30 matches",
            "30+ matches","30+ matches","30+ matches","30+ matches"
        ],
        "win_segment": [
            "0-25%","76-100%",
            "0-25%","26-50%","51-75%","76-100%",
            "0-25%","26-50%","51-75%","76-100%",
            "0-25%","26-50%","51-75%","76-100%",
            "0-25%","26-50%","51-75%","76-100%",
            "0-25%","26-50%","51-75%","76-100%"
        ],
        "users": [
            88381, 41020,
            89133, 31864, 299013, 42767,
            3493, 6883, 70483, 182251,
            502, 2201, 43337, 89729,
            93, 1977, 12880, 11266,
            38, 603, 2127, 36818
        ],
        "d1": [
            0.1792, 0.2123,
            0.1700, 0.2586, 0.2245, 0.3030,
            0.2367, 0.4285, 0.4514, 0.4132,
            0.3207, 0.5956, 0.5901, 0.5745,
            0.7096, 0.7389, 0.7562, 0.7383,
            0.8421, 0.8739, 0.8514, 0.1795
        ],
        "d3": [
            0.0563, 0.0706,
            0.0544, 0.0902, 0.0813, 0.1073,
            0.0770, 0.1644, 0.1623, 0.1507,
            0.1553, 0.2762, 0.2442, 0.2340,
            0.3118, 0.4264, 0.3923, 0.3718,
            0.6052, 0.5339, 0.5397, 0.0620
        ],
        "d7": [
            0.0243, 0.0291,
            0.0234, 0.0400, 0.0355, 0.0406,
            0.0334, 0.0626, 0.0690, 0.0646,
            0.0498, 0.1281, 0.1111, 0.1092,
            0.1505, 0.2210, 0.2072, 0.2045,
            0.3157, 0.3034, 0.3422, 0.0294
        ],
        "d14": [
            0.0094, 0.0103,
            0.0089, 0.0155, 0.0145, 0.0146,
            0.0131, 0.0257, 0.0269, 0.0259,
            0.0199, 0.0522, 0.0416, 0.0481,
            0.0645, 0.0935, 0.1015, 0.1127,
            0.1578, 0.1492, 0.1937, 0.0123
        ]
    })

    df_melt = df.melt(
        id_vars=["match_segment", "win_segment"],
        value_vars=["d1", "d3", "d7", "d14"],
        var_name="day",
        value_name="retention"
    )
    day_order = ["d1", "d3", "d7", "d14"]
    df_melt["day"] = pd.Categorical(df_melt["day"], categories=day_order, ordered=True)


    # Plot: One chart per match segment

    os.makedirs(save_dir, exist_ok=True)

    unique_segments = df["match_segment"].unique()

    for seg in unique_segments:

        seg_df = df_melt[df_melt["match_segment"] == seg]

        fig, ax = plt.subplots(figsize=(10, 6))

        for win_seg in seg_df["win_segment"].unique():
            temp = seg_df[seg_df["win_segment"] == win_seg]

            ax.plot(
                temp["day"],
                temp["retention"],
                marker="o",
                linewidth=2,
                label=win_seg
            )

        ax.set_title(f"Retention Curve – {seg}", fontsize=16)
        ax.set_xlabel("Day", fontsize=12)
        ax.set_ylabel("Retention Rate", fontsize=12)
        ax.grid(alpha=0.3)
        ax.legend(title="Win-Rate Segment")

        save_path = os.path.join(save_dir, f"{seg.replace(' ', '_')}_retention_curve.png")
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.show()

    df_display = df.copy()
    for c in ["d1", "d3", "d7", "d14"]:
        df_display[c] = (df_display[c] * 100).map("{:.2f}%".format)

    return df_display
