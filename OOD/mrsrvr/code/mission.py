from plateau import Plateau
from mR import MarsRover
from itertools import count
class Mission:

    def __init__(self):
        """ init """
        self.roverCount = count(1)
    
    def parse(self, content: str) -> None:
        """ reads through one case and does instructions """
        # gets content for this test case
        lines = content.strip().split("\n")
        idx = 0

        # set up the plateau
        try:
            plateau = self._setUpPlateau(lines[idx])
        except ValueError as e:
            print(f"Skipping this test case: {e}")
            return 
        idx += 1

        # iterates through number of rocks and places it on board
        try:
            numRocks = int(lines[idx])
        except ValueError as e:
            print(f"Number of rocks should be an integer, got {e}")

        idx += 1
        for _ in range(numRocks):
            try:
                self._setUpRocks(plateau, lines[idx])
            except ValueError as e:
                print(f"Skipping this Rock: {e}")
            idx += 1 

        # creates rover(s) and does instructions for each in sequential order
        while idx < len(lines):
            try:
                rover = self._setUpRover(lines[idx], plateau)
                for ins in lines[idx + 1]:
                    try:
                        rover.command(ins)
                    except ValueError as e:
                        print(f"Skipping this command: {e}")
                plateau.newRock(*rover.getCoordinates())
                self.roverAnswer(rover)
            except ValueError as e:
                print(f"Skipping this rover: {e}")
            idx += 2

        print("End of current test case")
    
    @staticmethod
    def _setUpRover(inpt: str, plateau: Plateau) -> MarsRover:
        """ Create rover """
        try:
            # these 2 cases, python will raise on its own
            x, y, direction = inpt.split() # set x, y and direction  
            x, y = int(x), int(y)
        except ValueError as e:
            raise ValueError(f"Invalid rover input, expected 'x(int) y(int) direction(char)' got {inpt}") from e
        return MarsRover(x, y, direction, plateau)
        
    @staticmethod
    def _setUpPlateau(inpt: str) -> Plateau:
        """ creates plateau with right corner 'x, y'"""
        try:
            x, y = map(int, inpt.split())
        except ValueError as e:
            raise ValueError(f"Expected coordinate 'x(int) y(int)', got {inpt}") from e 
        return Plateau(x, y)
    
    @staticmethod
    def _setUpRocks(plateau: Plateau, coord: str) -> None:
        """ sets up the rocks on plateau """
        try:
            x, y = map(int, coord.split())
        except ValueError as e:
            raise ValueError(f"Expected coordinate 'x(int) y(int)', got {coord}") from e
        plateau.newRock(x, y)

    def roverAnswer(self, rover: MarsRover) -> None:
        """ prints out current location of rover """
        print(f"Rover number {next(self.roverCount)} is currently at {rover.getLocation()}")

        