import numpy as np
import os

def load_measurement(n: int, filepath: str):
    files = {
        "Blau": f"Blau0{n}.csv",
        "Rot": f"Rot0{n}.csv",
        "RotBlau": f"RotBlau0{n}.csv",
        "Referenz": f"Referenz0{n}.csv"
    }

    data = {}
    for name, fname in files.items():
        path = os.path.join(filepath, fname)
        csv = np.genfromtxt(path, delimiter=",")
        data[name] = (csv[:, 0], csv[:, 1])

    return data

def load_measurement_var(n: int, filepath: str, measure_type: str):
    if measure_type == 'methyl':
        files = {
            "Blau": f"Blau0{n}.csv",
            "Referenz": f"ReferenzWasser0{n}.csv"
        }
    elif measure_type == 'glas':
        files = {
            "Blau": f"Glas1{n}.csv",
            "Referenz": f"Referenz1{n}.csv"
        }
    else:
        raise ValueError

    data = {}
    for name, fname in files.items():
        path = os.path.join(filepath, fname)
        csv = np.genfromtxt(path, delimiter=",")
        data[name] = (csv[:, 0], csv[:, 1])

    return data

def plot_visible_spectrum(ax, x_min, x_max,
                          y_min=-0.05, y_max=0.0,
                          n_lambda=2000,
                          show_edge=True,
                          alpha_def=1.0):
    """
    Draws a smooth visible spectrum in the range y_min..y_max.

    - Visible range (380-780 nm): smooth color gradient, alpha = 1
    - UV edge: constant violet color with fading alpha
    - IR edge: constant red color with fading alpha
    """

    lambdas = np.linspace(x_min, x_max, n_lambda)

    # -----------------------
    # Wavelength → RGB mapping
    # -----------------------
    def wavelength_to_rgb(l):
        if l < 380:
            return (0.5, 0.0, 1.0)   # violet edge color
        if l > 780:
            return (1.0, 0.0, 0.0)   # red edge color
        if l < 440:
            return (-(l - 440) / 120, 0, 1)
        if l < 490:
            return (0, (l - 440) / 50, 1)
        if l < 510:
            return (0, 1, -(l - 510) / 20)
        if l < 580:
            return ((l - 510) / 70, 1, 0)
        if l < 645:
            return (1, -(l - 645) / 65, 0)
        return (1, 0, 0)

    rgb = np.array([wavelength_to_rgb(l) for l in lambdas])

    # -----------------------
    # Alpha channel
    # -----------------------
    alpha = np.zeros_like(lambdas)

    visible = (lambdas >= 380) & (lambdas <= 780)
    alpha[visible] = alpha_def

    if show_edge:
        # UV fade
        uv_min = 330
        uv = (lambdas >= uv_min) & (lambdas < 380)
        alpha[uv] = (lambdas[uv] - uv_min) / (380 - uv_min)

        # IR fade
        ir_max = 840
        ir = (lambdas > 780) & (lambdas <= ir_max)
        alpha[ir] = (ir_max - lambdas[ir]) / (ir_max - 780)


    rgba = np.zeros((1, n_lambda, 4))
    rgba[0, :, :3] = rgb
    rgba[0, :, 3] = alpha

    ax.imshow(
        rgba,
        extent=[x_min, x_max, y_min, y_max],
        aspect="auto",
        interpolation="bicubic",
        zorder=0
    )