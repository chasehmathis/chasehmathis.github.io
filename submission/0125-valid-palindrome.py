class Solution:
    def is1Palindrome(self, s: str) -> bool:

        s = s.lower()
        alph = "abcdefghijklmnopqrstuvwxyz"
        alph = set(list(alph))
        
        start = 0
        end = len(s)-1
        while start < end:
            while start < end and s[start] not in alph:
                start += 1
            while start < end and s[end] not in alph:
                end -= 1

            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
    


