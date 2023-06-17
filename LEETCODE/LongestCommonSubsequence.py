# Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        maximum = 0

        cs = [[0 for j in range(len(text1))] for i in range(len(text2))]
        for row in range(len(text2)):
            for column in range(len(text1)):
                if text2[row] == text1[column]:
                    if row == 0 or column == 0: # if its the first element
                        cs[row][column] = 1
                        maximum = max(maximum, 1) # set new maximum if greater than 1
                    elif row != 0 and column != 0: # neither first
                        cs[row][column] = cs[row-1][column-1] + 1
                        maximum = max(maximum, cs[row][column]) # set new maximum if greater than current maximum
                else:
                    if row == 0 and column != 0: # first row
                        cs[row][column] = cs[row][column - 1]
                    elif row != 0 and column == 0: # first column
                        cs[row][column] = cs[row - 1][column]
                    elif row != 0 and column != 0: # neither first
                        cs[row][column] = max(cs[row][column - 1], cs[row - 1][column])
        return maximum

# codeDominar's really fast solution for reference and comparison
# https://leetcode.com/problems/longest-common-subsequence/solutions/2913309/beats-98-codedominar-solution-bottom-up-approach/
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

#         for i in range(len(text1)-1,-1,-1):
#             for j in range(len(text2)-1,-1,-1):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                 else:
#                     dp[i][j] = max(dp[i][j+1],dp[i+1][j])
#         return dp[0][0]
        
