class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        ret = ""
        j = 0

        for i in range(len(t)):
            if j >= len(s):
                break
            if t[i] == s[j]:
                ret += s[j]
                j += 1
                

        return ret == s

        

            
