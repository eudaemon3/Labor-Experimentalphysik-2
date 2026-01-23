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
slit_width = np.array(list(map(slit_measure_to_mm, slit_width))) 
delta_width = 0.1 #mm

d_dist = np.array([0.13, 0.23, 0.43]) #mm
lam = 0.000633 #mm
f1 = 300 #mm

image_files = sorted([
    f for f in os.listdir(folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

fig, axes = plt.subplots(1, 3, figsize=(10, 3))

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
    ax_img.set_title(rf"$d = {d_dist[i]:.2f}\,\mathrm{{mm}}$", fontsize=16)
    ax_img.axis("off")

plt.tight_layout()
plt.show()

w_theo = lambda d : f1*lam/d
d_plot = np.linspace(0.1, 0.8, 1000)
print(slit_width)
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