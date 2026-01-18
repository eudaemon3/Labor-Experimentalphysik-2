# Promt für LLM

Rolle & Ziel: Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es, mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das letzte Kapitel Fourieroptik schreiben.
Input: 
1. Bestehender Laborbericht Abbe-Theorie
2. Python code zur Auswertung der Aufgabe: 

```python
def extract_intensity_profile(image_path):

    # Bild laden und in Graustufen konvertieren
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)
    height, width = img_array.shape
    y_start = height // 2 - 40
    y_end = height // 2 + 40

    # Mittelung über vertikalen Bereich
    profile = np.mean(img_array[y_start:y_end, :], axis=0)
    
    return profile

def plot_intensity_profile(profile):
    fig, ax = plt.subplots(figsize=(6,4))
    
    x = np.arange(len(profile))
    
    # Normierung auf Maximum
    profile_norm = profile / np.max(profile)
    
    ax.plot(x, profile_norm, linewidth=1.5, color='blue')
    ax.set_xlabel(r'$x$ / Pixel', fontsize=16)
    ax.set_ylabel(r'$I/I_\text{max}$ / 1', fontsize=16)
    ax.grid(True, alpha=1)
    ax.set_ylim([0, 1.1])
    
    plt.tight_layout()
    plt.show()

path = "/home/loki/Workspace/Labor/Experimentalphysik2/01_AbbeTheorie/data/"
files = {
    '0': 'V02_Objekt_Beugung_0.png',
    '1': 'V02_Objekt_Beugung_1.png',
    '3': 'V02_Objekt_Beugung_3.png',
    '5': 'V02_Objekt_Beugung_5.png',
    'alle': 'V02_Objekt_Beugung.png'
}

for name, filename in files.items():
    profile = extract_intensity_profile(path + filename)
    plot_intensity_profile(profile)

```

Anforderungen an den Output:
* Schreibe mir das Kapitel {Fourieroptik} für den bestehenden Bericht. 
* Gib den unter Kapiteln passende Überschriften
* Analysiere den alten Laborbericht und den Teil des bestehenden BErichts und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau.
* Die Formatierung der Tabellen und Bilder sind ebenfalls aus den Berichten zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Subindizes sind als text zu formatieren $X_\text{y}$ und alle MEsswerte sind mit einer Unsicherheit anzugeben.
* Diese Kapitel sollte nicht zu lang sen, da es nur ein optionales Kapitel ist.

Inhalt: Für den letzten Versuch soll eine Verbiundung zur Fourier Optik hergestellt werden. Dazu wird der Intensitätsquerschnitt der in Versuch 2 Angefertigten Objektbilder betrachtet. Es wird dazu über den Bereich der mittleren 80 pixel der Mittelwert gebildet und normiert. Der Graph wird dann für die verschiedenen Anzahlen der sichtbaren Beugungsordnungen gezeigt. Die fünf Abbildungen solle nin einer gemeinsamen Grafik angezeigt werden.  

* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.

Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil als Latex code aus.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Beginne mir einer Analyse des bestehenden Berichts! Wichtige Punkte die du übernehmen kannst sind:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach das Kapitel gemäß der neuen Aufgabe.

# Promt für LLM

Rolle & Ziel: Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das Kapitel Auswertung schreiben. Im letzten Schritt soll die Auswertung für den vierten Versuch "Farbeindruck verschiedener Proben" verfasst werden.
Input: 
1. Bestehender Laborbericht Spektralphotometer:
2. Python code zur Auswertung der Aufgabe bestehend aus zwei Teilen: 

Anforderungen an den Output:
* Schreibe mir das Kapitel "Farbeindruck verschiedener Proben" für den aktuellen Bericht. 
* Verwende die bestehende Analyse und analysiere den bestehenden Bericht und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau. Achte darauf keine Wortwiederholungen zu verwenden.
* Die Formatierung der Tabellen und Bilder sind ebenfalls aus den Berichten zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Subindizes sind als text zu formatieren $X_\text{y}$ und alle Messwerte sind mit einer Unsicherheit anzugeben.
* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.

