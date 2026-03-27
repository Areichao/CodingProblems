class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # T: O(log(min(n, m))) S: O(1)
        # binary search on smaller array. make sure nums1 is always the smaller one
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        # variables for lengths of each list, then setup the shorter (list 1) for binary search
        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1

        # basic while loop for binary search
        while left <= right:
            # list1 partition is basic middle search algorithm for binary search
            part1 = (right + left) // 2
            # list2 partition depends on the number of left elements in list1, and the total left elements if lists were to combine
            part2 = (len1 + len2 + 1) // 2 - part1

            # edge cases, set min and max of each partition (max for lefts, min for rights, and +/-inf if they are edge cases)
            maxL1 = (float('-inf') if part1 == 0 else nums1[part1 - 1])
            minR1 = (float('inf') if part1 == len1 else nums1[part1])
            maxL2 = (float('-inf') if part2 == 0 else nums2[part2 - 1])
            minR2 = (float('inf') if part2 == len2 else nums2[part2])

            # in the case that both left partitions are correct, we have the median
            if maxL1 <= minR2 and maxL2 <= minR1:
                # calculation for if the length of both combined is even, otherwise take the middle number
                if (len1 + len2) % 2 == 0:
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2
                return max(maxL1, maxL2)
            
            # if the max number in left partition is greater than min partition on right, move right pointer, otherwise left. 
            elif maxL1 > minR2:
                right = part1 - 1
            else:
                left = part1 + 1