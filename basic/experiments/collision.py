from ..particle import Particle
import matplotlib.pyplot as plt
import numpy as np
import math

p1 = Particle()
data = [[], []]

for i in range(50):
    
    '''
    
    Horizontal Bounds:
        x=0, x=10, therefore the particle must have an x position 0 <= posx <= 10
    Vertical Bounds:
        y=0, y=10, therefore the particle must have a y position 0 <= posy <= 10

    '''


    # IGNORE THIS MESSY MESS. IT WILL BE FIXED. JUST TRYING TO MAP EVERYTHING OUT AS PLAINLY AS POSSIBLE!

    curr  = p1.update_particle_position()
    next = p1.sim_particle_position()

    print(f"Current: {curr}, Next: {next}")

    if i == 0:
        p1.change_velocity(1,1,1)

    if next.real >= 10:
        
        vx = 10 - curr.real # distance from bound x=10

        p1.change_velocity(vx, 1, 1) # keep it on the collision course controlled. dt=1 always just for simplicity's sake
        p1.update_particle_position() # collision

        data[0].append(p1.position.real)
        data[1].append(p1.position.imag)

        
        speed = math.hypot(p1.velocity.real, p1.velocity.imag) # get speed from slope
        angle = math.atan2(p1.velocity.real, p1.velocity.imag) # find the angle between the x and y using tan\theta=y/x

        angle = math.pi - angle + np.random.uniform(-0.2,0.2) # reflect velocity vector horizontally. +-.2 rad to avoid linearty

        vy = np.random.choice([-1, 1]) # random y sign. either deflects up or down

        p1.change_velocity(math.cos(angle)*speed, math.sin(angle)*speed, 1)
        p1.update_particle_position() # after collision/new slope

        data[0].append(p1.position.real)
        data[1].append(p1.position.imag)

    if next.real < 0 and i!=0:
        
        vx = curr.real # distance from bound x=0

        p1.change_velocity(vx, 1, 1) # keep it on the collision course controlled. dt=1 always just for simplicity's sake
        p1.update_particle_position() # collision

        data[0].append(p1.position.real)
        data[1].append(p1.position.imag)

        factor = np.random.uniform(0.75,1.2) # random mod to change the slope
        vy = np.random.choice([-1, 1]) # random y sign. either deflects up or down

        p1.change_velocity(-1*p1.velocity.real*factor, vy, 1)
        p1.update_particle_position() # after collision/new slope

        data[0].append(p1.position.real)
        data[1].append(p1.position.imag)

    data[0].append(p1.position.real)
    data[1].append(p1.position.imag)

fig, ax = plt.subplots()
plt.plot(data[0], data[1])
plt.show()