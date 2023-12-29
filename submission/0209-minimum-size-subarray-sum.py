class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minn = float('inf')

        i = 0
        j = 0
        s = 0
        while j < len(nums):

            s += nums[j]
            j += 1

            while s >= target:
                minn = min(minn, j - i)
                s -= nums[i]
                i += 1
    
        if minn == float('inf'):
            return 0
        return minn

        
