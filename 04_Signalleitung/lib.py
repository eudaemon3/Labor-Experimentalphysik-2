import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_csv_folder(folder_path):
    """
    Plots all CSV files in a given folder.
    X-axis: time
    Y-axis: voltage (one or multiple columns)
    """

    for filename in sorted(os.listdir(folder_path)):
        if not filename.lower().endswith(".csv"):
            continue

        file_path = os.path.join(folder_path, filename)

        # Read CSV, skip the first two header rows
        df = pd.read_csv(file_path, skiprows=3, header=None)

        time = df.iloc[:, 0]
        voltages = df.iloc[:, 1:]
        print(filename)
        fig, ax = plt.subplots(1,1, figsize=(6,4))
        for col in voltages.columns:
            ax.plot(time, voltages[col], label=f"Channel {col}")

        ax.set_xlabel("Time $t$ / s", fontsize=16)
        ax.set_ylabel("Voltage $U$ / V", fontsize=16)
        ax.legend(fontsize=16, frameon=True)
        ax.grid(True)
        plt.tight_layout()
        plt.show()



