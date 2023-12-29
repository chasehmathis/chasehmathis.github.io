class Solution:
    def maxArea(self, height: List[int]) -> int:

        # two pointer

        max_area = 0
        a_pointer = 0
        b_pointer = len(height) - 1 # the last one

        while (a_pointer < b_pointer):
            if height[a_pointer] == height[b_pointer]:
                proposed_area = height[a_pointer] * (b_pointer - a_pointer)
            if height[a_pointer] < height[b_pointer]:
                proposed_area = height[a_pointer] * (b_pointer - a_pointer)
                max_area = max(max_area, proposed_area)
                a_pointer += 1
            else:
                proposed_area = height[b_pointer] * (b_pointer - a_pointer)
                max_area = max(max_area, proposed_area)
                b_pointer -= 1

        return max_area


