"""

A System contains multiple particles and puts them onto the same plane
Interactions with particles in the system can be enabled and disabled.

"""

# particles shouldn't start off at the same point, especially if collision is on. It'll just screw everything up.
# maybe random initial positions? modify the px and py properties of each particle?

from particle import Particle

class System:
    
    def __init__(self, particles:list[Particle], collision=True):

        self.particles = particles
        self.collision = collision

        # self.data = [[[[], []]] * len(particles)]
        self.data = {index:[[],[]] for index, _ in enumerate(particles)}
    
    def show_particle_names(self):
        """
        Return a list of each particle's `name` property.
        Note: Particles' default name is "particle"
        """
        return [particle.name for particle in self.particles]

    def simulate(self):

        for i in range(500):
            for index, particle in enumerate(self.particles):
                
                px, py = particle.loop(1, system=True)

                # Append x and y positions to the respective array in the particle's dictionary

                self.data[index][0].append(px) 
                self.data[index][1].append(py) 
        
        return self.data


