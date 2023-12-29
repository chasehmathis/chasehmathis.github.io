class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        i = 0
        j = i + 1

        while j < len(nums):
            if nums[j] == nums[i]:
                return nums[j]
            j += 1
            i += 1
        return None

