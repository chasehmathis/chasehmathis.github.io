class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # memo = {}
        # def dfs(nums, i, sl, sr):
        #     if (i, sl) in memo:
        #         return memo[i,sl]

        #     if i == len(nums):
        #         return sl == sr

        #     # accept or decline
        #     accept = dfs(nums, i + 1, sl + nums[i], sr - nums[i])

        #     decline = dfs(nums, i + 1, sl, sr)
        #     memo[(i,sl)] = accept or decline
        #     return accept or decline

        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
        # return dfs(nums, 0, 0, sum_of_nums)

        
        # # Step 2: Quick check to see if partitioning is possible
        if sum_of_nums % 2 != 0:
            return False
        
        target = sum_of_nums // 2
        
        # # Step 1: Initialize the DP Array
        # dp = [False] * (target + 1)
        
        # # Step 2: Base Case
        # dp[0] = True
        
        # # Step 3: Update Rule
        # for num in nums:
        #     for i in range(target, num - 1, -1):
        #         # print(dp)
        #         dp[i] = dp[i] or dp[i - num]
        
        # return dp[-1]
        
        s = set()
        s.add(0)
        for i in range(len(nums)):
            next_s = set()
            for val in s:
                val += nums[i]
                next_s.add(val)
            
            s.add(nums[i])
            s = s.union(next_s)
        return sum_of_nums//2 in s


