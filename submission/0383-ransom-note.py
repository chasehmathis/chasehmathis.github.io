class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:


        d = {}

        for let in magazine:
            if let not in d:
                d[let] = 0

            d[let] += 1


        for let in ransomNote:
            if let not in d:
                return False

            num = d[let]
            if num <= 0:
                return False

            d[let] -= 1

        return True
