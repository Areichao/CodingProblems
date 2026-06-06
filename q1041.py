class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """ given a set of instructions, is the robot bound in a circle? """
        # keep track of the robots current direction and coordinates
        direction = 0 # North direction
        x = y = 0

        # store all possible directions as direction: 1 unit vectors 
        dirVec = [(0, 1),(1, 0),(0, -1),(-1, 0)] # N E S W, 0, 1, 2, 3

        # loop through instruction string
        for i in instructions:
            if i == "G": # go straight 1 in direction its facing
                dx, dy = dirVec[direction]
                x += dx
                y += dy
            elif i == "L": # turn left 
                direction = (direction - 1) % 4 # at max, goes to -1 and -1 % 4 = 3 (West)
            else: # turn right 
                direction = (direction + 1) % 4 # at max, goes to 4 and 4 % 4 = 0 (North)

        return True if (x, y) == (0, 0) or direction else False # direction cannot be 0 or north