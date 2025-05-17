import unittest
from particle import Particle

class VelocityTests(unittest.TestCase): # Run testcases with varying velocities on a test particle

    def test_positive_velocity(self): # vx > 0 and vy > 0
        p = Particle()
        self.assertEqual(p.change_velocity(1,1,1), complex(1,1))
    
    def test_negative_velocity(self): # vx < 0 and/or vy < 0
        p = Particle()
        self.assertEqual(p.change_velocity(-1,3,1), complex(-1,3))
        self.assertEqual(p.change_velocity(-4,-2,1), complex(-4,-2))

class PositionTests(unittest.TestCase): # Run testcases for different positions with different velocities
    pass

if __name__ == "__main__":
    unittest.main()