class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        ans = 0

        # get into position with last few characters being spaces
        while s[i] == " ":
            i -= 1


        while s[i] != " " and i >= 0:
            ans += 1
            i -= 1


        return ans
