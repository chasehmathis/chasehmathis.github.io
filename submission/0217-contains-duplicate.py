class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mem = set()

        for num in nums:
            if num not in mem:
                mem.add(num)
            else:
                return True


        return False
