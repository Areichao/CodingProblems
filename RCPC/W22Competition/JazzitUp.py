class Solution(object):
    def squarefree(self, n):
        """
            :type n: int
            :rtype: int
        """
        for note in range(2, n):
            numberOfNotes = n * note
            # cant figure out for odd
            if (numberOfNotes % 4 != 0) and ((numberOfNotes - 1) % 8 != 0):
                return note



n  = int(input())
ans = Solution()
print(ans.squarefree(n))