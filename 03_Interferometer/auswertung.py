import numpy as np
import matplotlib.pyplot as plt
import os
from lib import analyze_interference_image, slit_measure_to_mm
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

# ROI: (x, y, width, height)
ROI = (50, 450, 950, 90)

folder_path = "03_Interferometer/data/"
slit_width_measure = [(3,5), (4,0), (3,10), (2,20), (1,30), (0,40)]
delta_width = 0.01 #mm


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

    sort_idx = np.argsort(width)[::-1]

    image_files = image_files[sort_idx]
    curve_case = curve_case[sort_idx]
    width = width[sort_idx]

    

    fig, axes = plt.subplots(3, 2, figsize=(10, 8), sharex=False, sharey=False)
    axes = axes.flatten()

    intensity_handle = None
    min_handle = None
    max_handle = None

    for i, filename in enumerate(image_files):
        ax = axes[i]
        image_path = os.path.join(folder_path, filename)

        data = analyze_interference_image(
            image_path=image_path,
            roi_params=ROI,
            curve_case=curve_case[i],
            _show_img=False
        )

        if curve_case[i] == 1:
            x_pixels, intensity, min_ind, max_ind, contrast = data  # type: ignore

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
        else:
            x_pixels, intensity, contrast = data  # type: ignore

        intensity_handle, = ax.plot(
            x_pixels,
            intensity,
            'b-',
            label='Intensity profile'
        )

        """
        ax.text(
            0.85,
            0.85,
            rf"$K \approx {contrast:.2f}$",
            transform=ax.transAxes,
            ha="center",
            va="top",
            fontsize=16
        )
        """
        
        ax.set_title(rf"Breite $b = ({width[i]:.3f} \pm {delta_width:.3f})\,\mathrm{{mm}}$", fontsize=16)

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
    plt.show()