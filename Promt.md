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

Rolle & Ziel: Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es mir beim Schreiben meines aktuellen Laborberichts Signalleitung zu helfen. Du sollst dazu das Kapitel Vesuchsdurchführung und Auswertung für den fünften Versuch "Einfluss verschiedener Signalformen" verfassen.

Input: 
1. Bestehender Laborbericht mit Bildern.
2. Python code zur Auswertung der Aufgabe:

```python 
files = [
    "data50.csv",  # 1.0 MHz
    "data55.csv",  # 2.0 MHz
    "data56.csv",  # ~2.3 MHz (dip)
    "data57.csv",  # 2.4 MHz
    "data60.csv",  # 3.0 MHz
    "data61.csv",  # 4.0 MHz
]

folder_path = "data/Signalleitung/V05_sine"

fig, axes = plt.subplots(
    2, 3,
    figsize=(10, 6),
    sharex=True,
    sharey=True
)

legend_handles = None
legend_labels = None
axes = axes.flatten()

for i,ax in enumerate(axes):
    df = pd.read_csv(
        os.path.join(folder_path, files[i]),
        skiprows=3,
        header=None
    )

    time = df.iloc[:, 0].to_numpy()
    voltage1 = df.iloc[:, 1].to_numpy()
    voltage2 = df.iloc[:, 2].to_numpy()

    # ---- frequency determination via peaks ----
    voltage2_ac = voltage2 - np.mean(voltage2)
    peaks, _ = find_peaks(voltage2_ac, prominence=0.2*np.max(np.abs(voltage2_ac)))

    T = np.mean(np.diff(time[peaks]))
    frequency = 1 / T

    l1, = ax.plot(time * 1e6, voltage1, color="blue", lw=1)
    l2, = ax.plot(time * 1e6, voltage2, color="crimson", lw=1)

    if legend_handles is None:
        legend_handles = [l1, l2]
        legend_labels = [r"Eingang $U_1$", r"Ausgang $U_2$"]

    ax.set_title(fr"$f = {frequency/1e6:.2f}\,\mathrm{{MHz}}$", fontsize=16)
    ax.grid(True)
    ax.set_xlim(-1,1)
    if i in [0,3]:
        ax.set_ylabel(r"Voltage $U$ / V", fontsize=16)
    if i in [3,4,5]:
        ax.set_xlabel(r"Time $t$ / $\mu$s", fontsize=16)

fig.legend(
    legend_handles,
    legend_labels,
    loc='lower center',
    ncol=len(legend_labels),
    fontsize=16
)

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.show()
```

Anforderungen an den Output:
* Schreibe mir das fünfte Kapitel "Einfluss verschiedener Signalformen" für den aktuellen Bericht.
* Analysiere den bestehenden Bericht und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der analysierten Kapitel.
* Wichtig! Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau. Achte weiters darauf keine Wortwiederholungen und koplexe Ausdrücke zu verwenden.
* Die Formatierung der Tabellen und Bilder sind ebenfalls aus den Berichten zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Subindizes sind als text zu formatieren $X_\text{y}$ und alle Messwerte sind mit einer Unsicherheit anzugeben.
* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.
* Im bestehenden Bericht sind bereits alle Bilder eingefügt. Die captions dieser Figuren sind mithilfe der inhaltlichen Angaben zu überarbeiten.

Inhalt: 
Durchführung: Für den fünften Versuchsteil soll der Einfluss verschiedener Signalformen auf das Verhalten in einem Koaxial Kabel untersucht werden. Dazu wird die Schaltung aus Versuch 1a aufgebaut und anstatt mit Rechteckpulsen einmal mit einer Dreieckspannung von 100kHz und mit Sinussignalen verschiedener Frequnzen betrieben.

Auswertung: IN der ersten Abbildung ist der Verlauf der Dreieck Spannung am Eingang vom Kabel in gelb und am Ausgang in grün dargestellt. In der zweiten Abbildung jeweils U_1 und U_2 von 6 verschiedenen Sinus signalen mit den Frequnzen freq = [0.5, 1.0, 1.5, 2.0, 2.3, 2.4, 3.0, 4.0, 5.0] #MHz. Es ist jeweils der selbe ZEitabschnitt geplottet.

Diskussion:
BEi dem Dreiecksignal ist U_1 und U_2 nahezu ein identisches signal. BEi den verschiedenen Sinus Signalen erkennt man, dass bei 2.3 mHz ca das Eingangssignal null wird. Das liegt daran, dass diese Frequnz der ersten Harmonischen stehenden Welle entspricht. Die rücklaufende Welle überlagert sich destruktiv. Weitere Frequnzen bei welchen das selbe Verhaten festgestellt wurde sind 7.2 und 12.1 MHz was die Annahme der stehenden Welle bestätigt. Die 2 Frequnzen sind nicht in der Abbildung. 


Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil als Latex code aus.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.
* Wichtiger Hinweiß: Im bestehenden Bericht ist die Verscuhsdurchführung schon geschrieben. Überarbeite diese und schreibe mir das vollständige Kapitel 4.

Beginne mir einer Analyse des bestehenden Berichts und erweitere die bestehende Analyse. Wichtige Punkte die du übernehmen sollst sind:
* Wortwahl, Satzlänge und Übergänge,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach das Kapitel gemäß der neuen Aufgabe.
