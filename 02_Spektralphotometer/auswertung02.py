import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement_var, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# -----------------------
# Load all measurements
# -----------------------
folder = "02_Spektralphotometer/data/Messung03"
data = {n: load_measurement_var(n, folder, 'methyl') for n in range(1, 6)}

c = 'Blau'
T_all, E_all = [], []
E_664_list = []

for n in range(1, 6):
    lam, I0 = data[n]["Referenz"]
    _, IT = data[n][c]

    T = IT / I0
    E = -np.log(T)

    T_all.append(T)
    E_all.append(E)

    idx = np.argmin(np.abs(lam - 664))   # Index des nächstliegenden Werts
    E_664_list.append(E[idx])

T_all = np.array(T_all)
E_all = np.array(E_all)

T_mean = T_all.mean(axis=0)
T_std = T_all.std(axis=0)

E_mean = E_all.mean(axis=0)
E_std = E_all.std(axis=0)
lambda_axis = lam

# Konzentration
# ------------------------------------------------------------------
epsilon = 77790      # L mol^-1 cm^-1
d = 1.0              # cm (10 mm)

E_664_array = np.array(E_664_list)

E_664_mean = np.mean(E_664_array)
E_664_std  = np.std(E_664_array, ddof=1) 

# Konzentration
c_mean = E_664_mean / (epsilon * d)
delta_c = E_664_std / (epsilon * d)
print(f"E Werte: {E_664_array} ")
print(f"Konzentration: {c_mean:.3e} ± {delta_c:.3e} mol/L")

# Plot
# ------------------------------------------------------------------
fig1, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 4))

lim1 = (0.85, 1.05)
a1 = (lim1[1] - lim1[0])*0.1

lim2 = (-0.02, 0.12)
a2 = (lim2[1] - lim2[0])*0.1

idx = np.argmin(np.abs(lam - 664))   # Index des nächstliegenden Werts
E_point = E_mean[idx]
T_point = T_mean[idx]

plot_visible_spectrum(
    ax=ax1, show_edge=False,
    x_min=380, x_max=800, 
    y_min=lim1[0]-1.1*a1, y_max=lim1[0]-0.7*a1,
    alpha_def=0.7
)

plot_visible_spectrum(
    ax=ax2, show_edge=False,
    x_min=380, x_max=800, 
    y_min=lim2[0]-1.1*a2, y_max=lim2[0]-0.7*a2,
    alpha_def=0.7
)

ax1.plot(lambda_axis, T_mean, color='blue', linewidth=1.3)
ax1.fill_between(
    lambda_axis,
    T_mean - T_std,
    T_mean + T_std,
    color='tab:blue',
    alpha=0.3
)

ax1.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax1.set_ylabel(r"Transmission $T$ / 1", fontsize=16)
ax1.set_ylim(lim1[0]-1.1*a1, lim1[1])
ax1.set_xlim(400, 780)
ax1.grid(True)

plt.tight_layout()

ax2.plot(lambda_axis, E_mean, color="blue", linewidth=1.3)

show_error = True
if show_error:
    ax2.fill_between(
        lambda_axis,
        E_mean - E_std,
        E_mean + E_std,
        color="tab:blue",
        alpha=0.3
    )

ax2.errorbar(664, E_664_mean, marker='o', markersize=5, yerr=E_664_std, color='k', linewidth=1.1, capsize=4)

ax2.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax2.set_ylabel(r"Extinktion $E$ / 1",fontsize=16)
ax2.set_ylim(lim2[0]-1.1*a2, lim2[1])
ax2.set_xlim(400, 780)
ax2.grid(True)

plt.tight_layout()
plt.show()