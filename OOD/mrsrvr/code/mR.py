# https://code.google.com/archive/p/marsrovertechchallenge
from plateau import Plateau
class MarsRover:
    # class level constants
    UNITVECTORS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N E S W
    DIRECTIONS = ("N", "E", "S", "W") # clockwise direction: index 0 1 2 3
    INSTRUCTIONS = {"L": "turnLeft", "R": "turnRight", "M": "move"}

    def __init__(self, x: int, y: int, direction: str, plateau: Plateau):
        """ initalize a mars rover with its starting coordinate """
        self.plateau = plateau # the platform that this mars rover is moving on -> assuming different rovers might have different plateaus
        self.x, self.y, self.direction = x, y, direction
        
        # check if direction is valid
        if self.direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction, expected one of N E S W got {self.direction}")
        # check if coordinate is valid
        if not self.plateau.validSpot(self.x, self.y):
            raise ValueError(f"Rover coordinates invalid, either on a rock or out of bounds. given: {self.x} {self.y}")
        
        self.direction = self.DIRECTIONS.index(self.direction) # get integer value for direction
    
    def turnLeft(self) -> None:
        """ Turn the rover left """
        self.direction = (self.direction - 1) % 4
    
    def turnRight(self) -> None:
        """ Turn the rover right """
        self.direction = (self.direction + 1) % 4

    def move(self) -> None:
        """ moves the x and y value of the rover depending on where its facing (moves 1 unit) """
        # given the direction, add value onto x or y coordinate IF the spot is valid
        x, y = self.UNITVECTORS[self.direction]
        newX, newY = self.x + x, self.y + y
        if self.plateau.offEdge(newX, newY):
            self.x, self.y = self.plateau.newSpot(newX, newY)

        elif not self.plateau.hitRock(newX, newY):
            self.x += x
            self.y += y

    def command(self, instruction: str) -> None:
        """ executes command based on input character """
        if instruction not in self.INSTRUCTIONS:
            raise ValueError(f"Unknown instruction {instruction}")
        getattr(self, self.INSTRUCTIONS[instruction])()

    def getCoordinates(self) -> tuple:
        """ returns (x, y) location of rover """
        return (self.x, self.y)

    def getLocation(self) -> str:
        """ returns the coordinate and direction of the mars rover """
        return f"{self.x} {self.y} {self.DIRECTIONS[self.direction]}"

    
    