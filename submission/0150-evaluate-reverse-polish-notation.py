class Solution:

    @staticmethod
    def map_ops(op, num1, num2):

        if op == "+":
            return num1 + num2
        elif op == '/':
            return int(num1/num2)

        elif op == '*':
            return num1 * num2

        elif op == '-':
            return num1 - num2

        else:
            return None
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque

        stack = deque()


        ret = 0
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))

            else:
                r = stack.pop()
                l = stack.pop()
                res = self.map_ops(token, l, r)
                stack.append(res)
    
        return stack.pop()



       