Inhalt: Für den Vierten Versuch sollen lediglich die Spektren verschiedener Messungen verglichen werden und dadurch der Farbeindruck erklährt werden. Die genaue Aufgabe ist es: "qualitativ möglich, aus photospektroskopischen Daten den entsprechenden Farbeindruck zu erklären". Erklähre dazu kurz dass in einer Figur links die Rohdaten der Messung von MEtylenblau und den Farbfiltern gemeinsam angeführt sind und rechts ein Vergleich der berechneten Transmissionen $T$ zu erkennen ist. Gib der Abbildung dann noch eine passende caption. Dies ist alles zur Auswertung. 
Schreibe ebenfalls die Diskussion des Kapitels neu und beschreibe mehr, dass beim blauen Farbfilter und MEtylenbalu eine große Transmission im blauen bereich z erkennen ist. Beim roten Farbfilter entsprechend im blauen Wellenlängenbereich keine Transmission dafür stark im roten. Die rohdaten zeigen das identische Verhalten an, allerdings sind die relativen Anteile im Transmissionsspektrum viel besser erkennbar. Die Länge der Diskussion sollte aber in etwa gleich lang sein wie der bestehnde Teil, vielleicht um 20% länger. Auf jeden Fall passend zum restlichen Bericht.   


Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil als Latex code aus.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Verwende die bestehende Analyse der alten Berichte und verfasse das neue Kapitel basierend auf dieser.  
Betrachte ebenfalls den bestehenden Bericht um das neue Kapitel möglicht passend in den Beericht einzufügen. Als nächstes betrachte den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach das Kapitel gemäß der neuen Aufgabe.

```python
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement, load_measurement_var, plot_visible_spectrum

plt.style.use('science')
plt.rcParams.update({'font.size': 15})

# Farbfilter
folder_filter = "02_Spektralphotometer/data/Messung01"
data_f = load_measurement(1, folder_filter)
lam_f, I0_f = data_f["Referenz"]
IT_f_blau = data_f["Blau"][1]
IT_f_rot  = data_f["Rot"][1]

# Methylenblau
folder_methyl = "02_Spektralphotometer/data/Messung03"
data_m = load_measurement_var(1, folder_methyl, "methyl")
lam_m, I0_m = data_m["Referenz"]
IT_m = data_m["Blau"][1]

# Transmission
T_f_blau = IT_f_blau / I0_f
T_f_rot  = IT_f_rot  / I0_f
T_m      = IT_m / I0_m

# Plot 1
# -------------------------------------------------------------------------------

fig1, axes = plt.subplots(1,2, figsize=(10, 4.5))

ax = axes[0]
plot_visible_spectrum(
    ax=ax,
    x_min=min(lam_f), x_max=max(lam_f),
    y_min=-0.1, y_max=-0.07,
)

ax.plot(lam_f, IT_f_blau, color="tab:blue", linewidth=1.3, label=r"Filter blau")
ax.plot(lam_f, IT_f_rot, color="crimson", linewidth=1.3, label=r"Filter rot")
ax.plot(lam_m, IT_m, color="black", linewidth=1.3, label=r"Methylenblau")
ax.plot(lam_f, I0_f, color="gray", linestyle="-", linewidth=1.3, label=r"Referenz")

ax.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=17)
ax.set_ylabel(r"Intensität $I$ / a.u.", fontsize=17)
ax.grid(True)

# Legende unter der Achse
handles, labels = ax.get_legend_handles_labels()
leg1 = fig1.legend(
    handles, labels,
    loc="lower center",
    bbox_to_anchor=(0.52, -0.01),
    ncol=2, fontsize=17
)

ax2 = axes[1]

plot_visible_spectrum(
    ax=ax2, show_edge=False,
    x_min=380, x_max=800,
    y_min=-0.1, y_max=-0.07,
    alpha_def=1
)

ax2.plot(lam_f, T_f_blau, color="tab:blue", linewidth=1.3, label="T (Filter blau)")
ax2.plot(lam_f, T_f_rot, color="crimson", linewidth=1.3, label="T (Filter rot)")
ax2.plot(lam_m, T_m, color="black", linewidth=1.3, label="T (Methylenblau)")

ax2.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=17)
ax2.set_ylabel(r"Transmission $T$ / 1", fontsize=17)
ax2.set_xlim(400, 780)
ax2.set_ylim(-0.1, 1.1)
ax2.grid(True)


plt.tight_layout(rect=[0, 0.15, 1, 1]) # type: ignore

plt.show()
```