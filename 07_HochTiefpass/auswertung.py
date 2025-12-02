import numpy as np

R1 = 2700   #O
C = 100e-9 #F
L = 10e-3  #H

f_G = 1/(2*np.pi*R1*C)
print(f_G/5)

s = np.array([1, 1.26, 1.59, 2.52, 4.0, 6.34, 7.98, 10])
print(f_G*s)

f_0 = 1/(2*np.pi*np.sqrt(L*C))

f_0mess = 4897
print(f_0mess*s)
print(f_0/50)

R2B = 47 #Ohm
fC = 1/(2*np.pi) * 1/np.sqrt(L*C) * (1- R2B**2 * C / (2*L))
print(fC)


