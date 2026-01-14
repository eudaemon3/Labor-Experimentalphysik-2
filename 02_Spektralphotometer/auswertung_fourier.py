import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement_var
from scipy.interpolate import interp1d

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# Calculate
# ------------------------------------------------------------
folder = "02_Spektralphotometer/data/Messung05"
channel = 'Blau'
n_p = 1.519

data = load_measurement_var(1, folder, 'glas')
lam, I0 = data["Referenz"]
_, IT = data[channel]
T = IT / I0

mask = np.logical_and(lam >= 700, lam <= 720)
lam_slice = lam[mask]
T_slice = T[mask]

lam_m = lam_slice * 1e-9  # nm -> m
nu = 1 / lam_m            # Wellenzahl in 1/m

# Interpolate and FFT
# ------------------------------------------------------------
n_points = len(nu)
nu_lin = np.linspace(nu.min(), nu.max(), n_points)
interp_func = interp1d(nu[::-1], T_slice[::-1], kind='cubic')
T_interp = interp_func(nu_lin)

# Mittelwert subtrahieren (wichtig für FFT)
T_centered = T_interp - np.mean(T_interp)
FT = np.fft.fft(T_centered)

# Frequenz in Metern (komplementäre Variable zur Wellenzahl)
freq = np.fft.fftfreq(len(nu_lin), d=(nu_lin[1]-nu_lin[0]))  
ampl = np.abs(FT) / n_points

# Nur positive Frequenzen
pos = freq > 0
freq_pos = freq[pos]
ampl_pos = ampl[pos]

# Schichtdicke direkt aus Frequenz
length_m = freq_pos / (2 * n_p)  # KORREKTUR: keine Inversion!
length_um = length_m * 1e6

# Plot
# ------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(length_um, ampl_pos, color='forestgreen', lw=1.2)
ax2.set_xlabel(r"Schichtdicke / µm", fontsize=16)
ax2.set_ylabel("Amplitude der FT", fontsize=16)
ax2.grid(True)
plt.tight_layout()
plt.show()

# Schichtdicke 
# ------------------------------------------------------------
peak_idx = np.argmax(ampl_pos)
d = length_um[peak_idx]
print(f"Dominanter Peak bei Schichtdicke: {d:.3f} µm")