class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0, len(nums) - 1
        minn = float('inf')
        while l <= r:

            m = (l + r)//2
            minn = min(minn, nums[m])

            # right has th the min
            if nums[m] > nums[r]:
                l = m + 1
            
            #left has the min
            else:
                r = m -1

        return min(minn, nums[l])
          
