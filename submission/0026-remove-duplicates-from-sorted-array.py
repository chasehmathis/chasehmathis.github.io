class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        s = set([])
        for num in nums:
            if num not in s:
                s.add(num)
                nums[i] = num
                i += 1


        return i
            
