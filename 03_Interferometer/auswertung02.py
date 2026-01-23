import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import cv2
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

folder_path = "03_Interferometer/data/Versuch02/"
ROI = (50, 425, 950, 130)

titles = ["Bandpass", "Langpass", "Ohne Filter"]

image_files = sorted([
    f for f in os.listdir(folder_path)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

fig, axes = plt.subplots(3, 2, figsize=(9, 6.5),
                         gridspec_kw={"width_ratios": [1, 1.2]})

for i, filename in enumerate(image_files):
    ax_img, ax_plot = axes[i]
    img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)

    # ROI & Profil
    x, y, w, h = ROI
    roi = img[y:y+h, x:x+w]
    intensity = np.mean(roi, axis=0)
    intensity /= intensity.max()
    pixels = np.arange(len(intensity))

    # --- Bild links ---
    ax_img.imshow(img, cmap="gray", aspect="auto")
    ax_img.add_patch(Rectangle((x, y), w, h,
                               edgecolor="red", facecolor="none", 
                               linewidth=0.9, linestyle='--'))
    ax_img.set_title(titles[i], fontsize=15)
    ax_img.axis("off")

    # --- Profil rechts ---
    ax_plot.plot(pixels, intensity, 'b-')
    ax_plot.set_ylim(-0.1, 1.1)
    ax_plot.grid(True)

    if i == 2:
        ax_plot.set_xlabel(r"Pixel $p$ / 1", fontsize=15)
    ax_plot.set_ylabel(r"$I / I_{\max}$ / 1", fontsize=15)

plt.tight_layout()
plt.show()