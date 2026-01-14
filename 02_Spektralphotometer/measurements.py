import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement, load_measurement_var, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# Load measurement 
# ------------------------------------------------------------------------------

folder = "02_Spektralphotometer/data/Messung03"
measurement = load_measurement_var(1, folder, 'methyl')

all_lambda = np.concatenate([v[0] for v in measurement.values()])
x_min = np.min(all_lambda)
x_max = np.max(all_lambda)

# Plot
# ------------------------------------------------------------------------------

plot_specs = {
    "Blau": ("tab:blue", r"$I_{T,\mathrm{M}}(\lambda)$"),
    #"Rot": ("crimson", r"$I_{T,\mathrm{R}}(\lambda)$"),
    #"RotBlau": ("rebeccapurple", r"$I_{T,\mathrm{RB}}(\lambda)$"),
    "Referenz": ("black", r"$I_0(\lambda)$")
}

fig, ax = plt.subplots(figsize=(6, 4))

plot_visible_spectrum(
    ax,
    x_min=x_min,
    x_max=x_max,
    y_min=-0.08,
    y_max=-0.04,
) 

for name, (lam, I) in measurement.items():
    color, label = plot_specs[name]
    ax.plot(lam, I, color=color, label=label, zorder=2, linewidth=1.1)

ax.set_xlim(x_min, x_max)

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax.set_ylabel(r"Intensität $I$ / a.u.", fontsize=16)

ax.grid(True,'major')
# ax.grid(True,'minor', alpha=0.5, linestyle='--')
ax.legend(frameon=True, fontsize=16)

plt.tight_layout()
plt.show()