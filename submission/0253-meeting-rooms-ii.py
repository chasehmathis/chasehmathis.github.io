class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # intervals.sort(key = lambda x: x[1])

        # machines = [intervals[0][1]]

        # for i in range(1, len(intervals)):
        #     start_time = intervals[i][0]
            
        #     dist_list = []
        #     for j in range(len(machines)):
        #         if start_time >= machines[j]:
        #             dist_list.append((j, start_time - machines[j]))

            
        #     if len(dist_list) == 0:
        #         machines.append(intervals[i][1])

        #     else:
        #         idx, minn = 0, float('inf')
        #         for k, dist in dist_list:
        #             if dist < minn:
        #                 minn = dist
        #                 idx = k
                
        #         machines[idx] = minn + machines[idx]

        # return len(machines)
        
        import heapq

        intervals.sort(key = lambda x: x[0])

        heap = []

        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                
                heapq.heappushpop(heap, interval[1])
            
            else:
                heapq.heappush(heap, interval[1])

        return len(heap)




    
        
