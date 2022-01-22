class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        # base case
        if len(string_x) == 0:
            return True 
        elif string_x[0] != string_x[-1]:
            return False
        # recursive case 
        else:
            return self.isPalindrome(string_x[1:-1])
    

# TESTING CODE HERE
example1 = Solution()
print(example1.isPalindrome(1000021))

