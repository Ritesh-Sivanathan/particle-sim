'''

5/17/2025

Varying and testing different parameter sizes for a Particle.

'''


from ...particle import Particle
import random
import matplotlib.pyplot as plt

myParticle = Particle() # Instantiate a basic particle

data = [[], []]
counter = 0
myParticle.change_velocity(1,1,1)

while counter < 25000:

    V_Lower = -0.85
    V_Upper = 0.95

    DT_Lower = 1.2
    DT_Upper = 2.2
    
    print(myParticle.update_particle_position())
    myParticle.change_velocity(myParticle.velocity.real*(random.uniform(V_Lower,V_Upper)), myParticle.velocity.imag*(random.uniform(V_Lower,V_Upper)), myParticle.delta_time*(round(random.uniform(DT_Lower, DT_Upper), 3)))

    data[0].append(myParticle.position.real)
    data[1].append(myParticle.position.imag)

    counter += 1

fig, ax = plt.subplots()
ax.plot(data[0], data[1])
plt.show()