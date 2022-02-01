class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        index = 0
        while index in range(len(s)):
            # subtraction cases
            if ((s[index] == "I") or (s[index] == "X") or (s[index] == "C")) and (index != (len(s) - 1)) and (symbols[s[index+1]] > symbols[s[index]]):
                number += symbols[s[index+1]] - symbols[s[index]]
                index += 2
            else:
                number += symbols[s[index]]
                index += 1 

        return number

print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("III"))