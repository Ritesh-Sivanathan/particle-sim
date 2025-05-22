from ..particle import Particle
from ..system import System
import matplotlib.pyplot as plt
import numpy as np
import math

p1 = Particle()
p2 = Particle()

data0 = [[], []]
data1 = [[], []]

# Sinusoidal Movement

x = np.arange(0, 5*np.pi, 0.1)

for i in x:

    p1.change_velocity(np.sin(i),1,1)
    p2.change_velocity(np.cos(i),1,1)

    data0[0].append(p1.position.real)
    data0[1].append(p1.position.imag)

    data1[0].append(p2.position.real)
    data1[1].append(p2.position.imag)

    # real-time collision
    # if p1.position.real == p2.position.real and p1.position.imag == p2.position.imag:
    #     print(p1.position.real, p1.position.imag)

    # path collision
    if p1.position.real in data1[0] or p2.position.real in data0[0] or p1.position.imag in data1[1] or p2.position.imag in data0[1]:
        print("col")

    p1.update_particle_position()
    p2.update_particle_position()

plt.plot(data0[1], data0[0], label="Particle 1", color='blue', marker='o')
plt.plot(data1[1], data1[0], label="Particle 2", color='red', marker='x')
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Positions of Particle X vs Y")
plt.legend()

plt.grid(True)
plt.show()