class Solution:
    import math
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        # sort the list so it turns into two sum 2
        
        nums.sort() # O(n log(n))
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                a = nums[i]
                d[a] = {}
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    # binary search
                    b = nums[j]
                    c = nums[k]
                    res = a + b + c
                    if res > 0:
                        # guess is to big, move right pointer back
                        k -= 1

                    elif res < 0:
                        #guess to small, move left pointer back
                        j += 1

                    if res == 0:
                        if b not in d[a]:
                            d[a][b] = {}
                            if c not in d[a][b]:
                                d[a][b][c] = 0
                                ret.append([a, b, c])
                        j += 1

        return ret


        
