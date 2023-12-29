class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = set()
        r, l = 0, -k
        if(k <= 0): return False
        while r < len(nums):
            if nums[r] in mem:
                return True
            if l >= 0 and nums[l] in mem:
                mem.remove(nums[l])

            mem.add(nums[r])

            l += 1
            r += 1

        return False

