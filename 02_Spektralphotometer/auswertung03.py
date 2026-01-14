import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement_var
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# -----------------------
# Load all measurements
# -----------------------
folder = "02_Spektralphotometer/data/Messung05"
data = {n: load_measurement_var(n, folder, 'glas') for n in range(1, 6)}


lam, I0 = data[1]["Referenz"]
_, IT = data[1]['Blau']

T = IT / I0

T_all = np.array(T)
mask = np.logical_and(lam >= 700, lam <= 720)
lam_slice = lam[mask]
T_slice = T_all[mask]

peaks, props = find_peaks(T_slice, distance=5)
peak_nu = 1/lam_slice[peaks] * 1e3 #mu m

index = np.array(range(len(peak_nu)))

def ffit(m, k, d):
    return k*m + d
popt, pcov = curve_fit(ffit, index, peak_nu)
m_fine = np.linspace(0, max(index), 1000)
nu_fine = ffit(m_fine, *popt)

k, _ = popt
dk = np.sqrt(np.diag(pcov))[0]
n_p = 1.519

d = 1/abs(2*n_p*k)
dd = abs(d*dk/k)
print(f"Steigung alpha = {k*1000} pm {dk*1000} mm^-1")
print(f"Dicke d = {d} pm {dd} mu m")

# Plot
# ------------------------------------------------------------------
fig1, ax1 = plt.subplots(1,1, figsize=(6, 4))

ax1.plot(lam_slice, T_slice, color='tab:orange', linewidth=1.1, label='Signal')
ax1.scatter(lam_slice[peaks], T_slice[peaks], marker='d', color='blue', label='detektierte Peaks')
ax1.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax1.set_ylabel(r"Transmission $T$ / 1", fontsize=16)
ax1.legend(frameon=True, fontsize=16, ncols=2, loc='lower center')
ax1.set_ylim(0.89, 0.945)
ax1.grid(True)
plt.tight_layout()

fig2, ax2 = plt.subplots(1,1, figsize=(6, 4))
ax2.plot(index, peak_nu, 'bd', label="detektierte Peaks")
ax2.plot(m_fine, nu_fine, color='crimson', label="Ausgleichsgerade")
ax2.set_ylabel(r"Wellenzahl $\nu_m$ / $\mu\text{m}^{-1}$", fontsize=16)
ax2.set_xlabel(r"Index $m$ / 1", fontsize=16)
ax2.legend(frameon=True, fontsize=16)
ax2.grid(True)

plt.tight_layout()
plt.show()