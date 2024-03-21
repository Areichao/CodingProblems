class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # number of columns/rows
        columns = len(grid[0])
        rows = len(grid)

    def BFSearch(self, grid: List[List[int]], k:int, origin: tuple[int]) -> bool:
        """ returns true if it reaches the end point and """