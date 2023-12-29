class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        import heapq
        from collections import defaultdict
        freq = defaultdict(int)
        for task in tasks: # O(n)
            freq[task] += 1

        task_heap = [] # (count, task)

        # initialize the heap. 
        # m is num of unique tasks
        for k,v in freq.items():
            heapq.heappush(task_heap, (-v, k)) # O(m) at most n << n


        time = 0
        cool_down = collections.deque()
        while task_heap or cool_down:
            time += 1
            if cool_down and time - cool_down[0][0] > n:
                _, task = cool_down.popleft()
                heapq.heappush(task_heap, (-freq[task], task))

            if task_heap:
                count, task = heapq.heappop(task_heap)
                freq[task] -= 1

                if freq[task] > 0:
                    cool_down.append((time, task))

        return time
