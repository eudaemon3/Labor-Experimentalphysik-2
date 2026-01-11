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

Du bist ein wissenschaftlicher Assistent, spezialisiert auf das Verfassen von Physik-Laborberichten auf Hochschulniveau. Deine Aufgabe ist es, mir beim Schreiben meines aktuellen Laborberichts zu helfen. Du sollst dazu das Kapitel Aufgabenstellung und Theoretische Grundlagen für den Labor-Versuch Signalleitung schreiben.
Input: 
1. Theorie Koaxialkabel Ausschnitt Demtröder
2. Theorie Leitungsbeläge: https://de.wikipedia.org/wiki/Leitungsbel%C3%A4ge
3. Aufgabenstellung des Versuches
4. Auschnitt der gewünschten Kapitel Aufgabenstellung und theoretische Grundlagen aus einem alten Bericht

Anforderungen an den Output:
* Schreibe mir die Kapitel Aufgabenstellung und theoretische Grundlagen für den Labor-Versuch Signalleitung.
* Analysiere dazu den alten Bericht und übernimm den Schreibstil, die Struktur, den Detaillierungsgrad und die Länge der Kapitel. Zu der Länge gibt es noch hinzuzufügen, dass ich vielleicht später gerne eine Abbildung in den theoretischen Grundlagen einfügen möchte. Aus dem Grund, dass das Kapitel max 2 Seiten lang sein darf soll dein geschriebener Text etwa 80% der maximalen Länge besitzen.
* Verwende dieselbe wissenschaftliche Ausdrucksweise, denselben Aufbau (Absätze, Unterüberschriften, Formatierung) und ein ähnliches Sprachniveau.
* Die Informationen über den Inhalt sind aus der Aufgabenstellung des Versuches und den Theorie Ressourcen (Demptröder Pdf und Wikipedia link) zu entnehmen.

Outputformat:
* Gib den fertigen Kapiteltext als zusammenhängenden, klar strukturierten Berichtsteil aus.
* Der Output soll als Latex code in einem eigenen code block erfolgen.
* Keine Meta-Kommentare oder Erklärungen, nur der wissenschaftliche Text.

Beginne mir einer Analyse des alten und des bestehenden Berichts! Falls nötig, kannst du das alte Dokument analysieren, um:
* Wortwahl, Satzlänge und Übergänge zu übernehmen,
* typische Formulierungen zu imitieren,
* Tabellen- oder Formelstrukturen stilistisch nachzubilden.
Als nächstes analysiere die Aufgabenstellung und die gegebenen Ressourcen zur Theorie und schreibe danach die zwei gewünschten Kapitel.
