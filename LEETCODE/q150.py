class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #'+', '-', '*', and '/'.
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left/right))
            else:
                stack.append(int(token))
        return stack.pop()
