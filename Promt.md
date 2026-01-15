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

Rolle & Ziel: Du bist weiterhin ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es immer noch, mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das Kapitel Auswertung schreiben. Im nächsten Schritt soll die Auswertung für den fünften Versuch Glasplatte verfasst werden.
Input: 
1. Bestehender Laborbericht Spektralphotometer 
2. Python code zur Auswertung der Aufgabe bestehend aus zwei Teilen: 
Anforderungen an den Output:
* Schreibe mir das Kapitel Dicke einer Glasplatte für den aktuellen Bericht. 
* Gib den unter Kapiteln passende Überschriften
* Verwende die bestehende Analyse und übernimm wie zuvor den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Unterkapitel.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau. Achte darauf keine Wortwiederholungen zu verwenden.
* Die Formatierung der Tabellen und Bilder sind ebenfalls aus den Berichten zu entnehmen. Wichtig ist immer eine passende caption der Figuren und Tabellen zu verwenden. Subindizes sind als text zu formatieren $X_\text{y}$ und alle Messwerte sind mit einer Unsicherheit anzugeben.
* Falls inhaltliche Unsicherheiten bestehen, formuliere plausible und physikalisch korrekte Annahmen.

Inhalt: Für den fünften Versuch soll die Dicke einer planparallelen Glasplatte durch Auswerten der Interferenzmaxima im Transmissionspektrum bestimmt werden. Dazu wird einmal das Referenzsspektrum und einmal das Intensitätsspektrum der glasplatte gemessen. Plot wie bei den vorigen Messungen. Hier reicht eine Messung, da das bilden des Mittelwerts die Genauigkeit der Position der Peaks nicht erhöht. Dazu ein kurzer Begründungsatz. Es wird entsprechend die Transmission berechnet und ein Bereich zwischen 700 und 720 nm ausgewählt. In diesem Bereich werden die Maxima mit einer Software \cite{peak_finder} charakterisiert und die zugehörigen Wellenlängen extrahiert. Aus nu = 1/lambda folgt dann der Zusammenhang mit der Wellenzahl. Mithilfe von einer linearen Regressionsrechnung wird nu gegenüber dem "Peak-Index" m aufgetragen und aus der Steigung die Dicke der Schicht bestimmt. 
Als alternative Methode wurde die Fourier Transformation verweendet: Aus dem ausgewählten Spektrum der Transmission T wird durch eine lineare Interpolation ein Spektrum abhängig von der Wellenzahl nu T(nu) gebildet und dann dieses Transformiert und nur der positive Teil vrwendet, da die Transformierte nu -> l einer Länge entspricht und nur l > 0 sinvoll ist. Wie zuvor wird die gemessene Länge in die Schichtdicke umgerechnet und der Verlauf F(T)(d) in Abhängigkeit von d geplottet. Aus dem markanten Peak kann dann auf der x Achse die Dicke Abgelesen werden. Die Methode mit Fourier ist nur optional und soll deshalb nicht zu ausführlich beschrieben werden! Versuche dich also hier kürzer zu halten. 

Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil als Latex code aus.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Verwende die bestehende Analyse der alten Berichte und verfasse das neue Kapitel basierend auf dieser.  
Betrachte ebenfalls den bestehenden Bericht um das neue Kapitel möglicht passend in den BEericht einzufügen. Als nächstes betrachte den vorgegebenen code und die Inhaltlichen Anforderungen und schreibe danach das Kapitel gemäß der neuen Aufgabe.

```python
# Teil 1
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from plot_lib import load_measurement_var
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# -----------------------
# Load all measurements
# -----------------------
folder = "02_Spektralphotometer/data/Messung05"
data = {n: load_measurement_var(n, folder, 'glas') for n in range(1, 6)}


lam, I0 = data[1]["Referenz"]
_, IT = data[1]['Blau']

T = IT / I0

T_all = np.array(T)
mask = np.logical_and(lam >= 700, lam <= 720)
lam_slice = lam[mask]
T_slice = T_all[mask]

peaks, props = find_peaks(T_slice, distance=5)
peak_nu = 1/lam_slice[peaks] * 1e3 #mu m

index = np.array(range(len(peak_nu)))

def ffit(m, k, d):
    return k*m + d
popt, pcov = curve_fit(ffit, index, peak_nu)
m_fine = np.linspace(0, max(index), 1000)
nu_fine = ffit(m_fine, *popt)

k, _ = popt
dk = np.sqrt(np.diag(pcov))[0]
n_p = 1.519

d = 1/abs(2*n_p*k)
dd = abs(d*dk/k)
print(f"Steigung alpha = {k*1000} pm {dk*1000} mm^-1")
print(f"Dicke d = {d} pm {dd} mu m")

# Plot
# ------------------------------------------------------------------
fig1, ax1 = plt.subplots(1,1, figsize=(6, 4))

ax1.plot(lam_slice, T_slice, color='tab:orange', linewidth=1.1, label='Signal')
ax1.scatter(lam_slice[peaks], T_slice[peaks], marker='d', color='blue', label='detektierte Peaks')
ax1.set_xlabel(r"Wellenlänge $\lambda$ / nm", fontsize=16)
ax1.set_ylabel(r"Transmission $T$ / 1", fontsize=16)
ax1.legend(frameon=True, fontsize=16, ncols=2, loc='lower center')
ax1.set_ylim(0.89, 0.945)
ax1.grid(True)
plt.tight_layout()

fig2, ax2 = plt.subplots(1,1, figsize=(6, 4))
ax2.plot(index, peak_nu, 'bd', label="detektierte Peaks")
ax2.plot(m_fine, nu_fine, color='crimson', label="Ausgleichsgerade")
ax2.set_ylabel(r"Wellenzahl $\nu_m$ / $\mu\text{m}^{-1}$", fontsize=16)
ax2.set_xlabel(r"Index $m$ / 1", fontsize=16)
ax2.legend(frameon=True, fontsize=16)
ax2.grid(True)

plt.tight_layout()
plt.show()
```
```python
# Teil 2
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

# Interpolate
# ------------------------------------------------------------
n_points = len(nu)
nu_lin = np.linspace(nu.min(), nu.max(), n_points)
interp_func = interp1d(nu[::-1], T_slice[::-1], kind='linear')
T_interp = interp_func(nu_lin)

# FFT
# ------------------------------------------------------------
T_centered = T_interp - np.mean(T_interp)
FT = np.fft.fft(T_centered)

length = np.fft.fftfreq(len(nu_lin), d=(nu_lin[1]-nu_lin[0]))  
ampl = np.abs(FT) / n_points

pos = length > 0
ampl_pos = ampl[pos]
length_um = length[pos] / (2 * n_p)  * 1e6

# Plot
# ------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(length_um, ampl_pos*1000, color='blue', lw=1.2)
ax2.set_xlabel(r"Schichtdicke d / µm", fontsize=16)
ax2.set_ylabel(r"Amplitude $|F(T(\nu))|$ / a.u.", fontsize=16)
ax2.grid(True)
plt.tight_layout()
plt.show()
```

