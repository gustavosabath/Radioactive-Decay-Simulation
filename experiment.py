import numpy as np
import subprocess
isotopes = {
    "Carbono-14": 5730, 
    "Iodo-131": 8/365,       
    "Uranio-238": 4.47e9
}
T_half = isotopes["Carbono-14"]
n0 = 1000
dt = 10 #years
steps = T_half / dt # How many steps to achieve half of n0
p = 1 - ((0.5)**(1/steps))

t_metade = None
t_counter = 0
N = [n0]
t = [t_counter]
half_reached = False
while n0 > 0:
    t_counter += dt
    meias_vidas = t_counter / T_half

    print(
    f"Tempo: {t_counter:.0f} anos | "
    f"Meias-vidas: {meias_vidas:.2f}"
    )
    decayed = 0
    for _ in range(n0):
        r = np.random.rand()
        if r < p:
            decayed += 1
    n0 -= decayed
    if not half_reached and n0 <= 500:
        t_metade = t_counter
        print(
        f"Metade atingida em {t_counter} anos"
        )
        half_reached = True
    N.append(n0)
    t.append(t_counter)
    print(f"Time counter: {t_counter}")
erro = abs(t_metade - T_half)

print(
    f"Erro da simulacao: {erro:.2f} anos"
)
payload = zip(t, N)
payload = [f"{x[0]}#{x[1]}" for x in payload]
payload = ";".join(payload)
lenWritten = 0
with open("experiment.dat", 'w') as f:
    lenWritten = f.write(payload)
if lenWritten > 0 :
    subprocess.Popen(['python', 'main.py'])
