import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # [2,3,6,2,4] --> [2,2,3,4,6]

        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if -x > -y:
                heapq.heappush(maxHeap, x-y)

        if not maxHeap:
                return 0        
        return -maxHeap[0]


        