# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def validar(node, Limit):
            nonlocal res

            if not node:
                return

            if node.val >= Limit:
                res+= 1

            newLimit = max(Limit, node.val)
            validar(node.left, newLimit)
            validar(node.right, newLimit)

        validar(root,float('-inf'))

        return res

        