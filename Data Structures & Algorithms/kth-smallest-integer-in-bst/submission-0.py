# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        heap = []

        heapq.heapify(heap)

        heapq.heappush(heap, -(root.val))

        def heapInsert(node):
            nonlocal heap

            if node:
                if node.left:
                    heapq.heappush(heap, -(node.left.val))
                    heapInsert(node.left)
                if node.right:
                    heapq.heappush(heap, -(node.right.val))
                    heapInsert(node.right)

        heapInsert(root)

        while len(heap) > k:
            heapq.heappop(heap)

        return -(heapq.heappop(heap))


        