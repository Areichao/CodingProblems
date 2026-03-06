import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search O (n log m) space: O(1)
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            midSpeed = (maxSpeed + minSpeed) // 2
            # iterate through to see if this speed works
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / midSpeed)
                if hours >= h:
                    break # break early if speed too slow
            if hours > h: # if too slow, midSpeed + 1 becomes the new minSpeed
                minSpeed = midSpeed + 1
            else: # otherwise, if less than or equal to hours, we make this the maximum
                maxSpeed = midSpeed
        return maxSpeed
