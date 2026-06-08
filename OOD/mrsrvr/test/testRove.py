import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))

import unittest
from mR import MarsRover
from plateau import Plateau

class TestRove(unittest.TestCase):
    def setUp(self):
        self.plateau = Plateau(5, 5)
        self.rover = MarsRover(1, 1, "N", self.plateau)

    def test_moveBlocked(self):
        self.plateau.newRock(1, 2)
        self.rover.command("M")
        self.assertEqual(self.rover.getCoordinates(), (1, 1))


if __name__ == "__main__":
    unittest.main()
