class Solution:
    import math
    from collections import defaultdict
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # freq = defaultdict(int)

        # for i, num in enumerate(nums):
        #     freq[num] += 1

        # heap = []

        # for num, count in freq.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (count, num))

        #     else:
        #         if count > heap[0][0]: # if it is larger than the smallest one:
        #             heapq.heappushpop(heap, (count, num))

        # return [x[1] for x in heap]

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        ret = []
        for i in reversed(range(len(buckets))):
            ret.extend(buckets[i])
            if len(ret) >= k:
                break

        return ret
            


