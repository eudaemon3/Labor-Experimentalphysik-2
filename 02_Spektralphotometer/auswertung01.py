import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from collections import defaultdict
from plot_lib import load_measurement, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 15})

folder = "02_Spektralphotometer/data/Messung01"
data = {n: load_measurement(n, folder) for n in range(1, 6)}
colors = ["Blau", "Rot", "RotBlau"]

T_all = defaultdict(list)
E_all = defaultdict(list)

for n in range(1, 6):
    lam, I0 = data[n]["Referenz"]

    for c in colors:
        _, IT = data[n][c]

        T = IT / I0
        E = -np.log(T)

        T_all[c].append(T)
        E_all[c].append(E)

for c in colors:
    T_all[c] = np.array(T_all[c]) # type: ignore
    E_all[c] = np.array(E_all[c]) # type: ignore

T_mean = {c: np.mean(T_all[c],axis=0) for c in colors}
T_std  = {c: np.std(T_all[c],axis=0)  for c in colors}

E_mean = {c: np.mean(E_all[c],axis=0) for c in colors}
E_std  = {c: np.std(E_all[c],axis=0)  for c in colors}

lambda_axis = lam

# -----------------------
# FIGURE 1: Transmission
# -----------------------
fig1, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 4))

plot_specs = {
    "Blau": ("tab:blue", r"$T_B$"),
    "Rot": ("crimson", r"$T_R$"),
    "RotBlau": ("rebeccapurple", r"$T_{RB}$")
}

plot_visible_spectrum(
    ax=ax1, show_edge=False,
    x_min=380, x_max=800, 
    y_min=-0.075, y_max=-0.04,
    alpha_def=0.7
)

for c in colors:
    color, name = plot_specs[c]
    ax1.plot(lambda_axis, T_mean[c], label=name, color=color, linewidth=1.4)
    ax1.fill_between(
        lambda_axis,
        T_mean[c] - T_std[c],
        T_mean[c] + T_std[c],
        color=color,
        alpha=0.4
    )

ax1.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=18)
ax1.set_ylabel(r"Transmission $T$ / 1", fontsize=18)
ax1.legend(frameon=True, fontsize=17, ncols=3, loc='upper center')
ax1.set_ylim(-0.075, 1.15)
ax1.set_xlim(380, 780)
ax1.grid(True)

plt.tight_layout()

plot_visible_spectrum(
    ax=ax2, show_edge=False,
    x_min=380, x_max=800, 
    y_min=-0.29, y_max=-0.122,
    alpha_def=0.7
)

ax2.plot(lambda_axis, E_mean["Blau"], label=r"$E_B$", color="tab:blue", linewidth=1.3)
ax2.plot(lambda_axis, E_mean["Rot"], label=r"$E_R$", color="crimson")

ax2.plot(lambda_axis, E_mean["RotBlau"], label=r"$E_{RB}$", color="rebeccapurple")

#E_sum = E_mean["Rot"] + E_mean["Blau"]
#ax2.plot(lambda_axis, E_sum, label=r"$E_R$ + $E_B$", color="black", linestyle="-")

ax2.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=18)
ax2.set_ylabel(r"Extinktion $E$ / 1",fontsize=18)
ax2.legend(frameon=True, fontsize=17)
ax2.set_ylim(-0.29, 6)
ax2.set_xlim(380, 780)
ax2.grid(True)

plt.tight_layout()

fig3, ax = plt.subplots(figsize=(6, 4))

plot_visible_spectrum(
    ax=ax, show_edge=False,
    x_min=380, x_max=800, 
    y_min=-0.32, y_max=-0.12,
    alpha_def=0.7
)

ax.plot(lambda_axis, E_mean["Blau"], label=r"$E_B$", color="tab:blue", linewidth=1.3)
ax.plot(lambda_axis, E_mean["Rot"], label=r"$E_R$", color="crimson")

ax.plot(lambda_axis, E_mean["RotBlau"], label=r"$E_{RB}$", color="rebeccapurple")

E_sum = E_mean["Rot"] + E_mean["Blau"]
ax.plot(lambda_axis, E_sum, label=r"$E_R$ + $E_B$", color="black", linestyle="-")

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax.set_ylabel(r"Extinktion $E$ / 1",fontsize=16)
ax.legend(frameon=True, fontsize=16)
ax.set_ylim(-0.32, 6.6)
ax.set_xlim(380, 780)
ax.grid(True)

plt.tight_layout()
plt.show()