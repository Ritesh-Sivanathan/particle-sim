'''

Particle object.


'''

class Particle:

    def __init__(self):
        self.position = [0, 0]
        self.velocity = [0, 0]
    
    def update_particle_position(self,x:int=None,y:int=None):
        
        '''
        
        Update the position of the particle using the current velocity
        There are two optional arguments to use when calling this function.
            x is the specific x value the particle should move to. If this is provided, the particle's position will be updated accordingly
            y is the specific y value the particle should move to.
        
        '''

        if not x and not y:
            self.position[0] += self.velocity[0] # Update x position 
            self.position[1] += self.velocity[1] # Update y position
        else:
            self.position[0] = x
            self.position[1] = y

        return self.position

    def simulate_particle_position(self):

        '''
        
        Simulate the particle's position within the next time interval. 
        The particle's position or velocity is NOT affected by calling this function.

        '''

        return [(self.position[0] + self.velocity[0]), (self.position[1] + self.velocity[1])]

    def update_velocity(self, vx, vy):
        
        self.velocity = [vx, vy]
        
        return self.velocity