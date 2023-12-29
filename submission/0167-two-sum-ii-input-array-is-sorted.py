class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # binary search

        left, right = 0, len(numbers) - 1
        res = None
        while res != target:
        
            res = numbers[left] + numbers[right]

            if res > target:
                # overshot move right back
                right -= 1

            if res < target:
                #undershot move left forward
                left += 1


        ret = [left + 1, right + 1]
        return ret
