import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Konstanten
f = 50  
T = 1/f 
omega = 2 * np.pi * f 
U_hat = 325  
I_hat = 10

t = np.linspace(0, 2*T, 1000)

# ===== Leistungsverläufe für verschiedene Phasenwinkel =====
fig2, axes = plt.subplots(3, 1, figsize=(14, 12))
fig2.suptitle('Teil 2: Spannung, Strom und Leistung bei verschiedenen Phasenverschiebungen', 
              fontsize=16, fontweight='bold')

phasen = [
    {'phi': 0, 'name': 'φ = 0° (Rein ohmsch)', 'color': 'blue'},
    {'phi': 90, 'name': 'φ = 90° (Rein induktiv)', 'color': 'red'},
    {'phi': -45, 'name': 'φ = -45° (Gemischte Last, kapazitiv)', 'color': 'green'}
]

for idx, phase_info in enumerate(phasen):
    ax = axes[idx]
    phi = np.radians(phase_info['phi'])
    
    # Spannung, Strom und Leistung
    u = U_hat * np.sin(omega * t)
    i = I_hat * np.sin(omega * t + phi)
    s = u * i
    
    # Effektivwerte und Leistungen
    U_eff = U_hat / np.sqrt(2)
    I_eff = I_hat / np.sqrt(2)
    P = U_eff * I_eff * np.cos(phi)
    Q = U_eff * I_eff * np.sin(phi)
    S = U_eff * I_eff
    
    # Plotten
    ax2 = ax.twinx()
    
    line1 = ax.plot(t * 1000, u, 'b-', linewidth=2, label='Spannung u(t)')
    line2 = ax.plot(t * 1000, i * (U_hat/I_hat), 'r-', linewidth=2, 
                    label=f'Strom i(t) (skaliert, φ={phase_info["phi"]}°)')
    line3 = ax2.plot(t * 1000, s, 'g-', linewidth=2.5, alpha=0.7, label='Leistung s(t)')
    ax2.axhline(y=P, color='purple', linestyle='--', linewidth=1.5, label=f'P = {P:.1f}W')
    ax2.fill_between(t * 1000, 0, s, alpha=0.2, color='green')
    
    ax.grid(True, alpha=0.3)
    ax.set_ylabel('Spannung/Strom [V/A]', fontsize=11)
    ax2.set_ylabel('Leistung [W]', fontsize=11, color='green')
    ax.set_title(f'{phase_info["name"]}   |   P={P:.0f}W, Q={Q:.0f}var, S={S:.0f}VA, cos φ={np.cos(phi):.3f}', 
                 fontsize=12, fontweight='bold')
    ax.set_xlim(0, 2*T*1000)
    
    # Legende
    lines = line1 + line2 + line3
    labels = [l.get_label() for l in lines]
    lines.append(ax2.lines[1])
    labels.append(ax2.lines[1].get_label())
    ax.legend(lines, labels, loc='upper right')
    
    if idx == 2:
        ax.set_xlabel('Zeit [ms]', fontsize=11)

plt.tight_layout()
plt.show()

# ===== TEIL 3: Phasenbeziehungen bei R, L, C =====
fig3, axes = plt.subplots(3, 1, figsize=(14, 12))
fig3.suptitle('Teil 3: Phasenbeziehungen bei verschiedenen Bauelementen', 
              fontsize=16, fontweight='bold')

komponenten = [
    {'name': 'Ohmscher Widerstand R', 'phi': 0, 'beschreibung': 'u und i in Phase'},
    {'name': 'Induktivität L', 'phi': 90, 'beschreibung': 'i eilt u um 90° nach'},
    {'name': 'Kondensator C', 'phi': -90, 'beschreibung': 'i eilt u um 90° vor'}
]

for idx, komp in enumerate(komponenten):
    ax = axes[idx]
    phi = np.radians(komp['phi'])
    
    u = U_hat * np.sin(omega * t)
    i = I_hat * np.sin(omega * t + phi)
    
    ax.plot(t * 1000, u, 'b-', linewidth=2.5, label='Spannung u(t)')
    ax.plot(t * 1000, i * (U_hat/I_hat), 'r-', linewidth=2.5, label='Strom i(t) (skaliert)')
    
    # Nulldurchgänge markieren
    zero_crossings_u = np.where(np.diff(np.sign(u)))[0]
    zero_crossings_i = np.where(np.diff(np.sign(i)))[0]
    if len(zero_crossings_u) > 0:
        ax.axvline(x=t[zero_crossings_u[0]] * 1000, color='b', linestyle=':', alpha=0.5)
    if len(zero_crossings_i) > 0:
        ax.axvline(x=t[zero_crossings_i[0]] * 1000, color='r', linestyle=':', alpha=0.5)
    
    ax.grid(True, alpha=0.3)
    ax.set_ylabel('Amplitude [V/A]', fontsize=11)
    ax.set_title(f'{komp["name"]}   |   {komp["beschreibung"]}   |   φ = {komp["phi"]}°', 
                 fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_xlim(0, 2*T*1000)
    
    if idx == 2:
        ax.set_xlabel('Zeit [ms]', fontsize=11)

plt.tight_layout()
plt.show()
