'''

More realistic random movement.

'''

from ..particle import Particle
import matplotlib.pyplot as plt
import numpy as np
import random

p = Particle()
data = [[], []]

x,y = 0,0
vx, vy = 0,0

for _ in range(500):
    
    vx = np.random.normal(0, 0.5)
    vy = np.random.normal(0, 0.5)
    
    p.change_velocity(vx, vy, np.random.uniform(0.01, 0.03))

    px, py = p.update_particle_position()

    data[0].append(px)
    data[1].append(py)

fig, ax = plt.subplots()
ax.plot(data[0], data[1])
plt.show()