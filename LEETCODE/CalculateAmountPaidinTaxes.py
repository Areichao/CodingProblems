# brackets[i] = [upperi, percenti]
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        """ calculate how much you are taxed based off tax brackets given """
        prev = 0
        totalTax = 0
        for bracket in brackets:
            if income - (bracket[0] - prev) <= 0:
                totalTax += income * (bracket[1] * 0.01)
                break
            else:
                income -= (bracket[0] - prev)
                totalTax += (bracket[0] - prev) * (bracket[1] * 0.01)
                prev = bracket[0]
        return totalTax