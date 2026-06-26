import numpy as np

T_half = 5730 #years

def simulate(balls, frametime, dt):
    steps = T_half / (dt*frametime) # How many steps to achieve half of n0
    p = 1 - ((0.5)**(1/steps))
    for nucleus in balls:
        r = np.random.rand()
        if r < p:
            nucleus[2] = False