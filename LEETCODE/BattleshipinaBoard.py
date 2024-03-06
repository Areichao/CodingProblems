class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """ battle ship in a board q.419"""
        '''
        Input: board = [["X",".",".","X"],
                        [".",".",".","X"],
                        [".",".",".","X"]]
        Output: 2
        Example 2:

        Input: board = [["."]]
        Output: 0
        '''

        # linear solution   
        # traverse through the board, check if X is the start of a new ship. that is, 
        # if there is . on the top and . on its left as well. 

        # cases:
            # if it has no top piece (row = 0) then only check left
            # if it has no left piece (column = 0) then only check top 
            # if it has neither top or left (row = 0 and column = 0) then its a start piece.
        counter = 0 # keep track of number of ships
        for row in range(len(board)): # traverse through rows
            for column in range(len(board[0])): # traverse through columns
                if board[row][column] == "X":
                    if (row == 0 or board[row - 1][column] == ".") and (column == 0 or board[row][column - 1] == "."): 
                            counter += 1
        return counter
