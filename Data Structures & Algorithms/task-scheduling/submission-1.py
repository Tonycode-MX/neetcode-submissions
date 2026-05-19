import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        q = []

        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt != 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.pop(0)[0])


        return time
        