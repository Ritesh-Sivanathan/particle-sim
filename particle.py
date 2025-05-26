"""

2D Bounded Particle

Particle().loop() returns a 2D array containing the x and y points of the particle during the simulation

Example Usage:

 p = Particle(...)
 p.loop(100)

"""

import numpy as np

class Particle:

    """

    Simulates a 2D particle in a bounded rectangular space.
    Only .loop(iterations) is public

    Args:

        px (float) : Initial x position
        py (float) : Initial y position
        vx (float) : Initial x velocity
        vy (float) : Initial y velocity

        dt (float) : timestep
        
        min_x (float) : Minimum x boundary : min_x ≠ max_x
        max_x (float) : Maximum x boundary : max_x ≠ min_x
        min_y (float) : Minimum y boundary : min_y ≠ max_y
        max_y (float) : Maximum y boundary : max_y ≠ min_y

        logging (boolean) : Return a log of the particle's positions

    """

    def __init__(self, px=0, py=0, vx=1, vy=1, dt=1, min_x=0, max_x=10, min_y=0, max_y=10, logging=True):
        
        self.px = px
        self.py = py
        
        self.vx = vx
        self.vy = vy
        self.dt = dt

        self.min_x = min_x
        self.max_x = max_x
        
        self.min_y = min_y
        self.max_y = max_y
        
        self.logging = logging

        self.data = [[], []]

    def _handle_collision(self):

        ''' Particle position and boundary collision update logic. '''

        # Using `getattr`` and `setattr` because self.xyz makes code look completely unreadable

        for axis in ["x", "y"]: # iterate through axes x,y so we can access the respective velocities and positions using [get/set]attr

            velocity = getattr(self, f"v{axis}")
            position = getattr(self, f"p{axis}")
            max_val = getattr(self, f"max_{axis}")
            min_val = getattr(self, f"min_{axis}")

            next_position = position + velocity # Position of either x or y after next timestep
            
            if next_position > max_val: # If past upper bounds
                
                t = (max_val-position)/velocity # Exact time during the next timestep that the collision happens
                
                # Set the position of the particle to where the collision with the upper boundary happens

                setattr(self, f"p{axis}", max_val - velocity*(self.dt-t))
                setattr(self, f"v{axis}", -velocity*np.random.uniform(0.9,1.1))
            
            elif next_position < min_val: # If under lower bounds

                t = (min_val-position)/velocity # Exact time during the next timestep that the collision happens
                
                # Set the position of the particle to where the collision with the upper boundary happens
                
                setattr(self, f"p{axis}", min_val - velocity*(self.dt-t)) 
                setattr(self, f"v{axis}", -velocity*np.random.uniform(0.9,1.1))
            
            else:
                setattr(self, f"p{axis}", next_position)

    def _log_position(self):

        """ Logs position data of particle  """
        
        self.data[0].append(self.px)
        self.data[1].append(self.py)
        
    def loop(self, iterations):

        for _ in range(iterations): # Loop over number of iterations provided

            self._handle_collision()

            if self.logging:
                self._log_position()

        return self.data