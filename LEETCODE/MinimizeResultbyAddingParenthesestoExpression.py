class Solution:
    def minimizeResult(self, expression: str) -> str:
        currMin = eval(expression)
        outputString = "(" + expression + ")" # output string
        # for numbers in range string
        for p1 in range(len(expression)):
            # same thing but from the back of the string 
            for p2 in range(len(expression)- 1, -1, -1):
                # add * sign for eval() function
                if p1 != 0 and p2 != (len(expression)-1):
                    newExpression = expression[:p1] + "*(" + expression[p1:p2+1] + ")*" + expression[p2+1:]
                elif p1 != 0:
                    newExpression = expression[:p1] + "*(" + expression[p1:p2+1] + ")" + expression[p2+1:]
                elif p2 != (len(expression)-1):
                    newExpression = expression[:p1] + "(" + expression[p1:p2+1] + ")*" + expression[p2+1:]
                else:
                    newExpression = expression[:p1] + "(" + expression[p1:p2+1] + ")" + expression[p2+1:]
                # calculate the current evaluation
                print("the new expression is: ", newExpression)
                calculated = eval(newExpression)
                print("calculated value is: ", calculated)
                # if the calculated value is less than the current minimum
                if calculated < currMin:
                    # set new minimum and output value
                    currMin = calculated
                    outputString = expression[:p1] + "(" + expression[p1:p2+1] + ")" + expression[p2+1:]
                # if the next index is the plus sign, break the inner loop
                if expression[p2 - 1] == "+":
                    break
            # if the next index is the plus sign, break the program entirely
            if expression[p1 + 1] == "+":
                break
        return outputString
    
# "247+38"
object = Solution()
print(object.minimizeResult("247+38"))