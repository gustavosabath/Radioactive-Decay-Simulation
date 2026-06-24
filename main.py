import matplotlib.pyplot as plt
import numpy as np

def euler_decay(l, n0, h, size):
    N = [n0]
    for _ in range(1, size):
        N.append(N[-1] + h*(-l*N[-1]))
    return np.array(N)

def get_dt_near0(t, n0, l):
    for dt in t:
        N = n0*np.exp(-l*dt)
        print(N)
        if N == 0:
            return dt
    raise Exception("dt not found")

n0 = 1000
T_half = 5730 # anos
l = np.log(2)/T_half
h = 10
t = np.arange(0, 100000, h)
N_analytic = n0*np.exp(-l*t)
N_numeric = euler_decay(l, n0, h, len(t))

N_sim = []
t_sim = []
with open('experiment.dat', 'r') as f:
    payload = f.read().strip().split(';')
    payload = [[int(x) for x in line.split('#')] for line in payload]
    t_sim = [x[0] for x in payload]
    N_sim = [x[1] for x in payload]

plt.plot(t, N_analytic, label="Analytic solution", color='#000000')
plt.plot(t, N_numeric, label="Numeric solution", linestyle='--')
plt.plot(t_sim, N_sim, label="Simulation")

plt.xlim(0, t[-1])
plt.ylim(0, n0)
plt.legend()
plt.show()