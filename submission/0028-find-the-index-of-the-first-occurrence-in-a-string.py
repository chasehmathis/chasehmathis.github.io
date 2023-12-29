class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        window = len(needle)
        while i < len(haystack):
            print(haystack[i:window])
            if haystack[i:window+i] == needle:
                return i
            i += 1
        

        return -1
