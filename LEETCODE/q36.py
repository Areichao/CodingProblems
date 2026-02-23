class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for rowIndex in range(9): # traverse row by row, left to right
            for columnIndex in range(9):
                # check if the number is already in any of the sets. if it is, return false
                num = board[rowIndex][columnIndex]
                squareIndex = (rowIndex // 3) * 3 + (columnIndex // 3) # split the squares into numbers 0-8, row * 3 to determine if the number starts with 0, 3 or 6.
                if num != '.':
                    if (num in rows[rowIndex] or num in columns[columnIndex] or num in squares[squareIndex]):
                        return False
                    # otherwise, add to the set and continue
                    rows[rowIndex].add(num)
                    columns[columnIndex].add(num)
                    squares[squareIndex].add(num)

        return True