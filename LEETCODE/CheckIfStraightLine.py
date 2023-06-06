import math
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        # if 3 or higher: compare
        for i in range(2, len(coordinates)):
            # starting on third, find c value between coord 1 & 2, then 2 & 3, then calculate c between 1 and 3 and check if they are the same. 
            # next iteration: 2 & 3, 3 & 4, then 2 & 4 and see if they are the same
            # repeat till done
            twoBefore = coordinates[i-2]
            oneBefore = coordinates[i-1]
            current = coordinates[i]
            x1 = twoBefore[0]
            x2 = oneBefore[0]
            x3 = current[0]
            y1 = twoBefore[1]
            y2 = oneBefore[1]
            y3 = current[1]
            dist1 = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))
            dist2 = math.sqrt(((x3-x2) ** 2) + ((y3-y2) ** 2))
            final = math.sqrt(((x3-x1) ** 2) + ((y3-y1) ** 2))

            if final != (dist1 + dist2):
                return False
            if (y2 > y1) and (y3 < y2):
                return False
            if (y2 < y1) and (y3 > y2):
                return False
        return True
    
    # def pythFindC(self, a: int, b: int) -> float:
    #     """ takes side a and b and returns c in a right triangle """
    #     # might have to convert into float
    #     return ((a**2) + (b**2))

   #def distanceVector(self, x1: int, x2: int, y1: int, y2: int) -> float:
      #  """ gets the distance between two points and returns the value """
      #  pass
       # # do distance vector formula here
