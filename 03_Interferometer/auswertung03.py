import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.signal import find_peaks
import scienceplots

plt.style.use('science')
plt.rcParams.update({'font.size': 14})

folder = "03_Interferometer/data/Versuch03/"
images = ["3_Ohne.jpg", "3_Verschoben.jpg"]   # anpassen!
ROI = (50, 440, 950, 100)

lam = 0.633      # µm
n = 1.492        

def extract_profile(path, ROI):
    x, y, w, h = ROI
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    roi = img[y:y+h, x:x+w] # type: ignore
    profile = np.mean(roi, axis=0)
    return profile / profile.max()

profiles = []
for img in images:
    profiles.append(extract_profile(folder + img, ROI))

pixels = np.arange(len(profiles[0]))

peak_pos = []
colors = ["crimson", "tab:orange"]
markers = ['d', 'o']
fig, ax = plt.subplots(figsize=(6,4.5))
for i,prof in enumerate(profiles):
    peaks, _ = find_peaks(prof, prominence=0.07)
    ax.scatter(peaks, prof[peaks], label='detektierte Maxima', color=colors[i], marker=markers[i])
    peak_pos.append((peaks))

ax.plot(pixels, profiles[0], label="ohne Schicht", color='blue', linewidth=1.2)
ax.plot(pixels, profiles[1], label="mit Schicht", color='rebeccapurple', linewidth=1.2)

ax.set_xlabel(r"Pixel $p$ / 1", fontsize=16)
ax.set_ylabel(r"Intensität $\frac{I}{I_{\max}}$ / 1", fontsize=16)
ax.set_xlim(300, 700)
ax.set_ylim(0.02, 1.1)
ax.grid(True)
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.18),
    ncols=2,
    frameon=True,
    fontsize=16
)

plt.tight_layout()
plt.show()

dist_pixel = abs(peak_pos[1][1] - peak_pos[0][1])
delta_pixel = 2

print(f"Verschiebung des Nullten Maximums: Δp = {dist_pixel} Pixel")

N = 4
dist_maxima_pixel = peak_pos[0][N] - peak_pos[0][0]
pixel_to_um = N*lam / dist_maxima_pixel
delta_pixel_to_um = pixel_to_um*delta_pixel/dist_maxima_pixel

delta_s = dist_pixel * pixel_to_um   # optische Weglängendifferenz in µm
uncert_delta_s = delta_s*(delta_pixel/dist_pixel + delta_pixel_to_um/pixel_to_um)
t = delta_s / (n - 1)
dt = uncert_delta_s / (n - 1)

print(fr"Pixel to um $\hat p = {pixel_to_um:.6f} \pm {delta_pixel_to_um:.6f} \frac \mu \textm\text Pixel$")
print(f"Optische Weglängendifferenz Δs = {delta_s:.2f} pm {uncert_delta_s:.3f} µm")
print(f"Schichtdicke t = {t:.2f} pm {dt:.3f} µm")