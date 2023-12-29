class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums: return 0


        n = len(nums)

        maxx = minn = ans = nums[0]

        for i in range(1, n):

            num = nums[i]

            if num < 0:
                maxx, minn = minn, maxx

            maxx = max(maxx*num, num)
            minn = min(minn*num, num)

            ans = max(ans, maxx)

        return ans
