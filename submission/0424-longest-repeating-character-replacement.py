class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        if len(s) == 1:
            return 1

        start = 0
        end = 1

        freq = defaultdict(int)
        freq[s[start]] += 1
        
        max_len = 0
        max_freq = 1

        for end in range(1, len(s)):
            freq[s[end]] += 1

            max_freq = max(max_freq, freq[s[end]])

            num_to_change = (end - start + 1) - max_freq

            while num_to_change > k:
                print(start, end, num_to_change)
                freq[s[start]] -= 1
                start += 1

                max_freq = max(freq.values())

                num_to_change = (end - start + 1) - max_freq
            max_len = max(max_len, (end - start + 1))
        return max_len
