import numpy as np
import matplotlib.pyplot as plt

s = 1.0
ms = 0.001 * s

V = 1.0
mV = 0.001 * V

Ohm = 1.0
MOhm = 1000000 * Ohm

A = 1.0
nA = 0.000000001

tau_m = 10*ms
E_l = -70*mV
V_th = -40*mV
R_m = 10 * MOhm
I_e = 3.1*nA
delta_t = 0.25*ms

V = -70*mV

vs = []
ts = []

for i in np.arange(0, 1*s, 0.25*ms):
    V = V + delta_t * (E_l-V+R_m*I_e)/tau_m
    if V >= V_th:
        # spike
        V = E_l
    vs.append(V)
    ts.append(i)


print(vs)
plt.plot(ts, vs)
plt.show()
