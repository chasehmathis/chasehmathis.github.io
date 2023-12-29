class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxx = 0
        stack = [] # tuple (start_idx, height)

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                maxx = max(maxx, h * (i - idx))
                start = idx
            stack.append((start, height))
        
        n = len(heights)
        for i, h in stack:
            width = n - i
            maxx = max(width * h, maxx)

        return maxx
