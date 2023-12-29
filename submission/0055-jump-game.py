class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # start backwards

        last_position = len(nums) - 1
        i = last_position - 1
        while i >= 0:

            if nums[i] + i >= last_position:
                last_position = i

            i -= 1
        return last_position == 0

