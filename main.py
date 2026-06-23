import matplotlib.pyplot as plt
import numpy as np

def euler_decay(l, n0, h, size):
    N = [n0]
    for _ in range(1, size):
        N.append(N[-1] + h*(-l*N[-1]))
    return np.array(N)


n0 = 50000
T_half = 5730 # anos]
uranium = 4e9
l = np.log(2)/T_half
h = 10
t = np.arange(0, 100000, h)
N_analytic = n0*np.exp(-l*t)
N_numeric = euler_decay(l, n0, h, len(t))

plt.plot(t, N_analytic, label="Analytic solution", color='#000000')
plt.plot(t, N_numeric, label="Numeric solution", linestyle='--')

plt.xlim(0,50000)
plt.ylim(0, 50000)
plt.legend()
plt.show()