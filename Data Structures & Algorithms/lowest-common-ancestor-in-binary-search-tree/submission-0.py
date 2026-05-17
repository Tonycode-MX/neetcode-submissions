# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        elif p.val <= root.val >= q.val:
            left = root.left
            return self.lowestCommonAncestor(left, p,q)

        else:
            right = root.right
            return self.lowestCommonAncestor(right,p,q)
        