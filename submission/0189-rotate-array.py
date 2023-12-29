class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # modulus length of List
        n = len(nums)
        numCopy = nums[:]
        i = 0
        while i < n:
            idx = (i + k)% n
            nums[idx] = numCopy[i]
            i += 1

        return nums



        
