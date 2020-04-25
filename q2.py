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

# -------------------
delta_t = 0.25*ms

tau_m = 20*ms
E_l = -70*mV
V_rest= -80*mV
V_th= -54*mV
R_mI_e = 18*mV

R_mgs = 0.15
P = 0.5
tau_s = 10*ms
E_s = -1 *mV

# -----------------------
V_a = np.random.randint(54, 80) * -1 * mV
V_b = np.random.randint(54, 80) * -1 * mV

s_a = 0
s_b = 0

v_as = []
v_bs = []
ts = []
for i in np.arange(0, 1*s, 0.25*ms):
    ts.append(i)
    # Decay the voltage of the neurons
    V_a = V_a + delta_t * (E_l - V_a + R_mI_e)/tau_m
    V_b = V_b + delta_t * (E_l - V_b + R_mI_e)/tau_m
    # Check for spikes
    if V_a >= V_th:
        # spike
        V_a = E_l
        s_a = s_a + P

    if V_b >= V_th:
        # spike
        V_b = E_l
        s_b = s_a + P

    # Decay the synapses
    s_a = s_a + delta_t * (-s_a / tau_s)
    s_b = s_b + delta_t * (-s_b / tau_s)

    # Calculate synapse voltages
    s_V_a = R_mgs  * s_a * (E_s - V_a)
    s_V_b = R_mgs  * s_b * (E_s - V_b)

    # Add synapse voltage onto other neuron
    V_b = V_b + s_V_a
    V_a = V_a + s_V_b

    v_as.append(V_a)
    v_bs.append(V_b)

plt.plot(ts, v_as, color="red")
plt.plot(ts, v_bs, color="blue")

plt.show()




#
