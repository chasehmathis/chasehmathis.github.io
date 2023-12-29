class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxx = 0
        let_set = set()
        
        while r < len(s):
            if s[r] not in let_set:
                let_set.add(s[r])
                maxx = max(len(let_set), maxx)
                r += 1
            else:
                let_set.remove(s[l])
                l += 1
        
        return maxx

