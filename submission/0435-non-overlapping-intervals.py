class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])

        num_to_remove = 0
        last = None
        print(intervals)
        for i in intervals:

            if not last:
                last = i
            else:
                if i[0] < last[1]:
                    num_to_remove += 1
                else:
                    last = i

        return num_to_remove
            
