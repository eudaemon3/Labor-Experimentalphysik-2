import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement, load_measurement_var, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 15})

# Farbfilter
folder_filter = "02_Spektralphotometer/data/Messung01"
data_f = load_measurement(1, folder_filter)
lam_f, I0_f = data_f["Referenz"]
IT_f_blau = data_f["Blau"][1]
IT_f_rot  = data_f["Rot"][1]

# Methylenblau
folder_methyl = "02_Spektralphotometer/data/Messung03"
data_m = load_measurement_var(1, folder_methyl, "methyl")
lam_m, I0_m = data_m["Referenz"]
IT_m = data_m["Blau"][1]

# Transmission
T_f_blau = IT_f_blau / I0_f
T_f_rot  = IT_f_rot  / I0_f
T_m      = IT_m / I0_m

# Plot 1
# -------------------------------------------------------------------------------

fig1, axes = plt.subplots(1,2, figsize=(10, 4.5))

ax = axes[0]
plot_visible_spectrum(
    ax=ax,
    x_min=min(lam_f), x_max=max(lam_f),
    y_min=-0.1, y_max=-0.07,
)

ax.plot(lam_f, IT_f_blau, color="tab:blue", linewidth=1.3, label=r"Filter blau")
ax.plot(lam_f, IT_f_rot, color="crimson", linewidth=1.3, label=r"Filter rot")
ax.plot(lam_m, IT_m, color="black", linewidth=1.3, label=r"Methylenblau")
ax.plot(lam_f, I0_f, color="gray", linestyle="-", linewidth=1.3, label=r"Referenz")

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=17)
ax.set_ylabel(r"Intensität $I$ / a.u.", fontsize=17)
ax.grid(True)

# Legende unter der Achse
handles, labels = ax.get_legend_handles_labels()
leg1 = fig1.legend(
    handles, labels,
    loc="lower center",
    bbox_to_anchor=(0.52, -0.01),
    ncol=2, fontsize=17
)

ax2 = axes[1]

plot_visible_spectrum(
    ax=ax2, show_edge=False,
    x_min=380, x_max=800,
    y_min=-0.1, y_max=-0.07,
    alpha_def=1
)

ax2.plot(lam_f, T_f_blau, color="tab:blue", linewidth=1.3, label="T (Filter blau)")
ax2.plot(lam_f, T_f_rot, color="crimson", linewidth=1.3, label="T (Filter rot)")
ax2.plot(lam_m, T_m, color="black", linewidth=1.3, label="T (Methylenblau)")

ax2.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=17)
ax2.set_ylabel(r"Transmission $T$ / 1", fontsize=17)
ax2.set_xlim(400, 780)
ax2.set_ylim(-0.1, 1.1)
ax2.grid(True)


plt.tight_layout(rect=[0, 0.15, 1, 1]) # type: ignore

plt.show()