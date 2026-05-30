# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def explorer(node, level):
            if not node:
                return
            
            if len(res)-1 < level:
                res.append([])

            res[level].append(node.val)

            explorer(node.left, level+1)
            explorer(node.right, level+1)

        explorer(root, 0)

        return res
        