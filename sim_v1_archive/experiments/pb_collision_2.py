'''

2nd iteration of particle-bound collision

'''

from ..particle import Particle
import matplotlib.pyplot as plt
import numpy as np

x, y = [], []
p1 = Particle()

for i in range(500):
    
    p1.change_velocity(1,1,1)
    p1.update_particle_position()

    x.append(p1.position.real)
    y.append(p1.position.imag)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()