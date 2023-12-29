class Solution:
    def isValid(self, s: str) -> bool:

        #parentheses
        open_parentheses = ['(', '[', '{']
        close_parentheses = [')', ']', '}']

        #stack
        stack = []

        #loop through string
        for i in range(len(s)):
            #if opening parentheses, add to stack
            if s[i] in open_parentheses:
                stack.append(s[i])
            #if closing parentheses, check if it matches the last opening parentheses
            elif s[i] in close_parentheses:
                if len(stack) == 0:
                    return False
                elif close_parentheses.index(s[i]) == open_parentheses.index(stack[-1]):
                    stack.pop()
                else:
                    return False

        #if stack is empty, return true
        if len(stack) == 0:
            return True


