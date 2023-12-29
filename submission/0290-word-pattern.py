class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        
        d = {}
        lst = s.split()
        s = set()

        if len(lst) != len(pattern):
            return False
        for i, let in enumerate(pattern):
            if let not in d:
                if lst[i] in s:
                    return False
                d[let] = lst[i]
                s.add(lst[i])

            else:
                if d[let] != lst[i]:
                    return False

        return True
            
