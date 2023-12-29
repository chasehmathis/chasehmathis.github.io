class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left pass
        L = [1]*len(nums)
        for i in range(1,len(nums)):
            L[i] = nums[i-1] * L[i-1]

        # right pass
        R = [1]*len(nums)
        for i in reversed(range(len(nums)-1)):
            R[i] = nums[i+1] * R[i + 1]

        ret = [1]* len(nums)
        for i in range(len(nums)):
            ret[i] = L[i]*R[i]

        return ret


        
