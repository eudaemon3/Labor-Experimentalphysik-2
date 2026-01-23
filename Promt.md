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

Rolle & Ziel: Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es mir beim Schreiben meines aktuellen Laborberichts Interferometer zu helfen. Du sollst dazu das Kapitel Auswertung schreiben. Im diesem letzten Schritt soll die Auswertung für den vierten Versuch verfasst werden.
Input: 
1. Bestehender Laborbericht mit Bildern.
2. Python code zur Auswertung der Aufgabe. 

Anforderungen an den Output:
* Schreibe mir das vierte Kapitel für den aktuellen Bericht. Gib dem Kapitel eine passende Überschrift.
* Analysiere den bestehenden Bericht und baue auf der bestehenden Analyse auf. Übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der analysierten Kapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau. Achte darauf keine Wortwiederholungen zu verwenden und dass der Text zum rest des Berichtes passt.
* Die Formatierung der Tabellen und Bilder sind ebenfalls aus den Berichten zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Subindizes sind als text zu formatieren $X_\text{y}$ und alle Messwerte sind mit einer Unsicherheit anzugeben.
* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.
* Im bestehenden Bericht sind bereits alle bilder eingefügt. Die captions dieser Figuren sind mithilfe der inhaltlichen Angaben zu überarbeiten und auszubessern.

Inhalt: Für den vierten Versuch soll die Größe der Lichtquelle bestimmt werden, bei der für einen bestimmten Abstand d vom Doppeltspalt das Licht noch räumlich kohärent ist. Dazu wird für die drei verfügbaren Spaltabstände des Doppelspalts jeweils das ertste Kontrastminimum durch verstelle nder Spaltbreite $w$ ermittelt. Die 3 zugehörigen Interferenzmuster sind in der ersten Abbildung angeführt. Der markierte Bereich dient hier nur zu visualisierungs Zwecken.
Als nächstes werden die Messpunkte und der Theoretisch erwartete Verlauf in einem Diagramm w(d) dargestellt. Die Unsicherheit für w ergibt sich aus dem in Kapitel 1 angeführen Argumenten der Nullpunktverschiebung.


Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil als Latex code aus.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.
* Wichtiger Hinweiß: Die Diskussion soll vorerst nicht geschrieben werden. Fokusiere dich nur auf die Auswertung

Beginne mir einer Analyse des bestehenden Berichts und erweitere die bestehende Analyse! Wichtige Punkte die du übernehmen kannst sind:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach das Kapitel gemäß der neuen Aufgabe.

```python Skript
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from lib import slit_measure_to_mm
from matplotlib.patches import Rectangle
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

folder = "03_Interferometer/data/Versuch04/"
ROI = (50, 425, 950, 130)
slit_width = [(4,35), (3,5), (1,4)]
slit_width = list(map(slit_measure_to_mm, slit_width))
delta_width = 0.1 #mm

d_dist = np.array([0.13, 0.23, 0.43]) #mm
lam = 0.000633 #mm
f1 = 300 #mm

image_files = sorted([
    f for f in os.listdir(folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

fig, axes = plt.subplots(1, 3, figsize=(8, 2.5))

for i, filename in enumerate(image_files):
    ax_img = axes[i]
    img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)

    # ROI & Profil
    x, y, w, h = ROI
    roi = img[y:y+h, x:x+w] #type: ignore

    ax_img.imshow(img, cmap="gray", aspect="auto")
    ax_img.add_patch(Rectangle((x, y), w, h,
                            edgecolor="red", facecolor="none", 
                            linewidth=0.9, linestyle='--'))
    ax_img.set_title(rf"Doppelspalt $d = {d_dist[i]:.2f}\,\mathrm{{mm}}$", fontsize=16)
    ax_img.axis("off")

plt.tight_layout()
plt.show()

w_theo = lambda d : f1*lam/(2*d)
d_plot = np.linspace(0.1, 0.8, 1000)

fig,ax = plt.subplots(1,1,figsize=(6,4))
ax.errorbar(
    d_dist,
    slit_width,
    yerr=delta_width,
    marker='d',
    linestyle='none',
    capsize=5,
    color='crimson',
    label="Messdaten"
)

ax.plot(
    d_plot,
    w_theo(d_plot),
    'b-',
    label=r"Theorie: $w(d) = f_1\lambda / d$"
)

ax.set_xlabel(r"Spaltabstand $d$ / mm", fontsize=16)
ax.set_ylabel(r"Breite $w$ / mm", fontsize=16)

ax.grid(True)
ax.legend(fontsize=16, frameon=True)

plt.tight_layout()
plt.show()
```

