# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = 0
        def length(node):

            if not node:
                return 0

            leftLength = length(node.left)
            rightLength = length(node.right)

            self.balance = max(self.balance, abs(rightLength - leftLength))

            return 1 + max(leftLength, rightLength)

        length(root)

        if self.balance > 1:
            return False

        return True
        