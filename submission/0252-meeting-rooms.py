class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort(key = lambda x: x[0])
    
        # Check for overlapping intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False  # Overlapping intervals found

        return True
