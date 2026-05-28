# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validar(root, downLimit, upLimit):
            if not root:
                return True

            if not (downLimit < root.val < upLimit):
                return False

            return validar(root.left, downLimit, root.val) and validar(root.right, root.val, upLimit)

        return validar(root, float('-inf'), float('inf'))
        