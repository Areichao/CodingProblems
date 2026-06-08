import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
import unittest
from plateau import Plateau

class TestPlateau(unittest.TestCase):
    def setUp(self):
        """ runs before every test """
        self.plateau = Plateau(5, 5)

    def test_validSpot(self):
        self.assertTrue(self.plateau.validSpot(1, 1))
    
    def test_outOfBounds(self):
        self.assertFalse(self.plateau.validSpot(6, 6))
    
    def test_rock(self):
        self.plateau.newRock(2, 2)
        self.assertFalse(self.plateau.validSpot(2, 2))

if __name__ == "__main__":
    unittest.main()