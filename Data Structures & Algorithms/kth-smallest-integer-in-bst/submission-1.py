# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sortedTree = []

        def recorrido_inOrder(node):
            if not node:
                return
                
            recorrido_inOrder(node.left)
            
            sortedTree.append(node.val)
            
            recorrido_inOrder(node.right)

        recorrido_inOrder(root)

        return sortedTree[k-1]
        