import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# -------------------------------------------------------
# Messdaten
# -------------------------------------------------------

# Forward (Durchlass)
I_forward = np.array([12.95, 28.0, 42.52, 57.29, 71.7, 82.4, 93.8, 102.2,
                      111.9, 122.5, 132.3, 142.1, 151.9, 161.6, 172.3, 181.8, 191.9])  # mA
U_forward = np.array([0.698, 0.732, 0.750, 0.763, 0.773, 0.779, 0.784, 0.788,
                      0.792, 0.796, 0.799, 0.802, 0.805, 0.808, 0.810, 0.813, 0.815])  # V

# Reverse (Sperrrichtung)
U_reverse = np.array([4.813, 11.16, 18.86, 25.16, 31.59, 35.65, 39.71])  # V
I_reverse = np.array([0.001, 0.0014, 0.0018, 0.0022, 0.0025, 0.0027, 0.003])  # µA


# -------------------------------------------------------
# Formatter (wie im Beispiel)
# -------------------------------------------------------

def diode_ytick_formatter(value, pos):
    if value >= 0:
        return f"{value:.0f} mA"
    else:
        # Umrechnung nA = µA * 1000
        nA = -value * 1000
        return f"-{nA:.0f} nA"
    

    
formatter = ticker.FuncFormatter(diode_ytick_formatter)


# -------------------------------------------------------
# Plot Setup
# -------------------------------------------------------

figure = plt.figure(1, (14, 8))
axe = plt.subplot(111)

axe.set_title("I-U-Diodenkennlinie aus Messdaten")
axe.set_xlabel("Spannung U (V)")
axe.set_ylabel("Strom I (mA / nA)")

axe.grid(True)

# Achsen wie im Beispiel
axe.axhline(0, color='black', linewidth=1)
axe.axvline(0, color='black', linewidth=1)

# Schattierte Bereiche
#axe.axvspan(-40, 0, facecolor='green', alpha=0.15)
#axe.axvspan(0, 0.7, facecolor='blue', alpha=0.10)
#axe.axvspan(0.7, 2, facecolor='blue', alpha=0.20)

# Bereichslimits
axe.set_xlim(-40, 2)
axe.set_ylim(-4, 220)  # mA oben, nA umgerechnet unten


axe.plot(U_forward, I_forward, 'o-', label="Durchlassrichtung")

I_rev_plot = -I_reverse * 1000    # µA → nA, dann negativ
U_rev_plot = -U_reverse

axe.plot(U_rev_plot, I_rev_plot, 's-', label="Sperrrichtung")

axe.yaxis.set_major_formatter(formatter)

axe.legend()
plt.tight_layout()
plt.show()