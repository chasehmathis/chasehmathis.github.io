class Solution:
    def longestPalindrome(self, s):

        def expand_around_center(s, left, right):
            while right < len(s) and left >= 0 and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            a = expand_around_center(s, i, i)
            b = expand_around_center(s, i, i+1)

            if len(a) > len(longest):
                longest = a
            if len(b) > len(longest):
                longest = b


        return longest
        

        
