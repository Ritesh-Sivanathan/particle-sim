'''

System of particles. Collision logic will be implemented here.

'''

from .particle import Particle

class System:

    def __init__(self, particles):
        self.particles:list[Particle] = []
        self.bounds = [0, 0]

    def show_particles(self):

        for particle in self.particles:
            print(particle)

    def particle_positions(self):

        posx = []
        posy= []

        for particle in self.particles:
            posx.append(particle.position.real)
            posy.append(particle.position.imag)
        
        return (posx, posy)

    def particle_velocities(self):

        vx = []
        vy = []

        for particle in self.particles:
            vx.append(particle.velocity.real)
            vy.append(particle.velocity.imag)
        
        return (vx, vy)
        
        
        
        
    
