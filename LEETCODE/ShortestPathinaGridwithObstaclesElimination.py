from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        """ shortest path -> bfs """
        # initialize rows and columns and last location
        rows = len(grid)
        columns = len(grid[0])
        finish = (rows-1, columns-1)

        # if we have enough k to take the shortest path
        if k >= rows + columns - 2:
            return rows + columns - 2
        
        # if we dont we gotta do graph thingy
        # initialize queue -> (steps_taken, (rows, columns, steps_remaining))
        queue = deque([(0,(0,0,k))])
        # initialize set -> nodes that are already visited
        visited = {(0,0,k)}

        # initialize all the possible directions (up, down, left, right)
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        
        # while the queue exists lol
        while queue:
            steps_taken, (row, column, k_remain) = queue.popleft()
            # if the current row and column is what we are looking for, return the number of steps
            if (row, column) == finish:
                return steps_taken
            # for each direction you can go in 
            for direction in directions:
                # if that direction exists
                if 0 <= row + direction[0] < rows and  0 <= column + direction[1] < columns:
                    # new_k_value will be k_remain - grid[row+direction][column+direction] 
                    newK = k_remain - grid[row+direction[0]][column+direction[1]]
                    newValue = (steps_taken+1,(row+direction[0], column+direction[1], newK))
                    # if newK is greater than 0 or equal
                    if newK >=0:
                        if newValue[1] not in visited:
                            queue.append(newValue)
                            visited.add(newValue[1])


        # if we go through the while loop and we did not return anything,
        return -1
                

