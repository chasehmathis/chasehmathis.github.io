class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1, d2 = {}, {}

        for let in s:
            if let not in d1:
                d1[let] = 0

            d1[let] += 1

        for let in t:
            if let not in d1:
                return False

            if d1[let] == 0:
                return False

            d1[let] -= 1

        for v in d1.values():
            if v != 0:
                return False


        return True
