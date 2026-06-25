import numpy as np

T_half = 5730 #years
dt = 10 #years
steps = T_half / dt # How many steps to achieve half of n0
p = 1 - ((0.5)**(1/steps))

def simulate(balls):
    for nucleus in balls:
        r = np.random.rand()
        if r < p:
            nucleus[2] = False