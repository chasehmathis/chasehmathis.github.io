class Solution:
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        s1_counter = Counter(s1)

        
        s2_counter = Counter(s2[:len(s1)]) # initialize at first window

        for i in range(len(s1), len(s2)):
            # if the counter is the same
            if s1_counter == s2_counter:
                return True

            s2_counter[s2[i]] += 1
            s2_counter[s2[i - len(s1)]] -= 1
        return s1_counter == s2_counter



