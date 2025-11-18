import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy.optimize import curve_fit

plt.style.use('science')
plt.rcParams.update({'font.size': 14})
# Messdaten
theta = np.array([90, 85, 80, 75, 70, 65])  # Grad
dtheta = 1 
U = np.array([92.8, 38.3, 5.4, 5.2, 33.6, 90.7])  # mV

# Unsicherheiten
dU_Multimeter = U * 0.005 + 0.2  # mV
dU_Detektor = U * 0.02 + 0.3  # mV 
dU = np.sqrt(dU_Multimeter**2 + dU_Detektor**2)  # mV

# Fitfunktion für Malus-Gesetz: U = A * cos²(θ - θ₀)
def malus_fit(theta_deg, A, theta0):
    theta_rad = np.deg2rad(theta_deg - theta0)
    return A * np.cos(theta_rad)**2

# Startwerte für den Fit
p0 = [100, 75]  

# Curve Fit
popt, pcov = curve_fit(malus_fit, theta, U, p0=p0, sigma=dU, absolute_sigma=True)
A_fit, theta0_fit = popt
dA_fit, dtheta0_fit = np.sqrt(np.diag(pcov))

# Winkel für Plot (dichtere Abtastung)
theta_fit = np.linspace(0, 180, 500)
U_fit = malus_fit(theta_fit, A_fit, theta0_fit)

# Polarisationsachse berechnen (Minimum bei θ₀, Maximum bei θ₀ - 90°)
theta_min = theta0_fit 
dtheta_min = dtheta0_fit
theta_max = theta0_fit - 90
dtheta_max = dtheta0_fit

# Polardiagramm erstellen
fig, ax = plt.subplots(1, 1, figsize=(6, 5), subplot_kw={'projection': 'polar'})

line_pol = ax.plot([np.deg2rad(theta_max), np.deg2rad(theta_max)], [0, A_fit], 
        'g--', linewidth=1, label=f'Polarisationsachse: {theta_max:.1f}°')

line_min = ax.plot([np.deg2rad(theta_min), np.deg2rad(theta_min)], [0, A_fit], 
        'orange', linestyle='--', linewidth=1, label=f'Minimum: {theta_min:.1f}°')

points = ax.errorbar(np.deg2rad(theta), U, xerr=np.deg2rad(dtheta), yerr=dU, 
            fmt='d', color='blue', markersize=4, capsize=5, label='Messdaten')

line_fit = ax.plot(np.deg2rad(theta_fit), U_fit, 'r-', linewidth=1, label='Ausgleichskurve')

ax.set_theta_zero_location('E')  
ax.set_theta_direction(1)  
ax.set_thetamin(0)  
ax.set_thetamax(180)  

# Radiusachse beschriften
ax.set_ylim(0, 110)
ax.text(np.deg2rad(5), 80, r'$U$ / mV', fontsize=14, ha='center')

# Legende mit 2 Spalten: links Messdaten+Fit, rechts Achsen
handles = [points, line_fit[0], line_pol[0], line_min[0]]
labels = ['Messdaten', 'Ausgleichskurve', f'Polarisationsachse: {theta_max:.1f}°', f'Minimum: {theta_min:.1f}°']
ax.legend(handles, labels, loc='lower center', frameon=True, fontsize=14, ncol=2)
ax.grid(True)

plt.tight_layout()
plt.show()

# Ergebnisse ausgeben
print("=" * 70)
print("BESTIMMUNG DER POLARISATIONSACHSE DER 3D-BRILLE")
print("=" * 70)
print(f"\nFitparameter:")
print(f"  Amplitude A = ({A_fit:.1f} ± {dA_fit:.1f}) mV")
print(f"  Winkel minimaler Transmission θ_min = ({theta_min:.1f} ± {dtheta_min:.1f})°")
print(f"\nPolarisationsachse der 3D-Brille:")
print(f"  θ_max = θ_min - 90° = ({theta_max:.1f} ± {dtheta_max:.1f})°")
print(f"\nAlternative Messung (direkte Bestimmung des Minimums):")
print(f"  θ_min = (77,0 ± 0,5)°")
print(f"  θ_max = θ_min - 90° = ({theta_max - 1:.0f} ± 0,5)°")
print("=" * 70)