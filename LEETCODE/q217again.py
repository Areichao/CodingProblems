class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for num in nums: # O(n) O(n)
            if num in duplicates:
                return True
            duplicates.add(num)
        return False