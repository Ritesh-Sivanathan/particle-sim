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
        # print(f"collision x:{p1.position.real} y:{p1.position.imag}")

    if p1.position.imag >= 10:
        random_y = np.random.random()
        p1.change_velocity(1, -random_y, 1)

    if p1.position.imag <= 0:
        random_y = np.random.random()
        p1.change_velocity(1, random_y, 1)

    elif p1.position.real <= 0 and i!=0:
        random_y = np.random.random()
        p1.change_velocity(1, random_y, 1)
        # print(f"collision x:{p1.position.real} y:{p1.position.imag}")

    if p1.position.real > 10:
        print(p1.position.real)

    p1.update_particle_position()

    data[0].append(p1.position.real)
    data[1].append(p1.position.imag)

fig, ax = plt.subplots()

plt.axvline(x=0)
plt.axvline(x=10)
plt.axhline(y=0)
plt.axhline(y=10)

plt.plot(data[0], data[1])
plt.show()