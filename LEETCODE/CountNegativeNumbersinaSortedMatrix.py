class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for list1 in grid:
            i = len(grid[0]) - 1
            while i >= 0 and list1[i] < 0:
                count += 1
                i -= 1
        return count
        