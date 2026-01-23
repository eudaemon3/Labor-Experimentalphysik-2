import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.signal import find_peaks

def slit_measure_to_mm(measure:tuple, zero=0.15):
    turns, ticks = measure
    return turns*0.5 + ticks*0.01 - zero

def analyze_interference_image(image_path: str, roi_params: tuple, show_img: bool=False):
    roi_x, roi_y, roi_width, roi_height = roi_params

    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img_gray is None:
        raise FileNotFoundError(f"Bild nicht gefunden: {image_path}")

    img_rgb = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
    roi = img_gray[
        roi_y : roi_y + roi_height,
        roi_x : roi_x + roi_width
    ]

    intensity = np.mean(roi, axis=0)
    intensity /= np.max(intensity)

    x_pixels = np.arange(len(intensity))

    if show_img:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.imshow(img_rgb, cmap="gray")
        ax.add_patch(
            Rectangle(
                (roi_x, roi_y),
                roi_width,
                roi_height,
                edgecolor="red",
                facecolor="none",
                linewidth=0.9,
                linestyle='--'
            )
        )
        ax.axis("off")
        plt.show()

    return x_pixels, intensity

def clac_contrast(x_pixels, intensity, window=5):
    max_ind = np.argmax(intensity)
    I_max = np.mean(intensity[max_ind - window : max_ind + window + 1])
    sigma_I_max = np.std(intensity[max_ind - window : max_ind + window + 1])

    peaks, _ = find_peaks(-intensity, distance=50, prominence=0.07)
    min_ind = [i for i in peaks if i >= 350 and i <= 600]

    if len(min_ind) <= 0: 
        return 0,0,0,0

    I_min_left = np.mean(intensity[min_ind[0] - window : min_ind[0] + window + 1])
    sigma_I_min_left = np.std(intensity[min_ind[0] - window : min_ind[0] + window + 1])

    if len(min_ind) > 1:
        I_min_right = np.mean(intensity[min_ind[1] - window : min_ind[1] + window + 1])
        sigma_I_min_right = np.std(intensity[min_ind[1] - window : min_ind[1] + window + 1])
        I_min = (I_min_left + I_min_right)/2
        sigma_I_min = (sigma_I_min_left + sigma_I_min_right)/2

    else:
        I_min = I_min_left
        sigma_I_min = sigma_I_min_left
    
    contrast = (I_max - I_min)/(I_max + I_min)
    contrast_uncert =  np.sqrt((2 * I_min / (I_max + I_min)**2 * sigma_I_max)**2 + (2 * I_max / (I_max + I_min)**2 * sigma_I_min)**2)
            
    return min_ind, max_ind, contrast, contrast_uncert