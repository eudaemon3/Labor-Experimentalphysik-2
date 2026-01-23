import numpy as np
import matplotlib.pyplot as plt
import os
from lib import analyze_interference_image, slit_measure_to_mm, clac_contrast
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# ROI: (x, y, width, height)
ROI = (50, 450, 950, 90)

folder_path = "03_Interferometer/data/"
slit_width_measure = [(3,5), (4,0), (3,10), (2,20), (1,30), (0,40)]
delta_width = 0.05 #mm

d = 0.23 #mm
lam = 0.000633 #mm
f1 = 300 #mm

if __name__ == "__main__":

    image_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])
    if not image_files:
        raise RuntimeError("Keine Bilddateien im angegebenen Ordner gefunden.")

    curve_case = [0, 2, 2, 1, 1, 1]
    width = [slit_measure_to_mm(i) for i in slit_width_measure]

    image_files = np.array(image_files)
    curve_case = np.array(curve_case)
    width = np.array(width)
    print(width, delta_width)
    # [1.535 1.985 1.585 1.185 0.785 0.385] 0.01 #mm

    sort_idx = np.argsort(width)[::-1]

    image_files = image_files[sort_idx]
    curve_case = curve_case[sort_idx]
    width = width[sort_idx]

    fig, axes = plt.subplots(3, 2, figsize=(10, 8), sharex=False, sharey=False)
    axes = axes.flatten()

    intensity_handle = None
    min_handle = None
    max_handle = None
    K,dK = [],[]

    for i, filename in enumerate(image_files):
        ax = axes[i]
        image_path = os.path.join(folder_path, filename)
        print(image_path)
        x_pixels, intensity = analyze_interference_image(
            image_path=image_path,
            roi_params=ROI
        )

        if curve_case[i] in [1,2]:
            min_ind, max_ind, contrast, delta_contrast = clac_contrast(x_pixels, intensity)

            min_handle = ax.scatter(
                x_pixels[min_ind],
                intensity[min_ind],
                color="crimson",
                marker='d',
                label='detected Minima'
            )

            max_handle = ax.scatter(
                x_pixels[max_ind],
                intensity[max_ind],
                color="rebeccapurple",
                marker='o',
                label='detected Maxima'
            )
            K.append(contrast)
            dK.append(delta_contrast)
        else:
            K.append(0)
            dK.append(0)

        intensity_handle, = ax.plot(
            x_pixels,
            intensity,
            'b-',
            label='Intensity profile'
        )
        
        ax.set_title(rf"Breite $b = ({width[i]:.2f} \pm {delta_width:.2f})\,\mathrm{{mm}}$", fontsize=16)

        if i in [4,5]:
            ax.set_xlabel(r"Pixel $p$ / 1", fontsize=16)
        if i in [0, 2, 4]:
            ax.set_ylabel(r"Intensität $\frac{I}{I_\text{max}}$ / 1",fontsize=16)
        ax.grid(True)
        ax.set_ylim(-0.1, 1.1)
    # Gemeinsame Legende unterhalb der Plots
    fig.legend(
        handles=[intensity_handle, min_handle, max_handle],
        labels=['Intensitäts Profil', 'detektierte Minima', 'detektierte Maxima'],
        loc='lower center',
        ncol=3,
        frameon=True,
        fontsize=16
    )

    plt.tight_layout(rect=[0, 0.06, 1, 1]) # type: ignore

    K_theo = lambda w: np.abs(
        np.sin(2*np.pi*d*w/(lam*f1)) /
        (2*np.pi*d*w/(lam*f1))
    )

    w_plot = np.linspace(0.001, max(width), 1000)
    fig2, ax = plt.subplots(figsize=(6,4))

    ax.plot(
        w_plot,
        K_theo(w_plot/4),
        color="crimson",
        label=r"Theorie $K(w)$"
    )
    print(K, dK[3:])
    # Output: 
    # K:[np.float64(0.11847190975820222), np.float64(0.07160006519909957), 0, np.float64(0.27340953159994186), np.float64(0.6821441948864503), np.float64(0.8918463935261413)] 
    # dK: [np.float64(0.002871359042297514), np.float64(0.006991521736039729), np.float64(0.008112170358122337), -, -, -]
    ax.errorbar(width[:3] + 0.1, K[:3], xerr=delta_width, marker='d', linestyle='none', color="rebeccapurple",capsize=5, label=r'indirekte Auswertung')
    ax.errorbar(width[3:] +0.1, K[3:], yerr=dK[3:], xerr=delta_width, color='blue', marker='d', linestyle='none', capsize=5, label=r"direkte Auswertung")
    ax.set_xlabel(r"Breite $w$ / mm", fontsize=16)
    ax.set_ylabel(r"Kontrast $K$ / 1", fontsize=16)
    ax.grid(True)
    ax.legend(fontsize=16, frameon=True)
    ax.set_xlim(-0.1, 2.4)

    plt.tight_layout()
    plt.show()


