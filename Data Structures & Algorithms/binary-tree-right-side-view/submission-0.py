# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vista = []

        def explore(node, level):
            if not node:
                return

            if len(vista) == level:
                vista.append(node.val)

            explore(node.right, level+1)
            explore(node.left, level+1)

        explore(root, 0)

        return vista

        