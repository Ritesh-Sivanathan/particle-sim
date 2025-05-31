from particle import Particle
from system import System
import numpy as np
import matplotlib.pyplot as plt

vix = np.random.randint(1,25)
viy = np.random.randint(1,25)

particle = Particle(vx=vix, vy=viy, max_x=10500, max_y=10500)
system = System(particles=[particle],)

data = system.simulate()
print(data[0][0])

# data = particle.loop(50000)

# fig, ax = plt.subplots()
# plt.plot(data[0], data[1])
# plt.title(f"vix={vix} viy={viy}")
# plt.show()