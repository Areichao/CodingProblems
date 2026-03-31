class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # run fast and slow on linked list version of list (use value as pointer to next index)
        # stop once they are at the same node
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # once index are the same, we ignore fast pointer, and create another slow pointer at the start
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        # once they intersect, that is the start of cycle (our dupe)
        return slow