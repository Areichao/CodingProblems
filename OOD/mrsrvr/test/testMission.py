import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))

import unittest
from mission import Mission

class TestMission(unittest.TestCase):
    
    def setUp(self):
        self.validInput = """5 5
0
1 1 N
MMMM"""

    def test_validInput(self):
        """ basic valid input runs without error """
        mission = Mission()
        mission.parse(self.validInput)

    def test_multipleRovers(self):
        """ multiple rovers are processed sequentially """
        raw = """5 5
0
1 1 N
MM
1 5 S
MM"""
        mission = Mission()
        mission.parse(raw)

    def test_badPlateau(self):
        """ bad plateau input raises error """
        raw = """hello world
0
1 1 N
MMMM"""
        mission = Mission()
        with self.assertRaises(ValueError):
            mission.parse(raw)

    def test_badRock(self):
        """ bad rock coordinate raises error """
        raw = """5 5
1
hello world
1 1 N
MMMM"""
        mission = Mission()
        with self.assertRaises(ValueError):
            mission.parse(raw)

if __name__ == "__main__":
    unittest.main()