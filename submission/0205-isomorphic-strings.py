class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
    
        char_map = {}
        
        for i in range(len(s)):

            if s[i] in char_map:
                c = char_map[s[i]]

                if c != t[i]:
                    return False
            elif t[i] not in char_map.values():
                char_map[s[i]] = t[i]

            else:
                return False

        return True
