import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement, load_measurement_var, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 15})

# ============================================================
# DATEN – nur Messung 1
# ============================================================

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

# ============================================================
# FIGUR 1 – INTENSITÄTEN
# ============================================================

fig1, ax = plt.subplots(figsize=(6, 4.5))

plot_visible_spectrum(
    ax=ax,
    x_min=min(lam_f), x_max=max(lam_f),
    y_min=-0.1, y_max=-0.07,
)

ax.plot(lam_f, IT_f_blau,color="tab:blue",linewidth=1.4,label=r"$I_T$ (Filter blau)")
ax.plot(lam_f, IT_f_rot,color="crimson",linewidth=1.4,label=r"$I_T$ (Filter rot)")
ax.plot(lam_m, IT_m,color="black",linewidth=1.3,label=r"$I_T$ (Methylenblau)")
ax.plot(lam_f, I0_f, color="gray", linestyle="-", linewidth=1.3, label=r"$I_0$ (Referenz)")

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax.set_ylabel(r"Intensität $I$ / a.u.", fontsize=16)
ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
fig1.legend(
    handles, labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.2),  
    ncol=2,
    fontsize=16,
)

plt.tight_layout()

# ============================================================
# FIGUR 2 – TRANSMISSION 
# ============================================================

fig2, ax = plt.subplots(figsize=(6, 4))

plot_visible_spectrum(
    ax=ax, show_edge=False,
    x_min=380, x_max=800,
    y_min=-0.1, y_max=-0.07,
    alpha_def=0.7
)

ax.plot(lam_f, T_f_blau,color="tab:blue", linewidth=1.3, label="T (Filter blau)")
ax.plot(lam_f, T_f_rot, color="crimson", linewidth=1.3, label="T (Filter rot)")
ax.plot(lam_m, T_m, color="black",linewidth=1.3, label="T (Methylenblau)")

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax.set_ylabel(r"Transmission $T$ / 1", fontsize=16)
ax.set_xlim(400, 780)
ax.set_ylim(-0.1, 1.1)
ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
fig2.subplots_adjust(bottom=0.32)
leg2 = fig2.legend(
    handles, labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.08),
    ncol=2,
    fontsize=16,
)

plt.tight_layout()
plt.show()