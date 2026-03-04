class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRow = 0
        rightRow = len(matrix) - 1
        while leftRow < rightRow:
            middle = (rightRow + leftRow) // 2
            if matrix[middle][-1] < target: # if the rightmost element of the middle row is less than target
                leftRow = middle + 1 # search bottom half of the current matrix
            elif matrix[middle][0] > target: # if the leftmost element of middle row is greater than target
                rightRow = middle - 1
            else: # binary search inside the current matrix
                left, right = 0, len(matrix[middle]) - 1
                while left < right:
                    mid = (left + right) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] < target:
                        left = mid + 1
                    else: 
                        right = mid
                return matrix[middle][left] == target
            
        # loop ended: candidate row is leftRow (== rightRow)
        row = leftRow
        if not (matrix[row][0] <= target <= matrix[row][-1]):
            return False
        
        left, right = 0, len(matrix[row]) - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else: 
                right = mid
        return matrix[row][left] == target



