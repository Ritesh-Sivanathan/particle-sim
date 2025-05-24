
'''

Initial Prototyping for first real iteration of the particle and system.
Next prototype in coll.py
No further changes will be made to this iteration as of 5/23/2025

'''


from particle import Particle
import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 500

XMAX, YMAX = 10, 10
XMIN, YMIN = 0, 0

p1 = Particle()

pts = [[], []]
sim_pts = [[], []]
intervals = np.random.randint(low=1,high=ITERATIONS,size=np.random.randint(ITERATIONS*0.6)) # 60% of the particle's movement will be random

for i in range(ITERATIONS):

    if i == 0:
        p1.update_velocity(np.random.uniform(0.5,2),np.random.uniform(0.5,2))

    spx, spy = p1.simulate_particle_position()

    if np.int32(i) in intervals:
        p1.velocity += np.random.normal(scale=0.5, size=2)

    match spx:

        case _ if spx >= XMAX:
            t = (XMAX - p1.position[0]) / p1.velocity[0] # Timestep that the collision between the particle and the XMAX bound happened
            y_c = p1.position[1]+p1.velocity[1]*t # y-coordinate that the collision occurred
            y_factor = np.random.choice([np.random.uniform(.45,1.1), np.random.uniform(-.45,-1.1)])
            angle_mod = (np.random.uniform(0.05,0.95))*np.random.choice([-1, 1])
            p1.update_velocity(-p1.velocity[0],angle_mod*(p1.velocity[1]+y_factor))

        case _ if spx <= XMIN:
            
            t = (p1.position[0]-XMIN) / p1.velocity[0] # Timestep that the collision between particle and XMIN happened
            y_c = p1.position[1]+p1.velocity[1]*t
            y_factor = np.random.choice([np.random.uniform(.45,1.1), np.random.uniform(-.45,-1.1)])
            angle_mod = (np.random.uniform(0.05,0.95))*np.random.choice([-1, 1])
            p1.update_velocity(abs(p1.velocity[0]),angle_mod*(p1.velocity[1]+y_factor))

    # match spy:
        
    #     case _ if spy > YMAX:
            
    #         t = (YMAX - p1.position[1])/(p1.velocity[1])
    #         x_c = p1.position[0] + p1.velocity[0]*t
    #         x_factor = np.random.choice([np.random.uniform(.45,1.1), np.random.uniform(-.45,-1.1)])
    #         p1.update_velocity(1*x_factor,-1)

    #     case _ if spy == YMIN:

    #         t = (p1.position[1]-YMIN)/(p1.velocity[1])
    #         x_c = p1.position[0] + p1.velocity[0]*t
    #         x_factor = np.random.choice([np.random.uniform(.45,1.1), np.random.uniform(-.45,-1.1)])
    #         p1.update_velocity(1*x_factor,1)

    x,y = p1.update_particle_position()
    pts[0].append(x)
    pts[1].append(y)

fig, ax = plt.subplots()
plt.plot(pts[0], pts[1])
plt.show()