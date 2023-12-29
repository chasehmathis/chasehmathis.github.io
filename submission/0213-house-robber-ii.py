class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
                return 0
        if len(nums) <= 2:
            return max(nums)

        def helper(nums):
            if len(nums) == 0:
                return 0
            if len(nums) <= 2:
                return max(nums)

            # old house robber
            n = len(nums)
            dp = [0]*n

            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

            return dp[-1]

        # case one rob house one

        first = helper(nums[0:-1])
        last = helper(nums[1:])

        return max(first, last)
