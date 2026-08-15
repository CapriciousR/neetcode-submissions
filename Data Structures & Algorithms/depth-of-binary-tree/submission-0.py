# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root, currHt):
            if not root:
                return currHt
            lmax = getDepth(root.left, currHt+1)
            rmax = getDepth(root.right, currHt+1)
            return max(lmax, rmax)
        
        return getDepth(root, 0)