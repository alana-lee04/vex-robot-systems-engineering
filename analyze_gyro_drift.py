"""Gyroscope drift characterization test: summary statistics and boxplot.

Reads data/gyroscope_drift.csv (angle deviation from 90 degrees after four
turns, three trials at each turn speed) and saves figures/gyro_drift_boxplot.png.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/gyroscope_drift.csv")

summary = df.groupby("turn_speed")["angle_deviation_deg"].agg(["mean", "std", "min", "max"]).round(1)
print("Angle deviation from 90 degrees by turn speed:")
print(summary)

speeds = sorted(df["turn_speed"].unique())
groups = [df.loc[df["turn_speed"] == s, "angle_deviation_deg"] for s in speeds]

fig, ax = plt.subplots(figsize=(6, 4))
ax.boxplot(groups, tick_labels=[str(s) for s in speeds])
for i, g in enumerate(groups, start=1):
    ax.scatter([i] * len(g), g, color="#1f4e79", zorder=3, s=25)
ax.set_xlabel("Turn speed (motor power)")
ax.set_ylabel("Deviation from 90° (degrees)")
ax.set_title("Gyroscope drift after four 90° turns")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig("figures/gyro_drift_boxplot.png", dpi=150)
print("Saved figures/gyro_drift_boxplot.png")
