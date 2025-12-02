import numpy as np
import matplotlib.pyplot as plt
import math

# --- Parameter ---
f_hp = 500
f_lp = 300
C = 100e-9

R_hp = 1/(2*np.pi*f_hp*C)
R_lp = 1/(2*np.pi*f_lp*C)

# --- Frequenzachsen ---
f_hp_range = np.logspace(math.log10(f_hp/100), math.log10(f_hp*100), 500)
f_lp_range = np.logspace(math.log10(f_lp/100), math.log10(f_lp*100), 500)

# --- Übertragungsfunktionen ---
w_hp = 2*np.pi*f_hp_range
H_hp = 1j*w_hp*R_hp*C / (1 + 1j*w_hp*R_hp*C)

w_lp = 2*np.pi*f_lp_range
H_lp = 1/(1 + 1j*w_lp*R_lp*C)

# --- Phasen korrekt berechnen ---
phase_hp = np.angle(H_hp, deg=True)
phase_hp = np.unwrap(np.deg2rad(phase_hp)) * 180/np.pi   # kontinuierliche Phase
phase_hp = phase_hp - 90                                   # Hochpass-Korrektur

phase_lp = np.angle(H_lp, deg=True)
phase_lp = np.unwrap(np.deg2rad(phase_lp)) * 180/np.pi

# --- Plot: CR Hochpass ---
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.semilogx(f_hp_range, 20*np.log10(np.abs(H_hp)))
ax1.set_title("CR-Hochpass – Amplitudengang")
ax1.set_xlabel("Frequenz [Hz]")
ax1.set_ylabel("Amplitude [dB]")
ax1.grid(True, which="both")

ax2.semilogx(f_hp_range, phase_hp)
ax2.set_title("CR-Hochpass – Phasengang (korrigiert)")
ax2.set_xlabel("Frequenz [Hz]")
ax2.set_ylabel("Phase [°]")
ax2.grid(True, which="both")

plt.tight_layout()
plt.show()

# --- Plot: RC Tiefpass ---
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.semilogx(f_lp_range, 20*np.log10(np.abs(H_lp)))
ax1.set_title("RC-Tiefpass – Amplitudengang")
ax1.set_xlabel("Frequenz [Hz]")
ax1.set_ylabel("Amplitude [dB]")
ax1.grid(True, which="both")

ax2.semilogx(f_lp_range, phase_lp)
ax2.set_title("RC-Tiefpass – Phasengang")
ax2.set_xlabel("Frequenz [Hz]")
ax2.set_ylabel("Phase [°]")
ax2.grid(True, which="both")

plt.tight_layout()
plt.show()