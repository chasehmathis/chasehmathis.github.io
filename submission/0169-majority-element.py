class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #n = len(nums)
        #d = {}
        #maxx = 0
        #for num in nums:
        #    if num not in d:
        #        d[num] = 0
        #    d[num] += 1
        #    if d[num] > maxx:
        #        maxx = d[num]
        #    if maxx > n//2:
        #        return num
        #return None

        nums.sort()
        return nums[len(nums)//2]


