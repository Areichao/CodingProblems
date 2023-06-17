# also the hamming weight question
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n & 1 # and entire n with 1, if rightmost bit is 1 result will add 1
            n = n >> 1 # bitshift one to the right
        return result