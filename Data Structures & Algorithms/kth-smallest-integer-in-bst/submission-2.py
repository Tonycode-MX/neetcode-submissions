# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.counter = 0
        self.res = None

        def recorrido_inOrder(node):
            if not node or self.res is not None:
                return
                
            recorrido_inOrder(node.left)
            
            self.counter += 1
            if self.counter == k:
                self.res = node.val
            
            recorrido_inOrder(node.right)

        recorrido_inOrder(root)

        return self.res
        