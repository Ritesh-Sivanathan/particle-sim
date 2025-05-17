from particle import Particle

class System:

    def __init__(self):
        self.particles:list[Particle] = []
        self.bounds = [0, 0]

    def show_particles(self):

        for particle in self.particles:
            print(particle)

    def check_collision(self):

        posx = []
        posy = []

        for particle in self.particles:
            posx.append(particle.position.real)
            posy.append(particle.position.imag)
        
        
        
    
