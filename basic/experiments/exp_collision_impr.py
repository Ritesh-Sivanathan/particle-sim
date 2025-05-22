from ..particle import Particle

import matplotlib.pyplot as plt
import numpy as np

data = [[], []] # x, y
p1 = Particle()

for i in range(500):

    if i == 0:
        p1.change_velocity(1,1,1)

    if p1.position.real >= 10:
        random_y = np.random.random()
        p1.change_velocity(-1, -random_y, 1)

    if p1.position.imag >= 10:
        random_y = np.random.random()
        p1.change_velocity(-1, -random_y, 1)

    if p1.position.imag <= 0 and i != 0:
        random_y = np.random.random()
        p1.change_velocity(1, random_y, 1)

    elif p1.position.real <= 0 and i!=0:
        random_y = np.random.random()
        p1.change_velocity(1, random_y, 1)

    if p1.position.real > 10:
        print(p1.velocity.real, p1.velocity.imag)

    p1.update_particle_position()

    data[0].append(p1.position.real)
    data[1].append(p1.position.imag)

fig, ax = plt.subplots()

plt.axvline(x=0, c="blue")
plt.axvline(x=10, c="blue")
plt.axhline(y=0, c="red")
plt.axhline(y=10, c="red")

plt.savefig()
plt.plot(data[0], data[1])
plt.show()