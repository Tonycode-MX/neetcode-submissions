# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def length(head):

            if not head:
                return 0

            leftLength = length(head.left)
            rightLength = length(head.right)

            self.max_diameter = max(self.max_diameter, leftLength + rightLength)

            return 1 + max(leftLength, rightLength)


        length(root)

        return self.max_diameter

        
        