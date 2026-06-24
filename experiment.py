import numpy as np
import subprocess

n0 = 1000
T_half = 5730 #years
dt = 10 #years
steps = T_half / dt # How many steps to achieve half of n0
p = 1 - ((0.5)**(1/steps))

t_counter = 0
N = [n0]
t = [t_counter]

while n0 > 0:
    t_counter += dt
    decayed = 0
    for _ in range(n0):
        r = np.random.rand()
        if r < p:
            decayed += 1
    n0 -= decayed
    N.append(n0)
    t.append(t_counter)
    print(f"Time counter: {t_counter}")
    
payload = zip(t, N)
payload = [f"{x[0]}#{x[1]}" for x in payload]
payload = ";".join(payload)
lenWritten = 0
with open("experiment.dat", 'w') as f:
    lenWritten = f.write(payload)
if lenWritten > 0 :
    subprocess.Popen(['python', 'main.py'])