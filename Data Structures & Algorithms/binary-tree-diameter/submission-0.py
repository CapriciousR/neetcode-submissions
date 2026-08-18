# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def getDepth(root):
            if not root:
                return 0
            nonlocal dia
            left = getDepth(root.left)
            right = getDepth(root.right)

            dia = max(dia, left+right)

            return 1+max(left,right)
        getDepth(root)
        return dia


