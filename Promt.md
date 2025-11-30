# Promt für LLM

Rolle & Ziel: Du bist weiterhin ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es, mir beim Schreiben meines aktuellen Laborberichts zu helfen.
Input: 
1. Alter Laborbericht Halbleiterdiode aus der vorigen Nachricht 
2. Alter Laborbericht Mikroskop aus der vorigen Nachricht 
3. Bestehedner Laborbericht mir den ersten zwei Kapiteln:
4. Python code zur Auswertung der Aufgabe: 

```python
U_R = 9.323        # V
U_C = 8.922        # V
R   = 68           # Ohm
C   = 47e-6        # F
t_phi = 4.22e-3    # s
T = 20e-3          # s
tan_delta = 0.05

I = U_R / R
R_I = T / (2* np.pi * C * tan_delta)

I_R = U_C / R_I
I_C = I_R / tan_delta

phi_meas = 2 * np.pi * (t_phi / T)    # rad
phi_meas_deg = np.degrees(phi_meas)

plt.rcParams.update({"font.size": 14, "figure.dpi": 120})

# Skalierungen auf 1
Scale_I = 1 / I
Scale_U = 1 / U_C

fig = plt.figure(figsize=(5,5))
ax = plt.gca()
ax.set_aspect("equal", adjustable="box")

plt.grid(True, linestyle="--", alpha=1)

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.05, 1.05)

plt.xlabel(r"$\mathfrak{Re}$", fontsize=16)
plt.ylabel(r"$\mathfrak{Im}$", fontsize=16)

arrowstyle = "-|>"
ms = 10

# U_C (blau)
arr_UC = FancyArrowPatch(
    (0, 0), 
    (U_C*Scale_U, 0),
    arrowstyle=arrowstyle, color="blue",
    linewidth=2, mutation_scale=ms,
    shrinkA=0, shrinkB=0)
ax.add_patch(arr_UC)
plt.text(U_C*Scale_U*1.01, 0.015, r"$U_C$", color="blue", fontsize=16)

# I_C (rot)
arr_IC = FancyArrowPatch(
    (0,0),
    (0, I_C*Scale_I),
    arrowstyle=arrowstyle, color="tab:orange",
    linewidth=1.5, mutation_scale=ms,
    shrinkA=0, shrinkB=0)
ax.add_patch(arr_IC)
plt.text(-0.08, I_C*Scale_I*0.99, r"$I_\text{C}$", color="tab:orange", fontsize=16)

arr_IR = FancyArrowPatch(
    (0,I_C*Scale_I), (I_R*Scale_I, I_C*Scale_I),
    arrowstyle=arrowstyle, color="tab:orange",
    linewidth=1.5, linestyle="-", mutation_scale=ms,
    shrinkA=0, shrinkB=0)
ax.add_patch(arr_IR)
plt.text(I_R*Scale_I + 0.02, I_C*Scale_I*0.99, r"$I_{\mathrm{R}}$", color="tab:orange", fontsize=16)

# Gemessener I (rot)
I_meas_x = I*Scale_I*np.cos(phi_meas)
I_meas_y = I*Scale_I*np.sin(phi_meas)

arr_I_meas = FancyArrowPatch(
    (0,0), (I_meas_x, I_meas_y),
    arrowstyle=arrowstyle, color="crimson",
    linewidth=1.5, mutation_scale=ms,
    shrinkA=0, shrinkB=0)
ax.add_patch(arr_I_meas)
plt.text(I_meas_x*1.1, I_meas_y*0.98, r"$I$", color="crimson", fontsize=16)

# Theoretischer Strom (gestrichelt)
arr_I_theo = FancyArrowPatch(
    (0,0), (I_R*Scale_I, I_C*Scale_I),
    arrowstyle=arrowstyle, color="crimson",
    linewidth=1.5, linestyle="--", 
    mutation_scale=ms, shrinkA=0, shrinkB=0)
ax.add_patch(arr_I_theo)

arc_radius = 0.11
arc = Arc((0,0),
          2*arc_radius, 2*arc_radius,
          angle=0,
          theta1=0,
          theta2=phi_meas_deg,
          linewidth=1.2,
          color="black")
ax.add_patch(arc)

plt.text(
    arc_radius*1.2*np.cos(phi_meas/2),
    arc_radius*1.2*np.sin(phi_meas/2),
    r"$\varphi_{\mathrm{mess}} \approx %.2f^\circ$" % phi_meas_deg,
    fontsize=16
)

plt.show()
```

Anforderungen an den Output:
* Schreibe mir nur das Kapitel Auswertung für den dritten Versuche. 
* Analysiere die beiden alten Laborberichte und den bestehenden Bericht und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau.

Inhalt:
* Der Inhalt für den dritten Versuch soll beschreiben, dass mit dem Oszilloskop der Verlauf der Spannung über einen Widerstand $R$ und einen KOndensator $C$, sowie der Effektivwert gemessen. Diese zwei Verläufe sind in einer Abbildung zu sehen (Caption für die Abbildung Ch1 = U_R1 und CH2 = U_C1). Mit dem Oszilloskop wurde außerdem die Phasenverschiebung mit einer Cursor Messung die Phasenverschiebung bestimmt, für die UNsicherheit wurde ein Achtel der division also 0.25 ms gewählt und der Winkel berechnet (Winkel phi mit Unscherheit angeben). Als nächstes wird noch der innenwiderstand R_I für das Ersatzschaltblid des Realen Kondensators berechnet mit dem aus der Angabe gegebene Wert tan(delta) = 0.05. Aus R_I folgen dann die Ströme I_R und I_C.
Die ermittelten Größen werden in einem Zeigerdiagramm aufgetragen. Die in dem PLot angezeigen Zeiger entnimm aus dem code. Zuletzt noch eine kurze beschreibung des Plots

* Verwende die folgende Struktur für das Kapitel wobei nur die Auswertung zu schreiben ist: 
\section{Strom und Spannung an einem Kondensator}
\subsection{Auswertung}
\subsection{Diskussion}

* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.
* Die Formatierung der Tabellen und Bilder sind aus dem alten Bericht zu entnehmen. Wichtig ist auch immer eine passende caption zu verwenden.
Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil aus, bereit zum Einfügen als Latex code in ein Dokument.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

BEginne mir einer Analysie die zwei alten BErichte aus der vorigen Nachricht. Als nächstes gehe durch den bestehenden Bericht durch und erweitere die Analyse. Wichtige Punkte die du übernehmen kannst sind:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes  Analyse den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach die neuen Kapitel gemäß der neuen Aufgabe.