class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        import heapq
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            last_end = res[-1][1]
            
            if start <= last_end:
                if end > last_end:
                    res[-1][1] = end
            else:
                res.append([start, end])

        return res
