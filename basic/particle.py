
class Particle:

    '''
    
    Particle class to create particle objects.
    Instantiating a particle object using this class takes no arguments
    
    '''

    def __init__(self):
        
        # All properties will be set to 0. Start at the origin and no movement until it is explicitly set.

        self.position = complex(0, 0) # Position on the complex plane. In form x+iy
        self.velocity = complex(0, 0) # Complex velocity. In form vx+ivy. In (units/second)
        self.delta_time = 1.

    def change_velocity(self, x, y, dt): # Override the previous velocity of the particle at 1 second intervals
        
        '''
        Change the velocity of the particle in units/second.
        The velocity stays at the constant rate provided until it is reassigned. 
        Default velocity is 0.
        '''
        
        self.velocity = complex(x,y) # Update the velocity property of the object
        self.delta_time = dt # Update the delta_time of the velocity
        return self.velocity # Return the velocity (would return a complex number vx, ivy)

    def modify_velocity(self, x, y, dt):

        pass
    
    def update_particle_position(self):
        
        '''
        Update the particle's position based on its current velocity.
        '''

        pos = complex((self.position.real + (self.velocity.real*self.delta_time)), (self.position.imag + (self.velocity.imag*self.delta_time))) # Increment the position x and y by adding the respective velocities multiplied by the delta time
        
        self.position = pos # Update the object's velocity property

        return (self.position.real, self.position.imag)