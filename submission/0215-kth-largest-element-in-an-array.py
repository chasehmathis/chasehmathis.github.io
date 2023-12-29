class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        first_k = nums[:k]
        heapq.heapify(first_k) # O(k)

        for num in nums[k:]:
            smallest = first_k[0]
            if num > smallest:
                heapq.heappop(first_k)
                heapq.heappush(first_k, num)

        return first_k[0]
