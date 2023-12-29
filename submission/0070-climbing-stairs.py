class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return n
        prev1, prev2 = 1,1

        for n in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return curr


        
