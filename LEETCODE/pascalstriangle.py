class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            pascalsTriangle = [[1], [1, 1]]
            for i in range(2, numRows):
                newRow = [1]
                for j in range(1, i): # previous row
                    newRow.append(pascalsTriangle[i-1][j-1] + pascalsTriangle[i-1][j])
                newRow.append(1)
                pascalsTriangle.append(newRow)
            return pascalsTriangle

