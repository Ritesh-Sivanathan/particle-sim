'''

5/17/2025

Simulating more realistic random movement.

'''

from ..particle import Particle
import matplotlib.pyplot as plt
import random

p = Particle()
counter = 0
data = [[], []]

while counter < 1000:
    
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)

    px, py = p.update_particle_position()
    
    if px <= 0 and vx <= 0:
        vx *= -1
    if py <= 0 and vy <= 0:
        vy *= -1

    p.change_velocity(vx,vy,random.uniform(1,5))

    data[0].append(px)
    data[1].append(py)

    counter += 1

fig, ax = plt.subplots()
ax.plot(data[0], data[1])
plt.show()