class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            if d[num] < 3:
                nums[i] = num
                i += 1


        return i
