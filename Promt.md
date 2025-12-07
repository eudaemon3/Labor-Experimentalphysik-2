# Promt für LLM

Rolle & Ziel: Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es, mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das Kapitel Auswertung schreiben.
Input: 
1. Alter Laborbericht Halbleiterdiode:
2. Bestehender Laborbericht:
3. Python code zur Auswertung der Aufgabe: 

```python
# Werte Einlesen
data = pd.read_csv('data/V1_Hochpass.csv', dtype=float, header=0)
freq, U_e, U_a, phi = data.to_numpy().T     # Hz, V, V, Grad
dU_e = U_e * 0.02 # Abschätzung Unsicherheit Oszilloskop siehe Kapitel 1
dU_a = U_a * 0.02
dphi = 0.5     # Grad
df = freq * 0.001

# Theoretische Größen
R1 = 2700       # Ohm
dR = R1*0.05
C = 100e-9      # F
dC = C*0.1

# Grenzfrequnenz:
f_G = 1/(2*np.pi*R1*C)
df_G = f_G * (dC/C + dR/R1)
print(f_G, df_G) ## Output: 589.4627521922049 88.41941282883074

# Theoreische Kurven
w_hp = 2 * np.pi * freq
H_hp = 1j * w_hp * R1 * C / (1 + 1j * w_hp * R1 * C)

Q_theo = 20 * np.log10(np.abs(H_hp))
phi_theo = np.angle(H_hp, deg=True)   

# Gemessene Verstärkung und Phase
Q_mess = 20 * np.log10(U_a / U_e)
k = 20.0 / np.log(10.0)
dQ_mess = k * (dU_a / U_a + dU_e / U_e) 

fig, (ax,ax2) = plt.subplots(1, 2, figsize=(10, 4))

# --- Verstärkung (links) ---
ax.set_xscale("log")
ax.set_xlabel(r"$f$ / Hz", fontsize=16)
ax.set_ylabel(r"$Q$ / dB", fontsize=16)

ax.errorbar(freq, Q_mess, yerr=dQ_mess,  fmt="bd", label="Messwerte", markersize=5, capsize=5)
ax.set_xlim(min(freq)-15, max(freq)+3000)
ax.plot(freq, Q_theo, "-", label="Theorie", linewidth=1, color='crimson')

ax.axvline(f_G, color="black", linestyle=":", linewidth=1.3, label=r'$f_\text{G}$')
ax.axhline(-3, color="black", linestyle=":", linewidth=1.3)

ax.grid(True, ls="--", which="minor", alpha=0.4)
ax.grid(True, ls="-", which="major", alpha=1)

# --- Phase (rechts) ---
ax2.set_xscale("log")
ax2.set_xlabel(r"$f$ / Hz", fontsize=16)
ax2.set_ylabel(r"$\varphi$ / deg",fontsize=16)

ax2.errorbar(freq, phi, yerr=dphi, fmt="bd", label="Messwerte", markersize=5, capsize=5)
ax2.set_xlim(min(freq)-15, max(freq)+3000)
ax2.plot(freq, phi_theo, "-", label="Theorie", linewidth=1, color='crimson')

ax2.axvline(f_G, color="black", linestyle=":", linewidth=1.3)
ax2.axhline(45, color="black", linestyle=":", linewidth=1.3)

ax2.grid(True, ls="--", which="minor", alpha=0.4)
ax2.grid(True, ls="-", which="major", alpha=1)

lines_1, labels_1 = ax.get_legend_handles_labels()
plot_lines = [lines_1[2], lines_1[0], lines_1[1]]
plot_labels = [labels_1[2], labels_1[0], labels_1[1]]
# ax1.legend(lines_1, labels_1,loc="lower right", frameon=True, fontsize=16)
fig.legend(
    plot_lines, plot_labels,
    loc="lower center",
    ncol=3,
    fontsize=16,
    bbox_to_anchor=(0.525, -0.06)   # move the legend slightly below the subplots
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.23)  # make space for legend
```

Anforderungen an den Output:
* Schreibe mir nur das Kapitel Auswertung für den ersten Versuch Hochpass. 
* Analysiere den alten Laborberichte und den bestehenden Bericht und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau.

Inhalt:
Der Inhalt für den ersten Versuch gliedert sich in drei Abschnitte:
1. Im ersten Schritt wird eine Schaltung von einem Hochpassfilter aufgabeaut mit den Komponenten aus dem angegebenen code. Von diesem wird im ersten Schritt die Grenzfrequenz berechnet. Dann wird in einem Bereich von +- einer Dekade um die Grenzfrequnz die Eingangsspannung $U_\text{E}$, die Ausgangsspannung $U_\text{A}$ und der Phasenversatz $\varphi$ gemessen. Als eingang dient eine Sinusshchwingung mit 2 V Peak to Peak. Diese Werte werden dann in einem Bode diagramm aufgetragen, wobei links das Amplitudenverhältnis $Q$ in Dezibel gegenüber der logarithmisch skalierten Frerqunz aufgetragen ist(Plot ist also doppelt logarithmisch). Rechts wird die Pahse gegenüber der logarithmisch sklierten Frequnz aufgetragen. Außerden wird der Theoretische Verlauf der Übertragungsfunktion berechnet und ebenfalls im Bode Diagramm angeführt. Genaueren Kontext entnimm dem beigefügten Python code!
2. Im zweiten Unterkapitel wird die Sprungantwort der Schaltung dargestellt. Dazu wählt man als Eingangssignal eine Rechteckspannung mit 2 V peak to peak bei einem Fünftel der Grenzfrequenz und einem Fünzigstel der Grenzfrequenz. Die jeweiligen Oszilloskop-Aufnahmen der Sprungantwort sind in den zwei Abbildungen der Figur zu erkennen.
3. Zuletzt wird noch das Verhalten als Differenzierer Untersucht. Dazu wählt man weiterhin als Eingangssignal mit 2V Peak-Peak und einem Fünfzigstel der Grenzfrequnenz $f_\text{G} / 50$ nun allerdings als Dreieckspannung und zeichnet das Verhalten der Schaltung mit dem Oszilloskop auf. Dies ist in der Abbiuldung zu sehen.

* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.
* Die Formatierung der Tabellen und Bilder sind aus dem alten Bericht zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Tabellen sind entsprechend siunitx zu formatieren, Subindizes sind als text zu formatieren $X_\text{y}$, alle MEsswerte sind mit einer Unsicherheit anzugeben.

Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil aus, bereit zum Einfügen als Latex code in ein Dokument.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Beginne mir einer Analyse des alten Berichts! Wichtige Punkte die du übernehmen kannst sind:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere den vorgegebenen code, den bestehenden Bericht und die Inhaltlichen Anforderungen und schreibe danach die neuen Kapitel gemäß der neuen Aufgabe.


# Promt für LLM

Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es, mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das Kapitel Auswertung für den dritten Versuch RLC Paralell Schwingkreis schreiben.
Input: 
1. Alter Laborbericht Halbleiterdiode aus der vorigen Nachricht
2. Bestehender Laborbericht:
3. Python code zur Auswertung der Aufgabe: 
```python
R2B = 47       # Ohm
dR = R2B * 0.05
C = 100e-9      # F
dC = C*0.1
L = 10e-3      #H
dL = L*0.1

# Nur Qualitative Analyse unf Vergleich!
# Unsicherheit wird nicht angegeben, da relativ groß
f0 = 1/(2*np.pi*np.sqrt(L*C))
print(f'f_0 = {f0:.2f} ')

fC = f_0 * np.sqrt(1 - R2B**2 * C / (2*L))
fL = f_0 * np.sqrt((1+ np.sqrt(1+(2*R2B**2 * C/L)))/2)
print(f'f_C = {fC:.2f}')
print(f'f_L = {fL:.2f}')

f0_mess = 4897
df0_mess = f_0mess * 0.001
fC_mess = 4776 
dfC_mess = fC_mess * 0.001
fL_mess = 5064
dfL_mess = fL_mess * 0.001
print(f'f_0_mess = {f0_mess} pm {df0_mess:.0f}')
print(f'f_C_mess = {fC_mess} pm {dfC_mess:.0f}')
print(f'f_L_mess = {fL_mess} pm {dfL_mess+1:.0f}')
```
Output:
```
f_0 = 5032.92 
f_C = 5005.05
f_L = 5060.34
f_0_mess = 4897 pm 5
f_C_mess = 4776 pm 5
f_L_mess = 5064 pm 6
```
4. Gegebene Messdurchführung:
Aufbau gemäß Abbildung 6. Verwenden Sie den Dämpfungswiderstand R2B
der letzten Übung. Sie können den Versuchsaufbau der vorhergehenden Übung direkt
übernehmen. Berechnen Sie mit den Werten der verwendeten Bauteile die zu erwartende
Frequenz f_C bzw f_L.
Stellen Sie die Resonanzfrequenz f_0, bei der die Phase φ gleich null ist, ein. Verringern Sie
die Frequenz von UE und Sie werden feststellen, dass UC größer wird. Allerdings verändert
sich aufgrund der Frequenzabhängigkeit des Gesamtwiderstandes der Schaltung und der
daraus resultierenden „Überlastung“ des Signalgenerators auch die Amplitude von UE.
Regeln Sie die Amplitude von UE am Signalgenerator nach, sodass diese wieder den Wert bei
f_0 aufweist. Suchen Sie auf diese Weise das Maximum von UC.
Gesucht: Frequenz fC, bei der das Verhältnis von UC zu UE maximal wird. Und Frequnz fL bei der das Verhältnis von UL zu UE maximal wird. Vergleich von
„gemessenen“ und „berechneten“ Werten, Kommentierung der Ergebnisse mit Bezug auf
eventuell auftretende Abweichungen.

Anforderungen an den Output:
* Schreibe mir noch das letzte Unter-Kapitel für den vierten Versuch RLC Serienschwingkreis. 
* Analysiere dazu den alten und den bestehenden Bericht nocheinmal und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau.
* Die Formatierung der Tabellen und Bilder sind aus dem alten Bericht zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. 

Inhalt:
Für den vierten Verscuh wird die Messung entsprechend der Angabe durchgeführt und einerseits die Theorteischen Frequnenzen berechnet und die Gemessenen Frequnenzen ermittelt. Beschreibe dazu kurz in ca 2 Satzren die verwendete Messmethode und präsentiere die Berechneten und gemessenen Frequenzen übertsichtlich in einer Tabelle.  

Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil aus.
* Der Output soll als Latex code in einem eigenen code block erfolgen.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Beginne mir einer Analyse des alten und des bestehenden Berichts! Falls nötig, kannst du das alte Dokument analysieren, um:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere den vorgegebenen code, die gegebene Messdurchführung und die Inhaltlichen Anforderungen und schreibe danach die neuen Kapitel gemäß der neuen Aufgabe.
