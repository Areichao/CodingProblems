class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # count variable set to 0 originally
        # flag to check if first instance of 1
        # for each number in nums
        # if number is 1 and its the first instant of 1
        # then start counter
        # else, if number is 0 then add to counter. if number is 1 and counter >= k then reset counter to 0
        # but if number is 1 and counter < k, return false (early return)
        # finally, return true
        # [0,0,0,1,0,1]
        # Time complexity O(n) and space complexity O(1)
        count_between = 0
        first_one = True

        for bin in nums:
            if bin == 1 and first_one:
                count_between = 0
                first_one = False
            elif bin == 1 and not first_one and count_between < k:
                return False
            elif bin == 1 and count_between >= k:
                count_between = 0
            else:
                count_between += 1
        return True