
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        switch = {0: ')', 1: '}', 2: ']'}
        rightParenthesis = []
        for bracket in s:
            if (bracket == '(') or (bracket == '{') or (bracket == '['):
                rightParenthesis.append(bracket)
            else:
                if (len(rightParenthesis) == 0):
                    return False
                elif ((bracket == switch.get(0)) and (rightParenthesis[-1] == '(')) or ((bracket == switch.get(1)) and (rightParenthesis[-1] == '{')) or ((bracket == switch.get(2)) and (rightParenthesis[-1] == '[')):
                    rightParenthesis.pop()
                else:
                    return False
                    
        return (len(rightParenthesis) == 0)

# TESTING CODE HERE
example1 = Solution()
print(example1.isValid("(])"))
