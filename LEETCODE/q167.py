class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        for i, num in enumerate(numbers):
            while num + numbers[right] > target:
                right -= 1
            if num + numbers[right] == target:
                return [i + 1, right + 1]