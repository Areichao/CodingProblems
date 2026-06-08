class Plateau:
    def __init__(self, x: int, y: int):
        """ initialize the plateau for the rover to move around """
        # minimum is assumed to be 0 for both x and y. this sets the maximum value x or y can be
        self.maxX, self.maxY = x, y

        self.rocks = set() # stored as tuple values of (x, y)

    def newRock(self, x: int, y: int) -> None:
        """ adds a new rock into the plateau """
        # ignores if the rock is already on -> set does this automatically
        if self.validSpot(x, y):
            self.rocks.add((x, y))
        else:
            raise ValueError(f"Rock placement is out of bounds or there is another rock, got {x}, {y}")
    
    def validSpot(self, x: int, y: int) -> bool:
        """ returns true if the given coordinate of the plateau is valid """
        return not (self.hitRock(x, y) or self.offEdge(x, y))
    
    def hitRock(self, x: int, y: int) -> bool:
        """ returns true if the rover has hit a rock """
        return (x, y) in self.rocks
    
    def offEdge(self, x: int, y: int) -> bool:
        """ returns true if the rover is now off an edge """
        return x < 0 or x > self.maxX or y < 0 or y > self.maxY
    
    def newSpot(self, x: int, y: int) -> tuple[int, int]:
        """ returns the coordinate of the new spot OR original if rover cannot wrap """
        new = (x, y)
        if x < 0:
            new = (self.maxX, y)
        elif x > self.maxX:
            new = (0, y)
        elif y < 0: 
            new = (x, self.maxY)
        elif y > self.maxY:
            new = (x, 0)
        
        return new if not self.hitRock(*new) else (x, y)
        


