import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.MinHeap, self.k = nums, k
        heapq.heapify(self.MinHeap)

        while len(self.MinHeap) > self.k:
            heapq.heappop(self.MinHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.MinHeap, val)

        if len(self.MinHeap) > self.k:
            heapq.heappop(self.MinHeap)
        
        return self.MinHeap[0]
