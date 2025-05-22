from ..particle import Particle

import matplotlib.pyplot as plt
import numpy as np

data = [[], []] # x, y
p1 = Particle()

for i in range(500):

    if i == 0:
        p1.change_velocity(1,1,1)

    if p1.position.real >= 10:
        p1.change_velocity(-1, -0.5, 1)
        print(f"collision x:{p1.position.real} y:{p1.position.imag}")
    elif p1.position.real <= 0 and i!=1:
        p1.change_velocity(1, 0.5, 1)
        print(f"collision x:{p1.position.real} y:{p1.position.imag}")

    p1.update_particle_position()

    data[0].append(p1.position.real)
    data[1].append(p1.position.imag)

fig, ax = plt.subplots()
plt.plot(data[1], data[0])
plt.show()