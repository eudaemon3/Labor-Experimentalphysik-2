import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

theta = 329 - np.array([300,290,280,270,260,250,240,230,220,210,200,190,180,120,110,100,90,80,70,60,50,40,30,20,10,0]) 
theta = np.deg2rad(theta)[:7]
Voltages = np.array([221,121,21,6.7,77.6,146.5,191.9,205,186,146,116,140,198,212,107,14.9,4.5,61.5,140,188,196,176,134,106,147,206])[:7]

def ffit(theta, A, phi):
    return A*np.cos(theta + phi)**2

popt, pcov = curve_fit(ffit, theta, Voltages)

theta_fine = np.linspace(np.min(theta),np.max(theta),1000)

plt.plot(theta_fine, ffit(theta_fine, *popt))
plt.errorbar(theta, Voltages, yerr=Voltages*0.02, fmt='bd', capsize=5)
plt.show()

