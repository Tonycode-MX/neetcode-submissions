import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist_idx = []

        for i, pair in enumerate(points):
            distance = math.sqrt((pair[0])**2 + (pair[1])**2)
            dist_idx.append([distance, i])

        heapq.heapify(dist_idx)

        while len(res)<k:
            lower_dist = heapq.heappop(dist_idx)
            res.append(points[lower_dist[1]])

        return res

        



        