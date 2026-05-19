import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = nums

        heapq.heapify(max_heap)

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        k_largest = heapq.heappop(max_heap)

        return k_largest


        