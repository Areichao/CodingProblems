class Solution:
    def trap(self, height: List[int]) -> int:
        # O(1) memory solution with double pointers
        if len(height) == 0:
            return 0
        # init
        leftPointer = 0
        rightPointer = len(height)-1
        maxLeft = height[leftPointer]
        maxRight = height[rightPointer]
        waterStored = 0
        # iterate through before pointers cross paths
        while rightPointer > leftPointer:
            # left maximum is still smaller or equal, move left pointer
            if maxLeft <= maxRight:
                leftPointer += 1
                # since this is minimum, subtract height of current index from this
                if maxLeft - height[leftPointer] > 0:
                    waterStored += maxLeft - height[leftPointer]
                else:
                    maxLeft = height[leftPointer] # new maximum
            else: # bring right pointer one to the left
                rightPointer -= 1
                # since this is minimum, same thing but for right side
                if maxRight - height[rightPointer] > 0:
                    waterStored += maxRight - height[rightPointer]
                else:
                    maxRight = height[rightPointer]
        return waterStored