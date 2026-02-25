class Solution:
    def isValid(self, s: str) -> bool:
        "([])"
        stack = []
        parenthesis = {"{":"}", "[": "]", "(":")"}
        for par in s:
            if par in parenthesis:
                stack.append(par)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if parenthesis[top] != par: # if it does not match its opening half
                    return False
        return not stack
