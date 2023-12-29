class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        dp[n] = True

        for i in reversed(range(n)):
            #  go backwards
            for word in wordDict:
                
                condition_1 = i + len(word) <= n
                condition_2 = word == s[i:i + len(word)]

                if condition_1 and condition_2:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break # incase of duplicates

        return dp[0]

        
